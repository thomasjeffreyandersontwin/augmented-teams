# Validation Status - code
Started: 2025-12-23 19:12:24
Files: 5

## chain_dependencies_properly
**repl_session.py** - 19 violation(s)

[!] WARNING (line 167)
Passing self.current_behavior as parameter to _find_action(). Access it directly in the method through self.current_behavior instead.

```python
        return REPLCommandResponse(output=output, response=f"ERROR: action '{action_name}' not found", status="error")
    
    def _validate_current_behavior_and_action(self, action_name: str) -> Optional[REPLCommandResponse]:
        if not self.has_current_behavior:
```

[!] WARNING (line 177)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return None
    
    def _move_to_next_behavior_first_action(self, next_behavior_index: int, mark_current_complete: bool = False) -> REPLCommandResponse:
        behaviors = list(self.bot.behaviors)
```

[!] WARNING (line 198)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return self._execute_action_instructions(next_first_action.action_name)
    
    def _advance_to_action_in_current_behavior(self, next_action) -> REPLCommandResponse:
        self.current_state['current_action'] = f"{self.current_behavior_state}.{next_action.action_name}"
```

[!] WARNING (line 494)
Passing self.current_behavior_name as parameter to _update_state_and_generate_response(). Access it directly in the method through self.current_behavior_name instead.

```python
        self._save_state(state_data)
    
    def _handle_action_command(self, action_name: str) -> REPLCommandResponse:
        action_name = action_name.strip()
```

[!] WARNING (line 512)
Passing self.current_behavior_name as parameter to _render_action_parameters(). Access it directly in the method through self.current_behavior_name instead.

```python
        return None
    
    def _handle_help_command(self, args: str) -> REPLCommandResponse:
        args = args.strip()
```

[!] WARNING (line 560)
Passing self.current_action_name as parameter to _execute_action_instructions(). Access it directly in the method through self.current_action_name instead.

```python
        return self._handle_instructions_command()
    
    def _handle_instructions_command(self) -> REPLCommandResponse:
        if not self.has_current_action:
```

[!] WARNING (line 592)
Passing self.current_action_name as parameter to _find_action_index(). Access it directly in the method through self.current_action_name instead.

```python
        return REPLCommandResponse(output=output, response=output, status="success", action=self.current_action_name)
    
    def _handle_confirm_command(self) -> REPLCommandResponse:
        if not self.has_current_action:
```

[!] WARNING (line 592)
Passing self.current_behavior_name as parameter to _error_behavior_not_found(). Access it directly in the method through self.current_behavior_name instead.

```python
        return REPLCommandResponse(output=output, response=output, status="success", action=self.current_action_name)
    
    def _handle_confirm_command(self) -> REPLCommandResponse:
        if not self.has_current_action:
```

[!] WARNING (line 619)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        self.current_state['completed_actions'] = completed_actions
    
    def _advance_to_next_behavior(self) -> REPLCommandResponse:
        behavior_name = self.current_behavior_name
```

[!] WARNING (line 619)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        self.current_state['completed_actions'] = completed_actions
    
    def _advance_to_next_behavior(self) -> REPLCommandResponse:
        behavior_name = self.current_behavior_name
```

[!] WARNING (line 654)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return self._execute_action_instructions(next_first_action.action_name)
    
    def _advance_to_next_action(self, behavior, current_index: int) -> REPLCommandResponse:
        actions = list(behavior.actions)
```

[!] WARNING (line 675)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return self._go_back_within_behavior(completed_actions)
    
    def _go_back_to_previous_behavior(self) -> REPLCommandResponse:
        completed_behaviors = list(self.completed_behaviors)
```

[!] WARNING (line 714)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return self._execute_action_instructions(last_action.action_name)
    
    def _go_back_within_behavior(self, completed_actions: List[Dict]) -> REPLCommandResponse:
        last_completed = completed_actions.pop()
```

[!] WARNING (line 725)
Passing self.current_action_name as parameter to _find_action_index(). Access it directly in the method through self.current_action_name instead.

```python
        return self._execute_action_instructions(new_action_state.split('.')[-1])
    
    def _handle_next_command(self) -> REPLCommandResponse:
        if not self.has_current_action:
```

[!] WARNING (line 725)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return self._execute_action_instructions(new_action_state.split('.')[-1])
    
    def _handle_next_command(self) -> REPLCommandResponse:
        if not self.has_current_action:
```

[!] WARNING (line 725)
Passing self.current_behavior_name as parameter to _error_behavior_not_found(). Access it directly in the method through self.current_behavior_name instead.

```python
        return self._execute_action_instructions(new_action_state.split('.')[-1])
    
    def _handle_next_command(self) -> REPLCommandResponse:
        if not self.has_current_action:
```

[!] WARNING (line 757)
Passing self.current_behavior_name as parameter to _find_behavior_index(). Access it directly in the method through self.current_behavior_name instead.

