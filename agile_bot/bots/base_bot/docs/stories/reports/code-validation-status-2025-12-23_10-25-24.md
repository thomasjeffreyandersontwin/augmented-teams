# Validation Status - code
Started: 2025-12-23 10:25:24
Files: 247

## avoid_excessive_guards
**action.py** - 1 violation(s)

[!] WARNING (line 162)
Line 162: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    def execute(self, context: ActionContext = None) -> Dict[str, Any]:
        self.track_activity_on_start()
        if context is None:
            context = self.context_class()
        try:
```

---

## avoid_excessive_guards
**actions.py** - 1 violation(s)

[!] WARNING (line 183)
Line 183: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

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
    def from_dict(cls, data: Dict[str, Any]) -> 'ScopeConfig':
        if not data:
            return cls()
        
```

---

## avoid_excessive_guards
**behaviors.py** - 2 violation(s)

[!] WARNING (line 247)
Line 247: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
        next_behavior_obj = self.next()
        expected_next = next_behavior_obj.name if next_behavior_obj else None
        if requested_matched is None:
            matches = False
        elif requested_matched == current_behavior:
            matches = True
        elif expected_next is None:
            matches = True
        else:
            matches = requested_matched == expected_next
        logger.debug(f'Behavior order check: requested={requested_behavior} ({requested_matched}), current={current_behavior}, expected_next={expected_next}, matches={matches}')
```

[!] WARNING (line 251)
Line 251: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
        elif requested_matched == current_behavior:
            matches = True
        elif expected_next is None:
            matches = True
        else:
            matches = requested_matched == expected_next
        logger.debug(f'Behavior order check: requested={requested_behavior} ({requested_matched}), current={current_behavior}, expected_next={expected_next}, matches={matches}')
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
**repl_session.py** - 1 violation(s)

[!] WARNING (line 43)
Line 43: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    
    def display_current_state(self) -> REPLStateDisplay:
        if self.current_state is None:
            return REPLStateDisplay(
                output="No behavior action state found. Please select a behavior to begin.",
                state_loaded=False
            )
        
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
**code_scanner.py** - 1 violation(s)

[!] WARNING (line 38)
Line 38: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
        
        # Store knowledge_graph in instance for scanners that need it
        if knowledge_graph is not None:
            self.knowledge_graph = knowledge_graph
        
```

---

## avoid_excessive_guards
**cover_all_paths_scanner.py** - 1 violation(s)

[!] WARNING (line 39)
Line 39: Variable truthiness check detected (if has_code:). Assume variable exists - let code fail fast if missing.

```python
                            has_code = True
                            break
                    if has_code:
                        break
            
```

---

## avoid_excessive_guards
**scanner_orchestrator.py** - 1 violation(s)

[!] WARNING (line 47)
Line 47: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
        scanner: 'Scanner' = None
    ) -> 'Scan':
        if scanner is None:
            scanner = self.selects_scanner_helpers_by_rule(rule)
        
```

---

## avoid_excessive_guards
**violation.py** - 1 violation(s)

[!] WARNING (line 57)
Line 57: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
        }
        
        if self._location is not None:
            result['location'] = self._location
        
```

---

## avoid_excessive_guards
**rules.py** - 1 violation(s)

[!] WARNING (line 145)
Line 145: Variable truthiness check detected (if changed:). Assume variable exists - let code fail fast if missing.

