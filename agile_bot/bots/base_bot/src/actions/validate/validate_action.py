from pathlib import Path
from typing import Dict, Any, List, Optional, TYPE_CHECKING
import logging
import traceback
import json
import threading
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
        
        # Check if validation should run in background
        # Default to True only for code behavior, False for others (can be overridden with background parameter)
        default_background = self.behavior.name == 'code'
        run_in_background = parameters.get('background', default_background)
        
        if run_in_background:
            # Run validation in background thread
            return self._execute_background(parameters)
        else:
            # Run validation synchronously (original behavior)
            return self._execute_synchronous(parameters)
    
    def _execute_background(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Execute validation in a background thread."""
        # Build validation scope early to get file count for status message
        try:
            validation_scope = ValidationScope(parameters or {}, self.behavior.bot_paths, behavior_name=self.behavior.name)
            files = validation_scope.all_files()
            total_files = sum(len(f) for f in files.values())
        except Exception as e:
            logger.warning(f"Could not pre-compute file count: {e}")
            total_files = 0
        
        # Get status file path for user message
        status_path = self.behavior.bot_paths.workspace_directory / 'agile_bot' / 'bots' / self.behavior.bot_name / 'docs' / 'stories' / 'code-validation-status.md'
        
        # Start background thread
        def run_validation():
            try:
                # Note: Activity tracking start is handled by execute() method
                # We need to track completion here when background thread finishes
                result = self._execute_synchronous(parameters)
                # Track completion in background thread
                self.track_activity_on_completion(outputs=result)
                logger.info("Background validation completed successfully")
            except Exception as e:
                error_msg = str(e)
                # Track completion with error
                self.track_activity_on_completion(outputs={'error': error_msg})
                logger.error(f"Background validation failed: {e}")
                import traceback
                traceback.print_exc()
                # Update status file with error
                try:
                    status_path.parent.mkdir(parents=True, exist_ok=True)
                    with open(status_path, 'a', encoding='utf-8') as f:
                        f.write(f"\n\n## ERROR\n\nValidation failed with error: {e}\n")
                except Exception as status_err:
                    logger.error(f"Could not write error to status file: {status_err}")
        
        # Use daemon=False so the thread continues even if CLI returns
        # The thread will complete the validation and update the status file
        validation_thread = threading.Thread(target=run_validation, daemon=False, name="ValidationThread")
        validation_thread.start()
        
        # Return immediately with status message
        status_path_relative = status_path.relative_to(self.behavior.bot_paths.workspace_directory)
        
        return {
            'instructions': {
                'base_instructions': [
                    "",
                    "=" * 70,
                    "**VALIDATION RUNNING IN BACKGROUND**",
                    "=" * 70,
                    "",
                    "**CRITICAL: YOU MUST POLL THE STATUS FILE EVERY 10 SECONDS UNTIL VALIDATION COMPLETES**",
                    "",
                    f"Validation has been started in the background. It will scan {total_files} file(s).",
                    "",
                    "**Status File:**",
                    f"  {status_path_relative}",
                    "",
                    "**AI ASSISTANT DIRECTIVES:**",
                    "1. YOU MUST read the status file every 10 seconds to check progress",
                    "2. YOU MUST report the current status summary to the user each time you check",
                    "3. Continue polling every 10 seconds until validation is complete",
                    "4. When complete, YOU MUST read and report the final summary from the status file",
                    "5. Also check the full report at: docs/stories/code-validation-report.md",
                    "",
                    "The validation is running asynchronously and will update the status file in real-time.",
                    "The status file shows progress as scanners complete their work.",
                    "",
                    "**Status File Location:**",
                    f"  {status_path_relative}",
                    "",
                    "**Report File Location (when complete):**",
                    "  docs/stories/code-validation-report.md",
                    "",
                    "=" * 70,
                    ""
                ]
            },
            '_background_execution': True,  # Flag to tell execute() not to track completion immediately
            'background': True,
            'status_file': str(status_path_relative),
            'total_files': total_files
        }
    
    def _execute_synchronous(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Execute validation synchronously (original implementation)."""
        try:
            # Create validation context - it builds everything internally
            from agile_bot.bots.base_bot.src.actions.validate.rules import ValidationContext
            validation_context = ValidationContext.from_parameters(
                behavior=self.behavior,
                parameters=parameters
            )
            
            logger.info(f"Files to validate: {sum(len(f) for f in validation_context.files.values())} files")
            
            # Use streaming writer for real-time feedback
            streaming_writer = StreamingValidationReportWriter(self.behavior.name, self.behavior.bot_paths)
            streaming_writer.start(validation_context.files)
            
            # Update context with streaming callbacks
            from agile_bot.bots.base_bot.src.actions.validate.rules import ValidationCallbacks
            validation_context.callbacks = ValidationCallbacks(
                on_scanner_start=streaming_writer.on_scanner_start,
                on_scanner_complete=streaming_writer.on_scanner_complete,
                on_file_scanned=streaming_writer.on_file_scanned
            )
            
            logger.info("Injecting validation instructions...")
            result = self.injectValidationInstructions(validation_context, streaming_writer)
            instructions = result.get('instructions', {})
            validation_rules = instructions.get('validation_rules', [])
            
            # Finish the streaming report with summary
            streaming_writer.finish(instructions, validation_rules)
            
            # Also write the full detailed report (for complete formatting)
            writer = ValidationReportWriter(self.behavior.name, self.behavior.bot_paths)
            writer.write(instructions, validation_rules, validation_context.files)
            return result
        except Exception as e:
            logger.error(f"Error in synchronous validation: {e}")
            logger.error(f"Error type: {type(e).__name__}")
            logger.error(f"Parameters: {parameters}")
            logger.error(f"Full traceback:\n{traceback.format_exc()}")
            # Re-raise the exception - don't wrap it, let it propagate
            raise
    
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
    
    def injectValidationInstructions(self, validation_context: 'ValidationContext',
                                      streaming_writer: Optional['StreamingValidationReportWriter'] = None) -> Dict[str, Any]:
        """Inject validation instructions into action instructions."""
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
        
        # Validate using context - context already has all parameters
        processed_rules = self.rules.validate(validation_context)
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
