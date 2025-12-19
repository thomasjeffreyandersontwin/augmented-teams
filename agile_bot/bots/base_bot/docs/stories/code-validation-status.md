# Validation Status - code
Started: 2025-12-19 10:31:19
Files: 92

## avoid_excessive_guards
**actions.py** - 1 violation(s)

[!] WARNING (line 156)
Line 156: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

---

## avoid_excessive_guards
**file_link_builder.py** - 2 violation(s)

[!] WARNING (line 27)
Line 27: Variable truthiness check detected (if not is_absolute:). Assume variable exists - let code fail fast if missing.

[!] WARNING (line 52)
Line 52: Variable truthiness check detected (if line_number:). Assume variable exists - let code fail fast if missing.

---

## avoid_excessive_guards
**rules.py** - 1 violation(s)

[!] WARNING (line 42)
Line 42: Variable truthiness check detected (if has_scope_in_params:). Assume variable exists - let code fail fast if missing.

---

## avoid_excessive_guards
**behaviors.py** - 2 violation(s)

[!] WARNING (line 247)
Line 247: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

[!] WARNING (line 251)
Line 251: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

---

## avoid_unnecessary_parameter_passing
**actions.py** - 1 violation(s)

[!] WARNING (line 114)
Instance property "self.current" is extracted to variable "current_action_obj" and passed to internal method "_mark_action_completed". Access via self.current directly instead.

---

## avoid_unnecessary_parameter_passing
**build_action.py** - 1 violation(s)

[!] WARNING (line 51)
Instance property "self.knowledge_graph_spec.knowledge_graph" is extracted to variable "story_graph" and passed to internal method "_add_update_instructions". Access via self.knowledge_graph_spec.knowledge_graph directly instead.

---

## chain_dependencies_properly
**rule_loader.py** - 1 violation(s)

[!] WARNING (line 20)
Method "_load_rules_from_glob" in class "RuleLoader" takes parameter "behavior" that is already injected in __init__. Use self.behavior instead.

---

## delegate_to_lowest_level
**file_discovery.py** - 1 violation(s)

[i] INFO (line 21)
Method "should_include_file" in class "FileDiscovery" iterates through "exclude_patterns" instead of delegating to collection class. Delegate to collection class instead.

---

## eliminate_duplication
**nodes.py** - 1 violation(s)

[X] ERROR (line 230)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (from_dict:230-234):
```python
sequential_order = float(data.get('sequential_order', index + 1))
scenario = cls(name=data.get('name', ''), sequential_order=sequential_order, type=data.get('type', ''), background=data.get('backgroun...
```

Location (from_dict:273-277):
```python
sequential_order = float(data.get('sequential_order', index + 1))
scenario_outline = cls(name=data.get('name', ''), sequential_order=sequential_order, type=data.get('type', ''), background=data.get('b...
```

---

## keep_functions_small_focused
**scanner_status_formatter.py** - 1 violation(s)

[i] INFO (line 29)
Function "categorize_scanner_rules" has deep nesting (depth=5) - should be under 4 levels. Extract nested logic to helper functions.

```python
        return lines

    def categorize_scanner_rules(self, validation_rules: List[Dict[str, Any]]) -> Dict:
        """Categorize rules by execution status."""
        executed_rules = []
        load_failed_rules = []
        execution_failed_rules = []
        no_scanner_rules = []
        for rule_dict in validation_rules:
            category = self._get_rule_category(rule_dict)
            if category == 'executed':
                executed_rules.append(self._build_executed_rule_entry(rule_dict))
            elif category == 'load_failed':
                load_failed_rules.append(self._build_failed_rule_entry(rule_dict))
            elif category == 'execution_failed':
                execution_failed_rules.append(self._build_failed_rule_entry(rule_dict))
            elif category == 'no_scanner':
                no_scanner_rules.append(self._get_rule_file(rule_dict))
        return {'executed': executed_rules, 'load_failed': load_failed_rules, 'execution_failed': execution_failed_rules, 'no_scanner': no_scanner_rules}

```

---

## provide_meaningful_context
**scanner_status_formatter.py** - 1 violation(s)

[!] WARNING (line 6)
Line 6 contains magic number - replace with named constant

---

## provide_meaningful_context
**validation_scanner_status_builder.py** - 1 violation(s)

[!] WARNING (line 8)
Line 8 contains magic number - replace with named constant

---

## remove_bad_comments
**validation_scanner_status_builder.py** - 1 violation(s)

[!] WARNING (line 143)
Line 143 has commented-out code - delete it (it's in git history if needed)

---

## simplify_control_flow
**scanner_status_formatter.py** - 1 violation(s)

[!] WARNING (line 29)
Function "categorize_scanner_rules" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

---

## use_clear_function_parameters
**workflow_status_builder.py** - 1 violation(s)

[!] WARNING (line 115)
Function "_build_current_behavior_section" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

---

## use_clear_function_parameters
**render_instruction_formatter.py** - 1 violation(s)

[!] WARNING (line 33)
Function "_update_instructions_dict" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

---

## use_clear_function_parameters
**rule.py** - 2 violation(s)

[!] WARNING (line 143)
Function "_execute_file_by_file_scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

[!] WARNING (line 155)
Function "_execute_cross_file_scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

---

## use_clear_function_parameters
**rules.py** - 5 violation(s)

[!] WARNING (line 176)
Function "_process_scanner_result" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

[!] WARNING (line 192)
Function "_execute_scanner" has 10 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

[!] WARNING (line 212)
Function "_process_rule" has 9 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

[!] WARNING (line 224)
Function "validate" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

[!] WARNING (line 229)
Function "_create_legacy_context" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

---

## use_clear_function_parameters
**validation_executor.py** - 1 violation(s)

[!] WARNING (line 81)
Function "_process_scanner_status" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

---

## use_clear_function_parameters
**validation_scanner_status_builder.py** - 3 violation(s)

[!] WARNING (line 38)
Function "_categorize_rule_by_status" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

[!] WARNING (line 241)
Function "_get_rule_status_display" has vague parameter name "info" - use descriptive name

[!] WARNING (line 255)
Function "_format_rule_scanner_info" has vague parameter name "info" - use descriptive name

---

## use_clear_function_parameters
**parameter_info_builder.py** - 1 violation(s)

[!] WARNING (line 24)
Function "add_param_detail" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

---

Completed: 2025-12-19 10:31:45
Total violations: 30
Scanners executed: 34
