# Validation Status - code
Started: 2025-12-27 01:00:31
Files: 25

## avoid_excessive_guards
**command_parser.py** - 1 violation(s)

[!] WARNING (line 65)
Line 65: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

```python
        
        # Treat unrecognized single-word commands as potential behavior names (dot notation with just behavior)
        if not args:  # Single word, no arguments
            return ParsedCommand(command_type="dot_notation", behavior=command)
        
```

---

## avoid_excessive_guards
**repl_session.py** - 1 violation(s)

[!] WARNING (line 390)
Line 390: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

```python
    def parse_command_parameters(self, args: str) -> Dict[str, Any]:
        params = {}
        if not args:
            return params
        
```

---

## avoid_excessive_guards
**meta.py** - 1 violation(s)

[!] WARNING (line 27)
Line 27: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

```python
        args = args.strip()
        
        if not args:
            output = self.help_resource.main_help
        else:
            if not self.has_current_behavior:
                return self.error_no_current_behavior()
            action_help = self.help_resource.action_help(self.current_behavior_name, args)
            if not action_help:
                behavior_help = self.help_resource.behavior_help(self.current_behavior_name)
                if not behavior_help:
                    return self.error_behavior_not_found(self.current_behavior_name)
                output = f"ERROR: Action '{args}' not found"
            else:
                output = action_help.help_text
        
```

---

## delegate_to_lowest_level
**repl_help.py** - 1 violation(s)

[i] INFO (line 24)
Method "format_as_lines" in class "StageCollection" iterates through "_stages" instead of delegating to collection class. Delegate to collection class instead.

---

## eliminate_duplication
**status_display.py** - 1 violation(s)

[X] ERROR (line 88)
Duplicate code detected: functions __init__, reset have identical bodies - extract to shared function

---

## eliminate_duplication
**navigation.py** - 2 violation(s)

[X] ERROR (line 46)
Duplicate code detected: functions _validate_navigation_state, _validate_navigation_state have identical bodies - extract to shared function

[X] ERROR (line 59)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (execute:59-78):
```python
behavior = self.current_behavior
next_act = self.next_action
if next_act:
    behavior.actions.navigate_to(next_act.name)
    return self.display_navigation()
next_beh = self.next_behavior
if next_beh...
```

Location (execute:95-114):
```python
error = self._validate_navigation_state()
if error:
    return error
behavior = self.current_behavior
prev_act = self.previous_action
if prev_act:
    behavior.actions.navigate_to(prev_act.name)
    r...
```

---

## eliminate_duplication
**repl_command.py** - 1 violation(s)

[X] ERROR (line 12)
Duplicate code detected: functions name, execute have identical bodies - extract to shared function

---


## Cross-File Duplication Analysis
Scanning 25 files...
Extracted 340 code blocks
Starting 57630 pairwise comparisons...
Comparing: 5% (2,882/57,630) - 3 violations - ETA: 18s  
Comparing: 10% (5,763/57,630) - 9 violations - ETA: 15s  
Found 10 violations so far...
Comparing: 15% (8,645/57,630) - 13 violations - ETA: 14s  
Comparing: 20% (11,526/57,630) - 14 violations - ETA: 14s  
Comparing: 25% (14,408/57,630) - 14 violations - ETA: 15s  
Comparing: 30% (17,289/57,630) - 14 violations - ETA: 15s  
Comparing: 35% (20,171/57,630) - 14 violations - ETA: 14s  
Comparing: 40% (23,052/57,630) - 14 violations - ETA: 13s  
Comparing: 45% (25,934/57,630) - 14 violations - ETA: 13s  
Comparing: 50% (28,815/57,630) - 14 violations - ETA: 11s  
Comparing: 55% (31,697/57,630) - 14 violations - ETA: 10s  
Comparing: 60% (34,578/57,630) - 14 violations - ETA: 9s  
Comparing: 65% (37,460/57,630) - 14 violations - ETA: 8s  
Comparing: 70% (40,341/57,630) - 14 violations - ETA: 7s  
Comparing: 75% (43,223/57,630) - 14 violations - ETA: 5s  
Comparing: 80% (46,104/57,630) - 14 violations - ETA: 4s  
Comparing: 85% (48,986/57,630) - 14 violations - ETA: 3s  
Comparing: 90% (51,867/57,630) - 14 violations - ETA: 2s  
Comparing: 95% (54,749/57,630) - 14 violations - ETA: 1s  
Comparing: 100% (57,630/57,630) - 15 violations - ETA: 0s  
Complete: 57630 comparisons, 15 violations

## keep_classes_small_with_single_responsibility
**repl_session.py** - 1 violation(s)

[!] WARNING (line 23)
Class "REPLSession" is 526 lines - should be under 300 lines (extract related methods into separate classes)

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

## keep_classes_small_with_single_responsibility
**workflow.py** - 1 violation(s)

[!] WARNING (line 10)
Class "WorkflowCommand" is 340 lines - should be under 300 lines (extract related methods into separate classes)

```python


class WorkflowCommand(InstructionDisplayCommand):
    @property
    def action_phase(self) -> str:
        return self.session.action_phase
    
    @property
    def is_submitted(self) -> bool:
        return self.action_phase == 'submitted'
    # ... (truncated)
```

