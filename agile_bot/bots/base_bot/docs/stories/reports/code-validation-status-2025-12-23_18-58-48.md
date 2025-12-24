# Validation Status - code
Started: 2025-12-23 18:58:48
Files: 3

## avoid_excessive_guards
**repl_session.py** - 1 violation(s)

[!] WARNING (line 224)
Line 224: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    def get_progress_line(self) -> str:
        """Get just the progress line for display in header."""
        if self.current_state is None:
            self.current_state = self._load_state()
        
```

---

## chain_dependencies_properly
**repl_session.py** - 21 violation(s)

[!] WARNING (line 287)
Passing self.current_behavior as parameter to _format_action_status_list(). Access it directly in the method through self.current_behavior instead.

```python
        )
    
    def _render_full_status(self) -> List[str]:
        """Render full workflow hierarchy for status command."""
```

[!] WARNING (line 585)
Passing self.current_behavior_name as parameter to _update_state_and_generate_response(). Access it directly in the method through self.current_behavior_name instead.

```python
        self._save_state(state_data)
    
    def _handle_action_command(self, action_name: str) -> REPLCommandResponse:
        action_name = action_name.strip()
```

[!] WARNING (line 585)
Passing self.current_behavior_name as parameter to _error_behavior_not_found(). Access it directly in the method through self.current_behavior_name instead.

```python
        self._save_state(state_data)
    
    def _handle_action_command(self, action_name: str) -> REPLCommandResponse:
        action_name = action_name.strip()
```

[!] WARNING (line 585)
Passing self.current_behavior_name as parameter to _error_action_not_found(). Access it directly in the method through self.current_behavior_name instead.

```python
        self._save_state(state_data)
    
    def _handle_action_command(self, action_name: str) -> REPLCommandResponse:
        action_name = action_name.strip()
```

[!] WARNING (line 615)
Passing self.current_behavior_name as parameter to _render_action_parameters(). Access it directly in the method through self.current_behavior_name instead.

```python
        return None
    
    def _handle_help_command(self, args: str) -> REPLCommandResponse:
        args = args.strip()
```

[!] WARNING (line 752)
Passing self.current_action_name as parameter to _execute_action_instructions(). Access it directly in the method through self.current_action_name instead.

```python
        return self._handle_instructions_command()
    
    def _handle_instructions_command(self) -> REPLCommandResponse:
        """Get instructions for current action."""
```

[!] WARNING (line 786)
Passing self.current_action_name as parameter to _find_action_index(). Access it directly in the method through self.current_action_name instead.

```python
        return REPLCommandResponse(output=output, response=output, status="success", action=self.current_action_name)
    
    def _handle_confirm_command(self) -> REPLCommandResponse:
        """Confirm/complete current action and advance to next."""
```

[!] WARNING (line 786)
Passing self.current_behavior_name as parameter to _error_behavior_not_found(). Access it directly in the method through self.current_behavior_name instead.

```python
        return REPLCommandResponse(output=output, response=output, status="success", action=self.current_action_name)
    
    def _handle_confirm_command(self) -> REPLCommandResponse:
        """Confirm/complete current action and advance to next."""
```

[!] WARNING (line 815)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        self.current_state['completed_actions'] = completed_actions
    
    def _advance_to_next_behavior(self) -> REPLCommandResponse:
        """Advance to the next behavior after completing the current one."""
```

[!] WARNING (line 815)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        self.current_state['completed_actions'] = completed_actions
    
    def _advance_to_next_behavior(self) -> REPLCommandResponse:
        """Advance to the next behavior after completing the current one."""
```

[!] WARNING (line 851)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return self._execute_action_instructions(next_first_action.action_name)
    
    def _advance_to_next_action(self, behavior, current_index: int) -> REPLCommandResponse:
        """Advance to the next action within the current behavior."""
```

[!] WARNING (line 874)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return self._go_back_within_behavior(completed_actions)
    
    def _go_back_to_previous_behavior(self) -> REPLCommandResponse:
        """Go back to the last action of the previous behavior."""
```

[!] WARNING (line 914)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return self._execute_action_instructions(last_action.action_name)
    
    def _go_back_within_behavior(self, completed_actions: List[Dict]) -> REPLCommandResponse:
        """Go back to the previous action within the current behavior."""
```

[!] WARNING (line 926)
Passing self.current_action_name as parameter to _find_action_index(). Access it directly in the method through self.current_action_name instead.

