# Validation Status - code
Started: 2025-12-30 03:09:17
Files: 275

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


## Cross-File Duplication Analysis
Scanning 1 changed file(s) against 20 total files...
Extracted 11 changed blocks, 615 reference blocks
Starting 6,765 pairwise comparisons...
Comparing: 5% (339/6,765) - 0 violations - ETA: 18s  
Comparing: 10% (677/6,765) - 0 violations - ETA: 8s  
Comparing: 15% (1,015/6,765) - 0 violations - ETA: 5s  
Comparing: 20% (1,353/6,765) - 0 violations - ETA: 4s  
Comparing: 25% (1,692/6,765) - 0 violations - ETA: 2s  
Comparing: 30% (2,030/6,765) - 0 violations - ETA: 2s  
Comparing: 35% (2,368/6,765) - 0 violations - ETA: 1s  
Comparing: 40% (2,706/6,765) - 0 violations - ETA: 1s  
Comparing: 45% (3,045/6,765) - 0 violations - ETA: 1s  
Comparing: 50% (3,383/6,765) - 0 violations - ETA: 0s  
Comparing: 55% (3,721/6,765) - 0 violations - ETA: 0s  
Comparing: 60% (4,059/6,765) - 0 violations - ETA: 0s  
Comparing: 65% (4,398/6,765) - 0 violations - ETA: 0s  
Comparing: 70% (4,736/6,765) - 0 violations - ETA: 0s  
Comparing: 75% (5,074/6,765) - 0 violations - ETA: 0s  
Comparing: 80% (5,412/6,765) - 0 violations - ETA: 0s  
Comparing: 85% (5,751/6,765) - 0 violations - ETA: 0s  
Comparing: 90% (6,089/6,765) - 0 violations - ETA: 0s  
Comparing: 95% (6,427/6,765) - 0 violations - ETA: 0s  
Complete: 6644 comparisons, 0 violations

## enforce_encapsulation
**cursor_api.py** - 1 violation(s)

[!] WARNING (line 298)
Method "_run_via_wsl" in class "CursorHeadlessAPI" has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

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

[i] INFO (line 193)
Function "_print_cleaned_stream_line" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 193)
Function "_print_cleaned_stream_line" uses parameter name "line" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 269)
Function "_run_cursor_agent" uses parameter name "prompt" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 269)
Function "_run_cursor_agent" uses parameter name "timeout" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 269)
Function "_run_cursor_agent" uses parameter name "resume_chat_id" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 285)
Function "_run_via_wsl" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 285)
Function "_run_via_wsl" uses parameter name "prompt" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 285)
Function "_run_via_wsl" uses parameter name "timeout" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 285)
Function "_run_via_wsl" uses parameter name "resume_chat_id" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 362)
Function "_run_directly" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 362)
Function "_run_directly" uses parameter name "prompt" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 362)
Function "_run_directly" uses parameter name "timeout" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 362)
Function "_run_directly" uses parameter name "resume_chat_id" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 398)
Function "sends_instruction" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 398)
Function "sends_instruction" uses parameter name "instruction" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 416)
Function "polls_session_status" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 433)
Function "terminates_session" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 438)
Function "_parse_cursor_output" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 438)
Function "_parse_cursor_output" uses parameter name "output" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

Completed: 2025-12-30 03:09:20
Total violations: 66
Scanners executed: 30
