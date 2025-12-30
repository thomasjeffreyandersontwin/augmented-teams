# Validation Status - code
Started: 2025-12-29 17:32:13
Files: 274

## eliminate_duplication
**headless_session.py** - 1 violation(s)

[X] ERROR (line 79)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (invokes_action:79-94):
```python
result.blocked_operation = 'submit'
result.operations_executed = ['instructions', 'submit']
result.operations_status = {'instructions': 'completed', 'submit': 'blocked'}
```

Location (invokes_behavior:108-122):
```python
result.blocked_action = 'clarify'
result.actions_executed = ['clarify']
result.actions_status = {'clarify': 'blocked'}
```

---


## Cross-File Duplication Analysis
Scanning 8 changed file(s) against 274 total files...
Extracted 60 changed blocks, 4160 reference blocks
Starting 249,600 pairwise comparisons...
Comparing: 5% (12,480/249,600) - 0 violations - ETA: 82s  
Comparing: 10% (24,960/249,600) - 0 violations - ETA: 68s  
Comparing: 15% (37,440/249,600) - 0 violations - ETA: 67s  
Comparing: 20% (49,920/249,600) - 0 violations - ETA: 66s  
Comparing: 25% (62,400/249,600) - 0 violations - ETA: 66s  
Comparing: 30% (74,880/249,600) - 0 violations - ETA: 65s  
Comparing: 35% (87,360/249,600) - 0 violations - ETA: 64s  
Comparing: 40% (99,840/249,600) - 0 violations - ETA: 64s  
Comparing: 45% (112,320/249,600) - 0 violations - ETA: 59s  
Comparing: 50% (124,800/249,600) - 0 violations - ETA: 51s  
Comparing: 55% (137,280/249,600) - 0 violations - ETA: 45s  
Comparing: 60% (149,760/249,600) - 0 violations - ETA: 39s  
Comparing: 65% (162,240/249,600) - 0 violations - ETA: 34s  
Comparing: 70% (174,720/249,600) - 0 violations - ETA: 29s  
Comparing: 75% (187,200/249,600) - 0 violations - ETA: 24s  
Comparing: 80% (199,680/249,600) - 0 violations - ETA: 19s  
Comparing: 85% (212,160/249,600) - 0 violations - ETA: 14s  
Comparing: 90% (224,640/249,600) - 0 violations - ETA: 9s  
Comparing: 95% (237,120/249,600) - 0 violations - ETA: 4s  
Complete: 246666 comparisons, 0 violations

## keep_functions_small_focused
**execution_context.py** - 1 violation(s)

[!] WARNING (line 18)
Function "loads_from_context_file" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    
    @classmethod
    def loads_from_context_file(cls, path: Path) -> 'ExecutionContext':
        if not path.exists():
            return cls()
        
        content = path.read_text()
        
        user_message = ''
        chat_history = []
        file_references = []
        
        current_section = None
        for line in content.split('\n'):
            line_stripped = line.strip()
            
            if line_stripped.startswith('User Intent:'):
                current_section = 'user_message'
                user_message = line_stripped.replace('User Intent:', '').strip()
            elif line_stripped.startswith('Chat History:'):
                current_section = 'chat_history'
            elif line_stripped.startswith('File References:'):
                current_section = 'file_references'
            elif line_stripped.startswith('-') and current_section == 'chat_history':
                chat_history.append(line_stripped[1:].strip())
            elif line_stripped.startswith('-') and current_section == 'file_references':
                file_references.append(line_stripped[1:].strip())
        
        return cls(
            user_message=user_message,
            chat_history=chat_history,
            file_references=file_references
        )
    
