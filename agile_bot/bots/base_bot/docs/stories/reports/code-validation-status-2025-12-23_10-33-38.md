# Validation Status - code
Started: 2025-12-23 10:33:38
Files: 1

## avoid_excessive_guards
**repl_session.py** - 1 violation(s)

[!] WARNING (line 43)
Line 43: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    
    def display_current_state(self) -> REPLStateDisplay:
        if self.current_state is None:
            return REPLStateDisplay(
                output="No behavior action state found. Please select a behavior to begin.",
                state_loaded=False
            )
        
```

---


## Cross-File Duplication Analysis
Scanning 1 files...
Extracted 91 code blocks
Starting 4095 pairwise comparisons...
Comparing: 5% (205/4,095) - 0 violations - ETA: 18s  
Comparing: 10% (410/4,095) - 0 violations - ETA: 8s  
Comparing: 15% (615/4,095) - 0 violations - ETA: 5s  
Comparing: 20% (819/4,095) - 0 violations - ETA: 4s  
Comparing: 25% (1,024/4,095) - 0 violations - ETA: 2s  
Comparing: 30% (1,229/4,095) - 0 violations - ETA: 2s  
Comparing: 35% (1,434/4,095) - 0 violations - ETA: 1s  
Comparing: 40% (1,638/4,095) - 0 violations - ETA: 1s  
Comparing: 45% (1,843/4,095) - 0 violations - ETA: 1s  
Comparing: 50% (2,048/4,095) - 0 violations - ETA: 0s  
Comparing: 55% (2,253/4,095) - 0 violations - ETA: 0s  
Comparing: 60% (2,457/4,095) - 0 violations - ETA: 0s  
Comparing: 65% (2,662/4,095) - 0 violations - ETA: 0s  
Comparing: 70% (2,867/4,095) - 0 violations - ETA: 0s  
Comparing: 75% (3,072/4,095) - 0 violations - ETA: 0s  
Comparing: 80% (3,276/4,095) - 0 violations - ETA: 0s  
Comparing: 85% (3,481/4,095) - 0 violations - ETA: 0s  
Comparing: 90% (3,686/4,095) - 0 violations - ETA: 0s  
Comparing: 95% (3,891/4,095) - 0 violations - ETA: 0s  
Comparing: 100% (4,095/4,095) - 0 violations - ETA: 0s  
Complete: 4095 comparisons, 0 violations

## keep_classes_small_with_single_responsibility
**repl_session.py** - 1 violation(s)

[!] WARNING (line 14)
Class "REPLSession" is 505 lines - should be under 300 lines (extract related methods into separate classes)

```python


class REPLSession:
    
    def __init__(self, bot, workspace_directory: Path):
        self.bot = bot
        self.workspace_directory = Path(workspace_directory)
        self.state_file = workspace_directory / 'behavior_action_state.json'
        self.current_state = self._load_state()
    
    # ... (truncated)
```

---

## keep_functions_small_focused
**repl_session.py** - 1 violation(s)

[!] WARNING (line 106)
Function "read_and_execute_command" is 47 lines - should be under 20 lines (extract complex logic to helper functions)

```python
            return None
    
    def read_and_execute_command(self, command: str) -> REPLCommandResponse:
        command = command.strip()
        
        if not command:
            return REPLCommandResponse(
                output="",
                response="",
                status="empty"
            )
        
        parts = command.split(maxsplit=1)
        command_verb = parts[0].lower()
        command_args = parts[1] if len(parts) > 1 else ""
        
        if command_verb == "behavior":
            return self._handle_behavior_command(command_args)
        elif command_verb == "action":
            return self._handle_action_command(command_args)
        elif command_verb == "help":
            return self._handle_help_command(command_args)
        elif command_verb == "status":
            return self._handle_status_command()
        elif command_verb == "exit":
            return self._handle_exit_command()
        elif command_verb == "yes":
            return self._handle_advance_command()
        elif command_verb == "no":
            return self._handle_loop_back_command()
        elif command_verb == "workspace":
            return self._handle_workspace_command(command_args)
        elif command_verb == "go":
            return self._handle_go_command()
        elif command_verb == "scope":
            return self._handle_scope_command(command_args)
        elif command_verb == "clarify":
            return self._handle_action_execution("clarify", command_args)
        elif command_verb == "strategy":
            return self._handle_action_execution("strategy", command_args)
        elif command_verb == "build":
            return self._handle_action_execution("build", command_args)
        elif command_verb == "validate":
            return self._handle_action_execution("validate", command_args)
        elif command_verb == "render":
            return self._handle_action_execution("render", command_args)
        else:
            return REPLCommandResponse(
                output=f"ERROR: Unknown command '{command_verb}'",
                response=f"ERROR: Unknown command '{command_verb}'",
    # ... (truncated)
```

---

## maintain_vertical_density
**repl_session.py** - 1 violation(s)

[i] INFO (line 157)
Function "_handle_behavior_command" is 53 lines - consider improving vertical density by declaring variables near usage

```python
            )
    
    def _handle_behavior_command(self, behavior_name: str) -> REPLCommandResponse:
        behavior_name = behavior_name.strip()
        
        if not behavior_name:
            return REPLCommandResponse(
                output="ERROR: No behavior specified",
                response="ERROR: No behavior specified",
                status="error"
    # ... (truncated)
```

---

## simplify_control_flow
**repl_session.py** - 1 violation(s)

[!] WARNING (line 106)
Function "read_and_execute_command" has nesting depth of 15 - use guard clauses and extract nested blocks to reduce nesting

```python
            return None
    
    def read_and_execute_command(self, command: str) -> REPLCommandResponse:
        command = command.strip()
        
        if not command:
            return REPLCommandResponse(
                output="",
                response="",
                status="empty"
            )
        
        parts = command.split(maxsplit=1)
        command_verb = parts[0].lower()
        command_args = parts[1] if len(parts) > 1 else ""
    # ... (truncated)
```

---

Completed: 2025-12-23 10:33:39
Total violations: 5
Scanners executed: 30
