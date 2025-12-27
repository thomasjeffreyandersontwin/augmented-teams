# Validation Status - code
Started: 2025-12-27 00:56:33
Files: 270

## avoid_excessive_guards
**action.py** - 4 violation(s)

[!] WARNING (line 220)
Line 220: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    def execute(self, context: ActionContext = None) -> Dict[str, Any]:
        self.track_activity_on_start()
        if context is None:
            context = self.context_class()
        try:
```

[!] WARNING (line 311)
Line 311: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
        Loading/reading files is allowed. Writing files is NOT allowed.
        """
        if context is None:
            context = self.context_class()
        
```

[!] WARNING (line 408)
Line 408: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
        This is a template method. Subclasses override _do_submit() to customize.
        """
        if context is None:
            context = self.context_class()
        
```

[!] WARNING (line 430)
Line 430: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
        Updates workflow state and returns next action info.
        """
        if context is None:
            context = self.context_class()
        
```

---

## avoid_excessive_guards
**actions.py** - 1 violation(s)

[!] WARNING (line 207)
Line 207: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    def is_final_action(self) -> bool:
        try:
            if self.current is None:
                return False
            action_names = self.names
```

---

## avoid_excessive_guards
**action_context.py** - 1 violation(s)

[!] WARNING (line 144)
Line 144: Variable truthiness check detected (if not data:). Assume variable exists - let code fail fast if missing.

```python
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Scope':
        if not data:
            return cls()
        
```

---

## avoid_excessive_guards
**cli_help_renderer_visitor.py** - 3 violation(s)

[!] WARNING (line 19)
Line 19: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def formatter(self) -> CliTerminalFormatter:
        if self._formatter is None:
            self._formatter = CliTerminalFormatter()
        return self._formatter
```

[!] WARNING (line 25)
Line 25: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def description_extractor(self) -> DescriptionExtractor:
        if self._description_extractor is None:
            self._description_extractor = DescriptionExtractor(self.bot_name, self.bot_directory, self.formatter)
        return self._description_extractor
```

[!] WARNING (line 31)
Line 31: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def data_collector(self) -> ActionDataCollector:
        if self._data_collector is None:
            self._data_collector = ActionDataCollector(
                bot=self.bot,
                bot_name=self.bot_name,
                bot_directory=self.bot_directory,
                description_extractor=self.description_extractor
            )
        return self._data_collector
```

---

## avoid_excessive_guards
**cursor_command_renderer_visitor.py** - 3 violation(s)

[!] WARNING (line 22)
Line 22: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def formatter(self) -> CliTerminalFormatter:
        if self._formatter is None:
            self._formatter = CliTerminalFormatter()
        return self._formatter
```

[!] WARNING (line 28)
Line 28: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def description_extractor(self) -> DescriptionExtractor:
        if self._description_extractor is None:
            self._description_extractor = DescriptionExtractor(self.bot_name, self.bot_directory, self.formatter)
        return self._description_extractor
```

[!] WARNING (line 34)
Line 34: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def data_collector(self) -> ActionDataCollector:
        if self._data_collector is None:
            self._data_collector = ActionDataCollector(
                bot=self.bot,
                bot_name=self.bot_name,
                bot_directory=self.bot_directory,
                description_extractor=self.description_extractor
            )
        return self._data_collector
```

---

## avoid_excessive_guards
**cursor_help_renderer_visitor.py** - 3 violation(s)

[!] WARNING (line 21)
Line 21: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def formatter(self) -> CliTerminalFormatter:
        if self._formatter is None:
            self._formatter = CliTerminalFormatter()
        return self._formatter
```

[!] WARNING (line 27)
Line 27: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def description_extractor(self) -> DescriptionExtractor:
        if self._description_extractor is None:
            self._description_extractor = DescriptionExtractor(self.bot_name, self.bot_directory, self.formatter)
        return self._description_extractor
```

