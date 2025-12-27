from __future__ import annotations
from typing import TYPE_CHECKING, Dict, Any
import json
from agile_bot.bots.base_bot.src.repl_cli.cli_scope import CLIScope

if TYPE_CHECKING:
    from agile_bot.bots.base_bot.src.actions.action import Action
    from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession


class CLIAction:
    
    def __init__(self, action: Action, session: REPLSession):
        self._action = action
        self._session = session
    
    @property
    def name(self) -> str:
        return self._action.action_name
    
    @property
    def description(self) -> str:
        return self._action.description
    
    @property
    def status(self) -> str:
        if hasattr(self._action, 'is_completed') and self._action.is_completed:
            return "completed"
        return "pending"
    
    def instructions(self, args: str = "") -> str:
        try:
            context = self._parse_args_to_context(args)
            result = self._action.get_instructions(context)
            formatted = self._format_result(result)
            
            # Prepend scope display if scope is set (CLI layer adds formatting)
            instructions_obj = self._action.instructions
            if instructions_obj.scope:
                cli_scope = CLIScope(instructions_obj.scope, self._action.behavior.bot_paths.workspace_directory)
                scope_display = cli_scope.to_formatted_display()
                formatted = scope_display + formatted
            
            return formatted
        except Exception as e:
            return f"Error getting instructions: {str(e)}"
    
    def submit(self, args: str) -> str:
        try:
            context = self._parse_args_to_context(args)
            result = self._action.submit(context)
            return self._format_result(result)
        except Exception as e:
            return f"Error submitting: {str(e)}"
    
    def confirm(self) -> str:
        try:
            context = self._action.context_class()
            result = self._action.confirm(context)
            return self._format_result(result)
        except Exception as e:
            return f"Error confirming: {str(e)}"
    
    def _parse_args_to_context(self, args: str):
        context_class = self._action.context_class
        if not args or args.strip() == "":
            return context_class()
        
        try:
            args_dict = json.loads(args)
            return context_class(**args_dict)
        except (json.JSONDecodeError, TypeError):
            return context_class()
    
    def _format_result(self, action_result: Any) -> str:
        if isinstance(action_result, dict):
            # First check for formatted_output (from get_instructions)
            if 'formatted_output' in action_result:
                return action_result['formatted_output']
            # Then check for output (from submit/confirm)
            if 'output' in action_result:
                output = action_result['output']
                if isinstance(output, str):
                    return output
                return json.dumps(output, indent=2)
            return json.dumps(action_result, indent=2)
        if isinstance(action_result, str):
            return action_result
        return str(action_result)
    
    @property
    def domain_action(self) -> Action:
        return self._action