---

## keep_functions_small_focused
**command_parser.py** - 1 violation(s)

[!] WARNING (line 36)
Function "parse_command" is 23 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    OPERATIONS = ['instructions', 'submit', 'confirm']
    
    def parse_command(self, input_line: str) -> ParsedCommand:
        if not input_line or input_line.strip() == "":
            return ParsedCommand(command_type="empty")
        
        input_line = input_line.strip()
        
        if input_line in self.META_COMMANDS:
            return ParsedCommand(command_type="meta", operation=input_line)
        
        if input_line in self.WORKFLOW_COMMANDS:
            return ParsedCommand(command_type="workflow", operation=input_line)
        
        if '.' in input_line:
            return self._parse_dot_notation(input_line)
        
        if input_line in self.OPERATIONS:
            return ParsedCommand(command_type="operation", operation=input_line)
        
        parts = input_line.split(maxsplit=1)
        command = parts[0]
        args = parts[1] if len(parts) > 1 else ""
        
        if command in self.META_COMMANDS:
            return ParsedCommand(command_type="meta", operation=command, args=args)
        
        if command in self.OPERATIONS:
            return ParsedCommand(command_type="operation", operation=command, args=args)
        
        # Treat unrecognized single-word commands as potential behavior names (dot notation with just behavior)
        if not args:  # Single word, no arguments
            return ParsedCommand(command_type="dot_notation", behavior=command)
        
        return ParsedCommand(command_type="unknown", args=input_line)
    
```

---

## keep_functions_small_focused
**repl_help.py** - 1 violation(s)

[!] WARNING (line 215)
Function "main_help" is 53 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    
    @property
    def main_help(self) -> str:
        behaviors_list = " | ".join(self.behavior_names)
        
        lines = [
            "Core Commands:",
            "  echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation",
            "  echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action",
            "",
            "  Available Components:",
            f"    behaviors   -> {behaviors_list}",
            "",
            "    actions:"
        ]
        
        # Show actions with their parameter hints
        if self.session and self.session.has_current_behavior:
            behavior = self.session.current_behavior
            for action in behavior.actions._actions:
                action_name = action.action_name
                action_desc = next((a.description for a in self.action_descriptions if a.name == action_name), "")
                
                instructions_hint = self.session._get_instructions_params_hint(action)
                submit_hint = self.session._get_submit_params_hint(action)
                
                # Combine hints
                hints = []
                if instructions_hint:
                    hints.append(instructions_hint)
                if submit_hint:
                    hints.append(submit_hint)
                
                params_line = " | ".join(hints) if hints else ""
                
                lines.append(f"      {action_name:12} - {action_desc}")
                if params_line:
                    lines.append(f"                     {params_line}")
        else:
            # Fallback if no current behavior - delegate to collection class
            desc_collection = ActionDescriptionCollection(self.action_descriptions)
            lines.extend(desc_collection.format_as_lines())
        
        lines.append("")
        lines.append("    operations:")
        
        # Show operations with parameter hints if we have a current action
        if self.session and self.session.has_current_action:
            action_obj = self.session.current_action
            instructions_hint = self.session._get_instructions_params_hint(action_obj)
    # ... (truncated)
```

---

## keep_functions_small_focused
**repl_main.py** - 1 violation(s)

[!] WARNING (line 70)
Function "main" is 102 lines - should be under 20 lines (extract complex logic to helper functions)

```python


def main():
    # Bot directory was set at module level to always be story_bot
    # (where behaviors are loaded from)
    bot_name = 'story_bot'
    
    workspace_directory = get_workspace_directory()
    
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
    
    repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
    
    # Check TTY before printing header
    tty_result = repl_session.detect_tty()
    is_pipe_mode = not tty_result.tty_detected
    
    # Print header
    print("=" * 60)
    print(f"{bot_name.upper()} CLI")
    
    # Add explicit instruction when in piped mode
    if is_pipe_mode:
        print("")
        print("=" * 60)
        print("AI AGENT INSTRUCTIONS - PIPED MODE")
        print("=" * 60)
        print("")
        print("*** THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND ***")
        print("This is NORMAL and EXPECTED behavior in piped mode.")
        print("")
        print("HOW TO RUN COMMANDS (PowerShell):")
        print("-" * 60)
        print("Commands must be PIPED via echo, NOT passed as arguments!")
        print("")
    # ... (truncated)
```

---

## keep_functions_small_focused
**repl_session.py** - 1 violation(s)

[!] WARNING (line 181)
Function "get_context_header_for_ai" is 25 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        )
    
    def get_context_header_for_ai(self) -> str:
        if not self.has_current_action:
            return ""
        
        lines = []
        
        # Get bot name from bot_directory
        if self.bot and hasattr(self.bot, 'bot_paths'):
            bot_name = self.bot.bot_paths.bot_directory.name
        else:
            bot_name = 'UNKNOWN'
        lines.append(f"{bot_name.upper()} CLI")
        
        # Detect piped mode and add explicit AI instruction
        tty_result = self.detect_tty()
        if not tty_result.tty_detected:
            lines.append("")
            lines.append("*** PIPED MODE DETECTED ***")
            lines.append("This command will EXIT upon processing.")
            lines.append("AI: Please follow ALL instructions below.")
            lines.append("")
        
        if self.bot:
            bot_path = self.bot.bot_paths.bot_directory if hasattr(self.bot, 'bot_paths') else 'Unknown'
            lines.append(f"Bot Path: {bot_path}")
        lines.append(f"Work Path: {self.workspace_directory}")
        
        # Show hierarchical breadcrumbs (includes Progress line after scope)
        lines.append(self.status.hierarchical_status)
        
        
        
        return "\n".join(lines)
    