```python
        for file_type, file_list in files.items():
            changed = [f for f in file_list if f.stat().st_mtime > last_report_time]
            if changed:
                changed_files[file_type] = changed
        
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
**scanner_orchestrator.py** - 1 violation(s)

[!] WARNING (line 27)
Method "selects_scanner_helpers_by_rule" in class "ScannerOrchestrator" takes parameter "scanner_registry" that is already injected in __init__. Use self.scanner_registry instead.

```python
        return self._scanner_registry
    
    def selects_scanner_helpers_by_rule(
        self,
        rule: 'Rule',
    # ... (truncated)
```

---

## chain_dependencies_properly
**rule_loader.py** - 1 violation(s)

[!] WARNING (line 22)
Method "_load_rules_from_glob" in class "RuleLoader" takes parameter "behavior" that is already injected in __init__. Use self.behavior instead.

```python
        return bot_rules

    def _load_rules_from_glob(self, rules_dir: Path, pattern: str, behavior: str=None) -> List[Rule]:
        if behavior is None:
            if self.behavior and hasattr(self.behavior, 'name'):
    # ... (truncated)
```

---

## chain_dependencies_properly
**validation_scope.py** - 1 violation(s)

[!] WARNING (line 41)
Method "_extract_skiprule_from_scope" in class "ValidationScope" takes parameter "parameters" that is already injected in __init__. Use self.parameters instead.

```python
        return cls(params, bot_paths, behavior_name)
    
    def _extract_skiprule_from_scope(self, parameters: Dict[str, Any]) -> None:
        skiprule = []
        if 'scope' in parameters and isinstance(parameters.get('scope'), dict):
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

[i] INFO (line 48)
Method "visit_header" in class "MCPCodeVisitor" iterates through "behaviors" instead of delegating to collection class. Delegate to collection class instead.

---

## delegate_to_lowest_level
**display_section.py** - 1 violation(s)

[i] INFO (line 22)
Method "add_to" in class "DisplaySection" iterates through "header_lines" instead of delegating to collection class. Delegate to collection class instead.

---

## delegate_to_lowest_level
**rules_digest_guidance.py** - 1 violation(s)

[i] INFO (line 25)
Method "add_to" in class "RulesDigestGuidance" iterates through "lines" instead of delegating to collection class. Delegate to collection class instead.

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
**repl_session.py** - 2 violation(s)

[X] ERROR (line 246)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_handle_action_command:246-264):
```python
state_data = dict(self.current_state)
state_data['current_action'] = full_action
state_data['timestamp'] = datetime.now().isoformat()
self._save_state(state_data)
breadcrumbs = self._generate_breadcru...
```

Location (_handle_advance_command:383-401):
```python
state_data['completed_actions'] = completed_actions
state_data['current_action'] = full_action
state_data['timestamp'] = datetime.now().isoformat()
self._save_state(state_data)
breadcrumbs = self._gen...
```

[X] ERROR (line 421)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_handle_workspace_command:421-438):
```python
if not self.current_state:
    self.current_state = {'current_behavior': '', 'current_action': '', 'completed_actions': [], 'timestamp': datetime.now().isoformat()}
state_data = dict(self.current_stat...
```

Location (_handle_scope_command:477-496):
```python
if not self.current_state:
    self.current_state = {'current_behavior': '', 'current_action': '', 'completed_actions': [], 'timestamp': datetime.now().isoformat()}
state_data = dict(self.current_stat...
```

---

## eliminate_duplication
**visitor.py** - 1 violation(s)

[X] ERROR (line 28)
Duplicate code detected: functions visit_header, visit_behavior, visit_action, visit_action_help_section_header, visit_footer have identical bodies - extract to shared function

---

## eliminate_duplication
**mcp_code_visitor.py** - 1 violation(s)

[X] ERROR (line 60)
Duplicate code detected: functions visit_action, visit_action_help_section_header have identical bodies - extract to shared function

---

## eliminate_duplication
**generic_capability_scanner.py** - 1 violation(s)

[X] ERROR (line 42)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_check_capability_verbs:42-56):
```python
capability_verbs = ['exposes', 'provides', 'contains', 'represents', 'implements', 'supports']
name_lower = name.lower()
words = name_lower.split()
if words and words[0] in capability_verbs:
    locat...
```

Location (_check_passive_states:59-73):
```python
passive_patterns = ['tracks', 'maintains', 'stores', 'holds', 'keeps']
name_lower = name.lower()
words = name_lower.split()
if words and words[0] in passive_patterns:
    location = node.map_location(...
```

