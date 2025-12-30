# Validation Status - code
Started: 2025-12-30 02:37:02
Files: 275

## avoid_excessive_guards
**repl_session.py** - 1 violation(s)

[!] WARNING (line 1433)
Line 1433: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

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

[!] WARNING (line 269)
Internal method "_run_cursor_agent" receives parameter "timeout" that matches instance attribute. Consider accessing via self.timeout instead.

[!] WARNING (line 285)
Internal method "_run_via_wsl" receives parameter "timeout" that matches instance attribute. Consider accessing via self.timeout instead.

[!] WARNING (line 362)
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

[!] WARNING (line 269)
Method "_run_cursor_agent" in class "CursorHeadlessAPI" takes parameter "timeout" that is already injected in __init__. Use self.timeout instead.

```python
                sys.stdout.flush()
    
    def _run_cursor_agent(self, prompt: str, timeout: int, resume_chat_id: Optional[str] = None) -> subprocess.CompletedProcess:
        """Run cursor-agent CLI command.
        
    # ... (truncated)
```

[!] WARNING (line 285)
Method "_run_via_wsl" in class "CursorHeadlessAPI" takes parameter "timeout" that is already injected in __init__. Use self.timeout instead.

```python
            return self._run_directly(prompt, timeout, resume_chat_id)
    
    def _run_via_wsl(self, prompt: str, timeout: int, resume_chat_id: Optional[str] = None) -> subprocess.CompletedProcess:
        """Run cursor-agent via WSL Ubuntu on Windows."""
        import tempfile
    # ... (truncated)
```

[!] WARNING (line 362)
Method "_run_directly" in class "CursorHeadlessAPI" takes parameter "timeout" that is already injected in __init__. Use self.timeout instead.

