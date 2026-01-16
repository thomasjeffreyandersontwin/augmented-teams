# Validation Status - code
Started: 2026-01-15 20:37:52
Files: 286

## avoid_excessive_guards
**action.py** - 2 violation(s)

[!] WARNING (line 316)
Line 316: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    def execute(self, context: ActionContext = None) -> Dict[str, Any]:
        self.track_activity_on_start()
        if context is None:
            context = self.context_class()
        try:
```

[!] WARNING (line 405)
Line 405: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
        This is a template method. Subclasses override _prepare_instructions() to customize.
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
                return False
            # If we have a current action, check position
            if self.current is not None:
                return self.current.action_name == action_names[-1]
            # If no current action, fall back to state file: consider final if last action is marked completed
```

---

## avoid_excessive_guards
**markdown_action.py** - 1 violation(s)

[!] WARNING (line 22)
Line 22: Variable truthiness check detected (if is_completed:). Assume variable exists - let code fail fast if missing.

```python
        if self.is_current:
            marker = "➤"
        elif is_completed:
            marker = "[X]"
        else:
            marker = "[ ]"
        
```

---

## avoid_excessive_guards
**bot.py** - 1 violation(s)

[!] WARNING (line 301)
Line 301: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
        import os
        
        if scope_filter is None:
            # Return current scope instance for property access
            return self._scope
        
```

---

## avoid_excessive_guards
**adapters.py** - 4 violation(s)

[!] WARNING (line 132)
Line 132: Variable truthiness check detected (if is_completed:). Assume variable exists - let code fail fast if missing.

```python
    def render_marker(self, is_completed: bool, is_current: bool) -> str:
        """Render progress marker."""
        if is_completed:
            return self.add_color('[X]', 'green')
        elif is_current:
            return self.add_color('[>]', 'yellow')
        else:
            return '[ ]'

```

[!] WARNING (line 134)
Line 134: Variable truthiness check detected (if is_current:). Assume variable exists - let code fail fast if missing.

```python
        if is_completed:
            return self.add_color('[X]', 'green')
        elif is_current:
            return self.add_color('[>]', 'yellow')
        else:
            return '[ ]'

```

[!] WARNING (line 145)
Line 145: Variable truthiness check detected (if is_completed:). Assume variable exists - let code fail fast if missing.

```python
    def render_progress_marker(self, is_completed: bool, is_current: bool) -> str:
        """Render markdown progress marker."""
        if is_completed:
            return '[X]'
        elif is_current:
            return '[>]'
        else:
            return '[ ]'

```

[!] WARNING (line 147)
Line 147: Variable truthiness check detected (if is_current:). Assume variable exists - let code fail fast if missing.

```python
        if is_completed:
            return '[X]'
        elif is_current:
            return '[>]'
        else:
            return '[ ]'

```

---

## avoid_excessive_guards
**cli_session.py** - 2 violation(s)

[!] WARNING (line 78)
Line 78: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

```python
        # Special case: "bot" switches to a different bot
        elif verb == 'bot':
            if not args:
                # No bot name provided - show current bot and available bots
                result = {
                    'status': 'info',
                    'current_bot': self.bot.bot_name,
                    'registered_bots': self.bot.bots,
                    'message': f"Current bot: {self.bot.bot_name}. Available bots: {', '.join(self.bot.bots)}. Usage: bot <name>"
                }
            else:
                # Switch to specified bot
                target_bot_name = args.strip()
                try:
                    self.bot.active_bot = target_bot_name
                    # Update self.bot to reference the new active bot
                    self.bot = self.bot.active_bot
                    result = {
                        'status': 'success',
                        'message': f'Switched to bot: {target_bot_name}',
                        'bot_name': target_bot_name
                    }
                except ValueError as e:
                    result = {
                        'status': 'error',
                        'message': str(e)
                    }
        # Special case: "save" calls bot.save() with parsed parameters
```

[!] WARNING (line 646)
Line 646: Variable truthiness check detected (if not line:). Assume variable exists - let code fail fast if missing.

```python
                try:
                    line = input(f"[{self.bot.name}] > ").strip()
                    if not line:
                        continue
                    
