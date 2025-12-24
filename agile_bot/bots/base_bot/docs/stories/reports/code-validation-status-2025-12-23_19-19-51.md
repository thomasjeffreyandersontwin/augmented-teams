# Validation Status - code
Started: 2025-12-23 19:19:51
Files: 5

## delegate_to_lowest_level
**repl_help.py** - 6 violation(s)

[i] INFO (line 37)
Method "help_text" in class "ActionHelp" iterates through "_stages" instead of delegating to collection class. Delegate to collection class instead.

[i] INFO (line 47)
Method "help_text" in class "ActionHelp" iterates through "_context_parameters" instead of delegating to collection class. Delegate to collection class instead.

[i] INFO (line 101)
Method "actions_list" in class "BehaviorHelp" iterates through "action_names" instead of delegating to collection class. Delegate to collection class instead.

[i] INFO (line 168)
Method "main_help" in class "REPLHelp" iterates through "action_descriptions" instead of delegating to collection class. Delegate to collection class instead.

[i] INFO (line 178)
Method "main_help" in class "REPLHelp" iterates through "command_examples" instead of delegating to collection class. Delegate to collection class instead.

[i] INFO (line 184)
Method "main_help" in class "REPLHelp" iterates through "other_commands" instead of delegating to collection class. Delegate to collection class instead.

---

## eliminate_duplication
**repl_session.py** - 1 violation(s)

[X] ERROR (line 397)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_handle_confirm_command:397-401):
```python
self.bot.behaviors.close_current()
if next_behavior.actions.names:
    next_behavior.actions.navigate_to(next_behavior.actions.names[0])
return self._execute_action_instructions()
```

Location (_handle_next_command:433-437):
```python
self.bot.behaviors.navigate_to(next_behavior.name)
if next_behavior.actions.names:
    next_behavior.actions.navigate_to(next_behavior.actions.names[0])
return self._execute_action_instructions()
```

---


## Cross-File Duplication Analysis
Scanning 5 files...
Extracted 146 code blocks
Starting 10585 pairwise comparisons...
Comparing: 5% (530/10,585) - 0 violations - ETA: 18s  
Comparing: 10% (1,059/10,585) - 0 violations - ETA: 8s  
Comparing: 15% (1,588/10,585) - 0 violations - ETA: 5s  
Comparing: 20% (2,117/10,585) - 0 violations - ETA: 4s  
Comparing: 25% (2,647/10,585) - 0 violations - ETA: 2s  
Comparing: 30% (3,176/10,585) - 0 violations - ETA: 2s  
Comparing: 35% (3,705/10,585) - 0 violations - ETA: 1s  
Comparing: 40% (4,234/10,585) - 0 violations - ETA: 1s  
Comparing: 45% (4,764/10,585) - 0 violations - ETA: 1s  
Comparing: 50% (5,293/10,585) - 0 violations - ETA: 1s  
Comparing: 55% (5,822/10,585) - 0 violations - ETA: 1s  
Comparing: 60% (6,351/10,585) - 0 violations - ETA: 0s  
Comparing: 65% (6,881/10,585) - 0 violations - ETA: 0s  
Comparing: 70% (7,410/10,585) - 0 violations - ETA: 0s  
Comparing: 75% (7,939/10,585) - 0 violations - ETA: 0s  
Comparing: 80% (8,468/10,585) - 0 violations - ETA: 0s  
Comparing: 85% (8,998/10,585) - 0 violations - ETA: 0s  
Comparing: 90% (9,527/10,585) - 0 violations - ETA: 0s  
Comparing: 95% (10,056/10,585) - 0 violations - ETA: 0s  
Comparing: 100% (10,585/10,585) - 0 violations - ETA: 0s  
Complete: 10585 comparisons, 0 violations

## keep_classes_small_with_single_responsibility
**repl_session.py** - 1 violation(s)

[!] WARNING (line 14)
Class "REPLSession" is 552 lines - should be under 300 lines (extract related methods into separate classes)

```python


class REPLSession:
    STAGE_MAP = {
        'not_started': 'instructions',
        'instructions_given': 'instructions',
        'submitted': 'submitted'
    }
    
    COMMAND_HANDLERS = {
    # ... (truncated)
```

---

## place_imports_at_top
**repl_session.py** - 2 violation(s)

[X] ERROR (line 10)
Import statement found after non-import code. Move all imports to the top of the file.

```python
    TTYDetectionResult
)
from agile_bot.bots.base_bot.src.repl_cli.repl_help import REPLHelp
from agile_bot.bots.base_bot.src.repl_cli.repl_status import REPLStatus
```

[X] ERROR (line 11)
Import statement found after non-import code. Move all imports to the top of the file.

```python
)
from agile_bot.bots.base_bot.src.repl_cli.repl_help import REPLHelp
from agile_bot.bots.base_bot.src.repl_cli.repl_status import REPLStatus

```

---

Completed: 2025-12-23 19:19:54
Total violations: 10
Scanners executed: 30
