# Validation Status - code
Started: 2025-12-22 13:17:08
Files: 11

## chain_dependencies_properly
**cli_code_visitor.py** - 1 violation(s)

[!] WARNING (line 14)
Method "visit_header" in class "CliCodeVisitor" takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.

```python
        self.bot_name = bot_name
    
    def visit_header(self, bot_name: str) -> None:
        pass
    
```

---

## chain_dependencies_properly
**command_renderer.py** - 1 violation(s)

[!] WARNING (line 14)
Method "visit_header" in class "CursorCommandVisitor" takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.

```python
        self.output_lines = output_lines
    
    def visit_header(self, bot_name: str) -> None:
        pass
    
```

---

## chain_dependencies_properly
**cursor_help_renderer.py** - 1 violation(s)

[!] WARNING (line 12)
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
**mcp_code_visitor.py** - 1 violation(s)

[!] WARNING (line 20)
Method "visit_header" in class "MCPCodeVisitor" takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.

```python
        self.server_file_path = None
    
    def visit_header(self, bot_name: str) -> None:
        for behavior in self.behaviors:
            trigger_words = self._load_trigger_words(behavior)
    # ... (truncated)
```

---

## delegate_to_lowest_level
**mcp_code_visitor.py** - 1 violation(s)

[i] INFO (line 21)
Method "visit_header" in class "MCPCodeVisitor" iterates through "behaviors" instead of delegating to collection class. Delegate to collection class instead.

---

## eliminate_duplication
**visitor.py** - 1 violation(s)

[X] ERROR (line 7)
Duplicate code detected: functions visit_header, visit_behavior, visit_action, visit_action_help_section_header, visit_footer have identical bodies - extract to shared function

---

## eliminate_duplication
**cli_code_visitor.py** - 1 violation(s)

[X] ERROR (line 14)
Duplicate code detected: functions visit_header, visit_behavior, visit_action, visit_action_help_section_header have identical bodies - extract to shared function

---

## eliminate_duplication
**command_renderer.py** - 1 violation(s)

[X] ERROR (line 14)
Duplicate code detected: functions visit_header, visit_behavior, visit_action_help_section_header have identical bodies - extract to shared function

---

## eliminate_duplication
**help_renderer.py** - 1 violation(s)

[X] ERROR (line 13)
Duplicate code detected: functions render_header, _format_behavior_command, _format_behavior_title, _format_action_command have identical bodies - extract to shared function

---

## eliminate_duplication
**mcp_code_visitor.py** - 1 violation(s)

[X] ERROR (line 33)
Duplicate code detected: functions visit_action, visit_action_help_section_header have identical bodies - extract to shared function

---


## Cross-File Duplication Analysis
Scanning 11 files...
Extracted 227 code blocks
Starting 25651 pairwise comparisons...
Comparing: 5% (1,283/25,651) - 1 violations - ETA: 18s  
Comparing: 10% (2,566/25,651) - 7 violations - ETA: 8s  
Found 10 violations so far...
Comparing: 15% (3,848/25,651) - 14 violations - ETA: 8s  
Found 20 violations so far...
Comparing: 20% (5,131/25,651) - 20 violations - ETA: 7s  
Comparing: 25% (6,413/25,651) - 28 violations - ETA: 7s  
Comparing: 30% (7,696/25,651) - 29 violations - ETA: 6s  
Comparing: 35% (8,978/25,651) - 29 violations - ETA: 6s  
Found 30 violations so far...
Comparing: 40% (10,261/25,651) - 31 violations - ETA: 5s  
Comparing: 45% (11,543/25,651) - 32 violations - ETA: 4s  
Comparing: 50% (12,826/25,651) - 32 violations - ETA: 4s  
Comparing: 55% (14,109/25,651) - 32 violations - ETA: 3s  
Comparing: 60% (15,391/25,651) - 32 violations - ETA: 3s  
Comparing: 65% (16,674/25,651) - 32 violations - ETA: 2s  
Comparing: 70% (17,956/25,651) - 32 violations - ETA: 2s  
Comparing: 75% (19,239/25,651) - 32 violations - ETA: 2s  
Comparing: 80% (20,521/25,651) - 32 violations - ETA: 1s  
Comparing: 85% (21,804/25,651) - 32 violations - ETA: 1s  
Comparing: 90% (23,086/25,651) - 32 violations - ETA: 0s  
Comparing: 95% (24,369/25,651) - 32 violations - ETA: 0s  
Comparing: 100% (25,651/25,651) - 32 violations - ETA: 0s  
Complete: 25651 comparisons, 32 violations

## maintain_vertical_density
**cli_code_visitor.py** - 1 violation(s)

[i] INFO (line 31)
Function "_create_python_cli_script" is 82 lines - consider improving vertical density by declaring variables near usage

```python
        self._create_powershell_script()
    
    def _create_python_cli_script(self) -> Path:
        bot_dir = self.workspace_root / self.bot_location
        src_dir = bot_dir / 'src'
        src_dir.mkdir(parents=True, exist_ok=True)
        cli_file = src_dir / f'{self.bot_name}_cli.py'
        cli_code = f'''#!/usr/bin/env python3
"""
{self.bot_name.title().replace('_', ' ')} CLI Entry Point
    # ... (truncated)
```

---

## maintain_vertical_density
**mcp_code_visitor.py** - 1 violation(s)

[i] INFO (line 98)
Function "_build_server_code" is 66 lines - consider improving vertical density by declaring variables near usage

```python
        return server_file
    
    def _build_server_code(self, base_tools_code: str, behavior_tools_code: str) -> str:
        return f'''"""
{self.bot_name.title().replace('_', ' ')} MCP Server Entry Point

Runnable MCP server for {self.bot_name} using FastMCP with statically generated tools.
"""
from pathlib import Path
import sys
    # ... (truncated)
```

---

## maintain_vertical_density
**cursor_command_generator.py** - 1 violation(s)

[i] INFO (line 160)
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

[!] WARNING (line 57)
Function "_build_example_params" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        self.output_lines.append(f"  # {example_cmd}")
    
    def _build_example_params(self, params: List[str]) -> List[str]:
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
        return example_params
    # ... (truncated)
```

---

## stop_writing_useless_comments
**cli_code_visitor.py** - 1 violation(s)

[X] ERROR (line 85)
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

---

## stop_writing_useless_comments
**mcp_code_visitor.py** - 1 violation(s)

[X] ERROR (line 139)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

def main():
    """Main entry point for {self.bot_name} MCP server.

    Environment variables are bootstrapped before import:
    - BOT_DIRECTORY: Self-detected from script location
    - WORKING_AREA: Read from bot_config.json (or overridden by mcp.json env)
    
    All subsequent code reads from these environment variables.
    """
    bot_directory = get_bot_directory()
```

---

## use_domain_language
**orchestrator.py** - 1 violation(s)

[!] WARNING (line 27)
Function "generate_help" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").

---

Completed: 2025-12-22 13:17:18
Total violations: 17
Scanners executed: 30