```

---

## avoid_excessive_guards
**markdown_instructions.py** - 1 violation(s)

[!] WARNING (line 177)
Line 177: Variable truthiness check detected (if strategy_criteria:). Assume variable exists - let code fail fast if missing.

```python
        # Get saved decisions (check both 'decisions' and 'decisions_made' keys)
        saved_decisions = {}
        if strategy_criteria:
            saved_decisions = strategy_criteria.get('decisions', {}) or strategy_criteria.get('decisions_made', {})
        
```

---

## avoid_excessive_guards
**tty_instructions.py** - 1 violation(s)

[!] WARNING (line 142)
Line 142: Variable truthiness check detected (if strategy_criteria:). Assume variable exists - let code fail fast if missing.

```python
        # Get saved decisions (check both 'decisions' and 'decisions_made' keys)
        saved_decisions = {}
        if strategy_criteria:
            saved_decisions = strategy_criteria.get('decisions', {}) or strategy_criteria.get('decisions_made', {})
        
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
**resource_oriented_code_scanner.py** - 1 violation(s)

[!] WARNING (line 67)
Line 67: Variable truthiness check detected (if is_agent:). Assume variable exists - let code fail fast if missing.

```python
                    # Check if class name is an agent noun using NLTK
                    is_agent, base_verb, suffix = VocabularyHelper.is_agent_noun(cls.node.name)
                    if is_agent:
                        loader_classes[cls.node.name] = (file_path, cls.node, suffix)
            except (SyntaxError, UnicodeDecodeError) as e:
```

---

## avoid_excessive_guards
**scope.py** - 7 violation(s)

[!] WARNING (line 97)
Line 97: Variable truthiness check detected (if matching_story_groups:). Assume variable exists - let code fail fast if missing.

```python
            if matching_story_groups or matching_direct_stories or filtered_nested_sub_epics:
                filtered_sub_epic = {**sub_epic}
                if matching_story_groups:
                    filtered_sub_epic['story_groups'] = matching_story_groups
                if matching_direct_stories:
```

[!] WARNING (line 101)
Line 101: Variable truthiness check detected (if filtered_nested_sub_epics:). Assume variable exists - let code fail fast if missing.

```python
                if matching_direct_stories:
                    filtered_sub_epic['stories'] = matching_direct_stories
                if filtered_nested_sub_epics:
                    filtered_sub_epic['sub_epics'] = filtered_nested_sub_epics
                return filtered_sub_epic
```

[!] WARNING (line 181)
Line 181: Variable truthiness check detected (if not matches_include:). Assume variable exists - let code fail fast if missing.

```python
                            break
                
                if not matches_include:
                    continue
            
```

[!] WARNING (line 199)
Line 199: Variable truthiness check detected (if matches_exclude:). Assume variable exists - let code fail fast if missing.

```python
                            break
                
                if matches_exclude:
                    continue
            
```

[!] WARNING (line 417)
Line 417: Variable truthiness check detected (if not data:). Assume variable exists - let code fail fast if missing.

```python
        scope = cls(workspace_directory, bot_paths)
        
        if not data:
            return scope
        
```

[!] WARNING (line 97)
Line 97: Variable truthiness check detected (if matching_story_groups:). Assume variable exists - let code fail fast if missing.

```python
            if matching_story_groups or matching_direct_stories or filtered_nested_sub_epics:
                filtered_sub_epic = {**sub_epic}
                if matching_story_groups:
                    filtered_sub_epic['story_groups'] = matching_story_groups
                if matching_direct_stories:
```

[!] WARNING (line 101)
Line 101: Variable truthiness check detected (if filtered_nested_sub_epics:). Assume variable exists - let code fail fast if missing.

```python
                if matching_direct_stories:
                    filtered_sub_epic['stories'] = matching_direct_stories
                if filtered_nested_sub_epics:
                    filtered_sub_epic['sub_epics'] = filtered_nested_sub_epics
                return filtered_sub_epic
```

---

## avoid_excessive_guards
**clarify_action.py** - 1 violation(s)

[!] WARNING (line 59)
Line 59: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    def do_execute(self, context: ClarifyActionContext = None):
        """Execute clarify action - get instructions and save if answers provided."""
        if context is None:
            context = ClarifyActionContext()
        result = self.get_instructions(context)
