# Validation Status - tests
Started: 2025-12-22 13:21:45
Files: 12

## call_production_code_directly
**cursor_command_generator.py** - 2 violation(s)

[X] ERROR (line 261)
Line 261 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 262)
Line 262 uses fake/stub implementation - tests should call real production code directly

---

## helper_extraction_and_reuse
**visitor.py** - 1 violation(s)

[X] ERROR (line 7)
Duplicate code detected: functions visit_header, visit_behavior, visit_action, visit_action_help_section_header, visit_footer have identical bodies - extract to shared function

---

## helper_extraction_and_reuse
**cli_code_visitor.py** - 2 violation(s)

[X] ERROR (line 14)
Duplicate code detected: functions visit_header, visit_behavior, visit_action, visit_action_help_section_header have identical bodies - extract to shared function

[X] ERROR (line 35)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_create_python_cli_script:35-39):
```python
cli_file = src_dir / f'{self.bot_name}_cli.py'
cli_code = self._build_python_cli_code()
cli_file.write_text(cli_code, encoding='utf-8')
cli_file.chmod(cli_file.stat().st_mode | stat.S_IEXEC)
return cl...
```

Location (_create_shell_script:137-141):
```python
script_file = bot_dir / f'{self.bot_name}_cli'
script_content = f'#!/bin/bash\n\n    SCRIPT_DIR="$(cd "$(dirname "${{BASH_SOURCE[0]}}")" && pwd)"\n\n    export WORKING_DIR="${{WORKING_DIR:-$(cd "$SCRI...
```

---

## helper_extraction_and_reuse
**command_renderer.py** - 1 violation(s)

[X] ERROR (line 14)
Duplicate code detected: functions visit_header, visit_behavior, visit_action_help_section_header have identical bodies - extract to shared function

---

## helper_extraction_and_reuse
**help_renderer.py** - 1 violation(s)

[X] ERROR (line 13)
Duplicate code detected: functions render_header, _format_behavior_command, _format_behavior_title, _format_action_command have identical bodies - extract to shared function

---

## helper_extraction_and_reuse
**mcp_code_visitor.py** - 1 violation(s)

[X] ERROR (line 33)
Duplicate code detected: functions visit_action, visit_action_help_section_header have identical bodies - extract to shared function

---


## Cross-File Duplication Analysis
Scanning 12 files...
Extracted 278 code blocks
Starting 38503 pairwise comparisons...
Comparing: 5% (1,926/38,503) - 2 violations - ETA: 18s  
Comparing: 10% (3,851/38,503) - 3 violations - ETA: 14s  
Comparing: 15% (5,776/38,503) - 9 violations - ETA: 13s  
Found 10 violations so far...
Comparing: 20% (7,701/38,503) - 17 violations - ETA: 12s  
Found 20 violations so far...
Comparing: 25% (9,626/38,503) - 26 violations - ETA: 11s  
Found 30 violations so far...
Comparing: 30% (11,551/38,503) - 31 violations - ETA: 10s  
Comparing: 35% (13,477/38,503) - 31 violations - ETA: 10s  
Comparing: 40% (15,402/38,503) - 33 violations - ETA: 8s  
Comparing: 45% (17,327/38,503) - 34 violations - ETA: 7s  
Comparing: 50% (19,252/38,503) - 34 violations - ETA: 7s  
Comparing: 55% (21,177/38,503) - 34 violations - ETA: 6s  
Comparing: 60% (23,102/38,503) - 34 violations - ETA: 5s  
Comparing: 65% (25,027/38,503) - 34 violations - ETA: 4s  
Comparing: 70% (26,953/38,503) - 34 violations - ETA: 4s  
Comparing: 75% (28,878/38,503) - 34 violations - ETA: 3s  
Comparing: 80% (30,803/38,503) - 34 violations - ETA: 2s  
Comparing: 85% (32,728/38,503) - 34 violations - ETA: 2s  
Comparing: 90% (34,653/38,503) - 34 violations - ETA: 1s  
Comparing: 95% (36,578/38,503) - 34 violations - ETA: 0s  
Comparing: 100% (38,503/38,503) - 34 violations - ETA: 0s  
Complete: 38503 comparisons, 34 violations

## no_fallbacks_in_tests
**mcp_code_visitor.py** - 1 violation(s)

[X] ERROR (line 255)
Line 255 uses fallback/default value - tests should use explicit test data, not fallbacks

---

## self_documenting_tests
**cli_generator.py** - 1 violation(s)

[X] ERROR (line 34)
Useless comment: "# Get generated file paths" - delete it or improve the code instead

---

