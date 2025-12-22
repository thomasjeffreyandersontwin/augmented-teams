# Validation Status - code
Started: 2025-12-22 13:16:16
Files: 242

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

## eliminate_duplication
**visitor.py** - 1 violation(s)

[X] ERROR (line 7)
Duplicate code detected: functions visit_header, visit_behavior, visit_action, visit_action_help_section_header, visit_footer have identical bodies - extract to shared function

---


## Cross-File Duplication Analysis
Scanning 242 files...
Extracted 3476 code blocks
Starting 6039550 pairwise comparisons...
Comparing: 0% (30,194/6,039,550) - 0 violations - ETA: 1990s  
Comparing: 0% (51,498/6,039,550) - 0 violations - ETA: 2325s  
Comparing: 1% (73,765/6,039,550) - 0 violations - ETA: 2426s  
Comparing: 1% (93,266/6,039,550) - 0 violations - ETA: 2550s  
Comparing: 1% (109,930/6,039,550) - 0 violations - ETA: 2697s  
Comparing: 2% (132,357/6,039,550) - 0 violations - ETA: 2677s  
Comparing: 2% (149,239/6,039,550) - 0 violations - ETA: 2762s  
Comparing: 2% (164,733/6,039,550) - 1 violations - ETA: 2853s  
Comparing: 3% (193,999/6,039,550) - 1 violations - ETA: 2711s  
Comparing: 3% (207,537/6,039,550) - 1 violations - ETA: 2810s  
Comparing: 3% (220,484/6,039,550) - 1 violations - ETA: 2903s  
Comparing: 3% (231,462/6,039,550) - 1 violations - ETA: 3011s  
Comparing: 3% (241,319/6,039,550) - 1 violations - ETA: 3123s  
Comparing: 4% (259,565/6,039,550) - 1 violations - ETA: 3117s  
Comparing: 4% (287,417/6,039,550) - 1 violations - ETA: 3002s  
Comparing: 5% (310,470/6,039,550) - 1 violations - ETA: 2952s  
Comparing: 5% (330,237/6,039,550) - 1 violations - ETA: 2939s  
Comparing: 5% (348,360/6,039,550) - 1 violations - ETA: 2940s  
Comparing: 6% (371,617/6,039,550) - 1 violations - ETA: 2898s  
Comparing: 6% (394,117/6,039,550) - 1 violations - ETA: 2864s  
Comparing: 6% (405,073/6,039,550) - 1 violations - ETA: 2921s  
Comparing: 6% (421,236/6,039,550) - 1 violations - ETA: 2934s  
Comparing: 7% (435,276/6,039,550) - 1 violations - ETA: 2961s  
Comparing: 7% (456,592/6,039,550) - 1 violations - ETA: 2934s  
Comparing: 7% (473,736/6,039,550) - 1 violations - ETA: 2937s  
Comparing: 8% (497,914/6,039,550) - 1 violations - ETA: 2893s  
Comparing: 8% (526,979/6,039,550) - 1 violations - ETA: 2824s  
Comparing: 9% (556,198/6,039,550) - 1 violations - ETA: 2760s  
Comparing: 9% (581,029/6,039,550) - 1 violations - ETA: 2724s  
Comparing: 9% (598,477/6,039,550) - 1 violations - ETA: 2727s  
Comparing: 10% (610,108/6,039,550) - 1 violations - ETA: 2758s  
Comparing: 10% (633,780/6,039,550) - 1 violations - ETA: 2729s  