```

---

## avoid_excessive_guards
**strategy_action.py** - 1 violation(s)

[!] WARNING (line 192)
Line 192: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    def do_execute(self, context: StrategyActionContext = None):
        """Execute strategy action - get instructions and save if decisions provided."""
        if context is None:
            context = StrategyActionContext()
        result = self.get_instructions(context)
```

---

## avoid_excessive_guards
**file_link_builder.py** - 2 violation(s)

[!] WARNING (line 25)
Line 25: Variable truthiness check detected (if not is_absolute:). Assume variable exists - let code fail fast if missing.

```python
        file_path = Path(location)
        is_absolute = file_path.is_absolute() or (len(location) > 1 and location[1] == ':') or location.startswith('\\\\')
        if not is_absolute:
            return f'[`{location}`]({self.get_file_uri(location, line_number)})'
        if not self.workspace_directory:
```

[!] WARNING (line 48)
Line 48: Variable truthiness check detected (if line_number:). Assume variable exists - let code fail fast if missing.

```python
        except Exception as e:
            logger.debug(f'Failed to create fallback link for {location}: {e}')
            if line_number:
                return f'`{location}:{line_number}`'
            return f'`{location}`'
```

---

## avoid_excessive_guards
**cursor_command_visitor.py** - 3 violation(s)

[!] WARNING (line 37)
Line 37: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def formatter(self) -> CliTerminalFormatter:
        if self._formatter is None:
            self._formatter = CliTerminalFormatter()
        return self._formatter
```

[!] WARNING (line 43)
Line 43: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def description_extractor(self) -> DescriptionExtractor:
        if self._description_extractor is None:
            self._description_extractor = DescriptionExtractor(self.bot_name, self.bot_directory, self.formatter)
        return self._description_extractor
```

[!] WARNING (line 49)
Line 49: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

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

## avoid_unnecessary_parameter_passing
**render_action.py** - 2 violation(s)

[!] WARNING (line 49)
Instance property "self._render_specs" is extracted to variable "render_specs" and passed to internal method "_execute_synchronizers". Access via self._render_specs directly instead.

[!] WARNING (line 112)
Instance property "self._render_specs" is extracted to variable "render_specs" and passed to internal method "_execute_synchronizers". Access via self._render_specs directly instead.

---

## avoid_unnecessary_parameter_passing
**strategy_criteria.py** - 1 violation(s)

[!] WARNING (line 10)
Internal method "_format_options" receives parameter "options" that matches instance attribute. Consider accessing via self.options instead.

---

## chain_dependencies_properly
**bot.py** - 1 violation(s)

[!] WARNING (line 186)
Method "active_bot" in class "Bot" takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.

```python
    
    @active_bot.setter
    def active_bot(self, bot_name: str):
        """Switch to a different registered bot.
        
    # ... (truncated)
```

---

## chain_dependencies_properly
**prefer_object_model_over_config_scanner.py** - 1 violation(s)

[!] WARNING (line 36)
Method "scan_file" in class "PreferObjectModelOverConfigScanner" takes parameter "rule_obj" that is already injected in __init__. Use self.rule_obj instead.

```python
        ]
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, story_graph: Dict[str, Any] = None) -> List[Violation]:
        violations = []
        
    # ... (truncated)
```

---

## chain_dependencies_properly
**scope.py** - 1 violation(s)

[!] WARNING (line 481)
Method "apply_to_bot" in class "Scope" takes parameter "workspace_directory" that is already injected in __init__. Use self.workspace_directory instead.

```python
    
    # Legacy methods for backward compatibility
    def apply_to_bot(self, workspace_directory: Path = None):
        """Legacy method - save scope to state file."""
        self.save()
    # ... (truncated)
```

---

## delegate_to_lowest_level
**json_actions.py** - 1 violation(s)

[i] INFO (line 29)
Method "to_dict" in class "JSONActions" iterates through "_action_adapters" instead of delegating to collection class. Delegate to collection class instead.

---

## delegate_to_lowest_level
**json_behavior.py** - 1 violation(s)

