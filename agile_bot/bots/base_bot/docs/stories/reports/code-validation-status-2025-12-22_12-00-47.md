# Validation Status - code
Started: 2025-12-22 12:00:47
Files: 11

## chain_dependencies_properly
**command_renderer.py** - 1 violation(s)

[!] WARNING (line 16)
Method "visit_header" in class "CursorCommandVisitor" takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.

```python
        self.output_lines = output_lines
    
    def visit_header(self, bot_name: str) -> None:
        """Visit header - not used for command files."""
        pass
    # ... (truncated)
```

---

## chain_dependencies_properly
**cli_code_visitor.py** - 1 violation(s)

[!] WARNING (line 16)
Method "visit_header" in class "CliCodeVisitor" takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.

```python
        self.bot_name = bot_name
    
    def visit_header(self, bot_name: str) -> None:
        """Visit header - not used for code generation."""
        pass
    # ... (truncated)
```

---

## chain_dependencies_properly
**cursor_help_renderer.py** - 1 violation(s)

[!] WARNING (line 13)
Method "visit_header" in class "CursorHelpVisitor" takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.

```python
        self.formatter = formatter
    
    def visit_header(self, bot_name: str) -> None:
        name = bot_name if bot_name is not None else self.bot_name
        print(f"## Available Cursor Commands for {name}:")
    # ... (truncated)
```

---

## eliminate_duplication
**help_renderer.py** - 1 violation(s)

[X] ERROR (line 31)
Duplicate code detected: functions _format_behavior_command, _format_behavior_title, _format_action_command have identical bodies - extract to shared function

---


## Cross-File Duplication Analysis
Scanning 11 files...
Extracted 217 code blocks
Starting 23436 pairwise comparisons...
Comparing: 5% (1,172/23,436) - 0 violations - ETA: 18s  
Comparing: 10% (2,344/23,436) - 0 violations - ETA: 8s  
Comparing: 15% (3,516/23,436) - 0 violations - ETA: 7s  
Comparing: 20% (4,688/23,436) - 4 violations - ETA: 7s  
Comparing: 25% (5,859/23,436) - 6 violations - ETA: 6s  
Comparing: 30% (7,031/23,436) - 6 violations - ETA: 5s  
Comparing: 35% (8,203/23,436) - 9 violations - ETA: 4s  
Found 10 violations so far...
Comparing: 40% (9,375/23,436) - 15 violations - ETA: 4s  
Found 20 violations so far...
Comparing: 45% (10,547/23,436) - 22 violations - ETA: 4s  
Found 30 violations so far...
Comparing: 50% (11,718/23,436) - 31 violations - ETA: 3s  
Comparing: 55% (12,890/23,436) - 34 violations - ETA: 3s  
Comparing: 60% (14,062/23,436) - 34 violations - ETA: 2s  
Comparing: 65% (15,234/23,436) - 34 violations - ETA: 2s  
Comparing: 70% (16,406/23,436) - 34 violations - ETA: 2s  
Comparing: 75% (17,577/23,436) - 34 violations - ETA: 1s  
Comparing: 80% (18,749/23,436) - 34 violations - ETA: 1s  
Comparing: 85% (19,921/23,436) - 34 violations - ETA: 1s  
Comparing: 90% (21,093/23,436) - 34 violations - ETA: 0s  
Comparing: 95% (22,265/23,436) - 34 violations - ETA: 0s  
Comparing: 100% (23,436/23,436) - 34 violations - ETA: 0s  
Complete: 23436 comparisons, 34 violations

## keep_functions_small_focused
**command_renderer.py** - 1 violation(s)

[!] WARNING (line 24)
Function "visit_action" is 33 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        pass
    
    def visit_action(self, context: ActionHelpContext) -> None:
        """Visit an action and add its help to output."""
        # Extract short description (first line or first sentence)
        short_desc = context.action_description.split('\n')[0].split('.')[0] if context.action_description else context.action_name
        
        self.output_lines.append(f"### {context.action_name} - {short_desc}")
        self.output_lines.append(f"{self.python_command} --behavior {self.behavior_name} --action {context.action_name}")
        
        if context.parameters:
            for param in context.parameters:
                self.output_lines.append(f"  # Optional: {param}")
                if param in context.parameter_descriptions:
                    desc = context.parameter_descriptions[param]
                    # Format multi-line descriptions
                    for desc_line in desc.split('\n'):
                        self.output_lines.append(f"  #   {desc_line}")
            
            # Add example with first 2 parameters
            example_params = []
            for param in context.parameters[:2]:
                param_name = param.split()[0]  # Extract --param-name from "--param-name <type>"
                if '<dict>' in param:
                    example_params.append(f"{param_name} '{{\"key\": \"value\"}}'")
                elif '<list>' in param:
                    example_params.append(f'{param_name} "value1" "value2"')
                elif '<flag>' in param:
                    example_params.append(param_name)
                else:
                    example_params.append(f'{param_name} "value"')
            
            if example_params:
                self.output_lines.append("  #")
                self.output_lines.append("  # Full example:")
                example_cmd = f"{self.python_command} --behavior {self.behavior_name} --action {context.action_name} {' '.join(example_params)}"
                self.output_lines.append(f"  # {example_cmd}")
        else:
            self.output_lines.append("  # (No optional parameters)")
        
        self.output_lines.append("")
    
