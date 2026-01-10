"""
Minimal CLI session - command router that routes to Bot methods and uses adapters for serialization.
"""

import sys
from pathlib import Path
from typing import Any

from agile_bot.src.cli.adapter_factory import AdapterFactory
from agile_bot.src.cli.cli_results import CLICommandResponse


class CLISession:
    """
    Minimal command router - parses commands, routes to Bot, uses adapter for serialization.
    
    Architecture:
    - Parse command -> Route to Bot method -> Get domain object -> Adapter serializes -> Output
    """
    
    def __init__(self, bot, workspace_directory: Path, mode: str = None):
        """
        Initialize CLI session.
        
        Args:
            bot: Bot instance with flattened API
            workspace_directory: Workspace directory path
            mode: Output mode ('tty', 'markdown', 'json'). If None, auto-detects:
                  - 'tty' if stdin is a TTY (interactive terminal)
                  - 'markdown' if stdin is piped (for AI agents)
                  - 'json' can be set explicitly for web views
        """
        self.bot = bot
        self.workspace_directory = Path(workspace_directory)
        self.mode = mode
    
    def execute_command(self, command: str) -> CLICommandResponse:
        """
        Route command to Bot method, return command response.
        
        Command mappings:
        - "status" -> bot itself (serialized via TTYBot)
        - "scope" -> bot.scope -> Scope object (property)
        - "next" -> bot.next() -> NavigationResult object
        - "back" -> bot.back() -> NavigationResult object
        - "help" -> bot.help() -> Help object
        - "exit" -> bot.exit() -> ExitResult object
        - "behavior.action" -> bot.execute('behavior', 'action') -> ActionResult
        
        Args:
            command: Command string from user input
        
        Returns:
            CLICommandResponse with serialized output and metadata
        """
        # Parse command
        verb, args = self._parse_command(command)
        
        # Check for exit command
        cli_terminated = verb == 'exit'
        
        # Track if this command changes navigation state (should auto-display status)
        is_navigation_command = verb in ('next', 'back', 'current', 'scope')
        
        # Special case: "status" just returns the bot itself
        if verb == 'status':
            result = self.bot
        # Route to Bot method using reflection
        elif hasattr(self.bot, verb):
            attr = getattr(self.bot, verb)
            # Check if property or method
            if callable(attr):
                result = attr(args) if args else attr()
            else:
                result = attr  # It's a property (e.g., scope, bot_path)
                
                # Special case: If result is a Behavior object, navigate to it
                from agile_bot.src.behaviors.behavior import Behavior
                is_behavior = isinstance(result, Behavior)
                
                if is_behavior:
                    self.bot.behaviors.navigate_to(result.name)
                    result = self.bot.behaviors.current
                    is_navigation_command = True  # Navigating to behavior = navigation command
        else:
            # Check if it's an action shortcut (route to current behavior's action)
            result = self._handle_action_shortcut(verb, args)
            if result is None:
                # Not an action shortcut, try behavior.action pattern
                try:
                    result = self._route_to_behavior_action(command)
                    is_navigation_command = True  # behavior.action is navigation
                except ValueError:
                    # Not a valid command - return error in appropriate format
                    error_message = f"Unknown command '{verb}'"
                    if self.mode == 'json':
                        # Return JSON error
                        import json
                        error_dict = {
                            'status': 'error',
                            'message': error_message,
                            'command': verb
                        }
                        output = json.dumps(error_dict, indent=2)
                    else:
                        # Return plain text error for TTY/Markdown
                        output = f"ERROR: {error_message}"
                    return CLICommandResponse(
                        output=output,
                        status='error',
                        cli_terminated=False
                    )
            else:
                # Check if result is already Instructions (from non-workflow action execution)
                from agile_bot.src.instructions.instructions import Instructions
                if isinstance(result, Instructions):
                    # Non-workflow action returned instructions directly - don't treat as navigation
                    # Just serialize and return without showing current action instructions
                    adapter = self._get_adapter_for_domain(result)
                    output = adapter.serialize()
                    # Still show bot status after executing action
                    status_adapter = self._get_adapter_for_domain(self.bot)
                    status_output = status_adapter.serialize()
                    output = '\n'.join([
                        output,
                        "",
                        status_output
                    ])
                    return CLICommandResponse(
                        output=output,
                        cli_terminated=False
                    )
                else:
                    is_navigation_command = True  # Action shortcut is navigation
        
        # Get appropriate adapter for result type
        adapter = self._get_adapter_for_domain(result)
        output = adapter.serialize()
        
        # For navigation commands, auto-execute instructions and append full bot status
        if is_navigation_command and not cli_terminated:
            output_parts = [output]
            
            # Check if navigation succeeded
            navigation_succeeded = True
            if isinstance(result, dict) and 'status' in result:
                navigation_succeeded = result['status'] not in ['error', 'at_start', 'at_end']
            
            # Check if result is already an Instructions object (from "current" command)
            # to avoid printing instructions twice
            from agile_bot.src.instructions.instructions import Instructions
            result_is_instructions = isinstance(result, Instructions)
            
            # If navigation succeeded and result isn't already instructions, 
            # auto-execute instructions for new position
            # This applies to: next, back, scope changes, and behavior.action navigation
            if navigation_succeeded and not result_is_instructions:
                instructions_result = self.bot.current()
                
                # Check if we got an Instructions object or an error dict
                if isinstance(instructions_result, dict) and 'status' in instructions_result and instructions_result['status'] == 'error':
                    # Error getting instructions - show error message in appropriate format
                    error_message = instructions_result.get('message', 'Unknown error')
                    if self.mode == 'json':
                        import json
                        error_dict = {
                            'status': 'error',
                            'message': error_message
                        }
                        output_parts.append(json.dumps(error_dict, indent=2))
                    else:
                        output_parts.append("")
                        output_parts.append(f"ERROR: {error_message}")
                else:
                    # Got Instructions object - use adapter to serialize
                    output_parts.append("")
                    output_parts.append("=" * 100)
                    output_parts.append("INSTRUCTIONS")
                    output_parts.append("=" * 100)
                    
                    # Use adapter to format the Instructions object
                    instructions_adapter = self._get_adapter_for_domain(instructions_result)
                    output_parts.append(instructions_adapter.serialize())
            
            # Always append full bot status after navigation commands
            status_adapter = self._get_adapter_for_domain(self.bot)
            status_output = status_adapter.serialize()
            output_parts.append("")
            output_parts.append(status_output)
            
            output = '\n'.join(output_parts)
        
        return CLICommandResponse(
            output=output,
            cli_terminated=cli_terminated
        )
    
    def _parse_command(self, command: str) -> tuple[str, str]:
        """Parse command into verb and arguments."""
        parts = command.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args
    
    def _route_to_behavior_action(self, command: str) -> Any:
        """Route behavior or behavior.action commands to bot.
        
        Handles:
        - "behavior" -> bot.behaviors.navigate_to(behavior)
        - "behavior.action" -> bot.execute(behavior, action)
        - "behavior.action.operation" -> bot.execute(behavior, action, operation)
        """
        if '.' in command:
            # behavior.action or behavior.action.operation
            parts = command.split('.')
            behavior_name = parts[0]
            action_name = parts[1] if len(parts) > 1 else None
            if hasattr(self.bot, 'execute'):
                return self.bot.execute(behavior_name, action_name)
        else:
            # Single word - try as behavior name
            if hasattr(self.bot, 'behaviors') and hasattr(self.bot.behaviors, 'navigate_to'):
                try:
                    self.bot.behaviors.navigate_to(command)
                    # Return the behavior object after navigation
                    return self.bot.behaviors.current
                except ValueError:
                    # Not a valid behavior name
                    pass
        raise ValueError(f"Unknown command: {command}")
    
    def _handle_action_shortcut(self, action_name: str, args: str) -> Any:
        """Handle action shortcut commands (e.g., 'build', 'validate', 'rules').
        
        Routes to current behavior's action if action exists.
        For non-workflow actions (like 'rules'), directly executes and returns instructions.
        For workflow actions, navigates and shows instructions.
        Returns None if not an action shortcut (so caller can try other routing).
        """
        # Check if we have a current behavior
        if not self.bot.behaviors.current:
            return {
                'status': 'error',
                'message': 'No current behavior set. Please select a behavior first.'
            }
        
        behavior = self.bot.behaviors.current
        
        # Check if action exists in current behavior
        action = behavior.actions.find_by_name(action_name)
        if not action:
            # Not an action in current behavior - return None to try other routing
            return None
        
        # Check if this is a non-workflow action (like 'rules')
        # Non-workflow actions don't participate in workflow, so we execute them directly
        is_non_workflow = action in behavior.actions._non_workflow_actions
        
        if is_non_workflow:
            # For non-workflow actions, directly execute the action to get full instructions
            # This ensures we get the action's instructions with all its logic (e.g., rules loading)
            try:
                from ..actions.action_context import ActionContext
                context = action.context_class() if hasattr(action, 'context_class') else ActionContext()
                
                # Parse args if provided (e.g., for rules action with message)
                if args:
                    # Try to parse args as context parameters
                    # For now, just pass args as message if RulesActionContext is used
                    if hasattr(context, 'message'):
                        context.message = args
                
                # Call execute() for all non-workflow actions to get full execution logic
                result = action.execute(context)
                
                # Extract Instructions object from result dict
                if isinstance(result, dict) and 'instructions' in result:
                    instructions_dict = result['instructions']
                    # Reconstruct Instructions object from dict
                    from ..instructions.instructions import Instructions
                    if isinstance(instructions_dict, dict):
                        # Create new Instructions object and populate from dict
                        instructions = Instructions(
                            base_instructions=instructions_dict.get('base_instructions', []),
                            bot_paths=action.behavior.bot_paths,
                            scope=action.instructions.scope if hasattr(action, 'instructions') else None
                        )
                        # Update with all other data from dict
                        for key, value in instructions_dict.items():
                            if key not in ('base_instructions', 'display_content'):
                                instructions.set(key, value)
                        # Add display content
                        display_content = instructions_dict.get('display_content', [])
                        for line in display_content:
                            instructions.add_display(line)
                    else:
                        instructions = instructions_dict
                else:
                    # Fallback to get_instructions if execute doesn't return expected format
                    instructions = action.get_instructions(context)
                
                return instructions
            except Exception as e:
                return {
                    'status': 'error',
                    'message': f'Error executing {action_name}: {str(e)}'
                }
        else:
            # For workflow actions, navigate to the action and route normally
            behavior.actions.navigate_to(action_name)
            # Route to behavior.action pattern (which will execute and show instructions)
            return self._route_to_behavior_action(f"{behavior.name}.{action_name}")
    
    def _get_adapter_for_domain(self, domain_object: Any):
        """
        Select adapter based on domain object type and output context.
        
        Uses AdapterFactory to avoid cyclomatic complexity.
        """
        # Use explicit mode if set, otherwise auto-detect
        if self.mode:
            channel = self.mode
        else:
            # Auto-detect: TTY for interactive, markdown for piped (AI agents)
            is_piped = not sys.stdin.isatty()
            channel = 'markdown' if is_piped else 'tty'
        
        return AdapterFactory.create(domain_object, channel)
    
    def run(self):
        """
        Run CLI loop (for interactive mode).
        
        Reads commands from stdin and executes them.
        """
        try:
            while True:
                try:
                    line = input(f"[{self.bot.name}] > ").strip()
                    if not line:
                        continue
                    
                    response = self.execute_command(line)
                    print(response.output)
                    print("")  # Blank line after output
                    
                    if response.cli_terminated:
                        break
                    
                except EOFError:
                    print("\nExiting CLI...")
                    break
                except KeyboardInterrupt:
                    print("\n\nInterrupted by user. Exiting CLI...")
                    break
                except Exception as e:
                    print(f"Error: {e}", file=sys.stderr)
                    
        except KeyboardInterrupt:
            pass
