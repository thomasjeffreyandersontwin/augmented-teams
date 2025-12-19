# Validation Status - code
Started: 2025-12-18 21:43:46
Files: 172

## avoid_excessive_guards
**action.py** - 4 violation(s)

[!] WARNING (line 37)
Line 37: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

[!] WARNING (line 240)
Line 240: Variable truthiness check detected (if not current_behavior:). Assume variable exists - let code fail fast if missing.

[!] WARNING (line 258)
Line 258: Variable truthiness check detected (if not behavior_obj:). Assume variable exists - let code fail fast if missing.

[!] WARNING (line 376)
Line 376: Variable truthiness check detected (if context_instructions:). Assume variable exists - let code fail fast if missing.

---

## avoid_excessive_guards
**actions.py** - 3 violation(s)

[!] WARNING (line 126)
Line 126: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

[!] WARNING (line 256)
Line 256: Variable truthiness check detected (if current_action_obj:). Assume variable exists - let code fail fast if missing.

[!] WARNING (line 270)
Line 270: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

---

## avoid_excessive_guards
**action_scope.py** - 1 violation(s)

[!] WARNING (line 119)
Line 119: Variable truthiness check detected (if not scope_config:). Assume variable exists - let code fail fast if missing.

---

## avoid_excessive_guards
**behavior.py** - 1 violation(s)

[!] WARNING (line 98)
Line 98: Variable truthiness check detected (if next_action:). Assume variable exists - let code fail fast if missing.

---

## avoid_excessive_guards
**behaviors.py** - 3 violation(s)

[!] WARNING (line 91)
Line 91: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

[!] WARNING (line 292)
Line 292: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

[!] WARNING (line 296)
Line 296: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

---

## avoid_excessive_guards
**trigger_router.py** - 4 violation(s)

[!] WARNING (line 81)
Line 81: Variable truthiness check detected (if route:). Assume variable exists - let code fail fast if missing.

[!] WARNING (line 86)
Line 86: Variable truthiness check detected (if route:). Assume variable exists - let code fail fast if missing.

[!] WARNING (line 91)
Line 91: Variable truthiness check detected (if route:). Assume variable exists - let code fail fast if missing.

[!] WARNING (line 96)
Line 96: Variable truthiness check detected (if route:). Assume variable exists - let code fail fast if missing.

---

## avoid_excessive_guards
**mcp_server_generator.py** - 2 violation(s)

[!] WARNING (line 545)
Line 545: File existence check detected. Let file operations fail if file missing - handle errors centrally.

[!] WARNING (line 670)
Line 670: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

---

## avoid_excessive_guards
**nodes.py** - 1 violation(s)

[!] WARNING (line 557)
Line 557: hasattr() guard clause detected. Assume attributes exist - let AttributeError propagate if missing.

---

## avoid_excessive_guards
**build_action.py** - 1 violation(s)

[!] WARNING (line 64)
Line 64: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

---

## avoid_excessive_guards
**knowledge_graph_spec.py** - 2 violation(s)

[!] WARNING (line 76)
Line 76: Variable truthiness check detected (if not template_filename:). Assume variable exists - let code fail fast if missing.

[!] WARNING (line 85)
Line 85: Variable truthiness check detected (if not template_filename:). Assume variable exists - let code fail fast if missing.

---

## avoid_excessive_guards
**render_config_loader.py** - 2 violation(s)

[!] WARNING (line 111)
Line 111: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

[!] WARNING (line 105)
Line 105: hasattr() guard clause detected. Assume attributes exist - let AttributeError propagate if missing.

---

## avoid_excessive_guards
**render_instruction_formatter.py** - 1 violation(s)

[!] WARNING (line 71)
Line 71: Variable truthiness check detected (if not render_configs:). Assume variable exists - let code fail fast if missing.

---

## avoid_excessive_guards
**render_spec.py** - 1 violation(s)

[!] WARNING (line 13)
Line 13: Variable truthiness check detected (if config_file:). Assume variable exists - let code fail fast if missing.

---

## avoid_excessive_guards
**rule.py** - 2 violation(s)

[!] WARNING (line 26)
Line 26: Variable truthiness check detected (if scanner_path:). Assume variable exists - let code fail fast if missing.

[!] WARNING (line 163)
Line 163: Variable truthiness check detected (if violations_cross_file:). Assume variable exists - let code fail fast if missing.

---

## avoid_excessive_guards
**rules.py** - 3 violation(s)

[!] WARNING (line 66)
Line 66: Variable truthiness check detected (if has_scope_in_params:). Assume variable exists - let code fail fast if missing.

[!] WARNING (line 244)
Line 244: Variable truthiness check detected (if not rules:). Assume variable exists - let code fail fast if missing.

[!] WARNING (line 269)
Line 269: Variable truthiness check detected (if not formatted_sections:). Assume variable exists - let code fail fast if missing.

---

## avoid_excessive_guards
**validate_action.py** - 1 violation(s)