```

---

## maintain_vertical_density
**cli_code_visitor.py** - 1 violation(s)

[i] INFO (line 38)
Function "generate_python_cli_script" is 83 lines - consider improving vertical density by declaring variables near usage

```python
        self.generate_powershell_script()
    
    def generate_python_cli_script(self) -> Path:
        """Generate Python CLI script."""
        bot_dir = self.workspace_root / self.bot_location
        src_dir = bot_dir / 'src'
        src_dir.mkdir(parents=True, exist_ok=True)
        cli_file = src_dir / f'{self.bot_name}_cli.py'
        cli_code = f'''#!/usr/bin/env python3
"""
    # ... (truncated)
```

---

## maintain_vertical_density
**cursor_command_generator.py** - 1 violation(s)

[i] INFO (line 162)
Function "_build_rules_command" is 65 lines - consider improving vertical density by declaring variables near usage

```python
    

    def _build_rules_command(self, python_command: str, behavior_name: str) -> str:
        if behavior_name == 'code':
            examples = [
                f"# Write new production code following rules",
                f"{python_command} --behavior {behavior_name} --action rules --message \"Help me write a new ValidationContext class that encapsulates validation parameters\"",
                "",
                f"# Refactor existing code to follow rules",
                f"{python_command} --behavior {behavior_name} --action rules --message \"Refactor the _execute_scanner method to reduce parameters from 10 to 3\"",
    # ... (truncated)
```

---

## simplify_control_flow
**command_renderer.py** - 1 violation(s)

[!] WARNING (line 24)
Function "visit_action" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        pass
    
    def visit_action(self, context: ActionHelpContext) -> None:
        """Visit an action and add its help to output."""
        # Extract short description (first line or first sentence)
        short_desc = context.action_description.split('\n')[0].split('.')[0] if context.action_description else context.action_name
        
        self.output_lines.append(f"### {context.action_name} - {short_desc}")
        self.output_lines.append(f"{self.python_command} --behavior {self.behavior_name} --action {context.action_name}")
        
        if context.parameters:
            for param in context.parameters:
                self.output_lines.append(f"  # Optional: {param}")
                if param in context.parameter_descriptions:
                    desc = context.parameter_descriptions[param]
    # ... (truncated)
```

---

## simplify_control_flow
**cli_help_renderer.py** - 1 violation(s)

[!] WARNING (line 32)
Function "visit_action" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        print('```\n')
    
    def visit_action(self, context: ActionHelpContext) -> None:
        print(f'### {context.action_name}\n')
        print(f'{context.action_description}\n')
        print('```')
        print(f'python {self.cli_script_path} --behavior <behavior> --action {context.action_name} [parameters]')
        if context.parameters:
            print()
            for param in context.parameters:
                param_desc = context.parameter_descriptions.get(param, "Optional parameter")
                if '\n' in param_desc:
                    lines = param_desc.split('\n')
                    print(f'{param}:   {lines[0]}')
                    for line in lines[1:]:
    # ... (truncated)
```

---

## simplify_control_flow
**cursor_help_renderer.py** - 1 violation(s)

[!] WARNING (line 36)
Function "visit_action" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        print('```\n')
    
    def visit_action(self, context: ActionHelpContext) -> None:
        print(f'### {context.action_name}\n')
        print(f'{context.action_description}\n')
        print('```')
        print(f'/{context.bot_name}-<behavior> {context.action_name} [parameters]')
        if context.parameters:
            print()
            for param in context.parameters:
                param_desc = context.parameter_descriptions.get(param, "Optional parameter")
                if '\n' in param_desc:
                    lines = param_desc.split('\n')
                    print(f'{param}:   {lines[0]}')
                    for line in lines[1:]:
    # ... (truncated)
```

---

## stop_writing_useless_comments
**cli_visitor.py** - 6 violation(s)

[X] ERROR (line 7)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class CliVisitor(ABC):
    """Base visitor for CLI artifact generation."""
    
```

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @abstractmethod
    def visit_header(self, bot_name: str) -> None:
        """Visit the header section."""
        pass
```

[X] ERROR (line 16)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @abstractmethod
    def visit_behavior(self, context: BehaviorHelpContext) -> None:
        """Visit a behavior."""
        pass
```

[X] ERROR (line 21)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @abstractmethod
    def visit_action(self, context: ActionHelpContext) -> None:
        """Visit an action."""
        pass
```

[X] ERROR (line 26)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @abstractmethod
    def visit_action_help_section_header(self) -> None:
        """Visit the action help section header."""
        pass
```

[X] ERROR (line 30)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def visit_footer(self) -> None:
        """Visit the footer section (optional)."""
        pass
```

---

## stop_writing_useless_comments
**action_data_collector.py** - 10 violation(s)

[X] ERROR (line 10)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class ActionDataCollector:
    """Collects action and behavior data for rendering."""
    
```

[X] ERROR (line 20)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_behavior_order(self, behavior) -> int:
        """Get order for behavior from config."""
        behavior_json_path = self.bot_directory / 'behaviors' / behavior.name / 'behavior.json'
```

[X] ERROR (line 29)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def sort_behaviors_for_display(self, behaviors):
        """Sort behaviors by order."""
        behaviors_list = list(behaviors)
```

[X] ERROR (line 39)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_behavior_actions(self, behavior) -> List[str]:
        """Get action names for a behavior."""
        action_names_str = self.description_extractor.get_action_names_from_behavior(behavior.name)
```

[X] ERROR (line 44)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_action_parameters(self, action_name: str) -> List[str]:
        """Get parameter list for an action from its context class."""
        action_class = ActionFactory.get_action_class(action_name)
```

[X] ERROR (line 62)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_parameter_descriptions(self, action_name: str, parameters: List[str]) -> Dict[str, str]:
        """Get descriptions for action parameters."""
        descriptions = {}
```

[X] ERROR (line 70)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _get_single_parameter_description(self, action_name: str, param: str) -> str:
        """Get description for a single parameter."""
        if 'key_questions_answered' in param:
```

[X] ERROR (line 84)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _get_scope_description(self, action_name: str) -> str:
        """Get scope description for an action."""
        if action_name == 'validate':
```

[X] ERROR (line 90)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_action_description(self, action_name: str) -> str:
        """Get description for an action."""
        description = self.description_extractor.get_action_description(action_name)
```

[X] ERROR (line 97)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_behavior_description(self, behavior_name: str) -> str:
        """Get description for a behavior."""
        return self.description_extractor.get_behavior_description(f'{self.bot_name}-{behavior_name}')
```

---

## stop_writing_useless_comments
**command_renderer.py** - 6 violation(s)

[X] ERROR (line 8)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class CursorCommandVisitor(CliVisitor):
    """Visitor that renders cursor command files."""
    
```

[X] ERROR (line 17)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def visit_header(self, bot_name: str) -> None:
        """Visit header - not used for command files."""
        pass
```

[X] ERROR (line 21)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def visit_behavior(self, context: BehaviorHelpContext) -> None:
        """Visit a behavior - not used for command files (handled separately)."""
        pass
```

[X] ERROR (line 25)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def visit_action(self, context: ActionHelpContext) -> None:
        """Visit an action and add its help to output."""
        # Extract short description (first line or first sentence)
```

[X] ERROR (line 65)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def visit_action_help_section_header(self) -> None:
        """Visit action help section header - not used for command files."""
        pass
```

[X] ERROR (line 69)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def visit_footer(self) -> None:
        """Visit footer - add common patterns."""
        scope_epic = "{'type': 'epic', 'value': ['Epic Name']}"
```

---

## stop_writing_useless_comments
**cli_code_visitor.py** - 10 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class CliCodeVisitor(CliVisitor):
    """Visitor for generating CLI code files (Python, shell, PowerShell scripts)."""
    
```

[X] ERROR (line 17)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def visit_header(self, bot_name: str) -> None:
        """Visit header - not used for code generation."""
        pass
```

[X] ERROR (line 21)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def visit_behavior(self, context: BehaviorHelpContext) -> None:
        """Visit a behavior - not used for code generation."""
        pass
```

[X] ERROR (line 25)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def visit_action(self, context: ActionHelpContext) -> None:
        """Visit an action - not used for code generation."""
        pass
```

[X] ERROR (line 29)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def visit_action_help_section_header(self) -> None:
        """Visit action help section header - not used for code generation."""
        pass
```

[X] ERROR (line 33)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def visit_footer(self) -> None:
        """Visit footer - generate all CLI code files."""
        self.generate_python_cli_script()
```

[X] ERROR (line 39)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def generate_python_cli_script(self) -> Path:
        """Generate Python CLI script."""
        bot_dir = self.workspace_root / self.bot_location
```

[X] ERROR (line 93)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

def main():
    """Main CLI entry point.

    Environment variables are bootstrapped before import:
    - BOT_DIRECTORY: Self-detected from script location
    - WORKING_AREA: Read from bot_config.json (or pre-set by user)
    
    All subsequent code reads from these environment variables.
    """
    bot_directory = get_bot_directory()
```

[X] ERROR (line 123)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def generate_shell_script(self) -> Path:
        """Generate shell script wrapper."""
        bot_dir = self.workspace_root / self.bot_location
```

[X] ERROR (line 132)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def generate_powershell_script(self) -> Path:
        """Generate PowerShell script wrapper."""
        bot_dir = self.workspace_root / self.bot_location
```

---

## stop_writing_useless_comments
**unified_help_generator.py** - 7 violation(s)

[X] ERROR (line 8)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class UnifiedHelpGenerator:
    """Generator that visits behaviors and actions using a visitor pattern."""
    
```

[X] ERROR (line 18)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def generate(self) -> None:
        """Generate output by visiting all behaviors and actions."""
        self.visitor.visit_header(self.bot_name)
```

[X] ERROR (line 28)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def generate_help(self) -> None:
        """Backward compatibility alias for generate()."""
        self.generate()
```

[X] ERROR (line 32)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _render_action_help_section(self) -> None:
        """Backward compatibility - delegates to _visit_action_help_section."""
        self._visit_action_help_section()
```

[X] ERROR (line 36)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _visit_behavior(self, behavior) -> None:
        """Visit a behavior and create context for visitor."""
        behavior_name = behavior.name
```

[X] ERROR (line 51)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _get_additional_options(self, behavior_name: str) -> dict:
        """Get additional options for a behavior."""
        if behavior_name == 'code':
```

[X] ERROR (line 60)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _visit_action_help_section(self) -> None:
        """Visit all actions in the action help section."""
        self.visitor.visit_action_help_section_header()
```

---

## stop_writing_useless_comments
**help_renderer.py** - 6 violation(s)

[X] ERROR (line 10)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def visit_header(self, bot_name: str) -> None:
        """Visit header - delegates to render_header for backward compatibility."""
        self.render_header(bot_name)
```

[X] ERROR (line 15)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @abstractmethod
    def render_header(self, bot_name: str) -> None:
        """Render header (backward compatibility)."""
        pass
```

[X] ERROR (line 19)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def visit_behavior(self, context: BehaviorHelpContext) -> None:
        """Visit behavior - delegates to render_behavior_section for backward compatibility."""
        self.render_behavior_section(context)
```

[X] ERROR (line 23)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def visit_action(self, context: ActionHelpContext) -> None:
        """Visit action - delegates to render_action_help for backward compatibility."""
        self.render_action_help(context)
```

[X] ERROR (line 27)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def visit_action_help_section_header(self) -> None:
        """Visit action help section header - delegates for backward compatibility."""
        self.render_action_help_section_header()
```

[X] ERROR (line 54)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def render_action_help_section_header(self) -> None:
        """Render action help section header."""
        print('\n---\n')
```

---

## stop_writing_useless_comments
**cli_help_renderer.py** - 1 violation(s)

[X] ERROR (line 6)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class CliHelpVisitor(CliVisitor):
    """Visitor for generating CLI help output."""
    
```

---

## stop_writing_useless_comments
**cursor_help_renderer.py** - 1 violation(s)

[X] ERROR (line 7)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class CursorHelpVisitor(CliVisitor):
    """Visitor for generating cursor help output."""
    
```

---

## stop_writing_useless_comments
**cursor_command_generator.py** - 2 violation(s)

[X] ERROR (line 22)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _get_bot(self) -> Bot:
        """Lazy-load bot instance for dynamic help generation."""
        if self._bot is None:
```

[X] ERROR (line 30)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _get_data_collector(self) -> ActionDataCollector:
        """Lazy-load data collector for dynamic help generation."""
        if self._data_collector is None:
```

---

## stop_writing_useless_comments
**cli_generator.py** - 1 violation(s)

[X] ERROR (line 34)
Useless comment: "# Get generated file paths" - delete it or improve the code instead

```python
        code_visitor.visit_footer()  # Triggers code generation
        
        # Get generated file paths
        cli_python_path = bot_directory / 'src' / f'{self.bot_name}_cli.py'
```

---

## use_domain_language
**cli_code_visitor.py** - 3 violation(s)

[!] WARNING (line 38)
Function "generate_python_cli_script" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").

[!] WARNING (line 122)
Function "generate_shell_script" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").

[!] WARNING (line 131)
Function "generate_powershell_script" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").

---

Completed: 2025-12-22 12:00:57
Total violations: 63
Scanners executed: 30
