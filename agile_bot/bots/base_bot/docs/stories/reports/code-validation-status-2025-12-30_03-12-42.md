# Validation Status - code
Started: 2025-12-30 03:12:42
Files: 275

## avoid_excessive_guards
**repl_session.py** - 1 violation(s)

[!] WARNING (line 1459)
Line 1459: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

```python
    def parse_command_parameters(self, args: str) -> Dict[str, Any]:
        params = {}
        if not args:
            return params
        
```

---

## avoid_unnecessary_parameter_passing
**cursor_api.py** - 4 violation(s)

[!] WARNING (line 129)
Internal method "_run_with_streaming" receives parameter "timeout" that matches instance attribute. Consider accessing via self.timeout instead.

[!] WARNING (line 267)
Internal method "_run_cursor_agent" receives parameter "timeout" that matches instance attribute. Consider accessing via self.timeout instead.

[!] WARNING (line 283)
Internal method "_run_via_wsl" receives parameter "timeout" that matches instance attribute. Consider accessing via self.timeout instead.

[!] WARNING (line 356)
Internal method "_run_directly" receives parameter "timeout" that matches instance attribute. Consider accessing via self.timeout instead.

---

## chain_dependencies_properly
**cursor_api.py** - 4 violation(s)

[!] WARNING (line 129)
Method "_run_with_streaming" in class "CursorHeadlessAPI" takes parameter "timeout" that is already injected in __init__. Use self.timeout instead.

```python
            raise RecoverableError('cursor-agent timed out')
    
    def _run_with_streaming(self, cmd: List[str], timeout: int) -> subprocess.CompletedProcess:
        """Run command with real-time streaming output."""
        import time
    # ... (truncated)
```

[!] WARNING (line 267)
Method "_run_cursor_agent" in class "CursorHeadlessAPI" takes parameter "timeout" that is already injected in __init__. Use self.timeout instead.

```python
                sys.stdout.flush()
    
    def _run_cursor_agent(self, prompt: str, timeout: int, resume_chat_id: Optional[str] = None) -> subprocess.CompletedProcess:
        """Run cursor-agent CLI command.
        
    # ... (truncated)
```

[!] WARNING (line 283)
Method "_run_via_wsl" in class "CursorHeadlessAPI" takes parameter "timeout" that is already injected in __init__. Use self.timeout instead.

```python
            return self._run_directly(prompt, timeout, resume_chat_id)
    
    def _run_via_wsl(self, prompt: str, timeout: int, resume_chat_id: Optional[str] = None) -> subprocess.CompletedProcess:
        import tempfile
        
    # ... (truncated)
```

[!] WARNING (line 356)
Method "_run_directly" in class "CursorHeadlessAPI" takes parameter "timeout" that is already injected in __init__. Use self.timeout instead.

