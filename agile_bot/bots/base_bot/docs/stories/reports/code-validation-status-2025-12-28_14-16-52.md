# Validation Status - code
Started: 2025-12-28 14:16:52
Files: 274

## avoid_excessive_guards
**actions.py** - 1 violation(s)

[!] WARNING (line 261)
Line 261: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    def is_final_action(self) -> bool:
        try:
            if self.current is None:
                return False
            action_names = self.names
```

---

## avoid_excessive_guards
**action_context.py** - 1 violation(s)

[!] WARNING (line 146)
Line 146: Variable truthiness check detected (if not data:). Assume variable exists - let code fail fast if missing.

```python
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Scope':
        if not data:
            return cls()
        
```

---

## avoid_excessive_guards
**repl_session.py** - 1 violation(s)

[!] WARNING (line 492)
Line 492: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

```python
    def parse_command_parameters(self, args: str) -> Dict[str, Any]:
        params = {}
        if not args:
            return params
        
```

---

## avoid_excessive_guards
**markdown_formatter.py** - 2 violation(s)

[!] WARNING (line 10)
Line 10: Variable truthiness check detected (if is_completed:). Assume variable exists - let code fail fast if missing.

```python
    
    def status_marker(self, is_current: bool, is_completed: bool) -> str:
        if is_completed:
            return "- ●"
        elif is_current:
            return "- ➤"
        else:
            return "- ○"
    
```

[!] WARNING (line 12)
Line 12: Variable truthiness check detected (if is_current:). Assume variable exists - let code fail fast if missing.

```python
        if is_completed:
            return "- ●"
        elif is_current:
            return "- ➤"
        else:
            return "- ○"
    
```

---

## avoid_excessive_guards
**terminal_formatter.py** - 2 violation(s)

[!] WARNING (line 10)
Line 10: Variable truthiness check detected (if is_completed:). Assume variable exists - let code fail fast if missing.

```python
    
    def status_marker(self, is_current: bool, is_completed: bool) -> str:
        if is_completed:
            return "[OK]"
        elif is_current:
            return "[*]"
        else:
            return "[ ]"
    
```

[!] WARNING (line 12)
Line 12: Variable truthiness check detected (if is_current:). Assume variable exists - let code fail fast if missing.

```python
        if is_completed:
            return "[OK]"
        elif is_current:
            return "[*]"
        else:
            return "[ ]"
    
```

---

## delegate_to_lowest_level
**repl_help.py** - 1 violation(s)

[i] INFO (line 24)
Method "format_as_lines" in class "StageCollection" iterates through "_stages" instead of delegating to collection class. Delegate to collection class instead.

---

## eliminate_duplication
**actions.py** - 1 violation(s)

[X] ERROR (line 116)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (advance:116-123):
```python
self._current_index += 1
self.save_state()
return {'status': 'success', 'message': f'Advanced to action: {next_action.action_name}', 'action': next_action.action_name}
```

Location (go_back:143-150):
```python
self._current_index -= 1
self.save_state()
return {'status': 'success', 'message': f'Went back to action: {prev_action.action_name}', 'action': prev_action.action_name}
```

---