```python
                    pass
    
    def _run_directly(self, prompt: str, timeout: int, resume_chat_id: Optional[str] = None) -> subprocess.CompletedProcess:
        """Run cursor-agent directly on Linux/Mac."""
        if self.stream:
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
Scanning 2 changed file(s) against 275 total files...
Extracted 267 changed blocks, 4289 reference blocks
Starting 1,145,163 pairwise comparisons...
Comparing: 2% (32,037/1,145,163) - 0 violations - ETA: 347s  
Comparing: 5% (58,467/1,145,163) - 0 violations - ETA: 371s  
Comparing: 8% (101,543/1,145,163) - 0 violations - ETA: 308s  
Comparing: 10% (124,471/1,145,163) - 0 violations - ETA: 328s  
Comparing: 14% (162,351/1,145,163) - 0 violations - ETA: 302s  
Comparing: 16% (185,910/1,145,163) - 0 violations - ETA: 309s  
Comparing: 19% (218,938/1,145,163) - 0 violations - ETA: 296s  
Comparing: 21% (249,007/1,145,163) - 0 violations - ETA: 287s  
Comparing: 24% (281,389/1,145,163) - 0 violations - ETA: 276s  
Comparing: 26% (299,119/1,145,163) - 0 violations - ETA: 282s  
Comparing: 28% (328,654/1,145,163) - 0 violations - ETA: 273s  
Comparing: 30% (353,615/1,145,163) - 0 violations - ETA: 268s  
Comparing: 33% (380,979/1,145,163) - 0 violations - ETA: 260s  
Comparing: 34% (398,585/1,145,163) - 0 violations - ETA: 262s  
Comparing: 37% (425,434/1,145,163) - 0 violations - ETA: 253s  
Comparing: 38% (446,473/1,145,163) - 0 violations - ETA: 250s  
Comparing: 40% (469,291/1,145,163) - 0 violations - ETA: 244s  
Comparing: 42% (485,437/1,145,163) - 0 violations - ETA: 244s  
Comparing: 44% (507,793/1,145,163) - 0 violations - ETA: 238s  
Comparing: 46% (526,872/1,145,163) - 0 violations - ETA: 234s  
Comparing: 47% (546,164/1,145,163) - 0 violations - ETA: 230s  
Comparing: 48% (560,969/1,145,163) - 0 violations - ETA: 229s  
Comparing: 50% (580,842/1,145,163) - 0 violations - ETA: 223s  
Comparing: 52% (597,735/1,145,163) - 0 violations - ETA: 219s  
Comparing: 53% (614,584/1,145,163) - 0 violations - ETA: 215s  
Comparing: 55% (635,090/1,145,163) - 0 violations - ETA: 208s  
Comparing: 56% (650,274/1,145,163) - 0 violations - ETA: 205s  
Comparing: 58% (669,589/1,145,163) - 0 violations - ETA: 198s  
Comparing: 60% (688,757/1,145,163) - 0 violations - ETA: 192s  
Comparing: 61% (705,249/1,145,163) - 0 violations - ETA: 187s  
Comparing: 62% (718,715/1,145,163) - 0 violations - ETA: 183s  
Comparing: 64% (734,344/1,145,163) - 0 violations - ETA: 179s  
Comparing: 65% (751,320/1,145,163) - 0 violations - ETA: 172s  
Comparing: 66% (766,584/1,145,163) - 0 violations - ETA: 167s  
Comparing: 67% (778,239/1,145,163) - 0 violations - ETA: 165s  
Comparing: 68% (789,815/1,145,163) - 0 violations - ETA: 161s  
Comparing: 70% (804,000/1,145,163) - 0 violations - ETA: 157s  
Comparing: 71% (818,099/1,145,163) - 0 violations - ETA: 151s  
Comparing: 72% (829,744/1,145,163) - 0 violations - ETA: 148s  
Comparing: 73% (841,848/1,145,163) - 0 violations - ETA: 144s  
Comparing: 74% (857,813/1,145,163) - 0 violations - ETA: 137s  
Comparing: 76% (873,287/1,145,163) - 0 violations - ETA: 130s  
Comparing: 77% (888,715/1,145,163) - 0 violations - ETA: 124s  
Comparing: 79% (914,275/1,145,163) - 0 violations - ETA: 111s  
Comparing: 82% (944,873/1,145,163) - 1 violations - ETA: 95s  
Comparing: 83% (961,212/1,145,163) - 1 violations - ETA: 88s  
Comparing: 85% (979,292/1,145,163) - 2 violations - ETA: 79s  
Comparing: 87% (1,004,988/1,145,163) - 9 violations - ETA: 66s  
Found 10 violations so far...
Comparing: 89% (1,022,854/1,145,163) - 13 violations - ETA: 58s  
Comparing: 91% (1,047,853/1,145,163) - 13 violations - ETA: 46s  
Complete: 1079506 comparisons, 13 violations

## enforce_encapsulation
**repl_session.py** - 1 violation(s)

[!] WARNING (line 722)
Method "_handle_scope_command" in class "REPLSession" has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

---

## enforce_encapsulation
**cursor_api.py** - 1 violation(s)

[!] WARNING (line 298)
Method "_run_via_wsl" in class "CursorHeadlessAPI" has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

---

## keep_classes_small_with_single_responsibility
**repl_session.py** - 1 violation(s)

[!] WARNING (line 17)
Class "REPLSession" is 1562 lines - should be under 300 lines (extract related methods into separate classes)

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
Class "CursorHeadlessAPI" is 433 lines - should be under 300 lines (extract related methods into separate classes)

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
Function "_execute_operation_locally" is 80 lines - consider improving vertical density by declaring variables near usage

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

[i] INFO (line 1150)
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

[i] INFO (line 1278)
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

[i] INFO (line 1346)
Function "_execute_action_with_args" is 73 lines - consider improving vertical density by declaring variables near usage

```python
            return args_str.split()
    
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
Function "_run_with_streaming" is 63 lines - consider improving vertical density by declaring variables near usage

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

[i] INFO (line 193)
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

[i] INFO (line 285)
Function "_run_via_wsl" is 76 lines - consider improving vertical density by declaring variables near usage

```python
            return self._run_directly(prompt, timeout, resume_chat_id)
    
    def _run_via_wsl(self, prompt: str, timeout: int, resume_chat_id: Optional[str] = None) -> subprocess.CompletedProcess:
        """Run cursor-agent via WSL Ubuntu on Windows."""
        import tempfile
        
        # For very long prompts (> 4000 chars), write to temp file to avoid Windows command line length limits
        temp_file_path = None
        if len(prompt) > 4000:
            # Create temp file
    # ... (truncated)
```

---

## never_swallow_exceptions
**repl_session.py** - 2 violation(s)

[X] ERROR (line 1147)
Except block only contains pass at line 1147 - exceptions must be logged or rethrown, never swallowed

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
**cursor_api.py** - 1 violation(s)

[X] ERROR (line 359)
Except block only contains pass at line 359 - exceptions must be logged or rethrown, never swallowed