```python
                    pass
    
    def _run_directly(self, prompt: str, timeout: int, resume_chat_id: Optional[str] = None) -> subprocess.CompletedProcess:
        if self.stream:
            cmd = ['cursor-agent', '--print', '--output-format', 'stream-json', '--stream-partial-output', '--force']
    # ... (truncated)
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
Scanning 2 changed file(s) against 20 total files...
Extracted 266 changed blocks, 740 reference blocks
Starting 196,840 pairwise comparisons...
Found 10 violations so far...
Found 20 violations so far...
Found 30 violations so far...
Found 40 violations so far...
Comparing: 5% (9,842/196,840) - 45 violations - ETA: 46s  
Found 50 violations so far...
Found 60 violations so far...
Found 70 violations so far...
Found 80 violations so far...
Found 90 violations so far...
Found 100 violations so far...
Found 110 violations so far...
Found 120 violations so far...
Found 130 violations so far...
Found 140 violations so far...
Comparing: 10% (19,684/196,840) - 143 violations - ETA: 45s  
Found 150 violations so far...
Found 160 violations so far...
Found 170 violations so far...
Found 180 violations so far...
Found 190 violations so far...
Found 200 violations so far...
Found 210 violations so far...
Found 220 violations so far...
Found 230 violations so far...
Found 240 violations so far...
Found 250 violations so far...
Found 260 violations so far...
Comparing: 15% (29,526/196,840) - 264 violations - ETA: 44s  
Found 270 violations so far...
Found 280 violations so far...
Found 290 violations so far...
Found 300 violations so far...
Found 310 violations so far...
Found 320 violations so far...
Found 330 violations so far...
Found 340 violations so far...
Found 350 violations so far...
Comparing: 20% (39,368/196,840) - 356 violations - ETA: 48s  
Found 360 violations so far...
Found 370 violations so far...
Found 380 violations so far...
Found 390 violations so far...
Comparing: 25% (49,210/196,840) - 390 violations - ETA: 46s  
Found 400 violations so far...
Found 410 violations so far...
Found 420 violations so far...
Found 430 violations so far...
Found 440 violations so far...
Found 450 violations so far...
Comparing: 30% (59,052/196,840) - 451 violations - ETA: 44s  
Found 460 violations so far...
Found 470 violations so far...
Found 480 violations so far...
Found 490 violations so far...
Found 500 violations so far...
Found 510 violations so far...
Comparing: 35% (68,894/196,840) - 513 violations - ETA: 41s  
Found 520 violations so far...
Found 530 violations so far...
Comparing: 40% (78,736/196,840) - 536 violations - ETA: 38s  
Comparing: 45% (88,578/196,840) - 536 violations - ETA: 35s  
Comparing: 50% (98,420/196,840) - 536 violations - ETA: 33s  
Comparing: 55% (108,262/196,840) - 536 violations - ETA: 31s  
Comparing: 60% (118,104/196,840) - 539 violations - ETA: 27s  
Found 540 violations so far...
Comparing: 65% (127,946/196,840) - 549 violations - ETA: 24s  
Complete: 131304 comparisons, 549 violations

## enforce_encapsulation
**repl_session.py** - 1 violation(s)

[!] WARNING (line 722)
Method "_handle_scope_command" in class "REPLSession" has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

---

## enforce_encapsulation
**cursor_api.py** - 1 violation(s)

[!] WARNING (line 333)
Method "_run_via_wsl" in class "CursorHeadlessAPI" has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

---

## keep_classes_small_with_single_responsibility
**repl_session.py** - 1 violation(s)

[!] WARNING (line 17)
Class "REPLSession" is 1578 lines - should be under 300 lines (extract related methods into separate classes)

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

## keep_classes_small_with_single_responsibility
**cursor_api.py** - 1 violation(s)

[!] WARNING (line 30)
Class "CursorHeadlessAPI" is 418 lines - should be under 300 lines (extract related methods into separate classes)

```python


class CursorHeadlessAPI:
    """Executes instructions via cursor-agent CLI command.
    
    Uses --print flag for non-interactive/headless execution.
    On Windows, runs cursor-agent through WSL Ubuntu.
    """
    
    def __init__(self, api_key: str = None, model: str = None, timeout: int = 600, workspace_path: Optional[Path] = None, stream: bool = True):
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

## keep_functions_small_focused
**cursor_api.py** - 1 violation(s)

