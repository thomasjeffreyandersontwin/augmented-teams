# Validation Status - code
Started: 2025-12-30 02:58:53
Files: 275

## avoid_excessive_guards
**repl_session.py** - 1 violation(s)

[!] WARNING (line 1464)
Line 1464: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

```python
    def parse_command_parameters(self, args: str) -> Dict[str, Any]:
        params = {}
        if not args:
            return params
        
```

---

## eliminate_duplication
**repl_session.py** - 2 violation(s)

[X] ERROR (line 191)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (display_current_state:191-202):
```python
lines.append('```')
lines.append(str(self.workspace_directory))
lines.append('```')
lines.append('')
lines.append('To change path:')
lines.append('```')
lines.append('path demo/mob_minion             ...
```

Location (display_current_state:226-234):
```python
lines.append(formatter.subsection_separator())
lines.append(f'## {formatter.position_icon()} **Progress**')
lines.append('**Current Position:**')
lines.append('```')
lines.append(f'{self.progress_path...
```

[X] ERROR (line 469)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_handle_next_command:469-488):
```python
if not self.has_current_action:
    return REPLCommandResponse(output='ERROR: No current action', response='ERROR: No current action', status='error')
behavior = self.current_behavior
if not behavior:...
```

Location (_handle_back_command:505-524):
```python
if not self.has_current_action:
    return REPLCommandResponse(output='ERROR: No current action', response='ERROR: No current action', status='error')
behavior = self.current_behavior
if not behavior:...
```

---


## Cross-File Duplication Analysis
Scanning 1 changed file(s) against 20 total files...
Extracted 256 changed blocks, 740 reference blocks
Starting 189,440 pairwise comparisons...
Comparing: 5% (9,472/189,440) - 0 violations - ETA: 59s  
Comparing: 10% (18,944/189,440) - 0 violations - ETA: 54s  
Comparing: 15% (28,416/189,440) - 0 violations - ETA: 53s  
Comparing: 20% (37,888/189,440) - 0 violations - ETA: 52s  
Comparing: 25% (47,360/189,440) - 0 violations - ETA: 49s  
Comparing: 30% (56,832/189,440) - 0 violations - ETA: 47s  
Comparing: 35% (66,304/189,440) - 0 violations - ETA: 45s  
Comparing: 40% (75,776/189,440) - 0 violations - ETA: 43s  
Comparing: 45% (85,248/189,440) - 0 violations - ETA: 41s  
Comparing: 50% (94,720/189,440) - 0 violations - ETA: 39s  
Comparing: 55% (104,192/189,440) - 0 violations - ETA: 37s  
Comparing: 60% (113,664/189,440) - 1 violations - ETA: 32s  
Found 10 violations so far...
Comparing: 65% (123,136/189,440) - 13 violations - ETA: 28s  
Complete: 123904 comparisons, 13 violations

## enforce_encapsulation
**repl_session.py** - 1 violation(s)

[!] WARNING (line 725)
Method "_handle_scope_command" in class "REPLSession" has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

---

## keep_classes_small_with_single_responsibility
**repl_session.py** - 1 violation(s)

[!] WARNING (line 17)
Class "REPLSession" is 1582 lines - should be under 300 lines (extract related methods into separate classes)

```python


class REPLSession:
    def __init__(self, bot, workspace_directory: Path):
        self.cli_bot = CLIBot(bot, self)
        self.workspace_directory = Path(workspace_directory)
        tty_result = self.detect_tty()
        self.formatter = FormatterFactory.create_formatter(tty_detected=tty_result.tty_detected)
    
    @property
    # ... (truncated)
```

---

## keep_functions_small_focused
**repl_session.py** - 1 violation(s)

[!] WARNING (line 144)
Function "display_current_state" is 83 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return True
    
    def display_current_state(self, full=False) -> REPLStateDisplay:
        """Single source of truth for displaying current bot state.
        
        Returns REPLStateDisplay with formatted status output showing:
        - Bot name and paths
        - Current position header
        - Scope filter (if set)
        - Progress in workflow
        - Hierarchical behavior/action/operation tree
        """
        if not self.has_current_action:
            if not self._initialize_to_first_behavior_action():
                return REPLStateDisplay(
                    output="No behaviors available\n\n  help          - Show detailed help\n  exit          - Exit REPL",
                    state_loaded=False
                )
            return self.display_current_state(full=full)
        
        lines = []
        formatter = self.formatter
        
        # Get bot name from bot_directory
        if self.bot and hasattr(self.bot, 'bot_paths'):
            bot_name = self.bot.bot_paths.bot_directory.name
        else:
            bot_name = 'UNKNOWN'
        
        # THICK LINE at top
        lines.append(formatter.section_separator())
        lines.append("")
        
        # Bot section header
        lines.append(f"## {formatter.bot_icon()} Bot: {bot_name}")
        
        if self.bot:
            bot_path = self.bot.bot_paths.bot_directory if hasattr(self.bot, 'bot_paths') else 'Unknown'
            lines.append(f"**Bot Path:**")
            lines.append("```")
            lines.append(str(bot_path))
            lines.append("```")
        
        lines.append("")
        
        # Workspace section
        workspace_name = self.workspace_directory.name if hasattr(self.workspace_directory, 'name') else 'base_bot'
        lines.append(f"{formatter.workspace_icon()} **Workspace:** {workspace_name}")
        lines.append(f"**Path:**")
        lines.append("```")
    # ... (truncated)
```

---

## maintain_vertical_density
**repl_session.py** - 10 violation(s)

[i] INFO (line 144)
Function "display_current_state" is 114 lines - consider improving vertical density by declaring variables near usage

```python
        return True
    
    def display_current_state(self, full=False) -> REPLStateDisplay:
        """Single source of truth for displaying current bot state.
        
        Returns REPLStateDisplay with formatted status output showing:
        - Bot name and paths
        - Current position header
        - Scope filter (if set)
        - Progress in workflow
    # ... (truncated)
```

[i] INFO (line 268)
Function "_convert_domain_result_to_repl_response" is 57 lines - consider improving vertical density by declaring variables near usage

```python
        return state_display.output
    
    def _convert_domain_result_to_repl_response(self, result: Dict[str, Any], command: str) -> REPLCommandResponse:
        """Convert a domain method result to a REPL response.
        
        Args:
            result: Dict returned from domain method
            command: The command that was executed
        
        Returns:
    # ... (truncated)
```

[i] INFO (line 339)
Function "_handle_simple_command" is 59 lines - consider improving vertical density by declaring variables near usage

```python
        return self._handle_simple_command(command)
    
    def _handle_simple_command(self, command: str) -> REPLCommandResponse:
        parts = command.split(maxsplit=1)
        command_verb = parts[0].lower()
        command_args = parts[1] if len(parts) > 1 else ""
        
        # Meta commands
        if command_verb == 'help':
            return self._handle_help_command(command_args)
    # ... (truncated)
```

[i] INFO (line 549)
Function "_handle_instructions_command" is 56 lines - consider improving vertical density by declaring variables near usage

```python
        )
    
    def _handle_instructions_command(self, args: str = "") -> REPLCommandResponse:
        """Handle instructions command"""
        import sys
        print(f"[DEBUG] _handle_instructions_command called with args: '{args}'", file=sys.stderr)
        if not self.has_current_action:
            return REPLCommandResponse(
                output="ERROR: No current action to get instructions for",
                response="ERROR: No current action",
    # ... (truncated)
```

[i] INFO (line 627)
Function "_handle_confirm_command" is 54 lines - consider improving vertical density by declaring variables near usage

```python
            )
    
    def _handle_confirm_command(self) -> REPLCommandResponse:
        """Handle confirm command"""
        if not self.has_current_action:
            return REPLCommandResponse(
                output="ERROR: No current action to confirm",
                response="ERROR: No current action",
                status="error"
            )
    # ... (truncated)
```

[i] INFO (line 701)
Function "_handle_scope_command" is 65 lines - consider improving vertical density by declaring variables near usage

```python
        )
    
    def _handle_scope_command(self, args: str = "") -> REPLCommandResponse:
        """Handle scope command"""
        if not args:
            # Show current scope
            output = self.cli_bot.get_scope_display()
            return REPLCommandResponse(
                output=output,
                response=output,
    # ... (truncated)
```

[i] INFO (line 842)
Function "_execute_operation_locally" is 60 lines - consider improving vertical density by declaring variables near usage

```python
            return None, args.strip().strip('"').strip("'")
    
    def _execute_operation_locally(self, target: str, cli_args: str = "") -> str:
        """Execute a CLI operation locally and return its output.
        
        Args:
            target: CLI target (e.g., 'tests.build', 'tests.build.instructions', 'tests.build.submit')
            cli_args: CLI arguments like '--scope "X"'
        
        Returns:
    # ... (truncated)
```

[i] INFO (line 1133)
Function "_handle_dot_notation" is 127 lines - consider improving vertical density by declaring variables near usage

```python
            pass
    
    def _handle_dot_notation(self, command: str) -> REPLCommandResponse:
        """Handle dot notation commands (behavior.action.operation)"""
        # Parse dot notation: behavior.action.operation or action.operation or .operation
        parts = command.split()
        dot_path = parts[0]
        args = ' '.join(parts[1:]) if len(parts) > 1 else ""
        
        path_parts = dot_path.split('.')
    # ... (truncated)
```

[i] INFO (line 1261)
Function "_handle_action_shortcut" is 60 lines - consider improving vertical density by declaring variables near usage

```python
            )
    
    def _handle_action_shortcut(self, action_name: str, args_str: str) -> REPLCommandResponse:
        args_str = args_str.strip()
        
        # Parse CLI-style arguments (--message, --scope, etc.)
        cli_args = []
        subcommand = None
        
        if args_str:
    # ... (truncated)
```

[i] INFO (line 1366)
Function "_execute_action_with_args" is 73 lines - consider improving vertical density by declaring variables near usage

```python
        return converted_args
    
    def _execute_action_with_args(self, action_name: str, cli_args: list, operation: str = None) -> REPLCommandResponse:
        if not self.has_current_behavior:
            return REPLCommandResponse(
                output="ERROR: No current behavior set. Please select a behavior first.",
                response="ERROR: No current behavior set",
                status="error"
            )
        
    # ... (truncated)
```

---

## never_swallow_exceptions
**repl_session.py** - 2 violation(s)

[X] ERROR (line 1130)
Except block only contains pass at line 1130 - exceptions must be logged or rethrown, never swallowed

```python
            state_data['completed_behaviors'] = completed
            state_file.write_text(json.dumps(state_data, indent=2))
        except (json.JSONDecodeError, IOError):
            pass
    
```

[X] ERROR (line 78)
Except block only contains pass at line 78 - exceptions must be logged or rethrown, never swallowed

```python
                state_data = json.loads(state_file.read_text())
                return state_data.get('action_phase', 'not_started')
            except (json.JSONDecodeError, IOError):
                pass
        return 'not_started'
```

---

## refactor_completely_not_partially
**repl_session.py** - 3 violation(s)

[!] WARNING (line 72)
Fallback/legacy support code found (comment at line 72, code at line 73) - complete refactoring by removing old pattern support

[!] WARNING (line 239)
Fallback/legacy support code found (comment at line 239, code at line 240) - complete refactoring by removing old pattern support

[!] WARNING (line 1509)
Fallback/legacy support code found (comment at line 1509, code at line 1510) - complete refactoring by removing old pattern support

---

## simplify_control_flow
**repl_session.py** - 5 violation(s)

[!] WARNING (line 438)
Function "_handle_current_command" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        )
    
    def _handle_current_command(self) -> REPLCommandResponse:
        """Re-execute current operation based on progress state"""
        if not self.has_current_action:
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
        
        # Extract operation from progress (behavior.action.operation)
        progress = self.get_progress_line()
        if '.' in progress and 'Progress: ' in progress:
            parts = progress.replace('Progress: ', '').split('.')
    # ... (truncated)
```

[!] WARNING (line 701)
Function "_handle_scope_command" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        )
    
    def _handle_scope_command(self, args: str = "") -> REPLCommandResponse:
        """Handle scope command"""
        if not args:
            # Show current scope
            output = self.cli_bot.get_scope_display()
            return REPLCommandResponse(
                output=output,
                response=output,
                status="success"
            )
        
        # Handle "all" - clears the scope filter
        if args.lower() == 'all':
    # ... (truncated)
```

[!] WARNING (line 842)
Function "_execute_operation_locally" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
            return None, args.strip().strip('"').strip("'")
    
    def _execute_operation_locally(self, target: str, cli_args: str = "") -> str:
        """Execute a CLI operation locally and return its output.
        
        Args:
            target: CLI target (e.g., 'tests.build', 'tests.build.instructions', 'tests.build.submit')
            cli_args: CLI arguments like '--scope "X"'
        
        Returns:
            Output from the operation (instructions, submit result, confirm result, etc.)
        """
        # Parse target
        parts = target.split('.')
        if len(parts) < 2:
    # ... (truncated)
```

[!] WARNING (line 1133)
Function "_handle_dot_notation" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

```python
            pass
    
    def _handle_dot_notation(self, command: str) -> REPLCommandResponse:
        """Handle dot notation commands (behavior.action.operation)"""
        # Parse dot notation: behavior.action.operation or action.operation or .operation
        parts = command.split()
        dot_path = parts[0]
        args = ' '.join(parts[1:]) if len(parts) > 1 else ""
        
        path_parts = dot_path.split('.')
        
        # . alone means current position
        if dot_path == '.':
            return self._handle_current_command()
        
    # ... (truncated)
```

[!] WARNING (line 1329)
Function "_convert_repl_scope_to_cli_format" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
            return args_str.split()
    
    def _convert_repl_scope_to_cli_format(self, cli_args: list) -> list:
        import json
        converted_args = []
        i = 0
        while i < len(cli_args):
            arg = cli_args[i]
            if arg == '--scope' and i + 1 < len(cli_args):
                scope_value = cli_args[i + 1]
                if scope_value.startswith(('file:', 'files:')):
                    prefix = 'file:' if scope_value.startswith('file:') else 'files:'
                    paths = scope_value[len(prefix):].split(',')
                    paths = [p.strip() for p in paths if p.strip()]
                    json_scope = json.dumps({"type": "files", "value": paths})
    # ... (truncated)
```

---

## stop_writing_useless_comments
**repl_session.py** - 31 violation(s)

[X] ERROR (line 145)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def display_current_state(self, full=False) -> REPLStateDisplay:
        """Single source of truth for displaying current bot state.
        
        Returns REPLStateDisplay with formatted status output showing:
        - Bot name and paths
        - Current position header
        - Scope filter (if set)
        - Progress in workflow
        - Hierarchical behavior/action/operation tree
        """
        if not self.has_current_action:
```

[X] ERROR (line 260)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_context_header_for_ai(self) -> str:
        """Get status display as a string for AI context headers.
        
        This is a convenience method that extracts just the output string
        from display_current_state().
        """
        state_display = self.display_current_state()
```

[X] ERROR (line 269)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _convert_domain_result_to_repl_response(self, result: Dict[str, Any], command: str) -> REPLCommandResponse:
        """Convert a domain method result to a REPL response.
        
        Args:
            result: Dict returned from domain method
            command: The command that was executed
        
        Returns:
            REPLCommandResponse with appropriate formatting
        """
        status = result.get('status', 'success')
```

[X] ERROR (line 400)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_help_command(self, args: str = "") -> REPLCommandResponse:
        """Handle help command using bot.help"""
        if not args:
```

[X] ERROR (line 430)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_status_command(self) -> REPLCommandResponse:
        """Handle status command using bot.status"""
        state_display = self.display_current_state(full=True)
```

[X] ERROR (line 439)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_current_command(self) -> REPLCommandResponse:
        """Re-execute current operation based on progress state"""
        if not self.has_current_action:
```

[X] ERROR (line 468)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_next_command(self) -> REPLCommandResponse:
        """Handle next/advance navigation"""
        if not self.has_current_action:
```

[X] ERROR (line 504)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_back_command(self) -> REPLCommandResponse:
        """Handle back/previous navigation"""
        if not self.has_current_action:
```

[X] ERROR (line 550)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_instructions_command(self, args: str = "") -> REPLCommandResponse:
        """Handle instructions command"""
        import sys
```

[X] ERROR (line 607)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_submit_command(self, args: str = "") -> REPLCommandResponse:
        """Handle submit command"""
        if not self.has_current_action:
```

[X] ERROR (line 628)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_confirm_command(self) -> REPLCommandResponse:
        """Handle confirm command"""
        if not self.has_current_action:
```

[X] ERROR (line 683)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_path_command(self, args: str = "") -> REPLCommandResponse:
        """Handle path/workspace command"""
        if not args:
```

[X] ERROR (line 702)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_scope_command(self, args: str = "") -> REPLCommandResponse:
        """Handle scope command"""
        if not args:
```

[X] ERROR (line 768)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _validate_headless_ready(self, args: str) -> tuple[bool, REPLCommandResponse | None, any]:
        """Validate that headless mode is ready to execute.
        
        Returns:
            Tuple of (is_valid, error_response, config)
            - If is_valid is False, error_response contains the error to return
            - If is_valid is True, config contains the loaded configuration
        """
        from agile_bot.bots.base_bot.src.repl_cli.headless.headless_config import HeadlessConfig
```

[X] ERROR (line 809)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _parse_headless_args(self, args: str) -> tuple[str | None, str]:
        """Parse headless command args into target and message.
        
        Args:
            args: Raw argument string (e.g., 'test.build "message" --scope "X"')
        
        Returns:
            Tuple of (target, message) where:
            - target is the CLI target (e.g., 'test.build') or None
            - message is the rest (message + CLI args)
        """
        import shlex
```

[X] ERROR (line 843)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _execute_operation_locally(self, target: str, cli_args: str = "") -> str:
        """Execute a CLI operation locally and return its output.
        
        Args:
            target: CLI target (e.g., 'tests.build', 'tests.build.instructions', 'tests.build.submit')
            cli_args: CLI arguments like '--scope "X"'
        
        Returns:
            Output from the operation (instructions, submit result, confirm result, etc.)
        """
        # Parse target
```

[X] ERROR (line 904)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _prepare_headless_message(self, target: str | None, message: str) -> str:
        """Prepare the final message for headless execution.
        
        If a target is provided (behavior.action), gets instructions and combines with message.
        
        Args:
            target: Optional CLI target (e.g., 'tests.build')
            message: User message (may include CLI args like --scope)
        
        Returns:
            Final message to send to headless session
        """
        if target:
```

[X] ERROR (line 952)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _format_headless_result(self, execution_result) -> REPLCommandResponse:
        """Format headless execution result as a REPL response.
        
        Args:
            execution_result: Result from HeadlessSession.invokes()
        
        Returns:
            REPLCommandResponse with formatted output
        """
        output_lines = [
```

[X] ERROR (line 979)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_headless_command(self, args: str = "") -> REPLCommandResponse:
        """Handle headless command - execute instruction in headless mode"""
        from agile_bot.bots.base_bot.src.repl_cli.headless.headless_session import HeadlessSession
```

[X] ERROR (line 1024)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_behavior_command(self, behavior_name: str) -> REPLCommandResponse:
        """Handle behavior navigation"""
        behavior = self.cli_bot.behaviors.domain_behaviors.find_by_name(behavior_name)
```

[X] ERROR (line 1053)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def navigate_to_behavior_action(self, behavior_name: str, action_name: str):
        """Navigate to a specific behavior and action
        
        Raises:
            ValueError: If behavior or action not found
        """
        # Navigate to behavior
```

[X] ERROR (line 1074)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _wrap_navigation_with_instructions(self) -> REPLCommandResponse:
        """After navigation, auto-execute instructions for new position"""
        return self._handle_instructions_command()
```

[X] ERROR (line 1078)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _wrap_with_context_header(self, content: str, response_msg: str) -> REPLCommandResponse:
        """Wrap content with instructions header and CLI status section"""
        formatter = self.formatter
```

[X] ERROR (line 1119)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _mark_behavior_complete(self, behavior_name: str) -> None:
        """Mark a behavior as complete in the state file"""
        state_file = self.workspace_directory / 'behavior_action_state.json'
```

[X] ERROR (line 1134)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_dot_notation(self, command: str) -> REPLCommandResponse:
        """Handle dot notation commands (behavior.action.operation)"""
        # Parse dot notation: behavior.action.operation or action.operation or .operation
```

[X] ERROR (line 210)
Useless comment: "# Get scope display" - delete it or improve the code instead

```python
        lines.append(formatter.subsection_separator())
        
        # Get scope display
        scope_display = self.cli_bot.get_scope_display()
```

[X] ERROR (line 757)
Useless comment: "# Get the scope display lines" - delete it or improve the code instead

```python
        result = self.cli_bot.set_scope(scope)
        
        # Get the scope display lines
        output = self.cli_bot.get_scope_display()
```

[X] ERROR (line 938)
Useless comment: "# Execute the target operation locally to get output" - delete it or improve the code instead

```python
            cli_args = ' '.join(cli_args_parts)
            
            # Execute the target operation locally to get output
            operation_output = self._execute_operation_locally(target, cli_args)
```

[X] ERROR (line 991)
Useless comment: "# Execute in headless mode" - delete it or improve the code instead

```python
        target, message = self._parse_headless_args(args)
        
        # Execute in headless mode
        try:
```

[X] ERROR (line 1005)
Useless comment: "# Execute in headless mode" - delete it or improve the code instead

```python
                final_message = message
            
            # Execute in headless mode
            execution_result = session.invokes(message=final_message, context_file=None)
```

[X] ERROR (line 1060)
Useless comment: "# Get the behavior" - delete it or improve the code instead

```python
        # Navigate to behavior
        self.cli_bot.behaviors.domain_behaviors.navigate_to(behavior_name)
        # Get the behavior
        behavior = self.cli_bot.behaviors.domain_behaviors.find_by_name(behavior_name)
```

---

## use_domain_language
**repl_session.py** - 73 violation(s)

[i] INFO (line 17)
Class "REPLSession" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 18)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 82)
Function "set_action_phase" uses parameter name "phase" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 96)
Function "stage_name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 120)
Function "detect_tty" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 127)
Function "get_progress_line" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 144)
Function "display_current_state" uses parameter name "full" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 259)
Function "get_context_header_for_ai" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 268)
Function "_convert_domain_result_to_repl_response" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 268)
Function "_convert_domain_result_to_repl_response" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 326)
Function "read_and_execute_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 326)
Function "read_and_execute_command" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 339)
Function "_handle_simple_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 339)
Function "_handle_simple_command" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 399)
Function "_handle_help_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 399)
Function "_handle_help_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 429)
Function "_handle_status_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 438)
Function "_handle_current_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 467)
Function "_handle_next_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 503)
Function "_handle_back_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 549)
Function "_handle_instructions_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 549)
Function "_handle_instructions_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 606)
Function "_handle_submit_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 606)
Function "_handle_submit_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 627)
Function "_handle_confirm_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 682)
Function "_handle_path_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 701)
Function "_handle_scope_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 701)
Function "_handle_scope_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 767)
Function "_validate_headless_ready" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 808)
Function "_parse_headless_args" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 808)
Function "_parse_headless_args" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 842)
Function "_execute_operation_locally" uses parameter name "target" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 842)
Function "_execute_operation_locally" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 903)
Function "_prepare_headless_message" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 903)
Function "_prepare_headless_message" uses parameter name "target" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 903)
Function "_prepare_headless_message" uses parameter name "message" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 951)
Function "_format_headless_result" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 951)
Function "_format_headless_result" uses parameter name "execution_result" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 978)
Function "_handle_headless_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 978)
Function "_handle_headless_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1073)
Function "_wrap_navigation_with_instructions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1077)
Function "_wrap_with_context_header" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1077)
Function "_wrap_with_context_header" uses parameter name "content" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1077)
Function "_wrap_with_context_header" uses parameter name "response_msg" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1133)
Function "_handle_dot_notation" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1133)
Function "_handle_dot_notation" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1261)
Function "_handle_action_shortcut" uses parameter name "args_str" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1322)
Function "_tokenize_cli_args" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1322)
Function "_tokenize_cli_args" uses parameter name "args_str" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1329)
Function "_convert_repl_scope_to_cli_format" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1329)
Function "_convert_repl_scope_to_cli_format" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1366)
Function "_execute_action_with_args" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1366)
Function "_execute_action_with_args" uses parameter name "operation" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1440)
Function "display_confirm_prompt" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1465)
Function "parse_command_parameters" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1479)
Function "parse_scope_from_string" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1479)
Function "parse_scope_from_string" uses parameter name "scope_str" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1488)
Function "get_stored_scope" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1498)
Function "_get_scope_display_lines" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1522)
Function "_find_scope_matches" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1522)
Function "_find_scope_matches" uses parameter name "scope_values" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1535)
Function "_search_for_scope_match" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1535)
Function "_search_for_scope_match" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1546)
Function "_search_sub_epics" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1557)
Function "_search_stories" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1557)
Function "_search_stories" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1569)
Function "_matches_name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1569)
Function "_matches_name" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1569)
Function "_matches_name" uses parameter name "pattern" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1572)
Function "_format_node_with_children" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1572)
Function "_format_node_with_children" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1572)
Function "_format_node_with_children" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1572)
Function "_format_node_with_children" uses parameter name "indent" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

Completed: 2025-12-30 03:00:01
Total violations: 130
Scanners executed: 30