```

---

## keep_functions_small_focused
**repl_status.py** - 1 violation(s)

[!] WARNING (line 48)
Function "hierarchical_status" is 87 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    
    @property
    def hierarchical_status(self) -> str:
        lines = []
        
        # Show scope if set
        scope_lines = self._get_scope_display()
        if scope_lines:
            lines.append("-" * 60)
            lines.extend(scope_lines)
            lines.append("-" * 60)
        else:
            lines.append("-" * 60)
        
        # Add Progress line after scope
        if self.state.has_current_action:
            lines.append(f"Progress: {self.state.progress_path}.{self.state.stage_name}")
        else:
            lines.append("Progress: No active workflow")
        
        if not self.bot or not self.bot.behaviors:
            lines.append("No behaviors available")
            lines.append("-" * 60)
            return "\n".join(lines)
        
        current_behavior_name = self.state.current_behavior_name
        current_action_name = self.state.current_action_name
        completed_behaviors = self.state.completed_behaviors or []
        completed_actions = self.state.completed_action_names or []
        stage = self.state.stage_name
        
        for behavior in self.bot.behaviors:
            b_name = behavior.name
            is_current_behavior = b_name == current_behavior_name
            is_completed_behavior = b_name in completed_behaviors
            
            # Get behavior description if available
            b_desc = getattr(behavior, 'description', '') or ''
            
            # Format behavior marker
            if is_completed_behavior:
                marker = "[x]"
            elif is_current_behavior:
                marker = "[*]"
            else:
                marker = "[ ]"
            
            # Show behavior line - only show description for current behavior
            if is_current_behavior and b_desc:
                lines.append(f"{marker} {b_name} - {b_desc}")
    # ... (truncated)
```

---

## keep_functions_small_focused
**status_display.py** - 1 violation(s)

[!] WARNING (line 41)
Function "render" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

```python
class HierarchyTreeDisplay:
    
    def render(self, cli_bot: CLIBot) -> str:
        lines = []
        
        current_behavior = cli_bot.behaviors.current
        behaviors = cli_bot.behaviors.all
        
        for behavior_name in behaviors:
            behavior = cli_bot.behaviors.get_behavior(behavior_name)
            if behavior is None:
                continue
            
            is_current = current_behavior and behavior.name == current_behavior.name
            status_icon = "[*]" if is_current else "[ ]"
            
            lines.append(f"{status_icon} {behavior.name}")
            
            if is_current and behavior.actions:
                current_action = behavior.actions.current
                actions = behavior.actions.all
                
                for action_name in actions:
                    action = behavior.actions.get_action(action_name)
                    if action is None:
                        continue
                    
                    is_current_action = current_action and action.name == current_action.name
                    action_icon = "    [*]" if is_current_action else "    [ ]"
                    lines.append(f"{action_icon} {action.name}")
        
        return "\n".join(lines) if lines else "No behaviors loaded"

```

---

## keep_functions_small_focused
**meta.py** - 1 violation(s)

[!] WARNING (line 80)
Function "execute" is 31 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return "current"
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        if not self.has_current_action:
            return self.error_no_current_action()
        
        # Re-execute current operation based on progress state
        # Progress format is: behavior.action.operation
        progress = self.session.get_progress_line()
        
        # Extract operation from progress (last part after final dot)
        if '.' in progress and 'Progress: ' in progress:
            parts = progress.replace('Progress: ', '').split('.')
            if len(parts) >= 3:
                operation = parts[2]
                
                # Re-execute the current operation
                if operation == 'instructions':
                    # Import here to avoid circular dependency
                    from agile_bot.bots.base_bot.src.repl_cli.repl_commands.workflow import InstructionsCommand
                    cmd = InstructionsCommand(self.session)
                    return cmd.execute(args)
                elif operation == 'submit':
                    # Import here to avoid circular dependency
                    from agile_bot.bots.base_bot.src.repl_cli.repl_commands.workflow import SubmitCommand
                    cmd = SubmitCommand(self.session)
                    return cmd.execute(args)
                elif operation == 'confirm':
                    # Confirm doesn't make sense to re-execute
                    return REPLCommandResponse(
                        output="Cannot re-execute 'confirm'. Use 'next' or 'back' to navigate.",
                        response="Cannot re-execute confirm",
                        status="error"
                    )
        
        # Default: show instructions
        return self.display_instructions()