```

---

## keep_functions_small_focused
**execution_result.py** - 1 violation(s)

[!] WARNING (line 7)
Function "__init__" is 57 lines - should be under 20 lines (extract complex logic to helper functions)

```python
class ExecutionResult:
    
    def __init__(
        self,
        status: str,
        log_path: Optional[Path] = None,
        session_id: Optional[str] = None,
        message: Optional[str] = None,
        action_completed: bool = False,
        behavior_completed: bool = False,
        context_loaded: bool = False,
        instructions: str = '',
        api_called: bool = False,
        completed: bool = False,
        loop_count: int = 0,
        looping: bool = False,
        operation: Optional[str] = None,
        behavior: Optional[str] = None,
        action: Optional[str] = None,
        context_included: bool = False,
        operations_executed: Optional[list] = None,
        operations_status: Optional[dict] = None,
        current_operation: Optional[str] = None,
        loop_responses: Optional[List[str]] = None,
        blocked: bool = False,
        blocked_operation: Optional[str] = None,
        blocked_action: Optional[str] = None,
        actions_executed: Optional[list] = None,
        block_reason: Optional[str] = None,
        exit_code: int = 0,
        actions_status: Optional[dict] = None
    ):
        self.status = status
        self.log_path = log_path
        self.session_id = session_id
        self.message = message
        self.action_completed = action_completed
        self.behavior_completed = behavior_completed
        self.context_loaded = context_loaded
        self.instructions = instructions
        self.api_called = api_called
        self.completed = completed
        self.loop_count = loop_count
        self.looping = looping
        self.operation = operation
        self.behavior = behavior
        self.action = action
        self.context_included = context_included
        self.operations_executed = operations_executed or []
        self.operations_status = operations_status or {}
    # ... (truncated)
```

---

## maintain_vertical_density
**execution_result.py** - 1 violation(s)

[i] INFO (line 7)
Function "__init__" is 57 lines - consider improving vertical density by declaring variables near usage

```python
class ExecutionResult:
    
    def __init__(
        self,
        status: str,
        log_path: Optional[Path] = None,
        session_id: Optional[str] = None,
        message: Optional[str] = None,
        action_completed: bool = False,
        behavior_completed: bool = False,
    # ... (truncated)
```

---

## maintain_vertical_density
**headless_session.py** - 1 violation(s)

[i] INFO (line 159)
Function "_execute_with_monitoring" is 59 lines - consider improving vertical density by declaring variables near usage

```python
        return final
    
    def _execute_with_monitoring(self, instructions: str, context_loaded: bool, should_block: bool = False) -> ExecutionResult:
        self.log.appends_response(f'Session {self.session_id} started')
        self.log.appends_response(f'Instructions: {instructions}')
        
        loop_count = 0
        max_loops = 10
        api_called = True
        loop_responses = []
    # ... (truncated)
```

---

## place_imports_at_top
**headless_session.py** - 1 violation(s)

[X] ERROR (line 227)
Import statement found after non-import code. Move all imports to the top of the file.

```python


from datetime import datetime

```

---

## provide_meaningful_context
**error_recovery.py** - 1 violation(s)

[!] WARNING (line 9)
Line 9 contains magic number - replace with named constant

```python
    
    def __init__(self, max_attempts: int = 3, current_attempts: int = 0, wait_time: float = 60.0):
        self.max_attempts = max_attempts
```

---

## simplify_control_flow
**execution_context.py** - 1 violation(s)

[!] WARNING (line 18)
Function "loads_from_context_file" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
    
    @classmethod
    def loads_from_context_file(cls, path: Path) -> 'ExecutionContext':
        if not path.exists():
            return cls()
        
        content = path.read_text()
        
        user_message = ''
        chat_history = []
        file_references = []
        
        current_section = None
        for line in content.split('\n'):
            line_stripped = line.strip()
    # ... (truncated)
```

---

## use_clear_function_parameters
**execution_result.py** - 1 violation(s)

[!] WARNING (line 7)
Function "__init__" has 28 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
class ExecutionResult:
    
    def __init__(
        self,
        status: str,
    # ... (truncated)
```

---

Completed: 2025-12-29 17:33:48
Total violations: 9
Scanners executed: 29