```python
                try:
                    os.unlink(temp_file_path)
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

[!] WARNING (line 1489)
Fallback/legacy support code found (comment at line 1489, code at line 1490) - complete refactoring by removing old pattern support

---

## simplify_control_flow
**repl_session.py** - 4 violation(s)

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

[!] WARNING (line 1150)
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

[!] WARNING (line 193)
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

[X] ERROR (line 921)
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

[X] ERROR (line 969)
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

[X] ERROR (line 996)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_headless_command(self, args: str = "") -> REPLCommandResponse:
        """Handle headless command - execute instruction in headless mode"""
        from agile_bot.bots.base_bot.src.repl_cli.headless.headless_session import HeadlessSession
```

[X] ERROR (line 1041)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_behavior_command(self, behavior_name: str) -> REPLCommandResponse:
        """Handle behavior navigation"""
        behavior = self.cli_bot.behaviors.domain_behaviors.find_by_name(behavior_name)
```

[X] ERROR (line 1070)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def navigate_to_behavior_action(self, behavior_name: str, action_name: str):
        """Navigate to a specific behavior and action
        
        Raises:
            ValueError: If behavior or action not found
        """
        # Navigate to behavior
```

[X] ERROR (line 1091)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _wrap_navigation_with_instructions(self) -> REPLCommandResponse:
        """After navigation, auto-execute instructions for new position"""
        return self._handle_instructions_command()
```

[X] ERROR (line 1095)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _wrap_with_context_header(self, content: str, response_msg: str) -> REPLCommandResponse:
        """Wrap content with instructions header and CLI status section"""
        formatter = self.formatter
```

[X] ERROR (line 1136)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _mark_behavior_complete(self, behavior_name: str) -> None:
        """Mark a behavior as complete in the state file"""
        state_file = self.workspace_directory / 'behavior_action_state.json'
```

[X] ERROR (line 1151)
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

[X] ERROR (line 955)
Useless comment: "# Execute the target operation locally to get output" - delete it or improve the code instead

```python
            cli_args = ' '.join(cli_args_parts)
            
            # Execute the target operation locally to get output
            operation_output = self._execute_operation_locally(target, cli_args)
```

[X] ERROR (line 1008)
Useless comment: "# Execute in headless mode" - delete it or improve the code instead

```python
        target, message = self._parse_headless_args(args)
        
        # Execute in headless mode
        try:
```

[X] ERROR (line 1022)
Useless comment: "# Execute in headless mode" - delete it or improve the code instead

```python
                final_message = message
            
            # Execute in headless mode
            execution_result = session.invokes(message=final_message, context_file=None)
```

[X] ERROR (line 1077)
Useless comment: "# Get the behavior" - delete it or improve the code instead

```python
        # Navigate to behavior
        self.cli_bot.behaviors.domain_behaviors.navigate_to(behavior_name)
        # Get the behavior
        behavior = self.cli_bot.behaviors.domain_behaviors.find_by_name(behavior_name)
```

---

## stop_writing_useless_comments
**cursor_api.py** - 14 violation(s)

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

[X] ERROR (line 194)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _print_cleaned_stream_line(self, line: str):
        """Parse JSON stream line and print only meaningful content."""
        line = line.strip()
```

[X] ERROR (line 270)
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

[X] ERROR (line 286)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _run_via_wsl(self, prompt: str, timeout: int, resume_chat_id: Optional[str] = None) -> subprocess.CompletedProcess:
        """Run cursor-agent via WSL Ubuntu on Windows."""
        import tempfile
```

[X] ERROR (line 363)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _run_directly(self, prompt: str, timeout: int, resume_chat_id: Optional[str] = None) -> subprocess.CompletedProcess:
        """Run cursor-agent directly on Linux/Mac."""
        if self.stream:
```

[X] ERROR (line 399)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def sends_instruction(self, instruction: str) -> APIResponse:
        """Send additional instruction (runs new cursor-agent call)."""
        if not self._session_id:
```

[X] ERROR (line 417)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def polls_session_status(self) -> APIResponse:
        """Poll session status - for cursor-agent, it's synchronous so always done."""
        if not self._session_id:
```

[X] ERROR (line 434)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def terminates_session(self) -> None:
        """Terminate session (cleanup)."""
        self._session_id = None
```

[X] ERROR (line 439)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _parse_cursor_output(self, output: str) -> APIResponse:
        """Parse cursor-agent output.
        
        Since cursor-agent is synchronous and we use --output-format stream-json,
        by the time this is called the process has completed. Just return done=True.
        """
        if not output or not output.strip():
```

[X] ERROR (line 181)
Useless comment: "# Create CompletedProcess object" - delete it or improve the code instead

```python
                stderr_lines.append(stderr_output)
            
            # Create CompletedProcess object
            return subprocess.CompletedProcess(
```

---

Completed: 2025-12-30 02:45:46
Total violations: 87
Scanners executed: 30