[!] WARNING (line 57)
Function "starts_session" is 38 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return self._chat_id
    
    def starts_session(self, instructions: str) -> APIResponse:
        """Start a headless session by running cursor-agent with the instructions."""
        import uuid
        self._session_id = str(uuid.uuid4())[:8]
        
        print(f"[DEBUG] starts_session called, about to run cursor-agent")
        sys.stdout.flush()
        
        try:
            result = self._run_cursor_agent(instructions, timeout=self.timeout)
            
            print(f"[DEBUG] cursor-agent finished with returncode: {result.returncode}")
            sys.stdout.flush()
            
            if result.returncode != 0:
                error_msg = result.stderr.strip() if result.stderr else result.stdout.strip() or 'Unknown error'
                
                # Check for common errors
                if 'not found' in error_msg.lower() or 'not recognized' in error_msg.lower():
                    raise NonRecoverableError(
                        'cursor-agent not found. On Windows, install via WSL: '
                        'wsl -d Ubuntu -e bash -c "curl https://cursor.com/install -fsS | bash"'
                    )
                if 'unauthorized' in error_msg.lower() or 'authentication' in error_msg.lower():
                    raise NonRecoverableError(f'Authentication failed: {error_msg}')
                if 'rate limit' in error_msg.lower():
                    raise RecoverableError(f'Rate limited: {error_msg}')
                    
                raise RecoverableError(f'cursor-agent failed (exit {result.returncode}): {error_msg}')
            
            self._last_output = result.stdout
            response = self._parse_cursor_output(result.stdout)
            
            print(f"[DEBUG] _parse_cursor_output returned done={response.done}")
            sys.stdout.flush()
            
            # Extract chatId from response for session resumption
            # cursor-agent should return chatId in the response
            if response.session_id:
                self._chat_id = response.session_id
            
            return response
            
        except FileNotFoundError as e:
            raise NonRecoverableError(
                f'cursor-agent command not found: {e}. '
                'On Windows, install via WSL: wsl -d Ubuntu -e bash -c "curl https://cursor.com/install -fsS | bash"'
            )
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
Function "_handle_instructions_command" is 53 lines - consider improving vertical density by declaring variables near usage

```python
        )
    
    def _handle_instructions_command(self, args: str = "") -> REPLCommandResponse:
        """Handle instructions command"""
        if not self.has_current_action:
            return REPLCommandResponse(
                output="ERROR: No current action to get instructions for",
                response="ERROR: No current action",
                status="error"
            )
    # ... (truncated)
```

[i] INFO (line 624)
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

[i] INFO (line 698)
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

[i] INFO (line 839)
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

[i] INFO (line 1129)
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

[i] INFO (line 1257)
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

[i] INFO (line 1362)
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

## maintain_vertical_density
**cursor_api.py** - 3 violation(s)

[i] INFO (line 129)
Function "_run_with_streaming" is 61 lines - consider improving vertical density by declaring variables near usage

```python
            raise RecoverableError('cursor-agent timed out')
    
    def _run_with_streaming(self, cmd: List[str], timeout: int) -> subprocess.CompletedProcess:
        """Run command with real-time streaming output."""
        import time
        
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
    # ... (truncated)
```

[i] INFO (line 191)
Function "_print_cleaned_stream_line" is 75 lines - consider improving vertical density by declaring variables near usage

```python
            raise e
    
    def _print_cleaned_stream_line(self, line: str):
        """Parse JSON stream line and print only meaningful content."""
        line = line.strip()
        if not line:
            return
        
        try:
            data = json.loads(line)
    # ... (truncated)
```

[i] INFO (line 283)
Function "_run_via_wsl" is 72 lines - consider improving vertical density by declaring variables near usage

```python
            return self._run_directly(prompt, timeout, resume_chat_id)
    
    def _run_via_wsl(self, prompt: str, timeout: int, resume_chat_id: Optional[str] = None) -> subprocess.CompletedProcess:
        import tempfile
        
        temp_prompt_file = None
        temp_script_file = None
        
        try:
            if len(prompt) > 4000:
    # ... (truncated)
```

---

## never_swallow_exceptions
**repl_session.py** - 2 violation(s)

[X] ERROR (line 1126)
Except block only contains pass at line 1126 - exceptions must be logged or rethrown, never swallowed

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

## never_swallow_exceptions
**cursor_api.py** - 2 violation(s)

[X] ERROR (line 348)
Except block only contains pass at line 348 - exceptions must be logged or rethrown, never swallowed

```python
                try:
                    os.unlink(temp_prompt_file)
                except:
                    pass
            if temp_script_file:
```