```python
        return self._execute_action_instructions(new_action_state.split('.')[-1])
    
    def _handle_next_command(self) -> REPLCommandResponse:
        """Move forward to next action."""
```

[!] WARNING (line 926)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return self._execute_action_instructions(new_action_state.split('.')[-1])
    
    def _handle_next_command(self) -> REPLCommandResponse:
        """Move forward to next action."""
```

[!] WARNING (line 926)
Passing self.current_behavior_name as parameter to _error_behavior_not_found(). Access it directly in the method through self.current_behavior_name instead.

```python
        return self._execute_action_instructions(new_action_state.split('.')[-1])
    
    def _handle_next_command(self) -> REPLCommandResponse:
        """Move forward to next action."""
```

[!] WARNING (line 959)
Passing self.current_behavior_name as parameter to _find_behavior_index(). Access it directly in the method through self.current_behavior_name instead.

```python
        return self._execute_action_instructions(next_action.action_name)
    
    def _next_to_new_behavior(self) -> REPLCommandResponse:
        """Handle next command when at last action of current behavior."""
```

[!] WARNING (line 959)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return self._execute_action_instructions(next_action.action_name)
    
    def _next_to_new_behavior(self) -> REPLCommandResponse:
        """Handle next command when at last action of current behavior."""
```

[!] WARNING (line 1153)
Passing self.current_behavior_name as parameter to _navigate_to_action(). Access it directly in the method through self.current_behavior_name instead.

```python
        )
    
    def _validate_and_navigate_to_action(self, action_name: str) -> Optional[REPLCommandResponse]:
        """Validate current behavior exists and navigate to action. Returns error response or None on success."""
```

[!] WARNING (line 1153)
Passing self.current_behavior_name as parameter to _error_behavior_not_found(). Access it directly in the method through self.current_behavior_name instead.

```python
        )
    
    def _validate_and_navigate_to_action(self, action_name: str) -> Optional[REPLCommandResponse]:
        """Validate current behavior exists and navigate to action. Returns error response or None on success."""
```

[!] WARNING (line 1153)
Passing self.current_behavior_name as parameter to _error_action_not_found(). Access it directly in the method through self.current_behavior_name instead.

```python
        )
    
    def _validate_and_navigate_to_action(self, action_name: str) -> Optional[REPLCommandResponse]:
        """Validate current behavior exists and navigate to action. Returns error response or None on success."""
```

---

## eliminate_duplication
**repl_session.py** - 4 violation(s)

[X] ERROR (line 595)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_handle_action_command:595-607):
```python
if not self.has_current_behavior:
    return self._error_no_current_behavior()
behavior = self.current_behavior
if not behavior:
    return self._error_behavior_not_found(self.current_behavior_name, s...
```

Location (_validate_and_navigate_to_action:1155-1168):
```python
if not self.has_current_behavior:
    return self._error_no_current_behavior()
behavior = self.current_behavior
if not behavior:
    return self._error_behavior_not_found(self.current_behavior_name, s...
```

[X] ERROR (line 840)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_advance_to_next_behavior:840-849):
```python
next_behavior = behaviors[current_behavior_index + 1]
next_first_action = next_behavior.actions._actions[0]
self.current_state['current_behavior'] = self._build_full_behavior_path(next_behavior.name)
...
```

Location (_next_to_new_behavior:979-989):
```python
next_behavior = behaviors[current_behavior_index + 1]
next_first_action = next_behavior.actions._actions[0]
self.current_state['current_behavior'] = self._build_full_behavior_path(next_behavior.name)
...
```

[X] ERROR (line 853)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_advance_to_next_action:853-860):
```python
actions = list(behavior.actions)
next_action = actions[current_index + 1]
self.current_state['current_action'] = f'{self.current_behavior_state}.{next_action.action_name}'
self.current_state['action_p...
```

Location (_handle_next_command:950-957):
```python
self._mark_current_action_complete()
next_action = actions[current_index + 1]
self.current_state['current_action'] = f'{self.current_behavior_state}.{next_action.action_name}'
self.current_state['acti...
```

[X] ERROR (line 907)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_go_back_to_previous_behavior:907-912):
```python
self.current_state['action_phase'] = 'not_started'
self.current_state['completed_actions'] = new_completed_actions
self.current_state['completed_behaviors'] = completed_behaviors
self._save_state(self...
```

Location (_next_to_new_behavior:984-989):
```python
self.current_state['action_phase'] = 'not_started'
self.current_state['completed_actions'] = []
self.current_state['completed_behaviors'] = completed_behaviors
self._save_state(self.current_state)
ret...
```

