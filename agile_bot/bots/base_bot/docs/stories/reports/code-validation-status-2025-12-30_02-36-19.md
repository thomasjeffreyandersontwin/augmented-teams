# Validation Status - code
Started: 2025-12-30 02:36:19
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
Scanning 1 changed file(s) against 275 total files...
