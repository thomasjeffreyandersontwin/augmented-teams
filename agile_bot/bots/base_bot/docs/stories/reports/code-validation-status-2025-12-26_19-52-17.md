# Validation Status - code
Started: 2025-12-26 19:52:17
Files: 256

## avoid_excessive_guards
**action.py** - 4 violation(s)

[!] WARNING (line 199)
Line 199: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    def execute(self, context: ActionContext = None) -> Dict[str, Any]:
        self.track_activity_on_start()
        if context is None:
            context = self.context_class()
        try:
```

[!] WARNING (line 290)
Line 290: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
        Loading/reading files is allowed. Writing files is NOT allowed.
        """
        if context is None:
            context = self.context_class()
        
```

[!] WARNING (line 384)
Line 384: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
        This is a template method. Subclasses override _do_submit() to customize.
        """
        if context is None:
            context = self.context_class()
        
```

[!] WARNING (line 406)
Line 406: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

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

[!] WARNING (line 32)
Line 32: Variable truthiness check detected (if not data:). Assume variable exists - let code fail fast if missing.

```python
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Scope':
        if not data:
            return cls()
        
```

---

## avoid_excessive_guards
**cli_action_parsers.py** - 1 violation(s)

[!] WARNING (line 74)
Line 74: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
            value = parse_json_dict(value)
        
        if value is not None:
            kwargs[field_name] = value
    
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
**repl_session.py** - 1 violation(s)

[!] WARNING (line 377)
Line 377: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

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
**help_renderer_visitor.py** - 3 violation(s)

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
**repl_command.py** - 1 violation(s)

[!] WARNING (line 167)
Line 167: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
        try:
            # Call the action's get_instructions() - it formats everything
            if context is None:
                context = action.context_class()
            
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

## avoid_unnecessary_parameter_passing
**render_action.py** - 2 violation(s)

[!] WARNING (line 50)
Instance property "self._render_specs" is extracted to variable "render_specs" and passed to internal method "_execute_synchronizers". Access via self._render_specs directly instead.

[!] WARNING (line 84)
Instance property "self._render_specs" is extracted to variable "render_specs" and passed to internal method "_execute_synchronizers". Access via self._render_specs directly instead.

---

## avoid_unnecessary_parameter_passing
**strategy_criteria.py** - 1 violation(s)

[!] WARNING (line 10)
Internal method "_format_options" receives parameter "options" that matches instance attribute. Consider accessing via self.options instead.

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

## delegate_to_lowest_level
**file_discovery.py** - 1 violation(s)

[i] INFO (line 24)
Method "_matches_any_exclude_pattern" in class "FileDiscovery" iterates through "exclude_patterns" instead of delegating to collection class. Delegate to collection class instead.

---

## delegate_to_lowest_level
**scope.py** - 2 violation(s)

[i] INFO (line 32)
Method "_collect_blocks_from_files" in class "Scope" iterates through "files" instead of delegating to collection class. Delegate to collection class instead.

[i] INFO (line 38)
Method "_create_files_from_paths" in class "Scope" iterates through "_file_paths" instead of delegating to collection class. Delegate to collection class instead.

---

## eliminate_duplication
**cli_code_visitor.py** - 1 violation(s)

[X] ERROR (line 15)
Duplicate code detected: functions visit_header, visit_behavior, visit_action, visit_action_help_section_header have identical bodies - extract to shared function

---