```

---

## keep_functions_small_focused
**repl_command.py** - 1 violation(s)

[!] WARNING (line 164)
Function "display_instructions" is 32 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return self._wrap_with_context_header(content, f"Moved to {location}")
    
    def display_instructions(self, action=None, context=None, operation="instructions") -> REPLCommandResponse:
        # Use current action if none specified
        if action is None:
            action = self.current_action
        
        if not action:
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
        
        try:
            # Call the action's instructions() method - it formats everything
            formatted_output = action.instructions(args="" if context is None else str(context))
            
            # Format execution line
            if operation == "instructions":
                exec_line = f"Executing: {self.current_behavior_name}.{action.name}.instructions"
            else:
                exec_line = f"Executing: {self.current_behavior_name}.{action.name}"
            
            # Build content (just instructions, no submit message yet)
            content = "\n".join([
                exec_line,
                formatted_output
            ])
            
            # Wrap with context header
            response = self._wrap_with_context_header(content, content)
            
            response.action = action.name
            response.context_passed_to_action = context
            return response
        except Exception as e:
            error_msg = f"ERROR executing {action.name}.instructions(): {str(e)}"
            return REPLCommandResponse(
                output=error_msg,
                response=error_msg,
                status="error",
                action=action.name
            )

```

---

## keep_functions_small_focused
**state.py** - 1 violation(s)

[!] WARNING (line 159)
Function "execute" is 43 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return True
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        from agile_bot.bots.base_bot.src.actions.action_context import Scope, ScopeType
        
        args = args.strip()
        if not args:
            # Show current scope if no args (same display as banner)
            scope_lines = self.session._get_scope_display_lines()
            if scope_lines:
                output = "\n".join(scope_lines)
                return REPLCommandResponse(
                    output=output,
                    response=output,
                    status="success"
                )
            else:
                return REPLCommandResponse(
                    output="No scope set",
                    response="No scope set",
                    status="success"
                )
        
        # Handle "all" - clears the scope filter
        if args.lower() == 'all':
            self.session.clear_scope()
            return REPLCommandResponse(
                output="Scope filter cleared",
                response="Scope filter cleared",
                status="success"
            )
        
        if args.startswith(('file:', 'files:')):
            prefix = args.split(':', 1)[0].strip().lower()
            value_part = args.split(':', 1)[1].strip()
            scope_values_raw = [v.strip() for v in value_part.split(',') if v.strip()]
            scope_type = ScopeType.FILES
            scope_value = scope_values_raw
        else:
            scope_type = ScopeType.STORY
            scope_values_raw = [v.strip() for v in args.split(',') if v.strip()]
            scope_value = scope_values_raw
        
        scope = Scope(type=scope_type, value=scope_value)
        self.session.store_scope_parameters(scope)
        
        # Get the scope display lines (same as banner)
        scope_lines = self.session._get_scope_display_lines()
        output = "\n".join(scope_lines)
        
    # ... (truncated)
```

---

## keep_functions_small_focused
**workflow.py** - 2 violation(s)

[!] WARNING (line 150)
Function "execute_submit" is 110 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return {}
    
    def execute_submit(self, args: str = "") -> REPLCommandResponse:
        action = self.current_action
        if not action:
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
        
        try:
            # Parse arguments if provided and action uses ClarifyActionContext, StrategyActionContext, or ScopeActionContext
            context = action.domain_action.context_class()
            if args and isinstance(context, ClarifyActionContext):
                parsed = self._parse_clarification_args(args)
                # Set the parsed values if we found any
                if parsed['answers']:
                    context.answers = parsed['answers']
                if parsed['evidence_provided']:
                    context.evidence_provided = parsed['evidence_provided']
                if parsed['context']:
                    context.context = parsed['context']
            elif args and isinstance(context, StrategyActionContext):
                parsed = self._parse_strategy_args(args)
                # Set decisions as direct attributes on context
                if parsed['choices']:
                    for key, value in parsed['choices'].items():
                        setattr(context, key, value)
                if parsed['assumptions']:
                    context.assumptions = parsed['assumptions']
            elif args and isinstance(context, ScopeActionContext):
                parsed = self._parse_scope_args(args, action.name)
                # Set the parsed scope if we found one
                if 'scope' in parsed:
                    context.scope = parsed['scope']
            
            # Call the real action.submit() method
            result = action.domain_action.submit(context)
            
            # Format output
            status = result.get('status', 'unknown')
            message = result.get('message', 'Work submitted')
            saved_path = result.get('saved_path')
            questions_count = result.get('questions_answered', 0)
            evidence_count = result.get('evidence_count', 0)
            
            output_lines = [
                f"Executing: {self.current_behavior_name}.{self.current_action_name}.submit",
                "",
    # ... (truncated)
```

[!] WARNING (line 283)
Function "execute_confirm" is 44 lines - should be under 20 lines (extract complex logic to helper functions)

