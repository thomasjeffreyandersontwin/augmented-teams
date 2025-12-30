# Validation Status - code
Started: 2025-12-29 17:27:38
Files: 274

## avoid_excessive_guards
**action_context.py** - 3 violation(s)

[!] WARNING (line 101)
Line 101: Variable truthiness check detected (if not matches_include:). Assume variable exists - let code fail fast if missing.

```python
                        break
                
                if not matches_include:
                    continue
            
```

[!] WARNING (line 117)
Line 117: Variable truthiness check detected (if matches_exclude:). Assume variable exists - let code fail fast if missing.

```python
                        break
                
                if matches_exclude:
                    continue
            
```

[!] WARNING (line 188)
Line 188: Variable truthiness check detected (if not data:). Assume variable exists - let code fail fast if missing.

```python
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Scope':
        if not data:
            return cls()
        
```

---

## avoid_excessive_guards
**repl_session.py** - 1 violation(s)

[!] WARNING (line 1161)
Line 1161: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

```python
    def parse_command_parameters(self, args: str) -> Dict[str, Any]:
        params = {}
        if not args:
            return params
        
```

---

## avoid_excessive_guards
**vocabulary_helper.py** - 1 violation(s)

[!] WARNING (line 174)
Line 174: Variable truthiness check detected (if not synsets:). Assume variable exists - let code fail fast if missing.

```python
            synsets = wn.synsets(word_lower)
            
            if not synsets:
                return False
            
```

---

## eliminate_duplication
**action_context.py** - 1 violation(s)

[X] ERROR (line 88)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (filter_files:88-102):
```python
matches_include = False
for pattern in self.include_patterns:
    pattern_normalized = pattern.replace('\\', '/')
    if file_str == pattern_normalized or file_str.endswith(pattern_normalized) or fnma...
```

Location (filter_files:105-118):
```python
matches_exclude = False
for pattern in self.exclude_patterns:
    pattern_normalized = pattern.replace('\\', '/')
    if file_str == pattern_normalized or file_str.endswith(pattern_normalized) or fnma...
```

---

## eliminate_duplication
**repl_session.py** - 2 violation(s)

[X] ERROR (line 192)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (display_current_state:192-205):
```python
lines.append(str(self.workspace_directory))
lines.append('```')
lines.append('')
lines.append('To change path:')
lines.append('```')
lines.append('path demo/mob_minion              # Change to specifi...
```

Location (display_current_state:220-228):
```python
lines.append(formatter.subsection_separator())
lines.append(f'## {formatter.position_icon()} **Progress**')
lines.append('**Current Position:**')
lines.append('```')
lines.append(f'{self.progress_path...
```

[X] ERROR (line 459)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_handle_next_command:459-478):
```python
if not self.has_current_action:
    return REPLCommandResponse(output='ERROR: No current action', response='ERROR: No current action', status='error')
behavior = self.current_behavior
if not behavior:...
```

Location (_handle_back_command:495-514):
```python
if not self.has_current_action:
    return REPLCommandResponse(output='ERROR: No current action', response='ERROR: No current action', status='error')
behavior = self.current_behavior
if not behavior:...
```

---

