# Validation Status - code
Started: 2025-12-22 12:50:29
Files: 4

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


## Cross-File Duplication Analysis
Scanning 4 files...
Extracted 72 code blocks
Starting 2556 pairwise comparisons...
Comparing: 5% (128/2,556) - 0 violations - ETA: 18s  
Comparing: 10% (256/2,556) - 0 violations - ETA: 8s  
Comparing: 15% (384/2,556) - 0 violations - ETA: 5s  
Comparing: 20% (512/2,556) - 0 violations - ETA: 3s  
Comparing: 25% (639/2,556) - 0 violations - ETA: 3s  
Comparing: 30% (767/2,556) - 1 violations - ETA: 2s  
Comparing: 35% (895/2,556) - 3 violations - ETA: 1s  
Comparing: 40% (1,023/2,556) - 4 violations - ETA: 1s  
Comparing: 45% (1,151/2,556) - 6 violations - ETA: 1s  
Comparing: 50% (1,278/2,556) - 9 violations - ETA: 1s  
Found 10 violations so far...
Comparing: 55% (1,406/2,556) - 11 violations - ETA: 0s  
Comparing: 60% (1,534/2,556) - 14 violations - ETA: 0s  
Comparing: 65% (1,662/2,556) - 18 violations - ETA: 0s  
Found 20 violations so far...
Comparing: 70% (1,790/2,556) - 21 violations - ETA: 0s  
Comparing: 75% (1,917/2,556) - 24 violations - ETA: 0s  
Comparing: 80% (2,045/2,556) - 25 violations - ETA: 0s  
Comparing: 85% (2,173/2,556) - 25 violations - ETA: 0s  
Comparing: 90% (2,301/2,556) - 25 violations - ETA: 0s  
Comparing: 95% (2,429/2,556) - 25 violations - ETA: 0s  
Comparing: 100% (2,556/2,556) - 25 violations - ETA: 0s  
Complete: 2556 comparisons, 25 violations

## maintain_vertical_density
**cli_code_visitor.py** - 1 violation(s)

[i] INFO (line 38)
Function "_create_python_cli_script" is 83 lines - consider improving vertical density by declaring variables near usage

```python
        self._create_powershell_script()
    
    def _create_python_cli_script(self) -> Path:
        """Create Python CLI script file."""
        bot_dir = self.workspace_root / self.bot_location
        src_dir = bot_dir / 'src'
        src_dir.mkdir(parents=True, exist_ok=True)
        cli_file = src_dir / f'{self.bot_name}_cli.py'
        cli_code = f'''#!/usr/bin/env python3
"""
    # ... (truncated)
```

---

## simplify_control_flow
**command_renderer.py** - 1 violation(s)

[!] WARNING (line 65)
Function "_build_example_params" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        self.output_lines.append(f"  # {example_cmd}")
    
    def _build_example_params(self, params: List[str]) -> List[str]:
        """Build example parameter strings."""
        example_params = []
        for param in params:
            param_name = param.split()[0]
            if '<dict>' in param:
                example_params.append(f"{param_name} '{{\"key\": \"value\"}}'")
            elif '<list>' in param:
                example_params.append(f'{param_name} "value1" "value2"')
            elif '<flag>' in param:
                example_params.append(param_name)
            else:
                example_params.append(f'{param_name} "value"')
    # ... (truncated)
```

---

## stop_writing_useless_comments
**command_renderer.py** - 10 violation(s)

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
        short_desc = self._extract_short_description(context)
```

[X] ERROR (line 40)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _extract_short_description(self, context: ActionHelpContext) -> str:
        """Extract short description from action description."""
        if not context.action_description:
```

[X] ERROR (line 46)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _append_parameter_help(self, context: ActionHelpContext) -> None:
        """Append parameter help to output lines."""
        for param in context.parameters:
```

[X] ERROR (line 55)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _append_example_command(self, context: ActionHelpContext) -> None:
        """Append example command with parameters."""
        example_params = self._build_example_params(context.parameters[:2])
```

[X] ERROR (line 66)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _build_example_params(self, params: List[str]) -> List[str]:
        """Build example parameter strings."""
        example_params = []
```

[X] ERROR (line 81)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def visit_action_help_section_header(self) -> None:
        """Visit action help section header - not used for command files."""
        pass
```

[X] ERROR (line 85)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def visit_footer(self) -> None:
        """Visit footer - add common patterns."""
        scope_epic = "{'type': 'epic', 'value': ['Epic Name']}"
```

---

## stop_writing_useless_comments
**cli_help_renderer.py** - 3 violation(s)

[X] ERROR (line 6)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class CliHelpVisitor(CliVisitor):
    """Visitor for generating CLI help output."""
    
```

[X] ERROR (line 43)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _print_parameters(self, context: ActionHelpContext) -> None:
        """Print parameter descriptions."""
        for param in context.parameters:
```

[X] ERROR (line 52)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _print_multiline_parameter(self, param: str, param_desc: str) -> None:
        """Print multiline parameter description."""
        lines = param_desc.split('\n')
```

---

## stop_writing_useless_comments
**cursor_help_renderer.py** - 3 violation(s)

[X] ERROR (line 7)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class CursorHelpVisitor(CliVisitor):
    """Visitor for generating cursor help output."""
    
```

[X] ERROR (line 47)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _print_parameters(self, context: ActionHelpContext) -> None:
        """Print parameter descriptions."""
        for param in context.parameters:
```

[X] ERROR (line 56)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _print_multiline_parameter(self, param: str, param_desc: str) -> None:
        """Print multiline parameter description."""
        lines = param_desc.split('\n')
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
        """Visit footer - create all CLI code files."""
        self._create_python_cli_script()
```

[X] ERROR (line 39)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _create_python_cli_script(self) -> Path:
        """Create Python CLI script file."""
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

    def _create_shell_script(self) -> Path:
        """Create shell script wrapper file."""
        bot_dir = self.workspace_root / self.bot_location
```

[X] ERROR (line 132)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _create_powershell_script(self) -> Path:
        """Create PowerShell script wrapper file."""
        bot_dir = self.workspace_root / self.bot_location
```

---

Completed: 2025-12-22 12:50:30
Total violations: 31
Scanners executed: 30