---


## Cross-File Duplication Analysis
Scanning 3 files...
Extracted 333 code blocks
Starting 55278 pairwise comparisons...
Comparing: 5% (2,764/55,278) - 0 violations - ETA: 18s  
Comparing: 10% (5,528/55,278) - 0 violations - ETA: 9s  
Comparing: 15% (8,292/55,278) - 0 violations - ETA: 9s  
Comparing: 20% (11,056/55,278) - 0 violations - ETA: 9s  
Comparing: 25% (13,820/55,278) - 0 violations - ETA: 9s  
Comparing: 30% (16,584/55,278) - 0 violations - ETA: 8s  
Comparing: 35% (19,348/55,278) - 0 violations - ETA: 6s  
Comparing: 40% (22,112/55,278) - 0 violations - ETA: 5s  
Comparing: 45% (24,876/55,278) - 0 violations - ETA: 4s  
Comparing: 50% (27,639/55,278) - 0 violations - ETA: 3s  
Comparing: 55% (30,403/55,278) - 0 violations - ETA: 2s  
Comparing: 60% (33,167/55,278) - 0 violations - ETA: 2s  
Comparing: 65% (35,931/55,278) - 0 violations - ETA: 1s  
Comparing: 70% (38,695/55,278) - 0 violations - ETA: 1s  
Comparing: 75% (41,459/55,278) - 0 violations - ETA: 1s  
Comparing: 80% (44,223/55,278) - 0 violations - ETA: 0s  
Comparing: 85% (46,987/55,278) - 0 violations - ETA: 0s  
Comparing: 90% (49,751/55,278) - 0 violations - ETA: 0s  
Comparing: 95% (52,515/55,278) - 0 violations - ETA: 0s  
Comparing: 100% (55,278/55,278) - 0 violations - ETA: 0s  
Complete: 55278 comparisons, 0 violations

## keep_classes_small_with_single_responsibility
**repl_session.py** - 1 violation(s)

[!] WARNING (line 14)
Class "REPLSession" is 1155 lines - should be under 300 lines (extract related methods into separate classes)

```python


class REPLSession:
    """Interactive REPL session for navigating bot behaviors and actions."""
    
    # Constants
    STAGE_MAP = {
        'not_started': 'instructions',
        'instructions_given': 'instructions',
        'submitted': 'submitted'
    # ... (truncated)
```

---

## keep_functions_small_focused
**repl_session.py** - 1 violation(s)