[!] WARNING (line 64)
Line 64: Variable truthiness check detected (if run_in_background:). Assume variable exists - let code fail fast if missing.

---

## avoid_excessive_guards
**validation_report_writer.py** - 3 violation(s)

[!] WARNING (line 100)
Line 100: Variable truthiness check detected (if not violations:). Assume variable exists - let code fail fast if missing.

[!] WARNING (line 688)
Line 688: Variable truthiness check detected (if has_errors:). Assume variable exists - let code fail fast if missing.

[!] WARNING (line 690)
Line 690: Variable truthiness check detected (if has_warnings:). Assume variable exists - let code fail fast if missing.

---

## avoid_excessive_guards
**validation_scope.py** - 6 violation(s)

[!] WARNING (line 88)
Line 88: Variable truthiness check detected (if files_list:). Assume variable exists - let code fail fast if missing.

[!] WARNING (line 102)
Line 102: File existence check detected. Let file operations fail if file missing - handle errors centrally.

[!] WARNING (line 183)
Line 183: Variable truthiness check detected (if files:). Assume variable exists - let code fail fast if missing.

[!] WARNING (line 156)
Line 156: Variable truthiness check detected (if files:). Assume variable exists - let code fail fast if missing.

[!] WARNING (line 191)
Line 191: Variable truthiness check detected (if files:). Assume variable exists - let code fail fast if missing.

[!] WARNING (line 167)
Line 167: Variable truthiness check detected (if files:). Assume variable exists - let code fail fast if missing.

---

## avoid_technical_abstractions
**render_config_loader.py** - 1 violation(s)

[!] WARNING (line 10)
Class "RenderConfigLoader" separates technical abstraction. Keep technical details (saving, loading) as part of domain concepts instead.

---

## avoid_unnecessary_parameter_passing
**validation_scope.py** - 1 violation(s)

[!] WARNING (line 259)
Line 259: Passing self._behavior_name as parameter to _behavior_to_directory(). Access it directly in the method through self._behavior_name instead.

---

## chain_dependencies_properly
**action.py** - 2 violation(s)

[!] WARNING (line 186)
Method "_get_completed_actions_for_behavior" in class "Action" takes parameter "behavior" that is already injected in __init__. Use self.behavior instead.

[!] WARNING (line 195)
Method "_format_action_line" in class "Action" takes parameter "action_name" that is already injected in __init__. Use self.action_name instead.

---

## chain_dependencies_properly
**actions.py** - 1 violation(s)

[!] WARNING (line 40)
Method "_create_action_instance" in class "Actions" takes parameter "behavior" that is already injected in __init__. Use self.behavior instead.

---

## chain_dependencies_properly
**trigger_router.py** - 3 violation(s)

[!] WARNING (line 254)
Method "_load_bot_triggers" in class "TriggerRouter" takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.

[!] WARNING (line 278)
Method "_load_behavior_triggers" in class "TriggerRouter" takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.

[!] WARNING (line 304)
Method "_load_action_triggers" in class "TriggerRouter" takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.

---

## chain_dependencies_properly
**requirements_clarifications.py** - 1 violation(s)

[!] WARNING (line 40)
Method "load_all" in class "RequirementsClarifications" takes parameter "bot_paths" that is already injected in __init__. Use self.bot_paths instead.

---

## chain_dependencies_properly
**strategy_decision.py** - 1 violation(s)

[!] WARNING (line 47)
Method "load_all" in class "StrategyDecision" takes parameter "bot_paths" that is already injected in __init__. Use self.bot_paths instead.

---

## chain_dependencies_properly
**validation_scope.py** - 1 violation(s)

[!] WARNING (line 39)
Method "_behavior_to_directory" in class "ValidationScope" takes parameter "behavior_name" that is already injected in __init__. Use self.behavior_name instead.

---

## delegate_to_lowest_level
**actions.py** - 3 violation(s)

[i] INFO (line 114)
Method "find_by_name" in class "Actions" iterates through "_actions" instead of delegating to collection class. Delegate to collection class instead.

[i] INFO (line 120)
Method "find_by_order" in class "Actions" iterates through "_actions" instead of delegating to collection class. Delegate to collection class instead.

[i] INFO (line 134)
Method "__iter__" in class "Actions" iterates through "_actions" instead of delegating to collection class. Delegate to collection class instead.

---

## delegate_to_lowest_level
**behaviors.py** - 2 violation(s)

[i] INFO (line 85)
Method "find_by_name" in class "Behaviors" iterates through "_behaviors" instead of delegating to collection class. Delegate to collection class instead.

[i] INFO (line 99)
Method "__iter__" in class "Behaviors" iterates through "_behaviors" instead of delegating to collection class. Delegate to collection class instead.

---

## delegate_to_lowest_level
**bot.py** - 1 violation(s)

[i] INFO (line 43)
Method "__init__" in class "Bot" iterates through "behaviors" instead of delegating to collection class. Delegate to collection class instead.

---

## delegate_to_lowest_level
**render_action.py** - 2 violation(s)