[!] WARNING (line 33)
Line 33: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def data_collector(self) -> ActionDataCollector:
        if self._data_collector is None:
            self._data_collector = ActionDataCollector(
                bot=self.bot,
                bot_name=self.bot_name,
                bot_directory=self.bot_directory,
                description_extractor=self.description_extractor
            )
        return self._data_collector
```

---

## avoid_excessive_guards
**mcp_code_visitor.py** - 3 violation(s)

[!] WARNING (line 26)
Line 26: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def formatter(self) -> CliTerminalFormatter:
        if self._formatter is None:
            self._formatter = CliTerminalFormatter()
        return self._formatter
```

[!] WARNING (line 32)
Line 32: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def description_extractor(self) -> DescriptionExtractor:
        if self._description_extractor is None:
            self._description_extractor = DescriptionExtractor(self.bot_name, self.bot_directory, self.formatter)
        return self._description_extractor
```

[!] WARNING (line 38)
Line 38: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def data_collector(self) -> ActionDataCollector:
        if self._data_collector is None:
            self._data_collector = ActionDataCollector(
                bot=self.bot,
                bot_name=self.bot_name,
                bot_directory=self.bot_directory,
                description_extractor=self.description_extractor
            )
        return self._data_collector
```

---

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
**cover_all_paths_scanner.py** - 1 violation(s)

[!] WARNING (line 41)
Line 41: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
                            break
                    # Break outer loop if we found code
                    if found_code_node is not None:
                        break
            
```

---

## avoid_excessive_guards
**file_link_builder.py** - 2 violation(s)

[!] WARNING (line 24)
Line 24: Variable truthiness check detected (if not is_absolute:). Assume variable exists - let code fail fast if missing.

```python
        file_path = Path(location)
        is_absolute = file_path.is_absolute() or (len(location) > 1 and location[1] == ':') or location.startswith('\\\\')
        if not is_absolute:
            return f'[`{location}`]({self.get_file_uri(location, line_number)})'
        if not self.workspace_directory:
```

[!] WARNING (line 47)
Line 47: Variable truthiness check detected (if line_number:). Assume variable exists - let code fail fast if missing.

```python
        except Exception as e:
            logger.debug(f'Failed to create fallback link for {location}: {e}')
            if line_number:
                return f'`{location}:{line_number}`'
            return f'`{location}`'
```

---

## avoid_excessive_guards
**command_file_visitor.py** - 3 violation(s)

[!] WARNING (line 30)
Line 30: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def formatter(self) -> CliTerminalFormatter:
        if self._formatter is None:
            self._formatter = CliTerminalFormatter()
        return self._formatter
```

[!] WARNING (line 36)
Line 36: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def description_extractor(self) -> DescriptionExtractor:
        if self._description_extractor is None:
            self._description_extractor = DescriptionExtractor(self.bot_name, self.bot_directory, self.formatter)
        return self._description_extractor
```

[!] WARNING (line 42)
Line 42: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def data_collector(self) -> ActionDataCollector:
        if self._data_collector is None:
            self._data_collector = ActionDataCollector(
                bot=self.bot,
                bot_name=self.bot_name,
                bot_directory=self.bot_directory,
                description_extractor=self.description_extractor
            )
        return self._data_collector
```

---

## avoid_excessive_guards
**command_renderer_visitor.py** - 3 violation(s)

[!] WARNING (line 22)
Line 22: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def formatter(self) -> CliTerminalFormatter:
        if self._formatter is None:
            self._formatter = CliTerminalFormatter()
        return self._formatter
```

[!] WARNING (line 28)
Line 28: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def description_extractor(self) -> DescriptionExtractor:
        if self._description_extractor is None:
            self._description_extractor = DescriptionExtractor(self.bot_name, self.bot_directory, self.formatter)
        return self._description_extractor
```