[i] INFO (line 31)
Method "to_dict" in class "JSONBehaviors" iterates through "_behavior_adapters" instead of delegating to collection class. Delegate to collection class instead.

---

## delegate_to_lowest_level
**tty_behavior.py** - 1 violation(s)

[i] INFO (line 38)
Method "names" in class "TTYBehaviors" iterates through "behaviors" instead of delegating to collection class. Delegate to collection class instead.

---

## delegate_to_lowest_level
**base_hierarchical_adapter.py** - 3 violation(s)

[i] INFO (line 81)
Method "serialize" in class "BaseBehaviorsAdapter" iterates through "_behavior_adapters" instead of delegating to collection class. Delegate to collection class instead.

[i] INFO (line 134)
Method "_build_wrapped_hierarchy" in class "BaseActionsAdapter" iterates through "actions" instead of delegating to collection class. Delegate to collection class instead.

[i] INFO (line 146)
Method "serialize" in class "BaseActionsAdapter" iterates through "_action_adapters" instead of delegating to collection class. Delegate to collection class instead.

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
**cursor_command_visitor.py** - 1 violation(s)

[i] INFO (line 263)
Method "serialize" in class "CursorCommandGenerator" iterates through "_behavior_adapters" instead of delegating to collection class. Delegate to collection class instead.

---

## delegate_to_lowest_level
**scope.py** - 2 violation(s)

[i] INFO (line 32)
Method "_collect_blocks_from_files" in class "Scope" iterates through "files" instead of delegating to collection class. Delegate to collection class instead.

[i] INFO (line 38)
Method "_create_files_from_paths" in class "Scope" iterates through "_file_paths" instead of delegating to collection class. Delegate to collection class instead.

---

## detect_legacy_unused_code
**action.py** - 1 violation(s)

[!] WARNING (line 186)
Unused function '_merge_instructions' - consider removing dead code

---

## detect_legacy_unused_code
**action.py** - 1 violation(s)

[!] WARNING (line 186)
Unused function '_merge_instructions' - consider removing dead code

---

## detect_legacy_unused_code
**action.py** - 1 violation(s)

[!] WARNING (line 206)
Unused function '_inject_status_update_breadcrumbs' - consider removing dead code

---

## detect_legacy_unused_code
**action.py** - 1 violation(s)

[!] WARNING (line 206)
Unused function '_inject_status_update_breadcrumbs' - consider removing dead code

---

## detect_legacy_unused_code
**actions.py** - 1 violation(s)

[!] WARNING (line 221)
Unused function '_get_next_action_reminder' - consider removing dead code

---

## detect_legacy_unused_code
**actions.py** - 1 violation(s)

[!] WARNING (line 221)
Unused function '_get_next_action_reminder' - consider removing dead code

---

## detect_legacy_unused_code
**actions.py** - 1 violation(s)

[!] WARNING (line 273)
Unused function '_save_completed_action' - consider removing dead code

---

## detect_legacy_unused_code
**actions.py** - 1 violation(s)

[!] WARNING (line 273)
Unused function '_save_completed_action' - consider removing dead code

---

## detect_legacy_unused_code
**behaviors.py** - 1 violation(s)

[!] WARNING (line 251)
Unused function '_inject_next_behavior_reminder' - consider removing dead code

---

## detect_legacy_unused_code
**behaviors.py** - 1 violation(s)

[!] WARNING (line 259)
Unused function '_inject_next_behavior_reminder' - consider removing dead code

---

## detect_legacy_unused_code
**rule.py** - 1 violation(s)

[!] WARNING (line 219)
Unused function '_format_examples' - consider removing dead code

---

## detect_legacy_unused_code
**rule.py** - 1 violation(s)

[!] WARNING (line 219)
Unused function '_format_examples' - consider removing dead code

---

## detect_legacy_unused_code
**code_scanner.py** - 1 violation(s)

[!] WARNING (line 217)
Unused function '_get_all_code_files_parsed' - consider removing dead code

---

## detect_legacy_unused_code
**code_scanner.py** - 1 violation(s)

[!] WARNING (line 217)
Unused function '_get_all_code_files_parsed' - consider removing dead code

---

## detect_legacy_unused_code
**domain_language_scanner.py** - 1 violation(s)