```python
            )
    
    def execute_confirm(self) -> REPLCommandResponse:
        action = self.current_action
        behavior = self.current_behavior
        if not behavior or not action:
            return self.error_no_current_behavior()
        
        current_behavior_name = behavior.name
        current_action_name = action.name
        
        try:
            # Call the real action.confirm() method
            context = action.domain_action.context_class()
            result = action.domain_action.confirm(context)
            
            # Check if at last action BEFORE closing
            is_last_action = behavior.actions.next is None
            
            # Mark current action as complete and advance
            behavior.actions.domain_actions.close_current()
            
            # If not at last action, advance to next action and show navigation
            if not is_last_action:
                return self.display_navigation()
            
            # At last action - behavior is complete
            # Mark behavior as complete in state file
            self._mark_behavior_complete(current_behavior_name)
            
            # Check for next behavior BEFORE close_current since it advances the index
            next_behavior = self.bot.behaviors.next
            
            if next_behavior:
                # Advance to next behavior
                self.bot.behaviors.close_current()
                # Navigate to next behavior's first action
                if next_behavior.actions.names:
                    self.navigate_to_behavior_action(next_behavior.name, next_behavior.actions.names[0])
                    return self.display_navigation()
            
            # No more behaviors - all complete
            return REPLCommandResponse(
                output=f"COMPLETE: {current_behavior_name} behavior finished\n\nALL BEHAVIORS COMPLETE!",
                response="COMPLETE: All behaviors finished",
                status="success"
            )
        except Exception as e:
            error_msg = f"ERROR executing {current_action_name}.confirm(): {str(e)}"
            return REPLCommandResponse(
    # ... (truncated)
```

---

## keep_functions_small_focused
**cli_action_factory.py** - 1 violation(s)

[i] INFO (line 13)
Function "create_cli_action" has deep nesting (depth=5) - should be under 4 levels. Extract nested logic to helper functions.

```python
    
    @staticmethod
    def create_cli_action(action: Action, session: REPLSession) -> CLIAction:
        action_name = action.action_name
        
        if action_name == 'build':
            from agile_bot.bots.base_bot.src.repl_cli.cli_bot.cli_actions.build_cli_action import BuildCLIAction
            return BuildCLIAction(action, session)
        elif action_name == 'validate':
            from agile_bot.bots.base_bot.src.repl_cli.cli_bot.cli_actions.validate_cli_action import ValidateCLIAction
            return ValidateCLIAction(action, session)
        elif action_name == 'render':
            from agile_bot.bots.base_bot.src.repl_cli.cli_bot.cli_actions.render_cli_action import RenderCLIAction
            return RenderCLIAction(action, session)
        elif action_name == 'clarify':
            from agile_bot.bots.base_bot.src.repl_cli.cli_bot.cli_actions.clarify_cli_action import ClarifyCLIAction
            return ClarifyCLIAction(action, session)
        elif action_name == 'strategy':
            from agile_bot.bots.base_bot.src.repl_cli.cli_bot.cli_actions.strategy_cli_action import StrategyCLIAction
            return StrategyCLIAction(action, session)
        else:
            from agile_bot.bots.base_bot.src.repl_cli.cli_bot.cli_actions.cli_action import CLIAction
            return CLIAction(action, session)

```

---

## maintain_vertical_density
**repl_help.py** - 1 violation(s)

[i] INFO (line 215)
Function "main_help" is 83 lines - consider improving vertical density by declaring variables near usage

```python
    
    @property
    def main_help(self) -> str:
        behaviors_list = " | ".join(self.behavior_names)
        
        lines = [
            "Core Commands:",
            "  echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation",
            "  echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action",
            "",
    # ... (truncated)
```

---

## maintain_vertical_density
**repl_main.py** - 1 violation(s)

[i] INFO (line 70)
Function "main" is 126 lines - consider improving vertical density by declaring variables near usage

```python


def main():
    # Bot directory was set at module level to always be story_bot
    # (where behaviors are loaded from)
    bot_name = 'story_bot'
    
    workspace_directory = get_workspace_directory()
    
    bot_config_path = bot_directory / 'bot_config.json'
    # ... (truncated)
```

---

## maintain_vertical_density
**repl_session.py** - 1 violation(s)

[i] INFO (line 306)
Function "_execute_action_with_args" is 56 lines - consider improving vertical density by declaring variables near usage

```python
            return args_str.split()
    
    def _execute_action_with_args(self, action_name: str, cli_args: list, operation: str = None) -> REPLCommandResponse:
        if not self.has_current_behavior:
            return REPLCommandResponse(
                output="ERROR: No current behavior set. Please select a behavior first.",
                response="ERROR: No current behavior set",
                status="error"
            )
        
    # ... (truncated)
```

---

## maintain_vertical_density
**repl_status.py** - 1 violation(s)

[i] INFO (line 48)
Function "hierarchical_status" is 110 lines - consider improving vertical density by declaring variables near usage

```python
    
    @property
    def hierarchical_status(self) -> str:
        lines = []
        
        # Show scope if set
        scope_lines = self._get_scope_display()
        if scope_lines:
            lines.append("-" * 60)
            lines.extend(scope_lines)
    # ... (truncated)
```

---

## maintain_vertical_density
**state.py** - 1 violation(s)

[i] INFO (line 159)
Function "execute" is 54 lines - consider improving vertical density by declaring variables near usage

```python
        return True
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        from agile_bot.bots.base_bot.src.actions.action_context import Scope, ScopeType
        
        args = args.strip()
        if not args:
            # Show current scope if no args (same display as banner)
            scope_lines = self.session._get_scope_display_lines()
            if scope_lines:
    # ... (truncated)
```

---

## maintain_vertical_density
**workflow.py** - 3 violation(s)

[i] INFO (line 31)
Function "_parse_clarification_args" is 59 lines - consider improving vertical density by declaring variables near usage

