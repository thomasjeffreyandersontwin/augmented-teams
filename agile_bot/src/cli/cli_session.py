"""
Minimal CLI session - command router that routes to Bot methods and uses adapters for serialization.
"""

import sys
import logging
from pathlib import Path
from typing import Any, Dict

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
        
        # Check for --format json flag and set mode
        if args and ('--format json' in args or '--format=json' in args):
            # Set mode to json (stays that way until changed)
            self.mode = 'json'
            # Strip --format json from args
            args = args.replace('--format json', '').replace('--format=json', '').strip()
        
        # Check for exit command
        cli_terminated = verb == 'exit'
        
        # Track if this command changes navigation state (should auto-display status)
        is_navigation_command = verb in ('next', 'back', 'current', 'scope', 'path', 'workspace')
        
        # Special case: "status" just returns the bot itself
        if verb == 'status':
            result = self.bot
        # Special case: "bot" switches to a different bot
        elif verb == 'bot':
            if not args:
                # No bot name provided - show current bot and available bots
                result = {
                    'status': 'info',
                    'current_bot': self.bot.bot_name,
                    'registered_bots': self.bot.bots,
                    'message': f"Current bot: {self.bot.bot_name}. Available bots: {', '.join(self.bot.bots)}. Usage: bot <name>"
                }
            else:
                # Switch to specified bot
                target_bot_name = args.strip()
                try:
                    self.bot.active_bot = target_bot_name
                    # Update self.bot to reference the new active bot
                    self.bot = self.bot.active_bot
                    result = {
                        'status': 'success',
                        'message': f'Switched to bot: {target_bot_name}',
                        'bot_name': target_bot_name
                    }
                except ValueError as e:
                    result = {
                        'status': 'error',
                        'message': str(e)
                    }
        # Special case: "save" calls bot.save() with parsed parameters
        elif verb == 'save':
            params = self._parse_save_params(args)
            result = self.bot.save(**params)
            # Save returns a dict - serialize directly in JSON mode
            if self.mode == 'json':
                import json
                output = json.dumps(result, indent=2)
                return CLICommandResponse(
                    output=output,
                    status=result.get('status', 'success'),
                    cli_terminated=False
                )
        # Special case: "submitrules:behavior" calls bot.submit_behavior_rules()
        elif verb.startswith('submitrules:') or verb.startswith('submitrules '):
            behavior_name = verb.split(':', 1)[1] if ':' in verb else verb.split(' ', 1)[1]
            behavior_name = behavior_name.strip()
            result = self.bot.submit_behavior_rules(behavior_name)
            # Submit returns a dict - serialize based on mode
            if self.mode == 'json':
                import json
                output = json.dumps(result, indent=2)
                return CLICommandResponse(
                    output=output,
                    status=result.get('status', 'success'),
                    cli_terminated=False
                )
            else:
                # For TTY/markdown mode, show success message
                if result.get('status') == 'success':
                    output_lines = [
                        f"✓ {behavior_name} rules submitted to chat!",
                        f"  Behavior: {result.get('behavior')}",
                        f"  Action: {result.get('action')}",
                        f"  Length: {result.get('instructions_length', 0)} characters"
                    ]
                    
                    if result.get('cursor_status') == 'opened':
                        output_lines.append("  ✓ Cursor chat opened")
                    
                    return CLICommandResponse(
                        output='\n'.join(output_lines),
                        status='success',
                        cli_terminated=False
                    )
                else:
                    return CLICommandResponse(
                        output=f"Error: {result.get('message', 'Unknown error')}",
                        status='error',
                        cli_terminated=False
                    )
        # Special case: "submit" calls bot.submit_current_action() and returns result with instructions
        elif verb == 'submit':
            result = self.bot.submit_current_action()
            # Submit returns a dict - serialize based on mode
            if self.mode == 'json':
                import json
                output = json.dumps(result, indent=2)
                return CLICommandResponse(
                    output=output,
                    status=result.get('status', 'success'),
                    cli_terminated=False
                )
            else:
                # For TTY/markdown mode, show success message
                if result.get('status') == 'success':
                    output_lines = [
                        f"✓ Instructions copied to clipboard!",
                        f"  Behavior: {result.get('behavior')}",
                        f"  Action: {result.get('action')}",
                        f"  Length: {result.get('instructions_length', 0)} characters"
                    ]
                    
                    if result.get('cursor_status') == 'opened':
                        output_lines.append("  ✓ Cursor chat opened")
                    elif result.get('cursor_status', '').startswith('failed'):
                        output_lines.append(f"  ⚠ Could not open Cursor chat automatically")
                        output_lines.append("  → Open Cursor chat manually and paste (Ctrl+V)")
                    else:
                        output_lines.append("  → Paste into Cursor chat (Ctrl+V)")
                    
                    output = '\n'.join(output_lines)
                else:
                    output = f"✗ {result.get('message', 'Submit failed')}"
                
                return CLICommandResponse(
                    output=output,
                    status=result.get('status', 'success'),
                    cli_terminated=False
                )
        # Route to Bot method using reflection
        elif hasattr(self.bot, verb):
            attr = getattr(self.bot, verb)
            # Check if property or method
            if callable(attr):
                result = attr(args) if args else attr()
            else:
                result = attr  # It's a property (e.g., scope, bot_path)
                
                # Special case: If result is a Behavior object, execute it with current action
                from agile_bot.src.behaviors.behavior import Behavior
                is_behavior = isinstance(result, Behavior)
                
                if is_behavior:
                    # Execute behavior with current action (bot.execute handles navigation)
                    result = self.bot.execute(result.name, None)
                    is_navigation_command = True  # Executing behavior = navigation command
        else:
            # Check if it's an action shortcut (route to current behavior's action)
            result = self._handle_action_shortcut(verb, args)
            
            # Special case: if action is 'rules', automatically submit to chat
            if verb == 'rules' and result is not None:
                from agile_bot.src.instructions.instructions import Instructions
                if isinstance(result, Instructions):
                    # Submit the RULES instructions using behavior.submitRules()
                    if self.bot.behaviors.current:
                        submit_result = self.bot.behaviors.current.submitRules()
                    else:
                        submit_result = {
                            'status': 'error',
                            'message': 'No current behavior set'
                        }
                    
                    # Show success message
                    if submit_result.get('status') == 'success' and self.mode != 'json':
                        output_lines = [
                            f"✓ Rules submitted to chat!",
                            f"  Behavior: {submit_result.get('behavior')}",
                            f"  Action: {submit_result.get('action')}",
                            f"  Length: {submit_result.get('instructions_length', 0)} characters"
                        ]
                        
                        if submit_result.get('cursor_status') == 'opened':
                            output_lines.append("  ✓ Cursor chat opened")
                        
                        # Return submit result instead of instructions
                        return CLICommandResponse(
                            output='\n'.join(output_lines),
                            status='success',
                            cli_terminated=False
                        )
            
            if result is None:
                # Not an action shortcut, try behavior.action pattern
                try:
                    result = self._route_to_behavior_action(command)
                    # behavior.action is NOT a navigation command anymore - execute returns instructions
                    is_navigation_command = False
                    
                    # Special case: if action is 'rules', automatically submit to chat
                    if '.rules' in command.lower():
                        # Get the instructions that were just generated
                        from agile_bot.src.instructions.instructions import Instructions
                        if isinstance(result, Instructions):
                            # Submit the RULES instructions using behavior.submitRules()
                            if self.bot.behaviors.current:
                                submit_result = self.bot.behaviors.current.submitRules()
                            else:
                                submit_result = {
                                    'status': 'error',
                                    'message': 'No current behavior set'
                                }
                            
                            # Show success message
                            if submit_result.get('status') == 'success' and self.mode != 'json':
                                output_lines = [
                                    f"✓ Rules submitted to chat!",
                                    f"  Behavior: {submit_result.get('behavior')}",
                                    f"  Action: {submit_result.get('action')}",
                                    f"  Length: {submit_result.get('instructions_length', 0)} characters"
                                ]
                                
                                if submit_result.get('cursor_status') == 'opened':
                                    output_lines.append("  ✓ Cursor chat opened")
                                
                                # Return submit result instead of instructions
                                return CLICommandResponse(
                                    output='\n'.join(output_lines),
                                    status='success',
                                    cli_terminated=False
                                )
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
        
        # Check if result is Instructions (from behavior.action execution)
        from agile_bot.src.instructions.instructions import Instructions
        if isinstance(result, Instructions) and self.mode == 'json':
            # Build unified JSON response with instructions and bot status
            import json
            instructions_data = json.loads(output) if isinstance(output, str) else output
            status_adapter = self._get_adapter_for_domain(self.bot)
            status_json = status_adapter.serialize()
            status_data = json.loads(status_json) if isinstance(status_json, str) else status_json
            
            unified_response = {
                'instructions': instructions_data,
                'bot': status_data
            }
            output = json.dumps(unified_response, indent=2)
            return CLICommandResponse(
                output=output,
                cli_terminated=False
            )
        
        # For navigation commands, auto-execute instructions and append full bot status
        if is_navigation_command and not cli_terminated:
            # JSON mode: build unified structure { execution, instructions?, bot }
            # Text mode: concatenate text outputs with banners
            if self.mode == 'json':
                import json
                # Parse the initial result JSON
                result_data = json.loads(output) if isinstance(output, str) else output
                unified_response = {}
                
                # Add the navigation result (scope, navigation, etc.)
                if isinstance(result_data, dict):
                    unified_response.update(result_data)
                
                # Check if navigation succeeded
                navigation_succeeded = True
                if isinstance(result, dict) and 'status' in result:
                    navigation_succeeded = result['status'] not in ['error', 'at_start', 'at_end']
                
                # Check if result is already an Instructions object
                from agile_bot.src.instructions.instructions import Instructions
                result_is_instructions = isinstance(result, Instructions)
                
                # Add instructions if navigation succeeded
                if navigation_succeeded and not result_is_instructions:
                    instructions_result = self.bot.current()
                    
                    if isinstance(instructions_result, dict) and 'status' in instructions_result and instructions_result['status'] == 'error':
                        # Error getting instructions
                        unified_response['instructions_error'] = instructions_result.get('message', 'Unknown error')
                    else:
                        # Got Instructions object - serialize to dict
                        instructions_adapter = self._get_adapter_for_domain(instructions_result)
                        instructions_json = instructions_adapter.serialize()
                        instructions_data = json.loads(instructions_json) if isinstance(instructions_json, str) else instructions_json
                        unified_response['instructions'] = instructions_data
                
                # Always add full bot status
                status_adapter = self._get_adapter_for_domain(self.bot)
                status_json = status_adapter.serialize()
                status_data = json.loads(status_json) if isinstance(status_json, str) else status_json
                unified_response['bot'] = status_data
                
                output = json.dumps(unified_response, indent=2)
            else:
                # Text mode: concatenate with banners (original behavior)
                output_parts = [output]
                
                # Check if navigation succeeded
                navigation_succeeded = True
                if isinstance(result, dict) and 'status' in result:
                    navigation_succeeded = result['status'] not in ['error', 'at_start', 'at_end']
                
                # Check if result is already an Instructions object
                from agile_bot.src.instructions.instructions import Instructions
                result_is_instructions = isinstance(result, Instructions)
                
                # Add instructions if navigation succeeded
                if navigation_succeeded and not result_is_instructions:
                    instructions_result = self.bot.current()
                    
                    if isinstance(instructions_result, dict) and 'status' in instructions_result and instructions_result['status'] == 'error':
                        # Error getting instructions
                        error_message = instructions_result.get('message', 'Unknown error')
                        output_parts.append("")
                        output_parts.append(f"ERROR: {error_message}")
                    else:
                        # Got Instructions object - add banner and serialize
                        output_parts.append("")
                        output_parts.append("=" * 100)
                        output_parts.append("INSTRUCTIONS")
                        output_parts.append("=" * 100)
                        
                        instructions_adapter = self._get_adapter_for_domain(instructions_result)
                        output_parts.append(instructions_adapter.serialize())
                
                # Always append full bot status
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
    
    def _parse_save_params(self, args_string: str) -> Dict[str, Any]:
        """Parse save parameters from command arguments.
        
        Delegates to _parse_action_params since save uses the same parameter format.
        """
        return self._parse_action_params(args_string)
    
    def _parse_action_params(self, args_string: str) -> Dict[str, Any]:
        """Parse action parameters from command arguments.
        
        Supports: --answers, --decisions, --assumptions, --evidence_provided
        
        Args:
            args_string: Arguments portion of command (e.g., "--answers '{...}' --assumptions '[...]'")
        
        Returns:
            Dict of parsed parameters ready for action context
        """
        import re
        import json
        
        params = {}
        
        # Parse --answers '{"key": "value"}'
        answers_match = re.search(r"--answers\s+'([^']+)'", args_string)
        if answers_match:
            try:
                params['answers'] = json.loads(answers_match.group(1))
            except json.JSONDecodeError as e:
                logging.warning(f"Failed to parse --answers: {e}")
        
        # Parse --decisions '{"key": "value"}'
        decisions_match = re.search(r"--decisions\s+'([^']+)'", args_string)
        if decisions_match:
            try:
                params['decisions'] = json.loads(decisions_match.group(1))
            except json.JSONDecodeError as e:
                logging.warning(f"Failed to parse --decisions: {e}")
        
        # Parse --assumptions '["item1", "item2"]'
        assumptions_match = re.search(r"--assumptions\s+'([^']+)'", args_string)
        if assumptions_match:
            try:
                params['assumptions'] = json.loads(assumptions_match.group(1))
            except json.JSONDecodeError as e:
                logging.warning(f"Failed to parse --assumptions: {e}")
        
        # Parse --evidence_provided '{"key": "value"}'
        evidence_match = re.search(r"--evidence_provided\s+'([^']+)'", args_string)
        if evidence_match:
            try:
                params['evidence_provided'] = json.loads(evidence_match.group(1))
            except json.JSONDecodeError as e:
                logging.warning(f"Failed to parse --evidence_provided: {e}")
        
        return params
    
    def _route_to_behavior_action(self, command: str) -> Any:
        """Route behavior or behavior.action commands to bot with parameter support.
        
        Now parses CLI parameters like --answers, --decisions, --assumptions
        and passes them to bot.execute() as params dict.
        """
        # Split command into core command and arguments
        # Example: "shape.strategy --decisions '{...}'" -> "shape.strategy", "--decisions '{...}'"
        parts = command.split(maxsplit=1)
        command_core = parts[0]
        args_string = parts[1] if len(parts) > 1 else ''
        
        # Parse action parameters from arguments
        params = self._parse_action_params(args_string) if args_string else None
        
        if '.' in command_core:
            # behavior.action pattern
            command_parts = command_core.split('.')
            behavior_name = command_parts[0]
            action_name = command_parts[1] if len(command_parts) > 1 else None
            
            if hasattr(self.bot, 'execute'):
                return self.bot.execute(behavior_name, action_name, params)
        else:
            # Single word - try as behavior name and execute current action
            if hasattr(self.bot, 'execute'):
                result = self.bot.execute(command_core, None, params)
                # Check if it's an error (behavior not found)
                if isinstance(result, dict) and result.get('status') == 'error':
                    raise ValueError(result.get('message', 'Unknown error'))
                return result
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
