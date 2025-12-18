from pathlib import Path
from typing import Dict, Any, List, Optional, TYPE_CHECKING
import logging
import traceback
import json
from agile_bot.bots.base_bot.src.utils import read_json_file
from agile_bot.bots.base_bot.src.actions.action import Action
from agile_bot.bots.base_bot.src.actions.build.knowledge import Knowledge
from agile_bot.bots.base_bot.src.actions.validate.scanners.violation import Violation
from agile_bot.bots.base_bot.src.actions.validate.rule import Rule
from agile_bot.bots.base_bot.src.actions.validate.rules import Rules
from agile_bot.bots.base_bot.src.actions.validate.scanners.scanner_loader import ScannerLoader
from agile_bot.bots.base_bot.src.actions.validate.story_graph import StoryGraph
from agile_bot.bots.base_bot.src.actions.validate.validation_scope import ValidationScope
from agile_bot.bots.base_bot.src.actions.validate.validation_report_writer import ValidationReportWriter, StreamingValidationReportWriter

if TYPE_CHECKING:
    pass

logger = logging.getLogger(__name__)


class ScannerExecutionError(Exception):
    def __init__(self, rule_file: str, scanner_path: str, original_error: Exception):
        self.rule_file = rule_file
        self.scanner_path = scanner_path
        self.original_error = original_error
        message = (
            f"Scanner execution failed for rule '{rule_file}' "
            f"(scanner: {scanner_path}): {original_error}"
        )
        super().__init__(message)