[X] ERROR (line 353)
Except block only contains pass at line 353 - exceptions must be logged or rethrown, never swallowed

```python
                try:
                    os.unlink(temp_script_file)
                except:
                    pass
    
```

---

## refactor_completely_not_partially
**repl_session.py** - 3 violation(s)

[!] WARNING (line 72)
Fallback/legacy support code found (comment at line 72, code at line 73) - complete refactoring by removing old pattern support

[!] WARNING (line 239)
Fallback/legacy support code found (comment at line 239, code at line 240) - complete refactoring by removing old pattern support

[!] WARNING (line 1505)
Fallback/legacy support code found (comment at line 1505, code at line 1506) - complete refactoring by removing old pattern support

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

[!] WARNING (line 698)
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

[!] WARNING (line 839)
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

[!] WARNING (line 1129)
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

[!] WARNING (line 1325)
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

## simplify_control_flow
**cursor_api.py** - 2 violation(s)

[!] WARNING (line 129)
Function "_run_with_streaming" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
            raise RecoverableError('cursor-agent timed out')
    
    def _run_with_streaming(self, cmd: List[str], timeout: int) -> subprocess.CompletedProcess:
        """Run command with real-time streaming output."""
        import time
        
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',
            errors='replace',  # Replace invalid characters instead of crashing
            bufsize=1  # Line buffered
        )
    # ... (truncated)
```

[!] WARNING (line 191)
Function "_print_cleaned_stream_line" has nesting depth of 9 - use guard clauses and extract nested blocks to reduce nesting

```python
            raise e
    
    def _print_cleaned_stream_line(self, line: str):
        """Parse JSON stream line and print only meaningful content."""
        line = line.strip()
        if not line:
            return
        
        try:
            data = json.loads(line)
            msg_type = data.get('type', '')
            
            # Skip system init and thinking deltas
            if msg_type in ('system', 'user'):
                return
    # ... (truncated)
```

---

## stop_writing_useless_comments
**repl_session.py** - 29 violation(s)

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
        if not self.has_current_action:
```

[X] ERROR (line 604)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_submit_command(self, args: str = "") -> REPLCommandResponse:
        """Handle submit command"""
        if not self.has_current_action:
```

[X] ERROR (line 625)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_confirm_command(self) -> REPLCommandResponse:
        """Handle confirm command"""
        if not self.has_current_action:
```

[X] ERROR (line 680)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_path_command(self, args: str = "") -> REPLCommandResponse:
        """Handle path/workspace command"""
        if not args:
```

[X] ERROR (line 699)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_scope_command(self, args: str = "") -> REPLCommandResponse:
        """Handle scope command"""
        if not args:
```

[X] ERROR (line 765)
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

[X] ERROR (line 806)
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

[X] ERROR (line 840)
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

[X] ERROR (line 948)
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

[X] ERROR (line 975)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_headless_command(self, args: str = "") -> REPLCommandResponse:
        """Handle headless command - execute instruction in headless mode"""
        from agile_bot.bots.base_bot.src.repl_cli.headless.headless_session import HeadlessSession
```

[X] ERROR (line 1020)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_behavior_command(self, behavior_name: str) -> REPLCommandResponse:
        """Handle behavior navigation"""
        behavior = self.cli_bot.behaviors.domain_behaviors.find_by_name(behavior_name)
```

[X] ERROR (line 1049)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def navigate_to_behavior_action(self, behavior_name: str, action_name: str):
        """Navigate to a specific behavior and action
        
        Raises:
            ValueError: If behavior or action not found
        """
        # Navigate to behavior
```

[X] ERROR (line 1070)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _wrap_navigation_with_instructions(self) -> REPLCommandResponse:
        """After navigation, auto-execute instructions for new position"""
        return self._handle_instructions_command()
```