[i] INFO (line 101)
Method "templates" in class "RenderOutputAction" iterates through "_render_specs" instead of delegating to collection class. Delegate to collection class instead.

[i] INFO (line 109)
Method "synchronizers" in class "RenderOutputAction" iterates through "_render_specs" instead of delegating to collection class. Delegate to collection class instead.

---

## eliminate_duplication
**action.py** - 1 violation(s)

[X] ERROR (line 113)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_inject_clarification_data:113-127):
```python
bot_paths = self.behavior.bot_paths
clarification_data = RequirementsClarifications.load_all(bot_paths)
if not clarification_data:
    return []
instructions['clarification'] = clarification_data
retu...
```

Location (_inject_strategy_data:130-144):
```python
bot_paths = self.behavior.bot_paths
strategy_data = StrategyDecision.load_all(bot_paths)
if not strategy_data:
    return []
instructions['strategy'] = strategy_data
return ['', '**STRATEGY DATA AVAIL...
```

---

## eliminate_duplication
**trigger_domain.py** - 4 violation(s)

[X] ERROR (line 38)
Duplicate code detected: functions __getitem__, __getitem__ have identical bodies - extract to shared function

[X] ERROR (line 41)
Duplicate code detected: functions __contains__, __contains__ have identical bodies - extract to shared function

[X] ERROR (line 44)
Duplicate code detected: functions items, items have identical bodies - extract to shared function

[X] ERROR (line 47)
Duplicate code detected: functions keys, keys have identical bodies - extract to shared function

---

## eliminate_duplication
**trigger_router.py** - 1 violation(s)

[X] ERROR (line 271)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_load_triggers_from_behavior_file:271-276):
```python
content = behavior_file.read_text(encoding='utf-8')
behavior_data = json.loads(content)
return behavior_data.get('trigger_words', {}).get('patterns', [])
```

Location (_load_patterns_from_file:384-389):
```python
content = file_path.read_text(encoding='utf-8')
data = json.loads(content)
return data.get('patterns', [])
```

---

## eliminate_duplication
**domain.py** - 1 violation(s)

[X] ERROR (line 16)
Duplicate code detected: functions __str__, __str__ have identical bodies - extract to shared function

---

## eliminate_duplication
**nodes.py** - 1 violation(s)

[X] ERROR (line 329)
Duplicate code detected: functions steps, steps have identical bodies - extract to shared function

---

## eliminate_duplication
**render_instruction_formatter.py** - 1 violation(s)

[X] ERROR (line 132)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (format_executed_synchronizers:132-136):
```python
parts = []
parts.append('**Synchronizers Already Executed:**')
parts.append('')
parts.append('The following render configurations have been automatically executed via synchronizers:')
parts.append('')
```

Location (format_template_instructions:163-167):
```python
parts = []
parts.append('**Template-Based Render Configurations Requiring AI Handling:**')
parts.append('')
parts.append('The following render configurations use templates and require AI assistance to...
```

---

## eliminate_duplication
**validation_report_writer.py** - 1 violation(s)

[X] ERROR (line 840)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_format_violation_line:840-846):
```python
location = violation.get('location', 'unknown')
message = violation.get('violation_message', 'No message')
severity = violation.get('severity', 'error')
line_number = violation.get('line_number')
seve...
```

Location (sort_key:679-684):
```python
rule_file = rule_dict.get('rule_file', 'unknown')
status_info = rule_status_lookup.get(rule_file, {})
status = status_info.get('status', 'UNKNOWN')
has_errors = status_info.get('has_errors', False)
ha...
```

---


## Cross-File Duplication Analysis
Scanning 62 files...
Extracted 1295 code blocks
Starting 837865 pairwise comparisons...
Comparing: 46% (1,036,969/2,208,151) - 11 violations - ETA: 496s
Comparing: 9% (82,088/837,865) - 0 violations - ETA: 368s
Comparing: 2% (20,088/837,865) - 0 violations - ETA: 407s
Comparing: 47% (1,054,332/2,208,151) - 11 violations - ETA: 492s
Comparing: 11% (100,182/837,865) - 0 violations - ETA: 368s
Comparing: 4% (35,639/837,865) - 0 violations - ETA: 450s
Comparing: 49% (1,082,188/2,208,151) - 13 violations - ETA: 478s
Comparing: 14% (122,058/837,865) - 0 violations - ETA: 351s
Comparing: 6% (57,762/837,865) - 0 violations - ETA: 405s
Comparing: 49% (1,101,702/2,208,151) - 14 violations - ETA: 472s
Comparing: 16% (141,209/837,865) - 0 violations - ETA: 345s
Comparing: 9% (81,766/837,865) - 0 violations - ETA: 369s
Comparing: 50% (1,124,687/2,208,151) - 14 violations - ETA: 462s
Comparing: 19% (162,618/837,865) - 0 violations - ETA: 332s
Comparing: 11% (99,254/837,865) - 0 violations - ETA: 372s
