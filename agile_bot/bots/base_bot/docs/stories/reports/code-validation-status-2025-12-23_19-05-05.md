# Validation Status - code
Started: 2025-12-23 19:05:05
Files: 3

## chain_dependencies_properly
**repl_session.py** - 20 violation(s)

[!] WARNING (line 163)
Passing self.current_behavior as parameter to _find_action(). Access it directly in the method through self.current_behavior instead.

```python
        return REPLCommandResponse(output=output, response=f"ERROR: action '{action_name}' not found", status="error")
    
    def _validate_current_behavior_and_action(self, action_name: str) -> Optional[REPLCommandResponse]:
        if not self.has_current_behavior:
```

[!] WARNING (line 173)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return None
    
    def _move_to_next_behavior_first_action(self, next_behavior_index: int, mark_current_complete: bool = False) -> REPLCommandResponse:
        behaviors = list(self.bot.behaviors)
```

[!] WARNING (line 194)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return self._execute_action_instructions(next_first_action.action_name)
    
    def _advance_to_action_in_current_behavior(self, next_action) -> REPLCommandResponse:
        self.current_state['current_action'] = f"{self.current_behavior_state}.{next_action.action_name}"
```

[!] WARNING (line 280)
Passing self.current_behavior as parameter to _format_action_status_list(). Access it directly in the method through self.current_behavior instead.

```python
        )
    
    def _render_full_status(self) -> List[str]:
        output_lines = [f"Progress: {self.progress_path}.{self.stage_name}"]
```

[!] WARNING (line 566)
Passing self.current_behavior_name as parameter to _update_state_and_generate_response(). Access it directly in the method through self.current_behavior_name instead.

```python
        self._save_state(state_data)
    
    def _handle_action_command(self, action_name: str) -> REPLCommandResponse:
        action_name = action_name.strip()
```

[!] WARNING (line 584)
Passing self.current_behavior_name as parameter to _render_action_parameters(). Access it directly in the method through self.current_behavior_name instead.

```python
        return None
    
    def _handle_help_command(self, args: str) -> REPLCommandResponse:
        args = args.strip()
```

[!] WARNING (line 720)
Passing self.current_action_name as parameter to _execute_action_instructions(). Access it directly in the method through self.current_action_name instead.

```python
        return self._handle_instructions_command()
    
    def _handle_instructions_command(self) -> REPLCommandResponse:
        if not self.has_current_action:
```

[!] WARNING (line 752)
Passing self.current_action_name as parameter to _find_action_index(). Access it directly in the method through self.current_action_name instead.

```python
        return REPLCommandResponse(output=output, response=output, status="success", action=self.current_action_name)
    
    def _handle_confirm_command(self) -> REPLCommandResponse:
        if not self.has_current_action:
```

[!] WARNING (line 752)
Passing self.current_behavior_name as parameter to _error_behavior_not_found(). Access it directly in the method through self.current_behavior_name instead.

```python
        return REPLCommandResponse(output=output, response=output, status="success", action=self.current_action_name)
    
    def _handle_confirm_command(self) -> REPLCommandResponse:
        if not self.has_current_action:
```

[!] WARNING (line 779)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        self.current_state['completed_actions'] = completed_actions
    
    def _advance_to_next_behavior(self) -> REPLCommandResponse:
        behavior_name = self.current_behavior_name
```

[!] WARNING (line 779)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        self.current_state['completed_actions'] = completed_actions
    
    def _advance_to_next_behavior(self) -> REPLCommandResponse:
        behavior_name = self.current_behavior_name
```

[!] WARNING (line 814)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return self._execute_action_instructions(next_first_action.action_name)
    
    def _advance_to_next_action(self, behavior, current_index: int) -> REPLCommandResponse:
        actions = list(behavior.actions)
```

[!] WARNING (line 835)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return self._go_back_within_behavior(completed_actions)
    
    def _go_back_to_previous_behavior(self) -> REPLCommandResponse:
        completed_behaviors = list(self.completed_behaviors)
```

[!] WARNING (line 874)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return self._execute_action_instructions(last_action.action_name)
    
    def _go_back_within_behavior(self, completed_actions: List[Dict]) -> REPLCommandResponse:
        last_completed = completed_actions.pop()