[!] WARNING (line 375)
Function "read_and_execute_command" is 122 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return self.bot.behaviors.find_by_name(behavior_name)
    
    def read_and_execute_command(self, command: str) -> REPLCommandResponse:
        command = command.strip()
        
        if not command:
            return REPLCommandResponse(
                output="",
                response="",
                status="empty"
            )
        
        # Handle dot notation: behavior.action or behavior.action.operation
        if '.' in command:
            dot_parts = command.split('.')
            if len(dot_parts) == 2:
                # behavior.action
                behavior_name, action_name = dot_parts
                behavior = self._get_behavior(behavior_name)
                if behavior:
                    action = self._find_action(behavior, action_name)
                    if action:
                        # Navigate to behavior.action and execute instructions
                        full_action = f"{self.bot.bot_name}.{behavior_name}.{action_name}"
                        return self._update_state_and_generate_response(behavior_name, action_name, full_action)
                    else:
                        return REPLCommandResponse(
                            output=f"ERROR: Action '{action_name}' not found in behavior '{behavior_name}'",
                            response=f"ERROR: Action '{action_name}' not found",
                            status="error"
                        )
                else:
                    return REPLCommandResponse(
                        output=f"ERROR: Behavior '{behavior_name}' not found",
                        response=f"ERROR: Behavior '{behavior_name}' not found",
                        status="error"
                    )
            elif len(dot_parts) == 3:
                # behavior.action.operation
                behavior_name, action_name, operation = dot_parts
                behavior = self._get_behavior(behavior_name)
                if behavior:
                    action = self._find_action(behavior, action_name)
                    if action:
                        # Validate operation before navigating
                        if operation not in ["instructions", "submit", "confirm"]:
                            return REPLCommandResponse(
                                output=f"ERROR: Unknown operation '{operation}'. Use: instructions, submit, or confirm",
                                response=f"ERROR: Unknown operation '{operation}'",
                                status="error"
    # ... (truncated)
```

---

## maintain_vertical_density
**repl_session.py** - 1 violation(s)

[i] INFO (line 375)
Function "read_and_execute_command" is 129 lines - consider improving vertical density by declaring variables near usage

```python
        return self.bot.behaviors.find_by_name(behavior_name)
    
    def read_and_execute_command(self, command: str) -> REPLCommandResponse:
        command = command.strip()
        
        if not command:
            return REPLCommandResponse(
                output="",
                response="",
                status="empty"
    # ... (truncated)
```

---

## simplify_control_flow
**repl_session.py** - 2 violation(s)

[!] WARNING (line 287)
Function "_render_full_status" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        )
    
    def _render_full_status(self) -> List[str]:
        """Render full workflow hierarchy for status command."""
        output_lines = [f"Progress: {self.progress_path}.{self.stage_name}"]
        
        if self.bot and self.bot.behaviors:
            # Level 1: Behaviors
            behavior_parts = self._format_behavior_status_list()
            output_lines.append("Behaviors: " + " -> ".join(behavior_parts))
            
            # Level 2: Actions for current behavior
            if self.current_behavior:
                action_parts = self._format_action_status_list(self.current_behavior)
                output_lines.append("  Actions: " + " -> ".join(action_parts))
    # ... (truncated)
```

[!] WARNING (line 375)
Function "read_and_execute_command" has nesting depth of 21 - use guard clauses and extract nested blocks to reduce nesting

```python
        return self.bot.behaviors.find_by_name(behavior_name)
    
    def read_and_execute_command(self, command: str) -> REPLCommandResponse:
        command = command.strip()
        
        if not command:
            return REPLCommandResponse(
                output="",
                response="",
                status="empty"
            )
        
        # Handle dot notation: behavior.action or behavior.action.operation
        if '.' in command:
            dot_parts = command.split('.')
    # ... (truncated)
```

---

## stop_writing_useless_comments
**repl_session.py** - 57 violation(s)

[X] ERROR (line 15)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class REPLSession:
    """Interactive REPL session for navigating bot behaviors and actions."""
    
```

[X] ERROR (line 36)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def has_current_action(self) -> bool:
        """Check if there's a valid current action in state."""
        return bool(self.current_state and self.current_state.get('current_action'))
```

[X] ERROR (line 41)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def has_current_behavior(self) -> bool:
        """Check if there's a valid current behavior in state."""
        return bool(self.current_state and self.current_state.get('current_behavior'))
```

[X] ERROR (line 46)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def current_behavior_name(self) -> Optional[str]:
        """Get the simple name of the current behavior (without bot prefix)."""
        if not self.has_current_behavior:
```

[X] ERROR (line 53)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def current_action_name(self) -> Optional[str]:
        """Get the simple name of the current action (without behavior prefix)."""
        if not self.has_current_action:
```

[X] ERROR (line 60)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def current_action_state(self) -> Optional[str]:
        """Get the full current action state path (e.g., 'bot.behavior.action')."""
        if not self.has_current_action:
```

[X] ERROR (line 67)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def current_behavior_state(self) -> Optional[str]:
        """Get the full current behavior state path (e.g., 'bot.behavior')."""
        if not self.has_current_behavior:
```

[X] ERROR (line 74)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def action_phase(self) -> str:
        """Get the current action phase."""
        if not self.current_state:
```

[X] ERROR (line 81)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def stage_name(self) -> str:
        """Get the display stage name for the current action phase."""
        return self.STAGE_MAP.get(self.action_phase, self.action_phase)
```

[X] ERROR (line 86)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def progress_path(self) -> str:
        """Get the progress path for display (without bot name prefix)."""
        if not self.has_current_action:
```

[X] ERROR (line 94)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def behavior_names(self) -> List[str]:
        """Get list of all behavior names from the bot."""
        if not self.bot or not self.bot.behaviors:
```

[X] ERROR (line 101)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def completed_action_names(self) -> set:
        """Get set of completed action names for the current behavior."""
        if not self.current_state:
```

[X] ERROR (line 114)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def completed_behaviors(self) -> List[str]:
        """Get list of completed behavior names."""
        if not self.current_state:
```

[X] ERROR (line 121)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def current_behavior(self):
        """Get the current behavior object."""
        if not self.current_behavior_name:
```

[X] ERROR (line 131)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _get_action_names(self, behavior) -> List[str]:
        """Get list of action names for a behavior."""
        if not behavior or not behavior.actions:
```

[X] ERROR (line 137)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _build_full_behavior_path(self, behavior_name: str) -> str:
        """Build full behavior state path (e.g., 'bot.behavior')."""
        return f"{self.bot.bot_name}.{behavior_name}"
```

[X] ERROR (line 141)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _build_full_action_path(self, behavior_name: str, action_name: str) -> str:
        """Build full action state path (e.g., 'bot.behavior.action')."""
        return f"{self.bot.bot_name}.{behavior_name}.{action_name}"
```

[X] ERROR (line 145)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _format_status_item(self, name: str, is_current: bool, is_completed: bool, current_marker: str = "[*]") -> str:
        """Format an item with status indicator: [OK] done, [*] current, [ ] pending."""
        if is_completed:
```

[X] ERROR (line 154)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _find_action_index(self, behavior, action_name: str) -> int:
        """Find the index of an action within a behavior. Returns -1 if not found."""
        for i, action in enumerate(behavior.actions):
```

[X] ERROR (line 161)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _find_behavior_index(self, behavior_name: str) -> int:
        """Find the index of a behavior. Returns -1 if not found."""
        for i, b in enumerate(self.bot.behaviors):
```

[X] ERROR (line 168)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _error_no_current_action(self, context: str = "") -> REPLCommandResponse:
        """Create standard error response for missing current action."""
        msg = f"ERROR: No current action{' to ' + context if context else ''}"
```

[X] ERROR (line 173)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _error_no_current_behavior(self) -> REPLCommandResponse:
        """Create standard error response for missing current behavior."""
        return REPLCommandResponse(
```

[X] ERROR (line 181)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _error_behavior_not_found(self, behavior_name: str, show_available: bool = True) -> REPLCommandResponse:
        """Create standard error response for behavior not found."""
        if show_available:
```

[X] ERROR (line 193)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _error_action_not_found(self, action_name: str, behavior_name: str, behavior) -> REPLCommandResponse:
        """Create standard error response for action not found."""
        available = ", ".join(self._get_action_names(behavior))
```

[X] ERROR (line 223)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_progress_line(self) -> str:
        """Get just the progress line for display in header."""
        if self.current_state is None:
```

[X] ERROR (line 236)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _initialize_to_first_behavior_action(self) -> bool:
        """Initialize state to first behavior and first action. Returns True if successful."""
        if not self.bot or not self.bot.behaviors:
```

[X] ERROR (line 288)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _render_full_status(self) -> List[str]:
        """Render full workflow hierarchy for status command."""
        output_lines = [f"Progress: {self.progress_path}.{self.stage_name}"]
```

[X] ERROR (line 312)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _render_compact_status(self) -> List[str]:
        """Render compact view with behaviors and actions lists."""
        output_lines = [""]
```

[X] ERROR (line 329)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _format_behavior_status_list(self) -> List[str]:
        """Format all behaviors with status indicators."""
        parts = []
```

[X] ERROR (line 338)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _format_action_status_list(self, behavior) -> List[str]:
        """Format all actions in a behavior with status indicators."""
        parts = []
```

[X] ERROR (line 348)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _format_operation_status_list(self) -> List[str]:
        """Format operations with status indicators based on current stage."""
        if self.stage_name == 'instructions':
```

[X] ERROR (line 356)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _generate_breadcrumbs(self) -> str:
        """Generate breadcrumb navigation string for current behavior's actions."""
        behavior = self.current_behavior
```

[X] ERROR (line 540)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _navigate_to_action(self, behavior_name: str, action_name: str, full_action: str, state_updates: Dict = None):
        """Navigate to an action without executing. Updates state only."""
        state_data = dict(self.current_state) if self.current_state else {}
```

[X] ERROR (line 563)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _update_state_and_generate_response(self, behavior_name: str, action_name: str, full_action: str, state_updates: Dict = None) -> REPLCommandResponse:
        """Navigate to an action and execute instructions operation."""
        self._navigate_to_action(behavior_name, action_name, full_action, state_updates)
```

[X] ERROR (line 742)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_current_command(self) -> REPLCommandResponse:
        """Re-execute the current operation based on action_phase."""
        if not self.has_current_action:
```

[X] ERROR (line 753)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_instructions_command(self) -> REPLCommandResponse:
        """Get instructions for current action."""
        if not self.has_current_action:
```

[X] ERROR (line 759)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_submit_command(self) -> REPLCommandResponse:
        """Submit answers/evidence for current action."""
        if not self.has_current_action:
```

[X] ERROR (line 787)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_confirm_command(self) -> REPLCommandResponse:
        """Confirm/complete current action and advance to next."""
        if not self.has_current_action:
```

[X] ERROR (line 807)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _mark_current_action_complete(self) -> None:
        """Add current action to completed actions list."""
        completed_actions = self.current_state.get('completed_actions', [])
```

[X] ERROR (line 816)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _advance_to_next_behavior(self) -> REPLCommandResponse:
        """Advance to the next behavior after completing the current one."""
        behavior_name = self.current_behavior_name
```

[X] ERROR (line 852)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _advance_to_next_action(self, behavior, current_index: int) -> REPLCommandResponse:
        """Advance to the next action within the current behavior."""
        actions = list(behavior.actions)
```

[X] ERROR (line 863)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_back_command(self) -> REPLCommandResponse:
        """Move back to previous action."""
        if not self.has_current_action:
```

[X] ERROR (line 875)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _go_back_to_previous_behavior(self) -> REPLCommandResponse:
        """Go back to the last action of the previous behavior."""
        completed_behaviors = list(self.completed_behaviors)
```

[X] ERROR (line 915)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _go_back_within_behavior(self, completed_actions: List[Dict]) -> REPLCommandResponse:
        """Go back to the previous action within the current behavior."""
        last_completed = completed_actions.pop()
```

[X] ERROR (line 927)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_next_command(self) -> REPLCommandResponse:
        """Move forward to next action."""
        if not self.has_current_action:
```

[X] ERROR (line 960)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _next_to_new_behavior(self) -> REPLCommandResponse:
        """Handle next command when at last action of current behavior."""
        current_behavior_index = self._find_behavior_index(self.current_behavior_name)
```

[X] ERROR (line 992)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _execute_action_instructions(self, action_name: str) -> REPLCommandResponse:
        """Execute action and get instructions (mock)."""
        if not self.has_current_action:
```

[X] ERROR (line 1014)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def display_confirm_prompt(self) -> REPLStateDisplay:
        """Display confirmation prompt after action execution."""
        if not self.has_current_action:
```

[X] ERROR (line 1129)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_action_shortcut(self, action_name: str, subcommand: str) -> REPLCommandResponse:
        """Handle action shortcuts like 'clarify instructions', 'clarify submit', or 'clarify confirm'."""
        subcommand = subcommand.strip().lower()
```

[X] ERROR (line 1154)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _validate_and_navigate_to_action(self, action_name: str) -> Optional[REPLCommandResponse]:
        """Validate current behavior exists and navigate to action. Returns error response or None on success."""
        if not self.has_current_behavior:
```

[X] ERROR (line 30)
Useless comment: "# ==========================================================" - delete it or improve the code instead

```python
        self.current_state = self._load_state()
    
    # ========================================================================
    # Properties - Convenient accessors for common state/bot information
```

[X] ERROR (line 32)
Useless comment: "# ==========================================================" - delete it or improve the code instead

```python
    # ========================================================================
    # Properties - Convenient accessors for common state/bot information
    # ========================================================================
    
```

[X] ERROR (line 126)
Useless comment: "# ==========================================================" - delete it or improve the code instead

```python
        return self._get_behavior(self.current_behavior_name)
    
    # ========================================================================
    # Helper Methods - Reusable building blocks
```

[X] ERROR (line 128)
Useless comment: "# ==========================================================" - delete it or improve the code instead

```python
    # ========================================================================
    # Helper Methods - Reusable building blocks
    # ========================================================================
    
```

[X] ERROR (line 198)
Useless comment: "# ==========================================================" - delete it or improve the code instead

```python
        return REPLCommandResponse(output=output, response=f"ERROR: action '{action_name}' not found", status="error")
    
    # ========================================================================
    # State Management
```

[X] ERROR (line 200)
Useless comment: "# ==========================================================" - delete it or improve the code instead

```python
    # ========================================================================
    # State Management
    # ========================================================================
    
```

[X] ERROR (line 566)
Useless comment: "# Execute the action's first operation (instructions)" - delete it or improve the code instead

```python
        self._navigate_to_action(behavior_name, action_name, full_action, state_updates)
        
        # Execute the action's first operation (instructions)
        return self._execute_action_instructions(action_name)
```

---

Completed: 2025-12-23 18:59:07
Total violations: 88
Scanners executed: 30