[!] WARNING (line 81)
Unused function '_is_generic_usage' - consider removing dead code

---

## detect_legacy_unused_code
**domain_language_scanner.py** - 1 violation(s)

[!] WARNING (line 81)
Unused function '_is_generic_usage' - consider removing dead code

---

## detect_legacy_unused_code
**duplication_scanner.py** - 1 violation(s)

[!] WARNING (line 1400)
Unused function '_get_ast_signature' - consider removing dead code

---

## detect_legacy_unused_code
**duplication_scanner.py** - 1 violation(s)

[!] WARNING (line 1400)
Unused function '_get_ast_signature' - consider removing dead code

---

## detect_legacy_unused_code
**given_when_then_helpers_scanner.py** - 1 violation(s)

[!] WARNING (line 82)
Unused function '_get_helper_calls_in_file' - consider removing dead code

---

## detect_legacy_unused_code
**given_when_then_helpers_scanner.py** - 1 violation(s)

[!] WARNING (line 82)
Unused function '_get_helper_calls_in_file' - consider removing dead code

---

## detect_legacy_unused_code
**intention_revealing_names_scanner.py** - 1 violation(s)

[!] WARNING (line 280)
Unused function '_is_in_small_loop' - consider removing dead code

---

## detect_legacy_unused_code
**intention_revealing_names_scanner.py** - 1 violation(s)

[!] WARNING (line 280)
Unused function '_is_in_small_loop' - consider removing dead code

---

## detect_legacy_unused_code
**scanner_registry.py** - 1 violation(s)

[!] WARNING (line 65)
Unused function 'registers_helper' - consider removing dead code

---

## detect_legacy_unused_code
**scanner_registry.py** - 1 violation(s)

[!] WARNING (line 65)
Unused function 'registers_helper' - consider removing dead code

---

## detect_legacy_unused_code
**single_responsibility_scanner.py** - 1 violation(s)

[!] WARNING (line 132)
Unused function '_check_class_sr' - consider removing dead code

---

## detect_legacy_unused_code
**single_responsibility_scanner.py** - 1 violation(s)

[!] WARNING (line 132)
Unused function '_check_class_sr' - consider removing dead code

---

## detect_legacy_unused_code
**single_responsibility_scanner.py** - 1 violation(s)

[!] WARNING (line 173)
Unused function '_format_responsibility_examples' - consider removing dead code

---

## detect_legacy_unused_code
**single_responsibility_scanner.py** - 1 violation(s)

[!] WARNING (line 173)
Unused function '_format_responsibility_examples' - consider removing dead code

---

## detect_legacy_unused_code
**single_responsibility_scanner.py** - 1 violation(s)

[!] WARNING (line 183)
Unused function '_format_class_responsibility_examples' - consider removing dead code

---

## detect_legacy_unused_code
**single_responsibility_scanner.py** - 1 violation(s)

[!] WARNING (line 183)
Unused function '_format_class_responsibility_examples' - consider removing dead code

---

## detect_legacy_unused_code
**build_action.py** - 1 violation(s)

[!] WARNING (line 245)
Unused function '_convert_path_to_reference' - consider removing dead code

---

## detect_legacy_unused_code
**build_action.py** - 1 violation(s)

[!] WARNING (line 245)
Unused function '_convert_path_to_reference' - consider removing dead code

---

## detect_legacy_unused_code
**validation_report_writer.py** - 1 violation(s)

[!] WARNING (line 275)
Unused function '_build_report_lines' - consider removing dead code

---

## detect_legacy_unused_code
**validation_report_writer.py** - 1 violation(s)

[!] WARNING (line 275)
Unused function '_build_report_lines' - consider removing dead code

---

## detect_legacy_unused_code
**validation_scope.py** - 1 violation(s)

[!] WARNING (line 50)
Unused function '_should_include_file' - consider removing dead code

---

## detect_legacy_unused_code
**validation_scope.py** - 1 violation(s)

[!] WARNING (line 50)
Unused function '_should_include_file' - consider removing dead code

---

## detect_legacy_unused_code
**cursor_command_visitor.py** - 1 violation(s)