[X] ERROR (line 1074)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _wrap_with_context_header(self, content: str, response_msg: str) -> REPLCommandResponse:
        """Wrap content with instructions header and CLI status section"""
        formatter = self.formatter
```

[X] ERROR (line 1115)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _mark_behavior_complete(self, behavior_name: str) -> None:
        """Mark a behavior as complete in the state file"""
        state_file = self.workspace_directory / 'behavior_action_state.json'
```

[X] ERROR (line 1130)
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

[X] ERROR (line 754)
Useless comment: "# Get the scope display lines" - delete it or improve the code instead

```python
        result = self.cli_bot.set_scope(scope)
        
        # Get the scope display lines
        output = self.cli_bot.get_scope_display()
```

[X] ERROR (line 987)
Useless comment: "# Execute in headless mode" - delete it or improve the code instead

```python
        target, message = self._parse_headless_args(args)
        
        # Execute in headless mode
        try:
```

[X] ERROR (line 1001)
Useless comment: "# Execute in headless mode" - delete it or improve the code instead

```python
                final_message = message
            
            # Execute in headless mode
            execution_result = session.invokes(message=final_message, context_file=None)
```

[X] ERROR (line 1056)
Useless comment: "# Get the behavior" - delete it or improve the code instead

```python
        # Navigate to behavior
        self.cli_bot.behaviors.domain_behaviors.navigate_to(behavior_name)
        # Get the behavior
        behavior = self.cli_bot.behaviors.domain_behaviors.find_by_name(behavior_name)
```

---

## stop_writing_useless_comments
**cursor_api.py** - 7 violation(s)

[X] ERROR (line 31)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class CursorHeadlessAPI:
    """Executes instructions via cursor-agent CLI command.
    
    Uses --print flag for non-interactive/headless execution.
    On Windows, runs cursor-agent through WSL Ubuntu.
    """
    
```

[X] ERROR (line 54)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def chat_id(self) -> Optional[str]:
        """Return the cursor-agent chatId for session resumption."""
        return self._chat_id
```

[X] ERROR (line 58)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def starts_session(self, instructions: str) -> APIResponse:
        """Start a headless session by running cursor-agent with the instructions."""
        import uuid
```

[X] ERROR (line 109)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def resumes_session(self, prompt: str) -> APIResponse:
        """Resume an existing session with a new prompt.
        
        Requires a previous session to have been started with starts_session().
        """
        if not self._chat_id:
```

[X] ERROR (line 130)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _run_with_streaming(self, cmd: List[str], timeout: int) -> subprocess.CompletedProcess:
        """Run command with real-time streaming output."""
        import time
```

[X] ERROR (line 192)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _print_cleaned_stream_line(self, line: str):
        """Parse JSON stream line and print only meaningful content."""
        line = line.strip()
```

[X] ERROR (line 268)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _run_cursor_agent(self, prompt: str, timeout: int, resume_chat_id: Optional[str] = None) -> subprocess.CompletedProcess:
        """Run cursor-agent CLI command.
        
        On Windows, runs through WSL Ubuntu.
        Uses --print --output-format json for headless execution.
        
        Args:
            prompt: The prompt/message to send
            timeout: Execution timeout in seconds
            resume_chat_id: Optional chatId to resume an existing session
        """
        if self._is_windows:
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