```

[!] WARNING (line 885)
Passing self.current_action_name as parameter to _find_action_index(). Access it directly in the method through self.current_action_name instead.

```python
        return self._execute_action_instructions(new_action_state.split('.')[-1])
    
    def _handle_next_command(self) -> REPLCommandResponse:
        if not self.has_current_action:
```

[!] WARNING (line 885)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return self._execute_action_instructions(new_action_state.split('.')[-1])
    
    def _handle_next_command(self) -> REPLCommandResponse:
        if not self.has_current_action:
```

[!] WARNING (line 885)
Passing self.current_behavior_name as parameter to _error_behavior_not_found(). Access it directly in the method through self.current_behavior_name instead.

```python
        return self._execute_action_instructions(new_action_state.split('.')[-1])
    
    def _handle_next_command(self) -> REPLCommandResponse:
        if not self.has_current_action:
```

[!] WARNING (line 917)
Passing self.current_behavior_name as parameter to _find_behavior_index(). Access it directly in the method through self.current_behavior_name instead.

```python
        return self._execute_action_instructions(next_action.action_name)
    
    def _next_to_new_behavior(self) -> REPLCommandResponse:
        current_behavior_index = self._find_behavior_index(self.current_behavior_name)
```

[!] WARNING (line 917)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return self._execute_action_instructions(next_action.action_name)
    
    def _next_to_new_behavior(self) -> REPLCommandResponse:
        current_behavior_index = self._find_behavior_index(self.current_behavior_name)
```

[!] WARNING (line 1105)
Passing self.current_behavior_name as parameter to _navigate_to_action(). Access it directly in the method through self.current_behavior_name instead.

```python
        )
    
    def _validate_and_navigate_to_action(self, action_name: str) -> Optional[REPLCommandResponse]:
        error = self._validate_current_behavior_and_action(action_name)