```python
        return self.action_phase in ('not_started', 'instructions_given')
    
    def _parse_clarification_args(self, args: str) -> Dict[str, Any]:
        answers = {}
        evidence_provided = {}
        context = None
        
        if not args or not args.strip():
            return {'answers': answers, 'evidence_provided': evidence_provided, 'context': context}
        
    # ... (truncated)
```

[i] INFO (line 150)
Function "execute_submit" is 132 lines - consider improving vertical density by declaring variables near usage

```python
        return {}
    
    def execute_submit(self, args: str = "") -> REPLCommandResponse:
        action = self.current_action
        if not action:
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
    # ... (truncated)
```

[i] INFO (line 283)
Function "execute_confirm" is 53 lines - consider improving vertical density by declaring variables near usage

```python
            )
    
    def execute_confirm(self) -> REPLCommandResponse:
        action = self.current_action
        behavior = self.current_behavior
        if not behavior or not action:
            return self.error_no_current_behavior()
        
        current_behavior_name = behavior.name
        current_action_name = action.name
    # ... (truncated)
```

---

## never_swallow_exceptions
**repl_main.py** - 1 violation(s)

[X] ERROR (line 58)
Except block only contains pass at line 58 - exceptions must be logged or rethrown, never swallowed

```python
            elif 'WORKING_AREA' in bot_config:
                os.environ['WORKING_AREA'] = bot_config['WORKING_AREA']
        except:
            pass
    
```

---

## never_swallow_exceptions
**repl_status.py** - 2 violation(s)

[X] ERROR (line 168)
Except block only contains pass at line 168 - exceptions must be logged or rethrown, never swallowed

```python
                    if 'context' in fields:
                        return ' --context="..."'
            except:
                pass
        return ''
```

[X] ERROR (line 183)
Except block only contains pass at line 183 - exceptions must be logged or rethrown, never swallowed

```python
                    if 'assumptions_made' in fields or 'assumptions' in fields:
                        params.append('--assumptions="..."')
            except:
                pass
        if params:
```

---

## never_swallow_exceptions
**workflow.py** - 1 violation(s)

[X] ERROR (line 348)
Except block only contains pass at line 348 - exceptions must be logged or rethrown, never swallowed

```python
            state_data['completed_behaviors'] = completed
            state_file.write_text(json.dumps(state_data, indent=2))
        except (json.JSONDecodeError, IOError):
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

[X] ERROR (line 65)
Import statement found after non-import code. Move all imports to the top of the file.

```python
        os.environ['WORKING_AREA'] = str(workspace_root)

from agile_bot.bots.base_bot.src.bot.bot import Bot
from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
```

[X] ERROR (line 66)
Import statement found after non-import code. Move all imports to the top of the file.

```python

from agile_bot.bots.base_bot.src.bot.bot import Bot
from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
from agile_bot.bots.base_bot.src.bot.workspace import get_bot_directory, get_workspace_directory
```

[X] ERROR (line 67)
Import statement found after non-import code. Move all imports to the top of the file.

```python
from agile_bot.bots.base_bot.src.bot.bot import Bot
from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
from agile_bot.bots.base_bot.src.bot.workspace import get_bot_directory, get_workspace_directory

```

---

## provide_meaningful_context
**repl_main.py** - 8 violation(s)

[!] WARNING (line 101)
Line 101 contains magic number - replace with named constant

```python
    # Print header
    print("=" * 60)
    print(f"{bot_name.upper()} CLI")
```

[!] WARNING (line 107)
Line 107 contains magic number - replace with named constant

```python
        print("")
        print("=" * 60)
        print("AI AGENT INSTRUCTIONS - PIPED MODE")
```

[!] WARNING (line 109)
Line 109 contains magic number - replace with named constant

```python
        print("AI AGENT INSTRUCTIONS - PIPED MODE")
        print("=" * 60)
        print("")
```

[!] WARNING (line 115)
Line 115 contains magic number - replace with named constant

```python
        print("HOW TO RUN COMMANDS (PowerShell):")
        print("-" * 60)
        print("Commands must be PIPED via echo, NOT passed as arguments!")
```

[!] WARNING (line 126)
Line 126 contains magic number - replace with named constant

```python
        print("WHAT DOES NOT WORK:")
        print("-" * 60)
        print("  [X] python repl_main.py instructions        # No args!")
```

[!] WARNING (line 131)
Line 131 contains magic number - replace with named constant

```python
        print("WHAT WORKS:")
        print("-" * 60)
        print("  [OK] echo 'instructions' | python repl_main.py  # Piped input")
```

[!] WARNING (line 137)
Line 137 contains magic number - replace with named constant

```python
        print("PIPED MODE WORKFLOW:")
        print("-" * 60)
        print("1. Pipe command -> REPL runs -> shows output -> EXITS")
```

[!] WARNING (line 144)
Line 144 contains magic number - replace with named constant

```python
        print("CRITICAL RULES:")
        print("-" * 60)
        print("  - ALWAYS pipe commands: echo <cmd> | python repl_main.py")
```

---

## provide_meaningful_context
**repl_status.py** - 5 violation(s)

[!] WARNING (line 54)
Line 54 contains magic number - replace with named constant

```python
        if scope_lines:
            lines.append("-" * 60)
            lines.extend(scope_lines)
