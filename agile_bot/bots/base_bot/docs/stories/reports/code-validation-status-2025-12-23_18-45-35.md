# Validation Status - code
Started: 2025-12-23 18:45:35
Files: 3

## avoid_excessive_guards
**repl_main.py** - 1 violation(s)

[!] WARNING (line 132)
Line 132: Variable truthiness check detected (if is_pipe_mode:). Assume variable exists - let code fail fast if missing.

```python
            # Prompt for command
            try:
                if is_pipe_mode:
                    # Pipe mode: read from stdin without prompt
                    command = input().strip()
                else:
                    # Interactive mode: show prompt
                    command = input(f"[{bot_name}] > ").strip()
            except EOFError:
```

---

## avoid_excessive_guards
**repl_session.py** - 1 violation(s)

[!] WARNING (line 44)
Line 44: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    def get_progress_line(self) -> str:
        """Get just the progress line for display in header"""
        if self.current_state is None:
            self.current_state = self._load_state()
        
```

---

## chain_dependencies_properly
**repl_session.py** - 9 violation(s)

[!] WARNING (line 719)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return self._execute_action_instructions(action_name)
    
    def _handle_submit_command(self) -> REPLCommandResponse:
        """Submit answers/evidence for current action."""
```

[!] WARNING (line 764)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        )
    
    def _handle_confirm_command(self) -> REPLCommandResponse:
        """Confirm/complete current action and advance to next."""
```

[!] WARNING (line 764)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        )
    
    def _handle_confirm_command(self) -> REPLCommandResponse:
        """Confirm/complete current action and advance to next."""
```

[!] WARNING (line 764)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        )
    
    def _handle_confirm_command(self) -> REPLCommandResponse:
        """Confirm/complete current action and advance to next."""
```

[!] WARNING (line 864)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
            return self._execute_action_instructions(next_action.action_name)
    
    def _handle_back_command(self) -> REPLCommandResponse:
        """Stub: Move back to previous action."""
```

[!] WARNING (line 864)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
            return self._execute_action_instructions(next_action.action_name)
    
    def _handle_back_command(self) -> REPLCommandResponse:
        """Stub: Move back to previous action."""
```

[!] WARNING (line 946)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return self._execute_action_instructions(new_action_name)
    
    def _handle_next_command(self) -> REPLCommandResponse:
        """Move forward to next action."""
```

[!] WARNING (line 946)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return self._execute_action_instructions(new_action_name)
    
    def _handle_next_command(self) -> REPLCommandResponse:
        """Move forward to next action."""
```

[!] WARNING (line 1053)
Passing self.current_state as parameter to _save_state(). Access it directly in the method through self.current_state instead.

```python
        return self._execute_action_instructions(next_action_name)
    
    def _execute_action_instructions(self, action_name: str) -> REPLCommandResponse:
        """Execute action and get instructions (mock)."""