---

## eliminate_duplication
**scanner.py** - 1 violation(s)

[X] ERROR (line 50)
Duplicate code detected: functions scan_file, scan_cross_file, _scan_block have identical bodies - extract to shared function

---

## eliminate_duplication
**test_scanner.py** - 1 violation(s)

[X] ERROR (line 26)
Duplicate code detected: functions scan_file, scan_cross_file have identical bodies - extract to shared function

---

## eliminate_duplication
**build_action.py** - 1 violation(s)

[X] ERROR (line 198)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_replace_content_with_file_references:198-206):
```python
template_path_obj = Path(template_path)
if template_path_obj.is_absolute():
    rel_path = template_path_obj.relative_to(bot_dir)
    template_reference = f"{self.behavior.bot_name}/{str(rel_path).rep...
```

Location (_replace_content_with_file_references:230-238):
```python
config_path_obj = Path(config_path)
if config_path_obj.is_absolute():
    rel_path = config_path_obj.relative_to(bot_dir)
    config_reference = f"{self.behavior.bot_name}/{str(rel_path).replace('\\',...
```

---

## eliminate_duplication
**validation_report_writer.py** - 1 violation(s)

[X] ERROR (line 149)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_get_status_path:149-153):
```python
docs_path = self.bot_paths.documentation_path
docs_dir = self.workspace_directory / docs_path / 'reports'
docs_dir.mkdir(parents=True, exist_ok=True)
status_file = docs_dir / f'{self.behavior_name}-va...
```

Location (get_report_path:240-244):
```python
docs_path = self.bot_paths.documentation_path
docs_dir = self.workspace_directory / docs_path / 'reports'
docs_dir.mkdir(parents=True, exist_ok=True)
report_file = docs_dir / f'{self.behavior_name}-va...
```

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
**help_renderer_visitor.py** - 1 violation(s)

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