[!] WARNING (line 34)
Line 34: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def data_collector(self) -> ActionDataCollector:
        if self._data_collector is None:
            self._data_collector = ActionDataCollector(
                bot=self.bot,
                bot_name=self.bot_name,
                bot_directory=self.bot_directory,
                description_extractor=self.description_extractor
            )
        return self._data_collector
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

## avoid_excessive_guards
**ast_elements.py** - 6 violation(s)

[!] WARNING (line 47)
Line 47: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def get_many_functions(self) -> List[Function]:
        if self._elements is None:
            self._elements = self._extract_functions()
        return self._elements
```

[!] WARNING (line 86)
Line 86: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def get_many_classes(self) -> List[Class]:
        if self._elements is None:
            self._elements = self._extract_classes()
        return self._elements
```

[!] WARNING (line 122)
Line 122: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def get_many_if_statements(self) -> List[IfStatement]:
        if self._elements is None:
            self._elements = self._extract_if_statements()
        return self._elements
```

[!] WARNING (line 143)
Line 143: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    def has_bare_except(self) -> bool:
        for handler in self._node.handlers:
            if handler.type is None:
                return True
        return False
```

[!] WARNING (line 160)
Line 160: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def get_many_try_blocks(self) -> List[TryBlock]:
        if self._elements is None:
            self._elements = self._extract_try_blocks()
        return self._elements
```

[!] WARNING (line 196)
Line 196: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def get_many_imports(self) -> List[Import]:
        if self._elements is None:
            self._elements = self._extract_imports()
        return self._elements
```

---

## avoid_excessive_guards
**block.py** - 5 violation(s)

[!] WARNING (line 63)
Line 63: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    
    def has_similarity(self, other: 'Block', similarity_calculator) -> bool:
        if self._similarity_calculator is None:
            self._similarity_calculator = similarity_calculator
        return self._similarity_calculator.calculates_block_similarity(self, other)
```

[!] WARNING (line 68)
Line 68: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    
    def analyze_structure(self, code_structure_analyzer) -> List['Violation']:
        if self._code_structure_analyzer is None:
            self._code_structure_analyzer = code_structure_analyzer
        return self._code_structure_analyzer.analyzes_code_structure(self)
```

[!] WARNING (line 73)
Line 73: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    
    def calculate_complexity(self, complexity_metrics) -> dict:
        if self._complexity_metrics is None:
            self._complexity_metrics = complexity_metrics
        # This would use ComplexityMetrics to calculate various metrics
```

[!] WARNING (line 79)
Line 79: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    
    def check_class_naming(self, class_naming_checker) -> List['Violation']:
        if self._class_naming_checker is None:
            self._class_naming_checker = class_naming_checker
        return self._class_naming_checker.checks_class_name_matches_story(self) + \
```

[!] WARNING (line 85)
Line 85: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    
    def check_method_naming(self, method_naming_checker) -> List['Violation']:
        if self._method_naming_checker is None:
            self._method_naming_checker = method_naming_checker
        return self._method_naming_checker.checks_method_name_matches_scenario(self) + \