[!] WARNING (line 85)
Unused function '_get_cli_command' - consider removing dead code

---

## detect_legacy_unused_code
**cursor_command_visitor.py** - 1 violation(s)

[!] WARNING (line 85)
Unused function '_get_cli_command' - consider removing dead code

---

## detect_legacy_unused_code
**cursor_command_visitor.py** - 1 violation(s)

[!] WARNING (line 91)
Unused function '_get_current_command_files' - consider removing dead code

---

## detect_legacy_unused_code
**cursor_command_visitor.py** - 1 violation(s)

[!] WARNING (line 91)
Unused function '_get_current_command_files' - consider removing dead code

---

## detect_legacy_unused_code
**cursor_command_visitor.py** - 1 violation(s)

[!] WARNING (line 205)
Unused function '_build_action_command' - consider removing dead code

---

## detect_legacy_unused_code
**cursor_command_visitor.py** - 1 violation(s)

[!] WARNING (line 205)
Unused function '_build_action_command' - consider removing dead code

---

## eliminate_duplication
**utils.py** - 1 violation(s)

[X] ERROR (line 290)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (find_test_class_line:290-304):
```python
content = test_file_path.read_text(encoding='utf-8')
tree = ast.parse(content, filename=str(test_file_path))
for node in ast.walk(tree):
    if isinstance(node, ast.ClassDef) and node.name == test_cla...
```

Location (find_test_method_line:321-335):
```python
content = test_file_path.read_text(encoding='utf-8')
tree = ast.parse(content, filename=str(test_file_path))
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef) and node.name == test_...
```

---

## eliminate_duplication
**markdown_behavior.py** - 1 violation(s)

[X] ERROR (line 28)
Duplicate code detected: functions parse_command_text, parse_command_text have identical bodies - extract to shared function

---

## eliminate_duplication
**tty_behavior.py** - 1 violation(s)

[X] ERROR (line 56)
Duplicate code detected: functions parse_command_text, parse_command_text have identical bodies - extract to shared function

---

## eliminate_duplication
**bot.py** - 2 violation(s)

[X] ERROR (line 321)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (scope:321-331):
```python
is_clear = True
self._scope.clear()
self._scope.save()
from ..scope.scope_command_result import ScopeCommandResult
return ScopeCommandResult(status='success', message='Scope cleared', scope=self._scop...
```

Location (scope:333-342):
```python
self._scope.clear()
self._scope.save()
from ..scope.scope_command_result import ScopeCommandResult
return ScopeCommandResult(status='success', message='Scope cleared (set to all)', scope=self._scope)
```

[X] ERROR (line 518)
Duplicate code blocks detected (3 locations) - extract to helper function.

Location (next:518-532):
```python
first_action = behavior.action_names[0]
behavior.actions.navigate_to(first_action)
self.behaviors.save_state()
return {'status': 'success', 'message': f'Moved to {behavior.name}.{first_action}', 'beha...
```

Location (next:538-551):
```python
next_action = action_names[current_index + 1]
behavior.actions.navigate_to(next_action)
self.behaviors.save_state()
return {'status': 'success', 'message': f'Moved to {behavior.name}.{next_action}', '...
```

Location (back:583-599):
```python
prev_action = action_names[current_index - 1]
behavior.actions.navigate_to(prev_action)
self.behaviors.save_state()
return {'status': 'success', 'message': f'Moved back to {behavior.name}.{prev_action...
```

---

## eliminate_duplication
**markdown_bot.py** - 3 violation(s)

[X] ERROR (line 47)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (progress:47-51):
```python
lines = []
lines.append(MarkdownAdapter.format_header(self, 2, '🗺️ Progress'))
lines.append('')
lines.append(f'**Current Position:** {self.bot.progress_path}')
lines.append('')
```

Location (commands:62-66):
```python
lines = []
lines.append(MarkdownAdapter.format_header(self, 2, '💻 Commands'))
lines.append('')
lines.append('**status | back | current | next | path [dir] | scope [filter] | bot [name] | help | exit**...
```

[X] ERROR (line 62)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (commands:62-71):
```python
lines = []
lines.append(MarkdownAdapter.format_header(self, 2, '💻 Commands'))
lines.append('')
lines.append('**status | back | current | next | path [dir] | scope [filter] | bot [name] | help | exit**...
```