```

[!] WARNING (line 56)
Line 56 contains magic number - replace with named constant

```python
            lines.extend(scope_lines)
            lines.append("-" * 60)
        else:
```

[!] WARNING (line 58)
Line 58 contains magic number - replace with named constant

```python
        else:
            lines.append("-" * 60)
        
```

[!] WARNING (line 68)
Line 68 contains magic number - replace with named constant

```python
            lines.append("No behaviors available")
            lines.append("-" * 60)
            return "\n".join(lines)
```

[!] WARNING (line 150)
Line 150 contains magic number - replace with named constant

```python
        lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
        lines.append("-" * 60)
        
```

---

## provide_meaningful_context
**workflow.py** - 4 violation(s)

[!] WARNING (line 209)
Line 209 contains magic number - replace with named constant

```python
                    for q_key, answer in list(answers.items())[:5]:  # Show first 5
                        output_lines.append(f"  - {q_key}: {answer[:60]}{'...' if len(str(answer)) > 60 else ''}")
                    if len(answers) > 5:
```

[!] WARNING (line 219)
Line 219 contains magic number - replace with named constant

```python
                    for e_key, e_value in list(evidence.items())[:5]:  # Show first 5
                        output_lines.append(f"  - {e_key}: {str(e_value)[:60]}{'...' if len(str(e_value)) > 60 else ''}")
                    if len(evidence) > 5:
```

[!] WARNING (line 230)
Line 230 contains magic number - replace with named constant

```python
                    for idx, item in enumerate(saved_context[:5], 1):  # Show first 5
                        item_preview = item[:60] + ('...' if len(item) > 60 else '')
                        output_lines.append(f"  {idx}. {item_preview}")
```

[!] WARNING (line 256)
Line 256 contains magic number - replace with named constant

```python
                for idx, assumption in enumerate(assumptions[:5], 1):  # Show first 5
                    assumption_preview = assumption[:60] + ('...' if len(assumption) > 60 else '')
                    output_lines.append(f"  {idx}. {assumption_preview}")
```

---

## refactor_completely_not_partially
**repl_help.py** - 1 violation(s)

[!] WARNING (line 252)
Fallback/legacy support code found (comment at line 252, code at line 253) - complete refactoring by removing old pattern support

---

## refactor_completely_not_partially
**workflow.py** - 1 violation(s)

[!] WARNING (line 235)
Fallback/legacy support code found (comment at line 235, code at line 236) - complete refactoring by removing old pattern support

---

## simplify_control_flow
**repl_main.py** - 1 violation(s)

[!] WARNING (line 70)
Function "main" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python


def main():
    # Bot directory was set at module level to always be story_bot
    # (where behaviors are loaded from)
    bot_name = 'story_bot'
    
    workspace_directory = get_workspace_directory()
    
    bot_config_path = bot_directory / 'bot_config.json'
    
    if not bot_config_path.exists():
        print(f"ERROR: Bot config not found at {bot_config_path}")
        print("Please ensure you're running from the correct directory.")
        sys.exit(1)
    # ... (truncated)
```

---

## simplify_control_flow
**repl_status.py** - 3 violation(s)

[!] WARNING (line 48)
Function "hierarchical_status" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
    
    @property
    def hierarchical_status(self) -> str:
        lines = []
        
        # Show scope if set
        scope_lines = self._get_scope_display()
        if scope_lines:
            lines.append("-" * 60)
            lines.extend(scope_lines)
            lines.append("-" * 60)
        else:
            lines.append("-" * 60)
        
        # Add Progress line after scope
    # ... (truncated)
```

[!] WARNING (line 159)
Function "_get_instructions_params" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return "\n".join(lines)
    
    def _get_instructions_params(self, action) -> str:
        # Check if action has context_class with fields
        if hasattr(action, 'context_class') and action.context_class:
            try:
                import dataclasses
                if dataclasses.is_dataclass(action.context_class):
                    fields = [f.name for f in dataclasses.fields(action.context_class)]
                    if 'context' in fields:
                        return ' --context="..."'
            except:
                pass
        return ''
    
```

[!] WARNING (line 172)
Function "_get_submit_params" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return ''
    
    def _get_submit_params(self, action) -> str:
        params = []
        if hasattr(action, 'context_class') and action.context_class:
            try:
                import dataclasses
                if dataclasses.is_dataclass(action.context_class):
                    fields = [f.name for f in dataclasses.fields(action.context_class)]
                    if 'decisions' in fields:
                        params.append('--decisions="1:option,..."')
                    if 'assumptions_made' in fields or 'assumptions' in fields:
                        params.append('--assumptions="..."')
            except:
                pass
    # ... (truncated)
```

---

## simplify_control_flow
**status_display.py** - 1 violation(s)

[!] WARNING (line 41)
Function "render" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
class HierarchyTreeDisplay:
    
    def render(self, cli_bot: CLIBot) -> str:
        lines = []
        
        current_behavior = cli_bot.behaviors.current
        behaviors = cli_bot.behaviors.all
        
        for behavior_name in behaviors:
            behavior = cli_bot.behaviors.get_behavior(behavior_name)
            if behavior is None:
                continue
            
            is_current = current_behavior and behavior.name == current_behavior.name
            status_icon = "[*]" if is_current else "[ ]"
    # ... (truncated)
```