```python
        return self._execute_action_instructions(next_action.action_name)
    
    def _next_to_new_behavior(self) -> REPLCommandResponse:
        current_behavior_index = self._find_behavior_index(self.current_behavior_name)
```

[!] WARNING (line 757)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return self._execute_action_instructions(next_action.action_name)
    
    def _next_to_new_behavior(self) -> REPLCommandResponse:
        current_behavior_index = self._find_behavior_index(self.current_behavior_name)
```

[!] WARNING (line 945)
Passing self.current_behavior_name as parameter to _navigate_to_action(). Access it directly in the method through self.current_behavior_name instead.

```python
        )
    
    def _validate_and_navigate_to_action(self, action_name: str) -> Optional[REPLCommandResponse]:
        error = self._validate_current_behavior_and_action(action_name)
```

---

## delegate_to_lowest_level
**repl_help.py** - 2 violation(s)

[i] INFO (line 52)
Method "help_text" in class "ActionHelp" iterates through "parameters" instead of delegating to collection class. Delegate to collection class instead.

[i] INFO (line 74)
Method "actions_list" in class "BehaviorHelp" iterates through "action_names" instead of delegating to collection class. Delegate to collection class instead.

---

## eliminate_duplication
**repl_session.py** - 5 violation(s)

[X] ERROR (line 189)
Duplicate code blocks detected (3 locations) - extract to helper function.

Location (_move_to_next_behavior_first_action:189-196):
```python
self.current_state['current_behavior'] = self._build_full_behavior_path(next_behavior.name)
self.current_state['current_action'] = self._build_full_action_path(next_behavior.name, next_first_action.ac...
```

Location (_advance_to_next_behavior:643-650):
```python
next_behavior = behaviors[current_behavior_index + 1]
next_first_action = next_behavior.actions._actions[0]
self.current_state['current_behavior'] = self._build_full_behavior_path(next_behavior.name)
...
```

Location (_next_to_new_behavior:776-784):
```python
next_behavior = behaviors[current_behavior_index + 1]
next_first_action = next_behavior.actions._actions[0]
self.current_state['current_behavior'] = self._build_full_behavior_path(next_behavior.name)
...
```

[X] ERROR (line 190)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_move_to_next_behavior_first_action:190-194):
```python
self.current_state['current_action'] = self._build_full_action_path(next_behavior.name, next_first_action.action_name)
self.current_state['action_phase'] = 'not_started'
self.current_state['completed_...
```

Location (_next_to_new_behavior:780-784):
```python
self.current_state['current_action'] = self._build_full_action_path(next_behavior.name, next_first_action.action_name)
self.current_state['action_phase'] = 'not_started'
self.current_state['completed_...
```

[X] ERROR (line 191)
Duplicate code blocks detected (3 locations) - extract to helper function.

Location (_move_to_next_behavior_first_action:191-196):
```python
self.current_state['action_phase'] = 'not_started'
self.current_state['completed_actions'] = []
self.current_state['completed_behaviors'] = completed_behaviors
self._save_state(self.current_state)
ret...
```

Location (_go_back_to_previous_behavior:707-712):
```python
self.current_state['action_phase'] = 'not_started'
self.current_state['completed_actions'] = new_completed_actions
self.current_state['completed_behaviors'] = completed_behaviors
self._save_state(self...
```

Location (_next_to_new_behavior:781-786):
```python
self.current_state['action_phase'] = 'not_started'
self.current_state['completed_actions'] = []
self.current_state['completed_behaviors'] = completed_behaviors
self._save_state(self.current_state)
ret...
```

[X] ERROR (line 643)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_advance_to_next_behavior:643-652):
```python
next_behavior = behaviors[current_behavior_index + 1]
next_first_action = next_behavior.actions._actions[0]
self.current_state['current_behavior'] = self._build_full_behavior_path(next_behavior.name)
...
```

Location (_next_to_new_behavior:776-786):
```python
next_behavior = behaviors[current_behavior_index + 1]
next_first_action = next_behavior.actions._actions[0]
self.current_state['current_behavior'] = self._build_full_behavior_path(next_behavior.name)
...
```

[X] ERROR (line 655)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_advance_to_next_action:655-662):
```python
actions = list(behavior.actions)
next_action = actions[current_index + 1]
self.current_state['current_action'] = f'{self.current_behavior_state}.{next_action.action_name}'
self.current_state['action_p...
```

Location (_handle_next_command:748-755):
```python
self._mark_current_action_complete()
next_action = actions[current_index + 1]
self.current_state['current_action'] = f'{self.current_behavior_state}.{next_action.action_name}'
self.current_state['acti...
```

---


## Cross-File Duplication Analysis
Scanning 5 files...
Extracted 355 code blocks
Starting 62835 pairwise comparisons...
Comparing: 5% (3,142/62,835) - 0 violations - ETA: 18s  
Comparing: 10% (6,284/62,835) - 0 violations - ETA: 11s  