Location (format_header:111-120):
```python
header_text = MarkdownAdapter.format_header(self, 2, 'CLI STATUS section')
lines.append(header_text)
lines.append('')
lines.append('This section contains current scope filter (if set), current progres...
```

[X] ERROR (line 77)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (behavior_action_summary:77-91):
```python
lines = []
behavior_names = []
for behavior in self.bot.behaviors:
    name = behavior.name
    if name == (self.bot.behaviors.current.name if self.bot.behaviors.current else None):
        behavior_n...
```

Location (behavior_action_summary:96-101):
```python
name = action.action_name
if name == current_action_name:
    action_names.append(f'**{name}**')
else:
    action_names.append(name)
```

---

## eliminate_duplication
**tty_bot.py** - 2 violation(s)

[X] ERROR (line 91)
Duplicate code blocks detected (3 locations) - extract to helper function.

Location (header:91-96):
```python
lines.append(centered_text)
lines.append('This section contains current scope filter (if set), current progress in workflow, and available commands')
lines.append('Review the CLI STATUS section below ...
```

Location (run_instructions:106-111):
```python
lines.append(self.add_bold('Args:'))
lines.append('--scope "Epic, Sub Epic, Story"      # Filter by story names')
lines.append('--scope "file:path/one,path/two"     # Filter by file paths')
lines.appe...
```

Location (commands:120-125):
```python
lines.append('// Run')
lines.append("echo '[command]' | python repl_main.py")
lines.append('// to invoke commands')
lines.append('')
lines.append(self.section_separator())
return '\n'.join(lines)
```

[X] ERROR (line 103)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (run_instructions:103-111):
```python
lines.append("echo 'behavior.action' | python repl_main.py           # Defaults to 'instructions' operation")
lines.append("echo 'behavior.action.operation' | python repl_main.py  # Runs operation")
l...
```

Location (commands:117-125):
```python
lines.append(self.add_bold('💻 Commands:'))
lines.append(self.add_bold('status | back | current | next | path [dir] | scope [filter] | bot [name] | help | exit'))
lines.append('')
lines.append('// Run'...
```

---

## eliminate_duplication
**adapters.py** - 1 violation(s)

[X] ERROR (line 64)
Duplicate code detected: functions parse_command_text, parse_command_text, parse_command_text, parse_command_text have identical bodies - extract to shared function

---

## eliminate_duplication
**base_hierarchical_adapter.py** - 1 violation(s)

[X] ERROR (line 14)
Duplicate code detected: functions _build_wrapped_hierarchy, serialize, format_header, format_bot_info, format_footer, format_behavior_name have identical bodies - extract to shared function

---

## eliminate_duplication
**visitor.py** - 1 violation(s)

[X] ERROR (line 28)
Duplicate code detected: functions visit_header, visit_behavior, visit_action, visit_action_help_section_header, visit_footer have identical bodies - extract to shared function

---

## eliminate_duplication
**markdown_help.py** - 1 violation(s)

[X] ERROR (line 29)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (serialize:29-48):
```python
lines.append('    actions:')
for action_name, description in self.help_obj.components.actions:
    lines.append(f'      {action_name:<12} - {description}')
lines.append('')
lines.append('    operation...
```

Location (serialize:51-58):
```python
lines.append('')
lines.append('  Scope Command Details:')
for rule in self.help_obj.scope.important_rules:
    lines.append(f'    {rule}')
lines.append('')
lines.append('    Usage (pick ONE - each rep...
```

---

## eliminate_duplication
**tty_help.py** - 1 violation(s)

[X] ERROR (line 35)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (serialize:35-54):
```python
lines.append('    actions:')
for action_name, description in self.help_obj.components.actions:
    lines.append(f'      {action_name:<12} - {description}')
lines.append('')
lines.append('    operation...
```

Location (serialize:57-64):
```python
lines.append('')
lines.append('  Scope Command Details:')
for rule in self.help_obj.scope.important_rules:
    lines.append(f'    {rule}')
lines.append('')
lines.append('    Usage (pick ONE - each rep...
```

---