---

## simplify_control_flow
**meta.py** - 1 violation(s)

[!] WARNING (line 80)
Function "execute" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return "current"
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        if not self.has_current_action:
            return self.error_no_current_action()
        
        # Re-execute current operation based on progress state
        # Progress format is: behavior.action.operation
        progress = self.session.get_progress_line()
        
        # Extract operation from progress (last part after final dot)
        if '.' in progress and 'Progress: ' in progress:
            parts = progress.replace('Progress: ', '').split('.')
            if len(parts) >= 3:
                operation = parts[2]
    # ... (truncated)
```

---

## simplify_control_flow
**repl_command.py** - 1 violation(s)

[!] WARNING (line 97)
Function "_get_submit_message" has nesting depth of 9 - use guard clauses and extract nested blocks to reduce nesting

```python
        )
    
    def _get_submit_message(self, action) -> str:
        context_class = action.context_class
        
        # Get field names from the context class (excluding common base fields)
        if hasattr(context_class, '__dataclass_fields__'):
            fields = context_class.__dataclass_fields__
            # Filter out common base fields (scope is from ScopeActionContext, message is from RulesActionContext)
            common_fields = {'scope', 'message', 'background', 'skip_cross_file', 'all_files', 'force_full'}
            param_fields = [name for name in fields.keys() if name not in common_fields]
            
            if param_fields:
                # Build action-specific parameter examples
                param_examples = []
    # ... (truncated)
```

---

## simplify_control_flow
**workflow.py** - 2 violation(s)

[!] WARNING (line 31)
Function "_parse_clarification_args" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return self.action_phase in ('not_started', 'instructions_given')
    
    def _parse_clarification_args(self, args: str) -> Dict[str, Any]:
        answers = {}
        evidence_provided = {}
        context = None
        
        if not args or not args.strip():
            return {'answers': answers, 'evidence_provided': evidence_provided, 'context': context}
        
        # First try compact format: answers="q1=answer1, q2=answer2" or key_questions="q1=answer1, q2=answer2"
        compact_kq_pattern = r'(?:clarify\.)?(answers|key_questions)="([^"]+)"'
        compact_ev_pattern = r'(?:clarify\.)?evidence="([^"]+)"'
        
        kq_match = re.search(compact_kq_pattern, args)
    # ... (truncated)
```

[!] WARNING (line 150)
Function "execute_submit" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return {}
    
    def execute_submit(self, args: str = "") -> REPLCommandResponse:
        action = self.current_action
        if not action:
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
        
        try:
            # Parse arguments if provided and action uses ClarifyActionContext, StrategyActionContext, or ScopeActionContext
            context = action.domain_action.context_class()
            if args and isinstance(context, ClarifyActionContext):
    # ... (truncated)
```

---

## simplify_control_flow
**cli_action_factory.py** - 1 violation(s)

[!] WARNING (line 13)
Function "create_cli_action" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
    
    @staticmethod
    def create_cli_action(action: Action, session: REPLSession) -> CLIAction:
        action_name = action.action_name
        
        if action_name == 'build':
            from agile_bot.bots.base_bot.src.repl_cli.cli_bot.cli_actions.build_cli_action import BuildCLIAction
            return BuildCLIAction(action, session)
        elif action_name == 'validate':
            from agile_bot.bots.base_bot.src.repl_cli.cli_bot.cli_actions.validate_cli_action import ValidateCLIAction
            return ValidateCLIAction(action, session)
        elif action_name == 'render':
            from agile_bot.bots.base_bot.src.repl_cli.cli_bot.cli_actions.render_cli_action import RenderCLIAction
            return RenderCLIAction(action, session)
        elif action_name == 'clarify':
    # ... (truncated)
```

---

## stop_writing_useless_comments
**cli_scope.py** - 4 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class CLIScope:
    """CLI wrapper for Scope that adds display formatting."""
    
```

[X] ERROR (line 17)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @classmethod
    def from_state_file(cls, workspace_directory: Path) -> Optional['CLIScope']:
        """Load scope from bot state file and wrap it."""
        try:
```

[X] ERROR (line 34)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_formatted_display(self) -> str:
        """Render scope with CLI-specific formatting (warnings, separators, and AI instructions)."""
        lines = []
```

[X] ERROR (line 61)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def domain_scope(self) -> Scope:
        """Access the underlying domain Scope object."""
        return self._scope
```

---

## stop_writing_useless_comments
**cli_behaviors.py** - 1 violation(s)

[X] ERROR (line 65)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __iter__(self):
        """Make CLIBehaviors iterable - yields CLIBehavior objects for each behavior"""
        for behavior in self._behaviors._behaviors:
```

---

## stop_writing_useless_comments
**cli_actions.py** - 2 violation(s)

[X] ERROR (line 60)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def find_by_name(self, name: str) -> Optional[CLIAction]:
        """Find action by name (alias for get_action to match domain API)"""
        return self.get_action(name)
```

[X] ERROR (line 82)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __iter__(self):
        """Make CLIActions iterable - yields CLIAction objects for each action"""
        for action_name in self._actions.names:
```

---

Completed: 2025-12-27 01:00:59
Total violations: 77
Scanners executed: 30