```

---

## chain_dependencies_properly
**cursor_command_file_visitor.py** - 1 violation(s)

[!] WARNING (line 69)
Passing self.python_command as parameter to _write_command_file(). Access it directly in the method through self.python_command instead.

```python
            return set()
    
    def _generate_base_commands(self) -> None:
        self.commands[f'{self.bot_name}'] = self._write_command_file(
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

## chain_dependencies_properly
**prefer_object_model_over_config_scanner.py** - 1 violation(s)

[!] WARNING (line 36)
Method "scan_file" in class "PreferObjectModelOverConfigScanner" takes parameter "rule_obj" that is already injected in __init__. Use self.rule_obj instead.

```python
        ]
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Dict[str, Any] = None) -> List[Violation]:
        violations = []
        
    # ... (truncated)
```

---

## chain_dependencies_properly
**command_file_visitor.py** - 1 violation(s)

[!] WARNING (line 98)
Passing self.python_command as parameter to _write_command_file(). Access it directly in the method through self.python_command instead.

```python
            return set()
    
    def _generate_base_commands(self) -> None:
        self.commands[f'{self.bot_name}'] = self._write_command_file(
```

---

## delegate_to_lowest_level
**mcp_code_visitor.py** - 1 violation(s)

[i] INFO (line 21)
Method "visit_header" in class "MCPCodeVisitor" iterates through "behaviors" instead of delegating to collection class. Delegate to collection class instead.

---

## delegate_to_lowest_level
**mcp_code_visitor.py** - 1 violation(s)

[i] INFO (line 49)
Method "visit_header" in class "MCPCodeVisitor" iterates through "behaviors" instead of delegating to collection class. Delegate to collection class instead.

---

## delegate_to_lowest_level
**repl_help.py** - 1 violation(s)

[i] INFO (line 24)
Method "format_as_lines" in class "StageCollection" iterates through "_stages" instead of delegating to collection class. Delegate to collection class instead.

---

## delegate_to_lowest_level
**display_section.py** - 1 violation(s)

[i] INFO (line 12)
Method "add_to_instructions" in class "HeaderLineCollection" iterates through "_lines" instead of delegating to collection class. Delegate to collection class instead.

---

## delegate_to_lowest_level
**rules_digest_guidance.py** - 1 violation(s)

[i] INFO (line 10)
Method "add_to_instructions" in class "GuidanceLineCollection" iterates through "_lines" instead of delegating to collection class. Delegate to collection class instead.

---

## eliminate_duplication
**cli_code_visitor.py** - 1 violation(s)

[X] ERROR (line 15)
Duplicate code detected: functions visit_header, visit_behavior, visit_action, visit_action_help_section_header have identical bodies - extract to shared function

---

## eliminate_duplication
**cli_parser_generator_visitor.py** - 1 violation(s)

[X] ERROR (line 28)
Duplicate code detected: functions visit_behavior, visit_action_help_section_header have identical bodies - extract to shared function

---

## eliminate_duplication
**cursor_command_file_visitor.py** - 1 violation(s)

[X] ERROR (line 41)
Duplicate code detected: functions visit_action, visit_action_help_section_header have identical bodies - extract to shared function

---

## eliminate_duplication
**cursor_command_renderer_visitor.py** - 1 violation(s)

[X] ERROR (line 43)
Duplicate code detected: functions visit_header, visit_behavior, visit_action_help_section_header have identical bodies - extract to shared function

---

## eliminate_duplication
**cursor_help_renderer_visitor.py** - 1 violation(s)

[X] ERROR (line 58)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (visit_behavior:58-62):
```python
self._add_line(f'## {cmd_name}')
self._add_line('')
self._add_line(f'{context.behavior_description}')
self._add_line('')
self._add_line('```')
```

Location (visit_action:76-80):
```python
self._add_line(f'### {context.action_name}')
self._add_line('')
self._add_line(f'{context.action_description}')
self._add_line('')
self._add_line('```')
```

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

[X] ERROR (line 28)
Duplicate code detected: functions visit_header, visit_behavior, visit_action, visit_action_help_section_header, visit_footer have identical bodies - extract to shared function

---

## eliminate_duplication
**mcp_code_visitor.py** - 1 violation(s)

[X] ERROR (line 61)
Duplicate code detected: functions visit_action, visit_action_help_section_header have identical bodies - extract to shared function

---

## eliminate_duplication
**status_display.py** - 1 violation(s)

[X] ERROR (line 88)
Duplicate code detected: functions __init__, reset have identical bodies - extract to shared function

---

## eliminate_duplication
**command_file_visitor.py** - 1 violation(s)

[X] ERROR (line 70)
Duplicate code detected: functions visit_action, visit_action_help_section_header have identical bodies - extract to shared function

---

## eliminate_duplication
**command_renderer_visitor.py** - 2 violation(s)

[X] ERROR (line 43)
Duplicate code detected: functions visit_header, visit_behavior, visit_action_help_section_header have identical bodies - extract to shared function

[X] ERROR (line 94)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_build_example_params:94-103):
```python
param_name = param.split()[0]
if '<dict>' in param:
    example_params.append(f"""{param_name} '{{"key": "value"}}'""")
elif '<list>' in param:
    example_params.append(f'{param_name} "value1" "value...
```

Location (_build_example_params_powershell:108-117):
```python
param_name = param.split()[0]
if '<dict>' in param:
    example_params.append(f'{param_name}="{{`"key`": `"value`"}}"')
elif '<list>' in param:
    example_params.append(f'{param_name}="value1" "value...
```

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
Scanning 270 files...
Extracted 3908 code blocks
Starting 7634278 pairwise comparisons...
Comparing: 0% (37,185/7,634,278) - 0 violations - ETA: 2043s  
Comparing: 0% (62,253/7,634,278) - 0 violations - ETA: 2432s  
Comparing: 1% (84,387/7,634,278) - 0 violations - ETA: 2684s  
Comparing: 1% (101,794/7,634,278) - 0 violations - ETA: 2960s  
Comparing: 1% (124,332/7,634,278) - 0 violations - ETA: 3020s  
Comparing: 1% (141,146/7,634,278) - 0 violations - ETA: 3185s  
Comparing: 2% (154,348/7,634,278) - 0 violations - ETA: 3392s  
Comparing: 2% (179,855/7,634,278) - 2 violations - ETA: 3315s  
Comparing: 2% (199,002/7,634,278) - 2 violations - ETA: 3362s  
Comparing: 2% (211,418/7,634,278) - 2 violations - ETA: 3511s  
Comparing: 2% (222,739/7,634,278) - 2 violations - ETA: 3660s  
Comparing: 3% (233,205/7,634,278) - 2 violations - ETA: 3808s  
Comparing: 3% (243,100/7,634,278) - 2 violations - ETA: 3952s  
Comparing: 3% (253,991/7,634,278) - 2 violations - ETA: 4068s  
Comparing: 3% (279,232/7,634,278) - 2 violations - ETA: 3951s  
Comparing: 4% (309,189/7,634,278) - 2 violations - ETA: 3790s  
Comparing: 4% (338,886/7,634,278) - 2 violations - ETA: 3659s  
Comparing: 4% (352,519/7,634,278) - 2 violations - ETA: 3718s  
Comparing: 4% (365,111/7,634,278) - 2 violations - ETA: 3783s  
Comparing: 4% (381,519/7,634,278) - 2 violations - ETA: 3802s  
Comparing: 5% (394,736/7,634,278) - 2 violations - ETA: 3851s  
Comparing: 5% (417,404/7,634,278) - 2 violations - ETA: 3804s  
Found 10 violations so far...
Comparing: 5% (450,291/7,634,278) - 13 violations - ETA: 3669s  
Found 20 violations so far...
Comparing: 6% (470,538/7,634,278) - 25 violations - ETA: 3654s  
Comparing: 6% (488,624/7,634,278) - 28 violations - ETA: 3656s  
Comparing: 6% (505,981/7,634,278) - 28 violations - ETA: 3663s  
Comparing: 6% (531,722/7,634,278) - 28 violations - ETA: 3606s  
Comparing: 7% (559,774/7,634,278) - 28 violations - ETA: 3538s  
Comparing: 7% (590,162/7,634,278) - 28 violations - ETA: 3461s  
Comparing: 8% (625,378/7,634,278) - 28 violations - ETA: 3362s  
Comparing: 8% (652,967/7,634,278) - 28 violations - ETA: 3314s  
Found 30 violations so far...
Comparing: 9% (693,651/7,634,278) - 37 violations - ETA: 3202s  
Found 40 violations so far...
Comparing: 9% (729,561/7,634,278) - 47 violations - ETA: 3123s  
Found 50 violations so far...
