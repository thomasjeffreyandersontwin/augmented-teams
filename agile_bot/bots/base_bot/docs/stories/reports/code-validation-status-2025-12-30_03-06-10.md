# Validation Status - code
Started: 2025-12-30 03:06:10
Files: 275

## avoid_excessive_guards
**cli_action_parsers.py** - 1 violation(s)

[!] WARNING (line 89)
Line 89: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
            value = parse_json_dict(value)
        
        if value is not None:
            kwargs[field_name] = value
    
```

---

## avoid_excessive_guards
**repl_session.py** - 1 violation(s)

[!] WARNING (line 1464)
Line 1464: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

```python
    def parse_command_parameters(self, args: str) -> Dict[str, Any]:
        params = {}
        if not args:
            return params
        
```

---

## avoid_excessive_guards
**cli_bot.py** - 2 violation(s)

[!] WARNING (line 46)
Line 46: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def help(self) -> REPLHelp:
        if self._help is None:
            self._help = REPLHelp(self._bot)
        return self._help
```

[!] WARNING (line 52)
Line 52: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def status(self) -> REPLStatus:
        if self._status is None:
            self._status = REPLStatus(self, self._session, self._session.formatter)
        return self._status
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
Scanning 4 changed file(s) against 20 total files...
Extracted 399 changed blocks, 494 reference blocks
Starting 197,106 pairwise comparisons...
Comparing: 5% (9,856/197,106) - 0 violations - ETA: 66s  
Comparing: 10% (19,711/197,106) - 0 violations - ETA: 57s  
Comparing: 15% (29,566/197,106) - 0 violations - ETA: 55s  
Comparing: 20% (39,422/197,106) - 0 violations - ETA: 52s  
Comparing: 25% (49,277/197,106) - 0 violations - ETA: 48s  
Comparing: 30% (59,132/197,106) - 0 violations - ETA: 47s  
Comparing: 35% (68,988/197,106) - 0 violations - ETA: 45s  
Comparing: 40% (78,843/197,106) - 0 violations - ETA: 43s  
Comparing: 45% (88,698/197,106) - 0 violations - ETA: 40s  
Comparing: 50% (98,553/197,106) - 0 violations - ETA: 38s  
Comparing: 55% (108,409/197,106) - 0 violations - ETA: 35s  
Comparing: 60% (118,264/197,106) - 0 violations - ETA: 31s  