[i] INFO (line 603)
Function "_handle_submit_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 603)
Function "_handle_submit_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 624)
Function "_handle_confirm_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 679)
Function "_handle_path_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 698)
Function "_handle_scope_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 698)
Function "_handle_scope_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 764)
Function "_validate_headless_ready" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 805)
Function "_parse_headless_args" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 805)
Function "_parse_headless_args" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 839)
Function "_execute_operation_locally" uses parameter name "target" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 839)
Function "_execute_operation_locally" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 900)
Function "_prepare_headless_message" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 900)
Function "_prepare_headless_message" uses parameter name "target" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 900)
Function "_prepare_headless_message" uses parameter name "message" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 947)
Function "_format_headless_result" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 947)
Function "_format_headless_result" uses parameter name "execution_result" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 974)
Function "_handle_headless_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 974)
Function "_handle_headless_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1069)
Function "_wrap_navigation_with_instructions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1073)
Function "_wrap_with_context_header" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1073)
Function "_wrap_with_context_header" uses parameter name "content" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1073)
Function "_wrap_with_context_header" uses parameter name "response_msg" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1129)
Function "_handle_dot_notation" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1129)
Function "_handle_dot_notation" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1257)
Function "_handle_action_shortcut" uses parameter name "args_str" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1318)
Function "_tokenize_cli_args" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1318)
Function "_tokenize_cli_args" uses parameter name "args_str" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1325)
Function "_convert_repl_scope_to_cli_format" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1325)
Function "_convert_repl_scope_to_cli_format" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1362)
Function "_execute_action_with_args" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1362)
Function "_execute_action_with_args" uses parameter name "operation" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1436)
Function "display_confirm_prompt" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1461)
Function "parse_command_parameters" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1475)
Function "parse_scope_from_string" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1475)
Function "parse_scope_from_string" uses parameter name "scope_str" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1484)
Function "get_stored_scope" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1494)
Function "_get_scope_display_lines" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1518)
Function "_find_scope_matches" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1518)
Function "_find_scope_matches" uses parameter name "scope_values" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1531)
Function "_search_for_scope_match" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1531)
Function "_search_for_scope_match" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1542)
Function "_search_sub_epics" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1553)
Function "_search_stories" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1553)
Function "_search_stories" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1565)
Function "_matches_name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1565)
Function "_matches_name" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1565)
Function "_matches_name" uses parameter name "pattern" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1568)
Function "_format_node_with_children" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1568)
Function "_format_node_with_children" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1568)
Function "_format_node_with_children" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1568)
Function "_format_node_with_children" uses parameter name "indent" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**cursor_api.py** - 35 violation(s)

[i] INFO (line 19)
Class "APIResponse" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 30)
Class "CursorHeadlessAPI" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 37)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 37)
Function "__init__" uses parameter name "api_key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 37)
Function "__init__" uses parameter name "model" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 37)
Function "__init__" uses parameter name "timeout" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 37)
Function "__init__" uses parameter name "stream" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 49)
Function "session_id" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 53)
Function "chat_id" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 57)
Function "starts_session" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 57)
Function "starts_session" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 108)
Function "resumes_session" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 108)
Function "resumes_session" uses parameter name "prompt" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 129)
Function "_run_with_streaming" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 129)
Function "_run_with_streaming" uses parameter name "cmd" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 129)
Function "_run_with_streaming" uses parameter name "timeout" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 191)
Function "_print_cleaned_stream_line" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 191)
Function "_print_cleaned_stream_line" uses parameter name "line" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 267)
Function "_run_cursor_agent" uses parameter name "prompt" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 267)
Function "_run_cursor_agent" uses parameter name "timeout" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 267)
Function "_run_cursor_agent" uses parameter name "resume_chat_id" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 283)
Function "_run_via_wsl" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 283)
Function "_run_via_wsl" uses parameter name "prompt" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 283)
Function "_run_via_wsl" uses parameter name "timeout" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 283)
Function "_run_via_wsl" uses parameter name "resume_chat_id" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 356)
Function "_run_directly" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 356)
Function "_run_directly" uses parameter name "prompt" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 356)
Function "_run_directly" uses parameter name "timeout" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 356)
Function "_run_directly" uses parameter name "resume_chat_id" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 391)
Function "sends_instruction" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 391)
Function "sends_instruction" uses parameter name "instruction" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 408)
Function "polls_session_status" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 424)
Function "terminates_session" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 428)
Function "_parse_cursor_output" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 428)
Function "_parse_cursor_output" uses parameter name "output" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

Completed: 2025-12-30 03:13:41
Total violations: 188
Scanners executed: 29