## Cross-File Duplication Analysis
Scanning 247 files...
Extracted 3679 code blocks
Starting 6765681 pairwise comparisons...
Comparing: 0% (32,781/6,765,681) - 0 violations - ETA: 2053s  
Comparing: 0% (54,922/6,765,681) - 0 violations - ETA: 2443s  
Comparing: 1% (79,321/6,765,681) - 0 violations - ETA: 2529s  
Comparing: 1% (100,232/6,765,681) - 0 violations - ETA: 2660s  
Comparing: 1% (118,301/6,765,681) - 0 violations - ETA: 2809s  
Comparing: 2% (142,972/6,765,681) - 0 violations - ETA: 2779s  
Comparing: 2% (160,861/6,765,681) - 0 violations - ETA: 2874s  
Comparing: 2% (180,684/6,765,681) - 2 violations - ETA: 2915s  
Comparing: 3% (208,729/6,765,681) - 2 violations - ETA: 2827s  
Comparing: 3% (221,953/6,765,681) - 2 violations - ETA: 2948s  
Comparing: 3% (234,972/6,765,681) - 2 violations - ETA: 3057s  
Comparing: 3% (246,691/6,765,681) - 2 violations - ETA: 3171s  
Comparing: 3% (256,910/6,765,681) - 2 violations - ETA: 3293s  
Comparing: 4% (279,634/6,765,681) - 2 violations - ETA: 3247s  
Comparing: 4% (308,325/6,765,681) - 2 violations - ETA: 3141s  
Comparing: 4% (332,581/6,765,681) - 2 violations - ETA: 3095s  
Comparing: 5% (354,150/6,765,681) - 2 violations - ETA: 3077s  
Comparing: 5% (373,428/6,765,681) - 2 violations - ETA: 3081s  
Comparing: 5% (401,107/6,765,681) - 2 violations - ETA: 3014s  
Comparing: 6% (420,307/6,765,681) - 2 violations - ETA: 3019s  
Comparing: 6% (432,175/6,765,681) - 2 violations - ETA: 3077s  
Comparing: 6% (449,261/6,765,681) - 2 violations - ETA: 3093s  
Comparing: 6% (463,498/6,765,681) - 2 violations - ETA: 3127s  
Comparing: 7% (487,864/6,765,681) - 2 violations - ETA: 3088s  
Comparing: 7% (506,257/6,765,681) - 2 violations - ETA: 3091s  
Comparing: 7% (532,463/6,765,681) - 2 violations - ETA: 3043s  
Comparing: 8% (560,964/6,765,681) - 2 violations - ETA: 2986s  
Comparing: 8% (591,620/6,765,681) - 2 violations - ETA: 2922s  
Comparing: 9% (617,707/6,765,681) - 2 violations - ETA: 2886s  
Comparing: 9% (636,861/6,765,681) - 2 violations - ETA: 2887s  
Comparing: 9% (648,219/6,765,681) - 2 violations - ETA: 2925s  
Comparing: 10% (678,483/6,765,681) - 2 violations - ETA: 2871s  
Comparing: 10% (717,675/6,765,681) - 2 violations - ETA: 2781s  
Comparing: 11% (750,138/6,765,681) - 2 violations - ETA: 2726s  
Comparing: 11% (777,985/6,765,681) - 2 violations - ETA: 2693s  
Comparing: 11% (801,776/6,765,681) - 2 violations - ETA: 2677s  
Comparing: 12% (827,037/6,765,681) - 2 violations - ETA: 2656s  
Comparing: 12% (847,045/6,765,681) - 2 violations - ETA: 2655s  
Comparing: 12% (863,591/6,765,681) - 2 violations - ETA: 2665s  
Found 10 violations so far...
Found 20 violations so far...
Found 30 violations so far...
Comparing: 13% (889,408/6,765,681) - 30 violations - ETA: 2642s  
Comparing: 13% (920,426/6,765,681) - 30 violations - ETA: 2603s  
Comparing: 14% (951,194/6,765,681) - 30 violations - ETA: 2567s  
Comparing: 14% (988,098/6,765,681) - 30 violations - ETA: 2514s  
Comparing: 14% (1,011,058/6,765,681) - 30 violations - ETA: 2504s  
Comparing: 15% (1,027,899/6,765,681) - 30 violations - ETA: 2512s  
Comparing: 15% (1,042,851/6,765,681) - 30 violations - ETA: 2524s  
Found 40 violations so far...
Found 50 violations so far...
Found 60 violations so far...
Comparing: 15% (1,075,212/6,765,681) - 61 violations - ETA: 2487s  
Comparing: 16% (1,105,220/6,765,681) - 61 violations - ETA: 2458s  
Comparing: 16% (1,138,445/6,765,681) - 61 violations - ETA: 2422s  
Comparing: 17% (1,162,329/6,765,681) - 61 violations - ETA: 2410s  
Comparing: 17% (1,181,806/6,765,681) - 61 violations - ETA: 2409s  
Comparing: 17% (1,211,408/6,765,681) - 61 violations - ETA: 2384s  
Comparing: 18% (1,236,498/6,765,681) - 61 violations - ETA: 2370s  
Comparing: 18% (1,258,013/6,765,681) - 61 violations - ETA: 2364s  
Comparing: 18% (1,275,245/6,765,681) - 61 violations - ETA: 2368s  
Comparing: 19% (1,295,886/6,765,681) - 61 violations - ETA: 2363s  
Comparing: 19% (1,316,664/6,765,681) - 61 violations - ETA: 2359s  
Comparing: 19% (1,332,124/6,765,681) - 61 violations - ETA: 2365s  
Comparing: 20% (1,365,981/6,765,681) - 61 violations - ETA: 2332s  
Comparing: 20% (1,397,128/6,765,681) - 61 violations - ETA: 2305s  
Found 70 violations so far...
Comparing: 21% (1,427,050/6,765,681) - 70 violations - ETA: 2282s  
Found 80 violations so far...
Comparing: 21% (1,456,004/6,765,681) - 81 violations - ETA: 2261s  
Comparing: 22% (1,496,098/6,765,681) - 81 violations - ETA: 2219s  
Comparing: 22% (1,546,098/6,765,681) - 81 violations - ETA: 2160s  
Comparing: 23% (1,591,946/6,765,681) - 81 violations - ETA: 2112s  
Comparing: 24% (1,627,941/6,765,681) - 87 violations - ETA: 2082s  
Comparing: 24% (1,658,202/6,765,681) - 87 violations - ETA: 2063s  
Comparing: 24% (1,682,617/6,765,681) - 87 violations - ETA: 2053s  
Comparing: 25% (1,702,143/6,765,681) - 87 violations - ETA: 2052s  
Comparing: 25% (1,728,205/6,765,681) - 87 violations - ETA: 2040s  
Comparing: 25% (1,750,543/6,765,681) - 87 violations - ETA: 2033s  
Comparing: 26% (1,779,284/6,765,681) - 87 violations - ETA: 2017s  
Found 90 violations so far...
Comparing: 26% (1,817,226/6,765,681) - 90 violations - ETA: 1987s  
Comparing: 27% (1,845,429/6,765,681) - 90 violations - ETA: 1972s  
Comparing: 27% (1,875,226/6,765,681) - 92 violations - ETA: 1955s  
Comparing: 28% (1,902,213/6,765,681) - 92 violations - ETA: 1942s  
Comparing: 28% (1,921,304/6,765,681) - 92 violations - ETA: 1941s  
Comparing: 28% (1,939,322/6,765,681) - 92 violations - ETA: 1940s  
Comparing: 28% (1,956,185/6,765,681) - 92 violations - ETA: 1942s  
Comparing: 29% (1,970,464/6,765,681) - 92 violations - ETA: 1946s  
Comparing: 29% (1,983,215/6,765,681) - 92 violations - ETA: 1953s  
Comparing: 29% (1,995,186/6,765,681) - 92 violations - ETA: 1960s  
Comparing: 29% (2,006,476/6,765,681) - 92 violations - ETA: 1968s  
Comparing: 29% (2,027,928/6,765,681) - 92 violations - ETA: 1962s  
Comparing: 30% (2,054,627/6,765,681) - 92 violations - ETA: 1948s  
Comparing: 30% (2,075,647/6,765,681) - 92 violations - ETA: 1942s  
Comparing: 31% (2,104,717/6,765,681) - 92 violations - ETA: 1926s  
Comparing: 31% (2,140,834/6,765,681) - 92 violations - ETA: 1900s  
Comparing: 32% (2,171,890/6,765,681) - 92 violations - ETA: 1882s  
Comparing: 32% (2,197,469/6,765,681) - 92 violations - ETA: 1870s  
Comparing: 32% (2,225,796/6,765,681) - 92 violations - ETA: 1855s  
Comparing: 33% (2,250,230/6,765,681) - 92 violations - ETA: 1845s  
Comparing: 33% (2,273,118/6,765,681) - 92 violations - ETA: 1837s  
Comparing: 33% (2,297,406/6,765,681) - 92 violations - ETA: 1828s  
Comparing: 34% (2,315,487/6,765,681) - 94 violations - ETA: 1825s  
Comparing: 34% (2,320,900/6,765,681) - 94 violations - ETA: 1838s  
Comparing: 34% (2,326,360/6,765,681) - 94 violations - ETA: 1850s  
Comparing: 34% (2,331,748/6,765,681) - 94 violations - ETA: 1863s  
Comparing: 34% (2,337,100/6,765,681) - 94 violations - ETA: 1875s  
Comparing: 34% (2,342,418/6,765,681) - 94 violations - ETA: 1888s  
Comparing: 34% (2,358,314/6,765,681) - 94 violations - ETA: 1887s  
Found 100 violations so far...