```

---

## eliminate_duplication
**repl_session.py** - 5 violation(s)

[X] ERROR (line 185)
Duplicate code blocks detected (3 locations) - extract to helper function.

Location (_move_to_next_behavior_first_action:185-192):
```python
self.current_state['current_behavior'] = self._build_full_behavior_path(next_behavior.name)
self.current_state['current_action'] = self._build_full_action_path(next_behavior.name, next_first_action.ac...
```

Location (_advance_to_next_behavior:803-810):
```python
next_behavior = behaviors[current_behavior_index + 1]
next_first_action = next_behavior.actions._actions[0]
self.current_state['current_behavior'] = self._build_full_behavior_path(next_behavior.name)
...
```

Location (_next_to_new_behavior:936-944):
```python
next_behavior = behaviors[current_behavior_index + 1]
next_first_action = next_behavior.actions._actions[0]
self.current_state['current_behavior'] = self._build_full_behavior_path(next_behavior.name)
...
```

[X] ERROR (line 186)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_move_to_next_behavior_first_action:186-190):
```python
self.current_state['current_action'] = self._build_full_action_path(next_behavior.name, next_first_action.action_name)
self.current_state['action_phase'] = 'not_started'
self.current_state['completed_...
```

Location (_next_to_new_behavior:940-944):
```python
self.current_state['current_action'] = self._build_full_action_path(next_behavior.name, next_first_action.action_name)
self.current_state['action_phase'] = 'not_started'
self.current_state['completed_...
```

[X] ERROR (line 187)
Duplicate code blocks detected (3 locations) - extract to helper function.

Location (_move_to_next_behavior_first_action:187-192):
```python
self.current_state['action_phase'] = 'not_started'
self.current_state['completed_actions'] = []
self.current_state['completed_behaviors'] = completed_behaviors
self._save_state(self.current_state)
ret...
```

Location (_go_back_to_previous_behavior:867-872):
```python
self.current_state['action_phase'] = 'not_started'
self.current_state['completed_actions'] = new_completed_actions
self.current_state['completed_behaviors'] = completed_behaviors
self._save_state(self...
```

Location (_next_to_new_behavior:941-946):
```python
self.current_state['action_phase'] = 'not_started'
self.current_state['completed_actions'] = []
self.current_state['completed_behaviors'] = completed_behaviors
self._save_state(self.current_state)
ret...
```

[X] ERROR (line 803)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_advance_to_next_behavior:803-812):
```python
next_behavior = behaviors[current_behavior_index + 1]
next_first_action = next_behavior.actions._actions[0]
self.current_state['current_behavior'] = self._build_full_behavior_path(next_behavior.name)
...
```

Location (_next_to_new_behavior:936-946):
```python
next_behavior = behaviors[current_behavior_index + 1]
next_first_action = next_behavior.actions._actions[0]
self.current_state['current_behavior'] = self._build_full_behavior_path(next_behavior.name)
...
```

[X] ERROR (line 815)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_advance_to_next_action:815-822):
```python
actions = list(behavior.actions)
next_action = actions[current_index + 1]
self.current_state['current_action'] = f'{self.current_behavior_state}.{next_action.action_name}'
self.current_state['action_p...
```

Location (_handle_next_command:908-915):
```python
self._mark_current_action_complete()
next_action = actions[current_index + 1]
self.current_state['current_action'] = f'{self.current_behavior_state}.{next_action.action_name}'
self.current_state['acti...
```

---


## Cross-File Duplication Analysis
Scanning 3 files...
Extracted 395 code blocks
Starting 77815 pairwise comparisons...
Comparing: 5% (3,891/77,815) - 0 violations - ETA: 18s  
Comparing: 10% (7,782/77,815) - 0 violations - ETA: 14s  
Comparing: 15% (11,673/77,815) - 0 violations - ETA: 14s  
Comparing: 20% (15,563/77,815) - 0 violations - ETA: 14s  
Comparing: 25% (19,454/77,815) - 0 violations - ETA: 12s  
Comparing: 30% (23,345/77,815) - 0 violations - ETA: 10s  
Comparing: 35% (27,236/77,815) - 0 violations - ETA: 8s  
Comparing: 40% (31,126/77,815) - 0 violations - ETA: 6s  
Comparing: 45% (35,017/77,815) - 0 violations - ETA: 5s  
Comparing: 50% (38,908/77,815) - 0 violations - ETA: 4s  
Comparing: 55% (42,799/77,815) - 0 violations - ETA: 3s  
Comparing: 60% (46,689/77,815) - 0 violations - ETA: 2s  
Comparing: 65% (50,580/77,815) - 0 violations - ETA: 2s  
Comparing: 70% (54,471/77,815) - 0 violations - ETA: 1s  
Comparing: 75% (58,362/77,815) - 0 violations - ETA: 1s  
Comparing: 80% (62,252/77,815) - 0 violations - ETA: 1s  
Comparing: 85% (66,143/77,815) - 0 violations - ETA: 0s  
Comparing: 90% (70,034/77,815) - 0 violations - ETA: 0s  
Comparing: 95% (73,925/77,815) - 0 violations - ETA: 0s  
Comparing: 100% (77,815/77,815) - 0 violations - ETA: 0s  
Complete: 77815 comparisons, 0 violations

## keep_classes_small_with_single_responsibility
**repl_session.py** - 1 violation(s)

[!] WARNING (line 14)
Class "REPLSession" is 1098 lines - should be under 300 lines (extract related methods into separate classes)

```python


class REPLSession:
    STAGE_MAP = {
        'not_started': 'instructions',
        'instructions_given': 'instructions',
        'submitted': 'submitted'
    }
    
    def __init__(self, bot, workspace_directory: Path):
    # ... (truncated)
```

---

## stop_writing_useless_comments
**repl_session.py** - 2 violation(s)

[X] ERROR (line 522)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _navigate_to_action(self, behavior_name: str, action_name: str, full_action: str, state_updates: Dict = None):
        """Navigate to an action without executing. Updates state only."""
        state_data = dict(self.current_state) if self.current_state else {}
```

[X] ERROR (line 545)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _update_state_and_generate_response(self, behavior_name: str, action_name: str, full_action: str, state_updates: Dict = None) -> REPLCommandResponse:
        """Navigate to an action and execute instructions operation."""
        self._navigate_to_action(behavior_name, action_name, full_action, state_updates)
```

---

Completed: 2025-12-23 19:05:34
Total violations: 28
Scanners executed: 30