class ValidateRulesAction(Action):
    def __init__(self, behavior=None, action_config=None):
        super().__init__(behavior=behavior, action_config=action_config)
        self._rules = Rules(behavior=self.behavior, bot_paths=self.behavior.bot_paths)
    
    @property
    def action_name(self) -> str:
        """Action name is always 'validate' for ValidateRulesAction."""
        return 'validate'
    
    @action_name.setter
    def action_name(self, value: str):
        raise AttributeError("action_name is read-only for ValidateRulesAction")
    
    @property
    def rules(self) -> Rules:
        return self._rules
    
    def do_execute(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        logger.info("=== Starting validation ===")
        logger.info(f"Behavior: {self.behavior.name}")
        logger.info(f"Parameters: {parameters}")
        try:
            # Get knowledge graph spec so StoryGraph can read config internally
            logger.info("Loading knowledge graph...")
            knowledge = Knowledge(self.behavior)
            
            logger.info("Creating story graph...")
            story_graph = StoryGraph(
                self.behavior.bot_paths, 
                self.working_dir,
                knowledge_graph_spec=knowledge.knowledge_graph_spec
            )
            logger.info("Building validation scope...")
            validation_scope = ValidationScope(parameters or {}, self.behavior.bot_paths, behavior_name=self.behavior.name)
            scope_config = validation_scope.scope
            scope_keys = {'story_names', 'increment_priorities', 'epic_names', 'all'}
            has_scope_in_params = any(key in scope_config for key in scope_keys)
            
            if has_scope_in_params:
                story_graph['_validation_scope'] = scope_config
            
            logger.info("Discovering files to validate...")
            files = validation_scope.all_files()
            logger.info(f"Found {sum(len(f) for f in files.values())} files to validate")
            
            # Use streaming writer for real-time feedback
            streaming_writer = StreamingValidationReportWriter(self.behavior.name, self.behavior.bot_paths)
            streaming_writer.start(files)
            
            logger.info("Injecting validation instructions...")
            skiprule = parameters.get('skiprule', [])
            result = self.injectValidationInstructions(
                story_graph.content, 
                files=files,
                streaming_writer=streaming_writer,
                skiprule=skiprule
            )
            instructions = result.get('instructions', {})
            validation_rules = instructions.get('validation_rules', [])
            
            # Finish the streaming report with summary
            streaming_writer.finish(instructions, validation_rules)
            
            # Also write the full detailed report (for complete formatting)
            writer = ValidationReportWriter(self.behavior.name, self.behavior.bot_paths)
            writer.write(instructions, validation_rules, files)
            return result
        except FileNotFoundError as e:
            if "story graph" in str(e).lower() or "story-graph.json" in str(e):
                raise
            logger.error("=== ERROR in validate action ===")
            logger.error(f"Error type: {type(e).__name__}")
            logger.error(f"Error message: {e}")
            logger.error(f"Parameters: {parameters}")
            logger.error(f"Full traceback:\n{traceback.format_exc()}")
            error_msg = (
                f"Error in validate action: {e}\n"
                f"Parameters: {parameters}\n"
                f"Traceback:\n{traceback.format_exc()}"
            )
            raise RuntimeError(error_msg) from e
        except (json.JSONDecodeError, ValueError) as e:
            raise
        except Exception as e:
            logger.error("=== ERROR in validate action ===")
            logger.error(f"Error type: {type(e).__name__}")
            logger.error(f"Error message: {e}")
            logger.error(f"Parameters: {parameters}")
            logger.error(f"Full traceback:\n{traceback.format_exc()}")
            error_msg = (
                f"Error in validate action: {e}\n"
                f"Parameters: {parameters}\n"
                f"Traceback:\n{traceback.format_exc()}"
            )
            raise RuntimeError(error_msg) from e
    
    def inject_common_bot_rules(self) -> Dict[str, Any]:
        base_bot_rules_dir = self.bot_dir.parent / 'base_bot' / 'rules'
        common_rules = []
        for rule_file in base_bot_rules_dir.glob('*.json'):
            rule_data = read_json_file(rule_file)
            common_rules.append({
                'rule_file': f'agile_bot/bots/base_bot/rules/{rule_file.name}',
                'rule_content': rule_data
            })
        return {
            'validation_rules': common_rules
        }
    
    def inject_behavior_specific_and_bot_rules(self) -> Dict[str, Any]:
        all_rules = []
        bot_dir = self.behavior.bot_paths.bot_directory
        bot_rules_dir = bot_dir / 'rules'
        for rule_file in bot_rules_dir.glob('*.json'):
            rule_data = read_json_file(rule_file)
            all_rules.append({
                'rule_file': f'{bot_dir.name}/rules/{rule_file.name}',
                'rule_content': rule_data
            })
        behavior_rules_dir = bot_dir / 'behaviors' / self.behavior.name / 'rules'
        for rule_file in behavior_rules_dir.glob('*.json'):
            rule_data = read_json_file(rule_file)
            all_rules.append({
                'rule_file': f'{bot_dir.name}/behaviors/{self.behavior.name}/rules/{rule_file.name}',
                'rule_content': rule_data
            })
        common_rules_data = self.inject_common_bot_rules()
        all_rules.extend(common_rules_data.get('validation_rules', []))
        return {
            'validation_rules': all_rules
        }
    
    def get_action_instructions(self) -> List[str]:
        action_instructions = []
        base_actions_path = self.base_actions_dir
        config_path = base_actions_path / 'validate' / 'action_config.json'
        config = read_json_file(config_path)
        action_instructions = config.get('instructions', [])
        return action_instructions
    
    def inject_next_action_instructions(self):
        return ""
    
    def injectValidationInstructions(self, knowledge_graph: Dict[str, Any], files: Optional[Dict[str, List[Path]]] = None, 
                                      streaming_writer: Optional['StreamingValidationReportWriter'] = None,
                                      skiprule: Optional[List[str]] = None) -> Dict[str, Any]:
        action_instructions = self.get_action_instructions()
        writer = ValidationReportWriter(self.behavior.name, self.behavior.bot_paths)
        report_path = writer.get_report_path()
        report_link = writer.get_report_hyperlink()
        
        if not self.rules:
            action_instructions.append(f"\nValidation report: {report_link}")
            return {
                'instructions': {
                    'action': 'validate',
                    'behavior': self.behavior.name,
                    'base_instructions': action_instructions,
                    'validation_rules': [],
                    'content_to_validate': None,
                    'report_path': str(report_path),
                    'report_link': report_link
                }
            }
        
        files = files or {}
        
        # Pass streaming callbacks for real-time reporting
        on_scanner_start = streaming_writer.on_scanner_start if streaming_writer else None
        on_scanner_complete = streaming_writer.on_scanner_complete if streaming_writer else None
        on_file_scanned = streaming_writer.on_file_scanned if streaming_writer else None
        
        processed_rules = self.rules.validate(
            knowledge_graph, 
            files,
            on_scanner_start=on_scanner_start,
            on_scanner_complete=on_scanner_complete,
            on_file_scanned=on_file_scanned,
            skiprule=skiprule
        )
        violation_summary = self.rules.violation_summary
        
        # Extract scanner status for chat output
        scanner_status_lines = []
        executed_count = 0
        load_failed_count = 0
        execution_failed_count = 0
        no_scanner_count = 0
        
        for rule_dict in processed_rules:
            scanner_status = rule_dict.get('scanner_status', {})
            status = scanner_status.get('status', 'UNKNOWN')
            rule_file = rule_dict.get('rule_file', 'unknown')
            
            if status == 'EXECUTED':
                executed_count += 1
            elif status == 'LOAD_FAILED':
                load_failed_count += 1
                scanner_path = scanner_status.get('scanner_path', 'unknown')
                error = scanner_status.get('error', 'Unknown error')
                scanner_status_lines.append(f"[FAILED] {rule_file}: Scanner failed to load - {scanner_path}")
                scanner_status_lines.append(f"  Error: {error}")
            elif status == 'EXECUTION_FAILED':
                execution_failed_count += 1
                scanner_path = scanner_status.get('scanner_path', 'unknown')
                error = scanner_status.get('error', 'Unknown error')
                scanner_status_lines.append(f"[ERROR] {rule_file}: Scanner execution failed - {scanner_path}")
                scanner_status_lines.append(f"  Error: {error}")
            elif status == 'NO_SCANNER':
                no_scanner_count += 1
        
        # Always add scanner status to instructions for visibility
        scanner_status_header = [
            "\n=== SCANNER EXECUTION STATUS ===",
            f"Successfully Executed: {executed_count}",
            f"Load Failed: {load_failed_count}",
            f"Execution Failed: {execution_failed_count}",
            f"No Scanner: {no_scanner_count}",
            ""
        ]
        if scanner_status_lines:
            scanner_status_header.extend(scanner_status_lines)
        else:
            scanner_status_header.append("All scanners executed successfully.")
        scanner_status_header.append("=== END SCANNER STATUS ===\n")
        action_instructions.extend(scanner_status_header)
        
        if violation_summary:
            edit_instructions = [
                "Based on code scanner diagnostics, edit the knowledge graph to fix violations:",
                *violation_summary,
                "Review each violation and update the knowledge graph accordingly."
            ]
            action_instructions.extend(edit_instructions)
        action_instructions.append(f"\nValidation report: {report_link}")
        instructions = {
            'action': 'validate',
            'behavior': self.behavior.name,
            'base_instructions': action_instructions,
            'validation_rules': processed_rules,
            'content_to_validate': None,
            'report_path': str(report_path),
            'report_link': report_link
        }
        return {'instructions': instructions}
    
    def finalize_and_transition(self, next_action: str = None):
        class ActionResult:
            def __init__(self, next_action):
                self.next_action = next_action
        return ActionResult(next_action=next_action)