```

---

## eliminate_duplication
**repl_session.py** - 8 violation(s)

[X] ERROR (line 70)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (get_progress_line:70-82):
```python
current_action = self.current_state.get('current_action', '')
action_phase = self.current_state.get('action_phase', 'not_started')
stage_map = {'not_started': 'instructions', 'instructions_given': 'in...
```

Location (display_current_state:123-128):
```python
current_behavior = self.current_state.get('current_behavior', '')
current_action = self.current_state.get('current_action', '')
working_dir = self.current_state.get('working_directory', '')
action_pha...
```

[X] ERROR (line 159)
Duplicate code blocks detected (3 locations) - extract to helper function.

Location (display_current_state:159-168):
```python
behavior_obj_name = behavior_obj.name
if behavior_obj_name in completed_behaviors:
    behavior_parts.append(f'{behavior_obj_name} [OK]')
elif behavior_obj_name == behavior_name:
    behavior_parts.ap...
```

Location (display_current_state:183-191):
```python
action_name_str = action_obj.action_name
if action_name_str in completed_action_names:
    action_parts.append(f'{action_name_str} [OK]')
elif action_name_str == action_name:
    action_parts.append(f...
```

Location (_generate_breadcrumbs:257-264):
```python
action_name = action.action_name
if action_name in completed_action_names:
    breadcrumb_parts.append(f'{action_name} [OK]')
elif action_name == current_action_name:
    breadcrumb_parts.append(f'{ac...
```

[X] ERROR (line 412)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_handle_behavior_command:412-423):
```python
available_behaviors = [b.name for b in self.bot.behaviors]
behaviors_list = ', '.join(available_behaviors)
output_lines = [f"ERROR: behavior '{behavior_name}' not found", f'Available behaviors: {behav...
```

Location (_handle_action_command:524-535):
```python
available_actions = [a.action_name for a in behavior.actions._actions]
actions_list = ', '.join(available_actions)
output_lines = [f"ERROR: action '{action_name}' not found in behavior '{behavior_name...
```

[X] ERROR (line 572)
Duplicate code blocks detected (4 locations) - extract to helper function.

Location (_render_available_behaviors:572-591):
```python
behaviors_list = ' | '.join(behavior_names)
action_descriptions = {'clarify': 'Gather context and answer key questions', 'strategy': 'Plan the approach for this behavior', 'build': 'Execute the main w...
```

Location (_render_available_behaviors:592-597):
```python
output_lines.append('')
output_lines.append('    operations  -> instructions | submit | confirm')
output_lines.append('')
output_lines.append('  Examples:')
output_lines.append('    .                 ...
```

Location (_render_available_behaviors:598-603):
```python
output_lines.append('    action                      -> e.g., build - jump to action and execute first operation')
output_lines.append('    operation                   -> e.g., submit - jump to operat...
```

Location (_render_available_behaviors:604-609):
```python
output_lines.append('    status      - Show full workflow hierarchy')
output_lines.append('    back        - Go back to previous action')
output_lines.append('    current     - Re-execute current oper...
```

[X] ERROR (line 721)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_handle_submit_command:721-733):
```python
if not self.current_state or not self.current_state.get('current_action'):
    return REPLCommandResponse(output='ERROR: No current action to submit for', response='ERROR: No current action', status='...
```

Location (_execute_action_instructions:1055-1067):
```python
if not self.current_state or not self.current_state.get('current_action'):
    return REPLCommandResponse(output='ERROR: No current action', response='ERROR: No current action', status='error')
curren...
```

[X] ERROR (line 766)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_handle_confirm_command:766-782):
```python
if not self.current_state or not self.current_state.get('current_action'):
    return REPLCommandResponse(output='ERROR: No current action to confirm', response='ERROR: No current action', status='err...
```

Location (_handle_next_command:948-965):
```python
if not self.current_state or not self.current_state.get('current_action'):
    return REPLCommandResponse(output='ERROR: No current action', response='ERROR: No current action', status='error')
curren...
```

[X] ERROR (line 955)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_handle_next_command:955-969):
```python
current_action_name = self.current_state['current_action'].split('.')[-1]
behavior_name = self.current_state['current_behavior'].split('.')[-1]
behavior = self._get_behavior(behavior_name)
if not beha...
```

Location (display_confirm_prompt:1114-1126):
```python
behavior_name = self.current_state['current_behavior'].split('.')[-1]
action_name = current_action.split('.')[-1]
behavior = self._get_behavior(behavior_name)
if not behavior:
    return REPLStateDisp...
```

[X] ERROR (line 1286)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_handle_action_shortcut:1286-1293):
```python
available_actions = [a.action_name for a in behavior.actions._actions]
actions_list = ', '.join(available_actions)
return REPLCommandResponse(output=f"ERROR: action '{action_name}' not found in behavi...
```

Location (_handle_action_shortcut:1320-1327):
```python
available_actions = [a.action_name for a in behavior.actions._actions]
actions_list = ', '.join(available_actions)
return REPLCommandResponse(output=f"ERROR: action '{action_name}' not found in behavi...
```

---


## Cross-File Duplication Analysis
Scanning 3 files...
Extracted 363 code blocks
Starting 65703 pairwise comparisons...
Comparing: 5% (3,286/65,703) - 0 violations - ETA: 18s  
Comparing: 10% (6,571/65,703) - 0 violations - ETA: 10s  
Comparing: 15% (9,856/65,703) - 0 violations - ETA: 10s  
Comparing: 20% (13,141/65,703) - 0 violations - ETA: 11s  
Comparing: 25% (16,426/65,703) - 0 violations - ETA: 10s  
Comparing: 30% (19,711/65,703) - 0 violations - ETA: 8s  
Comparing: 35% (22,997/65,703) - 0 violations - ETA: 6s  
Comparing: 40% (26,282/65,703) - 0 violations - ETA: 5s  
Comparing: 45% (29,567/65,703) - 0 violations - ETA: 4s  
Comparing: 50% (32,852/65,703) - 0 violations - ETA: 3s  
Comparing: 55% (36,137/65,703) - 0 violations - ETA: 2s  
Comparing: 60% (39,422/65,703) - 0 violations - ETA: 2s  
Comparing: 65% (42,707/65,703) - 0 violations - ETA: 1s  
Comparing: 70% (45,993/65,703) - 0 violations - ETA: 1s  
Comparing: 75% (49,278/65,703) - 0 violations - ETA: 1s  
Comparing: 80% (52,563/65,703) - 0 violations - ETA: 0s  
Comparing: 85% (55,848/65,703) - 0 violations - ETA: 0s  
Comparing: 90% (59,133/65,703) - 0 violations - ETA: 0s  
Comparing: 95% (62,418/65,703) - 0 violations - ETA: 0s  
Comparing: 100% (65,703/65,703) - 0 violations - ETA: 0s  
Complete: 65703 comparisons, 0 violations

## keep_classes_small_with_single_responsibility
**repl_session.py** - 1 violation(s)

[!] WARNING (line 14)
Class "REPLSession" is 1327 lines - should be under 300 lines (extract related methods into separate classes)

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
**repl_main.py** - 1 violation(s)

[!] WARNING (line 69)
Function "main" is 79 lines - should be under 20 lines (extract complex logic to helper functions)

```python


def main():
    """Launch interactive REPL session"""
    
    # Bot directory was set at module level to always be story_bot
    # (where behaviors are loaded from)
    bot_name = 'story_bot'
    
    # Get workspace directory (where your stories/documents are)
    workspace_directory = get_workspace_directory()
    
    # Create bot instance
    bot_config_path = bot_directory / 'bot_config.json'
    
    if not bot_config_path.exists():
        print(f"ERROR: Bot config not found at {bot_config_path}")
        print("Please ensure you're running from the correct directory.")
        sys.exit(1)
    
    try:
        bot = Bot(
            bot_name=bot_name,
            bot_directory=bot_directory,
            config_path=bot_config_path
        )
    except Exception as e:
        print(f"ERROR: Failed to initialize bot: {e}")
        sys.exit(1)
    
    # Create REPL session
    repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
    
    # Get progress for header
    progress_line = repl_session.get_progress_line()
    
    # Print header with progress
    print("=" * 60)
    print(f"{bot_name.upper()} CLI")
    print("-" * 60)
    print(f"Bot Path: {bot_directory}")
    print(f"Work Path: {workspace_directory}")
    print(progress_line)
    print("=" * 60)
    
    # Display rest of state (commands menu)
    state_display = repl_session.display_current_state()
    print(state_display.output)
    
    # Check TTY
    # ... (truncated)
```

---

## keep_functions_small_focused
**repl_session.py** - 4 violation(s)

[!] WARNING (line 42)
Function "get_progress_line" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        )
    
    def get_progress_line(self) -> str:
        """Get just the progress line for display in header"""
        if self.current_state is None:
            self.current_state = self._load_state()
        
        if self.current_state is None:
            # Initialize to first behavior/action/operation
            if self.bot and self.bot.behaviors and len(self.bot.behaviors._behaviors) > 0:
                first_behavior = self.bot.behaviors._behaviors[0]
                first_action = first_behavior.actions._actions[0] if first_behavior.actions._actions else None
                
                if first_action:
                    state_data = {
                        'current_behavior': f'{self.bot.bot_name}.{first_behavior.name}',
                        'current_action': f'{self.bot.bot_name}.{first_behavior.name}.{first_action.action_name}',
                        'action_phase': 'not_started',
                        'working_directory': str(self.workspace_directory),
                        'completed_actions': [],
                        'completed_behaviors': []
                    }
                    self._save_state(state_data)
                    self.current_state = state_data
                    # Now get the progress line from the initialized state
                    return self.get_progress_line()
            
            # Fallback
            return "No active workflow"
        
        current_action = self.current_state.get('current_action', '')
        action_phase = self.current_state.get('action_phase', 'not_started')
        
        # Map action_phase to stage name
        stage_map = {
            'not_started': 'instructions',
            'instructions_given': 'instructions',
            'submitted': 'submitted'
        }
        stage_name = stage_map.get(action_phase, action_phase)
        
        # Remove bot name prefix from current_action for cleaner display
        progress_path = current_action.split('.', 1)[1] if '.' in current_action else current_action
        
        return f"Progress: {progress_path}.{stage_name}"
    
```

[!] WARNING (line 86)
Function "display_current_state" is 98 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return f"Progress: {progress_path}.{stage_name}"
    
    def display_current_state(self, full=False) -> REPLStateDisplay:
        if self.current_state is None:
            # Initialize to first behavior, first action, first operation
            if self.bot and self.bot.behaviors and len(self.bot.behaviors._behaviors) > 0:
                first_behavior = self.bot.behaviors._behaviors[0]
                first_action = first_behavior.actions._actions[0] if first_behavior.actions._actions else None
                
                if first_action:
                    full_behavior = f"{self.bot.bot_name}.{first_behavior.name}"
                    full_action = f"{full_behavior}.{first_action.action_name}"
                    
                    state_data = {
                        'current_behavior': full_behavior,
                        'current_action': full_action,
                        'action_phase': 'not_started',
                        'working_directory': str(self.workspace_directory),
                        'timestamp': datetime.now().isoformat(),
                        'completed_actions': [],
                        'completed_behaviors': []
                    }
                    self._save_state(state_data)
                    self.current_state = state_data
                    # Now display the initialized state
                    return self.display_current_state(full=full)
            
            # Fallback if no behaviors available
            output_lines = [
                "No behaviors available",
                "",
                "  help          - Show detailed help",
                "  exit          - Exit REPL"
            ]
            return REPLStateDisplay(
                output="\n".join(output_lines),
                state_loaded=False
            )
        
        current_behavior = self.current_state.get('current_behavior', '')
        current_action = self.current_state.get('current_action', '')
        working_dir = self.current_state.get('working_directory', '')
        action_phase = self.current_state.get('action_phase', 'not_started')
        
        behavior_name = current_behavior.split('.')[-1] if current_behavior else None
        action_name = current_action.split('.')[-1] if current_action else None
        
        # Map action_phase to stage name
        stage_map = {
            'not_started': 'instructions',
    # ... (truncated)
```

[!] WARNING (line 271)
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

[!] WARNING (line 1105)
Function "display_confirm_prompt" is 26 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        )
    
    def display_confirm_prompt(self) -> REPLStateDisplay:
        """Stub: Display confirmation prompt after action execution."""
        if not self.current_state or not self.current_state.get('current_action'):
            return REPLStateDisplay(
                output="ERROR: No current action",
                state_loaded=False
            )
        
        current_action = self.current_state['current_action']
        behavior_name = self.current_state['current_behavior'].split('.')[-1]
        action_name = current_action.split('.')[-1]
        
        # Get next action
        behavior = self._get_behavior(behavior_name)
        if not behavior:
            return REPLStateDisplay(
                output="ERROR: behavior not found",
                state_loaded=False
            )
        
        actions = behavior.actions._actions
        current_index = -1
        for i, action in enumerate(actions):
            if action.action_name == action_name:
                current_index = i
                break
        
        next_action_name = "none"
        if current_index >= 0 and current_index < len(actions) - 1:
            next_action_name = actions[current_index + 1].action_name
        
        output_lines = [
            f"EXECUTED {behavior_name}.{action_name}",
            "Results:",
            "[Mock results - not executing real action]",
            f"Continue to next action ({next_action_name})? (y/n/review)"
        ]
        
        return REPLStateDisplay(
            output="\n".join(output_lines),
            state_loaded=True,
            current_behavior=self.current_state['current_behavior'],
            current_action=current_action
        )
    
```

---

## maintain_vertical_density
**repl_main.py** - 1 violation(s)

[i] INFO (line 69)
Function "main" is 98 lines - consider improving vertical density by declaring variables near usage

```python


def main():
    """Launch interactive REPL session"""
    
    # Bot directory was set at module level to always be story_bot
    # (where behaviors are loaded from)
    bot_name = 'story_bot'
    
    # Get workspace directory (where your stories/documents are)
    # ... (truncated)
```

---

## maintain_vertical_density
**repl_session.py** - 7 violation(s)

[i] INFO (line 86)
Function "display_current_state" is 152 lines - consider improving vertical density by declaring variables near usage

```python
        return f"Progress: {progress_path}.{stage_name}"
    
    def display_current_state(self, full=False) -> REPLStateDisplay:
        if self.current_state is None:
            # Initialize to first behavior, first action, first operation
            if self.bot and self.bot.behaviors and len(self.bot.behaviors._behaviors) > 0:
                first_behavior = self.bot.behaviors._behaviors[0]
                first_action = first_behavior.actions._actions[0] if first_behavior.actions._actions else None
                
                if first_action:
    # ... (truncated)
```

[i] INFO (line 271)
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

[i] INFO (line 764)
Function "_handle_confirm_command" is 99 lines - consider improving vertical density by declaring variables near usage

```python
        )
    
    def _handle_confirm_command(self) -> REPLCommandResponse:
        """Confirm/complete current action and advance to next."""
        if not self.current_state or not self.current_state.get('current_action'):
            return REPLCommandResponse(
                output="ERROR: No current action to confirm",
                response="ERROR: No current action",
                status="error"
            )
    # ... (truncated)
```

[i] INFO (line 864)
Function "_handle_back_command" is 81 lines - consider improving vertical density by declaring variables near usage

```python
            return self._execute_action_instructions(next_action.action_name)
    
    def _handle_back_command(self) -> REPLCommandResponse:
        """Stub: Move back to previous action."""
        if not self.current_state or not self.current_state.get('current_action'):
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
    # ... (truncated)
```

[i] INFO (line 946)
Function "_handle_next_command" is 106 lines - consider improving vertical density by declaring variables near usage

```python
        return self._execute_action_instructions(new_action_name)
    
    def _handle_next_command(self) -> REPLCommandResponse:
        """Move forward to next action."""
        if not self.current_state or not self.current_state.get('current_action'):
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
    # ... (truncated)
```

[i] INFO (line 1053)
Function "_execute_action_instructions" is 51 lines - consider improving vertical density by declaring variables near usage

```python
        return self._execute_action_instructions(next_action_name)
    
    def _execute_action_instructions(self, action_name: str) -> REPLCommandResponse:
        """Execute action and get instructions (mock)."""
        if not self.current_state or not self.current_state.get('current_action'):
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
    # ... (truncated)
```

[i] INFO (line 1246)
Function "_handle_action_shortcut" is 95 lines - consider improving vertical density by declaring variables near usage

```python
            return {'type': 'story', 'value': [args]}
    
    def _handle_action_shortcut(self, action_name: str, subcommand: str) -> REPLCommandResponse:
        """Handle action shortcuts like 'clarify instructions', 'clarify submit', or 'clarify confirm'."""
        subcommand = subcommand.strip().lower()
        
        # If no subcommand, cycle through: instructions -> submit -> confirm
        if not subcommand:
            action_phase = self.current_state.get('action_phase', 'not_started')
            if action_phase == 'not_started':
    # ... (truncated)
```

---

## never_swallow_exceptions
**repl_main.py** - 1 violation(s)

[X] ERROR (line 57)
Except block only contains pass at line 57 - exceptions must be logged or rethrown, never swallowed

```python
            elif 'WORKING_AREA' in bot_config:
                os.environ['WORKING_AREA'] = bot_config['WORKING_AREA']
        except:
            pass
    
```

---

## place_imports_at_top
**repl_main.py** - 7 violation(s)

[X] ERROR (line 27)
Import statement found after non-import code. Move all imports to the top of the file.

```python
    exit                - Exit REPL
"""
import sys
import os
```

[X] ERROR (line 28)
Import statement found after non-import code. Move all imports to the top of the file.

```python
"""
import sys
import os
import json
```

[X] ERROR (line 29)
Import statement found after non-import code. Move all imports to the top of the file.

```python
import sys
import os
import json
from pathlib import Path
```

[X] ERROR (line 30)
Import statement found after non-import code. Move all imports to the top of the file.

```python
import os
import json
from pathlib import Path

```

[X] ERROR (line 64)
Import statement found after non-import code. Move all imports to the top of the file.

```python
        os.environ['WORKING_AREA'] = str(workspace_root)

from agile_bot.bots.base_bot.src.bot.bot import Bot
from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
```

[X] ERROR (line 65)
Import statement found after non-import code. Move all imports to the top of the file.

```python

from agile_bot.bots.base_bot.src.bot.bot import Bot
from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
from agile_bot.bots.base_bot.src.bot.workspace import get_bot_directory, get_workspace_directory
```

[X] ERROR (line 66)
Import statement found after non-import code. Move all imports to the top of the file.

```python
from agile_bot.bots.base_bot.src.bot.bot import Bot
from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
from agile_bot.bots.base_bot.src.bot.workspace import get_bot_directory, get_workspace_directory

```

---

## provide_meaningful_context
**repl_main.py** - 3 violation(s)

[!] WARNING (line 104)
Line 104 contains magic number - replace with named constant

```python
    # Print header with progress
    print("=" * 60)
    print(f"{bot_name.upper()} CLI")
```

[!] WARNING (line 106)
Line 106 contains magic number - replace with named constant

```python
    print(f"{bot_name.upper()} CLI")
    print("-" * 60)
    print(f"Bot Path: {bot_directory}")
```

[!] WARNING (line 110)
Line 110 contains magic number - replace with named constant

```python
    print(progress_line)
    print("=" * 60)
    
```

---

## refactor_completely_not_partially
**repl_session.py** - 2 violation(s)

[!] WARNING (line 67)
Fallback/legacy support code found (comment at line 67, code at line 68) - complete refactoring by removing old pattern support

[!] WARNING (line 111)
Fallback/legacy support code found (comment at line 111, code at line 112) - complete refactoring by removing old pattern support

---

## simplify_control_flow
**repl_main.py** - 1 violation(s)

[!] WARNING (line 69)
Function "main" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python


def main():
    """Launch interactive REPL session"""
    
    # Bot directory was set at module level to always be story_bot
    # (where behaviors are loaded from)
    bot_name = 'story_bot'
    
    # Get workspace directory (where your stories/documents are)
    workspace_directory = get_workspace_directory()
    
    # Create bot instance
    bot_config_path = bot_directory / 'bot_config.json'
    
    # ... (truncated)
```

---

## simplify_control_flow
**repl_session.py** - 3 violation(s)

[!] WARNING (line 86)
Function "display_current_state" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

```python
        return f"Progress: {progress_path}.{stage_name}"
    
    def display_current_state(self, full=False) -> REPLStateDisplay:
        if self.current_state is None:
            # Initialize to first behavior, first action, first operation
            if self.bot and self.bot.behaviors and len(self.bot.behaviors._behaviors) > 0:
                first_behavior = self.bot.behaviors._behaviors[0]
                first_action = first_behavior.actions._actions[0] if first_behavior.actions._actions else None
                
                if first_action:
                    full_behavior = f"{self.bot.bot_name}.{first_behavior.name}"
                    full_action = f"{full_behavior}.{first_action.action_name}"
                    
                    state_data = {
                        'current_behavior': full_behavior,
    # ... (truncated)
```

[!] WARNING (line 271)
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

[!] WARNING (line 1246)
Function "_handle_action_shortcut" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
            return {'type': 'story', 'value': [args]}
    
    def _handle_action_shortcut(self, action_name: str, subcommand: str) -> REPLCommandResponse:
        """Handle action shortcuts like 'clarify instructions', 'clarify submit', or 'clarify confirm'."""
        subcommand = subcommand.strip().lower()
        
        # If no subcommand, cycle through: instructions -> submit -> confirm
        if not subcommand:
            action_phase = self.current_state.get('action_phase', 'not_started')
            if action_phase == 'not_started':
                subcommand = "instructions"
            elif action_phase == 'instructions_given':
                subcommand = "submit"
            elif action_phase == 'submitted':
                subcommand = "confirm"
    # ... (truncated)
```

---

## stop_writing_useless_comments
**repl_main.py** - 6 violation(s)

[X] ERROR (line 70)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

def main():
    """Launch interactive REPL session"""
    
```

[X] ERROR (line 76)
Useless comment: "# Get workspace directory (where your stories/documents are)" - delete it or improve the code instead

```python
    bot_name = 'story_bot'
    
    # Get workspace directory (where your stories/documents are)
    workspace_directory = get_workspace_directory()
```

[X] ERROR (line 79)
Useless comment: "# Create bot instance" - delete it or improve the code instead

```python
    workspace_directory = get_workspace_directory()
    
    # Create bot instance
    bot_config_path = bot_directory / 'bot_config.json'
```

[X] ERROR (line 97)
Useless comment: "# Create REPL session" - delete it or improve the code instead

```python
        sys.exit(1)
    
    # Create REPL session
    repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
```

[X] ERROR (line 100)
Useless comment: "# Get progress for header" - delete it or improve the code instead

```python
    repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
    
    # Get progress for header
    progress_line = repl_session.get_progress_line()
```

[X] ERROR (line 146)
Useless comment: "# Execute command" - delete it or improve the code instead

```python
                continue
            
            # Execute command
            response = repl_session.read_and_execute_command(command)
```

---

## stop_writing_useless_comments
**repl_results.py** - 3 violation(s)

[X] ERROR (line 16)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
@dataclass
class REPLStateDisplay:
    """
    Result of displaying current REPL state.
    
    Returned by: REPLSession.display_current_state()
    
    Represents the REPL's current position in the workflow,
    including behavior, action, and breadcrumbs.
    """
    output: str
```

[X] ERROR (line 33)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
@dataclass
class REPLCommandResponse:
    """
    Result of executing a REPL command.
    
    Returned by: REPLSession.read_and_execute_command()
    
    Contains the command's output, status, and any state changes.
    """
    output: str
```

[X] ERROR (line 52)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
@dataclass
class TTYDetectionResult:
    """
    Result of TTY detection.
    
    Returned by: REPLSession.detect_tty()
    
    Determines whether interactive prompts should be enabled
    based on whether stdin is a TTY.
    """
    tty_detected: bool
```

---

## stop_writing_useless_comments
**repl_session.py** - 30 violation(s)

[X] ERROR (line 43)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_progress_line(self) -> str:
        """Get just the progress line for display in header"""
        if self.current_state is None:
```

[X] ERROR (line 452)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _navigate_to_action(self, behavior_name: str, action_name: str, full_action: str, state_updates: Dict = None):
        """Navigate to an action without executing. Updates state only."""
        state_data = dict(self.current_state) if self.current_state else {}
```

[X] ERROR (line 475)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _update_state_and_generate_response(self, behavior_name: str, action_name: str, full_action: str, state_updates: Dict = None) -> REPLCommandResponse:
        """Navigate to an action and execute instructions operation."""
        self._navigate_to_action(behavior_name, action_name, full_action, state_updates)
```

[X] ERROR (line 683)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_current_command(self) -> REPLCommandResponse:
        """Re-execute the current operation based on action_phase."""
        if not self.current_state or not self.current_state.get('current_action'):
```

[X] ERROR (line 705)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_instructions_command(self) -> REPLCommandResponse:
        """Get instructions for current action."""
        if not self.current_state or not self.current_state.get('current_action'):
```

[X] ERROR (line 720)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_submit_command(self) -> REPLCommandResponse:
        """Submit answers/evidence for current action."""
        if not self.current_state or not self.current_state.get('current_action'):
```

[X] ERROR (line 765)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_confirm_command(self) -> REPLCommandResponse:
        """Confirm/complete current action and advance to next."""
        if not self.current_state or not self.current_state.get('current_action'):
```

[X] ERROR (line 865)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_back_command(self) -> REPLCommandResponse:
        """Stub: Move back to previous action."""
        if not self.current_state or not self.current_state.get('current_action'):
```

[X] ERROR (line 947)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_next_command(self) -> REPLCommandResponse:
        """Move forward to next action."""
        if not self.current_state or not self.current_state.get('current_action'):
```

[X] ERROR (line 1054)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _execute_action_instructions(self, action_name: str) -> REPLCommandResponse:
        """Execute action and get instructions (mock)."""
        if not self.current_state or not self.current_state.get('current_action'):
```

[X] ERROR (line 1106)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def display_confirm_prompt(self) -> REPLStateDisplay:
        """Stub: Display confirmation prompt after action execution."""
        if not self.current_state or not self.current_state.get('current_action'):
```

[X] ERROR (line 1247)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_action_shortcut(self, action_name: str, subcommand: str) -> REPLCommandResponse:
        """Handle action shortcuts like 'clarify instructions', 'clarify submit', or 'clarify confirm'."""
        subcommand = subcommand.strip().lower()
```

[X] ERROR (line 151)
Useless comment: "# Get completed behaviors from state" - delete it or improve the code instead

```python
            output_lines.append(f"Progress: {progress_path}.{stage_name}")
            
            # Get completed behaviors from state
            completed_behaviors = self.current_state.get('completed_behaviors', [])
```

[X] ERROR (line 448)
Useless comment: "# Execute the first action's first operation (instructions)" - delete it or improve the code instead

```python
        self.current_state = state_data
        
        # Execute the first action's first operation (instructions)
        return self._execute_action_instructions(first_action.action_name)
```

[X] ERROR (line 478)
Useless comment: "# Execute the action's first operation (instructions)" - delete it or improve the code instead

```python
        self._navigate_to_action(behavior_name, action_name, full_action, state_updates)
        
        # Execute the action's first operation (instructions)
        return self._execute_action_instructions(action_name)
```

[X] ERROR (line 716)
Useless comment: "# Execute to get instructions" - delete it or improve the code instead

```python
        action_name = current_action.split('.')[-1]
        
        # Execute to get instructions
        return self._execute_action_instructions(action_name)
```

[X] ERROR (line 794)
Useless comment: "# Get next action" - delete it or improve the code instead

```python
        })
        
        # Get next action
        actions = behavior.actions._actions
```

[X] ERROR (line 842)
Useless comment: "# Update state to next behavior/action" - delete it or improve the code instead

```python
                full_action = f"{full_behavior}.{next_action_name}"
                
                # Update state to next behavior/action
                self.current_state['current_behavior'] = full_behavior
```

[X] ERROR (line 849)
Useless comment: "# Execute the next behavior's first action's instructions" - delete it or improve the code instead

```python
                self._save_state(self.current_state)
                
                # Execute the next behavior's first action's instructions
                return self._execute_action_instructions(next_action_name)
```

[X] ERROR (line 861)
Useless comment: "# Execute the next action's instructions" - delete it or improve the code instead

```python
            self._save_state(self.current_state)
            
            # Execute the next action's instructions
            return self._execute_action_instructions(next_action.action_name)
```

[X] ERROR (line 889)
Useless comment: "# Get previous behavior" - delete it or improve the code instead

```python
                )
            
            # Get previous behavior
            prev_behavior_name = completed_behaviors[-1]
```

[X] ERROR (line 920)
Useless comment: "# Update state to previous behavior/action" - delete it or improve the code instead

```python
                })
            
            # Update state to previous behavior/action
            self.current_state['current_behavior'] = full_behavior
```

[X] ERROR (line 943)
Useless comment: "# Execute the action's first operation (instructions)" - delete it or improve the code instead

```python
        new_action_name = new_action_state.split('.')[-1]
        
        # Execute the action's first operation (instructions)
        return self._execute_action_instructions(new_action_name)
```

[X] ERROR (line 958)
Useless comment: "# Get current behavior" - delete it or improve the code instead

```python
        behavior_name = self.current_state['current_behavior'].split('.')[-1]
        
        # Get current behavior
        behavior = self._get_behavior(behavior_name)
```

[X] ERROR (line 1021)
Useless comment: "# Update state to next behavior/action" - delete it or improve the code instead

```python
            full_action = f"{full_behavior}.{next_action_name}"
            
            # Update state to next behavior/action
            self.current_state['current_behavior'] = full_behavior
```

[X] ERROR (line 1029)
Useless comment: "# Execute the next behavior's first action's instructions" - delete it or improve the code instead

```python
            self._save_state(self.current_state)
            
            # Execute the next behavior's first action's instructions
            return self._execute_action_instructions(next_action_name)
```

[X] ERROR (line 1050)
Useless comment: "# Execute the next action's first operation (instructions)" - delete it or improve the code instead

```python
        self._save_state(self.current_state)
        
        # Execute the next action's first operation (instructions)
        return self._execute_action_instructions(next_action_name)
```

[X] ERROR (line 1117)
Useless comment: "# Get next action" - delete it or improve the code instead

```python
        action_name = current_action.split('.')[-1]
        
        # Get next action
        behavior = self._get_behavior(behavior_name)
```

[X] ERROR (line 1298)
Useless comment: "# Execute submit" - delete it or improve the code instead

```python
            self._navigate_to_action(behavior_name, action_name, full_action)
            
            # Execute submit
            return self._handle_submit_command()
```

[X] ERROR (line 1332)
Useless comment: "# Execute confirm" - delete it or improve the code instead

```python
            self._navigate_to_action(behavior_name, action_name, full_action)
            
            # Execute confirm
            return self._handle_confirm_command()
```

---

Completed: 2025-12-23 18:45:56
Total violations: 89
Scanners executed: 30
