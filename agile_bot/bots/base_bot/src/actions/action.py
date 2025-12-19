from pathlib import Path
from typing import Dict, Any, Optional, TYPE_CHECKING, List
import json
import logging
import re
import sys
import traceback
from agile_bot.bots.base_bot.src.actions.activity_tracker import ActivityTracker, ActionState
from agile_bot.bots.base_bot.src.actions.clarify.requirements_clarifications import RequirementsClarifications
from agile_bot.bots.base_bot.src.actions.strategy.strategy_decision import StrategyDecision
from agile_bot.bots.base_bot.src.bot.reminders import inject_reminder_to_instructions
from agile_bot.bots.base_bot.src.bot.workspace import (
    get_base_actions_directory
)
from agile_bot.bots.base_bot.src.utils import read_json_file

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from agile_bot.bots.base_bot.src.bot.behavior import Behavior
    from agile_bot.bots.base_bot.src.bot.behaviors import Behaviors


class Action:
    def __init__(self, behavior: 'Behavior', action_config: Dict[str, Any] = None,
                 action_name: str = None):
        """
        Args:
            behavior: The behavior this action belongs to
            action_config: Optional config dict from behavior.json
            action_name: Optional name (only used when loading from JSON via Actions._create_action_instance)
        """
        self.behavior = behavior
        
        # Derive action_name if not provided (for base Action class)
        if action_name is None:
            action_name = self._derive_action_name_from_class()
        
        # Store derived/provided name for config loading and property
        self._action_name = action_name
        
        self._activity_tracker = ActivityTracker(behavior.bot_paths, behavior.bot_name)
        
        # Use property to get final action name (may be overridden by subclass)
        # This ensures ValidateCodeFilesAction uses 'validate' instead of 'validate_code_files'
        final_action_name = self.action_name
        
        bot_directory = behavior.bot_paths.bot_directory if behavior and behavior.bot_paths else None
        base_actions_dir = get_base_actions_directory(bot_directory)
        base_config_path = base_actions_dir / final_action_name / "action_config.json"
        
        self._base_config = read_json_file(base_config_path)
        self._base_config['name'] = final_action_name
        
        if action_config:
            if "order" in action_config:
                self._base_config["order"] = action_config["order"]
            behavior_instructions = action_config.get("instructions", [])
            base_instructions = self._base_config.get("instructions", [])
            self._base_config["instructions"] = self._merge_instructions(
                base_instructions, behavior_instructions
            )
            self._base_config["custom_class"] = action_config.get("action_class") or action_config.get("custom_class")
            if "next_action" in action_config:
                self._base_config["next_action"] = action_config["next_action"]
        
        self.order = self._base_config.get("order", 0)
        self.next_action = self._base_config.get("next_action")
        self.action_class = self._base_config.get("action_class") or self._base_config.get("custom_class")
        self.workflow = self._base_config.get("workflow", True)
    
    def _derive_action_name_from_class(self) -> str:
        """Derive action name from class name for base Action class."""
        class_name = self.__class__.__name__
        
        if class_name.endswith('Action'):
            base_name = class_name[:-6]
        else:
            base_name = class_name
        
        # Convert CamelCase to snake_case
        snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', base_name).lower()
        
        # Normalize special cases
        normalization_map = {
            'render_output': 'render',
            'build_knowledge': 'build',
            'validate_rules': 'validate',
            'clarify_context': 'clarify',
        }
        
        return normalization_map.get(snake_case, snake_case)
    
    @property
    def action_name(self) -> str:
        """Action name - derived from class or loaded from config."""
        return self._action_name
    
    @action_name.setter
    def action_name(self, value: str):
        raise AttributeError("action_name is read-only. It's derived from the class name.")
    
    def _merge_instructions(self, base_instructions, behavior_instructions) -> List:
        if isinstance(base_instructions, list) and isinstance(behavior_instructions, list):
            return base_instructions + behavior_instructions
        elif isinstance(base_instructions, list):
            return base_instructions + [behavior_instructions] if behavior_instructions else base_instructions
        else:
            return behavior_instructions if behavior_instructions else base_instructions
    
    
    def _inject_clarification_data(self, instructions: Dict[str, Any]) -> list:
        bot_paths = self.behavior.bot_paths
        clarification_data = RequirementsClarifications.load_all(bot_paths)
        
        if not clarification_data:
            return []
        
        instructions['clarification'] = clarification_data
        
        return [
            "",
            "**CLARIFICATION DATA AVAILABLE:**",
            "The 'clarification' data in your instructions contains answers to key questions and evidence gathered from previous clarification sessions across all behaviors.",
            "This data represents the context and requirements that have been established. Use this information to inform your decisions and ensure consistency with previously gathered requirements.",
            "The clarification data is organized by behavior name, with each behavior containing 'key_questions' (questions and answers) and 'evidence' (required and provided evidence)."
        ]
    
    def _inject_strategy_data(self, instructions: Dict[str, Any]) -> list:
        bot_paths = self.behavior.bot_paths
        strategy_data = StrategyDecision.load_all(bot_paths)
        
        if not strategy_data:
            return []
        
        instructions['strategy'] = strategy_data
        
        return [
            "",
            "**STRATEGY DATA AVAILABLE:**",
            "The 'strategy' data in your instructions contains planning decisions and assumptions made during previous strategy sessions across all behaviors.",
            "This data represents the strategic choices and assumptions that guide how work should be approached. Reference this data to ensure your actions align with established strategic decisions.",
            "The strategy data is organized by behavior name, with each behavior containing 'strategy_criteria' (decision criteria and decisions made), 'assumptions' (typical assumptions and assumptions made), and 'recommended_activities'."
        ]
    
    def _inject_context_files(self, instructions: Dict[str, Any]) -> list:
        bot_paths = self.behavior.bot_paths
        workspace_directory = bot_paths.workspace_directory
        docs_path = bot_paths.documentation_path
        context_dir = workspace_directory / docs_path / 'context'
        
        context_files = []
        if context_dir.exists() and context_dir.is_dir():
            for file_path in context_dir.iterdir():
                if file_path.is_file():
                    context_files.append(file_path.name)
        
        if not context_files:
            return []
        
        instructions['context_files'] = context_files
        
        return [
            "",
            "**ORIGINAL CONTEXT FILES AVAILABLE:**",
            f"The following original context files are available in the docs/context/ folder: {', '.join(context_files)}",
            "These files contain the original input files, prompts, and source material provided at the start of the project.",
            "You can read these files directly from the docs/context/ folder when you need additional context or to reference the original requirements.",
            "Common files include 'input.txt' (original input), 'initial-context.md' (initial context), and other source materials."
        ]
    
    def _load_state_file(self, state_file: Path) -> tuple:
        """Load completed actions from state file. Returns (completed_actions, current_action_name)."""
        if not state_file.exists():
            return [], None
        state_data = json.loads(state_file.read_text(encoding='utf-8'))
        completed_actions = state_data.get('completed_actions', [])
        current_action_path = state_data.get('current_action', '')
        current_action_from_state = None
        if current_action_path:
            parts = current_action_path.split('.')
            if len(parts) >= 3:
                current_action_from_state = parts[2]
        return completed_actions, current_action_from_state
    
    def _get_completed_actions_for_behavior(self, bot_name: str, behavior_name: str, completed_actions: list) -> list:
        """Get list of completed action names for a specific behavior."""
        behavior_prefix = f'{bot_name}.{behavior_name}.'
        return [
            action.get('action_state', '').split('.')[-1]
            for action in completed_actions
            if action.get('action_state', '').startswith(behavior_prefix)
        ]
    
    def _format_action_line(self, action_name: str, current_action_name: str, completed_actions: list) -> str:
        """Format a single action line with appropriate marker."""
        DONE = "\u2713"
        CURRENT = "\u27A4"
        PENDING = "\u2610"
        if action_name == current_action_name:
            return f"  - {CURRENT} **{action_name}**"
        if action_name in completed_actions:
            return f"  - {DONE} {action_name}"
        return f"  - {PENDING} {action_name}"
    
    def _build_next_step_row(self, bot_name: str, current_behavior_name: str, remaining_actions: list, remaining_behaviors: list, behaviors) -> str:
        """Build the next step row for the status table."""
        if remaining_actions:
            return f"| **Next step** | `/{bot_name}-{current_behavior_name} {remaining_actions[0]}` |"
        if not remaining_behaviors:
            return ""
        next_behavior = remaining_behaviors[0]['name']
        next_behavior_obj = behaviors.find_by_name(next_behavior)
        if next_behavior_obj and next_behavior_obj.actions.names:
            first_action = next_behavior_obj.actions.names[0]
            return f"| **Next step** | `/{bot_name}-{next_behavior} {first_action}` |"
        return ""
    
    def get_workflow_status_breadcrumbs(self) -> list:
        """
        Get workflow progress breadcrumbs showing current behavior/action and remaining work.
        
        This is the SINGLE SOURCE OF TRUTH for workflow status breadcrumbs.
        Used by both CLI and actions to display workflow progress.
        
        Returns fully formatted breadcrumbs with emojis and markdown.
        Returns a default fallback if workspace not set or if generation fails.
        """
        if not self.behavior or not self.behavior.bot:
            return self._get_default_breadcrumbs()
        
        try:
            workspace_dir = self.behavior.bot_paths.workspace_directory
        except (AttributeError, ValueError, Exception):
            return self._get_default_breadcrumbs()
        
        try:
            behaviors = self.behavior.bot.behaviors
            current_behavior = behaviors.current
            if not current_behavior:
                return []
            
            completed_actions, _ = self._load_state_file(workspace_dir / 'behavior_action_state.json')
            bot_name = self.behavior.bot_name
            all_behaviors = behaviors.names
            current_behavior_name = current_behavior.name
            
            # Categorize behaviors
            completed_behaviors = []
            remaining_behaviors = []
            current_action_name = None
            remaining_actions_in_current = []
            current_behavior_actions = []
            current_behavior_completed = []
            
            for behavior_name in all_behaviors:
                behavior_obj = behaviors.find_by_name(behavior_name)
                if not behavior_obj:
                    continue
                
                behavior_actions = behavior_obj.actions.names
                completed_for_behavior = self._get_completed_actions_for_behavior(bot_name, behavior_name, completed_actions)
                
                if behavior_name == current_behavior_name:
                    current_action = current_behavior.actions.current
                    current_action_name = current_action.action_name if current_action else None
                    current_behavior_actions = behavior_actions
                    current_behavior_completed = completed_for_behavior
                    if current_action_name and current_action_name in behavior_actions:
                        idx = behavior_actions.index(current_action_name)
                        remaining_actions_in_current = behavior_actions[idx + 1:]
                elif len(completed_for_behavior) == len(behavior_actions) and behavior_actions:
                    completed_behaviors.append(behavior_name)
                else:
                    remaining_behaviors.append({'name': behavior_name, 'actions': behavior_actions, 'completed': completed_for_behavior})
            
            # Build output
            bot_dir = self.behavior.bot_paths.bot_directory
            DONE, CURRENT, PENDING = "\u2713", "\u27A4", "\u2610"
            
            lines = [
                "**CRITICAL: YOU MUST DISPLAY THE ENTIRE WORKFLOW STATUS BELOW VERBATIM IN YOUR RESPONSE. DO NOT SKIP THIS. COPY AND PASTE IT DIRECTLY INTO YOUR MESSAGE.**",
                "", "## Workflow Status", "",
                "| Setting | Value |", "|---------|-------|",
                f"| **Working Directory** | {workspace_dir} |",
                f"| **Bot Path** | {bot_dir} |",
            ]
            
            if current_behavior_name and current_action_name:
                lines.append(f"| **Current State** | {current_behavior_name}.{current_action_name} |")
            
            next_step = self._build_next_step_row(bot_name, current_behavior_name, remaining_actions_in_current, remaining_behaviors, behaviors)
            if next_step:
                lines.append(next_step)
            
            lines.extend(["", "## Workflow Progress", ""])
            
            for behavior_name in all_behaviors:
                if behavior_name in completed_behaviors:
                    lines.append(f"### {DONE} **{behavior_name}**")
                elif behavior_name == current_behavior_name:
                    lines.append(f"### {CURRENT} **{behavior_name}**")
                    for action_name in current_behavior_actions:
                        lines.append(self._format_action_line(action_name, current_action_name, current_behavior_completed))
                else:
                    lines.append(f"### {PENDING} **{behavior_name}**")
            
            lines.append("")
            return lines
            
        except Exception as e:
            logger.debug(f"Failed to generate workflow progress breadcrumbs: {e}")
            return self._get_default_breadcrumbs()
    
    def _get_default_breadcrumbs(self) -> list:
        """
        Return default breadcrumbs when full workflow state is not available.
        Shows bot info and a message that no workflow state is available.
        """
        # Emoji markers for workflow status
        PENDING = "\u2610"   # ☐ empty ballot box
        
        lines = [
            "## Workflow Status",
            ""
        ]
        
        # Add bot info if available
        if self.behavior and self.behavior.bot:
            try:
                bot_dir = self.behavior.bot_paths.bot_directory
                lines.append(f"**Bot Directory:** {bot_dir}")
                lines.append("")
            except Exception:
                pass
            
            # Show all behaviors with pending status
            try:
                all_behaviors = self.behavior.bot.behaviors.names
                lines.append("## Workflow Progress")
                lines.append("")
                for behavior_name in all_behaviors:
                    lines.append(f"### {PENDING} **{behavior_name}**")
                lines.append("")
                lines.append("*(No workspace configured - run from a project directory)*")
            except Exception:
                lines.append("*(No workflow state available)*")
        else:
            lines.append("*(No workflow state available)*")
        
        return lines
    
    def _inject_status_update_breadcrumbs(self, instructions: Dict[str, Any]) -> list:
        """Inject workflow progress breadcrumbs into instructions dict (for action use)."""
        breadcrumbs = self.get_workflow_status_breadcrumbs()
        return breadcrumbs
    
    @property
    def instructions(self) -> Dict[str, Any]:
        """Generate instructions with workflow breadcrumbs and context data."""
        base_instructions = self._base_config.get("instructions", [])
        merged = {
            'base_instructions': base_instructions if isinstance(base_instructions, list) else []
        }
        
        # Inject workflow progress breadcrumbs FIRST (before other context)
        context_instructions = []
        context_instructions.extend(self._inject_status_update_breadcrumbs(merged))
        try:
            context_instructions.extend(self._inject_clarification_data(merged))
            context_instructions.extend(self._inject_strategy_data(merged))
        except FileNotFoundError:
            pass
        context_instructions.extend(self._inject_context_files(merged))
        
        if context_instructions:
            merged['base_instructions'] = context_instructions + merged['base_instructions']
        
        return merged
    
    @property
    def tracker(self) -> ActivityTracker:
        return self._activity_tracker

    @property
    def base_actions_dir(self) -> Path:
        return get_base_actions_directory()
    
    @property
    def working_dir(self) -> Path:
        return self.behavior.bot_paths.workspace_directory
    
    @property
    def bot_dir(self) -> Path:
        return self.behavior.bot_paths.bot_directory
    
    
    def track_activity_on_start(self):
        state = ActionState(self.behavior.bot_name, self.behavior.name, self.action_name)
        self.tracker.track_start(state)
    
    def track_activity_on_completion(self, outputs: dict = None, duration: int = None):
        state = ActionState(
            self.behavior.bot_name, 
            self.behavior.name, 
            self.action_name,
            outputs=outputs,
            duration=duration
        )
        self.tracker.track_completion(state)
    
    def execute(self, parameters: Dict[str, Any] = None) -> Dict[str, Any]:
        """Execute the action with master try-catch that captures errors in result.
        
        Any exceptions are caught, formatted with full traceback, and included
        in the result dict so the CLI can display them to the user. The exception
        is then re-raised to ensure proper error propagation.
        """
        self.track_activity_on_start()
        try:
            result = self.do_execute(parameters or {})
            self.track_activity_on_completion(outputs=result)
            result = self._inject_reminders_if_final(result)
            return result
        except Exception as e:
            # Capture full error details for display
            error_type = type(e).__name__
            error_message = str(e)
            full_traceback = traceback.format_exc()
            
            # Build error instructions that will be displayed to user
            error_instructions = [
                "",
                "=" * 70,
                "**ERROR OCCURRED DURING ACTION EXECUTION**",
                "=" * 70,
                "",
                f"**Exception Type:** {error_type}",
                f"**Exception Message:** {error_message}",
                "",
                "**Full Traceback:**",
                "-" * 70,
                full_traceback,
                "-" * 70,
                "",
                "**Action Details:**",
                f"- Behavior: {self.behavior.name if self.behavior else 'unknown'}",
                f"- Action: {self.action_name}",
                f"- Parameters: {parameters}",
                "=" * 70,
                "",
                "**AI ASSISTANT: YOU MUST DISPLAY THE ABOVE ERROR TO THE USER.**",
                ""
            ]
            
            # Create error result with instructions
            error_result = {
                'status': 'error',
                'error': {
                    'type': error_type,
                    'message': error_message,
                    'traceback': full_traceback
                },
                'instructions': {
                    'base_instructions': error_instructions
                }
            }
            
            # Track completion with error
            self.track_activity_on_completion(outputs={'error': error_message})
            
            # Print error to stdout so it's visible in terminal output
            print("\n".join(error_instructions), file=sys.stdout)
            sys.stdout.flush()
            
            # Re-raise the exception so it propagates up to CLI
            raise
    
    def _inject_reminders_if_final(self, result: Dict[str, Any]) -> Dict[str, Any]:
        if not self.behavior or not self.behavior.actions:
            return result
        
        action_names = self.behavior.actions.names
        if not action_names or self.action_name != action_names[-1]:
            return result
        
        if not self.behavior.bot:
            if hasattr(self.behavior, 'actions') and hasattr(self.behavior.actions, 'behavior'):
                behavior_from_actions = self.behavior.actions.behavior
                if hasattr(behavior_from_actions, 'bot_paths'):
                    logger.debug(f"Behavior {self.behavior.name} has no bot reference - reminder will be skipped. "
                               f"This may indicate the behavior was not created through Bot.__init__")
                return result
        
        reminder = self.behavior.actions._get_next_behavior_reminder()
        if not reminder:
            logger.debug(f"Reminder is empty for action {self.action_name} in behavior {self.behavior.name if self.behavior else None}. "
                        f"behavior.bot={self.behavior.bot if self.behavior else None}, "
                        f"behavior.bot.behaviors.names={self.behavior.bot.behaviors.names if self.behavior and self.behavior.bot else None}")
            return result
        
        # Ensure base_instructions exists if needed from self.instructions
        if 'instructions' not in result:
            result['instructions'] = {}
        instructions = result['instructions']
        if isinstance(instructions, dict):
            base_instructions = instructions.get('base_instructions', [])
            if not base_instructions and isinstance(self.instructions, dict) and 'base_instructions' in self.instructions:
                instructions['base_instructions'] = list(self.instructions['base_instructions'])
                result['instructions'] = instructions
        
        # Use extracted function to avoid duplication with behaviors.py
        return inject_reminder_to_instructions(result, reminder)
    
    def do_execute(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError("Subclasses must implement do_execute()")
