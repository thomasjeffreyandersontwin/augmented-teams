# Validation Status - code
Started: 2026-01-16 00:35:14
Files: 287

## avoid_excessive_guards
**action.py** - 2 violation(s)

[!] WARNING (line 304)
Line 304: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    def execute(self, context: ActionContext = None) -> Dict[str, Any]:
        self.track_activity_on_start()
        if context is None:
            context = self.context_class()
        try:
```

[!] WARNING (line 393)
Line 393: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

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
**vocabulary_helper.py** - 1 violation(s)

[!] WARNING (line 190)
Line 190: Variable truthiness check detected (if not synsets:). Assume variable exists - let code fail fast if missing.

```python
            synsets = wn.synsets(word_lower)
            
            if not synsets:
                return False
            
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

[i] INFO (line 207)
Method "serialize" in class "CursorCommandGenerator" iterates through "_behavior_adapters" instead of delegating to collection class. Delegate to collection class instead.

---

## delegate_to_lowest_level
**scope.py** - 2 violation(s)

[i] INFO (line 32)
Method "_collect_blocks_from_files" in class "Scope" iterates through "files" instead of delegating to collection class. Delegate to collection class instead.

[i] INFO (line 38)
Method "_create_files_from_paths" in class "Scope" iterates through "_file_paths" instead of delegating to collection class. Delegate to collection class instead.

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
**tty_bot (1).py** - 2 violation(s)

[X] ERROR (line 82)
Duplicate code blocks detected (3 locations) - extract to helper function.

Location (header:82-87):
```python
lines.append(centered_text)
lines.append('This section contains current scope filter (if set), current progress in workflow, and available commands')
lines.append('Review the CLI STATUS section below ...
```

Location (run_instructions:97-102):
```python
lines.append(self.add_bold('Args:'))
lines.append('--scope "Epic, Sub Epic, Story"      # Filter by story names')
lines.append('--scope "file:path/one,path/two"     # Filter by file paths')
lines.appe...
```

Location (commands:111-116):
```python
lines.append('// Run')
lines.append("echo '[command]' | python repl_main.py")
lines.append('// to invoke commands')
lines.append('')
lines.append(self.section_separator())
return '\n'.join(lines)
```

[X] ERROR (line 94)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (run_instructions:94-102):
```python
lines.append("echo 'behavior.action' | python repl_main.py           # Defaults to 'instructions' operation")
lines.append("echo 'behavior.action.operation' | python repl_main.py  # Runs operation")
l...
```

Location (commands:108-116):
```python
lines.append(self.add_bold('💻 Commands:'))
lines.append(self.add_bold('status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit'))
lines.append('')
lines.append('// ...
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

## eliminate_duplication
**rules.py** - 1 violation(s)

[X] ERROR (line 96)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_get_files_for_validation:96-102):
```python
filtered_files = {}
for key, file_list in files_dict.items():
    filtered = context.scope.filters_files(file_list)
    if filtered:
        filtered_files[key] = filtered
return filtered_files
```

Location (_get_files_for_validation:122-128):
```python
filtered_files = {}
for key, file_list in all_files.items():
    filtered = context.scope.filters_files(file_list)
    if filtered:
        filtered_files[key] = filtered
return filtered_files
```

---

## eliminate_duplication
**rules_action.py** - 1 violation(s)

[X] ERROR (line 17)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_prepare_instructions:17-23):
```python
rules = Rules(behavior=self.behavior, bot_paths=self.behavior.bot_paths)
rules_digest = rules.formatted_rules_digest()
rule_names = self._get_rule_names(rules)
self._add_rules_list_to_display(instruct...
```

Location (do_execute:27-33):
```python
rules = Rules(behavior=self.behavior, bot_paths=self.behavior.bot_paths)
rules_digest = rules.formatted_rules_digest()
rule_names = self._get_rule_names(rules)
self._add_rules_list_to_display(instruct...
```

---

## eliminate_duplication
**vocabulary_helper.py** - 1 violation(s)

[X] ERROR (line 56)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (is_verb:56-61):
```python
word_lower = word.lower()
synsets = wn.synsets(word_lower, pos=wn.VERB)
return len(synsets) > 0
```

Location (is_noun:66-71):
```python
word_lower = word.lower()
synsets = wn.synsets(word_lower, pos=wn.NOUN)
return len(synsets) > 0
```

---

## eliminate_duplication
**scope.py** - 1 violation(s)

[X] ERROR (line 168)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (filter_files:168-179):
```python
pattern_normalized = pattern.replace('\\', '/')
try:
    if file_path_obj.match(pattern_normalized) or file_path_obj.match(f'**/{pattern_normalized}') or pattern_normalized in file_str:
        matche...
```

Location (filter_files:186-197):
```python
pattern_normalized = pattern.replace('\\', '/')
try:
    if file_path_obj.match(pattern_normalized) or file_path_obj.match(f'**/{pattern_normalized}') or pattern_normalized in file_str:
        matche...
```

---

## eliminate_duplication
**render_action.py** - 1 violation(s)

[X] ERROR (line 45)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_prepare_instructions:45-56):
```python
render_instructions = self._config_loader.load_render_instructions()
render_specs = self._render_specs
self._execute_synchronizers(render_specs)
merged_data = {'base_instructions': instructions.get('b...
```

Location (do_execute:110-122):
```python
render_instructions = self._config_loader.load_render_instructions()
render_specs = self._render_specs
self._execute_synchronizers(render_specs)
instructions = self.get_instructions(context)
merged_da...
```

---


## Cross-File Duplication Analysis
Scanning 287 changed file(s) against 20 total files...
Extracted 4304 changed blocks, 513 reference blocks
Starting 2,207,952 pairwise comparisons...
Comparing: 0% (20,162/2,207,952) - 0 violations - ETA: 1085s  
Comparing: 1% (36,197/2,207,952) - 0 violations - ETA: 1199s  
Comparing: 2% (59,690/2,207,952) - 0 violations - ETA: 1079s  
Comparing: 3% (71,550/2,207,952) - 0 violations - ETA: 1194s  
Comparing: 3% (82,272/2,207,952) - 0 violations - ETA: 1291s  
Comparing: 4% (90,628/2,207,952) - 0 violations - ETA: 1401s  
Comparing: 4% (98,057/2,207,952) - 0 violations - ETA: 1506s  
Comparing: 5% (110,684/2,207,952) - 0 violations - ETA: 1516s  
Comparing: 5% (121,667/2,207,952) - 0 violations - ETA: 1543s  
Found 10 violations so far...
Found 20 violations so far...
Found 30 violations so far...
Found 40 violations so far...
Found 50 violations so far...
Found 60 violations so far...
Found 70 violations so far...
Comparing: 6% (138,952/2,207,952) - 71 violations - ETA: 1489s  
Found 80 violations so far...
Found 90 violations so far...
Found 100 violations so far...
Found 110 violations so far...
Found 120 violations so far...
Found 130 violations so far...
Found 140 violations so far...
Found 150 violations so far...
Found 160 violations so far...
Found 170 violations so far...
Comparing: 7% (157,924/2,207,952) - 172 violations - ETA: 1428s  
Found 180 violations so far...
Comparing: 8% (181,461/2,207,952) - 180 violations - ETA: 1340s  
Found 190 violations so far...
Found 200 violations so far...
Found 210 violations so far...
Comparing: 9% (203,794/2,207,952) - 217 violations - ETA: 1278s  
Found 220 violations so far...
Found 230 violations so far...
Found 240 violations so far...
Found 250 violations so far...
Found 260 violations so far...
Found 270 violations so far...
Found 280 violations so far...
Found 290 violations so far...
Comparing: 10% (227,177/2,207,952) - 295 violations - ETA: 1220s  
Found 300 violations so far...
Found 310 violations so far...
Found 320 violations so far...
Found 330 violations so far...
Found 340 violations so far...
Comparing: 11% (251,353/2,207,952) - 347 violations - ETA: 1167s  
Comparing: 12% (283,293/2,207,952) - 347 violations - ETA: 1087s  
Comparing: 14% (309,788/2,207,952) - 347 violations - ETA: 1041s  
Comparing: 15% (335,148/2,207,952) - 347 violations - ETA: 1005s  
Comparing: 16% (360,520/2,207,952) - 347 violations - ETA: 973s  
Comparing: 17% (387,219/2,207,952) - 347 violations - ETA: 940s  
Comparing: 18% (410,163/2,207,952) - 347 violations - ETA: 920s  
Comparing: 20% (441,670/2,207,952) - 347 violations - ETA: 879s  
Comparing: 21% (473,774/2,207,952) - 347 violations - ETA: 841s  
Comparing: 22% (500,999/2,207,952) - 347 violations - ETA: 817s  
Comparing: 23% (523,254/2,207,952) - 347 violations - ETA: 804s  
Comparing: 25% (554,405/2,207,952) - 347 violations - ETA: 775s  
Comparing: 26% (575,506/2,207,952) - 347 violations - ETA: 765s  
Comparing: 27% (598,989/2,207,952) - 347 violations - ETA: 752s  
Comparing: 28% (619,247/2,207,952) - 347 violations - ETA: 744s  
Comparing: 28% (636,556/2,207,952) - 347 violations - ETA: 740s  
Comparing: 29% (653,064/2,207,952) - 347 violations - ETA: 738s  
Comparing: 30% (679,287/2,207,952) - 347 violations - ETA: 720s  
Comparing: 31% (700,763/2,207,952) - 347 violations - ETA: 709s  
Comparing: 32% (717,969/2,207,952) - 347 violations - ETA: 705s  
Comparing: 33% (737,115/2,207,952) - 347 violations - ETA: 698s  
Comparing: 34% (767,934/2,207,952) - 349 violations - ETA: 675s  
Comparing: 35% (794,605/2,207,952) - 349 violations - ETA: 658s  
Comparing: 37% (817,073/2,207,952) - 349 violations - ETA: 646s  
Comparing: 37% (837,306/2,207,952) - 349 violations - ETA: 638s  
Comparing: 38% (856,670/2,207,952) - 349 violations - ETA: 630s  
Comparing: 39% (882,455/2,207,952) - 349 violations - ETA: 615s  
Comparing: 41% (911,727/2,207,952) - 349 violations - ETA: 597s  
Comparing: 42% (930,264/2,207,952) - 349 violations - ETA: 590s  
Comparing: 43% (957,419/2,207,952) - 349 violations - ETA: 574s  
Comparing: 44% (984,963/2,207,952) - 349 violations - ETA: 558s  
Comparing: 45% (1,014,137/2,207,952) - 349 violations - ETA: 541s  
Comparing: 47% (1,041,810/2,207,952) - 349 violations - ETA: 526s  
Comparing: 48% (1,071,827/2,207,952) - 349 violations - ETA: 508s  
Comparing: 49% (1,102,477/2,207,952) - 349 violations - ETA: 491s  
Comparing: 51% (1,134,656/2,207,952) - 349 violations - ETA: 472s  
Comparing: 52% (1,163,335/2,207,952) - 349 violations - ETA: 457s  
Comparing: 53% (1,187,112/2,207,952) - 349 violations - ETA: 447s  
Comparing: 55% (1,217,539/2,207,952) - 349 violations - ETA: 431s  
Comparing: 56% (1,243,145/2,207,952) - 349 violations - ETA: 419s  
Comparing: 57% (1,274,773/2,207,952) - 349 violations - ETA: 402s  
Comparing: 58% (1,302,414/2,207,952) - 349 violations - ETA: 389s  
Comparing: 60% (1,331,450/2,207,952) - 349 violations - ETA: 375s  
Comparing: 61% (1,362,141/2,207,952) - 349 violations - ETA: 360s  
Comparing: 62% (1,385,962/2,207,952) - 349 violations - ETA: 349s  
Comparing: 63% (1,412,249/2,207,952) - 349 violations - ETA: 338s  
Comparing: 65% (1,443,378/2,207,952) - 349 violations - ETA: 323s  
Comparing: 66% (1,466,606/2,207,952) - 349 violations - ETA: 313s  
Comparing: 67% (1,494,254/2,207,952) - 349 violations - ETA: 300s  
Comparing: 69% (1,524,496/2,207,952) - 349 violations - ETA: 286s  
Comparing: 70% (1,551,385/2,207,952) - 349 violations - ETA: 275s  
Comparing: 71% (1,574,263/2,207,952) - 349 violations - ETA: 265s  
Comparing: 72% (1,591,768/2,207,952) - 349 violations - ETA: 259s  
Comparing: 72% (1,609,974/2,207,952) - 349 violations - ETA: 252s  
Comparing: 73% (1,633,696/2,207,952) - 349 violations - ETA: 242s  
Comparing: 74% (1,654,925/2,207,952) - 349 violations - ETA: 233s  
Comparing: 76% (1,682,824/2,207,952) - 349 violations - ETA: 221s  
Comparing: 77% (1,712,503/2,207,952) - 349 violations - ETA: 208s  
Comparing: 78% (1,742,057/2,207,952) - 349 violations - ETA: 195s  
Comparing: 80% (1,767,171/2,207,952) - 349 violations - ETA: 184s  
Comparing: 80% (1,786,245/2,207,952) - 349 violations - ETA: 177s  
Comparing: 82% (1,810,706/2,207,952) - 349 violations - ETA: 166s  
Comparing: 83% (1,834,210/2,207,952) - 349 violations - ETA: 156s  
Comparing: 83% (1,852,710/2,207,952) - 349 violations - ETA: 149s  
Comparing: 84% (1,871,904/2,207,952) - 349 violations - ETA: 141s  
Comparing: 85% (1,893,461/2,207,952) - 349 violations - ETA: 132s  
Comparing: 86% (1,916,102/2,207,952) - 349 violations - ETA: 123s  
Comparing: 87% (1,938,364/2,207,952) - 349 violations - ETA: 114s  
Comparing: 88% (1,960,842/2,207,952) - 349 violations - ETA: 104s  
Comparing: 89% (1,986,213/2,207,952) - 349 violations - ETA: 93s  
Comparing: 90% (2,006,585/2,207,952) - 349 violations - ETA: 85s  
Comparing: 91% (2,023,205/2,207,952) - 349 violations - ETA: 78s  
Comparing: 92% (2,048,502/2,207,952) - 349 violations - ETA: 67s  
Comparing: 94% (2,076,173/2,207,952) - 349 violations - ETA: 55s  
Comparing: 94% (2,092,435/2,207,952) - 349 violations - ETA: 49s  
Comparing: 95% (2,114,549/2,207,952) - 349 violations - ETA: 39s  
Comparing: 96% (2,127,883/2,207,952) - 349 violations - ETA: 34s  
Complete: 2139895 comparisons, 349 violations

## enforce_encapsulation
**bot_paths.py** - 1 violation(s)

[!] WARNING (line 63)
Method "update_workspace_directory" in class "BotPaths" has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

---

## enforce_encapsulation
**bot_path.py** - 1 violation(s)

[!] WARNING (line 102)
Method "update_workspace_directory" in class "BotPath" has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

---

## enforce_encapsulation
**cli_session.py** - 1 violation(s)

[!] WARNING (line 65)
Method "execute_command" in class "CLISession" has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

---

## enforce_encapsulation
**ac_consolidation_scanner.py** - 1 violation(s)

[!] WARNING (line 29)
Method "_check_duplicate_ac" in class "ACConsolidationScanner" has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

---

## enforce_encapsulation
**real_implementations_scanner.py** - 1 violation(s)

[!] WARNING (line 174)
Method "_find_src_locations" in class "RealImplementationsScanner" has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

---

## enforce_encapsulation
**scanner_loader.py** - 1 violation(s)

[!] WARNING (line 29)
Method "_load_scanner_class" in class "ScannerLoader" has Law of Demeter violation (method chain depth 4) - encapsulate access to related objects

---

## enforce_encapsulation
**scanner_registry.py** - 1 violation(s)

[!] WARNING (line 39)
Method "loads_scanner_class_with_error" in class "ScannerRegistry" has Law of Demeter violation (method chain depth 4) - encapsulate access to related objects

---

## enforce_encapsulation
**strategy_action.py** - 1 violation(s)

[!] WARNING (line 106)
Method "_format_instructions_for_display" in class "StrategyAction" has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

---

## enforce_encapsulation
**validate_action.py** - 1 violation(s)

[!] WARNING (line 184)
Method "_format_rules_with_file_paths" in class "ValidateRulesAction" has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

---

## hide_business_logic_behind_properties
**complexity_metrics.py** - 1 violation(s)

[!] WARNING (line 204)
Function "calculate_lcom" exposes calculation timing. Use property with "get_" or no prefix instead (e.g., "total_value" not "calculate_total_value").

```python
    
    @staticmethod
    def calculate_lcom(class_node: ast.ClassDef) -> float:
    # ... (truncated)
```

---

## hide_business_logic_behind_properties
**block.py** - 1 violation(s)

[!] WARNING (line 72)
Function "calculate_complexity" exposes calculation timing. Use property with "get_" or no prefix instead (e.g., "total_value" not "calculate_total_value").

```python
        return self._code_structure_analyzer.analyzes_code_structure(self)
    
    def calculate_complexity(self, complexity_metrics) -> dict:
    # ... (truncated)
```

---

## hide_calculation_timing
**complexity_metrics.py** - 1 violation(s)

[!] WARNING (line 204)
Function "calculate_lcom" exposes calculation timing. Use property with "get_" or no prefix instead (e.g., "total_value" not "calculate_total_value").

```python
    
    @staticmethod
    def calculate_lcom(class_node: ast.ClassDef) -> float:
    # ... (truncated)
```

---

## hide_calculation_timing
**block.py** - 1 violation(s)

[!] WARNING (line 72)
Function "calculate_complexity" exposes calculation timing. Use property with "get_" or no prefix instead (e.g., "total_value" not "calculate_total_value").

```python
        return self._code_structure_analyzer.analyzes_code_structure(self)
    
    def calculate_complexity(self, complexity_metrics) -> dict:
    # ... (truncated)
```

---

## keep_classes_small_with_single_responsibility
**action.py** - 1 violation(s)

[!] WARNING (line 23)
Class "Action" is 766 lines - should be under 300 lines (extract related methods into separate classes)

```python
logger = logging.getLogger(__name__)

class Action:
    # Class attribute: the context class this action expects
    # Subclasses override this to declare their typed context
    context_class: Type[ActionContext] = ActionContext

    def __init__(self, behavior: 'Behavior', action_config: Dict[str, Any]=None, action_name: str=None):
        self.behavior = behavior
        self.action_config = action_config
    # ... (truncated)
```

---

## keep_classes_small_with_single_responsibility
**behaviors.py** - 1 violation(s)

[!] WARNING (line 16)
Class "Behaviors" is 329 lines - should be under 300 lines (extract related methods into separate classes)

```python
logger = logging.getLogger(__name__)

class Behaviors:

    def __init__(self, bot_name: str, bot_paths: BotPath, allowed_behaviors: Optional[List[str]] = None):
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_path.parent.mkdir(parents=True, exist_ok=True); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'behaviors.py:18','message':'Behaviors.__init__ entry','data':{'bot_name':bot_name},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1'})+'\n'); log_file.close()
        # #endregion
        self.bot_name = bot_name
        self.bot_paths = bot_paths
    # ... (truncated)
```

---

## keep_classes_small_with_single_responsibility
**behaviors.py** - 1 violation(s)

[!] WARNING (line 16)
Class "Behaviors" is 315 lines - should be under 300 lines (extract related methods into separate classes)

```python
logger = logging.getLogger(__name__)

class Behaviors:

    def __init__(self, bot_name: str, bot_paths: BotPath, allowed_behaviors: Optional[List[str]] = None):
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_path.parent.mkdir(parents=True, exist_ok=True); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'behaviors.py:18','message':'Behaviors.__init__ entry','data':{'bot_name':bot_name},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1'})+'\n'); log_file.close()
        # #endregion
        self.bot_name = bot_name
        self.bot_paths = bot_paths
    # ... (truncated)
```

---

## keep_classes_small_with_single_responsibility
**bot.py** - 1 violation(s)

[!] WARNING (line 25)
Class "Bot" is 974 lines - should be under 300 lines (extract related methods into separate classes)

```python
        self.executed_instructions_from = f'{behavior}/{action}'

class Bot:
    # Class-level registry for bot switching
    _active_bot_instance: Optional['Bot'] = None
    _active_bot_name: Optional[str] = None

    def __init__(self, bot_name: str, bot_directory: Path, config_path: Path):
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_path.parent.mkdir(parents=True, exist_ok=True); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'bot.py:24','message':'Bot.__init__ entry','data':{'bot_name':bot_name,'bot_directory_param':str(bot_directory),'bot_directory_name':bot_directory.name if bot_directory else None},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1'})+'\n'); log_file.close()
    # ... (truncated)
```

---

## keep_classes_small_with_single_responsibility
**cli_session.py** - 1 violation(s)

[!] WARNING (line 14)
Class "CLISession" is 653 lines - should be under 300 lines (extract related methods into separate classes)

```python


class CLISession:
    """
    Minimal command router - parses commands, routes to Bot, uses adapter for serialization.
    
    Architecture:
    - Parse command -> Route to Bot method -> Get domain object -> Adapter serializes -> Output
    """
    
    # ... (truncated)
```

---

## keep_classes_small_with_single_responsibility
**bad_comments_scanner.py** - 1 violation(s)

[!] WARNING (line 13)
Class "BadCommentsScanner" is 303 lines - should be under 300 lines (extract related methods into separate classes)

```python


class BadCommentsScanner(CodeScanner):
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, story_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
    # ... (truncated)
```

---

## keep_classes_small_with_single_responsibility
**business_readable_test_names_scanner.py** - 1 violation(s)

[!] WARNING (line 15)
Class "BusinessReadableTestNamesScanner" is 324 lines - should be under 300 lines (extract related methods into separate classes)

```python


class BusinessReadableTestNamesScanner(TestScanner):
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, story_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
    # ... (truncated)
```

---

## keep_classes_small_with_single_responsibility
**class_based_organization_scanner.py** - 1 violation(s)

[!] WARNING (line 12)
Class "ClassBasedOrganizationScanner" is 513 lines - should be under 300 lines (extract related methods into separate classes)

```python


class ClassBasedOrganizationScanner(TestScanner):
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        return []  # Test scanning happens in scan_test_file, not scan_story_node
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, story_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
    # ... (truncated)
```

---

## keep_classes_small_with_single_responsibility
**complexity_metrics.py** - 1 violation(s)

[!] WARNING (line 7)
Class "ComplexityMetrics" is 358 lines - should be under 300 lines (extract related methods into separate classes)

```python


class ComplexityMetrics:
    
    @staticmethod
    def cyclomatic_complexity(func_node: ast.FunctionDef) -> int:
        complexity = 1  # Base complexity
        
        for node in ast.walk(func_node):
            # Decision points
    # ... (truncated)
```

---

## keep_classes_small_with_single_responsibility
**duplication_scanner.py** - 1 violation(s)

[!] WARNING (line 36)
Class "DuplicationScanner" is 1948 lines - should be under 300 lines (extract related methods into separate classes)

```python


class DuplicationScanner(CodeScanner):
    
    SCANNER_VERSION = "1.0"
    
    def _get_cache_dir(self, file_path: Optional[Path] = None) -> Path:
        if file_path:
            current = file_path.parent
            while current and current.parent != current:
    # ... (truncated)
```

---

## keep_classes_small_with_single_responsibility
**intention_revealing_names_scanner.py** - 1 violation(s)

[!] WARNING (line 15)
Class "IntentionRevealingNamesScanner" is 314 lines - should be under 300 lines (extract related methods into separate classes)

```python


class IntentionRevealingNamesScanner(CodeScanner):
    
    def __init__(self):
        super().__init__()
        self.story_graph = None
    
    def scan(self, story_graph: Dict[str, Any], rule_obj: Any = None, test_files: Optional[List['Path']] = None, code_files: Optional[List['Path']] = None, on_file_scanned: Optional[Any] = None) -> List[Dict[str, Any]]:
        self.story_graph = story_graph
    # ... (truncated)
```

---

## keep_classes_small_with_single_responsibility
**real_implementations_scanner.py** - 1 violation(s)

[!] WARNING (line 14)
Class "RealImplementationsScanner" is 522 lines - should be under 300 lines (extract related methods into separate classes)

```python


class RealImplementationsScanner(TestScanner):
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, story_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
    # ... (truncated)
```

---

## keep_classes_small_with_single_responsibility
**specification_match_scanner.py** - 1 violation(s)

[!] WARNING (line 15)
Class "SpecificationMatchScanner" is 465 lines - should be under 300 lines (extract related methods into separate classes)

```python


class SpecificationMatchScanner(TestScanner):
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, story_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
    # ... (truncated)
```

---

## keep_classes_small_with_single_responsibility
**verb_noun_scanner.py** - 1 violation(s)

[!] WARNING (line 31)
Class "VerbNounScanner" is 546 lines - should be under 300 lines (extract related methods into separate classes)

```python


class VerbNounScanner(StoryScanner):
    
    def scan_domain_concept(self, node: Any, rule_obj: Any) -> List[Dict[str, Any]]:
        return []
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        name = node.name
    # ... (truncated)
```

---

## keep_classes_small_with_single_responsibility
**scoping_parameter.py** - 1 violation(s)

[!] WARNING (line 4)
Class "ScopingParameter" is 321 lines - should be under 300 lines (extract related methods into separate classes)

```python


class ScopingParameter:
    def __init__(self, scope: Dict[str, Any]):
        self._scope_type = scope.get('type')
        self._scope_value = scope.get('value')

    def filter_story_graph(self, story_graph: Dict[str, Any]) -> Dict[str, Any]:
        if self._is_all_scope():
            return story_graph
    # ... (truncated)
```

---

## keep_functions_small_focused
**utils.py** - 3 violation(s)

[!] WARNING (line 89)
Function "build_test_file_link" is 27 lines - should be under 20 lines (extract complex logic to helper functions)

```python
# Used by CLI scope display and story document synchronizers

def build_test_file_link(test_file: str, workspace_directory: Path, story_file_path: Optional[Path] = None) -> str:
    """
    Build link to test file.
    
    Args:
        test_file: Name of test file (e.g., 'test_example.py')
        workspace_directory: Path to workspace directory
        story_file_path: Optional path to story markdown file (generates absolute path from workspace root)
    
    Returns:
        Markdown link string like ' | [Test](path/to/test.py)' or empty string if not found
    """
    if not test_file:
        return ""
    try:
        from agile_bot.src.bot.workspace import get_python_workspace_root
        workspace_root = get_python_workspace_root()
        test_file_path = workspace_root / 'agile_bot' / 'test' / test_file
        if not test_file_path.exists():
            return ""
        
        # If story_file_path provided, use absolute path from workspace root (starts with /)
        # VS Code/Cursor resolves /path as relative to workspace root
        if story_file_path:
            rel_path = test_file_path.relative_to(workspace_root)
            rel_path_str = '/' + str(rel_path).replace('\\', '/')
            return f" | [Test]({rel_path_str})"
        
        rel_path = test_file_path.relative_to(workspace_root)
        rel_path_str = str(rel_path).replace('\\', '/')
        return f" | [Test]({rel_path_str})"
    except (ValueError, AttributeError):
        # Fallback: try relative to workspace_directory
        test_file_path = workspace_directory / 'test' / test_file
        if not test_file_path.exists():
            return ""
        from agile_bot.src.actions.validate.file_link_builder import FileLinkBuilder
        link_builder = FileLinkBuilder(workspace_directory)
        file_uri = link_builder.get_file_uri(str(test_file_path))
        return f" | [Test]({file_uri})"

```

[!] WARNING (line 131)
Function "build_test_class_link" is 51 lines - should be under 20 lines (extract complex logic to helper functions)

```python


def build_test_class_link(test_file: str, test_class: str, workspace_directory: Path, story_file_path: Optional[Path] = None) -> str:
    """
    Build link to test class with line number.
    
    Args:
        test_file: Name of test file (e.g., 'test_example.py')
        test_class: Name of test class (e.g., 'TestMyFeature')
        workspace_directory: Path to workspace directory
        story_file_path: Optional path to story markdown file (generates absolute path from workspace root)
    
    Returns:
        Markdown link string like ' | [Test](path/to/test.py#L123)' or empty string if not found
    """
    if not test_file or not test_class or test_class == '?':
        return ""
    
    try:
        from agile_bot.src.bot.workspace import get_python_workspace_root
        workspace_root = get_python_workspace_root()
        test_file_path = workspace_root / 'agile_bot' / 'test' / test_file
        if not test_file_path.exists():
            return ""
        
        # Find line number of test class using AST
        line_number = find_test_class_line(test_file_path, test_class)
        
        # Only create link if we found the line number
        # Don't create link without line number as it may default to line 1
        if not line_number:
            return ""
        
        # If story_file_path provided, use absolute path from workspace root (starts with /)
        # VS Code/Cursor resolves /path as relative to workspace root
        if story_file_path:
            rel_path = test_file_path.relative_to(workspace_root)
            rel_path_str = '/' + str(rel_path).replace('\\', '/')
            return f" | [Test]({rel_path_str}#L{line_number})"
        
        # Use relative path with line number using #L format
        # VS Code/Cursor markdown links use #L123 format for line numbers
        rel_path = test_file_path.relative_to(workspace_root)
        rel_path_str = str(rel_path).replace('\\', '/')
        return f" | [Test]({rel_path_str}#L{line_number})"
    except (ValueError, AttributeError):
        # Fallback: try relative to workspace_directory
        test_file_path = workspace_directory / 'test' / test_file
        if not test_file_path.exists():
            return ""
    # ... (truncated)
```

[!] WARNING (line 204)
Function "build_test_method_link" is 51 lines - should be under 20 lines (extract complex logic to helper functions)

```python


def build_test_method_link(test_file: str, test_method: str, workspace_directory: Path, story_file_path: Optional[Path] = None) -> str:
    """
    Build link to test method with line number.
    
    Args:
        test_file: Name of test file (e.g., 'test_example.py')
        test_method: Name of test method (e.g., 'test_my_scenario')
        workspace_directory: Path to workspace directory
        story_file_path: Optional path to story markdown file (generates absolute path from workspace root)
    
    Returns:
        Markdown link string like ' | [Test](path/to/test.py#L456)' or empty string if not found
    """
    if not test_file or not test_method or test_method == '?':
        return ""
    
    try:
        from agile_bot.src.bot.workspace import get_python_workspace_root
        workspace_root = get_python_workspace_root()
        test_file_path = workspace_root / 'agile_bot' / 'test' / test_file
        if not test_file_path.exists():
            return ""
        
        # Find line number of test method using AST
        line_number = find_test_method_line(test_file_path, test_method)
        
        # Only create link if we found the line number
        # Don't create link without line number as it may default to line 1
        if not line_number:
            return ""
        
        # If story_file_path provided, use absolute path from workspace root (starts with /)
        # VS Code/Cursor resolves /path as relative to workspace root
        if story_file_path:
            rel_path = test_file_path.relative_to(workspace_root)
            rel_path_str = '/' + str(rel_path).replace('\\', '/')
            return f" | [Test]({rel_path_str}#L{line_number})"
        
        # Use relative path with line number using #L format
        # VS Code/Cursor markdown links use #L123 format for line numbers
        rel_path = test_file_path.relative_to(workspace_root)
        rel_path_str = str(rel_path).replace('\\', '/')
        return f" | [Test]({rel_path_str}#L{line_number})"
    except (ValueError, AttributeError):
        # Fallback: try relative to workspace_directory
        test_file_path = workspace_directory / 'test' / test_file
        if not test_file_path.exists():
            return ""
    # ... (truncated)
```

---

## keep_functions_small_focused
**action.py** - 2 violation(s)

[!] WARNING (line 230)
Function "instructions" is 34 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    
    @property
    def instructions(self) -> Instructions:
        base_instructions = self._base_config.get('instructions', [])
        
        # Replace context placeholders in base instructions
        if isinstance(base_instructions, list):
            base_instructions = self._replace_context_placeholders(base_instructions)
        
        # Load scope from state file
        scope = self._load_scope_from_state()
        
        inst = Instructions(
            base_instructions if isinstance(base_instructions, list) else [],
            bot_paths=self.behavior.bot_paths,
            scope=scope
        )
        
        # Add context instructions (clarification, strategy, context files) at the beginning
        context_instructions = []
        # Use shared dict to capture injected data
        injected_data = {}
        try:
            context_instructions.extend(self._inject_clarification_data(injected_data))
            context_instructions.extend(self._inject_strategy_data(injected_data))
        except FileNotFoundError as e:
            logger.debug(f'Clarification or strategy data files not found: {e}')
            raise
        context_instructions.extend(self._inject_context_files(injected_data))
        
        for key, value in injected_data.items():
            inst._data[key] = value
        
        # Add standard context sources at the very top
        for line in reversed(inst.context_sources_text):
            inst._data['base_instructions'].insert(0, line)
        inst._data['base_instructions'].insert(len(inst.context_sources_text), "")  # Add blank line after context sources
        
        # Add other context instructions after the context sources
        for line in reversed(context_instructions):
            inst._data['base_instructions'].insert(len(inst.context_sources_text) + 1, line)
        
        # Status breadcrumbs for CLI output
        # COMMENTED OUT: This is now handled by the REPL CLI layer
        # breadcrumbs = self._inject_status_update_breadcrumbs({})
        # for line in breadcrumbs:
        #     inst.add_display(line)
        
        return inst

```

[!] WARNING (line 384)
Function "get_instructions" is 31 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return inject_reminder_to_instructions(result, reminder)

    def get_instructions(self, context: ActionContext = None) -> Instructions:
        """Returns AI instructions and saves any guardrails provided in context.
        
        This is the single operation for all actions:
        - Saves guardrails if provided (answers, decisions, evidence, etc.)
        - Builds and returns instructions for AI
        
        This is a template method. Subclasses override _prepare_instructions() to customize.
        """
        if context is None:
            context = self.context_class()
        
        # Save guardrails if provided in context (answers, decisions, evidence, etc.)
        # Do this FIRST before building instructions
        self._save_guardrails_if_provided(context)
        
        # If context has a new scope, let the scope apply itself to the bot
        if hasattr(context, 'scope') and context.scope:
            context.scope.apply_to_bot(self.behavior.bot_paths.workspace_directory)
        
        # Get base instructions from property
        instructions = self.instructions.copy()
        
        # Get behavior-specific instructions from action_config if available
        if self.action_config and 'instructions' in self.action_config:
            behavior_instructions = self.action_config.get('instructions', [])
            if behavior_instructions:
                # Add behavior-specific instructions to base_instructions
                if isinstance(behavior_instructions, list):
                    instructions._data['base_instructions'].extend(behavior_instructions)
                elif isinstance(behavior_instructions, str):
                    instructions._data['base_instructions'].append(behavior_instructions)
        
        # Load behavior-level guardrails (key questions and evidence) if available
        self._load_behavior_guardrails(instructions)
        
        # Call template method for subclass customization
        self._prepare_instructions(instructions, context)
        
        # Add behavior and action metadata for JSON output
        self._add_behavior_action_metadata(instructions)
        
        # Build display content for chat submission
        self._build_display_content(instructions)
        
        # Return the Instructions object directly
        # CLI will use adapters to serialize it appropriately
        return instructions
    # ... (truncated)
```

---

## keep_functions_small_focused
**actions.py** - 2 violation(s)

[!] WARNING (line 15)
Function "__init__" is 32 lines - should be under 20 lines (extract complex logic to helper functions)

```python
class Actions:

    def __init__(self, behavior: 'Behavior'):
        self.behavior = behavior
        actions_workflow = behavior._config.get('actions_workflow', {})
        actions_list = actions_workflow.get('actions', [])
        
        # Separate workflow actions (have order) from non-workflow actions (no order)
        workflow_actions = [a for a in actions_list if a.get('order') is not None]
        non_workflow_actions = [a for a in actions_list if a.get('order') is None]
        
        # Sort workflow actions by order
        workflow_actions = sorted(workflow_actions, key=lambda x: x.get('order', 0))
        
        self._factory = ActionFactory(behavior)
        self._state_manager = ActionStateManager(behavior)
        
        # _actions contains only workflow actions (for sequencing)
        self._actions: List[Action] = []
        for action_dict in workflow_actions:
            action_name = action_dict.get('name', '')
            if action_name:
                action_instance = self._factory.create_action_instance(action_name=action_name, action_config=action_dict)
                self._actions.append(action_instance)
        
        # _non_workflow_actions contains actions that can be invoked but don't participate in workflow
        self._non_workflow_actions: List[Action] = []
        for action_dict in non_workflow_actions:
            action_name = action_dict.get('name', '')
            if action_name:
                action_instance = self._factory.create_action_instance(action_name=action_name, action_config=action_dict)
                self._non_workflow_actions.append(action_instance)
        
        # Automatically add 'rules' as a non-workflow action if not already present
        # This makes 'rules' available for all behaviors without needing to explicitly add it to behavior.json
        has_rules = any(action.action_name == 'rules' for action in self._non_workflow_actions)
        if not has_rules:
            try:
                rules_action_instance = self._factory.create_action_instance(action_name='rules', action_config=None)
                self._non_workflow_actions.append(rules_action_instance)
            except Exception as e:
                # If rules action can't be created (e.g., action_config.json doesn't exist), skip it
                logging.getLogger(__name__).debug(f'Could not auto-add rules action: {e}')
        
        self._current_index: Optional[int] = None
        self.load_state()

```

[!] WARNING (line 137)
Function "close_current" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        self.save_state()

    def close_current(self):
        # Ensure we have a current action before trying to close it
        if self.current is None:
            # No current action to close - ensure we're at the first action
            if self._actions:
                self._current_index = 0
            else:
                # No actions available
                return
        
        # Now that we've ensured _current_index is set, get the current action
        current_action = self.current
        if current_action is None:
            # Still no current action after setting index - something is wrong
            return
        
        state_file = self._state_manager.get_state_file_path()
        state_data = self._state_manager.load_or_create_state(state_file)
        self._ensure_current_behavior_in_state(state_data)
        self._mark_action_completed(state_data)
        self._advance_to_next_action()
        self._update_current_action_in_state(state_data)
        self._save_state_file(state_file, state_data)

```

---

## keep_functions_small_focused
**action_state_manager.py** - 1 violation(s)

[!] WARNING (line 35)
Function "load_state" is 36 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        state_file.write_text(json.dumps(state_data, indent=2), encoding='utf-8')

    def load_state(self, actions_list: List, current_index_ref: list) -> None:
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_path.parent.mkdir(parents=True, exist_ok=True); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'action_state_manager.py:35','message':'load_state entry','data':{'behavior_bot_name':self.behavior.bot_name,'behavior_name':self.behavior.name,'actions_count':len(actions_list),'action_names':[a.action_name for a in actions_list] if actions_list else []},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H3'})+'\n'); log_file.close()
        # #endregion
        state_data = self._load_state_data()
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'action_state_manager.py:37','message':'after _load_state_data','data':{'state_data_exists':state_data is not None,'current_behavior':state_data.get('current_behavior') if state_data else None,'current_action':state_data.get('current_action') if state_data else None},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1,H4'})+'\n'); log_file.close()
        # #endregion
        if state_data is None:
            # #region agent log
            import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'action_state_manager.py:38','message':'state_data is None, setting default','data':{},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1,H4'})+'\n'); log_file.close()
            # #endregion
            self._set_default_index(actions_list, current_index_ref)
            return
        is_current = self._is_current_behavior(state_data)
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'action_state_manager.py:40','message':'checking current behavior','data':{'is_current_behavior':is_current,'expected':f'{self.behavior.bot_name}.{self.behavior.name}','actual':state_data.get('current_behavior')},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H2'})+'\n'); log_file.close()
        # #endregion
        if not is_current:
            # #region agent log
            import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'action_state_manager.py:41','message':'not current behavior, setting default','data':{},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H2'})+'\n'); log_file.close()
            # #endregion
            self._set_default_index(actions_list, current_index_ref)
            return
        if self._try_set_from_current_action(state_data, actions_list, current_index_ref):
            # #region agent log
            import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'action_state_manager.py:43','message':'set from current_action','data':{'final_index':current_index_ref[0]},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H5'})+'\n'); log_file.close()
            # #endregion
            return
        if self._try_set_from_completed_actions(state_data, actions_list, current_index_ref):
            # #region agent log
            import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'action_state_manager.py:45','message':'set from completed_actions','data':{'final_index':current_index_ref[0]},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H5'})+'\n'); log_file.close()
            # #endregion
            return
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'action_state_manager.py:47','message':'fallback to default index','data':{},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H5'})+'\n'); log_file.close()
        # #endregion
        self._set_default_index(actions_list, current_index_ref)

```

---

## keep_functions_small_focused
**behaviors.py** - 1 violation(s)

[!] WARNING (line 307)
Function "load_state" is 23 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return None

    def load_state(self):
        if self.bot_paths is None:
            self._init_to_first_behavior()
            return
        workspace_dir = self.bot_paths.workspace_directory
        state_file = workspace_dir / 'behavior_action_state.json'
        if not state_file.exists() or not self._behaviors:
            self._init_to_first_behavior()
            return
        try:
            state_data = json.loads(state_file.read_text(encoding='utf-8'))
            behavior_name = self._extract_behavior_name_from_state(state_data.get('current_behavior', ''))
            if behavior_name:
                idx = self._find_behavior_index(behavior_name)
                if idx >= 0:
                    self._current_index = idx
                    # Load action state after navigating to behavior
                    if self.current:
                        self.current.actions.load_state()
                    return
            self._init_to_first_behavior()
        except Exception:
            self._init_to_first_behavior()

```

---

## keep_functions_small_focused
**bot.py** - 8 violation(s)

[!] WARNING (line 30)
Function "__init__" is 36 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    _active_bot_name: Optional[str] = None

    def __init__(self, bot_name: str, bot_directory: Path, config_path: Path):
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_path.parent.mkdir(parents=True, exist_ok=True); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'bot.py:24','message':'Bot.__init__ entry','data':{'bot_name':bot_name,'bot_directory_param':str(bot_directory),'bot_directory_name':bot_directory.name if bot_directory else None},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1'})+'\n'); log_file.close()
        # #endregion
        self.name = bot_name
        self.bot_name = bot_name
        self.config_path = Path(config_path)
        
        # Register this bot as the active one
        Bot._active_bot_instance = self
        Bot._active_bot_name = bot_name
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'bot.py:28','message':'Before BotPaths creation','data':{'bot_directory_to_pass':str(bot_directory)},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1'})+'\n'); log_file.close()
        # #endregion
        self.bot_paths = BotPath(bot_directory=bot_directory)
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'bot.py:28','message':'After BotPaths creation','data':{},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1'})+'\n'); log_file.close()
        # #endregion
        bot_config_path = self.bot_paths.bot_directory / 'bot_config.json'
        if not bot_config_path.exists():
            raise FileNotFoundError(f'Bot config not found at {bot_config_path}')
        self._config = read_json_file(bot_config_path)
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'bot.py:33','message':'Before Behaviors creation','data':{},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1'})+'\n'); log_file.close()
        # #endregion
        # Get allowed behaviors from bot_config.json
        allowed_behaviors = self._config.get('behaviors')
        self.behaviors = Behaviors(bot_name, self.bot_paths, allowed_behaviors=allowed_behaviors)
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'bot.py:33','message':'After Behaviors creation','data':{'behavior_count':len(self.behaviors._behaviors) if self.behaviors else 0},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1'})+'\n'); log_file.close()
        # #endregion
        self.behaviors._bot_instance = self
        for behavior in self.behaviors:
            behavior.bot = self
            # Ensure behavior.bot_name matches Bot's bot_name (not directory name)
            behavior.bot_name = self.bot_name
        
        # Create Scope instance with workspace context and load from state
        self._scope = Scope(self.bot_paths.workspace_directory, self.bot_paths)
        self._scope.load()
        
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'bot.py:37','message':'Bot.__init__ exit','data':{},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1'})+'\n'); log_file.close()
        # #endregion
```

[!] WARNING (line 286)
Function "scope" is 131 lines - should be under 20 lines (extract complex logic to helper functions)

```python
            }
    
    def scope(self, scope_filter: Optional[str] = None):
        """Set or view the scope filter for the current workflow.
        
        AI AGENTS: This command requires COMPLETE folder paths. When you pass a directory path,
        you MUST include the ENTIRE folder structure from root or working area.
        
        Args:
            scope_filter: Complete folder path or story name to filter by, or None to view current scope
        
        Returns:
            Dict with status, message, and scope data when setting scope, or Scope object when viewing
        """
        from ..scope.scope import ScopeType
        import os
        
        if scope_filter is None:
            # Return current scope instance for property access
            return self._scope
        
        # Track if this is a clear operation
        is_clear = False
        
        # Strip "set" or "clear" keywords from CLI commands
        scope_filter_lower = scope_filter.lower().strip()
        if scope_filter_lower.startswith('set '):
            scope_filter = scope_filter[4:].strip()  # Remove "set " prefix
            scope_filter_lower = scope_filter.lower().strip()  # Recalculate after removing "set"
        
        # Strip surrounding quotes (single or double) from the filter value
        scope_filter = scope_filter.strip()
        if (scope_filter.startswith('"') and scope_filter.endswith('"')) or \
           (scope_filter.startswith("'") and scope_filter.endswith("'")):
            scope_filter = scope_filter[1:-1]
            scope_filter_lower = scope_filter.lower().strip()  # Recalculate after stripping quotes
        
        if scope_filter_lower == 'clear':
            # Clear scope
            is_clear = True
            self._scope.clear()
            self._scope.save()
            from ..scope.scope_command_result import ScopeCommandResult
            return ScopeCommandResult(
                status='success',
                message='Scope cleared',
                scope=self._scope
            )
        
        if scope_filter.lower() == 'all':
    # ... (truncated)
```

[!] WARNING (line 501)
Function "next" is 24 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        }

    def next(self) -> Dict[str, Any]:
        """Navigate to the next action in the current behavior workflow.
        
        Returns:
            Dict with navigation result (new position, message)
        """
        if not self.behaviors.current:
            return {
                'status': 'error',
                'message': 'No behavior is currently active. Use a behavior.action command to start.'
            }
        
        behavior = self.behaviors.current
        current_action = behavior.actions.current_action_name
        
        if not current_action:
            # No current action, start with first action
            if behavior.action_names:
                first_action = behavior.action_names[0]
                behavior.actions.navigate_to(first_action)
                self.behaviors.save_state()  # Persist state
                return {
                    'status': 'success',
                    'message': f'Moved to {behavior.name}.{first_action}',
                    'behavior': behavior.name,
                    'action': first_action
                }
            else:
                return {
                    'status': 'error',
                    'message': f'Behavior {behavior.name} has no actions'
                }
        
        # Find next action
        action_names = behavior.action_names
        try:
            current_index = action_names.index(current_action)
            if current_index < len(action_names) - 1:
                next_action = action_names[current_index + 1]
                behavior.actions.navigate_to(next_action)
                self.behaviors.save_state()  # Persist state
                return {
                    'status': 'success',
                    'message': f'Moved to {behavior.name}.{next_action}',
                    'behavior': behavior.name,
                    'action': next_action
                }
            else:
    # ... (truncated)
```

[!] WARNING (line 606)
Function "execute" is 38 lines - should be under 20 lines (extract complex logic to helper functions)

```python
            }
    
    def execute(self, behavior_name: str, action_name: Optional[str] = None, params: Optional[Dict[str, Any]] = None) -> Any:
        """Execute a specific behavior.action and return instructions.
        
        Navigates to behavior/action and calls get_instructions() with optional parameters.
        
        Args:
            behavior_name: Name of the behavior to execute
            action_name: Name of the action to execute (optional, uses current action if None)
            params: Optional parameters to pass to action context (guardrails, answers, decisions, etc.)
        
        Returns:
            Instructions object from action.get_instructions()
        """
        # Find behavior
        behavior = self.behaviors.find_by_name(behavior_name)
        if not behavior:
            return {
                'status': 'error',
                'message': f'Behavior not found: {behavior_name}',
                'available_behaviors': [b.name for b in self.behaviors]
            }
        
        # Set as current behavior
        self.behaviors.navigate_to(behavior_name)
        
        # Determine action to execute
        if action_name:
            # Set specific action as current
            try:
                behavior.actions.navigate_to(action_name)
            except ValueError:
                return {
                    'status': 'error',
                    'message': f'Action not found: {action_name}',
                    'available_actions': behavior.action_names
                }
        else:
            # Use current action or first action
            if not behavior.actions.current_action_name:
                if behavior.action_names:
                    behavior.actions.navigate_to(behavior.action_names[0])
                else:
                    return {
                        'status': 'error',
                        'message': f'Behavior {behavior_name} has no actions'
                    }
        
        # Get current action
    # ... (truncated)
```

[!] WARNING (line 687)
Function "save" is 43 lines - should be under 20 lines (extract complex logic to helper functions)

```python
            }
    
    def save(self, answers: Optional[Dict[str, str]] = None,
             evidence_provided: Optional[Dict[str, str]] = None,
             decisions: Optional[Dict[str, str]] = None,
             assumptions: Optional[List[str]] = None) -> Dict[str, Any]:
        """Save guardrail data (answers, evidence, decisions, assumptions) for current behavior.
        
        Args:
            answers: Question-answer pairs for clarification
            evidence_provided: Evidence key-value pairs for clarification
            decisions: Criteria-decision pairs for strategy
            assumptions: List of assumption strings for strategy
        
        Returns:
            Status dict with success/error message
        """
        from ..actions.clarify.requirements_clarifications import RequirementsClarifications
        from ..actions.clarify.required_context import RequiredContext
        from ..actions.strategy.strategy_decision import StrategyDecision
        from ..actions.strategy.strategy import Strategy
        
        current_behavior = self.behaviors.current
        if not current_behavior:
            return {
                'status': 'error',
                'message': 'No current behavior set'
            }
        
        try:
            saved_items = []
            
            if answers or evidence_provided:
                required_context = RequiredContext(current_behavior.folder)
                clarifications = RequirementsClarifications(
                    behavior_name=current_behavior.name,
                    bot_paths=current_behavior.bot_paths,
                    required_context=required_context,
                    key_questions_answered=answers or {},
                    evidence_provided=evidence_provided or {},
                    context=None
                )
                clarifications.save()
                if answers:
                    saved_items.append('answers')
                if evidence_provided:
                    saved_items.append('evidence')
            
            if decisions or assumptions:
                strategy = Strategy(current_behavior.folder)
    # ... (truncated)
```

[!] WARNING (line 767)
Function "submit_behavior_rules" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

```python
            }
    
    def submit_behavior_rules(self, behavior_name: str) -> Dict[str, Any]:
        """Get rules for a behavior and submit them to AI chat.
        
        This is a convenience method that:
        1. Saves current position
        2. Navigates to behavior
        3. Submits rules using behavior.submitRules()
        4. Restores previous position
        
        Args:
            behavior_name: Name of the behavior to get rules for
            
        Returns:
            Status dict with success message and submission details
        """
        # Save current position
        saved_behavior = self.behaviors.current.name if self.behaviors.current else None
        saved_action = self.behaviors.current.actions.current_action_name if self.behaviors.current else None
        
        try:
            # Find the behavior
            behavior = self.behaviors.find_by_name(behavior_name)
            if not behavior:
                return {
                    'status': 'error',
                    'message': f'Behavior not found: {behavior_name}'
                }
            
            # Navigate to behavior (sets it as current)
            self.behaviors.navigate_to(behavior_name)
            
            # Submit the rules using behavior.submitRules()
            submit_result = behavior.submitRules()
            
            # Restore previous position if needed
            if saved_behavior and saved_action:
                try:
                    self.execute(saved_behavior, saved_action)
                except:
                    pass  # Don't fail if restore doesn't work
            
            return submit_result
            
        except Exception as e:
            logger.error(f'Error in submit_behavior_rules: {str(e)}', exc_info=True)
            return {
                'status': 'error',
                'message': f'Error getting rules for {behavior_name}: {str(e)}'
    # ... (truncated)
```

[!] WARNING (line 817)
Function "submit_instructions" is 37 lines - should be under 20 lines (extract complex logic to helper functions)

```python
            }
    
    def submit_instructions(self, instructions, behavior_name: str = None, action_name: str = None) -> Dict[str, Any]:
        """Submit given Instructions object to AI chat.
        
        Args:
            instructions: Instructions object with display_content to submit
            behavior_name: Optional behavior name (for reporting, will be inferred if not provided)
            action_name: Optional action name (for reporting, will be inferred if not provided)
            
        Returns:
            Status dict with success message, behavior/action info, and submission details
        """
        display_content = instructions.display_content
        if not display_content:
            return {
                'status': 'error',
                'message': 'No instructions available to submit'
            }
        
        # Convert display_content to string
        if isinstance(display_content, list):
            content_str = '\n'.join(display_content)
        else:
            content_str = str(display_content)
        
        # Copy to clipboard and automate Cursor chat using keyboard shortcuts
        clipboard_status = 'failed'
        cursor_status = 'not_attempted'
        
        try:
            import pyperclip
            import pyautogui
            import time
            
            # Copy to clipboard
            pyperclip.copy(content_str)
            clipboard_status = 'success'
            time.sleep(0.2)
            
            # Ctrl+L to open chat
            pyautogui.hotkey('ctrl', 'l')
            time.sleep(0.3)
            
            # Ctrl+V to paste
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.2)
            
            cursor_status = 'opened'
            
    # ... (truncated)
```

[!] WARNING (line 936)
Function "tree" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

```python
            }

    def tree(self) -> str:
        """Display behavior hierarchy tree.
        
        Returns:
            String representation of all behaviors and their actions
        """
        lines = []
        behaviors_list = list(self.behaviors)
        
        for i, behavior in enumerate(behaviors_list):
            is_last_behavior = (i == len(behaviors_list) - 1)
            behavior_prefix = "└──" if is_last_behavior else "├──"
            is_current_behavior = (self.behaviors.current and behavior.name == self.behaviors.current.name)
            behavior_marker = "➤ " if is_current_behavior else ""
            lines.append(f"{behavior_prefix} {behavior_marker}{behavior.name}")
            
            # Show actions
            action_names = behavior.action_names
            for j, action in enumerate(action_names):
                is_last_action = (j == len(action_names) - 1)
                action_prefix = "    └──" if is_last_behavior else "│   └──" if is_last_action else "│   ├──"
                if not is_last_behavior and not is_last_action:
                    action_prefix = "│   ├──"
                is_current_action = (is_current_behavior and 
                                   behavior.actions.current_action_name == action)
                action_marker = "➤ " if is_current_action else ""
                lines.append(f"{action_prefix} {action_marker}{action}")
        
        return "\n".join(lines)
    
```

---

## keep_functions_small_focused
**markdown_bot.py** - 1 violation(s)

[!] WARNING (line 75)
Function "behavior_action_summary" is 25 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    
    @property
    def behavior_action_summary(self):
        """Returns summary of all behaviors and actions."""
        lines = []
        
        # Get behavior names
        behavior_names = []
        for behavior in self.bot.behaviors:
            name = behavior.name
            if name == (self.bot.behaviors.current.name if self.bot.behaviors.current else None):
                behavior_names.append(f"**{name}**")
            else:
                behavior_names.append(name)
        
        lines.append(f"**Behaviors:** {' | '.join(behavior_names)}")
        
        # Get actions from current behavior
        behavior = self.bot.behaviors.current or next(iter(self.bot.behaviors), None)
        if behavior:
            action_names = []
            all_actions = list(behavior.actions) + list(behavior.actions._non_workflow_actions)
            current_action_name = behavior.actions.current.action_name if behavior.actions.current else None
            for action in all_actions:
                name = action.action_name
                if name == current_action_name:
                    action_names.append(f"**{name}**")
                else:
                    action_names.append(name)
            lines.append(f"**Actions:** {' | '.join(action_names)}")
        
        return '\n'.join(lines)
    
```

---

## keep_functions_small_focused
**workspace.py** - 1 violation(s)

[i] INFO (line 25)
Function "get_base_actions_directory" has deep nesting (depth=5) - should be under 4 levels. Extract nested logic to helper functions.

```python
    return Path(workspace.strip())

def get_base_actions_directory(bot_directory: Path=None) -> Path:
    """
    Get base actions directory.
    
    Args:
        bot_directory: Optional bot directory path. If None, uses BOT_DIRECTORY env var.
    
    Returns:
        Path to base_actions directory (from bot_config.json or default to agile_bot/base_actions)
    """
    from ..utils import read_json_file
    
    if bot_directory is None:
        bot_directory = get_bot_directory()
    
    # Try to read from bot_config.json
    config_paths = [
        bot_directory / 'bot_config.json',
        bot_directory / 'config' / 'bot_config.json'
    ]
    
    python_workspace_root = get_python_workspace_root()
    
    for config_path in config_paths:
        if config_path.exists():
            try:
                config = read_json_file(config_path)
                base_actions_path = config.get('baseActionsPath')
                if base_actions_path:
                    # If relative path, resolve from workspace root
                    path = Path(base_actions_path)
                    if not path.is_absolute():
                        path = python_workspace_root / base_actions_path
                    return path
            except Exception:
                pass  # Fall through to default
    
    # Default: base_actions at workspace root level
    return python_workspace_root / 'agile_bot' / 'base_actions'

```

---

## keep_functions_small_focused
**adapters.py** - 1 violation(s)

[!] WARNING (line 172)
Function "serialize" is 32 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        self.data = data
    
    def serialize(self) -> str:
        """Format data for TTY output with ANSI formatting."""
        if isinstance(self.data, dict):
            # Check if it's a scope response (status/message/scope)
            if 'scope' in self.data and isinstance(self.data['scope'], dict):
                scope_data = self.data['scope']
                scope_type = scope_data.get('type', 'all')
                target = scope_data.get('target', [])
                
                if target:
                    target_str = ', '.join(str(t) for t in target)
                    return f"\x1b[1mScope:\x1b[0m {scope_type}: {target_str}"
                else:
                    return f"\x1b[1mScope:\x1b[0m {scope_type}"
            # Check if it's an execution result
            elif 'status' in self.data and 'behavior' in self.data and 'action' in self.data:
                lines = []
                lines.append(f"\x1b[1mStatus:\x1b[0m {self.data['status']}")
                lines.append(f"\x1b[1mBehavior:\x1b[0m {self.data['behavior']}")
                lines.append(f"\x1b[1mAction:\x1b[0m {self.data['action']}")
                if 'message' in self.data:
                    lines.append(f"\x1b[1mMessage:\x1b[0m {self.data['message']}")
                if 'result' in self.data:
                    lines.append(f"\x1b[1mResult:\x1b[0m {self.data['result']}")
                return '\n'.join(lines)
            else:
                # Generic dict formatting
                lines = []
                for key, value in self.data.items():
                    lines.append(f"\x1b[1m{key}:\x1b[0m {value}")
                return '\n'.join(lines)
        # For lists/other types, use JSON as fallback
        import json
        return json.dumps(self.data, indent=2)
    
```

---

## keep_functions_small_focused
**adapter_factory.py** - 1 violation(s)

[!] WARNING (line 113)
Function "create" is 26 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    
    @classmethod
    def create(cls, domain_object: Any, channel: str, **kwargs):
        """
        Create appropriate adapter for domain object and channel.
        
        Args:
            domain_object: Domain object to adapt (Status, Scope, etc.)
            channel: Output channel ('json', 'tty', 'markdown')
            **kwargs: Additional arguments to pass to adapter constructor (e.g., is_current)
        
        Returns:
            Adapter instance wrapping domain_object
        
        Raises:
            ValueError: If no adapter registered for domain type and channel
        """
        domain_type = type(domain_object).__name__
        
        # Fallback for dict/list/str - use channel-specific generic adapter
        if domain_type in ('dict', 'list', 'str'):
            if channel == 'json':
                from agile_bot.src.cli.adapters import GenericJSONAdapter
                return GenericJSONAdapter(domain_object)
            elif channel == 'tty':
                from agile_bot.src.cli.adapters import GenericTTYAdapter
                return GenericTTYAdapter(domain_object)
            elif channel == 'markdown':
                from agile_bot.src.cli.adapters import GenericMarkdownAdapter
                return GenericMarkdownAdapter(domain_object)
            else:
                # Default to JSON for unknown channels
                from agile_bot.src.cli.adapters import GenericJSONAdapter
                return GenericJSONAdapter(domain_object)
        
        key = (domain_type, channel)
        
        if key not in cls._registry:
            raise ValueError(f"No {channel} adapter registered for {domain_type}")
        
        module_path, class_name = cls._registry[key]
        
        # Dynamic import
        import importlib
        module = importlib.import_module(module_path)
        adapter_class = getattr(module, class_name)
        
        return adapter_class(domain_object, **kwargs)
    
```

---

## keep_functions_small_focused
**cli_main.py** - 1 violation(s)

[!] WARNING (line 52)
Function "main" is 100 lines - should be under 20 lines (extract complex logic to helper functions)

```python
from agile_bot.src.cli.cli_session import CLISession

def main():
    bot_name = bot_directory.name
    workspace_directory = get_workspace_directory()
    bot_config_path = bot_directory / 'bot_config.json'
    
    if not bot_config_path.exists():
        print(f"ERROR: Bot config not found at {bot_config_path}", file=sys.stderr)
        sys.exit(1)
    
    try:
        bot = Bot(
            bot_name=bot_name,
            bot_directory=bot_directory,
            config_path=bot_config_path
        )
    except Exception as e:
        print(f"ERROR: Failed to initialize bot: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Check if we're in JSON mode (for Node.js panel integration)
    json_mode = os.environ.get('CLI_MODE', '').lower() == 'json'
    mode = 'json' if json_mode else None
    
    is_piped = not sys.stdin.isatty()
    
    # In piped mode, peek at stdin to check for --format json flag
    if is_piped and not json_mode:
        # Read first line to check for --format json
        first_line = sys.stdin.readline().strip()
        if '--format json' in first_line or '--format=json' in first_line:
            json_mode = True
            mode = 'json'
        # Put the line back by creating new stdin from it + rest of input
        import io
        remaining_input = sys.stdin.read()
        sys.stdin = io.StringIO(first_line + '\n' + remaining_input)
    
    cli_session = CLISession(bot=bot, workspace_directory=workspace_directory, mode=mode)
    
    # Check if we should suppress header (for panel integration or explicit JSON output)
    suppress_header = json_mode or os.environ.get('SUPPRESS_CLI_HEADER', '') == '1'
    
    # Print header (unless suppressed for JSON output)
    if not suppress_header:
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"\033[1m{bot_name.upper()} CLI\033[0m")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("")
    # ... (truncated)
```

---

## keep_functions_small_focused
**cli_session.py** - 2 violation(s)

[!] WARNING (line 38)
Function "execute_command" is 245 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        self.mode = mode
    
    def execute_command(self, command: str) -> CLICommandResponse:
        """
        Route command to Bot method, return command response.
        
        Command mappings:
        - "status" -> bot itself (serialized via TTYBot)
        - "scope" -> bot.scope -> Scope object (property)
        - "next" -> bot.next() -> NavigationResult object
        - "back" -> bot.back() -> NavigationResult object
        - "help" -> bot.help() -> Help object
        - "exit" -> bot.exit() -> ExitResult object
        - "behavior.action" -> bot.execute('behavior', 'action') -> ActionResult
        
        Args:
            command: Command string from user input
        
        Returns:
            CLICommandResponse with serialized output and metadata
        """
        # Parse command
        verb, args = self._parse_command(command)
        
        # Check for --format json flag and set mode
        if args and ('--format json' in args or '--format=json' in args):
            # Set mode to json (stays that way until changed)
            self.mode = 'json'
            # Strip --format json from args
            args = args.replace('--format json', '').replace('--format=json', '').strip()
        
        # Check for exit command
        cli_terminated = verb == 'exit'
        
        # Track if this command changes navigation state (should auto-display status)
        is_navigation_command = verb in ('next', 'back', 'current', 'scope', 'path', 'workspace')
        
        # Special case: "status" just returns the bot itself
        if verb == 'status':
            result = self.bot
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
    # ... (truncated)
```

[!] WARNING (line 636)
Function "run" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return AdapterFactory.create(domain_object, channel)
    
    def run(self):
        """
        Run CLI loop (for interactive mode).
        
        Reads commands from stdin and executes them.
        """
        try:
            while True:
                try:
                    line = input(f"[{self.bot.name}] > ").strip()
                    if not line:
                        continue
                    
                    response = self.execute_command(line)
                    print(response.output)
                    print("")  # Blank line after output
                    
                    if response.cli_terminated:
                        break
                    
                except EOFError:
                    print("\nExiting CLI...")
                    break
                except KeyboardInterrupt:
                    print("\n\nInterrupted by user. Exiting CLI...")
                    break
                except Exception as e:
                    print(f"Error: {e}", file=sys.stderr)
                    
        except KeyboardInterrupt:
            pass

```

---

## keep_functions_small_focused
**help.py** - 1 violation(s)

[i] INFO (line 181)
Function "__init__" has deep nesting (depth=5) - should be under 4 levels. Extract nested logic to helper functions.

```python
    """
    
    def __init__(self, bot=None):
        """Initialize Help.
        
        Args:
            bot: Bot instance for delegating to behaviors/actions
        """
        self.bot = bot
        self.commands = CommandsHelp()
        self.scope = ScopeHelp()
        
        # Components delegates to bot if available
        if bot:
            behaviors_names = bot.behaviors.names if hasattr(bot, 'behaviors') else []
            # Get all unique actions across all behaviors
            actions_list = []
            if hasattr(bot, 'behaviors'):
                for behavior in bot.behaviors:
                    for action in behavior.actions:
                        # Add if not already in list (by name)
                        if not any(a.action_name == action.action_name for a in actions_list):
                            actions_list.append(action)
            self.components = ComponentsHelp(behaviors_names, actions_list)
        else:
            self.components = ComponentsHelp()
    
```

---

## keep_functions_small_focused
**help_action.py** - 1 violation(s)

[!] WARNING (line 19)
Function "to_cli_type" is 33 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    
    @staticmethod
    def to_cli_type(python_type) -> str:
        """Convert Python type hint to CLI-friendly string.
        
        Examples:
            str -> "string"
            Path -> "path"
            dict -> "dict"
            Dict[str, Any] -> "dict"
            List[str] -> "list"
        """
        # Handle None type
        if python_type is type(None):
            return "none"
        
        # Handle basic types
        if python_type == str:
            return "string"
        elif python_type == Path:
            return "path"
        elif python_type == int:
            return "int"
        elif python_type == float:
            return "float"
        elif python_type == bool:
            return "bool"
        elif python_type == dict:
            return "dict"
        elif python_type == list:
            return "list"
        elif python_type == tuple:
            return "tuple"
        elif python_type == set:
            return "set"
        
        # Handle generic types (Dict[...], List[...], etc.)
        origin = get_origin(python_type)
        if origin is dict:
            return "dict"
        elif origin is list:
            return "list"
        elif origin is tuple:
            return "tuple"
        elif origin is set:
            return "set"
        
        # Fallback for unknown types
        return "value"

```

---

## keep_functions_small_focused
**markdown_help.py** - 1 violation(s)

[!] WARNING (line 14)
Function "serialize" is 50 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        self.help_obj = help_obj
    
    def serialize(self) -> str:
        """Convert Help to Markdown string - mirrors TTYHelp structure."""
        lines = []
        
        # Core Commands section
        lines.append(self.format_header(2, "Core Commands"))
        core = self.help_obj.commands.core
        lines.append(f"  {core.navigation_pattern}  - {core.description_full}")
        lines.append(f"  {core.short_navigation_pattern}           - {core.description_short}")
        lines.append("")
        
        # Available Components section
        lines.append("  Available Components:")
        lines.append(f"    behaviors   -> {self.help_obj.components.behaviors}")
        lines.append("")
        lines.append("    actions:")
        for action_name, description in self.help_obj.components.actions:
            lines.append(f"      {action_name:<12} - {description}")
        lines.append("")
        lines.append("    operations:")
        for operation, params in self.help_obj.components.operations.operations:
            if params:
                lines.append(f"      {operation:<12} {params}")
            else:
                lines.append(f"      {operation}")
        lines.append("")
        
        # Examples section
        lines.append("  Examples:")
        for cmd, desc in self.help_obj.commands.examples.examples:
            lines.append(f"    echo '{cmd}' | python repl_main.py{' ' * (30 - len(cmd))} -> {desc}")
        lines.append("")
        
        # Other Commands section
        lines.append("  Other Commands:")
        for cmd, desc in self.help_obj.commands.other.commands:
            lines.append(f"    echo '{cmd}' | python repl_main.py{' ' * (30 - len(cmd))} - {desc}")
        lines.append("")
        
        # Scope Command Details section
        lines.append("  Scope Command Details:")
        for rule in self.help_obj.scope.important_rules:
            lines.append(f"    {rule}")
        lines.append("")
        lines.append("    Usage (pick ONE - each replaces the previous scope):")
        for pattern, desc in self.help_obj.scope.usage_patterns:
            lines.append(f"      echo '{pattern}' | python repl_main.py{' ' * (55 - len(pattern))} - {desc}")
        lines.append("")
    # ... (truncated)
```

---

## keep_functions_small_focused
**tty_help.py** - 1 violation(s)

[!] WARNING (line 20)
Function "serialize" is 49 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        self.help_obj = help_obj
    
    def serialize(self) -> str:
        """Convert Help to TTY string - assembles all help sections."""
        lines = []
        
        # Core Commands section
        lines.append(self.add_color("Core Commands:", 'green'))
        core = self.help_obj.commands.core
        lines.append(f"  {core.navigation_pattern}  - {core.description_full}")
        lines.append(f"  {core.short_navigation_pattern}           - {core.description_short}")
        lines.append("")
        
        # Available Components section
        lines.append("  Available Components:")
        lines.append(f"    behaviors   -> {self.help_obj.components.behaviors}")
        lines.append("")
        lines.append("    actions:")
        for action_name, description in self.help_obj.components.actions:
            lines.append(f"      {action_name:<12} - {description}")
        lines.append("")
        lines.append("    operations:")
        for operation, params in self.help_obj.components.operations.operations:
            if params:
                lines.append(f"      {operation:<12} {params}")
            else:
                lines.append(f"      {operation}")
        lines.append("")
        
        # Examples section
        lines.append("  Examples:")
        for cmd, desc in self.help_obj.commands.examples.examples:
            lines.append(f"    echo '{cmd}' | python repl_main.py{' ' * (30 - len(cmd))} -> {desc}")
        lines.append("")
        
        # Other Commands section
        lines.append("  Other Commands:")
        for cmd, desc in self.help_obj.commands.other.commands:
            lines.append(f"    echo '{cmd}' | python repl_main.py{' ' * (30 - len(cmd))} - {desc}")
        lines.append("")
        
        # Scope Command Details section
        lines.append("  Scope Command Details:")
        for rule in self.help_obj.scope.important_rules:
            lines.append(f"    {rule}")
        lines.append("")
        lines.append("    Usage (pick ONE - each replaces the previous scope):")
        for pattern, desc in self.help_obj.scope.usage_patterns:
            lines.append(f"      echo '{pattern}' | python repl_main.py{' ' * (55 - len(pattern))} - {desc}")
        lines.append("")
    # ... (truncated)
```

---

## keep_functions_small_focused
**markdown_instructions.py** - 1 violation(s)

[!] WARNING (line 14)
Function "serialize" is 189 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        self.instructions = instructions
    
    def serialize(self) -> str:
        """Convert Instructions to Markdown string."""
        instructions_dict = self.instructions.to_dict()
        output_lines = []
        
        # SCOPE SECTION (only show if scope has actual filter values set, or is 'showAll')
        scope = self.instructions.scope
        # Check if scope has filter values (scope.value) - this determines if scope is "empty"
        # When scope.type is 'all', scope.value is empty → don't show scope section
        # When scope.type is 'showAll', scope.value is empty but we show full graph
        # When scope.type is 'story'/'files', scope.value has filter terms → show filtered results
        if scope and (scope.value or scope.type.value == 'showAll'):
            from agile_bot.src.cli.adapters import MarkdownAdapter
            
            output_lines.append("## Scope")
            output_lines.append("")
            if scope.type.value == 'story':
                output_lines.append(f"**Story Scope:** {', '.join(scope.value)}")
            elif scope.type.value == 'files':
                output_lines.append(f"**File Scope:** {', '.join(scope.value)}")
            elif scope.type.value == 'showAll':
                output_lines.append("**Scope:** Show All (entire story graph)")
            else:
                output_lines.append(f"**Scope:** {scope.type.value} - {', '.join(scope.value) if scope.value else 'all'}")
            output_lines.append("")
            
            # Get the filtered results (story graph or files)
            # Show results when scope has filter values OR when type is 'showAll'
            results = scope.results
            if results:
                # Use the appropriate adapter to serialize the scope results
                from agile_bot.src.cli.adapter_factory import AdapterFactory
                try:
                    adapter = AdapterFactory.create(results, 'markdown')
                    scope_content = adapter.serialize()
                    output_lines.append(scope_content)
                except Exception:
                    # Fallback: just show the filter value
                    pass
            
            output_lines.append("")
            output_lines.append("---")
            output_lines.append("")
        
        # BEHAVIOR INSTRUCTIONS SECTION
        behavior_metadata = instructions_dict.get('behavior_metadata', {})
        if behavior_metadata:
            behavior_name = behavior_metadata.get('name', 'unknown')
    # ... (truncated)
```

---

## keep_functions_small_focused
**tty_instructions.py** - 1 violation(s)

[!] WARNING (line 14)
Function "serialize" is 157 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        self.instructions = instructions
    
    def serialize(self) -> str:
        """Convert Instructions to TTY string - assembles all instruction sections."""
        instructions_dict = self.instructions.to_dict()
        output_lines = []
        
        # BEHAVIOR INSTRUCTIONS SECTION
        behavior_metadata = instructions_dict.get('behavior_metadata', {})
        if behavior_metadata:
            behavior_name = behavior_metadata.get('name', 'unknown')
            output_lines.append(f"{self.add_bold(f'Behavior Instructions - {behavior_name}')}")
            
            # Add behavior description
            behavior_description = behavior_metadata.get('description', '')
            if behavior_description:
                output_lines.append(f"The purpose of this behavior is to {behavior_description.lower()}")
                output_lines.append("")
            
            # Add behavior-level instructions if present
            behavior_instructions = behavior_metadata.get('instructions', [])
            if behavior_instructions:
                if isinstance(behavior_instructions, list):
                    output_lines.extend(behavior_instructions)
                elif isinstance(behavior_instructions, str):
                    output_lines.append(behavior_instructions)
                output_lines.append("")
        
        # ACTION INSTRUCTIONS SECTION
        action_metadata = instructions_dict.get('action_metadata', {})
        if action_metadata:
            action_name = action_metadata.get('name', 'unknown')
            output_lines.append(f"{self.add_bold(f'Action Instructions - {action_name}')}")
            
            # Add action description if available
            action_description = action_metadata.get('description', '')
            if action_description:
                output_lines.append(f"The purpose of this action is to {action_description.lower()}")
                output_lines.append("")
            
            # Add behavior-specific action instructions if present
            action_instructions = action_metadata.get('instructions', [])
            if action_instructions:
                output_lines.extend(action_instructions)
                output_lines.append("")
        
        output_lines.append("---")
        output_lines.append("")
        
        # Add base instructions (context sources + base action instructions)
    # ... (truncated)
```

---

## keep_functions_small_focused
**rule.py** - 1 violation(s)

[!] WARNING (line 117)
Function "scan" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return issubclass(self._scanner, TestScanner) or issubclass(self._scanner, CodeScanner)

    def scan(self, story_graph: Dict[str, Any], files: Optional[Dict[str, List[Path]]]=None, on_file_scanned: Optional[Any]=None, skip_cross_file: bool=False, changed_files: Optional[Dict[str, List[Path]]]=None, status_writer: Optional[Any]=None, max_cross_file_comparisons: int=20) -> Dict[str, Any]:
        if not self.has_scanner:
            return {}
        files = files or {}
        files_to_scan = changed_files if changed_files else files
        test_files = files_to_scan.get('test', [])
        code_files = files_to_scan.get('src', [])
        # For cross-file scanning: use scoped files if scope is active, otherwise all files
        # The 'files' parameter already contains scoped files when scope is active
        all_test_files = files.get('test', [])
        all_code_files = files.get('src', [])
        self._initialize_scan_state()
        try:
            scanner_instance = self._get_scanner_instance()
            self._execute_file_by_file_scan(scanner_instance, story_graph, test_files, code_files, on_file_scanned)
            # Cross-file scan uses the same scoped files - all_test_files/all_code_files are already scoped
            self._execute_cross_file_scan(scanner_instance, skip_cross_file, test_files, code_files, all_test_files, all_code_files, status_writer, max_cross_file_comparisons)
            return self._build_scan_result()
        except Exception as e:
            self._scan_error = str(e)
            self._scanner_execution_status = f'EXECUTION_FAILED: {str(e)}'
            raise

```

---

## keep_functions_small_focused
**rules.py** - 3 violation(s)

[!] WARNING (line 133)
Function "from_parameters" is 42 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    
    @classmethod
    def from_parameters(cls, parameters: Dict[str, Any], behavior, bot_paths, callbacks: Optional[ValidationCallbacks] = None) -> 'ValidationContext':
        from agile_bot.src.actions.action_context import ValidateActionContext, Scope, ScopeType, FileFilter
        from agile_bot.src.bot.behavior import Behavior
        
        if isinstance(behavior, str):
            behavior = Behavior(name=behavior, bot_paths=bot_paths)
        
        scope = None
        if 'scope' in parameters and parameters['scope']:
            scope_dict = parameters['scope']
            if isinstance(scope_dict, dict):
                scope_type_str = scope_dict.get('type', 'all')
                scope_type = ScopeType(scope_type_str)
                scope = Scope(
                    type=scope_type,
                    value=scope_dict.get('value', []),
                    exclude=scope_dict.get('exclude', []),
                    skiprule=scope_dict.get('skiprule', [])
                )
        elif 'test' in parameters or 'src' in parameters:
            # Convert test/src parameters to files scope
            file_paths = []
            if 'test' in parameters:
                test_files = parameters['test']
                if isinstance(test_files, str):
                    file_paths.append(test_files)
                elif isinstance(test_files, list):
                    file_paths.extend(test_files)
            if 'src' in parameters:
                src_files = parameters['src']
                if isinstance(src_files, str):
                    file_paths.append(src_files)
                elif isinstance(src_files, list):
                    file_paths.extend(src_files)
            
            if file_paths:
                scope = Scope(
                    type=ScopeType.FILES,
                    value=file_paths,
                    exclude=[],
                    skiprule=[]
                )
        
        all_files = parameters.get('all_files', False) or parameters.get('force_full', False)
        
        context = ValidateActionContext(
            scope=scope,
            background=parameters.get('background'),
    # ... (truncated)
```

[!] WARNING (line 195)
Function "get_last_report_timestamp" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return rules_instance._rule_filter.filter_files(self.files, self.exclude)

    def get_last_report_timestamp(self) -> float:
        logger = logging.getLogger(__name__)
        docs_path = self.bot_paths.documentation_path
        reports_dir = self.bot_paths.workspace_directory / docs_path / 'reports'
        logger.info(f'Looking for previous reports in: {reports_dir}')
        if not reports_dir.exists():
            logger.info('Reports directory does not exist - returning 0.0')
            return 0.0
        
        report_files = list(reports_dir.glob(f'{self.behavior.name}-validation-status-*.md'))
        logger.info(f'Found {len(report_files)} report files')
        if not report_files:
            logger.info('No report files found - returning 0.0')
            return 0.0
        
        current_time = time.time()
        previous_run_files = [f for f in report_files if (current_time - f.stat().st_mtime) > 10]
        logger.info(f'Found {len(previous_run_files)} previous run files (excluding files < 10 seconds old)')
        
        if not previous_run_files:
            logger.info('No previous run files found - returning 0.0')
            return 0.0
        
        most_recent = max(previous_run_files, key=lambda p: p.stat().st_mtime)
        logger.info(f'Most recent previous report: {most_recent.name} (timestamp: {most_recent.stat().st_mtime})')
        return most_recent.stat().st_mtime

```

[!] WARNING (line 322)
Function "formatted_rules_digest" is 24 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return '\n'.join(sections) if sections else 'No validation rules found.'

    def formatted_rules_digest(self) -> str:
        rules = self._load_rules()
        if not rules:
            return 'No validation rules found.'
        
        # Sort by priority (lower number = higher priority)
        rules = sorted(rules, key=lambda r: r.priority)
        
        lines = ['Rules to follow:', '']
        for i, rule in enumerate(rules):
            description = rule.description or 'No description'
            lines.append(f"- **{rule.name}**: {description}")
            
            # Add DO description if present
            do_section = rule.rule_content.get('do', {})
            do_desc = do_section.get('description', '')
            if do_desc:
                lines.append(f"  DO: {do_desc}")
            
            # Add DON'T description if present
            dont_section = rule.rule_content.get('dont', {})
            dont_desc = dont_section.get('description', '')
            if dont_desc:
                lines.append(f"  DON'T: {dont_desc}")
            
            # Add blank line between rules, but not after the last rule
            if i < len(rules) - 1:
                lines.append("")
        
        return '\n'.join(lines)

```

---

## keep_functions_small_focused
**background_common_setup_scanner.py** - 1 violation(s)

[!] WARNING (line 11)
Function "scan_story_node" has high cognitive complexity (17) - should be under 15. Reduce nesting and extract complex logic.

```python
class BackgroundCommonSetupScanner(StoryScanner):
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        if isinstance(node, Story):
            story_data = node.data
            scenarios = story_data.get('scenarios', [])
            background = story_data.get('background', [])
            
            if background:
                violation = self._check_background_has_when_then(background, node, rule_obj)
                if violation:
                    violations.append(violation)
                
                violation = self._check_background_scenario_specific(background, scenarios, node, rule_obj)
                if violation:
                    violations.append(violation)
            
            if len(scenarios) >= 3 and not background:
                violation = self._check_missing_background(scenarios, node, rule_obj)
                if violation:
                    violations.append(violation)
        
        return violations
    
```

---

## keep_functions_small_focused
**class_based_organization_scanner.py** - 1 violation(s)

[!] WARNING (line 17)
Function "scan_file" is 29 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return []  # Test scanning happens in scan_test_file, not scan_story_node
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, story_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        if not file_path.exists():
            return violations
        
        sub_epic_names = self._extract_sub_epic_names(story_graph)
        file_name = file_path.stem  # Without .py extension
        violation = self._check_file_name_matches_sub_epic(file_name, sub_epic_names, file_path, rule_obj, story_graph)
        if violation:
            violations.append(violation)
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
        
        content, lines, tree = parsed
        
        story_names = self._extract_story_names(story_graph)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                if node.name.startswith('Test'):
                    violation = self._check_class_name_matches_story(node.name, story_names, file_path, rule_obj)
                    if violation:
                        violations.append(violation)
                    
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef):
                            if item.name.startswith('test_'):
                                violation = self._check_method_name_matches_scenario(
                                    item.name, node.name, story_names, story_graph, file_path, rule_obj
                                )
                                if violation:
                                    violations.append(violation)
        
        return violations
    
```

---

## keep_functions_small_focused
**code_representation_scanner.py** - 1 violation(s)

[!] WARNING (line 19)
Function "scan_domain_concept" is 33 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    ]
    
    def scan_domain_concept(self, node: DomainConceptNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        node_name_lower = node.name.lower()
        for pattern in self.ABSTRACT_PATTERNS:
            if pattern in node_name_lower:
                violations.append(
                    Violation(
                        rule=rule_obj,
                        violation_message=f'Domain concept "{node.name}" uses abstract terminology. Domain models should represent code closely - refactor code if needed.',
                        location=node.map_location('name'),
                        line_number=None,
                        severity='info'
                    ).to_dict()
                )
                break
        
        for i, responsibility_data in enumerate(node.responsibilities):
            responsibility_name = responsibility_data.get('name', '')
            collaborators = responsibility_data.get('collaborators', [])
            
            for collab in collaborators:
                collab_lower = collab.strip().lower()
                for pattern in self.ABSTRACT_PATTERNS:
                    if pattern in collab_lower:
                        violations.append(
                            Violation(
                                rule=rule_obj,
                                violation_message=f'Responsibility "{responsibility_name}" uses abstract collaborator "{collab.strip()}". Use concrete domain concepts that exist in code.',
                                location=node.map_location(f'responsibilities[{i}].collaborators'),
                                line_number=None,
                                severity='info'
                            ).to_dict()
                        )
                        break
        
        return violations

```

---

## keep_functions_small_focused
**complexity_metrics.py** - 5 violation(s)

[!] WARNING (line 26)
Function "cognitive_complexity" is 28 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    
    @staticmethod
    def cognitive_complexity(func_node: ast.FunctionDef) -> int:
        complexity = 0
        nesting_level = 0
        
        def visit_node(node: ast.AST, level: int):
            nonlocal complexity
            
            # Increment complexity for decision points
            if isinstance(node, (ast.If, ast.For, ast.While, ast.ExceptHandler)):
                complexity += 1 + level  # Nesting adds to complexity
                # Visit children with increased nesting
                for child in ast.iter_child_nodes(node):
                    visit_node(child, level + 1)
            elif isinstance(node, ast.With):
                complexity += 1 + level
                for child in ast.iter_child_nodes(node):
                    visit_node(child, level + 1)
            elif isinstance(node, ast.BoolOp):
                complexity += len(node.values) - 1 + level
                for child in ast.iter_child_nodes(node):
                    visit_node(child, level)
            elif isinstance(node, ast.Assert):
                complexity += 1 + level
            else:
                # Visit children at same nesting level
                for child in ast.iter_child_nodes(node):
                    visit_node(child, level)
        
        for stmt in func_node.body:
            visit_node(stmt, 0)
        
        return complexity
    
```

[!] WARNING (line 86)
Function "detect_responsibilities_with_examples" is 34 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    
    @staticmethod
    def detect_responsibilities_with_examples(func_node: ast.FunctionDef) -> Dict[str, List[Dict[str, Any]]]:
        responsibilities: Dict[str, List[Dict[str, Any]]] = {}
        
        def add_example(resp_type: str, node: ast.AST):
            if resp_type not in responsibilities:
                responsibilities[resp_type] = []
            # Only keep first 2 examples per type to avoid verbose output
            if len(responsibilities[resp_type]) < 2:
                line = getattr(node, 'lineno', None)
                try:
                    code = ast.unparse(node) if hasattr(ast, 'unparse') else str(node)
                    if len(code) > 80:
                        code = code[:77] + '...'
                except:
                    code = '<code unavailable>'
                responsibilities[resp_type].append({'line': line, 'code': code})
        
        for node in ast.walk(func_node):
            # I/O operations - must be actual file/network operations, not dict methods
            if isinstance(node, ast.Call):
                func_name = ComplexityMetrics._get_call_name(node)
                if func_name and ComplexityMetrics._is_io_operation(func_name, node):
                    add_example('I/O', node)
            
            # Validation (assertions, checks, validations)
            if isinstance(node, ast.Assert):
                add_example('Validation', node)
            
            # Transformation (assignments with meaningful operations, not simple accessors)
            if isinstance(node, ast.Assign):
                if ComplexityMetrics._has_transformation(node):
                    add_example('Transformation', node)
            
            # Computation (math operations - but not simple comparisons or string ops)
            if isinstance(node, ast.BinOp):
                # Only count actual math, not string concatenation or list operations
                if isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow, ast.FloorDiv)):
                    add_example('Computation', node)
        
        return responsibilities
    
```

[!] WARNING (line 204)
Function "calculate_lcom" is 25 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    
    @staticmethod
    def calculate_lcom(class_node: ast.ClassDef) -> float:
        methods = [node for node in class_node.body if isinstance(node, ast.FunctionDef)]
        
        # Filter out simple property getters - they're data accessors, not real methods
        meaningful_methods = []
        for method in methods:
            if not ComplexityMetrics._is_simple_property_getter(method):
                meaningful_methods.append(method)
        
        if len(meaningful_methods) < 2:
            return 0.0  # Single method or no methods = perfect cohesion
        
        method_attributes = []
        for method in meaningful_methods:
            attrs = ComplexityMetrics._get_accessed_attributes(method, class_node)
            method_attributes.append(attrs)
        
        # Count pairs of methods that don't share attributes
        non_shared_pairs = 0
        total_pairs = 0
        
        for i in range(len(method_attributes)):
            for j in range(i + 1, len(method_attributes)):
                total_pairs += 1
                if not (method_attributes[i] & method_attributes[j]):
                    non_shared_pairs += 1
        
        if total_pairs == 0:
            return 0.0
        
        # LCOM = ratio of non-shared pairs to total pairs
        return non_shared_pairs / total_pairs
    
```

[!] WARNING (line 330)
Function "detect_class_responsibilities_with_examples" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    
    @staticmethod
    def detect_class_responsibilities_with_examples(class_node: ast.ClassDef) -> Dict[str, List[Dict[str, Any]]]:
        methods = [node for node in class_node.body if isinstance(node, ast.FunctionDef)]
        
        if len(methods) == 0:
            return {}
        
        # Group methods by responsibility type with examples
        responsibility_groups: Dict[str, List[Dict[str, Any]]] = {}
        
        for method in methods:
            responsibilities_detailed = ComplexityMetrics.detect_responsibilities_with_examples(method)
            if not responsibilities_detailed:
                # Method has no detected responsibility - classify as General
                if 'General' not in responsibility_groups:
                    responsibility_groups['General'] = []
                if len(responsibility_groups['General']) < 2:
                    code_sample = ComplexityMetrics._get_method_code_sample(method)
                    responsibility_groups['General'].append({
                        'method': method.name,
                        'line': method.lineno,
                        'code': code_sample
                    })
            else:
                for resp_type, examples in responsibilities_detailed.items():
                    if resp_type not in responsibility_groups:
                        responsibility_groups[resp_type] = []
                    if len(responsibility_groups[resp_type]) < 2 and examples:
                        first_example = examples[0]
                        responsibility_groups[resp_type].append({
                            'method': method.name,
                            'line': first_example.get('line'),
                            'code': first_example.get('code', '')
                        })
        
        return responsibility_groups

```

[!] WARNING (line 30)
Function "visit_node" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        nesting_level = 0
        
        def visit_node(node: ast.AST, level: int):
            nonlocal complexity
            
            # Increment complexity for decision points
            if isinstance(node, (ast.If, ast.For, ast.While, ast.ExceptHandler)):
                complexity += 1 + level  # Nesting adds to complexity
                # Visit children with increased nesting
                for child in ast.iter_child_nodes(node):
                    visit_node(child, level + 1)
            elif isinstance(node, ast.With):
                complexity += 1 + level
                for child in ast.iter_child_nodes(node):
                    visit_node(child, level + 1)
            elif isinstance(node, ast.BoolOp):
                complexity += len(node.values) - 1 + level
                for child in ast.iter_child_nodes(node):
                    visit_node(child, level)
            elif isinstance(node, ast.Assert):
                complexity += 1 + level
            else:
                # Visit children at same nesting level
                for child in ast.iter_child_nodes(node):
                    visit_node(child, level)
        
```

---

## keep_functions_small_focused
**cover_all_paths_scanner.py** - 1 violation(s)

[!] WARNING (line 13)
Function "scan_file" is 34 lines - should be under 20 lines (extract complex logic to helper functions)

```python
class CoverAllPathsScanner(TestScanner):
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, story_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
        
        content, lines, tree = parsed
        
        # Find all test methods
        functions = Functions(tree)
        test_methods = [function.node for function in functions.get_many_functions if function.node.name.startswith('test_')]
        
        for test_method in test_methods:
            # Check if test has actual code (not just pass/docstrings)
            found_code_node = None
            for stmt in test_method.body:
                if isinstance(stmt, ast.Pass):
                    continue
                elif isinstance(stmt, ast.Expr) and isinstance(stmt.value, (ast.Constant, ast.Str)):
                    # Skip docstrings
                    continue
                else:
                    for node in ast.walk(stmt):
                        if isinstance(node, (ast.Call, ast.Assign, ast.Assert, ast.Return, ast.Raise)):
                            found_code_node = node
                            break
                    # Break outer loop if we found code
                    if found_code_node is not None:
                        break
            
            if found_code_node is None:
                # No code snippet for empty test method violations (method definition line)
                violations.append(Violation(
                    rule=rule_obj,
                    violation_message=f'Test method "{test_method.name}" has no actual test code - tests must exercise behavior paths, not just contain pass statements',
                    location=str(file_path),
                    line_number=test_method.lineno,
                    severity='error'
                ).to_dict())
        
        return violations

```

---

## keep_functions_small_focused
**dead_code_scanner.py** - 2 violation(s)

[!] WARNING (line 23)
Function "scan" is 55 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    """Scanner for detecting dead/unused code."""
    
    def scan(
        self, 
        story_graph: Dict[str, Any], 
        rule_obj: Any = None,
        test_files: Optional[List[Path]] = None,
        code_files: Optional[List[Path]] = None,
        on_file_scanned: Optional[Any] = None
    ) -> List[Dict[str, Any]]:
        """Override scan to perform cross-file analysis for dead code detection.
        
        Dead code detection requires analyzing the entire codebase to determine
        what is used vs unused.
        """
        violations = []
        
        # Combine all files
        all_files = []
        if code_files:
            all_files.extend(code_files)
        if test_files:
            all_files.extend(test_files)
        
        if not all_files:
            return violations
        
        # First pass: collect all definitions and usages across all files
        definitions = {}  # {name: (file_path, line_number, node_type)}
        usages = set()  # {name}
        
        for file_path in all_files:
            if not file_path.exists() or not file_path.is_file():
                continue
            
            try:
                file_defs, file_usages = self._analyze_file(file_path)
                
                # Store definitions with file context
                for name, (line_num, node_type) in file_defs.items():
                    # Use qualified name for module-level items
                    qualified_name = f"{file_path.stem}.{name}"
                    definitions[qualified_name] = (file_path, line_num, node_type, name)
                    # Also store the simple name for cross-module usage detection
                    if name not in definitions:
                        definitions[name] = (file_path, line_num, node_type, name)
                
                usages.update(file_usages)
                
            except Exception as e:
    # ... (truncated)
```

[!] WARNING (line 108)
Function "scan_file" is 29 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return violations
    
    def scan_file(
        self,
        file_path: Path,
        rule_obj: Any = None,
        story_graph: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Scan a single file for dead code within that file only.
        
        This is a simpler analysis that only detects:
        - Private methods that are never called within the same file
        - Local variables that are assigned but never used
        """
        violations = []
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
        
        content, lines, tree = parsed
        
        # Find private methods and their usages within the file
        private_defs, private_usages = self._analyze_private_members(tree)
        
        for method_name, (line_num, class_name) in private_defs.items():
            if method_name not in private_usages:
                # Skip dunder methods - they're protocol implementations
                if method_name.startswith('__') and method_name.endswith('__'):
                    continue
                
                violation = self._create_violation_with_snippet(
                    rule_obj=rule_obj,
                    violation_message=f"Private method '{method_name}' in class '{class_name}' is never called - consider removing dead code",
                    file_path=file_path,
                    line_number=line_num,
                    severity='warning',
                    content=content,
                    start_line=line_num
                )
                violations.append(violation)
        
        return violations
    
```

---

## keep_functions_small_focused
**dependency_chaining_scanner.py** - 1 violation(s)

[!] WARNING (line 11)
Function "scan_domain_concept" is 32 lines - should be under 20 lines (extract complex logic to helper functions)

```python
class DependencyChainingScanner(DomainScanner):
    
    def scan_domain_concept(self, node: DomainConceptNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        has_instantiation = False
        instantiation_collaborators = []
        
        for i, responsibility_data in enumerate(node.responsibilities):
            responsibility_name = responsibility_data.get('name', '')
            resp_lower = responsibility_name.lower()
            
            if 'instantiated with' in resp_lower:
                has_instantiation = True
                collaborators = responsibility_data.get('collaborators', [])
                instantiation_collaborators = [c.strip() for c in collaborators]
                break
        
        # This is a simplified check - full implementation would track dependency chain
        if has_instantiation:
            for i, responsibility_data in enumerate(node.responsibilities):
                responsibility_name = responsibility_data.get('name', '')
                if 'instantiated with' in responsibility_name.lower():
                    continue
                
                collaborators = responsibility_data.get('collaborators', [])
                
                for collab in collaborators:
                    collab = collab.strip()
                    if collab and collab not in instantiation_collaborators:
                        if self._might_be_sub_collaborator(collab, instantiation_collaborators):
                            violations.append(
                                Violation(
                                    rule=rule_obj,
                                    violation_message=f'Responsibility "{responsibility_name}" may be accessing sub-collaborator "{collab}" directly. Access through owning object instead.',
                                    location=node.map_location(f'responsibilities[{i}].collaborators'),
                                    line_number=None,
                                    severity='info'
                                ).to_dict()
                            )
        
        return violations
    
```

---

## keep_functions_small_focused
**domain_grouping_code_scanner.py** - 1 violation(s)

[!] WARNING (line 22)
Function "scan_file" is 27 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    ]
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, story_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        if not file_path.exists():
            return violations
        
        file_path_str = str(file_path)
        for pattern in self.TECHNICAL_LAYER_PATTERNS:
            if re.search(pattern, file_path_str, re.IGNORECASE):
                violations.append(
                    Violation(
                        rule=rule_obj,
                        violation_message=f'File path "{file_path}" uses technical layer terminology. Organize by domain area instead.',
                        location=str(file_path),
                        line_number=None,
                        severity='info'
                    ).to_dict()
                )
                break
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
        
        content, lines, tree = parsed
        
        classes = Classes(tree)
        for cls in classes.get_many_classes:
            violation = self._check_class_name(cls.node, file_path, rule_obj)
            if violation:
                violations.append(violation)
        
        return violations
    
```

---

## keep_functions_small_focused
**domain_language_code_scanner.py** - 1 violation(s)

[!] WARNING (line 46)
Function "scan_file" is 32 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return super().scan(story_graph, rule_obj, test_files=test_files, code_files=code_files, on_file_scanned=on_file_scanned)
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, story_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        if not file_path.exists():
            return violations
        
        domain_terms = set()
        if self.story_graph:
            domain_terms = self._extract_domain_terms(self.story_graph)
        
        # Generic names that are acceptable in specific contexts
        generic_names = {'self', 'result', 'value', 'data', 'item', 'obj', 'workspace', 'root', 'path', 'config'}
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
        
        content, lines, tree = parsed
        
        classes = Classes(tree)
        for cls in classes.get_many_classes:
            class_violations = self._check_domain_language(cls.node, file_path, rule_obj, domain_terms, generic_names)
            violations.extend(class_violations)
            
            for child in cls.node.body:
                if isinstance(child, ast.FunctionDef):
                    func_violations = self._check_function_domain_language(
                        child, file_path, rule_obj, domain_terms, generic_names,
                        enclosing_class=cls.node.name
                    )
                    violations.extend(func_violations)
        
        for node in ast.iter_child_nodes(tree):
            if isinstance(node, ast.FunctionDef):
                func_violations = self._check_function_domain_language(
                    node, file_path, rule_obj, domain_terms, generic_names,
                    enclosing_class=None
                )
                violations.extend(func_violations)
        
        return violations
    
```

---

## keep_functions_small_focused
**domain_language_scanner.py** - 1 violation(s)

[!] WARNING (line 25)
Function "scan_domain_concept" is 45 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    ]
    
    def scan_domain_concept(self, node: DomainConceptNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        node_name_lower = node.name.lower()
        for term in ['data', 'config', 'parameter', 'result']:
            if term in node_name_lower and not self._is_domain_specific(node.name):
                violations.append(
                    Violation(
                        rule=rule_obj,
                        violation_message=f'Domain concept "{node.name}" uses generic term "{term}". Use domain-specific language instead (e.g., "PortfolioData" → "Portfolio", "TargetConfig" → "TargetAllocation").',
                        location=node.map_location('name'),
                        line_number=None,
                        severity='warning'
                    ).to_dict()
                )
        
        for i, responsibility_data in enumerate(node.responsibilities):
            responsibility_name = responsibility_data.get('name', '')
            collaborators = responsibility_data.get('collaborators', [])
            resp_lower = responsibility_name.lower()
            
            for collab in collaborators:
                collab_lower = collab.lower()
                for term in self.GENERIC_TERMS:
                    if term in collab_lower and not self._is_domain_specific(collab):
                        violations.append(
                            Violation(
                                rule=rule_obj,
                                violation_message=f'Responsibility "{responsibility_name}" uses generic collaborator "{collab}". Use domain-specific language instead.',
                                location=node.map_location(f'responsibilities[{i}].collaborators'),
                                line_number=None,
                                severity='warning'
                            ).to_dict()
                        )
                        break
            
            for pattern in self.GENERATE_PATTERNS:
                if re.search(pattern, resp_lower):
                    violations.append(
                        Violation(
                            rule=rule_obj,
                            violation_message=f'Responsibility "{responsibility_name}" uses generate/calculate. Use property instead (e.g., "Get recommended trades" not "Generate recommendation").',
                            location=node.map_location(f'responsibilities[{i}].name'),
                            line_number=None,
                            severity='warning'
                        ).to_dict()
                    )
                    break
    # ... (truncated)
```

---

## keep_functions_small_focused
**domain_scanner.py** - 1 violation(s)

[!] WARNING (line 17)
Function "scan" is 32 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    """
    
    def scan(
        self, 
        story_graph: Dict[str, Any], 
        rule_obj: Any = None,
        test_files: Optional[List['Path']] = None,
        code_files: Optional[List['Path']] = None,
        on_file_scanned: Optional[Any] = None
    ) -> List[Dict[str, Any]]:
        """Scan domain concepts in the story graph.
        
        Domain scanners ONLY scan domain concepts, not story/epic/sub-epic nodes.
        """
        if not rule_obj:
            raise ValueError("rule_obj parameter is required for DomainScanner")
        
        violations = []
        story_graph_data = story_graph.get('story_graph', story_graph)
        story_map = StoryMap(story_graph_data)
        
        # Domain scanners should ONLY scan domain concepts
        for epic in story_map.epics():
            # Scan domain concepts at epic level
            epic_violations = self._scan_domain_concepts(
                epic.data.get('domain_concepts', []),
                epic.epic_idx,
                None,
                rule_obj
            )
            violations.extend(epic_violations)
            
            # Walk through sub_epics to find domain concepts
            for node in story_map.walk(epic):
                if hasattr(node, 'data') and 'domain_concepts' in node.data:
                    sub_epic_violations = self._scan_domain_concepts(
                        node.data.get('domain_concepts', []),
                        epic.epic_idx,
                        getattr(node, 'sub_epic_path', None),
                        rule_obj
                    )
                    violations.extend(sub_epic_violations)
        
        return violations
    
```

---

## keep_functions_small_focused
**duplication_scanner.py** - 3 violation(s)

[!] WARNING (line 108)
Function "scan_file" is 63 lines - should be under 20 lines (extract complex logic to helper functions)

```python
            logger.debug(f"Cache write failed for {file_path}: {e}")
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, story_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        _safe_print(f"[DuplicationScanner.scan_code_file] Called for: {file_path}")
        
        if not file_path.exists():
            _safe_print(f"[DuplicationScanner.scan_code_file] File does not exist: {file_path}")
            return violations
        
        # Track time for timeout detection
        file_start_time = datetime.now()
        
        try:
            file_size = file_path.stat().st_size
            if file_size > 500_000:  # Skip files larger than 500KB
                _safe_print(f"Skipping large file ({file_size/1024:.1f}KB): {file_path}")
                return violations
        except Exception as e:
            _safe_print(f"Could not check file size for {file_path}: {e}")
        
        try:
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(file_path))
            lines = content.split('\n')
            
            functions = []
            
            def extract_functions_from_node(node: ast.AST, parent_class: str = None):
                if isinstance(node, ast.ClassDef):
                    # Found a class - extract its methods
                    for child in node.body:
                        extract_functions_from_node(child, node.name)
                elif isinstance(node, ast.FunctionDef):
                    # Found a function - extract it with class context
                    func_body = ast.unparse(node.body) if hasattr(ast, 'unparse') else str(node.body)
                    functions.append((node.name, func_body, node.lineno, node, parent_class))
            
            for node in tree.body:
                extract_functions_from_node(node, None)
            
            func_violations = self._check_duplicate_functions(functions, file_path, rule_obj, lines)
            violations.extend(func_violations)
            
            elapsed = (datetime.now() - file_start_time).total_seconds()
            if elapsed > FILE_SCAN_TIMEOUT:
                _safe_print(f"TIMEOUT: File scan exceeded {FILE_SCAN_TIMEOUT}s: {file_path} (stopping early)")
                return violations
            
    # ... (truncated)
```

[!] WARNING (line 1683)
Function "scan_cross_file" is 253 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return nearby_files
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
        test_files: Optional[List[Path]] = None,
        code_files: Optional[List[Path]] = None,
        all_test_files: Optional[List[Path]] = None,
        all_code_files: Optional[List[Path]] = None,
        status_writer: Optional[Any] = None,
        max_cross_file_comparisons: int = 20
    ) -> List[Dict[str, Any]]:
        violations = []
        
        # If all_* not provided, fall back to regular behavior
        if all_test_files is None:
            all_test_files = test_files
        if all_code_files is None:
            all_code_files = code_files
        
        # Combine changed files (to scan)
        changed_files = []
        if code_files:
            changed_files.extend(code_files)
        if test_files:
            changed_files.extend(test_files)
        
        # Combine all files (for reference)
        all_files = []
        if all_code_files:
            all_files.extend(all_code_files)
        if all_test_files:
            all_files.extend(all_test_files)
        
        if not changed_files or not all_files:
            return violations
        
        # Filter all_files to only include files in nearby packages
        all_files = self._filter_files_by_package_proximity(changed_files, all_files, max_files=max_cross_file_comparisons)
        
        if len(changed_files) < len(all_files):
            _safe_print(f"\n[CROSS-FILE] Incremental scan: Checking {len(changed_files)} changed file(s) against {len(all_files)} total files...")
        else:
            _safe_print(f"\n[CROSS-FILE] Full scan: Scanning {len(all_files)} files for cross-file duplication...")
        import sys
        
        def write_status(msg: str):
            if status_writer and hasattr(status_writer, 'write_cross_file_progress'):
                try:
                    status_writer.write_cross_file_progress(msg)
    # ... (truncated)
```

[!] WARNING (line 784)
Function "extract_from_node" has high cyclomatic complexity (18) - should be under 10. Extract decision logic to helper functions.

```python
                             ast.AsyncFor, ast.AsyncWith)
        
        def extract_from_node(node):
            if isinstance(node, control_structures):
                # Count nodes in this subtree
                num_nodes = len(list(ast.walk(node)))
                if min_nodes <= num_nodes <= max_nodes:
                    subtrees.append(node)
            
            if hasattr(node, 'body') and isinstance(node.body, list):
                for child in node.body:
                    extract_from_node(child)
            
            if hasattr(node, 'orelse') and isinstance(node.orelse, list):
                for child in node.orelse:
                    extract_from_node(child)
            
            if hasattr(node, 'handlers') and isinstance(node.handlers, list):
                for handler in node.handlers:
                    if hasattr(handler, 'body') and isinstance(handler.body, list):
                        for child in handler.body:
                            extract_from_node(child)
            
            if hasattr(node, 'finalbody') and isinstance(node.finalbody, list):
                for child in node.finalbody:
                    extract_from_node(child)
        
```

---

## keep_functions_small_focused
**full_result_assertions_scanner.py** - 1 violation(s)

[!] WARNING (line 38)
Function "scan_file" is 23 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    }

    def scan_file(self, file_path: Path, rule_obj: Any = None, story_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations: List[Dict[str, Any]] = []

        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations

        content, lines, tree = parsed

        for func in [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name.startswith("test")]:
            alias_targets = self._collect_result_aliases(func)
            if self._has_full_object_assert(func, alias_targets):
                continue  # already asserting full object on result-like object
            for node in ast.walk(func):
                if isinstance(node, ast.Assert):
                    if self._is_single_field_assert(node.test, alias_targets):
                        violations.append(
                            Violation(
                                rule=rule_obj,
                                violation_message="Assertion checks a single field of a complex result - assert the full object (or dataclass equality) using standard data.",
                                line_number=node.lineno,
                                location=str(file_path),
                                severity="warning",
                            ).to_dict()
                        )

        return violations

```

---

## keep_functions_small_focused
**function_size_scanner.py** - 1 violation(s)

[!] WARNING (line 151)
Function "visit_statement" is 32 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        multi_line_lines = set()
        
        def visit_statement(stmt_node):
            if hasattr(stmt_node, 'end_lineno') and hasattr(stmt_node, 'lineno') and stmt_node.end_lineno and stmt_node.lineno:
                if stmt_node.end_lineno > stmt_node.lineno:
                    # This statement spans multiple lines
                    if isinstance(stmt_node, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
                        # Assignment statement - check if the value/expression is multi-line
                        if hasattr(stmt_node, 'value') and stmt_node.value:
                            value = stmt_node.value
                            if hasattr(value, 'end_lineno') and hasattr(value, 'lineno') and value.end_lineno and value.lineno:
                                if value.end_lineno > value.lineno:
                                    # Multi-line expression in assignment
                                    # Exclude continuation lines (all except first)
                                    for line_num in range(value.lineno + 1, value.end_lineno + 1):
                                        multi_line_lines.add(line_num)
                    
                    elif isinstance(stmt_node, ast.Expr):
                        # Expression statement (e.g., function call)
                        if hasattr(stmt_node, 'value') and stmt_node.value:
                            value = stmt_node.value
                            if isinstance(value, ast.Call):
                                # Function call - check if it spans multiple lines
                                if hasattr(value, 'end_lineno') and hasattr(value, 'lineno') and value.end_lineno and value.lineno:
                                    if value.end_lineno > value.lineno:
                                        # Multi-line function call - exclude continuation lines
                                        for line_num in range(value.lineno + 1, value.end_lineno + 1):
                                            multi_line_lines.add(line_num)
                    
                    elif isinstance(stmt_node, ast.Return):
                        if stmt_node.value:
                            if hasattr(stmt_node.value, 'end_lineno') and hasattr(stmt_node.value, 'lineno') and stmt_node.value.end_lineno and stmt_node.value.lineno:
                                if stmt_node.value.end_lineno > stmt_node.value.lineno:
                                    # Multi-line return expression
                                    for line_num in range(stmt_node.value.lineno + 1, stmt_node.value.end_lineno + 1):
                                        multi_line_lines.add(line_num)
        
```

---

## keep_functions_small_focused
**given_precondition_scanner.py** - 1 violation(s)

[!] WARNING (line 12)
Function "scan_story_node" has high cognitive complexity (20) - should be under 15. Reduce nesting and extract complex logic.

```python
class GivenPreconditionScanner(StoryScanner):
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        if isinstance(node, Story):
            story_data = node.data
            scenarios = story_data.get('scenarios', [])
            
            for scenario_idx, scenario in enumerate(scenarios):
                scenario_steps = self._get_scenario_steps(scenario)
                
                for step_idx, step in enumerate(scenario_steps):
                    if step.startswith('Given') or step.startswith('And'):
                        violation = self._check_given_is_functionality(step, node, scenario_idx, step_idx, rule_obj)
                        if violation:
                            violations.append(violation)
        
        return violations
    
```

---

## keep_functions_small_focused
**given_state_not_actions_scanner.py** - 1 violation(s)

[!] WARNING (line 12)
Function "scan_story_node" has high cognitive complexity (20) - should be under 15. Reduce nesting and extract complex logic.

```python
class GivenStateNotActionsScanner(StoryScanner):
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        if isinstance(node, Story):
            story_data = node.data
            scenarios = story_data.get('scenarios', [])
            
            for scenario_idx, scenario in enumerate(scenarios):
                scenario_steps = self._get_scenario_steps(scenario)
                
                for step_idx, step in enumerate(scenario_steps):
                    if step.startswith('Given') or step.startswith('And'):
                        violation = self._check_given_is_action(step, node, scenario_idx, step_idx, rule_obj)
                        if violation:
                            violations.append(violation)
        
        return violations
    
```

---

## keep_functions_small_focused
**given_when_then_helpers_scanner.py** - 1 violation(s)

[!] WARNING (line 251)
Function "scan_cross_file" is 43 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return None, [], False, 0
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
        test_files: Optional[List[Path]] = None,
        code_files: Optional[List[Path]] = None,
        all_test_files: Optional[List[Path]] = None,
        all_code_files: Optional[List[Path]] = None,
        status_writer: Optional[Any] = None,
        max_cross_file_comparisons: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        violations = []
        
        if not test_files or len(test_files) < 2:
            # Need at least 2 files to detect cross-file issues
            return violations
        
        # Reuse base class method to parse all test files
        parsed_files = self._get_all_test_files_parsed(test_files)
        
        helper_definitions = {}  # func_name -> list of (file_path, line_number)
        
        for file_path, content, tree in parsed_files:
            # Reuse existing method to get defined helpers
            defined_helpers = self._get_defined_helper_functions(tree)
            
            for func_name, line_number in defined_helpers.items():
                if func_name not in helper_definitions:
                    helper_definitions[func_name] = []
                helper_definitions[func_name].append((
                    str(file_path),
                    line_number
                ))
        
        # Check: Duplicate helper functions across files (ONLY - no usage warnings)
        for func_name, definitions in helper_definitions.items():
            if len(definitions) > 1:
                # Same helper function defined in multiple files - should be consolidated
                files_list = ', '.join([f"{Path(f).name}:{line}" for f, line in definitions])
                violation = Violation(
                    rule=rule_obj,
                    violation_message=(
                        f'Helper function "{func_name}" is defined in {len(definitions)} different files. '
                        f'Consolidate into a shared helper file based on reuse scope. '
                        f'Found in: {files_list}'
                    ),
                    location=definitions[0][0],  # First occurrence
                    line_number=definitions[0][1],
                    severity='error'
    # ... (truncated)
```

---

## keep_functions_small_focused
**implementation_details_scanner.py** - 1 violation(s)

[!] WARNING (line 20)
Function "scan_story_node" is 25 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    ]
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        # Only scan actual Story nodes, not Epic or SubEpic nodes
        # Sub-epics can have imperative names like "Create Mobs" because they group stories
        if not isinstance(node, Story):
            return violations
        
        if not hasattr(node, 'name') or not node.name:
            return violations
        
        name_lower = node.name.lower()
        
        for verb in self.IMPLEMENTATION_VERBS:
            pattern = rf'\b{verb}\b'
            if re.search(pattern, name_lower):
                # If it's just "Verb Noun" without user context, it's likely implementation
                words = name_lower.split()
                # Check if verb is at the start (most common pattern for implementation operations)
                if verb in words[0] or (len(words) > 1 and verb in words[0:2]):
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Story "{node.name}" appears to be an implementation operation - should be a step within a story that describes user/system outcome',
                        location=node.name,
                        severity='error'
                    ).to_dict()
                    violations.append(violation)
                    break
        
        return violations

```

---

## keep_functions_small_focused
**intention_revealing_names_scanner.py** - 1 violation(s)

[!] WARNING (line 283)
Function "visit_node" has high cognitive complexity (23) - should be under 15. Reduce nesting and extract complex logic.

```python
        docstring_ranges = []
        
        def visit_node(node):
            if hasattr(node, 'body') and isinstance(node.body, list) and len(node.body) > 0:
                first_stmt = node.body[0]
                if isinstance(first_stmt, ast.Expr):
                    # Docstring is an expression with a constant string
                    if isinstance(first_stmt.value, (ast.Constant, ast.Str)):
                        if isinstance(first_stmt.value, ast.Constant):
                            docstring_value = first_stmt.value.value
                        else:  # ast.Str (Python < 3.8)
                            docstring_value = first_stmt.value.s
                        
                        if isinstance(docstring_value, str):
                            start_line = first_stmt.lineno if hasattr(first_stmt, 'lineno') else None
                            if start_line:
                                # Count lines in docstring content
                                docstring_lines = docstring_value.count('\n')
                                end_line = start_line + docstring_lines + 2
                                docstring_ranges.append((start_line, end_line))
            
            # Recursively visit child nodes
            for child in ast.iter_child_nodes(node):
                visit_node(child)
        
```

---

## keep_functions_small_focused
**invest_principles_scanner.py** - 1 violation(s)

[!] WARNING (line 11)
Function "scan_story_node" is 24 lines - should be under 20 lines (extract complex logic to helper functions)

```python
class InvestPrinciplesScanner(StoryScanner):
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        # Only check Story nodes (not epics/sub-epics)
        if not isinstance(node, Story):
            return violations
        
        if not hasattr(node, 'name') or not node.name:
            return violations
        
        # Check Testable: Story should have scenarios/scenario_outlines OR acceptance criteria in JSON
        story_data = node.data if hasattr(node, 'data') else {}
        scenarios = story_data.get('scenarios', [])
        scenario_outlines = story_data.get('scenario_outlines', [])
        acceptance_criteria = story_data.get('acceptance_criteria', [])
        
        # Story is testable if it has scenarios OR scenario_outlines OR acceptance criteria
        # Stories can have EITHER scenarios OR scenario_outlines (not requiring both)
        has_scenarios = (scenarios and len(scenarios) > 0) or (scenario_outlines and len(scenario_outlines) > 0)
        has_acceptance_criteria = acceptance_criteria and len(acceptance_criteria) > 0
        
        if not has_scenarios and not has_acceptance_criteria:
            violation = Violation(
                rule=rule_obj,
                violation_message=f'Story "{node.name}" lacks scenarios/scenario_outlines or acceptance criteria in story-graph.json - INVEST principle "Testable" requires clear testable outcomes',
                location=node.name,
                severity='warning'
            ).to_dict()
            violations.append(violation)
        
        # Small: Check sizing (already handled by StorySizingScanner, but we can add a reminder)
        # Independent: Hard to validate programmatically (requires dependency analysis)
        # Negotiable: Hard to validate programmatically
        # Valuable: Hard to validate programmatically
        # Estimable: Hard to validate programmatically (related to clarity)
        
        return violations

```

---

## keep_functions_small_focused
**noun_redundancy_scanner.py** - 1 violation(s)

[!] WARNING (line 12)
Function "scan_story_node" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

```python
class NounRedundancyScanner(StoryScanner):
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        if not hasattr(node, 'name') or not node.name:
            return violations
        
        name = node.name
        
        words = re.findall(r'\b[A-Z][a-z]+\b|\b[a-z]+\b', name)
        
        # This is a simplified check - full implementation would need parent context
        # For now, check if name has redundant patterns like "X Animation", "Y Animation"
        if len(words) >= 2:
            # This is a heuristic - full check needs sibling context
            pass
        
        if re.search(r'\d+|System|Component|Module|Manager|Handler', name, re.IGNORECASE):
            base_name = re.sub(r'\s+(System|Component|Module|Manager|Handler|\d+)$', '', name, flags=re.IGNORECASE)
            if base_name and base_name != name:
                violation = Violation(
                    rule=rule_obj,
                    violation_message=f'Story element "{name}" may have redundant noun - consider integrating with related concepts instead of using qualifiers',
                    location=node.name,
                    severity='warning'
                ).to_dict()
                violations.append(violation)
        
        return violations

```

---

## keep_functions_small_focused
**object_oriented_helpers_scanner.py** - 1 violation(s)

[!] WARNING (line 22)
Function "scan_file" is 42 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    HELPER_CALL_THRESHOLD = 2  # multiple given/when/then calls => likely fragmented

    def scan_file(self, file_path: Path, rule_obj: Any = None, story_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations: List[Dict[str, Any]] = []

        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations

        content, lines, tree = parsed

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith("test"):
                helper_used = self._uses_helper(node)
                param_count = self._count_params(node)
                parametrize_cols = self._parametrize_column_count(node)
                gwt_calls = self._given_when_then_calls(node)

                # Flag if heavy params or parametrize without OO helper
                if (param_count >= self.PARAM_THRESHOLD or parametrize_cols >= self.PARAMETRIZE_THRESHOLD) and not helper_used:
                    message = (
                        f'Test "{node.name}" has many parameters ({max(param_count, parametrize_cols)}) '
                        f"but no helper/factory usage - consolidate with BotTestHelper or shared helper object."
                    )
                    violations.append(
                        Violation(
                            rule=rule_obj,
                            violation_message=message,
                            line_number=node.lineno,
                            location=str(file_path),
                            severity="warning",
                        ).to_dict()
                    )

                # Flag if multiple given/when/then helpers (fragmented setup) and no OO helper present
                if gwt_calls >= self.HELPER_CALL_THRESHOLD and not helper_used:
                    message = (
                        f'Test "{node.name}" uses {gwt_calls} given/when/then helpers but no shared helper object; '
                        f"consolidate into BotTestHelper-style fixtures with standard data."
                    )
                    violations.append(
                        Violation(
                            rule=rule_obj,
                            violation_message=message,
                            line_number=node.lineno,
                            location=str(file_path),
                            severity="warning",
                        ).to_dict()
                    )

    # ... (truncated)
```

---

## keep_functions_small_focused
**parameterized_tests_scanner.py** - 1 violation(s)

[!] WARNING (line 9)
Function "scan" is 25 lines - should be under 20 lines (extract complex logic to helper functions)

```python
class ParameterizedTestsScanner(Scanner):
    
    def scan(
        self, 
        story_graph: Dict[str, Any], 
        rule_obj: Any = None,
        test_files: Optional[List['Path']] = None,
        code_files: Optional[List['Path']] = None,
        on_file_scanned: Optional[Any] = None
    ) -> List[Dict[str, Any]]:
        if not rule_obj:
            raise ValueError("rule_obj parameter is required for ParameterizedTestsScanner")
        
        violations = []
        story_map = StoryMap(story_graph)
        
        for epic in story_map.epics():
            for node in story_map.walk(epic):
                if isinstance(node, Story):
                    for scenario_outline in node.scenario_outlines:
                        if scenario_outline.examples_rows and len(scenario_outline.examples_rows) > 1:
                            location = scenario_outline.map_location()
                            violations.append(Violation(
                                rule=rule_obj,
                                violation_message=f"Scenario outline '{scenario_outline.name}' has {len(scenario_outline.examples_rows)} examples but may not use @pytest.mark.parametrize",
                                location=location,
                                severity='warning'
                            ).to_dict())
        
        return violations

```

---

## keep_functions_small_focused
**prefer_object_model_over_config_scanner.py** - 1 violation(s)

[!] WARNING (line 36)
Function "scan_file" is 36 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        ]
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, story_graph: Dict[str, Any] = None) -> List[Violation]:
        violations = []
        
        # Use self.rule_obj directly - let code fail if not set
        if not self.rule_obj:
            return violations
        
        # Store file_path for creating violations
        self.current_file_path = file_path
        
        # Read the file content
        if not file_path.exists():
            return violations
        
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception:
            return violations
        
        lines = content.split('\n')
        
        if self._is_exception_file(file_path):
            return violations
        
        for line_num, line in enumerate(lines, start=1):
            # Skip if line has explicit ignore comment
            if '# scanner ignore' in line or '# noqa' in line:
                continue
            
            if self._is_in_exception_context(lines, line_num):
                continue
            
            for pattern, description in self.config_access_patterns:
                if re.search(pattern, line):
                    violations.append(self._create_violation(
                        line_num,
                        f"{description}. Use object properties instead of accessing _config directly."
                    ))
            
            if re.search(self.config_file_pattern, line):
                # Only flag if it looks like we're reading config when an object might exist
                if self._looks_like_object_exists_context(lines, line_num):
                    violations.append(self._create_violation(
                        line_num,
                        "Reading config file directly when object model may exist. Use object properties instead."
                    ))
        
        return violations
    # ... (truncated)
```

---

## keep_functions_small_focused
**property_encapsulation_scanner.py** - 1 violation(s)

[!] WARNING (line 29)
Function "scan_domain_concept" is 30 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    ]
    
    def scan_domain_concept(self, node: DomainConceptNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        for i, responsibility_data in enumerate(node.responsibilities):
            responsibility_name = responsibility_data.get('name', '')
            resp_lower = responsibility_name.lower()
            
            for pattern in self.EXPOSED_STATE_PATTERNS:
                if re.search(pattern, resp_lower):
                    violations.append(
                        Violation(
                            rule=rule_obj,
                            violation_message=f'Responsibility "{responsibility_name}" exposes internal structure. Use property encapsulation instead (e.g., "Get holdings: Holdings" not "Get holdings list: List").',
                            location=node.map_location(f'responsibilities[{i}].name'),
                            line_number=None,
                            severity='warning'
                        ).to_dict()
                    )
                    break
            
            for pattern in self.CALCULATE_PATTERNS:
                if re.search(pattern, resp_lower):
                    violations.append(
                        Violation(
                            rule=rule_obj,
                            violation_message=f'Responsibility "{responsibility_name}" uses calculate/compute instead of property. Use "Get X" instead of "Calculate X" to hide calculation timing.',
                            location=node.map_location(f'responsibilities[{i}].name'),
                            line_number=None,
                            severity='warning'
                        ).to_dict()
                    )
                    break
        
        return violations

```

---

## keep_functions_small_focused
**resource_oriented_code_scanner.py** - 1 violation(s)

[!] WARNING (line 28)
Function "scan_cross_file" is 48 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return []
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
        test_files: Optional[List[Path]] = None,
        code_files: Optional[List[Path]] = None,
        all_test_files: Optional[List[Path]] = None,
        all_code_files: Optional[List[Path]] = None,
        status_writer: Optional[Any] = None,
        max_cross_file_comparisons: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        violations = []
        
        all_files = []
        if code_files:
            all_files.extend(code_files)
        if test_files:
            all_files.extend(test_files)
        
        if not all_files:
            return violations
        
        # First pass: collect all loader/manager classes and all classes
        loader_classes = {}  # class_name -> (file_path, class_node, pattern)
        all_classes = {}  # (file_path, class_name) -> class_node
        
        for file_path in all_files:
            if not file_path.exists():
                continue
            
            try:
                content = file_path.read_text(encoding='utf-8')
                tree = ast.parse(content, filename=str(file_path))
                
                classes = Classes(tree)
                for cls in classes.get_many_classes:
                    all_classes[(file_path, cls.node.name)] = cls.node
                    
                    # Check if class name is an agent noun using NLTK
                    is_agent, base_verb, suffix = VocabularyHelper.is_agent_noun(cls.node.name)
                    if is_agent:
                        loader_classes[cls.node.name] = (file_path, cls.node, suffix)
            except (SyntaxError, UnicodeDecodeError) as e:
                logger.debug(f'Skipping file {file_path} due to {type(e).__name__}: {e}')
                continue
        
        # Second pass: check if each agent noun class is owned by a domain object
        for loader_class_name, (loader_file, loader_node, suffix) in loader_classes.items():
            if not self._is_owned_by_domain_object(loader_class_name, loader_node, all_files, all_classes):
    # ... (truncated)
```

---

## keep_functions_small_focused
**scanner.py** - 1 violation(s)

[!] WARNING (line 18)
Function "scan" is 25 lines - should be under 20 lines (extract complex logic to helper functions)

```python
class Scanner(ABC):
    
    def scan(
        self, 
        story_graph: Dict[str, Any], 
        rule_obj: Any = None,
        test_files: Optional[List['Path']] = None,
        code_files: Optional[List['Path']] = None,
        on_file_scanned: Optional[Any] = None
    ) -> List[Dict[str, Any]]:
        violations = []
        
        # Combine all files - unified architecture
        all_files = []
        if test_files:
            all_files.extend(test_files)
        if code_files:
            all_files.extend(code_files)
        
        # Scan each file using unified scan_file() method
        for file_path in all_files:
            if file_path and file_path.exists() and file_path.is_file():
                file_violations = self.scan_file(file_path, rule_obj, story_graph)
                file_violations_list = file_violations if isinstance(file_violations, list) else [file_violations] if file_violations else []
                
                if file_violations_list:
                    violations.extend(file_violations_list)
                
                # Call callback immediately after each file is scanned
                if on_file_scanned:
                    on_file_scanned(file_path, file_violations_list, rule_obj)
        
        return violations
    
```

---

## keep_functions_small_focused
**scanner_registry.py** - 1 violation(s)

[!] WARNING (line 32)
Function "loads_scanner_class_with_error" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return scanner_class
    
    def loads_scanner_class_with_error(self, scanner_module_path: str) -> tuple[Optional[Type[Scanner]], Optional[str]]:
        if not scanner_module_path:
            return None, None
        
        try:
            module_path, class_name = scanner_module_path.rsplit('.', 1)
            
            scanner_name = re.sub(r'(?<!^)(?=[A-Z])', '_', class_name).lower().replace('_scanner', '').replace('scanner', '')
            
            paths_to_try = [
                module_path,  # Exact path from config
                f'agile_bot.src.scanners.{scanner_name}_scanner'
            ]
            
            if self._bot_name:
                paths_to_try.append(f'agile_bot.bots.{self._bot_name}.src.scanners.{scanner_name}_scanner')
            
            for path in paths_to_try:
                try:
                    module = importlib.import_module(path)
                    if hasattr(module, class_name):
                        scanner_class = getattr(module, class_name)
                        
                        if isinstance(scanner_class, type) and hasattr(scanner_class, 'scan'):
                            if issubclass(scanner_class, Scanner):
                                return scanner_class, None
                except (ImportError, AttributeError):
                    continue
            
            return None, f"Scanner class not found: {scanner_module_path}"
        except Exception as e:
            return None, f"Error loading scanner {scanner_module_path}: {e}"

```

---

## keep_functions_small_focused
**scanner_status_formatter.py** - 1 violation(s)

[i] INFO (line 26)
Function "categorize_scanner_rules" has deep nesting (depth=5) - should be under 4 levels. Extract nested logic to helper functions.

```python
        return lines

    def categorize_scanner_rules(self, validation_rules: List[Dict[str, Any]]) -> Dict:
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

## keep_functions_small_focused
**scenarios_cover_all_cases_scanner.py** - 1 violation(s)

[!] WARNING (line 12)
Function "scan_story_node" is 42 lines - should be under 20 lines (extract complex logic to helper functions)

```python
class ScenariosCoverAllCasesScanner(StoryScanner):
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        if isinstance(node, Story):
            story_data = node.data
            scenarios = story_data.get('scenarios', [])
            
            if len(scenarios) > 0:
                has_happy_path = False
                has_edge_case = False
                has_error_case = False
                
                for scenario_idx, scenario in enumerate(scenarios):
                    scenario_text = self._get_scenario_text(scenario)
                    
                    if self._is_happy_path(scenario_text):
                        has_happy_path = True
                    if self._is_edge_case(scenario_text):
                        has_edge_case = True
                    if self._is_error_case(scenario_text):
                        has_error_case = True
                
                if not has_happy_path:
                    violation = Violation(
                        rule=rule_obj,
                        violation_message='Story has no happy path scenario - add a scenario covering the normal success case',
                        location=node.map_location(),
                        severity='error'
                    ).to_dict()
                    violations.append(violation)
                
                if not has_edge_case and len(scenarios) > 1:
                    violation = Violation(
                        rule=rule_obj,
                        violation_message='Story has no edge case scenario - add scenarios covering boundary values and edge conditions',
                        location=node.map_location(),
                        severity='warning'
                    ).to_dict()
                    violations.append(violation)
                
                if not has_error_case and len(scenarios) > 1:
                    violation = Violation(
                        rule=rule_obj,
                        violation_message='Story has no error case scenario - add scenarios covering invalid inputs and error conditions',
                        location=node.map_location(),
                        severity='warning'
                    ).to_dict()
                    violations.append(violation)
    # ... (truncated)
```

---

## keep_functions_small_focused
**scenarios_on_story_docs_scanner.py** - 1 violation(s)

[!] WARNING (line 110)
Function "scan_story_node" is 24 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return super().scan(story_graph, rule_obj, test_files=test_files, code_files=code_files)
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        if isinstance(node, Story):
            # Skip stories not in scope (if scope is defined)
            if self._in_scope_story_names is not None:
                if node.name not in self._in_scope_story_names:
                    # Story is out of scope, skip validation
                    return violations
            
            story_data = node.data
            scenarios = story_data.get('scenarios', [])
            scenario_outlines = story_data.get('scenario_outlines', [])
            
            # Story is valid if it has EITHER scenarios OR scenario_outlines (not requiring both)
            has_scenarios = scenarios and len(scenarios) > 0
            has_scenario_outlines = scenario_outlines and len(scenario_outlines) > 0
            
            if not has_scenarios and not has_scenario_outlines:
                location = node.map_location()
                violation = Violation(
                    rule=rule_obj,
                    violation_message=f'Story "{node.name}" has no scenarios or scenario_outlines in story-graph.json - scenarios should be in JSON (scenarios or scenario_outlines fields)',
                    location=location,
                    severity='error'
                ).to_dict()
                violations.append(violation)
        
        return violations

```

---

## keep_functions_small_focused
**setup_similarity_scanner.py** - 1 violation(s)

[!] WARNING (line 25)
Function "scan" is 59 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    MIN_INTRA_DUP = 2  # within a single test

    def scan(
        self,
        story_graph: Dict[str, Any],
        rule_obj: Any = None,
        test_files: Optional[List["Path"]] = None,
        code_files: Optional[List["Path"]] = None,
        on_file_scanned: Optional[Any] = None,
    ) -> List[Dict[str, Any]]:
        violations: List[Dict[str, Any]] = []
        fingerprint_occurrences: Dict[Tuple[str, Tuple[str, ...]], List[Tuple[Path, int, str]]] = defaultdict(list)
        intra_duplicates: List[Dict[str, Any]] = []

        files = test_files or []
        for file_path in files:
            parsed = self._read_and_parse_file(file_path)
            if not parsed:
                continue
            content, lines, tree = parsed

            for func in [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name.startswith("test")]:
                payloads = self._collect_payloads(func)
                # Track intra-test duplicates
                per_func_counts: Dict[Tuple[str, Tuple[str, ...]], List[int]] = defaultdict(list)
                for fp, lineno in payloads:
                    per_func_counts[fp].append(lineno)
                    fingerprint_occurrences[fp].append((file_path, lineno, func.name))
                for fp, ln_list in per_func_counts.items():
                    if len(ln_list) >= self.MIN_INTRA_DUP:
                        first_line = sorted(ln_list)[0]
                        intra_duplicates.append(
                            Violation(
                                rule=rule_obj,
                                violation_message=(
                                    f'Test "{func.name}" builds {len(ln_list)} similar setup payloads; '
                                    f"centralize into a shared standard fixture/helper."
                                ),
                                line_number=first_line,
                                location=str(file_path),
                                severity="warning",
                            ).to_dict()
                        )

        # Cross-test reuse
        for fp, occs in fingerprint_occurrences.items():
            if len(occs) >= self.MIN_REUSE:
                keyset = fp[0]
                key_text = ", ".join(keyset.split(",")) if keyset else "keys"
                # Emit up to 5 locations for context
    # ... (truncated)
```

---

## keep_functions_small_focused
**standard_data_reuse_scanner.py** - 1 violation(s)

[!] WARNING (line 26)
Function "scan_file" is 47 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    }

    def scan_file(self, file_path: Path, rule_obj: Any = None, story_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations: List[Dict[str, Any]] = []

        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations

        content, lines, tree = parsed

        for func in [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name.startswith("test")]:
            dict_keysets = []
            for node in ast.walk(func):
                # Capture dict literals passed into calls or assigned
                dict_node = None
                if isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict):
                    dict_node = node.value
                elif isinstance(node, ast.Call):
                    for arg in list(node.args) + [kw.value for kw in node.keywords]:
                        if isinstance(arg, ast.Dict):
                            dict_node = arg
                            break

                if dict_node and self._dict_has_canonical_keys(dict_node):
                    keyset = self._dict_keyset(dict_node)
                    dict_keysets.append((keyset, node.lineno))
                    if not self._is_uppercase_constant(getattr(node, "targets", [])):
                        violations.append(
                            Violation(
                                rule=rule_obj,
                                violation_message="Inline dict with standard test data fields - reuse a shared standard data set (e.g., STANDARD_STATE) instead of recreating ad-hoc.",
                                line_number=node.lineno,
                                location=str(file_path),
                                severity="warning",
                            ).to_dict()
                        )

            # If multiple distinct keysets appear in same test, flag duplication/variation
            unique_keysets = {}
            for keyset, lineno in dict_keysets:
                unique_keysets.setdefault(keyset, []).append(lineno)
            if len(unique_keysets) > 1:
                lines = sorted({ln for lst in unique_keysets.values() for ln in lst})
                first_line = lines[0] if lines else func.lineno
                violations.append(
                    Violation(
                        rule=rule_obj,
                        violation_message="Test defines multiple ad-hoc data shapes for standard data fields; consolidate to a shared standard data set.",
                        line_number=first_line,
    # ... (truncated)
```

---

## keep_functions_small_focused
**story_enumeration_scanner.py** - 1 violation(s)

[!] WARNING (line 12)
Function "scan_story_node" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

```python
class StoryEnumerationScanner(StoryScanner):
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        if isinstance(node, Epic):
            epic_data = node.data
            
            estimated_stories = epic_data.get('estimated_stories')
            if estimated_stories:
                if isinstance(estimated_stories, str) and '~' in str(estimated_stories):
                    location = node.map_location('estimated_stories')
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Epic "{node.name}" uses "~{estimated_stories}" notation - all stories must be explicitly enumerated, not estimated',
                        location=location,
                        severity='error'
                    ).to_dict()
                    violations.append(violation)
            
            sub_epics = epic_data.get('sub_epics', [])
            for sub_epic_idx, sub_epic_data in enumerate(sub_epics):
                violation = self._check_sub_epic_stories(sub_epic_data, node, sub_epic_idx, rule_obj)
                if violation:
                    violations.append(violation)
        
        return violations
    
```

---

## keep_functions_small_focused
**story_map.py** - 1 violation(s)

[!] WARNING (line 35)
Function "map_location" has high cognitive complexity (22) - should be under 15. Reduce nesting and extract complex logic.

```python
        return self.data.get('name', '')
    
    def map_location(self, field: str = 'name') -> str:
        if isinstance(self, Epic):
            return f"epics[{self.epic_idx}].{field}"
        elif isinstance(self, SubEpic):
            if self.sub_epic_path:
                path_str = "".join([f".sub_epics[{idx}]" for idx in self.sub_epic_path])
                return f"epics[{self.epic_idx}]{path_str}.{field}"
            else:
                return f"epics[{self.epic_idx}].{field}"
        elif isinstance(self, Story):
            path_parts = [f"epics[{self.epic_idx}]"]
            if self.sub_epic_path:
                for idx in self.sub_epic_path:
                    path_parts.append(f"sub_epics[{idx}]")
            if self.story_group_idx is not None:
                path_parts.append(f"story_groups[{self.story_group_idx}]")
            path_parts.append(f"stories[{self.story_idx}]")
            path_parts.append(field)
            return ".".join(path_parts)
        return ""

```

---

## keep_functions_small_focused
**technical_abstraction_scanner.py** - 1 violation(s)

[!] WARNING (line 24)
Function "scan_domain_concept" is 31 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    ]
    
    def scan_domain_concept(self, node: DomainConceptNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        # Check if concept name is an agent noun related to technical operations
        is_agent, base_verb, suffix = VocabularyHelper.is_agent_noun(node.name)
        if is_agent and base_verb in ['save', 'load', 'store']:
            violations.append(
                Violation(
                    rule=rule_obj,
                    violation_message=f'Domain concept "{node.name}" separates technical abstraction (derived from verb "{base_verb}"). Keep technical details (saving, loading) as part of domain concepts instead.',
                    location=node.map_location('name'),
                    line_number=None,
                    severity='warning'
                ).to_dict()
            )
        
        # Check responsibilities for technical file operation patterns
        for i, responsibility_data in enumerate(node.responsibilities):
            responsibility_name = responsibility_data.get('name', '')
            resp_lower = responsibility_name.lower()
            for pattern in self.TECHNICAL_FILE_PATTERNS:
                if re.search(pattern, resp_lower):
                    violations.append(
                        Violation(
                            rule=rule_obj,
                            violation_message=f'Responsibility "{responsibility_name}" exposes technical abstraction. Stay at domain level (e.g., "Saves portfolio" not "Saves portfolio to file").',
                            location=node.map_location(f'responsibilities[{i}].name'),
                            line_number=None,
                            severity='warning'
                        ).to_dict()
                    )
                    break
        
        return violations

```

---

## keep_functions_small_focused
**technical_language_scanner.py** - 1 violation(s)

[!] WARNING (line 25)
Function "scan_story_node" is 26 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    ]
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        if not hasattr(node, 'name') or not node.name:
            return violations
        
        name_lower = node.name.lower()
        
        for verb in self.TECHNICAL_VERBS:
            if verb in name_lower:
                violation = Violation(
                    rule=rule_obj,
                    violation_message=f'Story element "{node.name}" uses technical implementation verb "{verb}" - use business language focusing on user experience',
                    location=node.name,
                    severity='error'
                ).to_dict()
                violations.append(violation)
                break
        
        for phrase in self.TECHNICAL_PHRASES:
            if phrase in name_lower:
                violation = Violation(
                    rule=rule_obj,
                    violation_message=f'Story element "{node.name}" uses technical implementation phrase "{phrase}" - focus on what user experiences, not how it\'s implemented',
                    location=node.name,
                    severity='error'
                ).to_dict()
                violations.append(violation)
                break
        
        return violations

```

---

## keep_functions_small_focused
**verb_noun_scanner.py** - 1 violation(s)

[!] WARNING (line 36)
Function "scan_story_node" is 28 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return []
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        name = node.name
        
        if not name:
            return violations
        
        node_type = self._get_node_type(node)
        
        violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
        if violation:
            violations.append(violation)
        
        violation = self._check_gerund_ending(name, node, node_type, rule_obj)
        if violation:
            violations.append(violation)
        
        violation = self._check_noun_verb_noun_pattern(name, node, node_type, rule_obj)
        if violation:
            violations.append(violation)
        
        violation = self._check_noun_verb_pattern(name, node, node_type, rule_obj)
        if violation:
            violations.append(violation)
        
        violation = self._check_actor_prefix(name, node, node_type, rule_obj)
        if violation:
            violations.append(violation)
        
        violation = self._check_noun_only(name, node, node_type, rule_obj)
        if violation:
            violations.append(violation)
        
        violation = self._check_third_person_singular(name, node, node_type, rule_obj)
        if violation:
            violations.append(violation)
        
        return violations
    
```

---

## keep_functions_small_focused
**vertical_slice_scanner.py** - 1 violation(s)

[!] WARNING (line 18)
Function "scan" is 24 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return violations
    
    def scan(
        self, 
        story_graph: Dict[str, Any], 
        rule_obj: Any = None,
        test_files: Optional[List['Path']] = None,
        code_files: Optional[List['Path']] = None,
        on_file_scanned: Optional[Any] = None
    ) -> List[Dict[str, Any]]:
        violations = []
        
        if not rule_obj:
            raise ValueError("rule_obj parameter is required")
        
        increments = story_graph.get('increments', [])
        
        for increment_idx, increment in enumerate(increments):
            increment_epics = increment.get('epics', [])
            
            if len(increment_epics) == 1:
                location = f"increments[{increment_idx}]"
                violation = Violation(
                    rule=rule_obj,
                    violation_message=f'Increment "{increment.get("name", f"Increment {increment_idx+1}")}" spans only 1 epic - increments should be vertical slices spanning multiple epics',
                    location=location,
                    severity='error'
                ).to_dict()
                violations.append(violation)
        
        return violations

```

---

## keep_functions_small_focused
**vocabulary_helper.py** - 2 violation(s)

[!] WARNING (line 74)
Function "is_agent_noun" has high cognitive complexity (20) - should be under 15. Reduce nesting and extract complex logic.

```python
    
    @staticmethod
    def is_agent_noun(word: str) -> tuple[bool, Optional[str], Optional[str]]:
        """
        Check if word is an agent noun (doer of action).
        Returns: (is_agent, base_verb, suffix) or (False, None, None)
        
        Examples:
            'Manager' -> (True, 'manage', 'er')
            'Processor' -> (True, 'process', 'or')
            'Portfolio' -> (False, None, None)
        """
        word_lower = word.lower()
        
        for suffix in VocabularyHelper.AGENT_SUFFIXES:
            if word_lower.endswith(suffix) and len(word_lower) > len(suffix) + 2:
                base = word_lower[:-len(suffix)]
                
                # Check if base is a verb
                if VocabularyHelper.is_verb(base):
                    return (True, base, suffix)
                
                # Check common irregular forms
                # manage -> manager, coordinate -> coordinator
                if suffix == 'er' or suffix == 'or':
                    # Try adding 'e' back
                    base_with_e = base + 'e'
                    if VocabularyHelper.is_verb(base_with_e):
                        return (True, base_with_e, suffix)
        
        return (False, None, None)
    
```

[!] WARNING (line 171)
Function "is_actor_or_role" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    
    @staticmethod
    def is_actor_or_role(word: str) -> bool:
        """
        Check if word represents an actor or role (person, system, agent).
        Uses WordNet to check if word is a hyponym of 'person' or 'system'.
        
        Examples:
            'customer' -> True (person who buys)
            'user' -> True (person who uses)
            'developer' -> True (person who develops)
            'system' -> True (computing system)
            'api' -> True (system interface)
            'order' -> False (not a person/system)
        """
        try:
            word_lower = word.lower()
            
            # Get all synsets for the word
            synsets = wn.synsets(word_lower)
            
            if not synsets:
                return False
            
            # Get hypernym paths for all synsets
            for synset in synsets:
                # Get all hypernyms (parent concepts)
                hypernyms = set()
                for path in synset.hypernym_paths():
                    hypernyms.update(path)
                
                # Check if any hypernym is 'person', 'user', 'system', or 'agent'
                for hypernym in hypernyms:
                    name = hypernym.name().split('.')[0]
                    if name in ['person', 'user', 'system', 'agent', 'entity', 'causal_agent']:
                        return True
            
            return False
        except Exception:
            return False
        
```

---

## keep_functions_small_focused
**json_scope.py** - 1 violation(s)

[!] WARNING (line 42)
Function "to_dict" is 30 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return self.scope.file_filter
    
    def to_dict(self) -> dict:
        """Convert Scope to dict with filtered content for panel display."""
        # Start with basic scope criteria
        result = {
            'type': self.scope.type.value,
            'filter': ', '.join(self.scope.value) if self.scope.value else '',
            'content': None,
            'graphLinks': []
        }
        
        # Add filtered content based on scope type
        if self.scope.type.value in ('story', 'showAll'):
            # Get filtered story graph
            story_graph = self.scope._get_story_graph_results()
            if story_graph:
                # Serialize story graph content (epics array)
                from agile_bot.src.story_graph.json_story_graph import JSONStoryGraph
                graph_adapter = JSONStoryGraph(story_graph)
                content = graph_adapter.to_dict().get('content', [])
                
                # Enrich content with test file links and document links
                # content is a dict with 'epics' key; keep the shape for the panel
                if content and 'epics' in content:
                    self._enrich_with_links(content['epics'], story_graph)
                    # keep as { 'epics': [...] } so scope_view can access content.epics
                    result['content'] = content
                else:
                    result['content'] = {'epics': []}
                
                # Add links to story map files if available
                if self.scope.bot_paths:
                    from pathlib import Path
                    docs_stories = self.scope.workspace_directory / 'docs' / 'stories'
                    story_map_file = docs_stories / 'story-map.md'
                    if story_map_file.exists():
                        result['graphLinks'].append({
                            'text': 'map',
                            'url': str(story_map_file)
                        })
        elif self.scope.type.value == 'files':
            # Get filtered file list
            files = self.scope._get_file_results()
            result['content'] = [{'path': str(f)} for f in files]
        
        return result
    
```

---

## keep_functions_small_focused
**markdown_scope.py** - 1 violation(s)

[!] WARNING (line 16)
Function "serialize" is 40 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        self.workspace_directory = workspace_directory or Path.cwd()
    
    def serialize(self) -> str:
        """Convert Scope to Markdown string - delegates to result domain adapters."""
        lines = []
        
        lines.append(self.format_header(2, "🎯 Scope"))
        lines.append("")
        
        # Display scope filter
        if self.scope.type.value == 'all':
            filter_display = "all (entire project)"
        else:
            filter_display = ', '.join(self.scope.value) if isinstance(self.scope.value, list) else str(self.scope.value) if self.scope.value else "all"
        
        lines.append(f"**🎯 Current Scope:** {filter_display}")
        lines.append("")
        
        # Get results from Scope and delegate to appropriate adapter
        results = self.scope.results
        
        if results is not None:
            # Check type and delegate
            from agile_bot.src.story_graph.story_graph import StoryGraph
            
            if isinstance(results, StoryGraph):
                # Delegate to MarkdownStoryGraph adapter
                from agile_bot.src.cli.adapter_factory import AdapterFactory
                story_graph_adapter = AdapterFactory.create(results, 'markdown')
                lines.append(story_graph_adapter.serialize())
            elif isinstance(results, list):
                # File list - format as markdown list
                if results:
                    for file_path in sorted(results):
                        try:
                            rel_path = file_path.relative_to(self.scope.workspace_directory)
                            lines.append(self.format_list_item(str(rel_path)))
                        except ValueError:
                            lines.append(self.format_list_item(str(file_path)))
                else:
                    lines.append("(no files found)")
        else:
            lines.append("(no scope set)")
        
        lines.append("")
        lines.append("To change scope (pick ONE - setting a new scope replaces the previous):")
        lines.append(self.format_list_item("`scope all` - Clear scope, work on entire project"))
        lines.append(self.format_list_item("`scope \"Story Name\"` - Filter by story (replaces any file scope)"))
        lines.append(self.format_list_item("`scope \"file:C:/path/to/**/*.py\"` - Filter by files (replaces any story scope)"))
        lines.append("")
    # ... (truncated)
```

---

## keep_functions_small_focused
**scope.py** - 4 violation(s)

[!] WARNING (line 41)
Function "filter_story_graph" is 60 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return node_name in self.search_terms
    
    def filter_story_graph(self, story_graph: Dict[str, Any]) -> Dict[str, Any]:
        """Filter story graph to only nodes matching this filter.
        
        Searches ALL levels (epics, sub-epics, nested sub-epics, stories) regardless of where the term appears.
        Recursively handles nested sub-epics at any depth.
        """
        if not self.search_terms and not self.increments:
            return story_graph
        
        all_filter_names = self.search_terms
        
        def name_matches(name: str) -> bool:
            return any(filter_name.lower() in name.lower() for filter_name in all_filter_names)
        
        def filter_sub_epic(sub_epic: Dict[str, Any]) -> Optional[Dict[str, Any]]:
            """Recursively filter a sub-epic and its nested sub-epics.
            
            Returns:
                Filtered sub-epic dict if it or any of its children match, None otherwise.
            """
            sub_epic_name = sub_epic.get('name', '')
            
            # Check if this sub-epic itself matches - if so, include entire sub-epic with all stories
            if name_matches(sub_epic_name):
                return sub_epic  # Include entire sub-epic if name matches
            
            # Check stories in story groups
            matching_story_groups = []
            for story_group in sub_epic.get('story_groups', []):
                matching_stories = []
                for story in story_group.get('stories', []):
                    if name_matches(story.get('name', '')):
                        matching_stories.append(story)
                
                if matching_stories:
                    matching_story_groups.append({
                        **story_group,
                        'stories': matching_stories
                    })
            
            # Check direct stories
            matching_direct_stories = []
            for story in sub_epic.get('stories', []):
                if name_matches(story.get('name', '')):
                    matching_direct_stories.append(story)
            
            # Recursively filter nested sub-epics
            filtered_nested_sub_epics = []
    # ... (truncated)
```

[!] WARNING (line 154)
Function "filter_files" is 42 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return False
    
    def filter_files(self, file_list: List[Path]) -> List[Path]:
        """Filter file list to only files matching this filter."""
        if not self.include_patterns and not self.exclude_patterns:
            return file_list
        
        from pathlib import PurePath
        filtered = []
        
        for file_path in file_list:
            file_str = str(file_path).replace('\\', '/')
            file_path_obj = PurePath(file_str)
            
            if self.include_patterns:
                matches_include = False
                for pattern in self.include_patterns:
                    pattern_normalized = pattern.replace('\\', '/')
                    try:
                        if (file_path_obj.match(pattern_normalized) or
                            file_path_obj.match(f'**/{pattern_normalized}') or
                            pattern_normalized in file_str):
                            matches_include = True
                            break
                    except (ValueError, TypeError):
                        if pattern_normalized in file_str:
                            matches_include = True
                            break
                
                if not matches_include:
                    continue
            
            if self.exclude_patterns:
                matches_exclude = False
                for pattern in self.exclude_patterns:
                    pattern_normalized = pattern.replace('\\', '/')
                    try:
                        if (file_path_obj.match(pattern_normalized) or
                            file_path_obj.match(f'**/{pattern_normalized}') or
                            pattern_normalized in file_str):
                            matches_exclude = True
                            break
                    except (ValueError, TypeError):
                        if pattern_normalized in file_str:
                            matches_exclude = True
                            break
                
                if matches_exclude:
                    continue
            
    # ... (truncated)
```

[!] WARNING (line 449)
Function "load" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        scope_file.write_text(json.dumps(self.to_dict(), indent=2))
    
    def load(self):
        """Load scope from scope.json file."""
        scope_file = self.workspace_directory / 'scope.json'
        
        if not scope_file.exists():
            return
        
        try:
            scope_data = json.loads(scope_file.read_text())
            
            if scope_data:
                # Update this instance from loaded data
                scope_type_str = scope_data.get('type', 'all')
                scope_type = ScopeType(scope_type_str)
                
                value = scope_data.get('value', [])
                if not isinstance(value, list):
                    value = [value] if value else []
                
                exclude = scope_data.get('exclude', [])
                if not isinstance(exclude, list):
                    exclude = [exclude] if exclude else []
                
                skiprule = scope_data.get('skiprule', [])
                if not isinstance(skiprule, list):
                    skiprule = [skiprule] if skiprule else []
                
                self.filter(scope_type, value, exclude, skiprule)
        except (json.JSONDecodeError, IOError, ValueError):
            pass
    
```

[!] WARNING (line 55)
Function "filter_sub_epic" is 35 lines - should be under 20 lines (extract complex logic to helper functions)

```python
            return any(filter_name.lower() in name.lower() for filter_name in all_filter_names)
        
        def filter_sub_epic(sub_epic: Dict[str, Any]) -> Optional[Dict[str, Any]]:
            """Recursively filter a sub-epic and its nested sub-epics.
            
            Returns:
                Filtered sub-epic dict if it or any of its children match, None otherwise.
            """
            sub_epic_name = sub_epic.get('name', '')
            
            # Check if this sub-epic itself matches - if so, include entire sub-epic with all stories
            if name_matches(sub_epic_name):
                return sub_epic  # Include entire sub-epic if name matches
            
            # Check stories in story groups
            matching_story_groups = []
            for story_group in sub_epic.get('story_groups', []):
                matching_stories = []
                for story in story_group.get('stories', []):
                    if name_matches(story.get('name', '')):
                        matching_stories.append(story)
                
                if matching_stories:
                    matching_story_groups.append({
                        **story_group,
                        'stories': matching_stories
                    })
            
            # Check direct stories
            matching_direct_stories = []
            for story in sub_epic.get('stories', []):
                if name_matches(story.get('name', '')):
                    matching_direct_stories.append(story)
            
            # Recursively filter nested sub-epics
            filtered_nested_sub_epics = []
            for nested_sub_epic in sub_epic.get('sub_epics', []):
                filtered_nested = filter_sub_epic(nested_sub_epic)
                if filtered_nested:
                    filtered_nested_sub_epics.append(filtered_nested)
            
            # If we have matches at any level, include this sub-epic
            if matching_story_groups or matching_direct_stories or filtered_nested_sub_epics:
                filtered_sub_epic = {**sub_epic}
                if matching_story_groups:
                    filtered_sub_epic['story_groups'] = matching_story_groups
                if matching_direct_stories:
                    filtered_sub_epic['stories'] = matching_direct_stories
                if filtered_nested_sub_epics:
                    filtered_sub_epic['sub_epics'] = filtered_nested_sub_epics
    # ... (truncated)
```

---

## keep_functions_small_focused
**scope_matcher.py** - 1 violation(s)

[!] WARNING (line 75)
Function "format_node_with_children" is 23 lines - should be under 20 lines (extract complex logic to helper functions)

```python


def format_node_with_children(node: Dict[str, Any], node_type: str, indent: int, use_emoji: bool = False) -> List[str]:
    """Format a node and its children recursively.
    
    Args:
        node: Node dictionary with name and children
        node_type: Type of node ('epic', 'sub epic', 'story')
        indent: Indentation level
        use_emoji: If True, use emoji formatting; if False, use bracket formatting
        
    Returns:
        List of formatted lines
    """
    lines = []
    prefix = "  " * indent
    name = node.get('name', 'Unknown')
    
    if use_emoji:
        emoji_map = {
            'epic': '🎯',
            'sub epic': '⚙️',
            'story': '📝'
        }
        emoji = emoji_map.get(node_type, '•')
        lines.append(f"{prefix}{emoji} {name}")
    else:
        lines.append(f"{prefix}[{node_type}] {name}")
    
    # Don't recurse into stories - stop at story level
    if node_type == 'story':
        return lines
    
    # Add sub_epics
    for sub_epic in node.get('sub_epics', []):
        lines.extend(format_node_with_children(sub_epic, 'sub epic', indent + 1, use_emoji))
    
    # Add stories from story_groups
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories', []):
            lines.extend(format_node_with_children(story, 'story', indent + 1, use_emoji))
    
    # Add direct stories (some structures have this)
    for story in node.get('stories', []):
        lines.extend(format_node_with_children(story, 'story', indent + 1, use_emoji))
    
    return lines

```

---

## keep_functions_small_focused
**tty_scope.py** - 1 violation(s)

[!] WARNING (line 21)
Function "serialize" is 38 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        self.scope = scope
    
    def serialize(self) -> str:
        """Convert Scope to TTY string - delegates to result domain adapters."""
        lines = []
        
        lines.append(self.add_bold("🎯 Scope"))
        
        # Display scope filter
        if self.scope.type.value == 'all':
            filter_display = "all (entire project)"
        else:
            filter_display = ', '.join(self.scope.value) if isinstance(self.scope.value, list) else str(self.scope.value) if self.scope.value else "all"
        
        lines.append(f"🎯 {self.add_bold('Current Scope:')} {filter_display}")
        lines.append("")
        
        # Get results from Scope and delegate to appropriate adapter
        results = self.scope.results
        
        if results is not None:
            # Check type and delegate
            from agile_bot.src.story_graph.story_graph import StoryGraph
            
            if isinstance(results, StoryGraph):
                # Delegate to TTYStoryGraph adapter
                from agile_bot.src.cli.adapter_factory import AdapterFactory
                storyGrapgAdapter = AdapterFactory.create(results, 'tty')
                lines.append(storyGrapgAdapter.serialize())
            elif isinstance(results, list):
                # File list - format as tree
                if results:
                    for file_path in sorted(results):
                        try:
                            rel_path = file_path.relative_to(self.scope.workspace_directory)
                            lines.append(f"  - {rel_path}")
                        except ValueError:
                            lines.append(f"  - {file_path}")
                else:
                    lines.append("  (no files found)")
        else:
            lines.append("  (no scope set)")
        
        lines.append("To change scope (pick ONE - setting a new scope replaces the previous):")
        lines.append("scope all                            # Clear scope, work on entire project")
        lines.append('scope "Story Name"                   # Filter by story (replaces any file scope)')
        lines.append('scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any story scope)')
        lines.append(self.subsection_separator())
        
        return '\n'.join(lines)
    # ... (truncated)
```

---

## keep_functions_small_focused
**markdown_story_graph.py** - 1 violation(s)

[!] WARNING (line 14)
Function "serialize" is 27 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        self.story_graph = story_graph
    
    def serialize(self) -> str:
        """Convert StoryGraph to Markdown string."""
        lines = []
        
        lines.append(self.format_header(2, "Story Graph"))
        lines.append("")
        
        lines.append(f"**Path:** `{self.story_graph.path}`")
        lines.append("")
        lines.append(f"**Epic Count:** {self.story_graph.epic_count}")
        lines.append("")
        
        features = []
        if self.story_graph.has_increments:
            features.append("Increments")
        if self.story_graph.has_domain_concepts:
            features.append("Domain Concepts")
        
        if features:
            lines.append(f"**Features:** {', '.join(features)}")
            lines.append("")
        
        # Show epic hierarchy
        content = self.story_graph.content
        if content and 'epics' in content:
            lines.append(self.format_header(3, "Epics"))
            lines.append("")
            
            for epic in content['epics']:
                epic_name = epic.get('name', 'Unknown')
                lines.append(f"- 🎯  **{epic_name}**")
                
                # Recursively show sub-epics and their stories
                for sub_epic in epic.get('sub_epics', []):
                    self._render_sub_epic(sub_epic, lines, indent_level=1)
                
                lines.append("")
        
        return ''.join(lines)
    
```

---

## keep_functions_small_focused
**tty_story_graph.py** - 1 violation(s)

[!] WARNING (line 39)
Function "serialize" is 24 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return self.story_graph.content
    
    def serialize(self) -> str:
        """Convert StoryGraph to TTY string."""
        lines = []
        
        lines.append(self.add_bold("Story Graph"))
        lines.append(f"Path: {self.story_graph.path}")
        lines.append(f"Epics: {self.story_graph.epic_count}")
        
        flags = []
        if self.story_graph.has_increments:
            flags.append("increments")
        if self.story_graph.has_domain_concepts:
            flags.append("domain concepts")
        
        if flags:
            lines.append(f"Features: {', '.join(flags)}")
        
        lines.append("")
        
        # Show epic hierarchy
        content = self.story_graph.content
        if content and 'epics' in content:
            lines.append(self.add_color("Epics:", 'cyan'))
            for epic in content['epics']:
                epic_name = epic.get('name', 'Unknown')
                lines.append(f"  🎯  {epic_name}")
                
                # Recursively show sub-epics and their stories
                for sub_epic in epic.get('sub_epics', []):
                    self._render_sub_epic(sub_epic, lines, indent_level=1)
        
        return '\n'.join(lines)
    
```

---

## keep_functions_small_focused
**build_action.py** - 1 violation(s)

[!] WARNING (line 197)
Function "inject_rules" is 41 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        instructions._data['base_instructions'] = new_instructions

    def inject_rules(self, instructions) -> None:
        validate_action = self.rules
        rules_obj = validate_action.rules
        rules_text = rules_obj.formatted_rules_digest()
        rules_data = validate_action.inject_behavior_specific_rules()
        all_rules = rules_data.get('validation_rules', [])
        
        # Get existing base_instructions (these are the CUSTOM INSTRUCTIONS - keep them FIRST)
        existing_instructions = instructions.get('base_instructions', [])
        new_instructions = []
        rules_section = []
        
        # Get schema path for placeholder replacement
        schema_path = self.behavior.bot_paths.workspace_directory / 'docs' / 'stories' / 'story-graph.json'
        
        # Keep ALL other instructions, replacing placeholders as we go
        for line in existing_instructions:
            if isinstance(line, str):
                # Replace {{rules}} - skip it here, will add rules section at the end
                if '{{rules}}' in line:
                    continue
                # Replace {{schema}} placeholder
                if '{{schema}}' in line:
                    line = line.replace('{{schema}}', f'**Schema:** Story graph template at `{schema_path}`')
                # Replace {{description}} placeholder
                if '{{description}}' in line:
                    line = line.replace('{{description}}', f'**Task:** Build {self.behavior.name} story graph from clarification and strategy data')
            # Keep all custom instructions
            new_instructions.append(line)
        
        # Prepare rules section to append at the END
        if rules_text != 'No validation rules found.':
            rules_lines = rules_text.split('\n')
            rules_section.extend(rules_lines)
        
        # Append rules section at the VERY END (after ALL custom instructions)
        if rules_section:
            # Strip trailing blank lines before adding rules
            while new_instructions and new_instructions[-1] == '':
                new_instructions.pop()
            new_instructions.append('')
            new_instructions.append('When building or adding to the story graph follow these rules,')
            new_instructions.extend(rules_section)
        
        # Replace base_instructions with: [custom instructions] + [rules at end]
        instructions._data['base_instructions'] = new_instructions
        instructions.set('rules', all_rules)
    
```

---

## keep_functions_small_focused
**requirements_clarifications.py** - 1 violation(s)

[!] WARNING (line 16)
Function "save" is 25 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        self.context = context

    def save(self):
        existing_data = self.load()
        # Get existing data for this behavior, or create new structure
        behavior_data = existing_data.get(self.behavior_name, {})
        existing_answers = behavior_data.get('key_questions', {}).get('answers', {})
        existing_evidence = behavior_data.get('evidence', {})
        existing_context = behavior_data.get('context')
        
        # Merge answers (new answers override existing)
        merged_answers = {**existing_answers, **self.key_questions_answered}
        
        # Get required evidence from guardrails
        required_evidence = self.required_context.evidence.evidence_list if self.required_context else []
        
        # Merge provided evidence (new evidence overrides existing)
        existing_provided = existing_evidence.get('provided', {}) if isinstance(existing_evidence, dict) else {}
        merged_provided = {**existing_provided, **self.evidence_provided}
        
        # Merge context - append new items to existing list
        final_context = existing_context or []
        if self.context is not None:
            if isinstance(self.context, list):
                # Append new context items to existing list
                final_context = final_context if isinstance(final_context, list) else []
                final_context.extend(self.context)
            else:
                # Handle legacy string context - convert to list
                final_context = final_context if isinstance(final_context, list) else []
                final_context.append(self.context)
        
        # New structure: evidence has 'required' and 'provided'
        new_data = {
            'key_questions': {
                'answers': merged_answers
            },
            'evidence': {
                'required': required_evidence,
                'provided': merged_provided
            },
            'context': final_context
        }
        merged_data = self.merge(existing_data, new_data, self.behavior_name)
        super().save(merged_data)

```

---

## keep_functions_small_focused
**tty_required_context.py** - 1 violation(s)

[!] WARNING (line 13)
Function "serialize" is 23 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        self.required_context = required_context
    
    def serialize(self) -> str:
        """Convert RequiredContext to TTY string."""
        lines = []
        
        # Display key questions
        key_questions = self.required_context.key_questions.questions
        if key_questions:
            lines.append("")
            lines.append(self.add_bold("Key Questions:"))
            if isinstance(key_questions, list):
                for question in key_questions:
                    lines.append(f"- {question}")
            elif isinstance(key_questions, dict):
                for question_key, question_text in key_questions.items():
                    lines.append(f"- {self.add_bold(f'{question_key}:')} {question_text}")
        
        # Display evidence requirements
        evidence_list = self.required_context.evidence.evidence_list
        if evidence_list:
            lines.append("")
            lines.append(self.add_bold("Evidence:"))
            if isinstance(evidence_list, list):
                # Show as comma-delimited list
                lines.append(', '.join(evidence_list))
            elif isinstance(evidence_list, dict):
                for evidence_key, evidence_desc in evidence_list.items():
                    lines.append(f"- {self.add_bold(f'{evidence_key}:')} {evidence_desc}")
        
        return '\n'.join(lines)
    
```

---

## keep_functions_small_focused
**tty_strategy.py** - 1 violation(s)

[!] WARNING (line 13)
Function "serialize" is 25 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        self.strategy = strategy
    
    def serialize(self) -> str:
        """Convert Strategy to TTY string."""
        lines = []
        
        # Display strategy criteria (decisions)
        strategy_criterias = self.strategy.strategy_criterias.strategy_criterias
        if strategy_criterias:
            lines.append("")
            lines.append(self.add_bold("Decisions:"))
            for criteria_key, criteria in strategy_criterias.items():
                lines.append("")
                question = criteria.question
                if question:
                    lines.append(f"{self.add_bold(f'{criteria_key}:')} {question}")
                else:
                    lines.append(self.add_bold(f"{criteria_key}:"))
                
                options = criteria.options
                if options:
                    for option in options:
                        lines.extend(self._format_option(option))
        
        # Display assumptions
        assumptions = self.strategy.assumptions.assumptions
        if assumptions:
            lines.append("")
            lines.append(self.add_bold("Assumptions:"))
            for assumption in assumptions:
                lines.append(f"- {assumption}")
        
        return '\n'.join(lines)
    
```

---

## keep_functions_small_focused
**render_config_loader.py** - 1 violation(s)

[!] WARNING (line 57)
Function "verify_synchronizer_class" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return config_entry

    def verify_synchronizer_class(self, synchronizer_class_path: str) -> None:
        module_path, class_name = synchronizer_class_path.rsplit('.', 1)
        possible_paths = [module_path, f'agile_bot.bots.{self.behavior.bot_name}.src.{module_path}', f'agile_bot.bots.{self.behavior.bot_name}.src.synchronizers.{module_path}']
        module = None
        for path in possible_paths:
            try:
                module = importlib.import_module(path)
                if hasattr(module, class_name):
                    break
                module = None
            except ImportError:
                continue
        
        # If module not found, skip verification (may be in test environment)
        if module is None:
            return
        
        synchronizer_class = getattr(module, class_name, None)
        if synchronizer_class is None:
            return
            
        has_render = hasattr(synchronizer_class, 'render')
        has_sync_methods = any((hasattr(synchronizer_class, method) for method in ['synchronize_outline', 'synchronize_increments', 'synchronize_exploration']))
        if not (has_render or has_sync_methods):
            raise ValueError(f'Synchronizer class {synchronizer_class_path} does not have required methods')

```

---

## keep_functions_small_focused
**json_strategy_action.py** - 1 violation(s)

[!] WARNING (line 66)
Function "to_dict" is 54 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return self.action.typical_assumptions
    
    def to_dict(self) -> dict:
        """Convert StrategyAction to dict."""
        # #region agent log
        import time
        with open(r'c:\dev\augmented-teams\.cursor\debug.log', 'a', encoding='utf-8') as f:
            f.write(json.dumps({'sessionId':'debug-session','runId':'initial','hypothesisId':'H1','location':'json_strategy_action.py:67','message':'to_dict called','data':{'behavior_name':self.action.behavior.name if self.action.behavior else None,'has_strategy':bool(self.action.strategy)},'timestamp':int(time.time()*1000)})+'\n')
        # #endregion
        
        result = {
            'action_name': self.action.action_name,
            'description': self.action.description,
            'order': self.action.order,
            'next_action': self.action.next_action,
            'workflow': self.action.workflow,
            'auto_confirm': self.action.auto_confirm,
            'skip_confirm': self.action.skip_confirm,
            'behavior': self.action.behavior.name if self.action.behavior else None,
        }
        
        # Add strategy-specific properties
        if self.action.strategy:
            # Get saved decisions from strategy.json
            from agile_bot.src.actions.strategy.strategy_decision import StrategyDecision
            saved_data = StrategyDecision.load_all(self.action.behavior.bot_paths)
            
            # #region agent log
            with open(r'c:\dev\augmented-teams\.cursor\debug.log', 'a', encoding='utf-8') as f:
                f.write(json.dumps({'sessionId':'debug-session','runId':'initial','hypothesisId':'H3,H4','location':'json_strategy_action.py:83','message':'loaded saved_data','data':{'saved_data_keys':list(saved_data.keys()) if saved_data else None,'saved_data':saved_data,'behavior_name':self.action.behavior.name},'timestamp':int(time.time()*1000)})+'\n')
            # #endregion
            
            behavior_data = saved_data.get(self.action.behavior.name, {}) if saved_data else {}
            saved_decisions = behavior_data.get('decisions', {})
            saved_assumptions = behavior_data.get('assumptions', [])
            
            # #region agent log
            with open(r'c:\dev\augmented-teams\.cursor\debug.log', 'a', encoding='utf-8') as f:
                f.write(json.dumps({'sessionId':'debug-session','runId':'initial','hypothesisId':'H3,H4','location':'json_strategy_action.py:93','message':'extracted behavior data','data':{'behavior_data':behavior_data,'saved_decisions':saved_decisions,'saved_assumptions':saved_assumptions},'timestamp':int(time.time()*1000)})+'\n')
            # #endregion
            
            # Convert strategy_criteria objects to dicts for JSON serialization
            serialized_criteria = {}
            
            # #region agent log
            with open(r'c:\dev\augmented-teams\.cursor\debug.log', 'a', encoding='utf-8') as f:
                f.write(json.dumps({'sessionId':'debug-session','runId':'initial','hypothesisId':'H2,H6','location':'json_strategy_action.py:102','message':'before serializing criteria','data':{'has_strategy_criteria':bool(self.action.strategy_criteria),'criteria_type':str(type(self.action.strategy_criteria)),'criteria_len':len(self.action.strategy_criteria) if self.action.strategy_criteria else 0},'timestamp':int(time.time()*1000)})+'\n')
            # #endregion
            
            if self.action.strategy_criteria:
    # ... (truncated)
```

---

## maintain_vertical_density
**utils.py** - 2 violation(s)

[i] INFO (line 131)
Function "build_test_class_link" is 71 lines - consider improving vertical density by declaring variables near usage

```python


def build_test_class_link(test_file: str, test_class: str, workspace_directory: Path, story_file_path: Optional[Path] = None) -> str:
    """
    Build link to test class with line number.
    
    Args:
        test_file: Name of test file (e.g., 'test_example.py')
        test_class: Name of test class (e.g., 'TestMyFeature')
        workspace_directory: Path to workspace directory
    # ... (truncated)
```

[i] INFO (line 204)
Function "build_test_method_link" is 71 lines - consider improving vertical density by declaring variables near usage

```python


def build_test_method_link(test_file: str, test_method: str, workspace_directory: Path, story_file_path: Optional[Path] = None) -> str:
    """
    Build link to test method with line number.
    
    Args:
        test_file: Name of test file (e.g., 'test_example.py')
        test_method: Name of test method (e.g., 'test_my_scenario')
        workspace_directory: Path to workspace directory
    # ... (truncated)
```

---

## maintain_vertical_density
**action.py** - 3 violation(s)

[i] INFO (line 433)
Function "_save_guardrails_if_provided" is 66 lines - consider improving vertical density by declaring variables near usage

```python
        return instructions
    
    def _save_guardrails_if_provided(self, context: ActionContext):
        """Save guardrails if provided in context parameters.
        
        This is common logic for all actions. Any action can receive and save guardrails:
        - Clarify action: answers, evidence
        - Strategy action: decisions, assumptions
        - Build action: build_config, decisions
        - etc.
    # ... (truncated)
```

[i] INFO (line 527)
Function "_load_all_saved_guardrails" is 95 lines - consider improving vertical density by declaring variables near usage

```python
        self._load_all_saved_guardrails(instructions)
    
    def _load_all_saved_guardrails(self, instructions):
        """Load all saved guardrail data (clarifications and strategy) for visibility on all pages.
        
        This ensures that once clarifications are answered or strategy decisions are made,
        they are visible on ALL pages (clarify, build, validate, render), not just their own page.
        """
        if not self.behavior:
            return
    # ... (truncated)
```

[i] INFO (line 696)
Function "_format_instructions_for_display" is 90 lines - consider improving vertical density by declaring variables near usage

```python
        pass
    
    def _format_instructions_for_display(self, instructions) -> str:
        """Template method: Format instructions for REPL display.
        
        Override in subclasses to customize display formatting.
        """
        # Use the proper interface to get instruction data
        instructions_dict = instructions.to_dict()
        output_lines = []
    # ... (truncated)
```

---

## maintain_vertical_density
**bot.py** - 5 violation(s)

[i] INFO (line 286)
Function "scope" is 161 lines - consider improving vertical density by declaring variables near usage

```python
            }
    
    def scope(self, scope_filter: Optional[str] = None):
        """Set or view the scope filter for the current workflow.
        
        AI AGENTS: This command requires COMPLETE folder paths. When you pass a directory path,
        you MUST include the ENTIRE folder structure from root or working area.
        
        Args:
            scope_filter: Complete folder path or story name to filter by, or None to view current scope
    # ... (truncated)
```

[i] INFO (line 501)
Function "next" is 56 lines - consider improving vertical density by declaring variables near usage

```python
        }

    def next(self) -> Dict[str, Any]:
        """Navigate to the next action in the current behavior workflow.
        
        Returns:
            Dict with navigation result (new position, message)
        """
        if not self.behaviors.current:
            return {
    # ... (truncated)
```

[i] INFO (line 606)
Function "execute" is 80 lines - consider improving vertical density by declaring variables near usage

```python
            }
    
    def execute(self, behavior_name: str, action_name: Optional[str] = None, params: Optional[Dict[str, Any]] = None) -> Any:
        """Execute a specific behavior.action and return instructions.
        
        Navigates to behavior/action and calls get_instructions() with optional parameters.
        
        Args:
            behavior_name: Name of the behavior to execute
            action_name: Name of the action to execute (optional, uses current action if None)
    # ... (truncated)
```

[i] INFO (line 687)
Function "save" is 79 lines - consider improving vertical density by declaring variables near usage

```python
            }
    
    def save(self, answers: Optional[Dict[str, str]] = None,
             evidence_provided: Optional[Dict[str, str]] = None,
             decisions: Optional[Dict[str, str]] = None,
             assumptions: Optional[List[str]] = None) -> Dict[str, Any]:
        """Save guardrail data (answers, evidence, decisions, assumptions) for current behavior.
        
        Args:
            answers: Question-answer pairs for clarification
    # ... (truncated)
```

[i] INFO (line 817)
Function "submit_instructions" is 72 lines - consider improving vertical density by declaring variables near usage

```python
            }
    
    def submit_instructions(self, instructions, behavior_name: str = None, action_name: str = None) -> Dict[str, Any]:
        """Submit given Instructions object to AI chat.
        
        Args:
            instructions: Instructions object with display_content to submit
            behavior_name: Optional behavior name (for reporting, will be inferred if not provided)
            action_name: Optional action name (for reporting, will be inferred if not provided)
            
    # ... (truncated)
```

---

## maintain_vertical_density
**cli_generator.py** - 2 violation(s)

[i] INFO (line 50)
Function "_create_shell_script" is 53 lines - consider improving vertical density by declaring variables near usage

```python
        return results
    
    def _create_shell_script(self) -> Path:
        """Create shell script (.sh) for Unix/Linux/Mac."""
        script_name = 'story_cli.sh' if self.bot_name == 'story_bot' else f'{self.bot_name}_cli.sh'
        script_file = self.workspace_root / 'agile_bot' / script_name
        
        script_content = f"""#!/bin/bash
# {self.bot_name.replace('_', ' ').title()} CLI Launcher (Unix/Linux/Mac)
#
    # ... (truncated)
```

[i] INFO (line 104)
Function "_create_powershell_script" is 52 lines - consider improving vertical density by declaring variables near usage

```python
        return script_file
    
    def _create_powershell_script(self) -> Path:
        """Create PowerShell script (.ps1) for Windows."""
        script_name = 'story_cli.ps1' if self.bot_name == 'story_bot' else f'{self.bot_name}_cli.ps1'
        script_file = self.workspace_root / 'agile_bot' / script_name
        
        script_content = f"""# {self.bot_name.replace('_', ' ').title()} CLI Launcher (Windows/PowerShell)
#
# Usage (for humans):
    # ... (truncated)
```

---

## maintain_vertical_density
**cli_main.py** - 1 violation(s)

[i] INFO (line 52)
Function "main" is 114 lines - consider improving vertical density by declaring variables near usage

```python
from agile_bot.src.cli.cli_session import CLISession

def main():
    bot_name = bot_directory.name
    workspace_directory = get_workspace_directory()
    bot_config_path = bot_directory / 'bot_config.json'
    
    if not bot_config_path.exists():
        print(f"ERROR: Bot config not found at {bot_config_path}", file=sys.stderr)
        sys.exit(1)
    # ... (truncated)
```

---

## maintain_vertical_density
**cli_session.py** - 2 violation(s)

[i] INFO (line 38)
Function "execute_command" is 402 lines - consider improving vertical density by declaring variables near usage

```python
        self.mode = mode
    
    def execute_command(self, command: str) -> CLICommandResponse:
        """
        Route command to Bot method, return command response.
        
        Command mappings:
        - "status" -> bot itself (serialized via TTYBot)
        - "scope" -> bot.scope -> Scope object (property)
        - "next" -> bot.next() -> NavigationResult object
    # ... (truncated)
```

[i] INFO (line 538)
Function "_handle_action_shortcut" is 81 lines - consider improving vertical density by declaring variables near usage

```python
        raise ValueError(f"Unknown command: {command}")
    
    def _handle_action_shortcut(self, action_name: str, args: str) -> Any:
        """Handle action shortcut commands (e.g., 'build', 'validate', 'rules').
        
        Routes to current behavior's action if action exists.
        For non-workflow actions (like 'rules'), directly executes and returns instructions.
        For workflow actions, navigates and shows instructions.
        Returns None if not an action shortcut (so caller can try other routing).
        """
    # ... (truncated)
```

---

## maintain_vertical_density
**markdown_help.py** - 1 violation(s)

[i] INFO (line 14)
Function "serialize" is 59 lines - consider improving vertical density by declaring variables near usage

```python
        self.help_obj = help_obj
    
    def serialize(self) -> str:
        """Convert Help to Markdown string - mirrors TTYHelp structure."""
        lines = []
        
        # Core Commands section
        lines.append(self.format_header(2, "Core Commands"))
        core = self.help_obj.commands.core
        lines.append(f"  {core.navigation_pattern}  - {core.description_full}")
    # ... (truncated)
```

---

## maintain_vertical_density
**tty_help.py** - 1 violation(s)

[i] INFO (line 20)
Function "serialize" is 60 lines - consider improving vertical density by declaring variables near usage

```python
        self.help_obj = help_obj
    
    def serialize(self) -> str:
        """Convert Help to TTY string - assembles all help sections."""
        lines = []
        
        # Core Commands section
        lines.append(self.add_color("Core Commands:", 'green'))
        core = self.help_obj.commands.core
        lines.append(f"  {core.navigation_pattern}  - {core.description_full}")
    # ... (truncated)
```

---

## maintain_vertical_density
**markdown_instructions.py** - 1 violation(s)

[i] INFO (line 14)
Function "serialize" is 240 lines - consider improving vertical density by declaring variables near usage

```python
        self.instructions = instructions
    
    def serialize(self) -> str:
        """Convert Instructions to Markdown string."""
        instructions_dict = self.instructions.to_dict()
        output_lines = []
        
        # SCOPE SECTION (only show if scope has actual filter values set, or is 'showAll')
        scope = self.instructions.scope
        # Check if scope has filter values (scope.value) - this determines if scope is "empty"
    # ... (truncated)
```

---

## maintain_vertical_density
**tty_instructions.py** - 1 violation(s)

[i] INFO (line 14)
Function "serialize" is 210 lines - consider improving vertical density by declaring variables near usage

```python
        self.instructions = instructions
    
    def serialize(self) -> str:
        """Convert Instructions to TTY string - assembles all instruction sections."""
        instructions_dict = self.instructions.to_dict()
        output_lines = []
        
        # BEHAVIOR INSTRUCTIONS SECTION
        behavior_metadata = instructions_dict.get('behavior_metadata', {})
        if behavior_metadata:
    # ... (truncated)
```

---

## maintain_vertical_density
**rules.py** - 2 violation(s)

[i] INFO (line 69)
Function "_get_files_for_validation" is 62 lines - consider improving vertical density by declaring variables near usage

```python
    
    @classmethod
    def _get_files_for_validation(cls, behavior, context: 'ValidateActionContext') -> Dict[str, List[Path]]:
        """Get files to validate based on behavior validation type and scope."""
        from agile_bot.src.actions.validate.file_discovery import FileDiscovery
        from agile_bot.src.scope import ScopeType
        from agile_bot.src.actions.validate.validation_type import ValidationType
        
        # Enforce story-graph-only behaviors to ignore file scopes entirely.
        validation_type = behavior.validation_type
    # ... (truncated)
```

[i] INFO (line 133)
Function "from_parameters" is 53 lines - consider improving vertical density by declaring variables near usage

```python
    
    @classmethod
    def from_parameters(cls, parameters: Dict[str, Any], behavior, bot_paths, callbacks: Optional[ValidationCallbacks] = None) -> 'ValidationContext':
        from agile_bot.src.actions.action_context import ValidateActionContext, Scope, ScopeType, FileFilter
        from agile_bot.src.bot.behavior import Behavior
        
        if isinstance(behavior, str):
            behavior = Behavior(name=behavior, bot_paths=bot_paths)
        
        scope = None
    # ... (truncated)
```

---

## maintain_vertical_density
**active_language_scanner.py** - 1 violation(s)

[i] INFO (line 41)
Function "_check_actor_in_name" is 90 lines - consider improving vertical density by declaring variables near usage

```python
        return violations
    
    def _check_actor_in_name(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        # Tokenize the name and check if first word is an actor/role
        words = name.split()
        if not words:
            return None
        
        first_word = words[0].lower()
        actor_index = 0
    # ... (truncated)
```

---

## maintain_vertical_density
**arrange_act_assert_scanner.py** - 2 violation(s)

[i] INFO (line 153)
Function "_validate_aaa_structure" is 59 lines - consider improving vertical density by declaring variables near usage

```python
        return None
    
    def _validate_aaa_structure(self, sections: Dict[str, List[ast.stmt]], test_node: ast.FunctionDef, 
                                file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        has_arrange = len(sections['arrange']) > 0
        has_act = len(sections['act']) > 0
        has_assert = len(sections['assert']) > 0
        
        # Also check comments/method names (fallback)
        test_lines = file_path.read_text(encoding='utf-8').split('\n')
    # ... (truncated)
```

[i] INFO (line 213)
Function "_validate_aaa_order" is 61 lines - consider improving vertical density by declaring variables near usage

```python
        return None
    
    def _validate_aaa_order(self, sections: Dict[str, List[ast.stmt]], test_node: ast.FunctionDef,
                           file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        arrange_lines = [stmt.lineno for stmt in sections['arrange'] if hasattr(stmt, 'lineno')]
        act_lines = [stmt.lineno for stmt in sections['act'] if hasattr(stmt, 'lineno')]
        assert_lines = [stmt.lineno for stmt in sections['assert'] if hasattr(stmt, 'lineno')]
        
        if not arrange_lines or not act_lines or not assert_lines:
            return None  # Missing sections handled elsewhere
    # ... (truncated)
```

---

## maintain_vertical_density
**bad_comments_scanner.py** - 2 violation(s)

[i] INFO (line 96)
Function "_is_actual_commented_code" is 81 lines - consider improving vertical density by declaring variables near usage

```python
            ).to_dict()
    
    def _is_actual_commented_code(self, comment_content: str, lines: List[str], line_num: int) -> bool:
        if not comment_content:
            return False
        
        # Check if there's production code immediately after this comment (within 2 lines)
        # If so, this is likely an explanatory comment, not commented-out code
        for i in range(1, min(3, len(lines) - line_num + 1)):
            if line_num + i - 1 < len(lines):
    # ... (truncated)
```

[i] INFO (line 219)
Function "_extract_comment_text" is 58 lines - consider improving vertical density by declaring variables near usage

```python
        return violations
    
    def _extract_comment_text(self, line: str) -> Optional[str]:
        in_single_quote = False
        in_double_quote = False
        in_triple_single = False
        in_triple_double = False
        escape_next = False
        
        i = 0
    # ... (truncated)
```

---

## maintain_vertical_density
**business_readable_test_names_scanner.py** - 1 violation(s)

[i] INFO (line 114)
Function "_check_business_readable" is 113 lines - consider improving vertical density by declaring variables near usage

```python
        return set(words)
    
    def _check_business_readable(self, test_name: str, file_path: Path, node: ast.FunctionDef, rule_obj: Any, domain_language: set) -> Optional[Dict[str, Any]]:
        name_without_prefix = test_name[5:] if test_name.startswith('test_') else test_name
        
        test_words = self._extract_words_from_text(name_without_prefix)
        
        # If ANY domain term matches, consider it business-readable and skip all technical jargon checks
        if domain_language and test_words:
            matching_domain_terms = test_words.intersection(domain_language)
    # ... (truncated)
```

---

## maintain_vertical_density
**class_based_organization_scanner.py** - 2 violation(s)

[i] INFO (line 132)
Function "_find_expected_scenario_name" is 123 lines - consider improving vertical density by declaring variables near usage

```python
        return None
    
    def _find_expected_scenario_name(self, method_name: str, story_graph: Dict[str, Any], class_name: str) -> Optional[str]:
        # Reconstruct full method name with 'test_' prefix for test_method field comparison
        full_method_name = f"test_{method_name}" if not method_name.startswith('test_') else method_name
        method_name_norm = self._normalize_name(method_name)
        
        story_name_from_class = class_name[4:] if class_name.startswith('Test') else class_name
        story_name_normalized = self._normalize_name(story_name_from_class)
        
    # ... (truncated)
```

[i] INFO (line 408)
Function "_find_sub_epic_for_method" is 64 lines - consider improving vertical density by declaring variables near usage

```python
        return sub_epics
    
    def _find_sub_epic_for_method(self, method_name: str, class_name: str, story_graph: Dict[str, Any]) -> Optional[str]:
        method_name_norm = self._normalize_name(method_name)
        story_name_from_class = class_name[4:] if class_name.startswith('Test') else class_name
        story_name_normalized = self._normalize_name(story_name_from_class)
        
        epics = story_graph.get('epics', [])
        
        for epic in epics:
    # ... (truncated)
```

---

## maintain_vertical_density
**class_size_scanner.py** - 1 violation(s)

[i] INFO (line 34)
Function "_check_class_size" is 56 lines - consider improving vertical density by declaring variables near usage

```python
        return violations
    
    def _check_class_size(self, class_node: ast.ClassDef, file_path: Path, rule_obj: Any, content: str) -> Optional[Dict[str, Any]]:
        violations = []
        
        # 1. Line count (existing check)
        if hasattr(class_node, 'end_lineno') and class_node.end_lineno:
            class_size = class_node.end_lineno - class_node.lineno + 1
        else:
            class_size = len(class_node.body) * 10
    # ... (truncated)
```

---

## maintain_vertical_density
**clear_parameters_scanner.py** - 1 violation(s)

[i] INFO (line 80)
Function "_check_parameters" is 56 lines - consider improving vertical density by declaring variables near usage

```python
        return False
    
    def _check_parameters(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any, domain_terms: set = None, content: str = None) -> Optional[Dict[str, Any]]:
        if domain_terms is None:
            domain_terms = set()
        
        # Allow more parameters for initialization functions (__init__)
        max_params = 7 if func_node.name == '__init__' else 5
        if len(func_node.args.args) > max_params:
            line_number = func_node.lineno if hasattr(func_node, 'lineno') else None
    # ... (truncated)
```

---

## maintain_vertical_density
**code_scanner.py** - 1 violation(s)

[i] INFO (line 44)
Function "_extract_domain_terms" is 106 lines - consider improving vertical density by declaring variables near usage

```python
        return []
    
    def _extract_domain_terms(self, story_graph: Dict[str, Any]) -> set:
        domain_terms = set()
        
        # These are domain concepts, not technical jargon
        common_domain_terms = {
            'json', 'data', 'param', 'params', 'parameter', 'parameters',
            'var', 'vars', 'variable', 'variables',
            'method', 'methods', 'class', 'classes', 'call', 'calls',
    # ... (truncated)
```

---

## maintain_vertical_density
**dead_code_scanner.py** - 1 violation(s)

[i] INFO (line 23)
Function "scan" is 84 lines - consider improving vertical density by declaring variables near usage

```python
    """Scanner for detecting dead/unused code."""
    
    def scan(
        self, 
        story_graph: Dict[str, Any], 
        rule_obj: Any = None,
        test_files: Optional[List[Path]] = None,
        code_files: Optional[List[Path]] = None,
        on_file_scanned: Optional[Any] = None
    ) -> List[Dict[str, Any]]:
    # ... (truncated)
```

---

## maintain_vertical_density
**dependency_chaining_code_scanner.py** - 1 violation(s)

[i] INFO (line 32)
Function "_check_dependency_chaining" is 68 lines - consider improving vertical density by declaring variables near usage

```python
        return violations
    
    def _check_dependency_chaining(self, class_node: ast.ClassDef, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        # Find __init__ method and collect constructor-injected parameters
        init_method = None
        init_params = []
        for node in ast.walk(class_node):
            if isinstance(node, ast.FunctionDef) and node.name == '__init__':
    # ... (truncated)
```

---

## maintain_vertical_density
**descriptive_function_names_scanner.py** - 1 violation(s)

[i] INFO (line 32)
Function "_check_descriptive_name" is 109 lines - consider improving vertical density by declaring variables near usage

```python
        return violations
    
    def _check_descriptive_name(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        func_name_lower = func_node.name.lower()
        func_name_original = func_node.name
        
        # Domain-specific terms that are acceptable (standard interface methods, common patterns)
        # These are well-known domain terms, not vague abbreviations
        acceptable_domain_terms = {
            'scan',  # Standard Scanner interface method
    # ... (truncated)
```

---

## maintain_vertical_density
**domain_language_code_scanner.py** - 1 violation(s)

[i] INFO (line 115)
Function "_check_function_domain_language" is 65 lines - consider improving vertical density by declaring variables near usage

```python
        return violations
    
    def _check_function_domain_language(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any,
                                      domain_terms: set, generic_names: set, 
                                      enclosing_class: Optional[str] = None) -> List[Dict[str, Any]]:
        violations = []
        func_name_lower = func_node.name.lower()
        
        # Skip generate/calculate check for builder/generator classes with domain prefix
        # e.g., MCPServerGenerator.generate_server() is legitimate
    # ... (truncated)
```

---

## maintain_vertical_density
**duplication_scanner.py** - 6 violation(s)

[i] INFO (line 108)
Function "scan_file" is 78 lines - consider improving vertical density by declaring variables near usage

```python
            logger.debug(f"Cache write failed for {file_path}: {e}")
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, story_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        _safe_print(f"[DuplicationScanner.scan_code_file] Called for: {file_path}")
        
        if not file_path.exists():
            _safe_print(f"[DuplicationScanner.scan_code_file] File does not exist: {file_path}")
            return violations
    # ... (truncated)
```

[i] INFO (line 335)
Function "_check_duplicate_code_blocks" is 292 lines - consider improving vertical density by declaring variables near usage

```python
        return False
    
    def _check_duplicate_code_blocks(self, functions: List[tuple], lines: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        all_blocks = []
        for func_tuple in functions:
            func_name, func_body, func_line, func_node, _ = func_tuple
            blocks = self._extract_code_blocks(func_node, func_line, func_name)
            all_blocks.extend(blocks)
    # ... (truncated)
```

[i] INFO (line 628)
Function "_extract_code_blocks" is 148 lines - consider improving vertical density by declaring variables near usage

```python
        return violations
    
    def _extract_code_blocks(self, func_node: ast.FunctionDef, func_start_line: int, func_name: str) -> List[Dict[str, Any]]:
        blocks = []
        MIN_NODES = 5  # Minimum AST nodes for a meaningful subtree
        MAX_NODES = 80  # Maximum nodes to avoid overly large blocks
        MIN_LINES = 5  # Minimum lines of code
        MAX_LINES = 20  # Maximum lines (goldilocks zone)
        
        # Skip blocks in test methods - test structure similarity is expected, not duplication
    # ... (truncated)
```

[i] INFO (line 1549)
Function "_log_violation_details" is 57 lines - consider improving vertical density by declaring variables near usage

```python
            return 0.7
    
    def _log_violation_details(self, file_path: Path, violations: List[Dict[str, Any]], lines: List[str]) -> None:
        if not violations:
            return
        
        # Log detailed violation information
        # Note: This can be verbose, but provides valuable debugging info
        
        _safe_print(f"\n[{file_path}] Found {len(violations)} duplication violation(s):")
    # ... (truncated)
```

[i] INFO (line 1607)
Function "_filter_files_by_package_proximity" is 75 lines - consider improving vertical density by declaring variables near usage

```python
        _safe_print("")  # Blank line after violations
    
    def _filter_files_by_package_proximity(
        self,
        changed_files: List[Path],
        all_files: List[Path],
        max_parent_levels: int = 3,
        max_files: int = 20
    ) -> List[Path]:
        """Filter all_files to only include files in nearby packages.
    # ... (truncated)
```

[i] INFO (line 1683)
Function "scan_cross_file" is 301 lines - consider improving vertical density by declaring variables near usage

```python
        return nearby_files
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
        test_files: Optional[List[Path]] = None,
        code_files: Optional[List[Path]] = None,
        all_test_files: Optional[List[Path]] = None,
        all_code_files: Optional[List[Path]] = None,
        status_writer: Optional[Any] = None,
    # ... (truncated)
```

---

## maintain_vertical_density
**excessive_guards_scanner.py** - 2 violation(s)

[i] INFO (line 123)
Function "_is_optional_config_check" is 53 lines - consider improving vertical density by declaring variables near usage

```python
        return defaults.get(message_key, f'Line {line_number}: Guard clause detected.')

    def _is_optional_config_check(self, guard_node: ast.If, source_lines: List[str]) -> bool:
        # File existence checks - only flag if NOT followed by creation logic
        test = guard_node.test
        if isinstance(test, ast.Call) and isinstance(test.func, ast.Attribute) and test.func.attr == 'exists':
            if self._is_followed_by_creation_logic(guard_node, source_lines):
                return True  # Has creation logic, so it's legitimate - don't flag
            # No creation logic - flag it
            return False
    # ... (truncated)
```

[i] INFO (line 226)
Function "_check_guard_pattern" is 62 lines - consider improving vertical density by declaring variables near usage

```python
        return False

    def _check_guard_pattern(self, guard_node: ast.If, file_path: Path, rule_obj: Any, source_lines: List[str], content: str) -> Optional[Dict[str, Any]]:
        test = guard_node.test
        
        # Skip file existence checks, optional config, hasattr(), early returns, etc.
        if self._is_optional_config_check(guard_node, source_lines):
            return None
        
        # None checks (if X is None:, if X is not None:)
    # ... (truncated)
```

---

## maintain_vertical_density
**function_size_scanner.py** - 1 violation(s)

[i] INFO (line 37)
Function "_check_function_size" is 110 lines - consider improving vertical density by declaring variables near usage

```python
        return violations
    
    def _check_function_size(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any, source_lines: List[str], content: str) -> Optional[Dict[str, Any]]:
        # Calculate function size (end_lineno - lineno + 1)
        if not hasattr(func_node, 'end_lineno') or not func_node.end_lineno:
            logger.debug(f'Function node missing end_lineno at {file_path}:{func_node.lineno}')
            return None
        
        func_start_line = func_node.lineno - 1  # Convert to 0-indexed
        func_end_line = func_node.end_lineno  # end_lineno is 1-indexed, exclusive
    # ... (truncated)
```

---

## maintain_vertical_density
**given_when_then_helpers_scanner.py** - 2 violation(s)

[i] INFO (line 149)
Function "_find_inline_code_blocks" is 74 lines - consider improving vertical density by declaring variables near usage

```python
        return None
    
    def _find_inline_code_blocks(self, test_node: ast.FunctionDef, test_body_lines: List[str],
                                 helper_functions: Set[str], tree: ast.AST) -> List[Tuple[int, int, List[str]]]:
        blocks = []
        current_block_start = None
        current_block_lines = []
        
        # test_body_lines includes the def line, so body starts at lineno + 1
        body_start_line = test_node.lineno
    # ... (truncated)
```

[i] INFO (line 251)
Function "scan_cross_file" is 55 lines - consider improving vertical density by declaring variables near usage

```python
        return None, [], False, 0
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
        test_files: Optional[List[Path]] = None,
        code_files: Optional[List[Path]] = None,
        all_test_files: Optional[List[Path]] = None,
        all_code_files: Optional[List[Path]] = None,
        status_writer: Optional[Any] = None,
    # ... (truncated)
```

---

## maintain_vertical_density
**import_placement_scanner.py** - 2 violation(s)

[i] INFO (line 123)
Function "_skip_try_import_error_block" is 53 lines - consider improving vertical density by declaring variables near usage

```python
        return stripped == 'try:' or stripped.startswith('try:')
    
    def _skip_try_import_error_block(self, lines: List[str], start_line: int) -> int:
        if start_line >= len(lines):
            return start_line
        
        try_line = lines[start_line]
        base_indent = len(try_line) - len(try_line.lstrip())
        
        # Start after the 'try:' line
    # ... (truncated)
```

[i] INFO (line 191)
Function "_check_import_placement" is 71 lines - consider improving vertical density by declaring variables near usage

```python
        return stripped.startswith('import ')
    
    def _check_import_placement(
        self, 
        lines: List[str], 
        import_section_end: int,
        file_path: Path, 
        rule_obj: Any
    ) -> List[Dict[str, Any]]:
        violations = []
    # ... (truncated)
```

---

## maintain_vertical_density
**intention_revealing_names_scanner.py** - 1 violation(s)

[i] INFO (line 68)
Function "_check_variable_names" is 59 lines - consider improving vertical density by declaring variables near usage

```python
        return violations
    
    def _check_variable_names(self, tree: ast.AST, file_path: Path, rule_obj: Any, content: str, domain_terms: set = None, docstring_ranges: List[tuple] = None) -> List[Dict[str, Any]]:
        violations = []
        
        if domain_terms is None:
            domain_terms = set()
        if docstring_ranges is None:
            docstring_ranges = []
        
    # ... (truncated)
```

---

## maintain_vertical_density
**meaningful_context_scanner.py** - 1 violation(s)

[i] INFO (line 65)
Function "_check_numbered_variables" is 77 lines - consider improving vertical density by declaring variables near usage

```python
        return violations
    
    def _check_numbered_variables(self, content: str, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        try:
            # Parse the file as AST to get actual variable names (AST automatically excludes comments and string literals)
            tree = ast.parse(content, filename=str(file_path))
            
            numbered_var_pattern = re.compile(r'^\w+\d+$')  # word followed by number (entire match)
    # ... (truncated)
```

---

## maintain_vertical_density
**no_guard_clauses_scanner.py** - 1 violation(s)

[i] INFO (line 30)
Function "_check_guard_clause_patterns" is 56 lines - consider improving vertical density by declaring variables near usage

```python
        return violations
    
    def _check_guard_clause_patterns(self, lines: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        guard_patterns = [
            (r'if\s+(not\s+)?\w+\.exists\(\):', 'File existence check - test should fail if file missing'),
            # Type checks (isinstance)
            (r'if\s+(not\s+)?isinstance\([^)]+\):', 'Type check guard clause - test should fail if wrong type'),
            # Attribute checks (hasattr)
    # ... (truncated)
```

---

## maintain_vertical_density
**one_concept_per_test_scanner.py** - 1 violation(s)

[i] INFO (line 35)
Function "_check_one_concept" is 74 lines - consider improving vertical density by declaring variables near usage

```python
        return violations
    
    def _check_one_concept(self, test_node: ast.FunctionDef, file_path: Path, content: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        violations = []
        
        # 1. Name pattern check (existing logic)
        test_name = test_node.name.lower()
        multi_concept_patterns = [
            r'\b(and|or|then|also|plus)\b',
            r'_(and|or|then|also|plus)_',
    # ... (truncated)
```

---

## maintain_vertical_density
**property_encapsulation_code_scanner.py** - 1 violation(s)

[i] INFO (line 30)
Function "_check_encapsulation" is 56 lines - consider improving vertical density by declaring variables near usage

```python
        return violations
    
    def _check_encapsulation(self, class_node: ast.ClassDef, content: str, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        class_source = ast.get_source_segment(content, class_node) or ''
        
        for node in ast.walk(class_node):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
    # ... (truncated)
```

---

## maintain_vertical_density
**real_implementations_scanner.py** - 2 violation(s)

[i] INFO (line 35)
Function "_check_test_methods_call_production_code" is 113 lines - consider improving vertical density by declaring variables near usage

```python
        return violations
    
    def _check_test_methods_call_production_code(
        self, content: str, lines: List[str], file_path: Path, rule_obj: Any, story_graph: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        violations = []
        
        try:
            tree = ast.parse(content, filename=str(file_path))
        except SyntaxError:
    # ... (truncated)
```

[i] INFO (line 291)
Function "_is_empty_or_todo_only" is 53 lines - consider improving vertical density by declaring variables near usage

```python
        return False
    
    def _is_empty_or_todo_only(self, method: ast.FunctionDef, source_lines: List[str]) -> bool:
        if not method.body:
            return True
        
        method_start = method.lineno - 1  # Convert to 0-indexed
        method_end = method.end_lineno if hasattr(method, 'end_lineno') else method_start + 50
        if method_start < len(source_lines):
            method_source = source_lines[method_start:method_end]
    # ... (truncated)
```

---

## maintain_vertical_density
**resource_oriented_code_scanner.py** - 2 violation(s)

[i] INFO (line 28)
Function "scan_cross_file" is 60 lines - consider improving vertical density by declaring variables near usage

```python
        return []
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
        test_files: Optional[List[Path]] = None,
        code_files: Optional[List[Path]] = None,
        all_test_files: Optional[List[Path]] = None,
        all_code_files: Optional[List[Path]] = None,
        status_writer: Optional[Any] = None,
    # ... (truncated)
```

[i] INFO (line 106)
Function "_class_uses_as_attribute" is 51 lines - consider improving vertical density by declaring variables near usage

```python
        return False
    
    def _class_uses_as_attribute(self, class_node: ast.ClassDef, loader_class_name: str, file_path: Path) -> bool:
        try:
            content = file_path.read_text(encoding='utf-8')
            # Simple check: see if loader class name appears in the file
            if loader_class_name not in content:
                return False
        except (UnicodeDecodeError, IOError):
            return False
    # ... (truncated)
```

---

## maintain_vertical_density
**separate_concerns_scanner.py** - 1 violation(s)

[i] INFO (line 33)
Function "_check_mixed_concerns" is 53 lines - consider improving vertical density by declaring variables near usage

```python
        return violations
    
    def _check_mixed_concerns(self, func_node: ast.FunctionDef, content: str, file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        from .complexity_metrics import ComplexityMetrics
        
        # Use ComplexityMetrics to detect responsibilities
        responsibilities = ComplexityMetrics.detect_responsibilities(func_node)
        
        if len(responsibilities) <= 1:
            # Single responsibility - no violation
    # ... (truncated)
```

---

## maintain_vertical_density
**setup_similarity_scanner.py** - 1 violation(s)

[i] INFO (line 25)
Function "scan" is 64 lines - consider improving vertical density by declaring variables near usage

```python
    MIN_INTRA_DUP = 2  # within a single test

    def scan(
        self,
        story_graph: Dict[str, Any],
        rule_obj: Any = None,
        test_files: Optional[List["Path"]] = None,
        code_files: Optional[List["Path"]] = None,
        on_file_scanned: Optional[Any] = None,
    ) -> List[Dict[str, Any]]:
    # ... (truncated)
```

---

## maintain_vertical_density
**single_responsibility_scanner.py** - 1 violation(s)

[i] INFO (line 66)
Function "_check_name_patterns" is 65 lines - consider improving vertical density by declaring variables near usage

```python
        return violations[0] if violations else None
    
    def _check_name_patterns(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        func_name = func_node.name.lower()
        
        action_verbs = [
            'validate', 'save', 'load', 'process', 'send', 'create', 'update', 'delete',
            'calculate', 'compute', 'transform', 'convert', 'parse', 'format', 'render',
            'execute', 'run', 'invoke', 'call', 'fetch', 'retrieve', 'store', 'write',
            'read', 'parse', 'build', 'generate', 'compile', 'extract', 'merge', 'split'
    # ... (truncated)
```

---

## maintain_vertical_density
**specification_match_scanner.py** - 2 violation(s)

[i] INFO (line 221)
Function "_extract_domain_terms" is 93 lines - consider improving vertical density by declaring variables near usage

```python
        return violations
    
    def _extract_domain_terms(self, story_graph: Dict[str, Any]) -> set:
        domain_terms = set()
        
        if not story_graph:
            return domain_terms
        
        epics = story_graph.get('epics', [])
        for epic in epics:
    # ... (truncated)
```

[i] INFO (line 418)
Function "_check_assertion_matches" is 59 lines - consider improving vertical density by declaring variables near usage

```python
        return violations
    
    def _check_assertion_matches(self, test_method: ast.FunctionDef, story: Dict[str, Any], 
                                 rule_obj: Any, file_path: Path) -> List[Dict[str, Any]]:
        violations = []
        
        acceptance_criteria = story.get('acceptance_criteria', [])
        if not acceptance_criteria:
            return violations
        
    # ... (truncated)
```

---

## maintain_vertical_density
**standard_data_reuse_scanner.py** - 1 violation(s)

[i] INFO (line 26)
Function "scan_file" is 54 lines - consider improving vertical density by declaring variables near usage

```python
    }

    def scan_file(self, file_path: Path, rule_obj: Any = None, story_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations: List[Dict[str, Any]] = []

        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations

        content, lines, tree = parsed
    # ... (truncated)
```

---

## maintain_vertical_density
**test_file_naming_scanner.py** - 1 violation(s)

[i] INFO (line 124)
Function "_find_sub_epic_for_method" is 64 lines - consider improving vertical density by declaring variables near usage

```python
        return sub_epics
    
    def _find_sub_epic_for_method(self, method_name: str, class_name: str, story_graph: Dict[str, Any]) -> Optional[str]:
        method_name_norm = self._to_snake_case(method_name)
        story_name_from_class = class_name[4:] if class_name.startswith('Test') else class_name
        story_name_normalized = self._to_snake_case(story_name_from_class)
        
        epics = story_graph.get('epics', [])
        
        for epic in epics:
    # ... (truncated)
```

---

## maintain_vertical_density
**verb_noun_scanner.py** - 3 violation(s)

[i] INFO (line 250)
Function "_check_noun_verb_pattern" is 82 lines - consider improving vertical density by declaring variables near usage

```python
        return None
    
    def _check_noun_verb_pattern(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        try:
            tokens, tags = self._get_tokens_and_tags(name)
            
            if len(tags) < 2:
                return None
            
            first_word = tags[0][0]
    # ... (truncated)
```

[i] INFO (line 333)
Function "_check_actor_prefix" is 76 lines - consider improving vertical density by declaring variables near usage

```python
        return None
    
    def _check_actor_prefix(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        name_lower = name.lower().strip()
        words = name_lower.split()
        
        if not words:
            return None
        
        first_word = words[0]
    # ... (truncated)
```

[i] INFO (line 410)
Function "_check_noun_only" is 167 lines - consider improving vertical density by declaring variables near usage

```python
        return None
    
    def _check_noun_only(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        try:
            tokens, tags = self._get_tokens_and_tags(name)
            
            if not tags:
                return None
            
            has_verb = any(self._is_verb(tag[1]) for tag in tags)
    # ... (truncated)
```

---

## maintain_vertical_density
**markdown_scope.py** - 1 violation(s)

[i] INFO (line 16)
Function "serialize" is 52 lines - consider improving vertical density by declaring variables near usage

```python
        self.workspace_directory = workspace_directory or Path.cwd()
    
    def serialize(self) -> str:
        """Convert Scope to Markdown string - delegates to result domain adapters."""
        lines = []
        
        lines.append(self.format_header(2, "🎯 Scope"))
        lines.append("")
        
        # Display scope filter
    # ... (truncated)
```

---

## maintain_vertical_density
**scope.py** - 3 violation(s)

[i] INFO (line 41)
Function "filter_story_graph" is 88 lines - consider improving vertical density by declaring variables near usage

```python
        return node_name in self.search_terms
    
    def filter_story_graph(self, story_graph: Dict[str, Any]) -> Dict[str, Any]:
        """Filter story graph to only nodes matching this filter.
        
        Searches ALL levels (epics, sub-epics, nested sub-epics, stories) regardless of where the term appears.
        Recursively handles nested sub-epics at any depth.
        """
        if not self.search_terms and not self.increments:
            return story_graph
    # ... (truncated)
```

[i] INFO (line 154)
Function "filter_files" is 51 lines - consider improving vertical density by declaring variables near usage

```python
        return False
    
    def filter_files(self, file_list: List[Path]) -> List[Path]:
        """Filter file list to only files matching this filter."""
        if not self.include_patterns and not self.exclude_patterns:
            return file_list
        
        from pathlib import PurePath
        filtered = []
        
    # ... (truncated)
```

[i] INFO (line 55)
Function "filter_sub_epic" is 51 lines - consider improving vertical density by declaring variables near usage

```python
            return any(filter_name.lower() in name.lower() for filter_name in all_filter_names)
        
        def filter_sub_epic(sub_epic: Dict[str, Any]) -> Optional[Dict[str, Any]]:
            """Recursively filter a sub-epic and its nested sub-epics.
            
            Returns:
                Filtered sub-epic dict if it or any of its children match, None otherwise.
            """
            sub_epic_name = sub_epic.get('name', '')
            
    # ... (truncated)
```

---

## maintain_vertical_density
**build_action.py** - 1 violation(s)

[i] INFO (line 115)
Function "_replace_schema_placeholders" is 81 lines - consider improving vertical density by declaring variables near usage

```python
        return behavior_to_content.get(self.behavior.name, [])
    
    def _replace_schema_placeholders(self, instructions) -> None:
        """Replace {{schema}} and {{description}} placeholders in base_instructions with template references."""
        base_instructions = instructions.get('base_instructions', [])
        new_instructions = []
        
        template = self.story_graph_template
        description_lines_list = []
        schema_explanation_lines = []
    # ... (truncated)
```

---

## maintain_vertical_density
**render_action.py** - 1 violation(s)

[i] INFO (line 43)
Function "_prepare_instructions" is 65 lines - consider improving vertical density by declaring variables near usage

```python
                    spec.mark_failed(str(e))
    
    def _prepare_instructions(self, instructions, context: ScopeActionContext):
        """Prepare render instructions with render specs and templates."""
        render_instructions = self._config_loader.load_render_instructions()
        render_specs = self._render_specs
        
        # Execute synchronizers during preparation
        self._execute_synchronizers(render_specs)
        
    # ... (truncated)
```

---

## maintain_vertical_density
**json_strategy_action.py** - 1 violation(s)

[i] INFO (line 66)
Function "to_dict" is 106 lines - consider improving vertical density by declaring variables near usage

```python
        return self.action.typical_assumptions
    
    def to_dict(self) -> dict:
        """Convert StrategyAction to dict."""
        # #region agent log
        import time
        with open(r'c:\dev\augmented-teams\.cursor\debug.log', 'a', encoding='utf-8') as f:
            f.write(json.dumps({'sessionId':'debug-session','runId':'initial','hypothesisId':'H1','location':'json_strategy_action.py:67','message':'to_dict called','data':{'behavior_name':self.action.behavior.name if self.action.behavior else None,'has_strategy':bool(self.action.strategy)},'timestamp':int(time.time()*1000)})+'\n')
        # #endregion
        
    # ... (truncated)
```

---

## maintain_vertical_density
**strategy_action.py** - 2 violation(s)

[i] INFO (line 35)
Function "_prepare_instructions" is 67 lines - consider improving vertical density by declaring variables near usage

```python
        return self.strategy.assumptions.assumptions
    
    def _prepare_instructions(self, instructions, context: StrategyActionContext):
        """Add strategy data (criteria, assumptions) and saved decisions to instructions.
        
        Note: Workflow instructions come from base_actions/strategy/action_config.json.
        This method adds only the behavior-specific data.
        """
        strategy_data = self.strategy.instructions
        
    # ... (truncated)
```

[i] INFO (line 103)
Function "_format_instructions_for_display" is 64 lines - consider improving vertical density by declaring variables near usage

```python
            pass  # Silently skip if can't load clarifications
    
    def _format_instructions_for_display(self, instructions) -> str:
        """Format strategy data for REPL display."""
        # Get base formatting first (includes scope warning if set)
        output_lines = super()._format_instructions_for_display(instructions).split('\n')
        
        # Get the instruction data
        instructions_dict = instructions.to_dict()
        
    # ... (truncated)
```

---

## maintain_vertical_density
**validate_action.py** - 1 violation(s)

[i] INFO (line 32)
Function "_prepare_instructions" is 71 lines - consider improving vertical density by declaring variables near usage

```python
        return self._rules

    def _prepare_instructions(self, instructions, context: ValidateActionContext):
        """Prepare validation instructions with rules and validation data."""
        # Get rules with file paths for AI to read
        rules_text = self._format_rules_with_file_paths()
        
        # Get story graph schema path
        schema_path = self.behavior.bot_paths.workspace_directory / 'docs' / 'stories' / 'story-graph.json'
        
    # ... (truncated)
```

---

## never_swallow_exceptions
**action.py** - 1 violation(s)

[X] ERROR (line 520)
Except block only contains pass at line 520 - exceptions must be logged or rethrown, never swallowed

```python
                    if 'guardrails' not in instructions._data:
                        instructions.set('guardrails', {'required_context': required_context.instructions})
        except Exception:
            # Silently skip if guardrails can't be loaded
            pass
    
```

---

## never_swallow_exceptions
**bot.py** - 1 violation(s)

[X] ERROR (line 805)
Except block only contains pass at line 805 - exceptions must be logged or rethrown, never swallowed

```python
                try:
                    self.execute(saved_behavior, saved_action)
                except:
                    pass  # Don't fail if restore doesn't work
            
```

---

## never_swallow_exceptions
**markdown_bot.py** - 1 violation(s)

[X] ERROR (line 136)
Except block only contains pass at line 136 - exceptions must be logged or rethrown, never swallowed

```python
                lines.append(markdown_scope.serialize())
                lines.append("")
            except (AttributeError, TypeError):
                pass
        
```

---

## never_swallow_exceptions
**workspace.py** - 1 violation(s)

[X] ERROR (line 59)
Except block only contains pass at line 59 - exceptions must be logged or rethrown, never swallowed

```python
                        path = python_workspace_root / base_actions_path
                    return path
            except Exception:
                pass  # Fall through to default
    
```

---

## never_swallow_exceptions
**cli_main.py** - 2 violation(s)

[X] ERROR (line 42)
Except block only contains pass at line 42 - exceptions must be logged or rethrown, never swallowed

```python
                if 'WORKING_AREA' in mcp_env:
                    os.environ['WORKING_AREA'] = mcp_env['WORKING_AREA']
        except:
            pass
    
```

[X] ERROR (line 147)
Except block only contains pass at line 147 - exceptions must be logged or rethrown, never swallowed

```python
                    response = cli_session.execute_command(command)
                    print(response.output, flush=True)
        except (KeyboardInterrupt, EOFError):
            pass
    elif is_piped:
```

---

## never_swallow_exceptions
**cli_session.py** - 1 violation(s)

[X] ERROR (line 665)
Except block only contains pass at line 665 - exceptions must be logged or rethrown, never swallowed

```python
                    print(f"Error: {e}", file=sys.stderr)
                    
        except KeyboardInterrupt:
            pass

```

---

## never_swallow_exceptions
**behavior_matcher.py** - 1 violation(s)

[X] ERROR (line 86)
Except block only contains pass at line 86 - exceptions must be logged or rethrown, never swallowed

```python
            if patterns:
                triggers[action_name] = patterns
        except FileNotFoundError:
            pass

```

---

## never_swallow_exceptions
**markdown_instructions.py** - 1 violation(s)

[X] ERROR (line 50)
Except block only contains pass at line 50 - exceptions must be logged or rethrown, never swallowed

```python
                    scope_content = adapter.serialize()
                    output_lines.append(scope_content)
                except Exception:
                    # Fallback: just show the filter value
                    pass
            
```

---

## never_swallow_exceptions
**verb_noun_scanner.py** - 1 violation(s)

[X] ERROR (line 572)
Except block only contains pass at line 572 - exceptions must be logged or rethrown, never swallowed

```python
                ).to_dict()
        
        except Exception:
            # NLTK POS tagging failed - return None to avoid false positives
            pass
        
```

---

## never_swallow_exceptions
**vocabulary_helper.py** - 3 violation(s)

[X] ERROR (line 22)
Except block only contains pass at line 22 - exceptions must be logged or rethrown, never swallowed

```python
    try:
        nltk.download('wordnet', quiet=True)
    except:
        pass  # Skip if download fails

```

[X] ERROR (line 30)
Except block only contains pass at line 30 - exceptions must be logged or rethrown, never swallowed

```python
    try:
        nltk.download('punkt_tab', quiet=True)
    except:
        pass  # Skip if download fails

```

[X] ERROR (line 38)
Except block only contains pass at line 38 - exceptions must be logged or rethrown, never swallowed

```python
    try:
        nltk.download('averaged_perceptron_tagger_eng', quiet=True)
    except:
        pass  # Skip if download fails

```

---

## never_swallow_exceptions
**scope.py** - 2 violation(s)

[X] ERROR (line 477)
Except block only contains pass at line 477 - exceptions must be logged or rethrown, never swallowed

```python
                
                self.filter(scope_type, value, exclude, skiprule)
        except (json.JSONDecodeError, IOError, ValueError):
            pass
    
```

[X] ERROR (line 498)
Except block only contains pass at line 498 - exceptions must be logged or rethrown, never swallowed

```python
                del state_data['scope']
                state_file.write_text(json.dumps(state_data, indent=2))
        except (json.JSONDecodeError, IOError):
            pass

```

---

## never_swallow_exceptions
**strategy_action.py** - 1 violation(s)

[X] ERROR (line 100)
Except block only contains pass at line 100 - exceptions must be logged or rethrown, never swallowed

```python
            if saved_clarifications and self.behavior.name in saved_clarifications:
                instructions.set('clarification', saved_clarifications[self.behavior.name])
        except Exception:
            pass  # Silently skip if can't load clarifications
    
```

---

## place_imports_at_top
**cli_main.py** - 8 violation(s)

[X] ERROR (line 10)
Import statement found after non-import code. Move all imports to the top of the file.

```python
"""

import sys
import os
```

[X] ERROR (line 11)
Import statement found after non-import code. Move all imports to the top of the file.

```python

import sys
import os
import json
```

[X] ERROR (line 12)
Import statement found after non-import code. Move all imports to the top of the file.

```python
import sys
import os
import json
from pathlib import Path
```

[X] ERROR (line 13)
Import statement found after non-import code. Move all imports to the top of the file.

```python
import os
import json
from pathlib import Path

```

[X] ERROR (line 16)
Import statement found after non-import code. Move all imports to the top of the file.

```python

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
```

[X] ERROR (line 48)
Import statement found after non-import code. Move all imports to the top of the file.

```python
        os.environ['WORKING_AREA'] = str(workspace_root)

from agile_bot.src.bot.bot import Bot
from agile_bot.src.bot.workspace import get_workspace_directory
```

[X] ERROR (line 49)
Import statement found after non-import code. Move all imports to the top of the file.

```python

from agile_bot.src.bot.bot import Bot
from agile_bot.src.bot.workspace import get_workspace_directory
from agile_bot.src.cli.cli_session import CLISession
```

[X] ERROR (line 50)
Import statement found after non-import code. Move all imports to the top of the file.

```python
from agile_bot.src.bot.bot import Bot
from agile_bot.src.bot.workspace import get_workspace_directory
from agile_bot.src.cli.cli_session import CLISession

```

---

## provide_meaningful_context
**adapters.py** - 1 violation(s)

[!] WARNING (line 56)
Line 56 contains magic number - replace with named constant

```python
        """Return light separator for subsections."""
        return "─" * 60
    
```

---

## provide_meaningful_context
**business_readable_test_names_scanner.py** - 7 violation(s)

[!] WARNING (line 269)
Line 269 uses numbered variable "start_line_0" - use meaningful descriptive name

```python
            # Use AST node to determine lines
            start_line_0 = ast_node.lineno - 1 if hasattr(ast_node, 'lineno') and ast_node.lineno else 0
            
```

[!] WARNING (line 272)
Line 272 uses numbered variable "end_line_0" - use meaningful descriptive name

```python
            if hasattr(ast_node, 'end_lineno') and ast_node.end_lineno:
                end_line_0 = ast_node.end_lineno  # end_lineno is 1-indexed, exclusive
            else:
```

[!] WARNING (line 275)
Line 275 uses numbered variable "end_line_0" - use meaningful descriptive name

```python
                # Estimate end by finding the maximum line number in the subtree
                end_line_0 = start_line_0 + 1
                for node in ast.walk(ast_node):
```

[!] WARNING (line 281)
Line 281 uses numbered variable "start_line_0" - use meaningful descriptive name

```python
            # Use provided line numbers (1-indexed, convert to 0-indexed)
            start_line_0 = start_line - 1
            if end_line is not None:
```

[!] WARNING (line 283)
Line 283 uses numbered variable "end_line_0" - use meaningful descriptive name

```python
            if end_line is not None:
                end_line_0 = end_line  # end_line is 1-indexed, exclusive (like end_lineno)
            else:
```

[!] WARNING (line 285)
Line 285 uses numbered variable "end_line_0" - use meaningful descriptive name

```python
            else:
                end_line_0 = start_line_0 + 1
        else:
```

[!] WARNING (line 278)
Line 278 uses numbered variable "end_line_0" - use meaningful descriptive name

```python
                    if hasattr(node, 'lineno') and node.lineno:
                        end_line_0 = max(end_line_0, node.lineno)
        elif start_line is not None:
```

---

## provide_meaningful_context
**class_based_organization_scanner.py** - 4 violation(s)

[!] WARNING (line 263)
Line 263 uses numbered variable "name1" - use meaningful descriptive name

```python
    
    def _names_match(self, name1: str, name2: str) -> bool:
        # Normalize: lowercase, remove spaces/punctuation
```

[!] WARNING (line 263)
Line 263 uses numbered variable "name2" - use meaningful descriptive name

```python
    
    def _names_match(self, name1: str, name2: str) -> bool:
        # Normalize: lowercase, remove spaces/punctuation
```

[!] WARNING (line 265)
Line 265 uses numbered variable "n1" - use meaningful descriptive name

```python
        # Normalize: lowercase, remove spaces/punctuation
        n1 = re.sub(r'[^\w]', '', name1.lower())
        n2 = re.sub(r'[^\w]', '', name2.lower())
```

[!] WARNING (line 266)
Line 266 uses numbered variable "n2" - use meaningful descriptive name

```python
        n1 = re.sub(r'[^\w]', '', name1.lower())
        n2 = re.sub(r'[^\w]', '', name2.lower())
        return n1 == n2
```

---

## provide_meaningful_context
**code_scanner.py** - 7 violation(s)

[!] WARNING (line 214)
Line 214 uses numbered variable "start_line_0" - use meaningful descriptive name

```python
            # Use AST node to determine lines
            start_line_0 = ast_node.lineno - 1 if hasattr(ast_node, 'lineno') and ast_node.lineno else 0
            
```

[!] WARNING (line 217)
Line 217 uses numbered variable "end_line_0" - use meaningful descriptive name

```python
            if hasattr(ast_node, 'end_lineno') and ast_node.end_lineno:
                end_line_0 = ast_node.end_lineno  # end_lineno is 1-indexed, exclusive
            else:
```

[!] WARNING (line 220)
Line 220 uses numbered variable "end_line_0" - use meaningful descriptive name

```python
                # Estimate end by finding the maximum line number in the subtree
                end_line_0 = start_line_0 + 1
                for node in ast.walk(ast_node):
```

[!] WARNING (line 226)
Line 226 uses numbered variable "start_line_0" - use meaningful descriptive name

```python
            # Use provided line numbers (1-indexed, convert to 0-indexed)
            start_line_0 = start_line - 1
            if end_line is not None:
```

[!] WARNING (line 228)
Line 228 uses numbered variable "end_line_0" - use meaningful descriptive name

```python
            if end_line is not None:
                end_line_0 = end_line  # end_line is 1-indexed, exclusive (like end_lineno)
            else:
```

[!] WARNING (line 230)
Line 230 uses numbered variable "end_line_0" - use meaningful descriptive name

```python
            else:
                end_line_0 = start_line_0 + 1
        else:
```

[!] WARNING (line 223)
Line 223 uses numbered variable "end_line_0" - use meaningful descriptive name

```python
                    if hasattr(node, 'lineno') and node.lineno:
                        end_line_0 = max(end_line_0, node.lineno)
        elif start_line is not None:
```

---

## provide_meaningful_context
**duplication_scanner.py** - 75 violation(s)

[!] WARNING (line 17)
Line 17 contains magic number - replace with named constant

```python
# Timeout for individual file scans (seconds)
FILE_SCAN_TIMEOUT = 60  # 60 seconds per file max

```

[!] WARNING (line 123)
Line 123 contains magic number - replace with named constant

```python
            if file_size > 500_000:  # Skip files larger than 500KB
                _safe_print(f"Skipping large file ({file_size/1024:.1f}KB): {file_path}")
                return violations
```

[!] WARNING (line 408)
Line 408 contains magic number - replace with named constant

```python
                    max_similarity = max(ast_similarity, content_similarity)
                elif max(ast_similarity, content_similarity) >= 0.90 and min(ast_similarity, content_similarity) >= 0.60:
                    max_similarity = max(ast_similarity, content_similarity)
```

[!] WARNING (line 604)
Line 604 contains magic number - replace with named constant

```python
                location = f"{block['func_name']}:{block['start_line']}-{block['end_line']}"
                preview = block['preview'][:200] + '...' if len(block['preview']) > 200 else block['preview']
                previews.append(f"Location ({location}):\n```python\n{preview}\n```")
```

[!] WARNING (line 942)
Line 942 contains magic number - replace with named constant

```python
        
        # If >= 60% are helper calls, consider it mostly helpers
        return (helper_count / total_count) >= 0.6
```

[!] WARNING (line 1754)
Line 1754 contains magic number - replace with named constant

```python
                if file_size > 500_000:  # Skip files larger than 500KB
                    _safe_print(f"Skipping large file ({file_size/1024:.1f}KB): {file_path}")
                    continue
```

[!] WARNING (line 1823)
Line 1823 contains magic number - replace with named constant

```python
                if file_size > 500_000:  # Skip files larger than 500KB
                    _safe_print(f"Skipping large file ({file_size/1024:.1f}KB): {file_path}")
                    continue
```

[!] WARNING (line 1229)
Line 1229 uses numbered variable "block1" - use meaningful descriptive name

```python
    
    def _operates_on_different_domains(self, block1: Dict[str, Any], block2: Dict[str, Any]) -> bool:
        domain_patterns1 = self._extract_domain_entities(block1)
```

[!] WARNING (line 1229)
Line 1229 uses numbered variable "block2" - use meaningful descriptive name

```python
    
    def _operates_on_different_domains(self, block1: Dict[str, Any], block2: Dict[str, Any]) -> bool:
        domain_patterns1 = self._extract_domain_entities(block1)
```

[!] WARNING (line 1362)
Line 1362 uses numbered variable "block1" - use meaningful descriptive name

```python
    
    def _compare_ast_blocks(self, block1: List[ast.stmt], block2: List[ast.stmt]) -> float:
        if len(block1) == 0 and len(block2) == 0:
```

[!] WARNING (line 1362)
Line 1362 uses numbered variable "block2" - use meaningful descriptive name

```python
    
    def _compare_ast_blocks(self, block1: List[ast.stmt], block2: List[ast.stmt]) -> float:
        if len(block1) == 0 and len(block2) == 0:
```

[!] WARNING (line 1380)
Line 1380 uses numbered variable "block1" - use meaningful descriptive name

```python
    
    def _compare_ast_structures(self, block1: List[ast.stmt], block2: List[ast.stmt]) -> float:
        if not block1 or not block2:
```

[!] WARNING (line 1380)
Line 1380 uses numbered variable "block2" - use meaningful descriptive name

```python
    
    def _compare_ast_structures(self, block1: List[ast.stmt], block2: List[ast.stmt]) -> float:
        if not block1 or not block2:
```

[!] WARNING (line 1400)
Line 1400 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_ast_nodes_deep(self, node1: ast.AST, node2: ast.AST) -> float:
        if type(node1) != type(node2):
```

[!] WARNING (line 1400)
Line 1400 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_ast_nodes_deep(self, node1: ast.AST, node2: ast.AST) -> float:
        if type(node1) != type(node2):
```

[!] WARNING (line 1434)
Line 1434 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_assign_nodes(self, node1: ast.Assign, node2: ast.Assign) -> float:
        # Compare number of targets
```

[!] WARNING (line 1434)
Line 1434 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_assign_nodes(self, node1: ast.Assign, node2: ast.Assign) -> float:
        # Compare number of targets
```

[!] WARNING (line 1443)
Line 1443 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_augassign_nodes(self, node1: ast.AugAssign, node2: ast.AugAssign) -> float:
        if type(node1.op) != type(node2.op):
```

[!] WARNING (line 1443)
Line 1443 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_augassign_nodes(self, node1: ast.AugAssign, node2: ast.AugAssign) -> float:
        if type(node1.op) != type(node2.op):
```

[!] WARNING (line 1448)
Line 1448 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_call_nodes(self, node1: ast.Call, node2: ast.Call) -> float:
        arg_count1 = len(node1.args) + len(node1.keywords)
```

[!] WARNING (line 1448)
Line 1448 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_call_nodes(self, node1: ast.Call, node2: ast.Call) -> float:
        arg_count1 = len(node1.args) + len(node1.keywords)
```

[!] WARNING (line 1466)
Line 1466 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_assert_nodes(self, node1: ast.Assert, node2: ast.Assert) -> float:
        test_sim = self._compare_expr_structure(node1.test, node2.test)
```

[!] WARNING (line 1466)
Line 1466 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_assert_nodes(self, node1: ast.Assert, node2: ast.Assert) -> float:
        test_sim = self._compare_expr_structure(node1.test, node2.test)
```

[!] WARNING (line 1470)
Line 1470 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_return_nodes(self, node1: ast.Return, node2: ast.Return) -> float:
        if node1.value is None and node2.value is None:
```

[!] WARNING (line 1470)
Line 1470 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_return_nodes(self, node1: ast.Return, node2: ast.Return) -> float:
        if node1.value is None and node2.value is None:
```

[!] WARNING (line 1477)
Line 1477 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_if_nodes(self, node1: ast.If, node2: ast.If) -> float:
        test_sim = self._compare_expr_structure(node1.test, node2.test)
```

[!] WARNING (line 1477)
Line 1477 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_if_nodes(self, node1: ast.If, node2: ast.If) -> float:
        test_sim = self._compare_expr_structure(node1.test, node2.test)
```

[!] WARNING (line 1483)
Line 1483 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_for_nodes(self, node1: ast.For, node2: ast.For) -> float:
        body_sim = self._compare_ast_structures(node1.body, node2.body)
```

[!] WARNING (line 1483)
Line 1483 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_for_nodes(self, node1: ast.For, node2: ast.For) -> float:
        body_sim = self._compare_ast_structures(node1.body, node2.body)
```

[!] WARNING (line 1488)
Line 1488 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_while_nodes(self, node1: ast.While, node2: ast.While) -> float:
        test_sim = self._compare_expr_structure(node1.test, node2.test)
```

[!] WARNING (line 1488)
Line 1488 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_while_nodes(self, node1: ast.While, node2: ast.While) -> float:
        test_sim = self._compare_expr_structure(node1.test, node2.test)
```

[!] WARNING (line 1493)
Line 1493 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_with_nodes(self, node1: ast.With, node2: ast.With) -> float:
        if len(node1.items) != len(node2.items):
```

[!] WARNING (line 1493)
Line 1493 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_with_nodes(self, node1: ast.With, node2: ast.With) -> float:
        if len(node1.items) != len(node2.items):
```

[!] WARNING (line 1499)
Line 1499 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_try_nodes(self, node1: ast.Try, node2: ast.Try) -> float:
        body_sim = self._compare_ast_structures(node1.body, node2.body)
```

[!] WARNING (line 1499)
Line 1499 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_try_nodes(self, node1: ast.Try, node2: ast.Try) -> float:
        body_sim = self._compare_ast_structures(node1.body, node2.body)
```

[!] WARNING (line 1506)
Line 1506 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_raise_nodes(self, node1: ast.Raise, node2: ast.Raise) -> float:
        if node1.exc is None and node2.exc is None:
```

[!] WARNING (line 1506)
Line 1506 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_raise_nodes(self, node1: ast.Raise, node2: ast.Raise) -> float:
        if node1.exc is None and node2.exc is None:
```

[!] WARNING (line 1513)
Line 1513 uses numbered variable "expr1" - use meaningful descriptive name

```python
    
    def _compare_expr_structure(self, expr1: ast.expr, expr2: ast.expr) -> float:
        if type(expr1) != type(expr2):
```

[!] WARNING (line 1513)
Line 1513 uses numbered variable "expr2" - use meaningful descriptive name

```python
    
    def _compare_expr_structure(self, expr1: ast.expr, expr2: ast.expr) -> float:
        if type(expr1) != type(expr2):
```

[!] WARNING (line 359)
Line 359 uses numbered variable "block1" - use meaningful descriptive name

```python
        compared_pairs = set()
        for i, block1 in enumerate(all_blocks):
            for j, block2 in enumerate(all_blocks[i+1:], start=i+1):
```

[!] WARNING (line 1230)
Line 1230 uses numbered variable "domain_patterns1" - use meaningful descriptive name

```python
    def _operates_on_different_domains(self, block1: Dict[str, Any], block2: Dict[str, Any]) -> bool:
        domain_patterns1 = self._extract_domain_entities(block1)
        domain_patterns2 = self._extract_domain_entities(block2)
```

[!] WARNING (line 1231)
Line 1231 uses numbered variable "domain_patterns2" - use meaningful descriptive name

```python
        domain_patterns1 = self._extract_domain_entities(block1)
        domain_patterns2 = self._extract_domain_entities(block2)
        
```

[!] WARNING (line 1254)
Line 1254 uses numbered variable "calls1" - use meaningful descriptive name

```python
    def _calls_different_methods(self, block1_nodes: List[ast.stmt], block2_nodes: List[ast.stmt]) -> bool:
        calls1 = self._extract_method_calls(block1_nodes)
        calls2 = self._extract_method_calls(block2_nodes)
```

[!] WARNING (line 1255)
Line 1255 uses numbered variable "calls2" - use meaningful descriptive name

```python
        calls1 = self._extract_method_calls(block1_nodes)
        calls2 = self._extract_method_calls(block2_nodes)
        
```

[!] WARNING (line 1374)
Line 1374 uses numbered variable "node1" - use meaningful descriptive name

```python
        similarities = []
        for node1, node2 in zip(block1, block2):
            similarity = self._compare_ast_nodes_deep(node1, node2)
```

[!] WARNING (line 1374)
Line 1374 uses numbered variable "node2" - use meaningful descriptive name

```python
        similarities = []
        for node1, node2 in zip(block1, block2):
            similarity = self._compare_ast_nodes_deep(node1, node2)
```

[!] WARNING (line 1385)
Line 1385 uses numbered variable "node1" - use meaningful descriptive name

```python
        similarities = []
        for node1 in block1:
            best_match = 0.0
```

[!] WARNING (line 1449)
Line 1449 uses numbered variable "arg_count1" - use meaningful descriptive name

```python
    def _compare_call_nodes(self, node1: ast.Call, node2: ast.Call) -> float:
        arg_count1 = len(node1.args) + len(node1.keywords)
        arg_count2 = len(node2.args) + len(node2.keywords)
```

[!] WARNING (line 1450)
Line 1450 uses numbered variable "arg_count2" - use meaningful descriptive name

```python
        arg_count1 = len(node1.args) + len(node1.keywords)
        arg_count2 = len(node2.args) + len(node2.keywords)
        
```

[!] WARNING (line 1459)
Line 1459 uses numbered variable "a1" - use meaningful descriptive name

```python
        arg_sims = []
        for a1, a2 in zip(node1.args, node2.args):
            arg_sims.append(self._compare_expr_structure(a1, a2))
```

[!] WARNING (line 1459)
Line 1459 uses numbered variable "a2" - use meaningful descriptive name

```python
        arg_sims = []
        for a1, a2 in zip(node1.args, node2.args):
            arg_sims.append(self._compare_expr_structure(a1, a2))
```

[!] WARNING (line 1885)
Line 1885 uses numbered variable "block1" - use meaningful descriptive name

```python
        # Compare each changed block against all blocks
        for i, block1 in enumerate(changed_blocks):
            for j, block2 in enumerate(all_blocks):
```

[!] WARNING (line 360)
Line 360 uses numbered variable "block2" - use meaningful descriptive name

```python
        for i, block1 in enumerate(all_blocks):
            for j, block2 in enumerate(all_blocks[i+1:], start=i+1):
                # Skip if same block
```

[!] WARNING (line 1263)
Line 1263 uses numbered variable "method_names1" - use meaningful descriptive name

```python
        if len(calls1) == len(calls2) and len(calls1) >= 2:
            method_names1 = {call for call in calls1}
            method_names2 = {call for call in calls2}
```

[!] WARNING (line 1264)
Line 1264 uses numbered variable "method_names2" - use meaningful descriptive name

```python
            method_names1 = {call for call in calls1}
            method_names2 = {call for call in calls2}
            
```

[!] WARNING (line 1387)
Line 1387 uses numbered variable "node2" - use meaningful descriptive name

```python
            best_match = 0.0
            for node2 in block2:
                similarity = self._compare_ast_nodes_deep(node1, node2)
```

[!] WARNING (line 1886)
Line 1886 uses numbered variable "block2" - use meaningful descriptive name

```python
        for i, block1 in enumerate(changed_blocks):
            for j, block2 in enumerate(all_blocks):
                # Skip if same file (within-file duplication already checked in scan_file)
```

[!] WARNING (line 1238)
Line 1238 uses numbered variable "func1" - use meaningful descriptive name

```python
                # If so, this is likely legitimate - each domain needs its own handlers
                func1 = block1['func_name']
                func2 = block2['func_name']
```

[!] WARNING (line 1239)
Line 1239 uses numbered variable "func2" - use meaningful descriptive name

```python
                func1 = block1['func_name']
                func2 = block2['func_name']
                if abs(len(func1) - len(func2)) <= 3:  # Similar length names
```

[!] WARNING (line 519)
Line 519 uses numbered variable "block1" - use meaningful descriptive name

```python
                    overlaps = False
                    for block1 in group_blocks:
                        for block2 in other_blocks:
```

[!] WARNING (line 1938)
Line 1938 uses numbered variable "file1" - use meaningful descriptive name

```python
                    # Found duplicate across files
                    file1 = block1['file_path']
                    file2 = block2['file_path']
```

[!] WARNING (line 1939)
Line 1939 uses numbered variable "file2" - use meaningful descriptive name

```python
                    file1 = block1['file_path']
                    file2 = block2['file_path']
                    func1 = block1['func_name']
```

[!] WARNING (line 1940)
Line 1940 uses numbered variable "func1" - use meaningful descriptive name

```python
                    file2 = block2['file_path']
                    func1 = block1['func_name']
                    func2 = block2['func_name']
```

[!] WARNING (line 1941)
Line 1941 uses numbered variable "func2" - use meaningful descriptive name

```python
                    func1 = block1['func_name']
                    func2 = block2['func_name']
                    start1 = block1['start_line']
```

[!] WARNING (line 1942)
Line 1942 uses numbered variable "start1" - use meaningful descriptive name

```python
                    func2 = block2['func_name']
                    start1 = block1['start_line']
                    end1 = block1['end_line']
```

[!] WARNING (line 1943)
Line 1943 uses numbered variable "end1" - use meaningful descriptive name

```python
                    start1 = block1['start_line']
                    end1 = block1['end_line']
                    start2 = block2['start_line']
```

[!] WARNING (line 1944)
Line 1944 uses numbered variable "start2" - use meaningful descriptive name

```python
                    end1 = block1['end_line']
                    start2 = block2['start_line']
                    end2 = block2['end_line']
```

[!] WARNING (line 1945)
Line 1945 uses numbered variable "end2" - use meaningful descriptive name

```python
                    start2 = block2['start_line']
                    end2 = block2['end_line']
                    
```

[!] WARNING (line 1947)
Line 1947 uses numbered variable "preview1" - use meaningful descriptive name

```python
                    
                    preview1 = block1['preview']
                    preview2 = block2['preview']
```

[!] WARNING (line 1948)
Line 1948 uses numbered variable "preview2" - use meaningful descriptive name

```python
                    preview1 = block1['preview']
                    preview2 = block2['preview']
                    
```

[!] WARNING (line 1956)
Line 1956 uses numbered variable "location1" - use meaningful descriptive name

```python
                    
                    location1 = f"{file1.name}:{func1} (lines {start1}-{end1})"
                    location2 = f"{file2.name}:{func2} (lines {start2}-{end2})"
```

[!] WARNING (line 1957)
Line 1957 uses numbered variable "location2" - use meaningful descriptive name

```python
                    location1 = f"{file1.name}:{func1} (lines {start1}-{end1})"
                    location2 = f"{file2.name}:{func2} (lines {start2}-{end2})"
                    
```

[!] WARNING (line 520)
Line 520 uses numbered variable "block2" - use meaningful descriptive name

```python
                    for block1 in group_blocks:
                        for block2 in other_blocks:
                            if (block1['func_name'] == block2['func_name'] and
```

[!] WARNING (line 1952)
Line 1952 uses numbered variable "preview1" - use meaningful descriptive name

```python
                    if len(preview1) > 300:
                        preview1 = preview1[:300] + '...'
                    if len(preview2) > 300:
```

[!] WARNING (line 1954)
Line 1954 uses numbered variable "preview2" - use meaningful descriptive name

```python
                    if len(preview2) > 300:
                        preview2 = preview2[:300] + '...'
                    
```

---

## provide_meaningful_context
**meaningful_context_scanner.py** - 3 violation(s)

[!] WARNING (line 37)
Line 37 contains magic number - replace with named constant

```python
        magic_number_patterns = [
            r'\b(200|404|500)\b',  # HTTP status codes
            r'\b(86400|3600|60)\b',  # Time constants (seconds in day/hour/minute)
```

[!] WARNING (line 38)
Line 38 contains magic number - replace with named constant

```python
            r'\b(200|404|500)\b',  # HTTP status codes
            r'\b(86400|3600|60)\b',  # Time constants (seconds in day/hour/minute)
            r'\b(1024|2048|4096)\b',  # Size constants
```

[!] WARNING (line 39)
Line 39 contains magic number - replace with named constant

```python
            r'\b(86400|3600|60)\b',  # Time constants (seconds in day/hour/minute)
            r'\b(1024|2048|4096)\b',  # Size constants
        ]
```

---

## provide_meaningful_context
**scanner_status_formatter.py** - 1 violation(s)

[!] WARNING (line 5)
Line 5 contains magic number - replace with named constant

```python

MAX_VIOLATION_DENSITY_FOR_GOOD_STATUS = 200
MAX_RULES_WITH_ERRORS_FOR_GOOD_STATUS = 5
```

---

## provide_meaningful_context
**separate_concerns_scanner.py** - 2 violation(s)

[!] WARNING (line 53)
Line 53 uses numbered variable "resp1" - use meaningful descriptive name

```python
        responsibility_set = set(responsibilities)
        for resp1, resp2 in incompatible_pairs:
            if resp1 in responsibility_set and resp2 in responsibility_set:
```

[!] WARNING (line 53)
Line 53 uses numbered variable "resp2" - use meaningful descriptive name

```python
        responsibility_set = set(responsibilities)
        for resp1, resp2 in incompatible_pairs:
            if resp1 in responsibility_set and resp2 in responsibility_set:
```

---

## provide_meaningful_context
**single_responsibility_scanner.py** - 2 violation(s)

[!] WARNING (line 105)
Line 105 uses numbered variable "verb1" - use meaningful descriptive name

```python
        if match:
            verb1 = match.group(1).lower()
            verb2 = match.group(2).lower()
```

[!] WARNING (line 106)
Line 106 uses numbered variable "verb2" - use meaningful descriptive name

```python
            verb1 = match.group(1).lower()
            verb2 = match.group(2).lower()
            if verb1 in action_verbs and verb2 in action_verbs:
```

---

## provide_meaningful_context
**useless_comments_scanner.py** - 2 violation(s)

[!] WARNING (line 84)
Line 84 contains magic number - replace with named constant

```python
                        rule_obj=rule_obj,
                        violation_message=f'Useless comment: "{line_stripped[:60]}" - delete it or improve the code instead',
                        file_path=file_path,
```

[!] WARNING (line 127)
Line 127 contains magic number - replace with named constant

```python
        before_docstring = content[:docstring_start]
        recent_context = before_docstring[-200:] if len(before_docstring) > 200 else before_docstring
        
```

---

## provide_meaningful_context
**validation_scanner_status_builder.py** - 1 violation(s)

[!] WARNING (line 7)
Line 7 contains magic number - replace with named constant

```python

MAX_VIOLATION_DENSITY_FOR_GOOD_STATUS = 200
MAX_RULES_WITH_ERRORS_FOR_GOOD_STATUS = 5
```

---

## refactor_completely_not_partially
**utils.py** - 5 violation(s)

[!] WARNING (line 121)
Fallback/legacy support code found (comment at line 121, code at line 122) - complete refactoring by removing old pattern support

[!] WARNING (line 175)
Fallback/legacy support code found (comment at line 175, code at line 176) - complete refactoring by removing old pattern support

[!] WARNING (line 197)
Fallback/legacy support code found (comment at line 197, code at line 198) - complete refactoring by removing old pattern support

[!] WARNING (line 248)
Fallback/legacy support code found (comment at line 248, code at line 249) - complete refactoring by removing old pattern support

[!] WARNING (line 270)
Fallback/legacy support code found (comment at line 270, code at line 271) - complete refactoring by removing old pattern support

---

## refactor_completely_not_partially
**action.py** - 2 violation(s)

[!] WARNING (line 226)
Fallback/legacy support code found (comment at line 226, code at line 227) - complete refactoring by removing old pattern support

[!] WARNING (line 546)
Fallback/legacy support code found (comment at line 546, code at line 547) - complete refactoring by removing old pattern support

---

## refactor_completely_not_partially
**adapter_factory.py** - 1 violation(s)

[!] WARNING (line 130)
Fallback/legacy support code found (comment at line 130, code at line 131) - complete refactoring by removing old pattern support

---

## refactor_completely_not_partially
**cli_session.py** - 1 violation(s)

[!] WARNING (line 605)
Fallback/legacy support code found (comment at line 605, code at line 606) - complete refactoring by removing old pattern support

---

## refactor_completely_not_partially
**help_action.py** - 1 violation(s)

[!] WARNING (line 64)
Fallback/legacy support code found (comment at line 64, code at line 65) - complete refactoring by removing old pattern support

---

## refactor_completely_not_partially
**markdown_instructions.py** - 2 violation(s)

[!] WARNING (line 51)
Fallback/legacy support code found (comment at line 51, code at line 52) - complete refactoring by removing old pattern support

[!] WARNING (line 225)
Fallback/legacy support code found (comment at line 225, code at line 226) - complete refactoring by removing old pattern support

---

## refactor_completely_not_partially
**tty_instructions.py** - 1 violation(s)

[!] WARNING (line 154)
Fallback/legacy support code found (comment at line 154, code at line 155) - complete refactoring by removing old pattern support

---

## refactor_completely_not_partially
**rules_action.py** - 2 violation(s)

[!] WARNING (line 56)
Fallback/legacy support code found (comment at line 56, code at line 57) - complete refactoring by removing old pattern support

[!] WARNING (line 62)
Fallback/legacy support code found (comment at line 62, code at line 63) - complete refactoring by removing old pattern support

---

## refactor_completely_not_partially
**json_scope.py** - 1 violation(s)

[!] WARNING (line 208)
Fallback/legacy support code found (comment at line 208, code at line 210) - complete refactoring by removing old pattern support

---

## refactor_completely_not_partially
**scope.py** - 1 violation(s)

[!] WARNING (line 480)
Fallback/legacy support code found (comment at line 480, code at line 481) - complete refactoring by removing old pattern support

---

## refactor_completely_not_partially
**build_action.py** - 2 violation(s)

[!] WARNING (line 62)
Fallback/legacy support code found (comment at line 62, code at line 63) - complete refactoring by removing old pattern support

[!] WARNING (line 142)
Fallback/legacy support code found (comment at line 142, code at line 143) - complete refactoring by removing old pattern support

---

## refactor_completely_not_partially
**validate_action.py** - 1 violation(s)

[!] WARNING (line 134)
Fallback/legacy support code found (comment at line 134, code at line 135) - complete refactoring by removing old pattern support

---

## simplify_control_flow
**action.py** - 8 violation(s)

[!] WARNING (line 136)
Function "_get_type_string" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

```python
        return help_dict
    
    def _get_type_string(self, python_type) -> str:
        """Convert Python type hint to string for help display."""
        if python_type is type(None):
            return "none"
        if python_type == str:
            return "string"
        elif python_type == Path:
            return "path"
        elif python_type == int:
            return "int"
        elif python_type == float:
            return "float"
        elif python_type == bool:
    # ... (truncated)
```

[!] WARNING (line 169)
Function "_get_parameter_description" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        return "value"
    
    def _get_parameter_description(self, param_name: str) -> str:
        """Get meaningful description for a parameter."""
        if 'answers' in param_name or 'key_questions_answered' in param_name:
            return "Dict mapping question keys to answer strings"
        elif 'evidence_provided' in param_name or 'evidence' in param_name:
            return "Dict mapping evidence types to evidence content"
        elif 'choices' in param_name or 'decisions_made' in param_name or 'decisions' in param_name:
            return "Dict mapping decision criteria keys to selected options/values"
        elif 'assumptions' in param_name or 'assumptions_made' in param_name:
            return "List of assumption strings"
        elif 'scope' in param_name:
            return "Scope structure: {'type': 'story'|'epic'|'increment'|'all', 'value': <names|priorities>}"
        elif 'path' in param_name or 'directory' in param_name:
    # ... (truncated)
```

[!] WARNING (line 384)
Function "get_instructions" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return inject_reminder_to_instructions(result, reminder)

    def get_instructions(self, context: ActionContext = None) -> Instructions:
        """Returns AI instructions and saves any guardrails provided in context.
        
        This is the single operation for all actions:
        - Saves guardrails if provided (answers, decisions, evidence, etc.)
        - Builds and returns instructions for AI
        
        This is a template method. Subclasses override _prepare_instructions() to customize.
        """
        if context is None:
            context = self.context_class()
        
        # Save guardrails if provided in context (answers, decisions, evidence, etc.)
    # ... (truncated)
```

[!] WARNING (line 433)
Function "_save_guardrails_if_provided" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return instructions
    
    def _save_guardrails_if_provided(self, context: ActionContext):
        """Save guardrails if provided in context parameters.
        
        This is common logic for all actions. Any action can receive and save guardrails:
        - Clarify action: answers, evidence
        - Strategy action: decisions, assumptions
        - Build action: build_config, decisions
        - etc.
        
        Args:
            context: Action context that may contain guardrail data
        """
        # Check for clarify data (answers, evidence)
    # ... (truncated)
```

[!] WARNING (line 500)
Function "_load_behavior_guardrails" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
                logging.getLogger(__name__).warning(f'Failed to save strategy data: {e}')
    
    def _load_behavior_guardrails(self, instructions):
        """Load behavior-level guardrails (key questions and evidence) if available.
        
        Note: For clarify action, guardrails are set in _prepare_instructions() instead.
        This method is a fallback for other actions that don't override _prepare_instructions().
        """
        try:
            # Check if behavior has guardrails
            if not self.behavior or not hasattr(self.behavior, 'guardrails'):
                return
            
            # Get required_context from behavior's guardrails
            guardrails_obj = self.behavior.guardrails
    # ... (truncated)
```

[!] WARNING (line 527)
Function "_load_all_saved_guardrails" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        self._load_all_saved_guardrails(instructions)
    
    def _load_all_saved_guardrails(self, instructions):
        """Load all saved guardrail data (clarifications and strategy) for visibility on all pages.
        
        This ensures that once clarifications are answered or strategy decisions are made,
        they are visible on ALL pages (clarify, build, validate, render), not just their own page.
        """
        if not self.behavior:
            return
        
        try:
            # Load saved clarification data
            from .clarify.requirements_clarifications import RequirementsClarifications
            from .clarify.required_context import RequiredContext
    # ... (truncated)
```

[!] WARNING (line 623)
Function "_add_behavior_action_metadata" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
            logging.getLogger(__name__).debug(f'Could not load saved strategy decisions: {e}')
    
    def _add_behavior_action_metadata(self, instructions):
        """Add behavior and action metadata as separate properties for JSON output."""
        # Add behavior metadata (using keys that TTY adapter expects)
        if self.behavior:
            behavior_data = {
                'name': self.behavior.name if hasattr(self.behavior, 'name') else 'unknown',
                'description': self.behavior.description if hasattr(self.behavior, 'description') else '',
                'instructions': []
            }
            
            # Add behavior-level instructions if present
            if hasattr(self.behavior, 'instructions') and self.behavior.instructions:
                behavior_instructions = self.behavior.instructions
    # ... (truncated)
```

[!] WARNING (line 696)
Function "_format_instructions_for_display" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        pass
    
    def _format_instructions_for_display(self, instructions) -> str:
        """Template method: Format instructions for REPL display.
        
        Override in subclasses to customize display formatting.
        """
        # Use the proper interface to get instruction data
        instructions_dict = instructions.to_dict()
        output_lines = []
        
        # Note: Scope display with CLI formatting is handled by CLI layer
        
        # BEHAVIOR INSTRUCTIONS SECTION
        if self.behavior:
    # ... (truncated)
```

---

## simplify_control_flow
**behaviors.py** - 1 violation(s)

[!] WARNING (line 307)
Function "load_state" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return None

    def load_state(self):
        if self.bot_paths is None:
            self._init_to_first_behavior()
            return
        workspace_dir = self.bot_paths.workspace_directory
        state_file = workspace_dir / 'behavior_action_state.json'
        if not state_file.exists() or not self._behaviors:
            self._init_to_first_behavior()
            return
        try:
            state_data = json.loads(state_file.read_text(encoding='utf-8'))
            behavior_name = self._extract_behavior_name_from_state(state_data.get('current_behavior', ''))
            if behavior_name:
    # ... (truncated)
```

---

## simplify_control_flow
**bot.py** - 2 violation(s)

[!] WARNING (line 152)
Function "bots" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
    
    @property
    def bots(self) -> List[str]:
        """Return list of all registered bot names.
        
        Discovers bots by scanning the parent bots directory for subdirectories
        containing bot_config.json files.
        
        Returns:
            List of bot names (directory names) that have valid bot_config.json
        """
        registered_bots = []
        
        # Get the parent bots directory (bot_directory.parent)
        bots_parent_dir = self.bot_paths.bot_directory.parent
    # ... (truncated)
```

[!] WARNING (line 286)
Function "scope" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
            }
    
    def scope(self, scope_filter: Optional[str] = None):
        """Set or view the scope filter for the current workflow.
        
        AI AGENTS: This command requires COMPLETE folder paths. When you pass a directory path,
        you MUST include the ENTIRE folder structure from root or working area.
        
        Args:
            scope_filter: Complete folder path or story name to filter by, or None to view current scope
        
        Returns:
            Dict with status, message, and scope data when setting scope, or Scope object when viewing
        """
        from ..scope.scope import ScopeType
    # ... (truncated)
```

---

## simplify_control_flow
**workspace.py** - 1 violation(s)

[!] WARNING (line 25)
Function "get_base_actions_directory" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
    return Path(workspace.strip())

def get_base_actions_directory(bot_directory: Path=None) -> Path:
    """
    Get base actions directory.
    
    Args:
        bot_directory: Optional bot directory path. If None, uses BOT_DIRECTORY env var.
    
    Returns:
        Path to base_actions directory (from bot_config.json or default to agile_bot/base_actions)
    """
    from ..utils import read_json_file
    
    if bot_directory is None:
    # ... (truncated)
```

---

## simplify_control_flow
**bot_path.py** - 1 violation(s)

[!] WARNING (line 26)
Function "_load_base_actions_directory" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        self._documentation_path = self._load_documentation_path()

    def _load_base_actions_directory(self) -> Path:
        """Load base_actions path from bot_config.json or use default."""
        # Try both config locations
        config_paths = [
            self._bot_directory / 'bot_config.json',
            self._bot_directory / 'config' / 'bot_config.json'
        ]
        
        for config_path in config_paths:
            if config_path.exists():
                try:
                    config = read_json_file(config_path)
                    base_actions_path = config.get('baseActionsPath')
    # ... (truncated)
```

---

## simplify_control_flow
**adapters.py** - 1 violation(s)

[!] WARNING (line 172)
Function "serialize" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        self.data = data
    
    def serialize(self) -> str:
        """Format data for TTY output with ANSI formatting."""
        if isinstance(self.data, dict):
            # Check if it's a scope response (status/message/scope)
            if 'scope' in self.data and isinstance(self.data['scope'], dict):
                scope_data = self.data['scope']
                scope_type = scope_data.get('type', 'all')
                target = scope_data.get('target', [])
                
                if target:
                    target_str = ', '.join(str(t) for t in target)
                    return f"\x1b[1mScope:\x1b[0m {scope_type}: {target_str}"
                else:
    # ... (truncated)
```

---

## simplify_control_flow
**adapter_factory.py** - 1 violation(s)

[!] WARNING (line 113)
Function "create" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
    
    @classmethod
    def create(cls, domain_object: Any, channel: str, **kwargs):
        """
        Create appropriate adapter for domain object and channel.
        
        Args:
            domain_object: Domain object to adapt (Status, Scope, etc.)
            channel: Output channel ('json', 'tty', 'markdown')
            **kwargs: Additional arguments to pass to adapter constructor (e.g., is_current)
        
        Returns:
            Adapter instance wrapping domain_object
        
        Raises:
    # ... (truncated)
```

---

## simplify_control_flow
**cli_main.py** - 1 violation(s)

[!] WARNING (line 52)
Function "main" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
from agile_bot.src.cli.cli_session import CLISession

def main():
    bot_name = bot_directory.name
    workspace_directory = get_workspace_directory()
    bot_config_path = bot_directory / 'bot_config.json'
    
    if not bot_config_path.exists():
        print(f"ERROR: Bot config not found at {bot_config_path}", file=sys.stderr)
        sys.exit(1)
    
    try:
        bot = Bot(
            bot_name=bot_name,
            bot_directory=bot_directory,
    # ... (truncated)
```

---

## simplify_control_flow
**cli_session.py** - 3 violation(s)

[!] WARNING (line 38)
Function "execute_command" has nesting depth of 12 - use guard clauses and extract nested blocks to reduce nesting

```python
        self.mode = mode
    
    def execute_command(self, command: str) -> CLICommandResponse:
        """
        Route command to Bot method, return command response.
        
        Command mappings:
        - "status" -> bot itself (serialized via TTYBot)
        - "scope" -> bot.scope -> Scope object (property)
        - "next" -> bot.next() -> NavigationResult object
        - "back" -> bot.back() -> NavigationResult object
        - "help" -> bot.help() -> Help object
        - "exit" -> bot.exit() -> ExitResult object
        - "behavior.action" -> bot.execute('behavior', 'action') -> ActionResult
        
    # ... (truncated)
```

[!] WARNING (line 538)
Function "_handle_action_shortcut" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        raise ValueError(f"Unknown command: {command}")
    
    def _handle_action_shortcut(self, action_name: str, args: str) -> Any:
        """Handle action shortcut commands (e.g., 'build', 'validate', 'rules').
        
        Routes to current behavior's action if action exists.
        For non-workflow actions (like 'rules'), directly executes and returns instructions.
        For workflow actions, navigates and shows instructions.
        Returns None if not an action shortcut (so caller can try other routing).
        """
        # Check if we have a current behavior
        if not self.bot.behaviors.current:
            return {
                'status': 'error',
                'message': 'No current behavior set. Please select a behavior first.'
    # ... (truncated)
```

[!] WARNING (line 636)
Function "run" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return AdapterFactory.create(domain_object, channel)
    
    def run(self):
        """
        Run CLI loop (for interactive mode).
        
        Reads commands from stdin and executes them.
        """
        try:
            while True:
                try:
                    line = input(f"[{self.bot.name}] > ").strip()
                    if not line:
                        continue
                    
    # ... (truncated)
```

---

## simplify_control_flow
**help.py** - 1 violation(s)

[!] WARNING (line 181)
Function "__init__" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
    """
    
    def __init__(self, bot=None):
        """Initialize Help.
        
        Args:
            bot: Bot instance for delegating to behaviors/actions
        """
        self.bot = bot
        self.commands = CommandsHelp()
        self.scope = ScopeHelp()
        
        # Components delegates to bot if available
        if bot:
            behaviors_names = bot.behaviors.names if hasattr(bot, 'behaviors') else []
    # ... (truncated)
```

---

## simplify_control_flow
**help_action.py** - 2 violation(s)

[!] WARNING (line 19)
Function "to_cli_type" has nesting depth of 9 - use guard clauses and extract nested blocks to reduce nesting

```python
    
    @staticmethod
    def to_cli_type(python_type) -> str:
        """Convert Python type hint to CLI-friendly string.
        
        Examples:
            str -> "string"
            Path -> "path"
            dict -> "dict"
            Dict[str, Any] -> "dict"
            List[str] -> "list"
        """
        # Handle None type
        if python_type is type(None):
            return "none"
    # ... (truncated)
```

[!] WARNING (line 232)
Function "_get_parameter_description" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        return params
    
    def _get_parameter_description(self, action_name: str, param_name: str) -> str:
        """Get meaningful description for a parameter (like ActionDataCollector does)"""
        # Check common parameter patterns
        if 'answers' in param_name or 'key_questions_answered' in param_name:
            return "Dict mapping question keys to answer strings"
        elif 'evidence_provided' in param_name or 'evidence' in param_name:
            return "Dict mapping evidence types to evidence content"
        elif 'choices' in param_name or 'decisions_made' in param_name or 'decisions' in param_name:
            return "Dict mapping decision criteria keys to selected options/values"
        elif 'assumptions' in param_name or 'assumptions_made' in param_name:
            return "List of assumption strings"
        elif 'scope' in param_name:
            return self._get_scope_description(action_name)
    # ... (truncated)
```

---

## simplify_control_flow
**markdown_instructions.py** - 1 violation(s)

[!] WARNING (line 14)
Function "serialize" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

```python
        self.instructions = instructions
    
    def serialize(self) -> str:
        """Convert Instructions to Markdown string."""
        instructions_dict = self.instructions.to_dict()
        output_lines = []
        
        # SCOPE SECTION (only show if scope has actual filter values set, or is 'showAll')
        scope = self.instructions.scope
        # Check if scope has filter values (scope.value) - this determines if scope is "empty"
        # When scope.type is 'all', scope.value is empty → don't show scope section
        # When scope.type is 'showAll', scope.value is empty but we show full graph
        # When scope.type is 'story'/'files', scope.value has filter terms → show filtered results
        if scope and (scope.value or scope.type.value == 'showAll'):
            from agile_bot.src.cli.adapters import MarkdownAdapter
    # ... (truncated)
```

---

## simplify_control_flow
**tty_instructions.py** - 1 violation(s)

[!] WARNING (line 14)
Function "serialize" has nesting depth of 8 - use guard clauses and extract nested blocks to reduce nesting

```python
        self.instructions = instructions
    
    def serialize(self) -> str:
        """Convert Instructions to TTY string - assembles all instruction sections."""
        instructions_dict = self.instructions.to_dict()
        output_lines = []
        
        # BEHAVIOR INSTRUCTIONS SECTION
        behavior_metadata = instructions_dict.get('behavior_metadata', {})
        if behavior_metadata:
            behavior_name = behavior_metadata.get('name', 'unknown')
            output_lines.append(f"{self.add_bold(f'Behavior Instructions - {behavior_name}')}")
            
            # Add behavior description
            behavior_description = behavior_metadata.get('description', '')
    # ... (truncated)
```

---

## simplify_control_flow
**rules.py** - 2 violation(s)

[!] WARNING (line 69)
Function "_get_files_for_validation" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
    
    @classmethod
    def _get_files_for_validation(cls, behavior, context: 'ValidateActionContext') -> Dict[str, List[Path]]:
        """Get files to validate based on behavior validation type and scope."""
        from agile_bot.src.actions.validate.file_discovery import FileDiscovery
        from agile_bot.src.scope import ScopeType
        from agile_bot.src.actions.validate.validation_type import ValidationType
        
        # Enforce story-graph-only behaviors to ignore file scopes entirely.
        validation_type = behavior.validation_type
        if validation_type == ValidationType.STORY_GRAPH:
            return {}

        # If scope type is FILES, use the file paths directly from scope.value
        if context.scope and context.scope.type == ScopeType.FILES:
    # ... (truncated)
```

[!] WARNING (line 133)
Function "from_parameters" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
    
    @classmethod
    def from_parameters(cls, parameters: Dict[str, Any], behavior, bot_paths, callbacks: Optional[ValidationCallbacks] = None) -> 'ValidationContext':
        from agile_bot.src.actions.action_context import ValidateActionContext, Scope, ScopeType, FileFilter
        from agile_bot.src.bot.behavior import Behavior
        
        if isinstance(behavior, str):
            behavior = Behavior(name=behavior, bot_paths=bot_paths)
        
        scope = None
        if 'scope' in parameters and parameters['scope']:
            scope_dict = parameters['scope']
            if isinstance(scope_dict, dict):
                scope_type_str = scope_dict.get('type', 'all')
                scope_type = ScopeType(scope_type_str)
    # ... (truncated)
```

---

## simplify_control_flow
**rules_action.py** - 1 violation(s)

[!] WARNING (line 40)
Function "_add_rules_list_to_display" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return [rule.name for rule in rules]
    
    def _add_rules_list_to_display(self, instructions, rule_names: list, rules: Rules) -> None:
        instructions.add_display("")
        instructions.add_display(f"## Rules Available ({len(rule_names)} total)")
        instructions.add_display("")
        # Create a mapping of rule names to rule objects for file path lookup
        rule_map = {rule.name: rule for rule in rules}
        for idx, rule_name in enumerate(rule_names, 1):
            rule = rule_map.get(rule_name)
            if rule:
                # Get full file path from rule's internal path
                if hasattr(rule, '_rule_file_path'):
                    file_path = str(rule._rule_file_path)
                    # Convert Windows paths to forward slashes for consistency
    # ... (truncated)
```

---

## simplify_control_flow
**arrange_act_assert_scanner.py** - 4 violation(s)

[!] WARNING (line 79)
Function "_detect_aaa_sections_ast" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations[0] if violations else None
    
    def _detect_aaa_sections_ast(self, test_node: ast.FunctionDef, content: str) -> Dict[str, List[ast.stmt]]:
        sections = {'arrange': [], 'act': [], 'assert': []}
        test_lines = content.split('\n')
        
        # Track current section based on comments
        current_section = None
        
        for i, stmt in enumerate(test_node.body):
            # Skip docstrings and pass
            if isinstance(stmt, (ast.Pass, ast.Expr)):
                if isinstance(stmt, ast.Expr) and isinstance(stmt.value, (ast.Constant, ast.Str)):
                    continue
            
    # ... (truncated)
```

[!] WARNING (line 114)
Function "_classify_statement" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        return sections
    
    def _classify_statement(self, stmt: ast.stmt) -> Optional[str]:
        # Assertions are always "assert"
        if isinstance(stmt, ast.Assert):
            return 'assert'
        
        for node in ast.walk(stmt):
            if isinstance(node, ast.Call):
                func_name = self._get_call_name(node)
                if func_name and ('assert' in func_name.lower() or 'verify' in func_name.lower()):
                    return 'assert'
        
        for node in ast.walk(stmt):
            if isinstance(node, ast.Call):
    # ... (truncated)
```

[!] WARNING (line 153)
Function "_validate_aaa_structure" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        return None
    
    def _validate_aaa_structure(self, sections: Dict[str, List[ast.stmt]], test_node: ast.FunctionDef, 
                                file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        has_arrange = len(sections['arrange']) > 0
        has_act = len(sections['act']) > 0
        has_assert = len(sections['assert']) > 0
        
        # Also check comments/method names (fallback)
        test_lines = file_path.read_text(encoding='utf-8').split('\n')
        start_line = test_node.lineno - 1
        end_line = test_node.end_lineno if hasattr(test_node, 'end_lineno') else start_line + 50
        test_body_lines = test_lines[start_line:end_line]
        
        has_given_comment = any('# Given' in line or '# Arrange' in line for line in test_body_lines)
    # ... (truncated)
```

[!] WARNING (line 275)
Function "_has_actual_code" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return None
    
    def _has_actual_code(self, test_node: ast.FunctionDef) -> bool:
        if not test_node.body:
            return False
        
        for stmt in test_node.body:
            if isinstance(stmt, ast.Pass):
                continue
            elif isinstance(stmt, ast.Expr) and isinstance(stmt.value, (ast.Constant, ast.Str)):
                continue
            else:
                for node in ast.walk(stmt):
                    if isinstance(node, (ast.Call, ast.Assign, ast.Assert, ast.Return, ast.Raise)):
                        return True
    # ... (truncated)
```

---

## simplify_control_flow
**ascii_only_scanner.py** - 1 violation(s)

[!] WARNING (line 28)
Function "_check_unicode_characters" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _check_unicode_characters(self, line: str, file_path: Path, line_num: int, rule_obj: Any) -> Optional[Dict[str, Any]]:
        try:
            line.encode('ascii')
        except UnicodeEncodeError:
            # Found non-ASCII characters
            # Find the problematic characters
            unicode_chars = []
            for char in line:
                try:
                    char.encode('ascii')
                except UnicodeEncodeError:
                    unicode_chars.append(char)
            
    # ... (truncated)
```

---

## simplify_control_flow
**background_common_setup_scanner.py** - 1 violation(s)

[!] WARNING (line 95)
Function "_get_scenario_steps" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return steps
    
    def _get_scenario_steps(self, scenario: Dict[str, Any]) -> List[str]:
        if isinstance(scenario, dict):
            if 'steps' in scenario:
                return scenario['steps']
            elif 'scenario' in scenario:
                scenario_text = scenario['scenario']
                if isinstance(scenario_text, str):
                    return [s.strip() for s in scenario_text.split('\n') if s.strip()]
        return []

```

---

## simplify_control_flow
**bad_comments_scanner.py** - 5 violation(s)

[!] WARNING (line 32)
Function "_check_commented_code" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _check_commented_code(self, lines: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        commented_block_start = None
        
        for line_num, line in enumerate(lines, 1):
            stripped = line.strip()
            
            if stripped.startswith('//') or stripped.startswith('#'):
                comment_content = stripped[2:].strip()
                
                # Only flag if this looks like actual executable code, not just a comment mentioning code
                if self._is_actual_commented_code(comment_content, lines, line_num):
                    if commented_block_start is None:
    # ... (truncated)
```

[!] WARNING (line 96)
Function "_is_actual_commented_code" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
            ).to_dict()
    
    def _is_actual_commented_code(self, comment_content: str, lines: List[str], line_num: int) -> bool:
        if not comment_content:
            return False
        
        # Check if there's production code immediately after this comment (within 2 lines)
        # If so, this is likely an explanatory comment, not commented-out code
        for i in range(1, min(3, len(lines) - line_num + 1)):
            if line_num + i - 1 < len(lines):
                next_line = lines[line_num + i - 1].strip()
                # Skip empty lines and comment lines
                if next_line and not next_line.startswith('//') and not next_line.startswith('#'):
                    if re.search(r'\b(def|class|if|for|while|return|import|from|=\s*[^=]|\(|\[|\{)\b', next_line):
                        # There's production code right after - this comment is explanatory
    # ... (truncated)
```

[!] WARNING (line 178)
Function "_check_html_in_comments" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def _check_html_in_comments(self, lines: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        html_patterns = [
            r'<p>', r'</p>', r'<ul>', r'</ul>', r'<li>', r'</li>',
            r'<div>', r'</div>', r'<span>', r'</span>', r'<br>', r'<br/>'
        ]
        
        for line_num, line in enumerate(lines, 1):
            comment_text = self._extract_comment_text(line)
            
            if comment_text:
                for pattern in html_patterns:
    # ... (truncated)
```

[!] WARNING (line 219)
Function "_extract_comment_text" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _extract_comment_text(self, line: str) -> Optional[str]:
        in_single_quote = False
        in_double_quote = False
        in_triple_single = False
        in_triple_double = False
        escape_next = False
        
        i = 0
        while i < len(line):
            char = line[i]
            
            if escape_next:
                escape_next = False
    # ... (truncated)
```

[!] WARNING (line 278)
Function "_check_misleading_todos" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return None
    
    def _check_misleading_todos(self, lines: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        for line_num, line in enumerate(lines, 1):
            if 'TODO' in line.upper() or 'FIXME' in line.upper():
                if 'needs to be implemented' in line.lower() or 'not implemented' in line.lower():
                    next_lines = lines[line_num:line_num+5]
                    has_implementation = any(
                        re.search(r'\b(function|def|class|return|if|for|while)\b', l)
                        for l in next_lines
                    )
                    
                    if has_implementation:
    # ... (truncated)
```

---

## simplify_control_flow
**business_readable_test_names_scanner.py** - 2 violation(s)

[!] WARNING (line 114)
Function "_check_business_readable" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return set(words)
    
    def _check_business_readable(self, test_name: str, file_path: Path, node: ast.FunctionDef, rule_obj: Any, domain_language: set) -> Optional[Dict[str, Any]]:
        name_without_prefix = test_name[5:] if test_name.startswith('test_') else test_name
        
        test_words = self._extract_words_from_text(name_without_prefix)
        
        # If ANY domain term matches, consider it business-readable and skip all technical jargon checks
        if domain_language and test_words:
            matching_domain_terms = test_words.intersection(domain_language)
            # If ANY domain term matches, skip all technical jargon checks
            # This prevents false positives for legitimate domain terms like 'param', 'method', 'data'
            if len(matching_domain_terms) >= 1:
                # Test name uses domain language - consider it business-readable
                return None
    # ... (truncated)
```

[!] WARNING (line 261)
Function "_extract_code_snippet" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return True
    
    def _extract_code_snippet(self, content: str, ast_node: Optional[ast.AST] = None, 
                             start_line: Optional[int] = None, end_line: Optional[int] = None,
                             context_before: int = 2, max_lines: int = 50) -> str:
        lines = content.split('\n')
        
        # Determine start and end lines
        if ast_node is not None:
            # Use AST node to determine lines
            start_line_0 = ast_node.lineno - 1 if hasattr(ast_node, 'lineno') and ast_node.lineno else 0
            
            if hasattr(ast_node, 'end_lineno') and ast_node.end_lineno:
                end_line_0 = ast_node.end_lineno  # end_lineno is 1-indexed, exclusive
            else:
    # ... (truncated)
```

---

## simplify_control_flow
**class_based_organization_scanner.py** - 6 violation(s)

[!] WARNING (line 17)
Function "scan_file" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

```python
        return []  # Test scanning happens in scan_test_file, not scan_story_node
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, story_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        if not file_path.exists():
            return violations
        
        sub_epic_names = self._extract_sub_epic_names(story_graph)
        file_name = file_path.stem  # Without .py extension
        violation = self._check_file_name_matches_sub_epic(file_name, sub_epic_names, file_path, rule_obj, story_graph)
        if violation:
            violations.append(violation)
        
        parsed = self._read_and_parse_file(file_path)
    # ... (truncated)
```

[!] WARNING (line 132)
Function "_find_expected_scenario_name" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

```python
        return None
    
    def _find_expected_scenario_name(self, method_name: str, story_graph: Dict[str, Any], class_name: str) -> Optional[str]:
        # Reconstruct full method name with 'test_' prefix for test_method field comparison
        full_method_name = f"test_{method_name}" if not method_name.startswith('test_') else method_name
        method_name_norm = self._normalize_name(method_name)
        
        story_name_from_class = class_name[4:] if class_name.startswith('Test') else class_name
        story_name_normalized = self._normalize_name(story_name_from_class)
        
        epics = story_graph.get('epics', [])
        
        best_match = None
        best_match_type = None  # 'scenario', 'story', 'sub_epic', 'epic'
        
    # ... (truncated)
```

[!] WARNING (line 382)
Function "_get_sub_epics_spanned_by_test_methods" has nesting depth of 8 - use guard clauses and extract nested blocks to reduce nesting

```python
        ).to_dict()
    
    def _get_sub_epics_spanned_by_test_methods(self, file_path: Path, story_graph: Dict[str, Any]) -> set:
        sub_epics = set()
        
        try:
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(file_path))
            
            # Find all test methods
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    if node.name.startswith('Test'):
                        class_name = node.name
                        
    # ... (truncated)
```

[!] WARNING (line 408)
Function "_find_sub_epic_for_method" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        return sub_epics
    
    def _find_sub_epic_for_method(self, method_name: str, class_name: str, story_graph: Dict[str, Any]) -> Optional[str]:
        method_name_norm = self._normalize_name(method_name)
        story_name_from_class = class_name[4:] if class_name.startswith('Test') else class_name
        story_name_normalized = self._normalize_name(story_name_from_class)
        
        epics = story_graph.get('epics', [])
        
        for epic in epics:
            sub_epics = epic.get('sub_epics', [])
            for sub_epic in sub_epics:
                sub_epic_name = sub_epic.get('name', '')
                sub_epic_name_norm = self._normalize_name(sub_epic_name) if sub_epic_name else ''
                
    # ... (truncated)
```

[!] WARNING (line 473)
Function "_find_closest_sub_epic_names" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return None
    
    def _find_closest_sub_epic_names(self, file_name: str, sub_epic_names: List[str], max_suggestions: int = 5) -> List[str]:
        if not sub_epic_names:
            return []
        
        scored_names = []
        file_name_lower = file_name.lower()
        
        for sub_epic_name in sub_epic_names:
            sub_epic_lower = sub_epic_name.lower()
            
            # Simple similarity: check for common substrings
            score = 0
            
    # ... (truncated)
```

[!] WARNING (line 507)
Function "_is_helper_file_only" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return [name for _, name in scored_names[:max_suggestions]]
    
    def _is_helper_file_only(self, file_path: Path) -> bool:
        try:
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    if node.name.startswith('Test'):
                        return False  # Has test class
                elif isinstance(node, ast.FunctionDef):
                    if node.name.startswith('test_'):
                        return False  # Has test method
            
    # ... (truncated)
```

---

## simplify_control_flow
**code_representation_scanner.py** - 1 violation(s)

[!] WARNING (line 19)
Function "scan_domain_concept" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
    ]
    
    def scan_domain_concept(self, node: DomainConceptNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        node_name_lower = node.name.lower()
        for pattern in self.ABSTRACT_PATTERNS:
            if pattern in node_name_lower:
                violations.append(
                    Violation(
                        rule=rule_obj,
                        violation_message=f'Domain concept "{node.name}" uses abstract terminology. Domain models should represent code closely - refactor code if needed.',
                        location=node.map_location('name'),
                        line_number=None,
                        severity='info'
    # ... (truncated)
```

---

## simplify_control_flow
**code_scanner.py** - 2 violation(s)

[!] WARNING (line 44)
Function "_extract_domain_terms" has nesting depth of 12 - use guard clauses and extract nested blocks to reduce nesting

```python
        return []
    
    def _extract_domain_terms(self, story_graph: Dict[str, Any]) -> set:
        domain_terms = set()
        
        # These are domain concepts, not technical jargon
        common_domain_terms = {
            'json', 'data', 'param', 'params', 'parameter', 'parameters',
            'var', 'vars', 'variable', 'variables',
            'method', 'methods', 'class', 'classes', 'call', 'calls',
            'config', 'configuration', 'configurations',
            'agent', 'bot', 'workflow', 'story', 'epic', 'scenario', 'action',
            'behavior', 'rule', 'rules', 'validation', 'validate', 'scanner',
            'file', 'files', 'directory', 'directories', 'path', 'paths',
            'state', 'states', 'tool', 'tools', 'server', 'catalog', 'metadata'
    # ... (truncated)
```

[!] WARNING (line 206)
Function "_extract_code_snippet" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
            return None
    
    def _extract_code_snippet(self, content: str, ast_node: Optional[ast.AST] = None, 
                             start_line: Optional[int] = None, end_line: Optional[int] = None,
                             context_before: int = 2, max_lines: int = 50) -> str:
        lines = content.split('\n')
        
        # Determine start and end lines
        if ast_node is not None:
            # Use AST node to determine lines
            start_line_0 = ast_node.lineno - 1 if hasattr(ast_node, 'lineno') and ast_node.lineno else 0
            
            if hasattr(ast_node, 'end_lineno') and ast_node.end_lineno:
                end_line_0 = ast_node.end_lineno  # end_lineno is 1-indexed, exclusive
            else:
    # ... (truncated)
```

---

## simplify_control_flow
**complete_refactoring_scanner.py** - 1 violation(s)

[!] WARNING (line 28)
Function "_check_fallback_legacy_support" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _check_fallback_legacy_support(self, lines: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        # Pattern to match comments that explicitly mention fallback or legacy
        fallback_comment_pattern = re.compile(
            r'#\s*(fallback|legacy).*',
            re.IGNORECASE
        )
        
        for line_num, line in enumerate(lines, 1):
            stripped = line.strip()
            
            if fallback_comment_pattern.match(stripped):
    # ... (truncated)
```

---

## simplify_control_flow
**complexity_metrics.py** - 5 violation(s)

[!] WARNING (line 10)
Function "cyclomatic_complexity" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
    
    @staticmethod
    def cyclomatic_complexity(func_node: ast.FunctionDef) -> int:
        complexity = 1  # Base complexity
        
        for node in ast.walk(func_node):
            # Decision points
            if isinstance(node, (ast.If, ast.For, ast.While, ast.ExceptHandler, ast.With)):
                complexity += 1
            # Boolean operators add complexity
            elif isinstance(node, ast.BoolOp):
                complexity += len(node.values) - 1
            elif isinstance(node, ast.Assert):
                complexity += 1
        
    # ... (truncated)
```

[!] WARNING (line 26)
Function "cognitive_complexity" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
    
    @staticmethod
    def cognitive_complexity(func_node: ast.FunctionDef) -> int:
        complexity = 0
        nesting_level = 0
        
        def visit_node(node: ast.AST, level: int):
            nonlocal complexity
            
            # Increment complexity for decision points
            if isinstance(node, (ast.If, ast.For, ast.While, ast.ExceptHandler)):
                complexity += 1 + level  # Nesting adds to complexity
                # Visit children with increased nesting
                for child in ast.iter_child_nodes(node):
                    visit_node(child, level + 1)
    # ... (truncated)
```

[!] WARNING (line 264)
Function "_get_accessed_attributes" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
    
    @staticmethod
    def _get_accessed_attributes(method_node: ast.FunctionDef, class_node: ast.ClassDef) -> Set[str]:
        attributes = set()
        
        class_attrs = set()
        for node in class_node.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        class_attrs.add(target.id)
        
        # Find attribute accesses in method
        for node in ast.walk(method_node):
            if isinstance(node, ast.Attribute):
    # ... (truncated)
```

[!] WARNING (line 330)
Function "detect_class_responsibilities_with_examples" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
    
    @staticmethod
    def detect_class_responsibilities_with_examples(class_node: ast.ClassDef) -> Dict[str, List[Dict[str, Any]]]:
        methods = [node for node in class_node.body if isinstance(node, ast.FunctionDef)]
        
        if len(methods) == 0:
            return {}
        
        # Group methods by responsibility type with examples
        responsibility_groups: Dict[str, List[Dict[str, Any]]] = {}
        
        for method in methods:
            responsibilities_detailed = ComplexityMetrics.detect_responsibilities_with_examples(method)
            if not responsibilities_detailed:
                # Method has no detected responsibility - classify as General
    # ... (truncated)
```

[!] WARNING (line 30)
Function "visit_node" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        nesting_level = 0
        
        def visit_node(node: ast.AST, level: int):
            nonlocal complexity
            
            # Increment complexity for decision points
            if isinstance(node, (ast.If, ast.For, ast.While, ast.ExceptHandler)):
                complexity += 1 + level  # Nesting adds to complexity
                # Visit children with increased nesting
                for child in ast.iter_child_nodes(node):
                    visit_node(child, level + 1)
            elif isinstance(node, ast.With):
                complexity += 1 + level
                for child in ast.iter_child_nodes(node):
                    visit_node(child, level + 1)
    # ... (truncated)
```

---

## simplify_control_flow
**consistent_vocabulary_scanner.py** - 1 violation(s)

[!] WARNING (line 43)
Function "_check_vocabulary_consistency" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return list(set(terms))  # Unique terms
    
    def _check_vocabulary_consistency(self, content: str, domain_terms: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        content_lower = content.lower()
        
        # Look for common synonyms that should use domain terms instead
        synonym_map = {
            'data': ['info', 'information', 'content'],
            'user': ['person', 'customer', 'client'],
            'system': ['application', 'app', 'service'],
        }
        
        for domain_term, synonyms in synonym_map.items():
    # ... (truncated)
```

---

## simplify_control_flow
**cover_all_paths_scanner.py** - 1 violation(s)

[!] WARNING (line 13)
Function "scan_file" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
class CoverAllPathsScanner(TestScanner):
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, story_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
        
        content, lines, tree = parsed
        
        # Find all test methods
        functions = Functions(tree)
        test_methods = [function.node for function in functions.get_many_functions if function.node.name.startswith('test_')]
        
    # ... (truncated)
```

---

## simplify_control_flow
**dead_code_scanner.py** - 3 violation(s)

[!] WARNING (line 23)
Function "scan" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
    """Scanner for detecting dead/unused code."""
    
    def scan(
        self, 
        story_graph: Dict[str, Any], 
        rule_obj: Any = None,
        test_files: Optional[List[Path]] = None,
        code_files: Optional[List[Path]] = None,
        on_file_scanned: Optional[Any] = None
    ) -> List[Dict[str, Any]]:
        """Override scan to perform cross-file analysis for dead code detection.
        
        Dead code detection requires analyzing the entire codebase to determine
        what is used vs unused.
        """
    # ... (truncated)
```

[!] WARNING (line 150)
Function "_analyze_file" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _analyze_file(self, file_path: Path) -> Tuple[Dict[str, Tuple[int, str]], Set[str]]:
        """Analyze a file to extract definitions and usages.
        
        Returns:
            Tuple of (definitions, usages) where:
            - definitions: {name: (line_number, node_type)}
            - usages: set of names that are referenced/called
        """
        definitions = {}
        usages = set()
        
        try:
            content = file_path.read_text(encoding='utf-8')
    # ... (truncated)
```

[!] WARNING (line 197)
Function "_analyze_private_members" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

```python
        return definitions, usages
    
    def _analyze_private_members(self, tree: ast.AST) -> Tuple[Dict[str, Tuple[int, str]], Set[str]]:
        """Analyze private members (_name) and their usages within classes.
        
        Returns:
            Tuple of (private_defs, private_usages) where:
            - private_defs: {method_name: (line_number, class_name)}
            - private_usages: set of method names that are called
        """
        private_defs = {}
        private_usages = set()
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
    # ... (truncated)
```

---

## simplify_control_flow
**delegation_code_scanner.py** - 3 violation(s)

[!] WARNING (line 32)
Function "_check_delegation" has nesting depth of 8 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _check_delegation(self, class_node: ast.ClassDef, content: str, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        is_collection_class = self._is_collection_class(class_node.name)
        
        for node in ast.walk(class_node):
            if isinstance(node, ast.FunctionDef):
                # Skip __init__ methods - setup code is fine
                if node.name == '__init__':
                    continue
                
                for stmt in ast.walk(node):
                    if isinstance(stmt, ast.For):
    # ... (truncated)
```

[!] WARNING (line 85)
Function "_is_plain_collection" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

```python
        return (name_lower.endswith('s') and len(name_lower) > 3) or 'collection' in name_lower
    
    def _is_plain_collection(self, class_node: ast.ClassDef, attr_name: str, content: str) -> bool:
        attr_name_lower = attr_name.lower()
        
        # Skip private attributes that are clearly plain lists
        if attr_name_lower.startswith('_'):
            # Common patterns for plain lists
            plain_list_indicators = ['pattern', 'spec', 'config', 'item', 'entry', 'element']
            if any(indicator in attr_name_lower for indicator in plain_list_indicators):
                return True
        
        for node in ast.walk(class_node):
            if isinstance(node, ast.AnnAssign):
                if isinstance(node.target, ast.Name) and node.target.id == attr_name:
    # ... (truncated)
```

[!] WARNING (line 117)
Function "_is_class_constant" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def _is_class_constant(self, class_node: ast.ClassDef, attr_name: str) -> bool:
        attr_name_upper = attr_name.upper()
        
        if attr_name == attr_name_upper or attr_name.isupper():
            for node in class_node.body:
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name) and target.id == attr_name:
                            if isinstance(node.value, (ast.List, ast.Dict, ast.Tuple)):
                                return True
                        elif isinstance(target, ast.Attribute) and target.attr == attr_name:
                            if isinstance(node.value, (ast.List, ast.Dict, ast.Tuple)):
                                return True
    # ... (truncated)
```

---

## simplify_control_flow
**dependency_chaining_code_scanner.py** - 4 violation(s)

[!] WARNING (line 32)
Function "_check_dependency_chaining" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _check_dependency_chaining(self, class_node: ast.ClassDef, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        # Find __init__ method and collect constructor-injected parameters
        init_method = None
        init_params = []
        for node in ast.walk(class_node):
            if isinstance(node, ast.FunctionDef) and node.name == '__init__':
                init_method = node
                init_params = [arg.arg for arg in node.args.args if arg.arg != 'self']
                break
        
        # Collect all instance attributes (from assignments, properties, etc.)
    # ... (truncated)
```

[!] WARNING (line 101)
Function "_collect_instance_attributes" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _collect_instance_attributes(self, class_node: ast.ClassDef) -> Set[str]:
        attrs = set()
        
        for node in ast.walk(class_node):
            # Collect self.X assignments
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Attribute):
                        if isinstance(target.value, ast.Name) and target.value.id == 'self':
                            attrs.add(target.attr)
            
            # Collect self.X in expressions (properties, method calls)
            if isinstance(node, ast.Attribute):
    # ... (truncated)
```

[!] WARNING (line 124)
Function "_check_method_calls_for_instance_attrs" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        return attrs
    
    def _check_method_calls_for_instance_attrs(
        self, func_node: ast.FunctionDef, class_name: str, file_path: Path, 
        rule_obj: Any, instance_attrs: Set[str]
    ) -> List[Dict[str, Any]]:
        violations = []
        
        for node in ast.walk(func_node):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Attribute):
                    if isinstance(node.func.value, ast.Name) and node.func.value.id == 'self':
                        for arg in node.args:
                            violation = self._check_argument(
                                arg, node.func.attr, class_name, file_path, rule_obj, instance_attrs, func_node.lineno
    # ... (truncated)
```

[!] WARNING (line 143)
Function "_check_argument" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _check_argument(
        self, arg_node: ast.AST, method_name: str, class_name: str, file_path: Path, 
        rule_obj: Any, instance_attrs: Set[str], line_num: int
    ) -> Optional[Dict[str, Any]]:
        if isinstance(arg_node, ast.Attribute):
            if isinstance(arg_node.value, ast.Name) and arg_node.value.id == 'self':
                attr_name = arg_node.attr
                if attr_name in instance_attrs:
                    try:
                        content = file_path.read_text(encoding='utf-8')
                        return self._create_violation_with_snippet(
                            rule_obj=rule_obj,
                            violation_message=f'Passing self.{attr_name} as parameter to {method_name}(). Access it directly in the method through self.{attr_name} instead.',
    # ... (truncated)
```

---

## simplify_control_flow
**dependency_chaining_scanner.py** - 1 violation(s)

[!] WARNING (line 11)
Function "scan_domain_concept" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
class DependencyChainingScanner(DomainScanner):
    
    def scan_domain_concept(self, node: DomainConceptNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        has_instantiation = False
        instantiation_collaborators = []
        
        for i, responsibility_data in enumerate(node.responsibilities):
            responsibility_name = responsibility_data.get('name', '')
            resp_lower = responsibility_name.lower()
            
            if 'instantiated with' in resp_lower:
                has_instantiation = True
                collaborators = responsibility_data.get('collaborators', [])
    # ... (truncated)
```

---

## simplify_control_flow
**domain_language_scanner.py** - 1 violation(s)

[!] WARNING (line 25)
Function "scan_domain_concept" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
    ]
    
    def scan_domain_concept(self, node: DomainConceptNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        node_name_lower = node.name.lower()
        for term in ['data', 'config', 'parameter', 'result']:
            if term in node_name_lower and not self._is_domain_specific(node.name):
                violations.append(
                    Violation(
                        rule=rule_obj,
                        violation_message=f'Domain concept "{node.name}" uses generic term "{term}". Use domain-specific language instead (e.g., "PortfolioData" → "Portfolio", "TargetConfig" → "TargetAllocation").',
                        location=node.map_location('name'),
                        line_number=None,
                        severity='warning'
    # ... (truncated)
```

---

## simplify_control_flow
**duplication_scanner.py** - 23 violation(s)

[!] WARNING (line 263)
Function "_is_simple_delegation" has nesting depth of 8 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def _is_simple_delegation(self, func_node: ast.FunctionDef) -> bool:
        if self._is_simple_property_getter(func_node):
            return True
        
        # Check if it's a simple method that just returns self.attr.method() or self.attr[item]
        executable_body = [stmt for stmt in func_node.body if not self._is_docstring_or_comment(stmt, func_node)]
        if len(executable_body) == 1:
            stmt = executable_body[0]
            if isinstance(stmt, ast.Return) and stmt.value:
                if isinstance(stmt.value, (ast.Call, ast.Subscript)):
                    # Method call or subscript - check if it's on self.attribute
                    if isinstance(stmt.value, ast.Call):
                        if isinstance(stmt.value.func, ast.Attribute):
    # ... (truncated)
```

[!] WARNING (line 296)
Function "_is_simple_property_getter" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def _is_simple_property_getter(self, func_node: ast.FunctionDef) -> bool:
        is_property = False
        for decorator in func_node.decorator_list:
            if isinstance(decorator, ast.Name) and decorator.id == 'property':
                is_property = True
                break
            elif isinstance(decorator, ast.Attribute):
                if decorator.attr in ('setter', 'deleter'):
                    # Setter/deleter, check if it's simple
                    pass
                elif hasattr(decorator, 'value') and isinstance(decorator.value, ast.Name):
                    if decorator.value.id == 'property':
                        is_property = True
    # ... (truncated)
```

[!] WARNING (line 335)
Function "_check_duplicate_code_blocks" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def _check_duplicate_code_blocks(self, functions: List[tuple], lines: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        all_blocks = []
        for func_tuple in functions:
            func_name, func_body, func_line, func_node, _ = func_tuple
            blocks = self._extract_code_blocks(func_node, func_line, func_name)
            all_blocks.extend(blocks)
        
        # Use similarity checking to find duplicate blocks
        SIMILARITY_THRESHOLD = 0.90  # Increased to 90% to reduce false positives
        
        # Debug: track comparison attempts
    # ... (truncated)
```

[!] WARNING (line 777)
Function "_extract_subtrees_from_function" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return blocks
    
    def _extract_subtrees_from_function(self, func_node: ast.FunctionDef, min_nodes: int, max_nodes: int) -> List[ast.AST]:
        subtrees = []
        
        # Control structures that represent semantic units
        control_structures = (ast.If, ast.For, ast.While, ast.Try, ast.With, 
                             ast.AsyncFor, ast.AsyncWith)
        
        def extract_from_node(node):
            if isinstance(node, control_structures):
                # Count nodes in this subtree
                num_nodes = len(list(ast.walk(node)))
                if min_nodes <= num_nodes <= max_nodes:
                    subtrees.append(node)
    # ... (truncated)
```

[!] WARNING (line 831)
Function "_get_statement_end_line" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def _get_statement_end_line(self, stmt: ast.stmt) -> int:
        if hasattr(stmt, 'end_lineno') and stmt.end_lineno:
            return stmt.end_lineno
        
        # For control structures, find the end of their body
        if isinstance(stmt, ast.If):
            end_line = stmt.lineno
            if stmt.body:
                end_line = max(end_line, self._get_body_end_line(stmt.body))
            if stmt.orelse:
                end_line = max(end_line, self._get_body_end_line(stmt.orelse))
            return end_line
        elif isinstance(stmt, (ast.For, ast.While, ast.AsyncFor)):
    # ... (truncated)
```

[!] WARNING (line 896)
Function "_is_mostly_helper_calls" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def _is_mostly_helper_calls(self, statements: List[ast.stmt]) -> bool:
        if not statements:
            return False
        
        helper_count = 0
        total_count = 0
        
        for stmt in statements:
            if self._is_docstring_or_comment(stmt):
                continue
            
            total_count += 1
            
    # ... (truncated)
```

[!] WARNING (line 945)
Function "_is_only_helper_calls" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return (helper_count / total_count) >= 0.6
    
    def _is_only_helper_calls(self, statements: List[ast.stmt]) -> bool:
        helper_patterns = [
            'given_', 'when_', 'then_',
            'create_', 'build_', 'make_', 'generate_',
            'verify_', 'assert_', 'check_', 'ensure_',
            'setup_', 'bootstrap_', 'initialize_',
            'get_', 'load_', 'fetch_'
        ]
        
        for stmt in statements:
            if isinstance(stmt, ast.Assign):
                if isinstance(stmt.value, ast.Call):
                    func_name = self._get_function_name(stmt.value.func)
    # ... (truncated)
```

[!] WARNING (line 1023)
Function "_count_actual_code_statements" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def _count_actual_code_statements(self, statements: List[ast.stmt]) -> int:
        count = 0
        for stmt in statements:
            if self._is_docstring_or_comment(stmt):
                continue
            
            if isinstance(stmt, ast.Pass):
                continue
            
            # Count simple executable statements
            if isinstance(stmt, (ast.Assign, ast.AnnAssign, ast.AugAssign, 
                                 ast.Expr, ast.Return, ast.Raise, ast.Assert,
                                 ast.Delete, ast.Import, ast.ImportFrom,
    # ... (truncated)
```

[!] WARNING (line 1077)
Function "_is_test_pattern" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return (assertion_count / total_count) >= 0.6
    
    def _is_test_pattern(self, statements: List[ast.stmt]) -> bool:
        if not statements:
            return False
        
        # Count helper calls and assertions
        helper_count = 0
        assertion_count = 0
        other_count = 0
        
        for stmt in statements:
            if self._is_docstring_or_comment(stmt):
                continue
            
    # ... (truncated)
```

[!] WARNING (line 1115)
Function "_is_list_building_pattern" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return test_pattern_ratio >= 0.75 and other_count <= 1
    
    def _is_list_building_pattern(self, statements: List[ast.stmt]) -> bool:
        if not statements:
            return False
        
        list_building_count = 0
        total_count = 0
        
        for stmt in statements:
            if self._is_docstring_or_comment(stmt):
                continue
            
            total_count += 1
            
    # ... (truncated)
```

[!] WARNING (line 1145)
Function "_is_simple_property" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return (list_building_count / total_count) >= 0.75
    
    def _is_simple_property(self, func_node: ast.FunctionDef) -> bool:
        if not func_node.decorator_list:
            return False
        
        has_property_decorator = False
        for decorator in func_node.decorator_list:
            if isinstance(decorator, ast.Name) and decorator.id == 'property':
                has_property_decorator = True
                break
            elif isinstance(decorator, ast.Attribute):
                if decorator.attr in ('setter', 'deleter'):
                    has_property_decorator = True
                    break
    # ... (truncated)
```

[!] WARNING (line 1172)
Function "_is_simple_constructor" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def _is_simple_constructor(self, func_node: ast.FunctionDef) -> bool:
        if func_node.name != '__init__':
            return False
        
        # Count statements that are just assignments to self
        executable_body = [stmt for stmt in func_node.body if not self._is_docstring_or_comment(stmt, func_node)]
        
        self_assignments = 0
        other_statements = 0
        
        for stmt in executable_body:
            if isinstance(stmt, (ast.Assign, ast.AnnAssign)):
                if isinstance(stmt, ast.Assign):
    # ... (truncated)
```

[!] WARNING (line 1229)
Function "_operates_on_different_domains" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return entities
    
    def _operates_on_different_domains(self, block1: Dict[str, Any], block2: Dict[str, Any]) -> bool:
        domain_patterns1 = self._extract_domain_entities(block1)
        domain_patterns2 = self._extract_domain_entities(block2)
        
        # If they have different domain entities and function names are similar,
        # they're likely legitimate separate implementations
        if domain_patterns1 and domain_patterns2:
            if domain_patterns1 != domain_patterns2:
                # If so, this is likely legitimate - each domain needs its own handlers
                func1 = block1['func_name']
                func2 = block2['func_name']
                if abs(len(func1) - len(func2)) <= 3:  # Similar length names
                    # Extract common prefixes (CRUD operations: create, read, update, delete, get, set)
    # ... (truncated)
```

[!] WARNING (line 1253)
Function "_calls_different_methods" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def _calls_different_methods(self, block1_nodes: List[ast.stmt], block2_nodes: List[ast.stmt]) -> bool:
        calls1 = self._extract_method_calls(block1_nodes)
        calls2 = self._extract_method_calls(block2_nodes)
        
        if not calls1 or not calls2:
            return False
        
        # If blocks have same number of calls but different method names, they're likely
        # structural patterns calling different methods (not duplication)
        if len(calls1) == len(calls2) and len(calls1) >= 2:
            method_names1 = {call for call in calls1}
            method_names2 = {call for call in calls2}
            
    # ... (truncated)
```

[!] WARNING (line 1279)
Function "_extract_method_calls" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def _extract_method_calls(self, nodes: List[ast.stmt]) -> List[str]:
        method_calls = []
        
        for node in nodes:
            if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
                call = node.value
                if isinstance(call.func, ast.Attribute):
                    # Method call: obj.method()
                    method_calls.append(call.func.attr)
                elif isinstance(call.func, ast.Name):
                    # Function call: func()
                    method_calls.append(call.func.id)
            elif isinstance(node, ast.Assign):
    # ... (truncated)
```

[!] WARNING (line 1304)
Function "_normalize_block" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def _normalize_block(self, statements: List[ast.stmt]) -> Optional[str]:
        try:
            normalized_parts = []
            for stmt in statements:
                stmt_type = type(stmt).__name__
                
                # Skip docstrings and comments
                if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant):
                    if isinstance(stmt.value.value, str) and stmt.value.value.strip().startswith('"""'):
                        continue
                
                # Normalize assignment: var = value -> ASSIGN
                if isinstance(stmt, ast.Assign):
    # ... (truncated)
```

[!] WARNING (line 1345)
Function "_get_block_preview" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
            return None
    
    def _get_block_preview(self, statements: List[ast.stmt]) -> str:
        try:
            if hasattr(ast, 'unparse'):
                preview_lines = []
                for stmt in statements:
                    # Skip docstrings when generating preview
                    if self._is_docstring_or_comment(stmt):
                        continue
                    preview_lines.append(ast.unparse(stmt))
                return "\n".join(preview_lines)
            else:
                return str(statements)
        except Exception as e:
    # ... (truncated)
```

[!] WARNING (line 1400)
Function "_compare_ast_nodes_deep" has nesting depth of 11 - use guard clauses and extract nested blocks to reduce nesting

```python
        return 0.0
    
    def _compare_ast_nodes_deep(self, node1: ast.AST, node2: ast.AST) -> float:
        if type(node1) != type(node2):
            return 0.0
        
        # Compare based on node type
        if isinstance(node1, ast.Assign):
            return self._compare_assign_nodes(node1, node2)
        elif isinstance(node1, ast.AugAssign):
            return self._compare_augassign_nodes(node1, node2)
        elif isinstance(node1, ast.Expr) and isinstance(node1.value, ast.Call):
            # Both are Expr nodes with Call values
            if isinstance(node2, ast.Expr) and isinstance(node2.value, ast.Call):
                return self._compare_call_nodes(node1.value, node2.value)
    # ... (truncated)
```

[!] WARNING (line 1513)
Function "_compare_expr_structure" has nesting depth of 8 - use guard clauses and extract nested blocks to reduce nesting

```python
        return 0.7 + 0.3 * self._compare_expr_structure(node1.exc, node2.exc)
    
    def _compare_expr_structure(self, expr1: ast.expr, expr2: ast.expr) -> float:
        if type(expr1) != type(expr2):
            return 0.0
        
        if isinstance(expr1, ast.Call):
            return self._compare_call_nodes(expr1, expr2)
        elif isinstance(expr1, ast.Attribute):
            # Compare attribute access structure (ignore attribute name)
            return 0.8 + 0.2 * self._compare_expr_structure(expr1.value, expr2.value)
        elif isinstance(expr1, ast.Name):
            # Names are different but structure is same
            return 0.9
        elif isinstance(expr1, ast.Constant):
    # ... (truncated)
```

[!] WARNING (line 1549)
Function "_log_violation_details" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
            return 0.7
    
    def _log_violation_details(self, file_path: Path, violations: List[Dict[str, Any]], lines: List[str]) -> None:
        if not violations:
            return
        
        # Log detailed violation information
        # Note: This can be verbose, but provides valuable debugging info
        
        _safe_print(f"\n[{file_path}] Found {len(violations)} duplication violation(s):")
        
        for idx, violation in enumerate(violations, 1):
            line_num = violation.get('line_number', '?')
            msg = violation.get('violation_message', '')
            
    # ... (truncated)
```

[!] WARNING (line 1607)
Function "_filter_files_by_package_proximity" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        _safe_print("")  # Blank line after violations
    
    def _filter_files_by_package_proximity(
        self,
        changed_files: List[Path],
        all_files: List[Path],
        max_parent_levels: int = 3,
        max_files: int = 20
    ) -> List[Path]:
        """Filter all_files to only include files in nearby packages.
        
        Priority:
        1. Same package (immediate siblings)
        2. Parent package
        3. Parent's parent package (up to max_parent_levels)
    # ... (truncated)
```

[!] WARNING (line 1683)
Function "scan_cross_file" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return nearby_files
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
        test_files: Optional[List[Path]] = None,
        code_files: Optional[List[Path]] = None,
        all_test_files: Optional[List[Path]] = None,
        all_code_files: Optional[List[Path]] = None,
        status_writer: Optional[Any] = None,
        max_cross_file_comparisons: int = 20
    ) -> List[Dict[str, Any]]:
        violations = []
        
        # If all_* not provided, fall back to regular behavior
    # ... (truncated)
```

[!] WARNING (line 784)
Function "extract_from_node" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
                             ast.AsyncFor, ast.AsyncWith)
        
        def extract_from_node(node):
            if isinstance(node, control_structures):
                # Count nodes in this subtree
                num_nodes = len(list(ast.walk(node)))
                if min_nodes <= num_nodes <= max_nodes:
                    subtrees.append(node)
            
            if hasattr(node, 'body') and isinstance(node.body, list):
                for child in node.body:
                    extract_from_node(child)
            
            if hasattr(node, 'orelse') and isinstance(node.orelse, list):
                for child in node.orelse:
    # ... (truncated)
```

---

## simplify_control_flow
**exact_variable_names_scanner.py** - 2 violation(s)

[!] WARNING (line 32)
Function "_extract_domain_concepts" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _extract_domain_concepts(self, story_graph: Dict[str, Any]) -> List[str]:
        concepts = []
        epics = story_graph.get('epics', [])
        for epic in epics:
            domain_concepts_list = epic.get('domain_concepts', [])
            for concept in domain_concepts_list:
                if isinstance(concept, dict):
                    concept_name = concept.get('name', '')
                    if concept_name:
                        concepts.append(concept_name.lower())
        return concepts
    
```

[!] WARNING (line 44)
Function "_check_variable_names" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return concepts
    
    def _check_variable_names(self, test_node: ast.FunctionDef, domain_concepts: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        # Find variable assignments in test
        for node in ast.walk(test_node):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        var_name = target.id.lower()
                        
                        if var_name in ['data', 'result', 'value', 'item', 'obj', 'thing']:
                            line_number = target.lineno if hasattr(target, 'lineno') else None
                            violation = Violation(
    # ... (truncated)
```

---

## simplify_control_flow
**excessive_guards_scanner.py** - 5 violation(s)

[!] WARNING (line 68)
Function "_is_guard_pattern" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def _is_guard_pattern(self, test_node: ast.AST) -> bool:
        # hasattr() checks
        if isinstance(test_node, ast.Call):
            if isinstance(test_node.func, ast.Name):
                if test_node.func.id == 'hasattr':
                    return True
        
        # isinstance() checks (defensive, not polymorphic)
        if isinstance(test_node, ast.Call):
            if isinstance(test_node.func, ast.Name):
                if test_node.func.id == 'isinstance':
                    return True
        
    # ... (truncated)
```

[!] WARNING (line 123)
Function "_is_optional_config_check" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

```python
        return defaults.get(message_key, f'Line {line_number}: Guard clause detected.')

    def _is_optional_config_check(self, guard_node: ast.If, source_lines: List[str]) -> bool:
        # File existence checks - only flag if NOT followed by creation logic
        test = guard_node.test
        if isinstance(test, ast.Call) and isinstance(test.func, ast.Attribute) and test.func.attr == 'exists':
            if self._is_followed_by_creation_logic(guard_node, source_lines):
                return True  # Has creation logic, so it's legitimate - don't flag
            # No creation logic - flag it
            return False
        
        # hasattr() checks - these are for optional attributes, don't flag
        if isinstance(test, ast.Call) and isinstance(test.func, ast.Name) and test.func.id == 'hasattr':
            return True
        
    # ... (truncated)
```

[!] WARNING (line 185)
Function "_is_followed_by_creation_logic" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return any(pattern in var_name for pattern in optional_patterns)
    
    def _is_followed_by_creation_logic(self, guard_node: ast.If, source_lines: List[str]) -> bool:
        if guard_node.orelse:
            for stmt in guard_node.orelse:
                if self._contains_creation_call(stmt):
                    return True
        
        # Look at lines after the if statement (including else branch)
        start_line = guard_node.lineno - 1  # Convert to 0-based index
        end_line = guard_node.end_lineno if hasattr(guard_node, 'end_lineno') else start_line + len(guard_node.body) + 1
        
        if guard_node.orelse:
            for stmt in guard_node.orelse:
                if hasattr(stmt, 'lineno'):
    # ... (truncated)
```

[!] WARNING (line 217)
Function "_contains_creation_call" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def _contains_creation_call(self, node: ast.AST) -> bool:
        creation_methods = ['write_text', 'write_bytes', 'mkdir', 'touch']
        for child in ast.walk(node):
            if isinstance(child, ast.Call):
                if isinstance(child.func, ast.Attribute):
                    if child.func.attr in creation_methods:
                        return True
        return False

```

[!] WARNING (line 226)
Function "_check_guard_pattern" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False

    def _check_guard_pattern(self, guard_node: ast.If, file_path: Path, rule_obj: Any, source_lines: List[str], content: str) -> Optional[Dict[str, Any]]:
        test = guard_node.test
        
        # Skip file existence checks, optional config, hasattr(), early returns, etc.
        if self._is_optional_config_check(guard_node, source_lines):
            return None
        
        # None checks (if X is None:, if X is not None:)
        # Only flag if it's checking a required variable, not optional config
        if isinstance(test, ast.Compare):
            for op in test.ops:
                if isinstance(op, (ast.Is, ast.IsNot)):
                    for comparator in test.comparators:
    # ... (truncated)
```

---

## simplify_control_flow
**full_result_assertions_scanner.py** - 4 violation(s)

[!] WARNING (line 38)
Function "scan_file" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
    }

    def scan_file(self, file_path: Path, rule_obj: Any = None, story_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations: List[Dict[str, Any]] = []

        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations

        content, lines, tree = parsed

        for func in [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name.startswith("test")]:
            alias_targets = self._collect_result_aliases(func)
            if self._has_full_object_assert(func, alias_targets):
                continue  # already asserting full object on result-like object
    # ... (truncated)
```

[!] WARNING (line 66)
Function "_is_single_field_assert" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations

    def _is_single_field_assert(self, test_expr: ast.AST, aliases: Set[str]) -> bool:
        targets = aliases or set()
        # assert obj['field'] == ... OR ... == obj['field']
        if isinstance(test_expr, ast.Compare):
            left = test_expr.left
            if self._is_subscript_or_attr_on_target(left, targets):
                return True
            # assert something == obj['field']
            for comp in test_expr.comparators:
                if self._is_subscript_or_attr_on_target(comp, targets):
                    return True
        # assert len(obj) == ... or ... == len(obj)
        if isinstance(test_expr, ast.Compare):
    # ... (truncated)
```

[!] WARNING (line 110)
Function "_has_full_object_assert" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return isinstance(node, ast.Name) and node.id in (self.TARGET_NAMES | aliases)

    def _has_full_object_assert(self, func_node: ast.FunctionDef, aliases: Set[str]) -> bool:
        """Detect if function asserts equality of whole object (dict or dataclass-like) on a result-like target."""
        for node in ast.walk(func_node):
            if isinstance(node, ast.Assert) and isinstance(node.test, ast.Compare):
                left = node.test.left
                comps = node.test.comparators
                if any(self._is_target_name(expr, aliases) for expr in [left, *comps]):
                    # if comparing target directly to something (likely full object)
                    if not any(isinstance(expr, (ast.Subscript, ast.Attribute)) for expr in [left, *comps]):
                        return True
        return False

```

[!] WARNING (line 122)
Function "_collect_result_aliases" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False

    def _collect_result_aliases(self, func_node: ast.FunctionDef) -> Set[str]:
        """
        Collect names that likely hold result/state objects:
        - Assignment from a call with result-ish name.
        - Assignment from an existing target name.
        """
        aliases: Set[str] = set()
        for node in ast.walk(func_node):
            if isinstance(node, ast.Assign):
                targets = [t.id for t in node.targets if isinstance(t, ast.Name)]
                source = node.value
                source_name = None
                if isinstance(source, ast.Name) and source.id in (self.TARGET_NAMES | aliases):
    # ... (truncated)
```

---

## simplify_control_flow
**function_size_scanner.py** - 4 violation(s)

[!] WARNING (line 148)
Function "_get_multi_line_expression_line_numbers" has nesting depth of 9 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations[0] if violations else None
    
    def _get_multi_line_expression_line_numbers(self, func_node: ast.FunctionDef) -> set:
        multi_line_lines = set()
        
        def visit_statement(stmt_node):
            if hasattr(stmt_node, 'end_lineno') and hasattr(stmt_node, 'lineno') and stmt_node.end_lineno and stmt_node.lineno:
                if stmt_node.end_lineno > stmt_node.lineno:
                    # This statement spans multiple lines
                    if isinstance(stmt_node, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
                        # Assignment statement - check if the value/expression is multi-line
                        if hasattr(stmt_node, 'value') and stmt_node.value:
                            value = stmt_node.value
                            if hasattr(value, 'end_lineno') and hasattr(value, 'lineno') and value.end_lineno and value.lineno:
                                if value.end_lineno > value.lineno:
    # ... (truncated)
```

[!] WARNING (line 192)
Function "_get_data_structure_line_numbers" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return multi_line_lines
    
    def _get_data_structure_line_numbers(self, func_node: ast.FunctionDef) -> set:
        data_structure_lines = set()  # Use set to avoid double-counting overlapping ranges
        
        # Find all top-level data structures (not nested inside other data structures)
        # We'll collect them and then count their lines
        top_level_data_structures = []
        
        def visit_node(node, parent_is_ds=False):
            is_data_structure = isinstance(node, (ast.List, ast.Dict, ast.Set, ast.Tuple))
            
            if is_data_structure and not parent_is_ds:
                # This is a top-level data structure
                top_level_data_structures.append(node)
    # ... (truncated)
```

[!] WARNING (line 224)
Function "_get_comment_and_docstring_line_numbers" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        return data_structure_lines
    
    def _get_comment_and_docstring_line_numbers(self, func_node: ast.FunctionDef, source_lines: List[str], func_start_line: int) -> set:
        comment_and_docstring_lines = set()
        
        # Find docstring (first statement in function body if it's a string literal)
        if func_node.body:
            first_stmt = func_node.body[0]
            if isinstance(first_stmt, ast.Expr) and isinstance(first_stmt.value, (ast.Str, ast.Constant)):
                string_value = first_stmt.value
                if isinstance(string_value, ast.Constant) and isinstance(string_value.value, str):
                    # This is a docstring
                    if hasattr(first_stmt, 'end_lineno') and hasattr(first_stmt, 'lineno') and first_stmt.end_lineno and first_stmt.lineno:
                        for line_num in range(first_stmt.lineno, first_stmt.end_lineno + 1):
                            comment_and_docstring_lines.add(line_num)
    # ... (truncated)
```

[!] WARNING (line 151)
Function "visit_statement" has nesting depth of 9 - use guard clauses and extract nested blocks to reduce nesting

```python
        multi_line_lines = set()
        
        def visit_statement(stmt_node):
            if hasattr(stmt_node, 'end_lineno') and hasattr(stmt_node, 'lineno') and stmt_node.end_lineno and stmt_node.lineno:
                if stmt_node.end_lineno > stmt_node.lineno:
                    # This statement spans multiple lines
                    if isinstance(stmt_node, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
                        # Assignment statement - check if the value/expression is multi-line
                        if hasattr(stmt_node, 'value') and stmt_node.value:
                            value = stmt_node.value
                            if hasattr(value, 'end_lineno') and hasattr(value, 'lineno') and value.end_lineno and value.lineno:
                                if value.end_lineno > value.lineno:
                                    # Multi-line expression in assignment
                                    # Exclude continuation lines (all except first)
                                    for line_num in range(value.lineno + 1, value.end_lineno + 1):
    # ... (truncated)
```

---

## simplify_control_flow
**given_precondition_scanner.py** - 2 violation(s)

[!] WARNING (line 12)
Function "scan_story_node" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
class GivenPreconditionScanner(StoryScanner):
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        if isinstance(node, Story):
            story_data = node.data
            scenarios = story_data.get('scenarios', [])
            
            for scenario_idx, scenario in enumerate(scenarios):
                scenario_steps = self._get_scenario_steps(scenario)
                
                for step_idx, step in enumerate(scenario_steps):
                    if step.startswith('Given') or step.startswith('And'):
                        violation = self._check_given_is_functionality(step, node, scenario_idx, step_idx, rule_obj)
    # ... (truncated)
```

[!] WARNING (line 30)
Function "_get_scenario_steps" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _get_scenario_steps(self, scenario: Dict[str, Any]) -> List[str]:
        steps = []
        if isinstance(scenario, dict):
            if 'steps' in scenario:
                steps = scenario['steps']
            elif 'scenario' in scenario:
                scenario_text = scenario['scenario']
                if isinstance(scenario_text, str):
                    steps = [s.strip() for s in scenario_text.split('\n') if s.strip()]
        return steps
    
```

---

## simplify_control_flow
**given_state_not_actions_scanner.py** - 2 violation(s)

[!] WARNING (line 12)
Function "scan_story_node" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
class GivenStateNotActionsScanner(StoryScanner):
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        if isinstance(node, Story):
            story_data = node.data
            scenarios = story_data.get('scenarios', [])
            
            for scenario_idx, scenario in enumerate(scenarios):
                scenario_steps = self._get_scenario_steps(scenario)
                
                for step_idx, step in enumerate(scenario_steps):
                    if step.startswith('Given') or step.startswith('And'):
                        violation = self._check_given_is_action(step, node, scenario_idx, step_idx, rule_obj)
    # ... (truncated)
```

[!] WARNING (line 30)
Function "_get_scenario_steps" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _get_scenario_steps(self, scenario: Dict[str, Any]) -> List[str]:
        steps = []
        
        if isinstance(scenario, dict):
            # Try different possible keys
            if 'steps' in scenario:
                steps = scenario['steps']
            elif 'scenario' in scenario:
                # Scenario might be a string with newlines
                scenario_text = scenario['scenario']
                if isinstance(scenario_text, str):
                    steps = [s.strip() for s in scenario_text.split('\n') if s.strip()]
            elif 'given' in scenario or 'when' in scenario or 'then' in scenario:
    # ... (truncated)
```

---

## simplify_control_flow
**given_when_then_helpers_scanner.py** - 3 violation(s)

[!] WARNING (line 48)
Function "_get_helper_functions" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _get_helper_functions(self, tree: ast.AST, content: str) -> Set[str]:
        helpers = set()
        
        defined_helpers = self._get_defined_helper_functions(tree)
        helpers.update(defined_helpers.keys())
        
        # Also check for imported helper functions (from conftest, test_helpers, etc.)
        # Look for imports and add any functions that match helper patterns
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                module = node.module or ''
                if any(helper_mod in module for helper_mod in ['conftest', 'test_helpers', '_helpers']):
                    for alias in node.names:
    # ... (truncated)
```

[!] WARNING (line 69)
Function "_get_defined_helper_functions" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return helpers
    
    def _get_defined_helper_functions(self, tree: ast.AST) -> Dict[str, int]:
        helpers = {}
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_name = node.name
                for pattern in self.HELPER_PATTERNS:
                    if re.match(pattern, func_name, re.IGNORECASE):
                        helpers[func_name] = node.lineno
                        break
        
        return helpers
    
```

[!] WARNING (line 149)
Function "_find_inline_code_blocks" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return None
    
    def _find_inline_code_blocks(self, test_node: ast.FunctionDef, test_body_lines: List[str],
                                 helper_functions: Set[str], tree: ast.AST) -> List[Tuple[int, int, List[str]]]:
        blocks = []
        current_block_start = None
        current_block_lines = []
        
        # test_body_lines includes the def line, so body starts at lineno + 1
        body_start_line = test_node.lineno
        
        docstring_range = self._get_docstring_line_range(test_node)
        
        # Track if we're in a multi-line function call and parenthesis balance
        in_multiline_call = False
    # ... (truncated)
```

---

## simplify_control_flow
**import_placement_scanner.py** - 2 violation(s)

[!] WARNING (line 33)
Function "_find_import_section_end" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _find_import_section_end(self, lines: List[str]) -> int:
        import_section_end = 0
        
        # Skip leading blank lines
        while import_section_end < len(lines) and not lines[import_section_end].strip():
            import_section_end += 1
        
        # Skip module docstring (triple-quoted string)
        if import_section_end < len(lines):
            line = lines[import_section_end].strip()
            if line.startswith('"""') or line.startswith("'''"):
                # Find end of docstring
                quote_char = line[:3]
    # ... (truncated)
```

[!] WARNING (line 123)
Function "_skip_try_import_error_block" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return stripped == 'try:' or stripped.startswith('try:')
    
    def _skip_try_import_error_block(self, lines: List[str], start_line: int) -> int:
        if start_line >= len(lines):
            return start_line
        
        try_line = lines[start_line]
        base_indent = len(try_line) - len(try_line.lstrip())
        
        # Start after the 'try:' line
        current_line = start_line + 1
        
        # Skip through the try block (all lines indented more than the 'try' statement)
        while current_line < len(lines):
            line = lines[current_line]
    # ... (truncated)
```

---

## simplify_control_flow
**intention_revealing_names_scanner.py** - 4 violation(s)

[!] WARNING (line 68)
Function "_check_variable_names" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _check_variable_names(self, tree: ast.AST, file_path: Path, rule_obj: Any, content: str, domain_terms: set = None, docstring_ranges: List[tuple] = None) -> List[Dict[str, Any]]:
        violations = []
        
        if domain_terms is None:
            domain_terms = set()
        if docstring_ranges is None:
            docstring_ranges = []
        
        # Generic names that should be flagged (excluding acceptable context names and domain terms)
        generic_names = ['info', 'thing', 'stuff', 'temp']
        
        # Collect all acceptable single-letter variable NAMES (those defined in loops, comprehensions, exceptions, etc.)
        # We collect just the names (not line numbers) because once a var is defined in a loop,
    # ... (truncated)
```

[!] WARNING (line 170)
Function "_collect_loop_and_comprehension_var_names" has nesting depth of 8 - use guard clauses and extract nested blocks to reduce nesting

```python
            ).to_dict()
    
    def _collect_loop_and_comprehension_var_names(self, tree: ast.AST) -> set:
        acceptable_names = set()
        
        for node in ast.walk(tree):
            if isinstance(node, ast.For):
                self._add_target_var_names(node.target, acceptable_names)
            
            # Exception handlers
            elif isinstance(node, ast.ExceptHandler):
                if node.name:
                    acceptable_names.add(node.name)
            
            # List/Set/Dict comprehensions and generator expressions
    # ... (truncated)
```

[!] WARNING (line 280)
Function "_get_docstring_ranges" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _get_docstring_ranges(self, tree: ast.AST) -> List[tuple]:
        docstring_ranges = []
        
        def visit_node(node):
            if hasattr(node, 'body') and isinstance(node.body, list) and len(node.body) > 0:
                first_stmt = node.body[0]
                if isinstance(first_stmt, ast.Expr):
                    # Docstring is an expression with a constant string
                    if isinstance(first_stmt.value, (ast.Constant, ast.Str)):
                        if isinstance(first_stmt.value, ast.Constant):
                            docstring_value = first_stmt.value.value
                        else:  # ast.Str (Python < 3.8)
                            docstring_value = first_stmt.value.s
    # ... (truncated)
```

[!] WARNING (line 283)
Function "visit_node" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        docstring_ranges = []
        
        def visit_node(node):
            if hasattr(node, 'body') and isinstance(node.body, list) and len(node.body) > 0:
                first_stmt = node.body[0]
                if isinstance(first_stmt, ast.Expr):
                    # Docstring is an expression with a constant string
                    if isinstance(first_stmt.value, (ast.Constant, ast.Str)):
                        if isinstance(first_stmt.value, ast.Constant):
                            docstring_value = first_stmt.value.value
                        else:  # ast.Str (Python < 3.8)
                            docstring_value = first_stmt.value.s
                        
                        if isinstance(docstring_value, str):
                            start_line = first_stmt.lineno if hasattr(first_stmt, 'lineno') else None
    # ... (truncated)
```

---

## simplify_control_flow
**meaningful_context_scanner.py** - 2 violation(s)

[!] WARNING (line 31)
Function "_check_magic_numbers" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _check_magic_numbers(self, lines: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        content = '\n'.join(lines)
        
        # Common magic numbers that should be constants
        magic_number_patterns = [
            r'\b(200|404|500)\b',  # HTTP status codes
            r'\b(86400|3600|60)\b',  # Time constants (seconds in day/hour/minute)
            r'\b(1024|2048|4096)\b',  # Size constants
        ]
        
        for line_num, line in enumerate(lines, 1):
            for pattern in magic_number_patterns:
    # ... (truncated)
```

[!] WARNING (line 65)
Function "_check_numbered_variables" has nesting depth of 13 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _check_numbered_variables(self, content: str, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        try:
            # Parse the file as AST to get actual variable names (AST automatically excludes comments and string literals)
            tree = ast.parse(content, filename=str(file_path))
            
            numbered_var_pattern = re.compile(r'^\w+\d+$')  # word followed by number (entire match)
            
            def check_name(var_name: str, lineno: int):
                if numbered_var_pattern.match(var_name):
                    # Exclude common test patterns
                    if var_name.startswith('test') or var_name in ['test1', 'test2']:
    # ... (truncated)
```

---

## simplify_control_flow
**minimize_mutable_state_scanner.py** - 1 violation(s)

[!] WARNING (line 26)
Function "_check_mutable_patterns" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _check_mutable_patterns(self, lines: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        mutable_patterns = [
            r'\.push\s*\(',  # Array mutation (JS)
            r'\.pop\s*\(',  # Array mutation (JS/Python)
            r'\.splice\s*\(',  # Array mutation (JS)
            r'\+\+\s*;',  # Increment mutation (JS)
            r'--\s*;',  # Decrement mutation (JS)
            r'=\s*\{.*\}\s*\.\w+\s*=',  # Object mutation
            r'\.append\s*\(',  # List mutation (Python)
            r'\.extend\s*\(',  # List mutation (Python)
            r'\.insert\s*\(',  # List mutation (Python)
    # ... (truncated)
```

---

## simplify_control_flow
**no_guard_clauses_scanner.py** - 2 violation(s)

[!] WARNING (line 30)
Function "_check_guard_clause_patterns" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _check_guard_clause_patterns(self, lines: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        guard_patterns = [
            (r'if\s+(not\s+)?\w+\.exists\(\):', 'File existence check - test should fail if file missing'),
            # Type checks (isinstance)
            (r'if\s+(not\s+)?isinstance\([^)]+\):', 'Type check guard clause - test should fail if wrong type'),
            # Attribute checks (hasattr)
            (r'if\s+(not\s+)?hasattr\([^)]+\):', 'Attribute existence check - test should fail if attribute missing'),
            # Variable truthiness checks in test functions
            (r'if\s+(not\s+)?\w+:', 'Variable truthiness check - test should fail if variable is None/empty'),
        ]
        
    # ... (truncated)
```

[!] WARNING (line 103)
Function "_check_function_guard_clauses" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _check_function_guard_clauses(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        for node in ast.walk(func_node):
            if isinstance(node, ast.If):
                guard_patterns = [
                    self._is_file_exists_check,
                    self._is_type_check,
                    self._is_hasattr_check,
                    self._is_variable_truthiness_check,
                ]
                
                for pattern_check in guard_patterns:
    # ... (truncated)
```

---

## simplify_control_flow
**object_oriented_helpers_scanner.py** - 3 violation(s)

[!] WARNING (line 80)
Function "_parametrize_column_count" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        )

    def _parametrize_column_count(self, func_node: ast.FunctionDef) -> int:
        """Estimate number of parametrize columns from decorators."""
        for decorator in func_node.decorator_list:
            if isinstance(decorator, ast.Call):
                if isinstance(decorator.func, ast.Attribute) and decorator.func.attr == "parametrize":
                    if decorator.args:
                        first_arg = decorator.args[0]
                        if isinstance(first_arg, (ast.Constant, ast.Str)) and isinstance(first_arg.value, str):
                            columns = [c.strip() for c in first_arg.value.split(",") if c.strip()]
                            return len(columns)
        return 0

```

[!] WARNING (line 92)
Function "_given_when_then_calls" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return 0

    def _given_when_then_calls(self, func_node: ast.FunctionDef) -> int:
        """Count calls to given_/when_/then_ helpers inside a test function."""
        count = 0
        for inner in ast.walk(func_node):
            if isinstance(inner, ast.Call):
                func = inner.func
                name = ""
                if isinstance(func, ast.Name):
                    name = func.id
                elif isinstance(func, ast.Attribute):
                    name = func.attr
                if name.startswith(("given_", "when_", "then_")):
                    count += 1
    # ... (truncated)
```

[!] WARNING (line 107)
Function "_uses_helper" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return count

    def _uses_helper(self, func_node: ast.FunctionDef) -> bool:
        """Detect Helper/Factory usage inside a test function."""
        for inner in ast.walk(func_node):
            if isinstance(inner, ast.Call):
                # direct call name
                if isinstance(inner.func, ast.Name) and "helper" in inner.func.id.lower():
                    return True
                if isinstance(inner.func, ast.Attribute) and "helper" in inner.func.attr.lower():
                    return True
            if isinstance(inner, ast.Assign):
                for target in inner.targets:
                    if isinstance(target, ast.Name) and "helper" in target.id.lower():
                        return True
    # ... (truncated)
```

---

## simplify_control_flow
**one_concept_per_test_scanner.py** - 1 violation(s)

[!] WARNING (line 110)
Function "_detect_multiple_concepts" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations[0] if violations else None
    
    def _detect_multiple_concepts(self, test_node: ast.FunctionDef, content: str) -> List[str]:
        concepts = []
        
        # Detect different types of operations
        has_setup = False
        has_action = False
        has_validation = False
        has_cleanup = False
        
        for stmt in test_node.body:
            if isinstance(stmt, ast.Assign):
                has_setup = True
            elif isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
    # ... (truncated)
```

---

## simplify_control_flow
**parameterized_tests_scanner.py** - 1 violation(s)

[!] WARNING (line 9)
Function "scan" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
class ParameterizedTestsScanner(Scanner):
    
    def scan(
        self, 
        story_graph: Dict[str, Any], 
        rule_obj: Any = None,
        test_files: Optional[List['Path']] = None,
        code_files: Optional[List['Path']] = None,
        on_file_scanned: Optional[Any] = None
    ) -> List[Dict[str, Any]]:
        if not rule_obj:
            raise ValueError("rule_obj parameter is required for ParameterizedTestsScanner")
        
        violations = []
        story_map = StoryMap(story_graph)
    # ... (truncated)
```

---

## simplify_control_flow
**prefer_object_model_over_config_scanner.py** - 1 violation(s)

[!] WARNING (line 98)
Function "_is_in_exception_context" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return any(exc in file_str for exc in exception_paths)
    
    def _is_in_exception_context(self, lines: List[str], current_line: int) -> bool:
        # Look backwards to find the current function/method definition
        # We need to check if we're INSIDE an exception function, not just if one exists nearby
        current_indent = len(lines[current_line - 1]) - len(lines[current_line - 1].lstrip())
        
        # Look backwards to find the function definition at same or lower indentation
        for i in range(current_line - 2, max(0, current_line - 50), -1):
            line = lines[i]
            line_indent = len(line) - len(line.lstrip())
            
            # Found a function/method definition at same or lower indentation
            if line_indent <= current_indent and ('def ' in line):
                for pattern in self.exception_patterns:
    # ... (truncated)
```

---

## simplify_control_flow
**primitive_vs_object_scanner.py** - 1 violation(s)

[!] WARNING (line 69)
Function "_check_function_parameters" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def _check_function_parameters(self, func_node: ast.FunctionDef, content: str, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        # Skip presentation boundary methods
        if self._is_presentation_boundary(func_node.name, content, func_node):
            return violations
        
        # Skip __init__ methods - they often need primitives for construction
        if func_node.name == '__init__':
            return violations
        
        for arg in func_node.args.args:
            # Skip self and cls
    # ... (truncated)
```

---

## simplify_control_flow
**property_encapsulation_code_scanner.py** - 2 violation(s)

[!] WARNING (line 30)
Function "_check_encapsulation" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _check_encapsulation(self, class_node: ast.ClassDef, content: str, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        class_source = ast.get_source_segment(content, class_node) or ''
        
        for node in ast.walk(class_node):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        field_name = target.id
                        if not field_name.startswith('_') and not field_name.startswith('__'):
                            parent = self._get_parent_function(node)
                            if parent and isinstance(parent, ast.FunctionDef) and parent.name == '__init__':
                                # No code snippet for field assignment violations
    # ... (truncated)
```

[!] WARNING (line 87)
Function "_get_parent_function" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _get_parent_function(self, node: ast.AST) -> Optional[ast.FunctionDef]:
        for parent in ast.walk(node):
            if isinstance(parent, ast.FunctionDef):
                for child in ast.walk(parent):
                    if child == node:
                        return parent
        return None

```

---

## simplify_control_flow
**real_implementations_scanner.py** - 7 violation(s)

[!] WARNING (line 209)
Function "_has_production_code_imports" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return imports
    
    def _has_production_code_imports(
        self, imports: List[ast.Import | ast.ImportFrom], src_locations: List[str], project_path: Path
    ) -> bool:
        if not imports:
            return False
        
        for imp in imports:
            if isinstance(imp, ast.ImportFrom):
                module = imp.module or ''
                if self._is_production_module(module, src_locations, project_path):
                    return True
            elif isinstance(imp, ast.Import):
                for alias in imp.names:
    # ... (truncated)
```

[!] WARNING (line 279)
Function "_is_test_infrastructure_import" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def _is_test_infrastructure_import(self, imp: ast.Import | ast.ImportFrom) -> bool:
        test_infra_modules = ['pytest', 'pathlib', 'json', 'typing', 'unittest', 'mock', 'unittest.mock']
        
        if isinstance(imp, ast.ImportFrom):
            module = imp.module or ''
            return module.split('.')[0] in test_infra_modules if module else False
        elif isinstance(imp, ast.Import):
            for alias in imp.names:
                if alias.name.split('.')[0] in test_infra_modules:
                    return True
        return False
    
```

[!] WARNING (line 291)
Function "_is_empty_or_todo_only" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def _is_empty_or_todo_only(self, method: ast.FunctionDef, source_lines: List[str]) -> bool:
        if not method.body:
            return True
        
        method_start = method.lineno - 1  # Convert to 0-indexed
        method_end = method.end_lineno if hasattr(method, 'end_lineno') else method_start + 50
        if method_start < len(source_lines):
            method_source = source_lines[method_start:method_end]
        else:
            method_source = []
        
        has_todo = any('TODO' in line or 'FIXME' in line for line in method_source)
        if has_todo:
    # ... (truncated)
```

[!] WARNING (line 345)
Function "_has_production_code_calls" has nesting depth of 8 - use guard clauses and extract nested blocks to reduce nesting

```python
        return not has_actual_code
    
    def _has_production_code_calls(
        self, method: ast.FunctionDef, imports: List[ast.Import | ast.ImportFrom],
        src_locations: List[str], project_path: Path, file_path: Path = None, tree: ast.AST = None
    ) -> bool:
        # Find all function calls in the method
        calls = []
        for node in ast.walk(method):
            if isinstance(node, ast.Call):
                calls.append(node)
        
        if not calls:
            return False
        
    # ... (truncated)
```

[!] WARNING (line 393)
Function "_helper_calls_production_code" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def _helper_calls_production_code(
        self, helper_name: str, file_path: Path, tree: ast.AST,
        src_locations: List[str], project_path: Path
    ) -> bool:
        # Find the helper function definition in the current file
        helper_func = None
        
        # First check current file
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == helper_name:
                helper_func = node
                break
        
    # ... (truncated)
```

[!] WARNING (line 456)
Function "_file_has_production_code_calls" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return None
    
    def _file_has_production_code_calls(self, file_path: Path, src_locations: List[str], project_path: Path) -> bool:
        try:
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(file_path))
            imports = self._find_imports(tree)
            
            if self._has_production_code_imports(imports, src_locations, project_path):
                return True
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    if self._has_production_code_calls(node, imports, src_locations, project_path, file_path, tree):
                        return True
    # ... (truncated)
```

[!] WARNING (line 473)
Function "_is_production_function" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def _is_production_function(
        self, name: str, imports: List[ast.Import | ast.ImportFrom],
        src_locations: List[str], project_path: Path
    ) -> bool:
        for imp in imports:
            if isinstance(imp, ast.ImportFrom):
                if imp.module and self._is_production_module(imp.module, src_locations, project_path):
                    for alias in imp.names:
                        if alias.asname == name or alias.name == name:
                            return True
            elif isinstance(imp, ast.Import):
                for alias in imp.names:
                    if alias.asname == name or alias.name == name:
    # ... (truncated)
```

---

## simplify_control_flow
**resource_oriented_code_scanner.py** - 2 violation(s)

[!] WARNING (line 28)
Function "scan_cross_file" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return []
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
        test_files: Optional[List[Path]] = None,
        code_files: Optional[List[Path]] = None,
        all_test_files: Optional[List[Path]] = None,
        all_code_files: Optional[List[Path]] = None,
        status_writer: Optional[Any] = None,
        max_cross_file_comparisons: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        violations = []
        
        all_files = []
    # ... (truncated)
```

[!] WARNING (line 106)
Function "_class_uses_as_attribute" has nesting depth of 10 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def _class_uses_as_attribute(self, class_node: ast.ClassDef, loader_class_name: str, file_path: Path) -> bool:
        try:
            content = file_path.read_text(encoding='utf-8')
            # Simple check: see if loader class name appears in the file
            if loader_class_name not in content:
                return False
        except (UnicodeDecodeError, IOError):
            return False
        
        for node in class_node.body:
            if isinstance(node, ast.FunctionDef) and node.name == '__init__':
                for stmt in ast.walk(node):
                    if isinstance(stmt, ast.Assign):
    # ... (truncated)
```

---

## simplify_control_flow
**scanner_loader.py** - 1 violation(s)

[!] WARNING (line 23)
Function "_load_scanner_class" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        return self._load_scanner_class(scanner_module_path)
    
    def _load_scanner_class(self, scanner_module_path: str) -> Tuple[Optional[type], Optional[str]]:
        try:
            module_path, class_name = scanner_module_path.rsplit('.', 1)
            
            # Convert VerbNounScanner -> verb_noun
            import re
            scanner_name = re.sub(r'(?<!^)(?=[A-Z])', '_', class_name).lower().replace('_scanner', '').replace('scanner', '')
            
            paths_to_try = [
                module_path,  # Exact path from config
                f'agile_bot.src.scanners.{scanner_name}_scanner'
            ]
            
    # ... (truncated)
```

---

## simplify_control_flow
**scanner_registry.py** - 1 violation(s)

[!] WARNING (line 32)
Function "loads_scanner_class_with_error" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        return scanner_class
    
    def loads_scanner_class_with_error(self, scanner_module_path: str) -> tuple[Optional[Type[Scanner]], Optional[str]]:
        if not scanner_module_path:
            return None, None
        
        try:
            module_path, class_name = scanner_module_path.rsplit('.', 1)
            
            scanner_name = re.sub(r'(?<!^)(?=[A-Z])', '_', class_name).lower().replace('_scanner', '').replace('scanner', '')
            
            paths_to_try = [
                module_path,  # Exact path from config
                f'agile_bot.src.scanners.{scanner_name}_scanner'
            ]
    # ... (truncated)
```

---

## simplify_control_flow
**scanner_status_formatter.py** - 1 violation(s)

[!] WARNING (line 26)
Function "categorize_scanner_rules" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return lines

    def categorize_scanner_rules(self, validation_rules: List[Dict[str, Any]]) -> Dict:
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
    # ... (truncated)
```

---

## simplify_control_flow
**scenarios_cover_all_cases_scanner.py** - 1 violation(s)

[!] WARNING (line 12)
Function "scan_story_node" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
class ScenariosCoverAllCasesScanner(StoryScanner):
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        if isinstance(node, Story):
            story_data = node.data
            scenarios = story_data.get('scenarios', [])
            
            if len(scenarios) > 0:
                has_happy_path = False
                has_edge_case = False
                has_error_case = False
                
                for scenario_idx, scenario in enumerate(scenarios):
    # ... (truncated)
```

---

## simplify_control_flow
**scenarios_on_story_docs_scanner.py** - 1 violation(s)

[!] WARNING (line 72)
Function "_extract_story_names_from_epic" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python


def _extract_story_names_from_epic(epic_data: Dict[str, Any]) -> Set[str]:
    story_names = set()
    for story in epic_data.get('stories', []):
        if isinstance(story, dict) and 'name' in story:
            story_names.add(story['name'])
        elif isinstance(story, str):
            story_names.add(story)
    for story_group in epic_data.get('story_groups', []):
        for story in story_group.get('stories', []):
            if isinstance(story, dict) and 'name' in story:
                story_names.add(story['name'])
            elif isinstance(story, str):
                story_names.add(story)
    # ... (truncated)
```

---

## simplify_control_flow
**scenario_outline_scanner.py** - 1 violation(s)

[!] WARNING (line 12)
Function "scan_story_node" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
class ScenarioOutlineScanner(StoryScanner):
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        if isinstance(node, Story):
            story_data = node.data
            scenarios = story_data.get('scenarios', [])
            
            for scenario_idx, scenario in enumerate(scenarios):
                scenario_text = self._get_scenario_text(scenario)
                
                if 'Scenario Outline' in scenario_text:
                    has_examples = 'Examples:' in scenario_text or 'examples' in str(scenario).lower()
                    
    # ... (truncated)
```

---

## simplify_control_flow
**scenario_specific_given_scanner.py** - 2 violation(s)

[!] WARNING (line 11)
Function "scan_story_node" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
class ScenarioSpecificGivenScanner(StoryScanner):
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        if isinstance(node, Story):
            story_data = node.data
            scenarios = story_data.get('scenarios', [])
            background = story_data.get('background', [])
            
            for scenario_idx, scenario in enumerate(scenarios):
                scenario_steps = self._get_scenario_steps(scenario)
                
                if scenario_steps:
                    first_step = scenario_steps[0]
    # ... (truncated)
```

[!] WARNING (line 36)
Function "_get_scenario_steps" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _get_scenario_steps(self, scenario: Dict[str, Any]) -> List[str]:
        steps = []
        if isinstance(scenario, dict):
            if 'steps' in scenario:
                steps = scenario['steps']
            elif 'scenario' in scenario:
                scenario_text = scenario['scenario']
                if isinstance(scenario_text, str):
                    steps = [s.strip() for s in scenario_text.split('\n') if s.strip()]
        return steps

```

---

## simplify_control_flow
**setup_similarity_scanner.py** - 2 violation(s)

[!] WARNING (line 25)
Function "scan" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
    MIN_INTRA_DUP = 2  # within a single test

    def scan(
        self,
        story_graph: Dict[str, Any],
        rule_obj: Any = None,
        test_files: Optional[List["Path"]] = None,
        code_files: Optional[List["Path"]] = None,
        on_file_scanned: Optional[Any] = None,
    ) -> List[Dict[str, Any]]:
        violations: List[Dict[str, Any]] = []
        fingerprint_occurrences: Dict[Tuple[str, Tuple[str, ...]], List[Tuple[Path, int, str]]] = defaultdict(list)
        intra_duplicates: List[Dict[str, Any]] = []

        files = test_files or []
    # ... (truncated)
```

[!] WARNING (line 90)
Function "_collect_payloads" has nesting depth of 8 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations

    def _collect_payloads(self, func_node: ast.FunctionDef) -> List[Tuple[Tuple[str, Tuple[str, ...]], int]]:
        payloads: List[Tuple[Tuple[str, Tuple[str, ...]], int]] = []
        for node in ast.walk(func_node):
            dict_node = None
            lineno = getattr(node, "lineno", None)

            if isinstance(node, ast.Dict):
                dict_node = node
            elif isinstance(node, ast.Call):
                # look at args/kwargs for dicts
                for arg in list(node.args) + [kw.value for kw in node.keywords]:
                    if isinstance(arg, ast.Dict):
                        dict_node = arg
    # ... (truncated)
```

---

## simplify_control_flow
**specification_match_scanner.py** - 8 violation(s)

[!] WARNING (line 38)
Function "_check_test_method_names" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _check_test_method_names(self, tree: ast.AST, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        vague_patterns = [
            r'^test_(init|setup|create|new|get|set|run|execute|do|handle|process|check|verify|test)$',
            r'^test_\w+_(init|setup|create|new|get|set|run|execute|do|handle|process|check|verify)$',
        ]
        
        functions = Functions(tree)
        for function in functions.get_many_functions:
            if function.node.name.startswith('test_'):
                is_vague = False
                for pattern in vague_patterns:
    # ... (truncated)
```

[!] WARNING (line 111)
Function "_check_variable_names" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violation_dict
    
    def _check_variable_names(self, tree: ast.AST, content: str, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        # Generic names that suggest mismatch with specification
        generic_names = ['data', 'result', 'value', 'item', 'obj', 'thing', 'name', 'root', 'path', 'config']
        
        test_methods = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith('test_'):
                test_methods.append(node)
        
        for test_method in test_methods:
            for child in ast.walk(test_method):
    # ... (truncated)
```

[!] WARNING (line 137)
Function "_is_in_helper_call" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _is_in_helper_call(self, assign_node: ast.Assign, test_method: ast.FunctionDef) -> bool:
        if isinstance(assign_node.value, ast.Call):
            func = assign_node.value.func
            if isinstance(func, ast.Name):
                func_name = func.id
                # Helper functions typically start with verify_, given_, when_, then_
                if func_name.startswith(('verify_', 'given_', 'when_', 'then_', 'create_', 'setup_')):
                    return True
            elif isinstance(func, ast.Attribute):
                func_name = func.attr
                if func_name.startswith(('verify_', 'given_', 'when_', 'then_', 'create_', 'setup_')):
                    return True
        return False
    # ... (truncated)
```

[!] WARNING (line 151)
Function "_check_assertions" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def _check_assertions(self, tree: ast.AST, content: str, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        # Patterns that suggest implementation detail assertions
        implementation_patterns = [
            r'\._(private|internal|_flag|_state|_cache)',
            r'\.called\b',  # Mock call checks
            r'\.assert_called',  # Mock assertion
            r'\._validate',  # Internal validation
        ]
        
        test_methods = []
        for node in ast.walk(tree):
    # ... (truncated)
```

[!] WARNING (line 221)
Function "_extract_domain_terms" has nesting depth of 12 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _extract_domain_terms(self, story_graph: Dict[str, Any]) -> set:
        domain_terms = set()
        
        if not story_graph:
            return domain_terms
        
        epics = story_graph.get('epics', [])
        for epic in epics:
            if isinstance(epic, dict):
                epic_name = epic.get('name', '')
                if epic_name:
                    domain_terms.update(self._extract_words_from_text(epic_name))
                
    # ... (truncated)
```

[!] WARNING (line 335)
Function "_find_matching_story" has nesting depth of 12 - use guard clauses and extract nested blocks to reduce nesting

```python
        return None
    
    def _find_matching_story(self, scenario: Optional[str], test_name: str, story_graph: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if not story_graph:
            return None
        
        scenario_name = None
        if scenario:
            # Look for "SCENARIO: <name>" pattern in docstring
            scenario_match = re.search(r'SCENARIO:\s*(.+?)(?:\n|$)', scenario, re.IGNORECASE)
            if scenario_match:
                scenario_name = scenario_match.group(1).strip()
        
        test_keywords = set(self._extract_words_from_text(test_name))
        
    # ... (truncated)
```

[!] WARNING (line 374)
Function "_check_variable_matches" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return None
    
    def _check_variable_matches(self, test_method: ast.FunctionDef, story: Dict[str, Any], 
                                domain_terms: set, rule_obj: Any, file_path: Path) -> List[Dict[str, Any]]:
        violations = []
        
        variable_names = []
        for node in ast.walk(test_method):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        variable_names.append((target.id, node.lineno if hasattr(node, 'lineno') else None))
        
        for var_name, line_number in variable_names:
            var_name_lower = var_name.lower()
    # ... (truncated)
```

[!] WARNING (line 418)
Function "_check_assertion_matches" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _check_assertion_matches(self, test_method: ast.FunctionDef, story: Dict[str, Any], 
                                 rule_obj: Any, file_path: Path) -> List[Dict[str, Any]]:
        violations = []
        
        acceptance_criteria = story.get('acceptance_criteria', [])
        if not acceptance_criteria:
            return violations
        
        assertions = []
        has_pytest_raises = False
        has_helper_assertions = False
        
        for node in ast.walk(test_method):
    # ... (truncated)
```

---

## simplify_control_flow
**standard_data_reuse_scanner.py** - 1 violation(s)

[!] WARNING (line 26)
Function "scan_file" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
    }

    def scan_file(self, file_path: Path, rule_obj: Any = None, story_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations: List[Dict[str, Any]] = []

        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations

        content, lines, tree = parsed

        for func in [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name.startswith("test")]:
            dict_keysets = []
            for node in ast.walk(func):
                # Capture dict literals passed into calls or assigned
    # ... (truncated)
```

---

## simplify_control_flow
**story_map.py** - 1 violation(s)

[!] WARNING (line 35)
Function "map_location" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return self.data.get('name', '')
    
    def map_location(self, field: str = 'name') -> str:
        if isinstance(self, Epic):
            return f"epics[{self.epic_idx}].{field}"
        elif isinstance(self, SubEpic):
            if self.sub_epic_path:
                path_str = "".join([f".sub_epics[{idx}]" for idx in self.sub_epic_path])
                return f"epics[{self.epic_idx}]{path_str}.{field}"
            else:
                return f"epics[{self.epic_idx}].{field}"
        elif isinstance(self, Story):
            path_parts = [f"epics[{self.epic_idx}]"]
            if self.sub_epic_path:
                for idx in self.sub_epic_path:
    # ... (truncated)
```

---

## simplify_control_flow
**swallowed_exceptions_scanner.py** - 1 violation(s)

[!] WARNING (line 26)
Function "_check_swallowed_exceptions" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _check_swallowed_exceptions(self, tree: ast.AST, file_path: Path, rule_obj: Any, content: str) -> List[Dict[str, Any]]:
        violations = []
        
        try_blocks = TryBlocks(tree)
        for try_block in try_blocks.get_many_try_blocks:
            for handler in try_block.exception_handlers:
                handler_body = handler.body
                if len(handler_body) == 0:
                    line_number = handler.lineno if hasattr(handler, 'lineno') else None
                    violation = self._create_violation_with_snippet(
                        rule_obj=rule_obj,
                        violation_message=f'Empty except block at line {line_number} - exceptions must be logged or rethrown, never swallowed',
                        file_path=file_path,
    # ... (truncated)
```

---

## simplify_control_flow
**test_file_naming_scanner.py** - 3 violation(s)

[!] WARNING (line 99)
Function "_get_sub_epics_spanned_by_test_methods" has nesting depth of 8 - use guard clauses and extract nested blocks to reduce nesting

```python
        ).to_dict()
    
    def _get_sub_epics_spanned_by_test_methods(self, file_path: Path, story_graph: Dict[str, Any]) -> set:
        sub_epics = set()
        
        try:
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(file_path))
            
            # Find all test methods
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    if node.name.startswith('Test'):
                        class_name = node.name
                        
    # ... (truncated)
```

[!] WARNING (line 124)
Function "_find_sub_epic_for_method" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        return sub_epics
    
    def _find_sub_epic_for_method(self, method_name: str, class_name: str, story_graph: Dict[str, Any]) -> Optional[str]:
        method_name_norm = self._to_snake_case(method_name)
        story_name_from_class = class_name[4:] if class_name.startswith('Test') else class_name
        story_name_normalized = self._to_snake_case(story_name_from_class)
        
        epics = story_graph.get('epics', [])
        
        for epic in epics:
            sub_epics = epic.get('sub_epics', [])
            for sub_epic in sub_epics:
                sub_epic_name = sub_epic.get('name', '')
                sub_epic_name_norm = self._to_snake_case(sub_epic_name) if sub_epic_name else ''
                
    # ... (truncated)
```

[!] WARNING (line 189)
Function "_find_closest_sub_epic_names" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return None
    
    def _find_closest_sub_epic_names(self, file_name: str, sub_epic_names: List[str], max_suggestions: int = 5) -> List[str]:
        if not sub_epic_names:
            return []
        
        scored_names = []
        file_name_lower = file_name.lower()
        
        for sub_epic_name in sub_epic_names:
            sub_epic_lower = sub_epic_name.lower()
            
            # Simple similarity: check for common substrings
            score = 0
            
    # ... (truncated)
```

---

## simplify_control_flow
**type_safety_scanner.py** - 2 violation(s)

[!] WARNING (line 152)
Function "_check_parameters_get_pattern" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _check_parameters_get_pattern(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any, content: str) -> List[Dict[str, Any]]:
        violations = []
        found_lines = set()  # Track lines to avoid duplicate violations
        
        for node in ast.walk(func_node):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Attribute):
                    if node.func.attr == 'get':
                        if isinstance(node.func.value, ast.Name):
                            var_name = node.func.value.id
                            if var_name in ('parameters', 'params', 'kwargs'):
                                line_no = node.lineno
                                if line_no not in found_lines:
    # ... (truncated)
```

[!] WARNING (line 183)
Function "_is_dict_any_annotation" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations[:3]
    
    def _is_dict_any_annotation(self, annotation: ast.AST) -> bool:
        if isinstance(annotation, ast.Subscript):
            if isinstance(annotation.value, ast.Name):
                if annotation.value.id == 'Dict':
                    if isinstance(annotation.slice, ast.Tuple):
                        if len(annotation.slice.elts) >= 2:
                            second_arg = annotation.slice.elts[1]
                            if isinstance(second_arg, ast.Name) and second_arg.id == 'Any':
                                return True
            # Also check for dict[str, Any] (lowercase, Python 3.9+)
            if isinstance(annotation.value, ast.Name):
                if annotation.value.id == 'dict':
                    if isinstance(annotation.slice, ast.Tuple):
    # ... (truncated)
```

---

## simplify_control_flow
**unnecessary_parameter_passing_scanner.py** - 3 violation(s)

[!] WARNING (line 56)
Function "_collect_instance_attributes" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _collect_instance_attributes(self, class_node: ast.ClassDef) -> set:
        attrs = set()
        
        # Find __init__ method
        for node in class_node.body:
            if isinstance(node, ast.FunctionDef) and node.name == '__init__':
                # Find all self.attr = ... assignments
                for stmt in ast.walk(node):
                    if isinstance(stmt, ast.Assign):
                        for target in stmt.targets:
                            if isinstance(target, ast.Attribute):
                                if isinstance(target.value, ast.Name) and target.value.id == 'self':
                                    attrs.add(target.attr)
    # ... (truncated)
```

[!] WARNING (line 115)
Function "_parameter_used_like_instance_attr" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return violations
    
    def _parameter_used_like_instance_attr(self, method_node: ast.FunctionDef, param_name: str) -> bool:
        # Look for patterns where the parameter is used directly (not modified)
        # This suggests it could be accessed via self instead
        for node in ast.walk(method_node):
            # If parameter is used in attribute access (e.g., param.property), it's likely not an instance attr
            if isinstance(node, ast.Attribute):
                if isinstance(node.value, ast.Name) and node.value.id == param_name:
                    return False  # Parameter is used as object, not as simple value
            
            # If parameter is assigned to, it's being modified, so it's not just passing through
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == param_name:
    # ... (truncated)
```

[!] WARNING (line 133)
Function "_check_property_extraction" has nesting depth of 11 - use guard clauses and extract nested blocks to reduce nesting

```python
        return True
    
    def _check_property_extraction(self, method_node: ast.FunctionDef, instance_attrs: set,
                                  file_path: Path, rule_obj: Any, lines: List[str], content: str) -> List[Dict[str, Any]]:
        violations = []
        
        # Look for patterns like: var = self.property; self._method(var)
        # Also handles nested: var = self.behavior.folder; self._method(var)
        assignments = []
        for i, stmt in enumerate(method_node.body):
            if isinstance(stmt, ast.Assign):
                for target in stmt.targets:
                    if isinstance(target, ast.Name):
                        attr_path = self._extract_self_attribute_path(stmt.value)
                        if attr_path:
    # ... (truncated)
```

---

## simplify_control_flow
**verb_noun_scanner.py** - 1 violation(s)

[!] WARNING (line 410)
Function "_check_noun_only" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return None
    
    def _check_noun_only(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        try:
            tokens, tags = self._get_tokens_and_tags(name)
            
            if not tags:
                return None
            
            has_verb = any(self._is_verb(tag[1]) for tag in tags)
            
            # Handle hyphenated verbs (e.g., "Auto-Run", "Re-execute", "Auto-Confirm")
            # When a noun is in front of a verb with a dash, we should accept it as valid
            if not has_verb and tokens:
                first_token = tokens[0]
    # ... (truncated)
```

---

## simplify_control_flow
**vocabulary_helper.py** - 2 violation(s)

[!] WARNING (line 74)
Function "is_agent_noun" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
    
    @staticmethod
    def is_agent_noun(word: str) -> tuple[bool, Optional[str], Optional[str]]:
        """
        Check if word is an agent noun (doer of action).
        Returns: (is_agent, base_verb, suffix) or (False, None, None)
        
        Examples:
            'Manager' -> (True, 'manage', 'er')
            'Processor' -> (True, 'process', 'or')
            'Portfolio' -> (False, None, None)
        """
        word_lower = word.lower()
        
        for suffix in VocabularyHelper.AGENT_SUFFIXES:
    # ... (truncated)
```

[!] WARNING (line 171)
Function "is_actor_or_role" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
    
    @staticmethod
    def is_actor_or_role(word: str) -> bool:
        """
        Check if word represents an actor or role (person, system, agent).
        Uses WordNet to check if word is a hyponym of 'person' or 'system'.
        
        Examples:
            'customer' -> True (person who buys)
            'user' -> True (person who uses)
            'developer' -> True (person who develops)
            'system' -> True (computing system)
            'api' -> True (system interface)
            'order' -> False (not a person/system)
        """
    # ... (truncated)
```

---

## simplify_control_flow
**json_scope.py** - 2 violation(s)

[!] WARNING (line 42)
Function "to_dict" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return self.scope.file_filter
    
    def to_dict(self) -> dict:
        """Convert Scope to dict with filtered content for panel display."""
        # Start with basic scope criteria
        result = {
            'type': self.scope.type.value,
            'filter': ', '.join(self.scope.value) if self.scope.value else '',
            'content': None,
            'graphLinks': []
        }
        
        # Add filtered content based on scope type
        if self.scope.type.value in ('story', 'showAll'):
            # Get filtered story graph
    # ... (truncated)
```

[!] WARNING (line 115)
Function "_enrich_sub_epic_with_links" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
                    self._enrich_sub_epic_with_links(sub_epic, test_dir, docs_stories_map, epic['name'])
    
    def _enrich_sub_epic_with_links(self, sub_epic: dict, test_dir: Path, docs_stories_map: Path, epic_name: str, parent_path: str = None):
        """Recursively enrich sub-epic with test file and document links."""
        # Build the document path (epic/sub-epic hierarchy)
        if parent_path:
            sub_epic_doc_folder = Path(parent_path) / f"⚙️ {sub_epic['name']}"
        else:
            sub_epic_doc_folder = docs_stories_map / f"🎯 {epic_name}" / f"⚙️ {sub_epic['name']}"
        
        # Initialize links array
        if 'links' not in sub_epic:
            sub_epic['links'] = []
        
        # Add test file link if test_file is specified
    # ... (truncated)
```

---

## simplify_control_flow
**markdown_scope.py** - 1 violation(s)

[!] WARNING (line 16)
Function "serialize" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        self.workspace_directory = workspace_directory or Path.cwd()
    
    def serialize(self) -> str:
        """Convert Scope to Markdown string - delegates to result domain adapters."""
        lines = []
        
        lines.append(self.format_header(2, "🎯 Scope"))
        lines.append("")
        
        # Display scope filter
        if self.scope.type.value == 'all':
            filter_display = "all (entire project)"
        else:
            filter_display = ', '.join(self.scope.value) if isinstance(self.scope.value, list) else str(self.scope.value) if self.scope.value else "all"
        
    # ... (truncated)
```

---

## simplify_control_flow
**scope.py** - 2 violation(s)

[!] WARNING (line 154)
Function "filter_files" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def filter_files(self, file_list: List[Path]) -> List[Path]:
        """Filter file list to only files matching this filter."""
        if not self.include_patterns and not self.exclude_patterns:
            return file_list
        
        from pathlib import PurePath
        filtered = []
        
        for file_path in file_list:
            file_str = str(file_path).replace('\\', '/')
            file_path_obj = PurePath(file_str)
            
            if self.include_patterns:
    # ... (truncated)
```

[!] WARNING (line 343)
Function "_get_file_results" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
            return None
    
    def _get_file_results(self) -> List[Path]:
        """Get filtered file list."""
        import glob as glob_module
        
        all_files = []
        paths = self.value if isinstance(self.value, list) else [self.value]
        
        for path_str in paths:
            has_glob = any(char in path_str for char in ['*', '?', '['])
            
            if has_glob:
                if not Path(path_str).is_absolute():
                    pattern = str(self.workspace_directory / path_str)
    # ... (truncated)
```

---

## simplify_control_flow
**scoping_parameter.py** - 1 violation(s)

[!] WARNING (line 302)
Function "_add_epic_stories" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
            self._add_story_name(story, story_names)
    
    def _add_epic_stories(self, increment: Dict[str, Any], story_names: Set[str]) -> None:
        """Extract story names from increment epics.
        
        Only supports sub_epics format: epics[].sub_epics[].stories[] or story_groups[].stories[]
        Does NOT support features format.
        """
        for epic in increment.get('epics', []):
            # Handle sub_epics format (story map structure)
            for sub_epic in epic.get('sub_epics', []):
                # Check for direct stories array
                for story in sub_epic.get('stories', []):
                    self._add_story_name(story, story_names)
                
    # ... (truncated)
```

---

## simplify_control_flow
**tty_scope.py** - 1 violation(s)

[!] WARNING (line 21)
Function "serialize" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

```python
        self.scope = scope
    
    def serialize(self) -> str:
        """Convert Scope to TTY string - delegates to result domain adapters."""
        lines = []
        
        lines.append(self.add_bold("🎯 Scope"))
        
        # Display scope filter
        if self.scope.type.value == 'all':
            filter_display = "all (entire project)"
        else:
            filter_display = ', '.join(self.scope.value) if isinstance(self.scope.value, list) else str(self.scope.value) if self.scope.value else "all"
        
        lines.append(f"🎯 {self.add_bold('Current Scope:')} {filter_display}")
    # ... (truncated)
```

---

## simplify_control_flow
**build_action.py** - 2 violation(s)

[!] WARNING (line 115)
Function "_replace_schema_placeholders" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return behavior_to_content.get(self.behavior.name, [])
    
    def _replace_schema_placeholders(self, instructions) -> None:
        """Replace {{schema}} and {{description}} placeholders in base_instructions with template references."""
        base_instructions = instructions.get('base_instructions', [])
        new_instructions = []
        
        template = self.story_graph_template
        description_lines_list = []
        schema_explanation_lines = []
        
        if template and template.exists:
            template_path = template.template_path
            if template_path:
                # Create relative path reference: bot_name/behaviors/behavior_name/content/story_graph/template_filename
    # ... (truncated)
```

[!] WARNING (line 245)
Function "_replace_content_with_file_references" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        instructions.set('rules', all_rules)
    
    def _replace_content_with_file_references(self, instructions) -> None:
        """Replace full content (templates, configs, rules) with file path references."""
        bot_dir = self.behavior.bot_paths.bot_directory
        
        # NOTE: Keep template_path and config_path as absolute paths for clickable links in frontend
        # Do NOT convert to relative references anymore
        # template_path = instructions.get('template_path')
        # if template_path:
        #     template_reference = self._convert_path_to_reference(template_path, bot_dir)
        #     instructions._data['template_path'] = template_reference
        
        # config_path = instructions.get('config_path')
        # if config_path:
    # ... (truncated)
```

---

## simplify_control_flow
**tty_required_context.py** - 1 violation(s)

[!] WARNING (line 13)
Function "serialize" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        self.required_context = required_context
    
    def serialize(self) -> str:
        """Convert RequiredContext to TTY string."""
        lines = []
        
        # Display key questions
        key_questions = self.required_context.key_questions.questions
        if key_questions:
            lines.append("")
            lines.append(self.add_bold("Key Questions:"))
            if isinstance(key_questions, list):
                for question in key_questions:
                    lines.append(f"- {question}")
            elif isinstance(key_questions, dict):
    # ... (truncated)
```

---

## simplify_control_flow
**tty_strategy.py** - 1 violation(s)

[!] WARNING (line 13)
Function "serialize" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        self.strategy = strategy
    
    def serialize(self) -> str:
        """Convert Strategy to TTY string."""
        lines = []
        
        # Display strategy criteria (decisions)
        strategy_criterias = self.strategy.strategy_criterias.strategy_criterias
        if strategy_criterias:
            lines.append("")
            lines.append(self.add_bold("Decisions:"))
            for criteria_key, criteria in strategy_criterias.items():
                lines.append("")
                question = criteria.question
                if question:
    # ... (truncated)
```

---

## simplify_control_flow
**render_instruction_builder.py** - 3 violation(s)

[!] WARNING (line 31)
Function "_add_spec_instructions" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return working_dir

    def _add_spec_instructions(self, base_instructions_list: List[str], executed_specs: List['RenderSpec'], template_specs: List['RenderSpec']) -> None:
        if executed_specs:
            # Find the end of context sources section (after the blank line following context sources)
            # Context sources typically look like:
            # [0]: "**Look for context in the following locations:**"
            # [1]: "- in this message and chat history"
            # [2]: "- in `{workspace}/docs/context/`"
            # [3]: "- generated files in `{workspace}/docs/stories/`"
            # [4]: "  clarification.json, planning.json"
            # [5]: ""  <- blank line
            # We want to insert AFTER this blank line
            insert_position = 1  # Default to position 1 if we can't find the pattern
            for i, line in enumerate(base_instructions_list):
    # ... (truncated)
```

[!] WARNING (line 149)
Function "_process_for_each_loops" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        parts.append('')
    
    def _process_for_each_loops(self, instructions_list: List[str], render_specs: List['RenderSpec']) -> List[str]:
        """Process {{#for_each_render_config}}...{{/for_each_render_config}} loops."""
        new_instructions = []
        i = 0
        while i < len(instructions_list):
            line = instructions_list[i]
            
            if '{{#for_each_render_config}}' in line:
                # Find the end of the loop
                loop_start = i + 1
                loop_end = None
                for j in range(loop_start, len(instructions_list)):
                    if '{{/for_each_render_config}}' in instructions_list[j]:
    # ... (truncated)
```

[!] WARNING (line 187)
Function "_expand_template_for_spec" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return new_instructions
    
    def _expand_template_for_spec(self, template_lines: List[str], spec: 'RenderSpec') -> List[str]:
        """Expand template lines with render_config placeholders replaced."""
        # Handle instructions - can be string or list
        instructions = spec.config_data.get('instructions', 'No instructions provided')
        if isinstance(instructions, list):
            instructions = '\n'.join(instructions)
        
        replacements = {
            '{render_config.name}': spec.name,
            '{render_config.instructions}': instructions,
            '{render_config.synchronizer}': spec.synchronizer.synchronizer_class_path if spec.synchronizer else 'N/A',
            '{render_config.template}': spec.config_data.get('template', 'N/A'),
            '{render_config.input}': spec.input or 'N/A',
    # ... (truncated)
```

---

## simplify_control_flow
**json_strategy_action.py** - 1 violation(s)

[!] WARNING (line 66)
Function "to_dict" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return self.action.typical_assumptions
    
    def to_dict(self) -> dict:
        """Convert StrategyAction to dict."""
        # #region agent log
        import time
        with open(r'c:\dev\augmented-teams\.cursor\debug.log', 'a', encoding='utf-8') as f:
            f.write(json.dumps({'sessionId':'debug-session','runId':'initial','hypothesisId':'H1','location':'json_strategy_action.py:67','message':'to_dict called','data':{'behavior_name':self.action.behavior.name if self.action.behavior else None,'has_strategy':bool(self.action.strategy)},'timestamp':int(time.time()*1000)})+'\n')
        # #endregion
        
        result = {
            'action_name': self.action.action_name,
            'description': self.action.description,
            'order': self.action.order,
            'next_action': self.action.next_action,
    # ... (truncated)
```

---

## simplify_control_flow
**strategy_action.py** - 1 violation(s)

[!] WARNING (line 103)
Function "_format_instructions_for_display" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
            pass  # Silently skip if can't load clarifications
    
    def _format_instructions_for_display(self, instructions) -> str:
        """Format strategy data for REPL display."""
        # Get base formatting first (includes scope warning if set)
        output_lines = super()._format_instructions_for_display(instructions).split('\n')
        
        # Get the instruction data
        instructions_dict = instructions.to_dict()
        
        # Format strategy criteria
        strategy_criteria = instructions_dict.get('strategy_criteria', {})
        if strategy_criteria:
            output_lines.append("")
            output_lines.append("**Decisions:**")
    # ... (truncated)
```

---

## simplify_control_flow
**validate_action.py** - 3 violation(s)

[!] WARNING (line 32)
Function "_prepare_instructions" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return self._rules

    def _prepare_instructions(self, instructions, context: ValidateActionContext):
        """Prepare validation instructions with rules and validation data."""
        # Get rules with file paths for AI to read
        rules_text = self._format_rules_with_file_paths()
        
        # Get story graph schema path
        schema_path = self.behavior.bot_paths.workspace_directory / 'docs' / 'stories' / 'story-graph.json'
        
        # Get scope description
        scope_text = self._format_scope_description(context)
        
        # Run scanners and get formatted results
        scanner_output = self._run_scanners_and_format_results(context)
    # ... (truncated)
```

[!] WARNING (line 104)
Function "_run_scanners_and_format_results" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
            instructions._data['rules'] = rule_files

    def _run_scanners_and_format_results(self, context: ValidateActionContext) -> str:
        """Run validation scanners and format results for display in instructions."""
        logger.info('Running scanners for instructions display...')
        
        try:
            # Execute validation synchronously
            result = self._executor.execute_synchronous(context)
            
            # Get the report path from the result
            instructions_dict = result.get('instructions', {})
            report_link = instructions_dict.get('report_link', '')
            
            # Read the generated validation report file
    # ... (truncated)
```

[!] WARNING (line 147)
Function "_format_scope_description" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
            return f'Error running scanners: {e}\n\nPlease review the validation report file in docs/stories/reports/'
    
    def _format_scope_description(self, context: ValidateActionContext) -> str:
        """Format scope description for validation instructions."""
        if context.scope:
            scope_type = context.scope.type.value  # ScopeType enum
            scope_value = context.scope.value
            
            if scope_type == 'epic':
                return f"epic(s): {', '.join(scope_value)}"
            elif scope_type == 'story':
                return f"story/stories: {', '.join(scope_value)}"
            elif scope_type == 'files':
                return f"file(s): {', '.join(scope_value)}"
            else:
    # ... (truncated)
```

---

## simplify_control_flow
**validation_scope.py** - 1 violation(s)

[!] WARNING (line 161)
Function "_get_explicit_files_for_behavior" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
            return 'src'

    def _get_explicit_files_for_behavior(self, file_key, behavior_dir):
        # Check if we have a files scope - if so, try both file_key and 'test'/'src' explicitly
        has_files_scope = (self._parameters.get('scope', {}).get('type') == 'files' if isinstance(self._parameters.get('scope'), dict) else False)
        
        if file_key in self._scope_config:
            files = self.files(file_key)
            if files:
                return files
        
        if behavior_dir in self._scope_config:
            files = self.files(behavior_dir)
            if files:
                return files
    # ... (truncated)
```

---

## simplify_control_flow
**cursor_command_visitor.py** - 1 violation(s)

[!] WARNING (line 146)
Function "_build_behavior_command" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return "\n".join(lines)
    
    def _build_behavior_command(self, behavior_name: str) -> str:
        bot_dir_str = str(self.bot_directory).replace('\\', '\\')
        workspace_str = str(self.workspace_root).replace('\\', '\\')
        
        behavior = self.bot.behaviors.find_by_name(behavior_name)
        if not behavior:
            return ""
        
        action_names = []
        if self.data_collector:
            action_names = self.data_collector.get_behavior_actions(behavior)
        
        behavior_name_underscore = behavior_name.replace('-', '_')
    # ... (truncated)
```

---

## stop_writing_useless_comments
**utils.py** - 7 violation(s)

[X] ERROR (line 90)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

def build_test_file_link(test_file: str, workspace_directory: Path, story_file_path: Optional[Path] = None) -> str:
    """
    Build link to test file.
    
    Args:
        test_file: Name of test file (e.g., 'test_example.py')
        workspace_directory: Path to workspace directory
        story_file_path: Optional path to story markdown file (generates absolute path from workspace root)
    
    Returns:
        Markdown link string like ' | [Test](path/to/test.py)' or empty string if not found
    """
    if not test_file:
```

[X] ERROR (line 132)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

def build_test_class_link(test_file: str, test_class: str, workspace_directory: Path, story_file_path: Optional[Path] = None) -> str:
    """
    Build link to test class with line number.
    
    Args:
        test_file: Name of test file (e.g., 'test_example.py')
        test_class: Name of test class (e.g., 'TestMyFeature')
        workspace_directory: Path to workspace directory
        story_file_path: Optional path to story markdown file (generates absolute path from workspace root)
    
    Returns:
        Markdown link string like ' | [Test](path/to/test.py#L123)' or empty string if not found
    """
    if not test_file or not test_class or test_class == '?':
```

[X] ERROR (line 205)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

def build_test_method_link(test_file: str, test_method: str, workspace_directory: Path, story_file_path: Optional[Path] = None) -> str:
    """
    Build link to test method with line number.
    
    Args:
        test_file: Name of test file (e.g., 'test_example.py')
        test_method: Name of test method (e.g., 'test_my_scenario')
        workspace_directory: Path to workspace directory
        story_file_path: Optional path to story markdown file (generates absolute path from workspace root)
    
    Returns:
        Markdown link string like ' | [Test](path/to/test.py#L456)' or empty string if not found
    """
    if not test_file or not test_method or test_method == '?':
```

[X] ERROR (line 278)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

def find_test_class_line(test_file_path: Path, test_class_name: str) -> Optional[int]:
    """
    Find the line number of a test class definition.
    
    Args:
        test_file_path: Path to test file
        test_class_name: Name of test class
    
    Returns:
        Line number (1-based) or None if not found
    """
    if not test_file_path.exists() or not test_class_name or test_class_name == '?':
```

[X] ERROR (line 309)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

def find_test_method_line(test_file_path: Path, test_method_name: str) -> Optional[int]:
    """
    Find the line number of a test method definition.
    
    Args:
        test_file_path: Path to test file
        test_method_name: Name of test method
    
    Returns:
        Line number (1-based) or None if not found
    """
    if not test_file_path.exists() or not test_method_name or test_method_name == '?':
```

[X] ERROR (line 299)
Useless comment: "# Return None so we don't create a broken link" - delete it or improve the code instead

```python
    except SyntaxError:
        # If there's a syntax error, we can't parse the file
        # Return None so we don't create a broken link
        return None
```

[X] ERROR (line 330)
Useless comment: "# Return None so we don't create a broken link" - delete it or improve the code instead

```python
    except SyntaxError:
        # If there's a syntax error, we can't parse the file
        # Return None so we don't create a broken link
        return None
```

---

## stop_writing_useless_comments
**action.py** - 25 violation(s)

[X] ERROR (line 102)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def description(self) -> str:
        """Get the action description from base config."""
        return self._base_config.get('description', '')
```

[X] ERROR (line 107)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def help(self) -> Dict[str, Any]:
        """Get parameter help for this action.
        
        Returns a dict with:
        - description: Action description
        - parameters: List of dicts with 'name', 'type', 'description' for each parameter
        """
        import dataclasses
```

[X] ERROR (line 137)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _get_type_string(self, python_type) -> str:
        """Convert Python type hint to string for help display."""
        if python_type is type(None):
```

[X] ERROR (line 170)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _get_parameter_description(self, param_name: str) -> str:
        """Get meaningful description for a parameter."""
        if 'answers' in param_name or 'key_questions_answered' in param_name:
```

[X] ERROR (line 199)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _replace_context_placeholders(self, instructions_list: List[str]) -> List[str]:
        """Replace standard context placeholders with actual values.
        
        For action-specific placeholders, override this method in the subclass.
        """
        replacements = {
```

[X] ERROR (line 218)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _load_scope_from_state(self) -> Optional[Scope]:
        """Get current scope from bot instance, not from stale state file.
        
        Uses the bot's current scope which reflects the actual CLI state,
        rather than loading from behavior_action_state.json which may be stale.
        """
        # Use bot's current scope if available (this reflects actual CLI state)
```

[X] ERROR (line 385)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def get_instructions(self, context: ActionContext = None) -> Instructions:
        """Returns AI instructions and saves any guardrails provided in context.
        
        This is the single operation for all actions:
        - Saves guardrails if provided (answers, decisions, evidence, etc.)
        - Builds and returns instructions for AI
        
        This is a template method. Subclasses override _prepare_instructions() to customize.
        """
        if context is None:
```

[X] ERROR (line 434)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _save_guardrails_if_provided(self, context: ActionContext):
        """Save guardrails if provided in context parameters.
        
        This is common logic for all actions. Any action can receive and save guardrails:
        - Clarify action: answers, evidence
        - Strategy action: decisions, assumptions
        - Build action: build_config, decisions
        - etc.
        
        Args:
            context: Action context that may contain guardrail data
        """
        # Check for clarify data (answers, evidence)
```

[X] ERROR (line 501)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _load_behavior_guardrails(self, instructions):
        """Load behavior-level guardrails (key questions and evidence) if available.
        
        Note: For clarify action, guardrails are set in _prepare_instructions() instead.
        This method is a fallback for other actions that don't override _prepare_instructions().
        """
        try:
```

[X] ERROR (line 528)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _load_all_saved_guardrails(self, instructions):
        """Load all saved guardrail data (clarifications and strategy) for visibility on all pages.
        
        This ensures that once clarifications are answered or strategy decisions are made,
        they are visible on ALL pages (clarify, build, validate, render), not just their own page.
        """
        if not self.behavior:
```

[X] ERROR (line 624)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _add_behavior_action_metadata(self, instructions):
        """Add behavior and action metadata as separate properties for JSON output."""
        # Add behavior metadata (using keys that TTY adapter expects)
```

[X] ERROR (line 664)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _build_display_content(self, instructions: Instructions):
        """Build display_content for chat submission from all instructions data.
        
        Uses the existing MarkdownInstructions adapter to format the complete instructions
        object as markdown, including behavior/action instructions, base instructions,
        guardrails, clarifications, strategy decisions, and all other data.
        
        IMPORTANT: Creates a temporary copy without display_content to avoid circular
        serialization (display_content shouldn't include itself).
        """
        from agile_bot.src.instructions.markdown_instructions import MarkdownInstructions
```

[X] ERROR (line 689)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _prepare_instructions(self, instructions, context: ActionContext):
        """Template method: Prepare action-specific instructions data.
        
        Override in subclasses to add guardrails, questions, evidence, etc.
        Subclasses should modify the instructions object in place.
        """
        pass
```

[X] ERROR (line 697)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _format_instructions_for_display(self, instructions) -> str:
        """Template method: Format instructions for REPL display.
        
        Override in subclasses to customize display formatting.
        """
        # Use the proper interface to get instruction data
```

[X] ERROR (line 155)
Useless comment: "# Handle generic types (Dict[...], List[...], etc.)" - delete it or improve the code instead

```python
            return "list"
        
        # Handle generic types (Dict[...], List[...], etc.)
        from typing import get_origin
```

[X] ERROR (line 237)
Useless comment: "# Load scope from state file" - delete it or improve the code instead

```python
            base_instructions = self._replace_context_placeholders(base_instructions)
        
        # Load scope from state file
        scope = self._load_scope_from_state()
```

[X] ERROR (line 429)
Useless comment: "# Return the Instructions object directly" - delete it or improve the code instead

```python
        self._build_display_content(instructions)
        
        # Return the Instructions object directly
        # CLI will use adapters to serialize it appropriately
```

[X] ERROR (line 451)
Useless comment: "# Get required context for this behavior" - delete it or improve the code instead

```python
                from .clarify.required_context import RequiredContext
                
                # Get required context for this behavior
                required_context = None
```

[X] ERROR (line 481)
Useless comment: "# Get strategy from behavior folder" - delete it or improve the code instead

```python
                from pathlib import Path
                
                # Get strategy from behavior folder
                strategy_obj = None
```

[X] ERROR (line 511)
Useless comment: "# Get required_context from behavior's guardrails" - delete it or improve the code instead

```python
                return
            
            # Get required_context from behavior's guardrails
            guardrails_obj = self.behavior.guardrails
```

[X] ERROR (line 566)
Useless comment: "# Load strategy data (criteria templates + saved decisions)" - delete it or improve the code instead

```python
        
        try:
            # Load strategy data (criteria templates + saved decisions)
            from .strategy.strategy_decision import StrategyDecision
```

[X] ERROR (line 570)
Useless comment: "# Load strategy criteria templates" - delete it or improve the code instead

```python
            from .strategy.strategy import Strategy
            
            # Load strategy criteria templates
            strategy = Strategy(self.behavior.folder)
```

[X] ERROR (line 574)
Useless comment: "# Load saved strategy decisions" - delete it or improve the code instead

```python
            strategy_data = strategy.instructions
            
            # Load saved strategy decisions
            saved_strategy = StrategyDecision.load_all(self.behavior.bot_paths)
```

[X] ERROR (line 583)
Useless comment: "# Get criteria template" - delete it or improve the code instead

```python
            
            if strategy_data:
                # Get criteria template
                criteria_template = strategy_data.get('strategy_criteria', {})
```

[X] ERROR (line 675)
Useless comment: "# Create a temporary copy without display_content to avoid c" - delete it or improve the code instead

```python
        from agile_bot.src.instructions.markdown_instructions import MarkdownInstructions

        # Create a temporary copy without display_content to avoid circular serialization
        # (display_content shouldn't include itself when serialized)
```

---

## stop_writing_useless_comments
**actions.py** - 1 violation(s)

[X] ERROR (line 262)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def is_action_completed(self, action_name: str) -> bool:
        """
        Check if an action is completed.
        
        Previous behavior marked all earlier actions as completed when the current
        index moved forward. That caused the panel to show checkmarks on every prior
        action, which we no longer want. Until we have explicit completion state,
        treat actions as not completed unless a real completion flag exists.
        """
        return False
```

---

## stop_writing_useless_comments
**action_context.py** - 3 violation(s)

[X] ERROR (line 45)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __post_init__(self):
        """Normalize strategy context fields and keep backward compatibility."""
        # Default collections to empty to simplify downstream checks
```

[X] ERROR (line 56)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_decisions(self) -> Dict[str, Any]:
        """Get all decision attributes (exclude assumption fields and internals)."""
        excluded = {'assumptions', 'assumptions_made', 'decisions_made'}
```

[X] ERROR (line 67)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def assumptions_list(self) -> Optional[List[str]]:
        """Alias to keep existing code using context.assumptions working."""
        return self.assumptions or self.assumptions_made
```

---

## stop_writing_useless_comments
**json_actions.py** - 5 violation(s)

[X] ERROR (line 10)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class JSONActions(BaseActionsAdapter, JSONAdapter):
    """Serializes Actions collection to JSON - delegates to JSONAction for each action."""
    
```

[X] ERROR (line 13)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, actions):
        """
        Initialize JSON adapter for Actions.
        
        Args:
            actions: Actions collection to serialize
        """
        BaseActionsAdapter.__init__(self, actions, 'json')
```

[X] ERROR (line 23)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Actions to JSON string - overrides base to use to_dict."""
        return json.dumps(self.to_dict(), indent=2)
```

[X] ERROR (line 27)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_dict(self) -> dict:
        """Convert Actions to dict."""
        actions_list = []
```

[X] ERROR (line 51)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def deserialize(self, data: str) -> dict:
        """Parse JSON string to dict."""
        return json.loads(data)
```

---

## stop_writing_useless_comments
**markdown_action.py** - 3 violation(s)

[X] ERROR (line 8)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class MarkdownAction(MarkdownAdapter):
    """Base Markdown adapter for Action - provides common serialization for status display."""
    
```

[X] ERROR (line 17)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def action_name(self):
        """Returns formatted action name with marker."""
        is_completed = getattr(self.action, 'is_completed', False)
```

[X] ERROR (line 38)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Action to Markdown string - returns formatted properties."""
        return self.action_name
```

---

## stop_writing_useless_comments
**markdown_actions.py** - 4 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class MarkdownActions(BaseActionsAdapter, MarkdownAdapter):
    """Serializes Actions collection to Markdown - delegates to MarkdownAction for each action."""
    
```

[X] ERROR (line 12)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, actions):
        """
        Initialize Markdown adapter for Actions.
        
        Args:
            actions: Actions collection to serialize
        """
        BaseActionsAdapter.__init__(self, actions, 'markdown')
```

[X] ERROR (line 22)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Actions to Markdown string - uses base class serialization."""
        return super().serialize()
```

[X] ERROR (line 26)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text into verb and args."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**tty_action.py** - 7 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYAction(TTYAdapter):
    """Serializes Action to TTY - exposes all Action properties."""
    
```

[X] ERROR (line 12)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, action, is_current: bool = False, is_completed: bool = False):
        """
        Initialize TTY adapter for Action.
        
        Args:
            action: Action to serialize
            is_current: Whether this is the current action
            is_completed: Whether this action is completed
        """
        self.action = action
```

[X] ERROR (line 27)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def action_name(self):
        """Returns formatted action name with icon and description."""
        if self.is_current:
```

[X] ERROR (line 49)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def name(self):
        """Returns action name."""
        return self.action.action_name
```

[X] ERROR (line 54)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def domain_action(self):
        """Returns underlying domain action (raw)."""
        return self.action
```

[X] ERROR (line 58)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Action to TTY string - returns formatted properties."""
        return self.action_name
```

[X] ERROR (line 62)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text into verb and args."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**tty_actions.py** - 7 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYActions(BaseActionsAdapter, TTYAdapter):
    """Serializes Actions collection to TTY - delegates to TTYAction for each action."""
    
```

[X] ERROR (line 12)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, actions):
        """
        Initialize TTY adapter for Actions.
        
        Args:
            actions: Actions collection to serialize
        """
        BaseActionsAdapter.__init__(self, actions, 'tty')
```

[X] ERROR (line 24)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def current(self):
        """Returns formatted current action display."""
        if self.actions.current:
```

[X] ERROR (line 33)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def names(self):
        """Return pipe-separated list of action names with current action bolded.
        
        Includes workflow actions first, then non-workflow actions (like 'rules') at the end.
        """
        current_action_name = self.actions.current.action_name if self.actions.current else None
```

[X] ERROR (line 58)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def all_actions(self):
        """Returns formatted list of all actions."""
        return self.serialize()
```

[X] ERROR (line 62)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Actions to TTY string - uses base class serialization."""
        return super().serialize()
```

[X] ERROR (line 67)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text into verb and args."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**behavior.py** - 4 violation(s)

[X] ERROR (line 67)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def is_completed(self) -> bool:
        """Check if this behavior is completed.
        
        Note: Completion should be explicitly tracked, not inferred from position.
        Returning False until we implement explicit completion tracking.
        """
        return False
```

[X] ERROR (line 127)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def validation_type(self) -> ValidationType:
        """Determine what this behavior validates by default.
        
        Returns:
            ValidationType.STORY_GRAPH: For behaviors that validate story graph only (shape, discovery, exploration, etc.)
            ValidationType.FILES: For behaviors that validate files only (code, tests)
            ValidationType.BOTH: For behaviors that validate both (default fallback)
        """
        # Behaviors that validate story graph only
```

[X] ERROR (line 147)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def submitRules(self) -> Dict[str, Any]:
        """Submit behavior rules instructions to AI chat.
        
        Executes the rules action to get instructions, then submits them to chat.
        
        Returns:
            Status dict with success message and submission details
        """
        if not self.bot:
```

[X] ERROR (line 169)
Useless comment: "# Execute the rules action to get instructions" - delete it or improve the code instead

```python
                }
            
            # Execute the rules action to get instructions
            from ..actions.action_context import ActionContext
```

---

## stop_writing_useless_comments
**behaviors.py** - 5 violation(s)

[X] ERROR (line 85)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def completed_behaviors(self) -> List[str]:
        """Get list of completed behavior names."""
        completed = []
```

[X] ERROR (line 123)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def next(self) -> Optional['Behavior']:
        """Get the next behavior without changing current state."""
        next_index = self._current_index + 1
```

[X] ERROR (line 130)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def previous(self) -> Optional['Behavior']:
        """Get the previous behavior without changing current state."""
        if self._current_index is None or self._current_index <= 0:
```

[X] ERROR (line 139)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def advance(self) -> Dict[str, Any]:
        """Advance to the next action in the current behavior, or next behavior if at end.
        
        Returns:
            Dict with status and information about the advancement
        """
        if not self.current:
```

[X] ERROR (line 186)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def go_back(self) -> Dict[str, Any]:
        """Go back to the previous action in the current behavior, or previous behavior if at start.
        
        Returns:
            Dict with status and information about going back
        """
        if not self.current:
```

---

## stop_writing_useless_comments
**json_behavior.py** - 10 violation(s)

[X] ERROR (line 12)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class JSONBehaviors(BaseBehaviorsAdapter, JSONAdapter):
    """Serializes Behaviors collection to JSON."""
    
```

[X] ERROR (line 15)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, behaviors: Behaviors):
        """
        Initialize JSON adapter for Behaviors.
        
        Args:
            behaviors: Behaviors collection to serialize
        """
        BaseBehaviorsAdapter.__init__(self, behaviors, 'json')
```

[X] ERROR (line 25)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Behaviors to JSON string - overrides base to use to_dict."""
        return json.dumps(self.to_dict(), indent=2)
```

[X] ERROR (line 29)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_dict(self) -> dict:
        """Convert Behaviors to dict."""
        behaviors_list = []
```

[X] ERROR (line 42)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class JSONBehavior(BaseBehaviorAdapter, JSONAdapter):
    """Serializes Behavior domain object to JSON."""
    
```

[X] ERROR (line 45)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, behavior: Behavior, is_current: bool = False):
        """
        Initialize JSON adapter for Behavior.
        
        Args:
            behavior: Behavior domain object to serialize
            is_current: Whether this is the current behavior
        """
        self.behavior = behavior
```

[X] ERROR (line 57)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def format_behavior_name(self) -> str:
        """JSON doesn't use this - use to_dict instead."""
        return ""
```

[X] ERROR (line 61)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Behavior to JSON string - overrides base to use to_dict."""
        return json.dumps(self.to_dict(), indent=2)
```

[X] ERROR (line 65)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_dict(self) -> dict:
        """Convert Behavior to dict."""
        result = {
```

[X] ERROR (line 98)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def deserialize(self, data: str) -> Behavior:
        """Reconstruct Behavior from JSON string.
        
        Note: Behavior objects typically require bot_paths and are loaded from config.
        This method is provided for completeness but may not be fully functional.
        """
        behavior_data = json.loads(data)
```

---

## stop_writing_useless_comments
**markdown_behavior.py** - 9 violation(s)

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class MarkdownBehaviors(BaseBehaviorsAdapter, MarkdownAdapter):
    """Serializes Behaviors collection to Markdown."""
    
```

[X] ERROR (line 14)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, behaviors: Behaviors):
        """
        Initialize Markdown adapter for Behaviors.
        
        Args:
            behaviors: Behaviors collection to serialize
        """
        BaseBehaviorsAdapter.__init__(self, behaviors, 'markdown')
```

[X] ERROR (line 24)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Behaviors to Markdown string - uses base class serialization."""
        return super().serialize()
```

[X] ERROR (line 29)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

[X] ERROR (line 36)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class MarkdownBehavior(BaseBehaviorAdapter, MarkdownAdapter):
    """Serializes Behavior domain object to Markdown."""
    
```

[X] ERROR (line 39)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, behavior: Behavior, is_current: bool = False):
        """
        Initialize Markdown adapter for Behavior.
        
        Args:
            behavior: Behavior domain object to serialize
            is_current: Whether this is the current behavior
        """
        self.behavior = behavior
```

[X] ERROR (line 51)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def format_behavior_name(self) -> str:
        """Returns formatted behavior name."""
        marker = "→ " if self.is_current else "  "
```

[X] ERROR (line 56)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Behavior to Markdown string - uses base class serialization."""
        return super().serialize()
```

[X] ERROR (line 61)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**tty_behavior.py** - 12 violation(s)

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYBehaviors(BaseBehaviorsAdapter, TTYAdapter):
    """Serializes Behaviors collection to TTY with hierarchy."""
    
```

[X] ERROR (line 14)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, behaviors: Behaviors):
        """
        Initialize TTY adapter for Behaviors.
        
        Args:
            behaviors: Behaviors collection to serialize
        """
        BaseBehaviorsAdapter.__init__(self, behaviors, 'tty')
```

[X] ERROR (line 26)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def current(self):
        """Returns formatted current behavior display."""
        if self.behaviors.current:
```

[X] ERROR (line 34)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def names(self):
        """Returns pipe-separated list of behavior names with current behavior bolded."""
        current_behavior_name = self.behaviors.current.name if self.behaviors.current else None
```

[X] ERROR (line 48)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def all_behaviors(self):
        """Returns formatted list of all behaviors."""
        return self.serialize()
```

[X] ERROR (line 52)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Behaviors to TTY string - uses base class serialization."""
        return super().serialize()
```

[X] ERROR (line 57)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text into verb and args."""
        parts = text.split(maxsplit=1)
```

[X] ERROR (line 64)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYBehavior(BaseBehaviorAdapter, TTYAdapter):
    """Serializes single Behavior to TTY - delegates to TTYActions."""
    
```

[X] ERROR (line 67)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, behavior: Behavior, is_current: bool = False):
        """
        Initialize TTY adapter for Behavior.
        
        Args:
            behavior: Behavior to serialize
            is_current: Whether this is the current behavior
        """
        self.behavior = behavior
```

[X] ERROR (line 79)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def format_behavior_name(self) -> str:
        """Returns formatted behavior name with icon."""
        if self.is_current:
```

[X] ERROR (line 89)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Behavior to TTY string - uses base class serialization."""
        return super().serialize()
```

[X] ERROR (line 94)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text into verb and args."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**behavior.py** - 2 violation(s)

[X] ERROR (line 64)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def is_completed(self) -> bool:
        """Check if this behavior is completed.
        
        Note: Completion should be explicitly tracked, not inferred from position.
        Returning False until we implement explicit completion tracking.
        """
        return False
```

[X] ERROR (line 124)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def validation_type(self) -> ValidationType:
        """Determine what this behavior validates by default.
        
        Returns:
            ValidationType.STORY_GRAPH: For behaviors that validate story graph only (shape, discovery, exploration, etc.)
            ValidationType.FILES: For behaviors that validate files only (code, tests)
            ValidationType.BOTH: For behaviors that validate both (default fallback)
        """
        # Behaviors that validate story graph only
```

---

## stop_writing_useless_comments
**behaviors.py** - 5 violation(s)

[X] ERROR (line 85)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def completed_behaviors(self) -> List[str]:
        """Get list of completed behavior names."""
        completed = []
```

[X] ERROR (line 123)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def next(self) -> Optional['Behavior']:
        """Get the next behavior without changing current state."""
        next_index = self._current_index + 1
```

[X] ERROR (line 130)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def previous(self) -> Optional['Behavior']:
        """Get the previous behavior without changing current state."""
        if self._current_index is None or self._current_index <= 0:
```

[X] ERROR (line 139)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def advance(self) -> Dict[str, Any]:
        """Advance to the next action in the current behavior, or next behavior if at end.
        
        Returns:
            Dict with status and information about the advancement
        """
        if not self.current:
```

[X] ERROR (line 186)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def go_back(self) -> Dict[str, Any]:
        """Go back to the previous action in the current behavior, or previous behavior if at start.
        
        Returns:
            Dict with status and information about going back
        """
        if not self.current:
```

---

## stop_writing_useless_comments
**bot.py** - 44 violation(s)

[X] ERROR (line 105)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def bot_directory(self) -> Path:
        """Return the bot directory path."""
        return self.bot_paths.bot_directory
```

[X] ERROR (line 110)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def workspace_directory(self) -> Path:
        """Return the workspace directory path."""
        return self.bot_paths.workspace_directory
```

[X] ERROR (line 115)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def progress_path(self) -> str:
        """Return current progress path (e.g., 'discovery.validate')."""
        if self.behaviors.current:
```

[X] ERROR (line 126)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def stage_name(self) -> str:
        """Return current stage name (Idle/Ready/In Progress)."""
        if not self.behaviors.current:
```

[X] ERROR (line 136)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def commands(self) -> 'Help':
        """Return available commands as Help object."""
        return self.help()
```

[X] ERROR (line 141)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def current_behavior_name(self) -> str:
        """Return current behavior name."""
        return self.behaviors.current.name if self.behaviors.current else None
```

[X] ERROR (line 146)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def current_action_name(self) -> str:
        """Return current action name."""
        if self.behaviors.current and self.behaviors.current.actions.current_action_name:
```

[X] ERROR (line 153)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def bots(self) -> List[str]:
        """Return list of all registered bot names.
        
        Discovers bots by scanning the parent bots directory for subdirectories
        containing bot_config.json files.
        
        Returns:
            List of bot names (directory names) that have valid bot_config.json
        """
        registered_bots = []
```

[X] ERROR (line 178)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def active_bot(self) -> 'Bot':
        """Return the currently active bot instance.
        
        Returns:
            The active Bot instance from the class-level registry
        """
        return Bot._active_bot_instance if Bot._active_bot_instance else self
```

[X] ERROR (line 187)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @active_bot.setter
    def active_bot(self, bot_name: str):
        """Switch to a different registered bot.
        
        Creates a new Bot instance for the specified bot and updates the
        class-level registry so all subsequent calls return the new instance.
        
        Args:
            bot_name: Name of the bot to switch to
        
        Raises:
            ValueError: If bot_name is not registered or invalid
        """
        # Validate bot exists
```

[X] ERROR (line 226)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def help(self, topic: Optional[str] = None):
        """Display help information about the bot, behaviors, or actions.
        
        Args:
            topic: Optional topic for specific help (behavior name, action name, etc.)
        
        Returns:
            Help domain object with hierarchical help structure
        """
        from agile_bot.src.help.help import Help
```

[X] ERROR (line 240)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def exit(self) -> Dict[str, Any]:
        """Exit the bot session gracefully.
        
        Returns:
            Dict with exit status and message
        """
        return {
```

[X] ERROR (line 252)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def current(self) -> Dict[str, Any]:
        """Get current action instructions.
        
        Returns:
            Dict with current action instructions
        """
        if not self.behaviors.current:
```

[X] ERROR (line 287)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def scope(self, scope_filter: Optional[str] = None):
        """Set or view the scope filter for the current workflow.
        
        AI AGENTS: This command requires COMPLETE folder paths. When you pass a directory path,
        you MUST include the ENTIRE folder structure from root or working area.
        
        Args:
            scope_filter: Complete folder path or story name to filter by, or None to view current scope
        
        Returns:
            Dict with status, message, and scope data when setting scope, or Scope object when viewing
        """
        from ..scope.scope import ScopeType
```

[X] ERROR (line 449)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def workspace(self, directory: Optional[str] = None) -> Dict[str, Any]:
        """Alias for path command - set or view the working directory.
        
        Args:
            directory: Path to set as working directory, or None to view current path
        
        Returns:
            Dict with path information or updated path status
        """
        return self.path(directory)
```

[X] ERROR (line 460)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def path(self, directory: Optional[str] = None) -> Dict[str, Any]:
        """Set or view the working directory.
        
        Args:
            directory: Path to set as working directory, or None to view current path
        
        Returns:
            Dict with path information or updated path status
        """
        if directory is None:
```

[X] ERROR (line 502)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def next(self) -> Dict[str, Any]:
        """Navigate to the next action in the current behavior workflow.
        
        Returns:
            Dict with navigation result (new position, message)
        """
        if not self.behaviors.current:
```

[X] ERROR (line 559)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def back(self) -> Dict[str, Any]:
        """Navigate to the previous action in the current behavior workflow.
        
        Returns:
            Dict with navigation result (new position, message)
        """
        if not self.behaviors.current:
```

[X] ERROR (line 607)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def execute(self, behavior_name: str, action_name: Optional[str] = None, params: Optional[Dict[str, Any]] = None) -> Any:
        """Execute a specific behavior.action and return instructions.
        
        Navigates to behavior/action and calls get_instructions() with optional parameters.
        
        Args:
            behavior_name: Name of the behavior to execute
            action_name: Name of the action to execute (optional, uses current action if None)
            params: Optional parameters to pass to action context (guardrails, answers, decisions, etc.)
        
        Returns:
            Instructions object from action.get_instructions()
        """
        # Find behavior
```

[X] ERROR (line 768)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def submit_behavior_rules(self, behavior_name: str) -> Dict[str, Any]:
        """Get rules for a behavior and submit them to AI chat.
        
        This is a convenience method that:
        1. Saves current position
        2. Navigates to behavior
        3. Submits rules using behavior.submitRules()
        4. Restores previous position
        
        Args:
            behavior_name: Name of the behavior to get rules for
            
        Returns:
            Status dict with success message and submission details
        """
        # Save current position
```

[X] ERROR (line 818)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def submit_instructions(self, instructions, behavior_name: str = None, action_name: str = None) -> Dict[str, Any]:
        """Submit given Instructions object to AI chat.
        
        Args:
            instructions: Instructions object with display_content to submit
            behavior_name: Optional behavior name (for reporting, will be inferred if not provided)
            action_name: Optional action name (for reporting, will be inferred if not provided)
            
        Returns:
            Status dict with success message, behavior/action info, and submission details
        """
        display_content = instructions.display_content
```

[X] ERROR (line 891)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def submit_current_action(self) -> Dict[str, Any]:
        """Submit current action instructions to AI agent.
        
        Gets the current action's instructions (including display_content with all 
        behavior instructions, action instructions, base instructions, and guardrails),
        copies them to clipboard, and opens Cursor chat.
        
        Returns:
            Status dict with success message, current context, and instructions content
        """
        current_behavior = self.behaviors.current
```

[X] ERROR (line 937)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def tree(self) -> str:
        """Display behavior hierarchy tree.
        
        Returns:
            String representation of all behaviors and their actions
        """
        lines = []
```

[X] ERROR (line 967)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def pos(self) -> Dict[str, Any]:
        """Get current position (behavior.action).
        
        Returns:
            Dict with current behavior and action
        """
        if not self.behaviors.current:
```

[X] ERROR (line 55)
Useless comment: "# Get allowed behaviors from bot_config.json" - delete it or improve the code instead

```python
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'bot.py:33','message':'Before Behaviors creation','data':{},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1'})+'\n'); log_file.close()
        # #endregion
        # Get allowed behaviors from bot_config.json
        allowed_behaviors = self._config.get('behaviors')
```

[X] ERROR (line 67)
Useless comment: "# Create Scope instance with workspace context and load from" - delete it or improve the code instead

```python
            behavior.bot_name = self.bot_name
        
        # Create Scope instance with workspace context and load from state
        self._scope = Scope(self.bot_paths.workspace_directory, self.bot_paths)
```

[X] ERROR (line 163)
Useless comment: "# Get the parent bots directory (bot_directory.parent)" - delete it or improve the code instead

```python
        registered_bots = []
        
        # Get the parent bots directory (bot_directory.parent)
        bots_parent_dir = self.bot_paths.bot_directory.parent
```

[X] ERROR (line 210)
Useless comment: "# Create new Bot instance for the target bot" - delete it or improve the code instead

```python
            return
        
        # Create new Bot instance for the target bot
        bots_parent_dir = self.bot_paths.bot_directory.parent
```

[X] ERROR (line 218)
Useless comment: "# Create new Bot instance (this will auto-register via __ini" - delete it or improve the code instead

```python
            raise FileNotFoundError(f"Bot config not found at {new_config_path}")
        
        # Create new Bot instance (this will auto-register via __init__)
        Bot(
```

[X] ERROR (line 236)
Useless comment: "# Return new Help object that delegates to bot's behaviors/a" - delete it or improve the code instead

```python
        from agile_bot.src.help.help import Help
        
        # Return new Help object that delegates to bot's behaviors/actions
        return Help(bot=self)
```

[X] ERROR (line 273)
Useless comment: "# Get instructions using get_instructions() method with defa" - delete it or improve the code instead

```python
        
        try:
            # Get instructions using get_instructions() method with default context
            from ..actions.action_context import ActionContext
```

[X] ERROR (line 278)
Useless comment: "# Return Instructions object directly for adapter serializat" - delete it or improve the code instead

```python
            instructions = action.get_instructions(context)
            
            # Return Instructions object directly for adapter serialization
            return instructions
```

[X] ERROR (line 302)
Useless comment: "# Return current scope instance for property access" - delete it or improve the code instead

```python
        
        if scope_filter is None:
            # Return current scope instance for property access
            return self._scope
```

[X] ERROR (line 356)
Useless comment: "# Handle multiple formats:" - delete it or improve the code instead

```python
        
        # Parse scope filter
        # Handle multiple formats:
        # 1. "story=TestStory" or "story:TestStory" (delimited)
```

[X] ERROR (line 436)
Useless comment: "# Update scope filter" - delete it or improve the code instead

```python
                prefix = 'story'
        
        # Update scope filter
        self._scope.filter(scope_type, scope_values)
```

[X] ERROR (line 440)
Useless comment: "# Return a ScopeCommandResult object that will be serialized" - delete it or improve the code instead

```python
        self._scope.save()
        
        # Return a ScopeCommandResult object that will be serialized properly
        from ..scope.scope_command_result import ScopeCommandResult
```

[X] ERROR (line 469)
Useless comment: "# Return current working directory" - delete it or improve the code instead

```python
        """
        if directory is None:
            # Return current working directory
            current_path = self.bot_paths.workspace_directory
```

[X] ERROR (line 477)
Useless comment: "# Set new working directory" - delete it or improve the code instead

```python
            }
        
        # Set new working directory
        new_path = Path(directory)
```

[X] ERROR (line 488)
Useless comment: "# Update the bot paths (with persistence)" - delete it or improve the code instead

```python
            }
        
        # Update the bot paths (with persistence)
        self.bot_paths.update_workspace_directory(new_path, persist=True)
```

[X] ERROR (line 653)
Useless comment: "# Get current action" - delete it or improve the code instead

```python
                    }
        
        # Get current action
        action = behavior.actions.current
```

[X] ERROR (line 665)
Useless comment: "# Get instructions using get_instructions() method with cont" - delete it or improve the code instead

```python
        
        try:
            # Get instructions using get_instructions() method with context
            from ..actions.action_context import ActionContext
```

[X] ERROR (line 679)
Useless comment: "# Return Instructions object directly for adapter serializat" - delete it or improve the code instead

```python
            instructions = action.get_instructions(context)
            
            # Return Instructions object directly for adapter serialization
            return instructions
```

[X] ERROR (line 915)
Useless comment: "# Get the current action object" - delete it or improve the code instead

```python
        
        try:
            # Get the current action object
            action = current_behavior.actions.find_by_name(current_action_name)
```

[X] ERROR (line 923)
Useless comment: "# Get instructions with display_content built" - delete it or improve the code instead

```python
                }
            
            # Get instructions with display_content built
            instructions = action.get_instructions()
```

---

## stop_writing_useless_comments
**json_bot.py** - 8 violation(s)

[X] ERROR (line 12)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class JSONBot(BaseBotAdapter, JSONAdapter):
    """Serializes Bot domain object to JSON - exposes all Bot properties."""
    
```

[X] ERROR (line 15)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, bot: Bot):
        """
        Initialize JSON adapter for Bot.
        
        Args:
            bot: Bot domain object to serialize
        """
        BaseBotAdapter.__init__(self, bot, 'json')
```

[X] ERROR (line 50)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def format_header(self) -> str:
        """JSON doesn't need header."""
        return ""
```

[X] ERROR (line 54)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def format_bot_info(self) -> str:
        """JSON doesn't use this - use to_dict instead."""
        return ""
```

[X] ERROR (line 58)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def format_footer(self) -> str:
        """JSON doesn't need footer."""
        return ""
```

[X] ERROR (line 62)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Bot to JSON string - overrides base to use to_dict."""
        return json.dumps(self.to_dict(), indent=2)
```

[X] ERROR (line 66)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_dict(self) -> dict:
        """Convert Bot to dict - ensures current_behavior is always included."""
        result = {
```

[X] ERROR (line 90)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def deserialize(self, data: str) -> dict:
        """Parse JSON string to dict."""
        return json.loads(data)
```

---

## stop_writing_useless_comments
**markdown_bot.py** - 14 violation(s)

[X] ERROR (line 10)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class MarkdownBot(BaseBotAdapter, MarkdownAdapter):
    """Serializes Bot domain object to Markdown - matches TTYBot structure."""
    
```

[X] ERROR (line 13)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, bot: Bot):
        """
        Initialize Markdown adapter for Bot.
        
        Args:
            bot: Bot domain object to serialize
        """
        BaseBotAdapter.__init__(self, bot, 'markdown')
```

[X] ERROR (line 25)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def name(self):
        """Returns formatted bot name header with registered bots."""
        lines = []
```

[X] ERROR (line 39)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def bot_paths(self):
        """Returns formatted bot paths display."""
        from agile_bot.src.cli.adapter_factory import AdapterFactory
```

[X] ERROR (line 46)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def progress(self):
        """Returns formatted progress section with behaviors hierarchy."""
        lines = []
```

[X] ERROR (line 61)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def commands(self):
        """Returns available commands quick reference."""
        lines = []
```

[X] ERROR (line 76)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def behavior_action_summary(self):
        """Returns summary of all behaviors and actions."""
        lines = []
```

[X] ERROR (line 107)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def format_header(self) -> str:
        """Returns CLI STATUS section header with AI instructions in markdown."""
        lines = []
```

[X] ERROR (line 124)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def format_bot_info(self) -> str:
        """Returns bot name and paths."""
        lines = []
```

[X] ERROR (line 149)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def format_footer(self) -> str:
        """Returns behavior/action summary."""
        return self.behavior_action_summary
```

[X] ERROR (line 153)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Bot to Markdown string - uses base class serialization."""
        result = super().serialize()
```

[X] ERROR (line 159)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

[X] ERROR (line 79)
Useless comment: "# Get behavior names" - delete it or improve the code instead

```python
        lines = []
        
        # Get behavior names
        behavior_names = []
```

[X] ERROR (line 90)
Useless comment: "# Get actions from current behavior" - delete it or improve the code instead

```python
        lines.append(f"**Behaviors:** {' | '.join(behavior_names)}")
        
        # Get actions from current behavior
        behavior = self.bot.behaviors.current or next(iter(self.bot.behaviors), None)
```

---

## stop_writing_useless_comments
**tty_bot (1).py** - 19 violation(s)

[X] ERROR (line 10)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYBot(BaseBotAdapter, TTYAdapter):
    """Serializes Bot domain object to TTY - exposes all Bot properties."""
    
```

[X] ERROR (line 13)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, bot: Bot):
        """
        Initialize TTY adapter for Bot.
        
        Args:
            bot: Bot domain object to serialize
        """
        BaseBotAdapter.__init__(self, bot, 'tty')
```

[X] ERROR (line 25)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def name(self):
        """Returns formatted bot name header."""
        return f"{self.add_bold('🤖 Bot:')} {self.bot.name}"
```

[X] ERROR (line 30)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def bot_name(self):
        """Returns raw bot name."""
        return self.bot.bot_name
```

[X] ERROR (line 35)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def bot_directory(self):
        """Returns formatted bot directory path."""
        return f"{self.add_bold('Bot Path:')}\n{str(self.bot.bot_paths.bot_directory)}"
```

[X] ERROR (line 40)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def workspace_directory(self):
        """Returns formatted workspace directory path."""
        return f"{self.add_bold('Workspace Path:')}\n{str(self.bot.bot_paths.workspace_directory)}"
```

[X] ERROR (line 45)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def bot_paths(self):
        """Returns formatted bot paths display."""
        from agile_bot.src.cli.adapter_factory import AdapterFactory
```

[X] ERROR (line 52)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def progress(self):
        """Returns formatted progress section with behaviors hierarchy."""
        lines = []
```

[X] ERROR (line 66)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def behaviors(self):
        """Returns formatted behaviors display."""
        from agile_bot.src.cli.adapter_factory import AdapterFactory
```

[X] ERROR (line 73)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def header(self):
        """Returns CLI STATUS section header with AI instructions."""
        lines = []
```

[X] ERROR (line 91)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def run_instructions(self):
        """Returns run instructions for executing behaviors/actions."""
        lines = []
```

[X] ERROR (line 106)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def commands(self):
        """Returns available commands quick reference."""
        lines = []
```

[X] ERROR (line 120)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def behavior_action_summary(self):
        """Returns summary of all behaviors and actions."""
        from agile_bot.src.cli.adapter_factory import AdapterFactory
```

[X] ERROR (line 136)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def format_header(self) -> str:
        """Returns CLI STATUS section header with AI instructions."""
        return self.header
```

[X] ERROR (line 140)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def format_bot_info(self) -> str:
        """Returns bot name and paths."""
        lines = []
```

[X] ERROR (line 159)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def format_footer(self) -> str:
        """Returns behavior/action summary."""
        return self.behavior_action_summary
```

[X] ERROR (line 163)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Bot to TTY string - uses base class serialization."""
        return super().serialize()
```

[X] ERROR (line 168)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

[X] ERROR (line 127)
Useless comment: "# Get actions from current behavior or first behavior" - delete it or improve the code instead

```python
        lines.append(f"{self.add_bold('Behaviors:')} {tty_behaviors.names}")
        
        # Get actions from current behavior or first behavior
        behavior = self.bot.behaviors.current or next(iter(self.bot.behaviors), None)
```

---

## stop_writing_useless_comments
**tty_bot.py** - 19 violation(s)

[X] ERROR (line 10)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYBot(BaseBotAdapter, TTYAdapter):
    """Serializes Bot domain object to TTY - exposes all Bot properties."""
    
```

[X] ERROR (line 13)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, bot: Bot):
        """
        Initialize TTY adapter for Bot.
        
        Args:
            bot: Bot domain object to serialize
        """
        BaseBotAdapter.__init__(self, bot, 'tty')
```

[X] ERROR (line 25)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def name(self):
        """Returns formatted bot name header with registered bots."""
        lines = []
```

[X] ERROR (line 39)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def bot_name(self):
        """Returns raw bot name."""
        return self.bot.bot_name
```

[X] ERROR (line 44)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def bot_directory(self):
        """Returns formatted bot directory path."""
        return f"{self.add_bold('Bot Path:')}\n{str(self.bot.bot_paths.bot_directory)}"
```

[X] ERROR (line 49)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def workspace_directory(self):
        """Returns formatted workspace directory path."""
        return f"{self.add_bold('Workspace Path:')}\n{str(self.bot.bot_paths.workspace_directory)}"
```

[X] ERROR (line 54)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def bot_paths(self):
        """Returns formatted bot paths display."""
        from agile_bot.src.cli.adapter_factory import AdapterFactory
```

[X] ERROR (line 61)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def progress(self):
        """Returns formatted progress section with behaviors hierarchy."""
        lines = []
```

[X] ERROR (line 75)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def behaviors(self):
        """Returns formatted behaviors display."""
        from agile_bot.src.cli.adapter_factory import AdapterFactory
```

[X] ERROR (line 82)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def header(self):
        """Returns CLI STATUS section header with AI instructions."""
        lines = []
```

[X] ERROR (line 100)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def run_instructions(self):
        """Returns run instructions for executing behaviors/actions."""
        lines = []
```

[X] ERROR (line 115)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def commands(self):
        """Returns available commands quick reference."""
        lines = []
```

[X] ERROR (line 129)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def behavior_action_summary(self):
        """Returns summary of all behaviors and actions."""
        from agile_bot.src.cli.adapter_factory import AdapterFactory
```

[X] ERROR (line 145)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def format_header(self) -> str:
        """Returns CLI STATUS section header with AI instructions."""
        return self.header
```

[X] ERROR (line 149)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def format_bot_info(self) -> str:
        """Returns bot name and paths."""
        lines = []
```

[X] ERROR (line 168)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def format_footer(self) -> str:
        """Returns behavior/action summary."""
        return self.behavior_action_summary
```

[X] ERROR (line 172)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Bot to TTY string - uses base class serialization."""
        return super().serialize()
```

[X] ERROR (line 177)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

[X] ERROR (line 136)
Useless comment: "# Get actions from current behavior or first behavior" - delete it or improve the code instead

```python
        lines.append(f"{self.add_bold('Behaviors:')} {tty_behaviors.names}")
        
        # Get actions from current behavior or first behavior
        behavior = self.bot.behaviors.current or next(iter(self.bot.behaviors), None)
```

---

## stop_writing_useless_comments
**workspace.py** - 2 violation(s)

[X] ERROR (line 6)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

def get_python_workspace_root() -> Path:
    """
    Get the root of the Python workspace (repository root).
    workspace.py is at: agile_bot/src/bot/workspace.py
    Go up: bot -> src -> agile_bot -> workspace_root
    """
    return Path(__file__).parent.parent.parent.parent
```

[X] ERROR (line 26)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

def get_base_actions_directory(bot_directory: Path=None) -> Path:
    """
    Get base actions directory.
    
    Args:
        bot_directory: Optional bot directory path. If None, uses BOT_DIRECTORY env var.
    
    Returns:
        Path to base_actions directory (from bot_config.json or default to agile_bot/base_actions)
    """
    from ..utils import read_json_file
```

---

## stop_writing_useless_comments
**bot_path.py** - 2 violation(s)

[X] ERROR (line 27)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _load_base_actions_directory(self) -> Path:
        """Load base_actions path from bot_config.json or use default."""
        # Try both config locations
```

[X] ERROR (line 88)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def test_path(self) -> Path:
        """Return the relative path to the test directory."""
        return Path('test')
```

---

## stop_writing_useless_comments
**json_bot_path.py** - 3 violation(s)

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class JSONBotPath(JSONAdapter):
    """Serializes BotPath to JSON - exposes all BotPath properties."""
    
```

[X] ERROR (line 38)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_dict(self) -> dict:
        """Convert BotPath to dict."""
        return {
```

[X] ERROR (line 48)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def deserialize(self, data: str) -> dict:
        """Parse JSON string to dict."""
        return json.loads(data)
```

---

## stop_writing_useless_comments
**markdown_bot_path.py** - 3 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class MarkdownBotPath(MarkdownAdapter):
    """Serializes BotPath to Markdown."""
    
```

[X] ERROR (line 15)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert BotPath to Markdown string."""
        lines = []
```

[X] ERROR (line 35)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**tty_bot_path.py** - 3 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYBotPath(TTYAdapter):
    """Serializes BotPath to TTY - exposes all BotPath properties."""
    
```

[X] ERROR (line 36)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert BotPath to TTY string."""
        lines = []
```

[X] ERROR (line 58)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**action_data_collector.py** - 10 violation(s)

[X] ERROR (line 10)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class ActionDataCollector:
    """Collects action and behavior data for rendering."""
    
```

[X] ERROR (line 20)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_behavior_order(self, behavior) -> int:
        """Get order for behavior from config."""
        return behavior.order
```

[X] ERROR (line 24)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def sort_behaviors_for_display(self, behaviors):
        """Sort behaviors by order."""
        behaviors_list = list(behaviors)
```

[X] ERROR (line 34)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_behavior_actions(self, behavior) -> List[str]:
        """Get action names for a behavior."""
        return behavior.action_names
```

[X] ERROR (line 38)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_action_parameters(self, action_name: str) -> List[str]:
        """Get parameter list for an action from its context class."""
        action_class = ActionFactory.get_action_class(action_name)
```

[X] ERROR (line 56)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_parameter_descriptions(self, action_name: str, parameters: List[str]) -> Dict[str, str]:
        """Get descriptions for action parameters."""
        descriptions = {}
```

[X] ERROR (line 64)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _get_single_parameter_description(self, action_name: str, param: str) -> str:
        """Get description for a single parameter."""
        if 'answers' in param or 'key_questions_answered' in param:
```

[X] ERROR (line 78)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _get_scope_description(self, action_name: str) -> str:
        """Get scope description for an action."""
        if action_name == 'validate':
```

[X] ERROR (line 84)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_action_description(self, action_name: str) -> str:
        """Get description for an action."""
        description = self.description_extractor.get_action_description(action_name)
```

[X] ERROR (line 91)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_behavior_description(self, behavior_name: str) -> str:
        """Get description for a behavior."""
        return self.description_extractor.get_behavior_description(f'{self.bot_name}-{behavior_name}')
```

---

## stop_writing_useless_comments
**adapters.py** - 35 violation(s)

[X] ERROR (line 12)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class ChannelAdapter(ABC):
    """Base for all channel adapters."""
    
```

[X] ERROR (line 16)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @abstractmethod
    def serialize(self) -> str:
        """Serialize domain object to string format."""
        pass
```

[X] ERROR (line 20)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TextAdapter(ChannelAdapter):
    """Base for text-based adapters (TTY, Markdown)."""
    
```

[X] ERROR (line 24)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @abstractmethod
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text into verb and params."""
        pass
```

[X] ERROR (line 29)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYAdapter(TextAdapter):
    """Base for terminal output adapters."""
    
```

[X] ERROR (line 32)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def add_color(self, text: str, color: str) -> str:
        """Add ANSI color codes."""
        colors = {
```

[X] ERROR (line 43)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def add_bold(self, text: str) -> str:
        """Add ANSI bold formatting."""
        return f"\033[1m{text}\033[0m"
```

[X] ERROR (line 47)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def format_indentation(self, level: int) -> str:
        """Format indentation for hierarchy."""
        return "  " * level
```

[X] ERROR (line 51)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def section_separator(self) -> str:
        """Return heavy separator for major sections."""
        return "━" * 100
```

[X] ERROR (line 55)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def subsection_separator(self) -> str:
        """Return light separator for subsections."""
        return "─" * 60
```

[X] ERROR (line 60)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @abstractmethod
    def serialize(self) -> str:
        """Convert domain object to TTY string."""
        pass
```

[X] ERROR (line 65)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @abstractmethod
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

[X] ERROR (line 73)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class JSONAdapter(ChannelAdapter):
    """Base for JSON adapters."""
    
```

[X] ERROR (line 77)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @abstractmethod
    def to_dict(self) -> Dict:
        """Convert domain object to dict."""
        pass
```

[X] ERROR (line 81)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert to JSON string."""
        import json
```

[X] ERROR (line 87)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class MarkdownAdapter(TextAdapter):
    """Base for Markdown adapters."""
    
```

[X] ERROR (line 90)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def format_header(self, level: int, text: str) -> str:
        """Format markdown header."""
        return f"{'#' * level} {text}\n"
```

[X] ERROR (line 94)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def format_list_item(self, text: str, indent: int = 0) -> str:
        """Format markdown list item."""
        return f"{'  ' * indent}- {text}\n"
```

[X] ERROR (line 98)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def format_code_block(self, content: str, language: str = "") -> str:
        """Format markdown code block."""
        return f"```{language}\n{content}\n```\n"
```

[X] ERROR (line 103)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @abstractmethod
    def serialize(self) -> str:
        """Convert domain object to Markdown string."""
        pass
```

[X] ERROR (line 108)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @abstractmethod
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

[X] ERROR (line 116)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class JSONProgressAdapter(JSONAdapter):
    """Base for JSON adapters that track progress."""
    
```

[X] ERROR (line 119)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def include_progress_fields(self, is_completed: bool, is_current: bool) -> Dict:
        """Standard progress fields."""
        return {
```

[X] ERROR (line 128)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYProgressAdapter(TTYAdapter):
    """Base for TTY adapters that track progress."""
    
```

[X] ERROR (line 131)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def render_marker(self, is_completed: bool, is_current: bool) -> str:
        """Render progress marker."""
        if is_completed:
```

[X] ERROR (line 141)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class MarkdownProgressAdapter(MarkdownAdapter):
    """Base for Markdown adapters that track progress."""
    
```

[X] ERROR (line 144)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def render_progress_marker(self, is_completed: bool, is_current: bool) -> str:
        """Render markdown progress marker."""
        if is_completed:
```

[X] ERROR (line 154)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class GenericJSONAdapter(JSONAdapter):
    """Generic JSON adapter for dict/list objects without custom domain objects."""
    
```

[X] ERROR (line 160)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_dict(self) -> Dict:
        """Return data as-is if dict, otherwise wrap it."""
        if isinstance(self.data, dict):
```

[X] ERROR (line 167)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class GenericTTYAdapter(TTYAdapter):
    """Generic TTY adapter for dict/list objects without custom domain objects."""
    
```

[X] ERROR (line 173)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Format data for TTY output with ANSI formatting."""
        if isinstance(self.data, dict):
```

[X] ERROR (line 208)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

[X] ERROR (line 216)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class GenericMarkdownAdapter(MarkdownAdapter):
    """Generic Markdown adapter for dict/list objects without custom domain objects."""
    
```

[X] ERROR (line 222)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Format data for Markdown output."""
        # Check if it's a scope response
```

[X] ERROR (line 239)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**adapter_factory.py** - 3 violation(s)

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class AdapterFactory:
    """
    Factory for creating channel adapters for domain objects.
    Uses registry pattern to avoid cyclomatic complexity.
    """
    
```

[X] ERROR (line 114)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @classmethod
    def create(cls, domain_object: Any, channel: str, **kwargs):
        """
        Create appropriate adapter for domain object and channel.
        
        Args:
            domain_object: Domain object to adapt (Status, Scope, etc.)
            channel: Output channel ('json', 'tty', 'markdown')
            **kwargs: Additional arguments to pass to adapter constructor (e.g., is_current)
        
        Returns:
            Adapter instance wrapping domain_object
        
        Raises:
            ValueError: If no adapter registered for domain type and channel
        """
        domain_type = type(domain_object).__name__
```

[X] ERROR (line 162)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @classmethod
    def register(cls, domain_type: str, channel: str, module_path: str, class_name: str):
        """
        Register new adapter mapping.
        Allows extending factory without modifying core code.
        """
        cls._registry[(domain_type, channel)] = (module_path, class_name)
```

---

## stop_writing_useless_comments
**cli_generator.py** - 7 violation(s)

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class CliGenerator:
    """Generates CLI scripts (shell and PowerShell) for bots."""
    
```

[X] ERROR (line 14)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, workspace_root: Path, bot_location: str):
        """
        Initialize CLI generator.
        
        Args:
            workspace_root: Root directory of the workspace
            bot_location: Relative path to bot directory (e.g., 'agile_bot/bots/story_bot')
        """
        self.workspace_root = Path(workspace_root)
```

[X] ERROR (line 26)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def generate_cli_code(self) -> Dict[str, str]:
        """
        Generate all CLI scripts.
        
        Returns:
            Dictionary with paths to generated files:
            - 'cli_script': Path to shell script (.sh)
            - 'cli_powershell': Path to PowerShell script (.ps1)
            - 'cli_python': Path to Python CLI entry point (for compatibility, returns module path)
        """
        results = {}
```

[X] ERROR (line 51)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _create_shell_script(self) -> Path:
        """Create shell script (.sh) for Unix/Linux/Mac."""
        script_name = 'story_cli.sh' if self.bot_name == 'story_bot' else f'{self.bot_name}_cli.sh'
```

[X] ERROR (line 105)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _create_powershell_script(self) -> Path:
        """Create PowerShell script (.ps1) for Windows."""
        script_name = 'story_cli.ps1' if self.bot_name == 'story_bot' else f'{self.bot_name}_cli.ps1'
```

[X] ERROR (line 91)
Useless comment: "# Set environment variables" - delete it or improve the code instead

```python
WORKSPACE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Set environment variables
export PYTHONPATH="$WORKSPACE_ROOT"
```

[X] ERROR (line 145)
Useless comment: "# Set environment variables" - delete it or improve the code instead

```python
$WORKSPACE_ROOT = Split-Path -Parent $SCRIPT_DIR

# Set environment variables
$env:PYTHONPATH = $WORKSPACE_ROOT
```

---

## stop_writing_useless_comments
**cli_results.py** - 2 violation(s)

[X] ERROR (line 14)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
@dataclass
class CLICommandResponse:
    """Response from a CLI command execution."""
    output: str
```

[X] ERROR (line 27)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
@dataclass
class TTYDetectionResult:
    """Result of TTY detection."""
    tty_detected: bool
```

---

## stop_writing_useless_comments
**cli_session.py** - 20 violation(s)

[X] ERROR (line 15)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class CLISession:
    """
    Minimal command router - parses commands, routes to Bot, uses adapter for serialization.
    
    Architecture:
    - Parse command -> Route to Bot method -> Get domain object -> Adapter serializes -> Output
    """
    
```

[X] ERROR (line 23)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, bot, workspace_directory: Path, mode: str = None):
        """
        Initialize CLI session.
        
        Args:
            bot: Bot instance with flattened API
            workspace_directory: Workspace directory path
            mode: Output mode ('tty', 'markdown', 'json'). If None, auto-detects:
                  - 'tty' if stdin is a TTY (interactive terminal)
                  - 'markdown' if stdin is piped (for AI agents)
                  - 'json' can be set explicitly for web views
        """
        self.bot = bot
```

[X] ERROR (line 39)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def execute_command(self, command: str) -> CLICommandResponse:
        """
        Route command to Bot method, return command response.
        
        Command mappings:
        - "status" -> bot itself (serialized via TTYBot)
        - "scope" -> bot.scope -> Scope object (property)
        - "next" -> bot.next() -> NavigationResult object
        - "back" -> bot.back() -> NavigationResult object
        - "help" -> bot.help() -> Help object
        - "exit" -> bot.exit() -> ExitResult object
        - "behavior.action" -> bot.execute('behavior', 'action') -> ActionResult
        
        Args:
            command: Command string from user input
        
        Returns:
            CLICommandResponse with serialized output and metadata
        """
        # Parse command
```

[X] ERROR (line 442)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _parse_command(self, command: str) -> tuple[str, str]:
        """Parse command into verb and arguments."""
        parts = command.split(maxsplit=1)
```

[X] ERROR (line 449)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _parse_save_params(self, args_string: str) -> Dict[str, Any]:
        """Parse save parameters from command arguments.
        
        Delegates to _parse_action_params since save uses the same parameter format.
        """
        return self._parse_action_params(args_string)
```

[X] ERROR (line 456)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _parse_action_params(self, args_string: str) -> Dict[str, Any]:
        """Parse action parameters from command arguments.
        
        Supports: --answers, --decisions, --assumptions, --evidence_provided
        
        Args:
            args_string: Arguments portion of command (e.g., "--answers '{...}' --assumptions '[...]'")
        
        Returns:
            Dict of parsed parameters ready for action context
        """
        import re
```

[X] ERROR (line 506)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _route_to_behavior_action(self, command: str) -> Any:
        """Route behavior or behavior.action commands to bot with parameter support.
        
        Now parses CLI parameters like --answers, --decisions, --assumptions
        and passes them to bot.execute() as params dict.
        """
        # Split command into core command and arguments
```

[X] ERROR (line 539)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_action_shortcut(self, action_name: str, args: str) -> Any:
        """Handle action shortcut commands (e.g., 'build', 'validate', 'rules').
        
        Routes to current behavior's action if action exists.
        For non-workflow actions (like 'rules'), directly executes and returns instructions.
        For workflow actions, navigates and shows instructions.
        Returns None if not an action shortcut (so caller can try other routing).
        """
        # Check if we have a current behavior
```

[X] ERROR (line 621)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _get_adapter_for_domain(self, domain_object: Any):
        """
        Select adapter based on domain object type and output context.
        
        Uses AdapterFactory to avoid cyclomatic complexity.
        """
        # Use explicit mode if set, otherwise auto-detect
```

[X] ERROR (line 637)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def run(self):
        """
        Run CLI loop (for interactive mode).
        
        Reads commands from stdin and executes them.
        """
        try:
```

[X] ERROR (line 62)
Useless comment: "# Set mode to json (stays that way until changed)" - delete it or improve the code instead

```python
        # Check for --format json flag and set mode
        if args and ('--format json' in args or '--format=json' in args):
            # Set mode to json (stays that way until changed)
            self.mode = 'json'
```

[X] ERROR (line 91)
Useless comment: "# Update self.bot to reference the new active bot" - delete it or improve the code instead

```python
                try:
                    self.bot.active_bot = target_bot_name
                    # Update self.bot to reference the new active bot
                    self.bot = self.bot.active_bot
```

[X] ERROR (line 207)
Useless comment: "# Execute behavior with current action (bot.execute handles " - delete it or improve the code instead

```python
                
                if is_behavior:
                    # Execute behavior with current action (bot.execute handles navigation)
                    result = self.bot.execute(result.name, None)
```

[X] ERROR (line 239)
Useless comment: "# Return submit result instead of instructions" - delete it or improve the code instead

```python
                            output_lines.append("  ✓ Cursor chat opened")
                        
                        # Return submit result instead of instructions
                        return CLICommandResponse(
```

[X] ERROR (line 255)
Useless comment: "# Get the instructions that were just generated" - delete it or improve the code instead

```python
                    # Special case: if action is 'rules', automatically submit to chat
                    if '.rules' in command.lower():
                        # Get the instructions that were just generated
                        from agile_bot.src.instructions.instructions import Instructions
```

[X] ERROR (line 279)
Useless comment: "# Return submit result instead of instructions" - delete it or improve the code instead

```python
                                    output_lines.append("  ✓ Cursor chat opened")
                                
                                # Return submit result instead of instructions
                                return CLICommandResponse(
```

[X] ERROR (line 289)
Useless comment: "# Return JSON error" - delete it or improve the code instead

```python
                    error_message = f"Unknown command '{verb}'"
                    if self.mode == 'json':
                        # Return JSON error
                        import json
```

[X] ERROR (line 298)
Useless comment: "# Return plain text error for TTY/Markdown" - delete it or improve the code instead

```python
                        output = json.dumps(error_dict, indent=2)
                    else:
                        # Return plain text error for TTY/Markdown
                        output = f"ERROR: {error_message}"
```

[X] ERROR (line 328)
Useless comment: "# Get appropriate adapter for result type" - delete it or improve the code instead

```python
                    is_navigation_command = True  # Action shortcut is navigation
        
        # Get appropriate adapter for result type
        adapter = self._get_adapter_for_domain(result)
```

[X] ERROR (line 588)
Useless comment: "# Create new Instructions object and populate from dict" - delete it or improve the code instead

```python
                    from ..instructions.instructions import Instructions
                    if isinstance(instructions_dict, dict):
                        # Create new Instructions object and populate from dict
                        instructions = Instructions(
```

---

## stop_writing_useless_comments
**orchestrator.py** - 2 violation(s)

[X] ERROR (line 93)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def generate_for_all_actions(self) -> None:
        """Traverse all (behavior, action) pairs - used for code generation."""
        self.visitor.visit_header(self.bot_name)
```

[X] ERROR (line 101)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _visit_behavior_action(self, behavior, action) -> None:
        """Visit a specific behavior-action pair with full object access."""
        context = ActionHelpContext(
```

---

## stop_writing_useless_comments
**visitor.py** - 1 violation(s)

[X] ERROR (line 24)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def data_collector(self):
        """Override in subclasses that need data collection."""
        return None
```

---

## stop_writing_useless_comments
**json_exit_result.py** - 3 violation(s)

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class JSONExitResult(JSONAdapter):
    """Serializes ExitResult to JSON - exposes all ExitResult properties."""
    
```

[X] ERROR (line 26)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_dict(self) -> dict:
        """Convert ExitResult to dict."""
        return {
```

[X] ERROR (line 33)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def deserialize(self, data: str) -> dict:
        """Parse JSON string to dict."""
        return json.loads(data)
```

---

## stop_writing_useless_comments
**markdown_exit_result.py** - 3 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class MarkdownExitResult(MarkdownAdapter):
    """Serializes ExitResult to Markdown."""
    
```

[X] ERROR (line 15)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert ExitResult to Markdown string."""
        lines = []
```

[X] ERROR (line 30)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**tty_exit_result.py** - 3 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYExitResult(TTYAdapter):
    """Serializes ExitResult to TTY - exposes all ExitResult properties."""
    
```

[X] ERROR (line 24)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert ExitResult to TTY string."""
        if self.exit_result.message:
```

[X] ERROR (line 31)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**help.py** - 25 violation(s)

[X] ERROR (line 16)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
@dataclass
class CoreCommands:
    """Core navigation and execution commands."""
    
```

[X] ERROR (line 20)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def navigation_pattern(self) -> str:
        """Returns the main navigation pattern."""
        return "echo '[behavior.][action.]operation' | python repl_main.py"
```

[X] ERROR (line 25)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def short_navigation_pattern(self) -> str:
        """Returns the short navigation pattern."""
        return "echo '[behavior][.action]' | python repl_main.py"
```

[X] ERROR (line 30)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def description_full(self) -> str:
        """Returns full navigation description."""
        return "navigate and perform operation"
```

[X] ERROR (line 35)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def description_short(self) -> str:
        """Returns short navigation description."""
        return "navigate to behavior/action"
```

[X] ERROR (line 41)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
@dataclass
class OtherCommands:
    """Utility commands for CLI."""
    
```

[X] ERROR (line 45)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def commands(self) -> List[tuple[str, str]]:
        """Returns list of (command, description) tuples."""
        return [
```

[X] ERROR (line 61)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
@dataclass
class CommandExamples:
    """Usage examples for CLI commands."""
    
```

[X] ERROR (line 65)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def examples(self) -> List[tuple[str, str]]:
        """Returns list of (command, description) tuples."""
        return [
```

[X] ERROR (line 78)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
@dataclass
class CommandsHelp:
    """Help for all CLI commands."""
    
```

[X] ERROR (line 88)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
@dataclass
class ScopeHelp:
    """Detailed help for scope command."""
    
```

[X] ERROR (line 92)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def important_rules(self) -> List[str]:
        """Returns important scope rules."""
        return [
```

[X] ERROR (line 103)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def usage_patterns(self) -> List[tuple[str, str]]:
        """Returns list of (pattern, description) tuples."""
        return [
```

[X] ERROR (line 113)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def correct_examples(self) -> List[tuple[str, str]]:
        """Returns list of (example, description) tuples."""
        return [
```

[X] ERROR (line 121)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def incorrect_examples(self) -> List[tuple[str, str]]:
        """Returns list of (example, reason) tuples for INCORRECT usage."""
        return [
```

[X] ERROR (line 131)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
@dataclass
class OperationsHelp:
    """Help for available operations."""
    
```

[X] ERROR (line 135)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def operations(self) -> List[tuple[str, str]]:
        """Returns list of (operation, parameters) tuples."""
        return [
```

[X] ERROR (line 145)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
@dataclass
class ComponentsHelp:
    """Help for available components (behaviors, actions, operations)."""
    
```

[X] ERROR (line 148)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, behaviors_names: Optional[List[str]] = None, actions_list: Optional[List] = None):
        """Initialize ComponentsHelp.
        
        Args:
            behaviors_names: List of behavior names (delegates to Behaviors.names)
            actions_list: List of Action objects (delegates to Actions)
        """
        self._behaviors_names = behaviors_names or []
```

[X] ERROR (line 160)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def behaviors(self) -> str:
        """Returns pipe-separated behavior names."""
        return " | ".join(self._behaviors_names)
```

[X] ERROR (line 165)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def actions(self) -> List[tuple[str, str]]:
        """Returns list of (action_name, description) tuples."""
        result = []
```

[X] ERROR (line 173)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class Help:
    """Main Help domain object.
    
    Provides hierarchical help information for the CLI:
    - Commands (core, other, examples)
    - Scope (rules, usage, examples)
    - Components (behaviors, actions, operations)
    """
    
```

[X] ERROR (line 182)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, bot=None):
        """Initialize Help.
        
        Args:
            bot: Bot instance for delegating to behaviors/actions
        """
        self.bot = bot
```

[X] ERROR (line 208)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def available_commands(self) -> List[str]:
        """Legacy property - returns list of command names."""
        return ['status', 'back', 'current', 'next', 'path', 'scope', 'help', 'exit']
```

[X] ERROR (line 194)
Useless comment: "# Get all unique actions across all behaviors" - delete it or improve the code instead

```python
        if bot:
            behaviors_names = bot.behaviors.names if hasattr(bot, 'behaviors') else []
            # Get all unique actions across all behaviors
            actions_list = []
```

---

## stop_writing_useless_comments
**help_action.py** - 5 violation(s)

[X] ERROR (line 16)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TypeHintConverter:
    """Converts Python type hints to CLI-friendly type strings for help display"""
    
```

[X] ERROR (line 20)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @staticmethod
    def to_cli_type(python_type) -> str:
        """Convert Python type hint to CLI-friendly string.
        
        Examples:
            str -> "string"
            Path -> "path"
            dict -> "dict"
            Dict[str, Any] -> "dict"
            List[str] -> "list"
        """
        # Handle None type
```

[X] ERROR (line 233)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _get_parameter_description(self, action_name: str, param_name: str) -> str:
        """Get meaningful description for a parameter (like ActionDataCollector does)"""
        # Check common parameter patterns
```

[X] ERROR (line 251)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _get_scope_description(self, action_name: str) -> str:
        """Get scope description for an action"""
        if action_name == 'validate':
```

[X] ERROR (line 53)
Useless comment: "# Handle generic types (Dict[...], List[...], etc.)" - delete it or improve the code instead

```python
            return "set"
        
        # Handle generic types (Dict[...], List[...], etc.)
        origin = get_origin(python_type)
```

---

## stop_writing_useless_comments
**json_help.py** - 5 violation(s)

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class JSONHelp(JSONAdapter):
    """Serializes Help domain object to JSON."""
    
```

[X] ERROR (line 14)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, help_obj: Help):
        """
        Initialize JSON adapter for Help.
        
        Args:
            help_obj: Help domain object to serialize
        """
        self.help_obj = help_obj
```

[X] ERROR (line 23)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_dict(self) -> dict:
        """Convert Help to dict - mirrors TTYHelp structure."""
        return {
```

[X] ERROR (line 48)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Help to JSON string."""
        return json.dumps(self.to_dict(), indent=2)
```

[X] ERROR (line 52)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def deserialize(self, data: str) -> Help:
        """Reconstruct Help from JSON string."""
        help_data = json.loads(data)
```

---

## stop_writing_useless_comments
**markdown_help.py** - 3 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class MarkdownHelp(MarkdownAdapter):
    """Serializes Help to Markdown."""
    
```

[X] ERROR (line 15)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Help to Markdown string - mirrors TTYHelp structure."""
        lines = []
```

[X] ERROR (line 76)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**tty_help.py** - 4 violation(s)

[X] ERROR (line 10)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYHelp(TTYAdapter):
    """Serializes Help domain object to TTY - delegates to help sub-objects."""
    
```

[X] ERROR (line 13)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, help_obj: Help):
        """Initialize TTY adapter for Help.
        
        Args:
            help_obj: Help domain object to serialize
        """
        self.help_obj = help_obj
```

[X] ERROR (line 21)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Help to TTY string - assembles all help sections."""
        lines = []
```

[X] ERROR (line 82)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text into verb and args."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**instructions.py** - 2 violation(s)

[X] ERROR (line 38)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def scope(self) -> Optional['Scope']:
        """Get the scope filter if set."""
        return self._scope
```

[X] ERROR (line 43)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def context_sources_text(self) -> List[str]:
        """Generate standard 'Look for context in the following locations' section with actual paths."""
        if not self._bot_paths:
```

---

## stop_writing_useless_comments
**json_instructions.py** - 3 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class JSONInstructions(JSONAdapter):
    """Serializes Instructions to JSON - returns structured instruction data."""
    
```

[X] ERROR (line 15)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Instructions to JSON string."""
        import json
```

[X] ERROR (line 20)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_dict(self) -> dict:
        """Convert Instructions to dictionary for JSON serialization."""
        return self.instructions.to_dict()
```

---

## stop_writing_useless_comments
**markdown_instructions.py** - 6 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class MarkdownInstructions(MarkdownAdapter):
    """Serializes Instructions to Markdown - formats for markdown documents."""
    
```

[X] ERROR (line 15)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Instructions to Markdown string."""
        instructions_dict = self.instructions.to_dict()
```

[X] ERROR (line 256)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _format_strategy_option(self, option) -> list:
        """Format a single decision criteria option for markdown display."""
        lines = []
```

[X] ERROR (line 272)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text (not used for Instructions)."""
        parts = text.split(maxsplit=1)
```

[X] ERROR (line 40)
Useless comment: "# Get the filtered results (story graph or files)" - delete it or improve the code instead

```python
            output_lines.append("")
            
            # Get the filtered results (story graph or files)
            # Show results when scope has filter values OR when type is 'showAll'
```

[X] ERROR (line 175)
Useless comment: "# Get saved decisions (check both 'decisions' and 'decisions" - delete it or improve the code instead

```python
            strategy_criteria = strategy_criteria or strategy_data['strategy_criteria']
        
        # Get saved decisions (check both 'decisions' and 'decisions_made' keys)
        saved_decisions = {}
```

---

## stop_writing_useless_comments
**tty_instructions.py** - 6 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYInstructions(TTYAdapter):
    """Serializes Instructions to TTY - formats all instruction components."""
    
```

[X] ERROR (line 15)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Instructions to TTY string - assembles all instruction sections."""
        instructions_dict = self.instructions.to_dict()
```

[X] ERROR (line 226)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _format_strategy_option(self, option, selected_value=None) -> list:
        """Format a single decision criteria option for display, marking if selected."""
        lines = []
```

[X] ERROR (line 255)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text (not used for Instructions)."""
        parts = text.split(maxsplit=1)
```

[X] ERROR (line 140)
Useless comment: "# Get saved decisions (check both 'decisions' and 'decisions" - delete it or improve the code instead

```python
            strategy_criteria = strategy_criteria or strategy_data['strategy_criteria']
        
        # Get saved decisions (check both 'decisions' and 'decisions_made' keys)
        saved_decisions = {}
```

[X] ERROR (line 193)
Useless comment: "# Get the selected value for this criterion" - delete it or improve the code instead

```python
                            output_lines.append(self.add_bold(f"{criteria_key}:"))
                        
                        # Get the selected value for this criterion
                        selected_value = saved_decisions.get(criteria_key) if saved_decisions else None
```

---

## stop_writing_useless_comments
**json_navigation.py** - 3 violation(s)

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class JSONNavigation(JSONAdapter):
    """Serializes NavigationResult to JSON - exposes all NavigationResult properties."""
    
```

[X] ERROR (line 30)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_dict(self) -> dict:
        """Convert NavigationResult to dict."""
        return {
```

[X] ERROR (line 38)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def deserialize(self, data: str) -> dict:
        """Parse JSON string to dict."""
        return json.loads(data)
```

---

## stop_writing_useless_comments
**markdown_navigation.py** - 3 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class MarkdownNavigation(MarkdownAdapter):
    """Serializes NavigationResult to Markdown."""
    
```

[X] ERROR (line 15)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert NavigationResult to Markdown string."""
        lines = []
```

[X] ERROR (line 37)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**tty_navigation.py** - 3 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYNavigation(TTYAdapter):
    """Serializes NavigationResult to TTY - exposes all NavigationResult properties."""
    
```

[X] ERROR (line 28)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert NavigationResult to TTY string."""
        lines = []
```

[X] ERROR (line 49)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**rule.py** - 1 violation(s)

[X] ERROR (line 236)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _format_rule_section(self, section_key: str, header: str, formatted: list) -> None:
        """Helper to format a rule section (DO or DON'T) with description and guidance."""
        section = self._rule_content.get(section_key, {})
```

---

## stop_writing_useless_comments
**rules.py** - 3 violation(s)

[X] ERROR (line 70)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @classmethod
    def _get_files_for_validation(cls, behavior, context: 'ValidateActionContext') -> Dict[str, List[Path]]:
        """Get files to validate based on behavior validation type and scope."""
        from agile_bot.src.actions.validate.file_discovery import FileDiscovery
```

[X] ERROR (line 48)
Useless comment: "# Get files - either from scope filter or discover all" - delete it or improve the code instead

```python
            story_graph_content = validation_scope.filter_story_graph(story_graph_content)
        
        # Get files - either from scope filter or discover all
        files = cls._get_files_for_validation(behavior, context)
```

[X] ERROR (line 266)
Useless comment: "# Load bot-level rules" - delete it or improve the code instead

```python
        all_rules = []
        
        # Load bot-level rules
        bot_rules = self._rule_loader.load_bot_rules()
```

---

## stop_writing_useless_comments
**rules_action.py** - 3 violation(s)

[X] ERROR (line 12)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _load_behavior_guardrails(self, instructions):
        """Rules action should not load guardrails/clarifications - it's just for displaying rules."""
        pass
```

[X] ERROR (line 16)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _prepare_instructions(self, instructions, context: RulesActionContext):
        """Prepare rules instructions by building rules digest and adding to display content."""
        rules = Rules(behavior=self.behavior, bot_paths=self.behavior.bot_paths)
```

[X] ERROR (line 44)
Useless comment: "# Create a mapping of rule names to rule objects for file pa" - delete it or improve the code instead

```python
        instructions.add_display(f"## Rules Available ({len(rule_names)} total)")
        instructions.add_display("")
        # Create a mapping of rule names to rule objects for file path lookup
        rule_map = {rule.name: rule for rule in rules}
```

---

## stop_writing_useless_comments
**rules_digest_guidance.py** - 1 violation(s)

[X] ERROR (line 5)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class GuidanceLineCollection:
    """Collection class for guidance lines"""
    def __init__(self, lines: List[str]):
```

---

## stop_writing_useless_comments
**rule_loader.py** - 1 violation(s)

[X] ERROR (line 17)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def load_bot_rules(self) -> List[Rule]:
        """Load bot-level rules from <bot_directory>/rules/"""
        bot_rules_dir = self.bot_paths.bot_directory / 'rules'
```

---

## stop_writing_useless_comments
**active_language_scanner.py** - 1 violation(s)

[X] ERROR (line 13)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class ActiveLanguageScanner(StoryScanner):
    """
    Validates that story names use active language without actor prefixes.
    Uses NLTK to detect actor/role words at the beginning of story names.
    """
    
```

---

## stop_writing_useless_comments
**actor_alternation_scanner.py** - 3 violation(s)

[X] ERROR (line 8)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class ActorAlternationScanner(StoryScanner):
    """
    Scans acceptance criteria to ensure actors alternate every 1-2 steps.
    Scenarios should show back-and-forth interaction between user and system.
    """
    
```

[X] ERROR (line 30)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _check_actor_alternation(self, ac: str, story: Story, ac_index: int, rule_obj: Any) -> Optional[Dict[str, Any]]:
        """Check if actors alternate properly in acceptance criteria."""
        lines = ac.split('\n')
```

[X] ERROR (line 75)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _extract_actor(self, line: str) -> Optional[str]:
        """Extract the actor (user/system) from a WHEN/THEN/AND line."""
        line_lower = line.lower()
```

---

## stop_writing_useless_comments
**behavioral_ac_scanner.py** - 1 violation(s)

[X] ERROR (line 13)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        """
        This scanner is disabled - it was counting AC incorrectly.
        The story_sizing_scanner handles AC count validation.
        
        AC counting rules:
        - Each WHEN starts a new AC
        - Each AND adds +1 to the AC count
        - THEN is part of the AC but doesn't add to count
        
        Example:
        WHEN user clicks button
        THEN system validates
        AND system saves
        AND system displays message
        = 3 AC (1 WHEN + 2 ANDs)
        """
        violations = []
```

---

## stop_writing_useless_comments
**dead_code_scanner.py** - 4 violation(s)

[X] ERROR (line 21)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class DeadCodeScanner(CodeScanner):
    """Scanner for detecting dead/unused code."""
    
```

[X] ERROR (line 151)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _analyze_file(self, file_path: Path) -> Tuple[Dict[str, Tuple[int, str]], Set[str]]:
        """Analyze a file to extract definitions and usages.
        
        Returns:
            Tuple of (definitions, usages) where:
            - definitions: {name: (line_number, node_type)}
            - usages: set of names that are referenced/called
        """
        definitions = {}
```

[X] ERROR (line 198)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _analyze_private_members(self, tree: ast.AST) -> Tuple[Dict[str, Tuple[int, str]], Set[str]]:
        """Analyze private members (_name) and their usages within classes.
        
        Returns:
            Tuple of (private_defs, private_usages) where:
            - private_defs: {method_name: (line_number, class_name)}
            - private_usages: set of method names that are called
        """
        private_defs = {}
```

[X] ERROR (line 231)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _is_entry_point_or_special(self, name: str, node_type: str) -> bool:
        """Check if a name is an entry point or special case that shouldn't be flagged."""
        
```

---

## stop_writing_useless_comments
**domain_scanner.py** - 2 violation(s)

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class DomainScanner(Scanner):
    """Base class for scanners that validate domain concepts.
    
    Domain scanners scan domain_concepts arrays in epics and sub_epics.
    They do NOT scan story/epic/sub-epic nodes themselves.
    """
    
```

[X] ERROR (line 86)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @abstractmethod
    def scan_domain_concept(self, node: DomainConceptNode, rule_obj: Any) -> List[Dict[str, Any]]:
        """Scan a single domain concept for violations.
        
        This method must be implemented by domain scanners.
        """
        pass
```

---

## stop_writing_useless_comments
**full_result_assertions_scanner.py** - 3 violation(s)

[X] ERROR (line 12)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class FullResultAssertionsScanner(TestScanner):
    """Detect assertions that only check a single field of complex objects instead of the whole result."""

```

[X] ERROR (line 111)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _has_full_object_assert(self, func_node: ast.FunctionDef, aliases: Set[str]) -> bool:
        """Detect if function asserts equality of whole object (dict or dataclass-like) on a result-like target."""
        for node in ast.walk(func_node):
```

[X] ERROR (line 123)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _collect_result_aliases(self, func_node: ast.FunctionDef) -> Set[str]:
        """
        Collect names that likely hold result/state objects:
        - Assignment from a call with result-ish name.
        - Assignment from an existing target name.
        """
        aliases: Set[str] = set()
```

---

## stop_writing_useless_comments
**object_oriented_helpers_scanner.py** - 5 violation(s)

[X] ERROR (line 12)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class ObjectOrientedHelpersScanner(TestScanner):
    """
    Detect test functions that rely on many ad-hoc given/when/then helpers or
    param-soup setups instead of consolidating through an object-oriented helper
    (e.g., BotTestHelper / factory objects).
    """

```

[X] ERROR (line 73)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _count_params(self, func_node: ast.FunctionDef) -> int:
        """Count parameters excluding self/cls."""
        return sum(
```

[X] ERROR (line 81)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _parametrize_column_count(self, func_node: ast.FunctionDef) -> int:
        """Estimate number of parametrize columns from decorators."""
        for decorator in func_node.decorator_list:
```

[X] ERROR (line 93)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _given_when_then_calls(self, func_node: ast.FunctionDef) -> int:
        """Count calls to given_/when_/then_ helpers inside a test function."""
        count = 0
```

[X] ERROR (line 108)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _uses_helper(self, func_node: ast.FunctionDef) -> bool:
        """Detect Helper/Factory usage inside a test function."""
        for inner in ast.walk(func_node):
```

---

## stop_writing_useless_comments
**reaction_chaining_scanner.py** - 3 violation(s)

[X] ERROR (line 8)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class ReactionChainingScanner(StoryScanner):
    """
    Scans acceptance criteria to ensure multiple system reactions are chained with 'And'.
    Checks that separate WHEN/THEN blocks aren't created for sequential system actions.
    """
    
```

[X] ERROR (line 30)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _check_reaction_chaining(self, ac: str, story: Story, ac_index: int, rule_obj: Any) -> Optional[Dict[str, Any]]:
        """Check if system reactions are properly chained with And instead of separate WHEN/THEN."""
        lines = [line.strip() for line in ac.split('\n') if line.strip()]
```

[X] ERROR (line 75)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _is_system_action(self, line: str) -> bool:
        """Check if a line describes a system action."""
        line_lower = line.lower()
```

---

## stop_writing_useless_comments
**resource_oriented_code_scanner.py** - 1 violation(s)

[X] ERROR (line 17)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class ResourceOrientedCodeScanner(CodeScanner):
    """
    Validates that code classes are named after resources (what they ARE)
    rather than actions (what they DO).
    
    Uses NLTK to detect agent nouns (Manager, Loader, Handler, etc.)
    """
    
```

---

## stop_writing_useless_comments
**resource_oriented_design_scanner.py** - 1 violation(s)

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class ResourceOrientedDesignScanner(DomainScanner):
    """
    Validates that domain concepts are named after resources (what they ARE)
    rather than actions (what they DO).
    
    Uses NLTK to detect agent nouns (Manager, Loader, Handler, etc.)
    which are nouns derived from verbs that describe doers of actions.
    """
    
```

---

## stop_writing_useless_comments
**scanner.py** - 1 violation(s)

[X] ERROR (line 51)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _empty_violation_list(self) -> List[Dict[str, Any]]:
        """Helper method for default empty implementations."""
        return []
```

---

## stop_writing_useless_comments
**setup_similarity_scanner.py** - 1 violation(s)

[X] ERROR (line 13)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class SetupSimilarityScanner(TestScanner):
    """
    Detect repeated setup payloads (dicts) across tests that should be centralized
    into shared helpers/fixtures/standard data sets.
    
    NOTE: This prototype derives signals purely from the code it scans—no hardcoded
    domain keys. It looks for repeated keysets/shapes across tests and flags reuse.
    """

```

---

## stop_writing_useless_comments
**standard_data_reuse_scanner.py** - 1 violation(s)

[X] ERROR (line 12)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class StandardDataReuseScanner(TestScanner):
    """Detect repeated ad-hoc inline data instead of shared canonical fixtures/constants."""

```

---

## stop_writing_useless_comments
**story_map.py** - 2 violation(s)

[X] ERROR (line 77)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def all_stories(self) -> List['Story']:
        """Return all Story nodes within this epic (including nested sub-epics)."""
        stories: List['Story'] = []
```

[X] ERROR (line 293)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def find_epic_by_name(self, epic_name: str) -> 'Epic':
        """Find an epic by name."""
        for epic in self.epics():
```

---

## stop_writing_useless_comments
**story_sizing_scanner.py** - 1 violation(s)

[X] ERROR (line 83)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _count_when_then_and(self, acceptance_criteria: List) -> int:
        """
        Count acceptance criteria based on WHEN/AND keywords.
        - Each WHEN = 1 AC
        - Each AND = +1 AC
        - THEN doesn't add to count (it's part of the WHEN AC)
        
        Example:
        WHEN user does X
        THEN system responds
        AND system does Y
        AND system does Z
        = 3 AC (1 WHEN + 2 ANDs)
        """
        combined_text = ' '.join([self._get_ac_text(ac) for ac in acceptance_criteria])
```

---

## stop_writing_useless_comments
**technical_abstraction_scanner.py** - 1 violation(s)

[X] ERROR (line 12)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TechnicalAbstractionScanner(DomainScanner):
    """
    Validates that domain concepts avoid exposing technical abstractions.
    Uses NLTK to detect agent nouns like Saver, Loader, Storage.
    """
    
```

---

## stop_writing_useless_comments
**test_scanner.py** - 1 violation(s)

[X] ERROR (line 27)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _empty_violation_list(self) -> List[Dict[str, Any]]:
        """Helper method for default empty implementations."""
        return []
```

---

## stop_writing_useless_comments
**verb_noun_scanner.py** - 3 violation(s)

[X] ERROR (line 206)
Useless comment: "# Handle verbs ending in -es (e.g., "fixes" -> "fix", "watch" - delete it or improve the code instead

```python
        if verb_lower.endswith("ies") and len(verb_lower) > 3:
            base = verb_lower[:-3] + "y"
        # Handle verbs ending in -es (e.g., "fixes" -> "fix", "watches" -> "watch", "goes" -> "go")
        elif verb_lower.endswith("es") and len(verb_lower) > 2:
```

[X] ERROR (line 419)
Useless comment: "# Handle hyphenated verbs (e.g., "Auto-Run", "Re-execute", "" - delete it or improve the code instead

```python
            has_verb = any(self._is_verb(tag[1]) for tag in tags)
            
            # Handle hyphenated verbs (e.g., "Auto-Run", "Re-execute", "Auto-Confirm")
            # When a noun is in front of a verb with a dash, we should accept it as valid
```

[X] ERROR (line 442)
Useless comment: "# Handle adverb-verb combinations (e.g., "proactively Valida" - delete it or improve the code instead

```python
                            has_verb = True
            
            # Handle adverb-verb combinations (e.g., "proactively Validate")
            # Adverb-verb combinations are ENCOURAGED and valid verb-noun format
```

---

## stop_writing_useless_comments
**vocabulary_helper.py** - 12 violation(s)

[X] ERROR (line 45)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class VocabularyHelper:
    """Helper class for linguistic analysis using NLTK."""
    
```

[X] ERROR (line 55)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @staticmethod
    def is_verb(word: str) -> bool:
        """Check if word can function as a verb using WordNet."""
        try:
```

[X] ERROR (line 65)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @staticmethod
    def is_noun(word: str) -> bool:
        """Check if word can function as a noun using WordNet."""
        try:
```

[X] ERROR (line 75)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @staticmethod
    def is_agent_noun(word: str) -> tuple[bool, Optional[str], Optional[str]]:
        """
        Check if word is an agent noun (doer of action).
        Returns: (is_agent, base_verb, suffix) or (False, None, None)
        
        Examples:
            'Manager' -> (True, 'manage', 'er')
            'Processor' -> (True, 'process', 'or')
            'Portfolio' -> (False, None, None)
        """
        word_lower = word.lower()
```

[X] ERROR (line 106)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @staticmethod
    def is_gerund(word: str) -> tuple[bool, Optional[str]]:
        """
        Check if word is a gerund (verb + ing).
        Returns: (is_gerund, base_verb) or (False, None)
        
        Examples:
            'Loading' -> (True, 'load')
            'Running' -> (True, 'run')
            'Thing' -> (False, None)
        """
        word_lower = word.lower()
```

[X] ERROR (line 144)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @staticmethod
    def get_pos_tags(text: str) -> List[tuple[str, str]]:
        """Get part-of-speech tags for text."""
        try:
```

[X] ERROR (line 154)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @staticmethod
    def is_verb_tag(tag: str) -> bool:
        """Check if POS tag indicates a verb."""
        verb_tags = ['VB', 'VBP', 'VBZ', 'VBD', 'VBG', 'VBN']
```

[X] ERROR (line 160)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @staticmethod
    def is_noun_tag(tag: str) -> bool:
        """Check if POS tag indicates a noun."""
        noun_tags = ['NN', 'NNS', 'NNP', 'NNPS']
```

[X] ERROR (line 166)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @staticmethod
    def is_proper_noun_tag(tag: str) -> bool:
        """Check if POS tag indicates a proper noun."""
        proper_noun_tags = ['NNP', 'NNPS']
```

[X] ERROR (line 172)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @staticmethod
    def is_actor_or_role(word: str) -> bool:
        """
        Check if word represents an actor or role (person, system, agent).
        Uses WordNet to check if word is a hyponym of 'person' or 'system'.
        
        Examples:
            'customer' -> True (person who buys)
            'user' -> True (person who uses)
            'developer' -> True (person who develops)
            'system' -> True (computing system)
            'api' -> True (system interface)
            'order' -> False (not a person/system)
        """
        try:
```

[X] ERROR (line 187)
Useless comment: "# Get all synsets for the word" - delete it or improve the code instead

```python
            word_lower = word.lower()
            
            # Get all synsets for the word
            synsets = wn.synsets(word_lower)
```

[X] ERROR (line 195)
Useless comment: "# Get all hypernyms (parent concepts)" - delete it or improve the code instead

```python
            # Get hypernym paths for all synsets
            for synset in synsets:
                # Get all hypernyms (parent concepts)
                hypernyms = set()
```

---

## stop_writing_useless_comments
**action_scope.py** - 1 violation(s)

[X] ERROR (line 20)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @classmethod
    def from_context(cls, context: 'ScopeActionContext', bot_paths: Optional[BotPath] = None) -> 'ActionScope':
        """Create ActionScope from ScopeActionContext.
        
        Args:
            context: ScopeActionContext with typed scope
            bot_paths: Optional BotPath instance
            
        Returns:
            ActionScope instance
        """
        params = {}
```

---

## stop_writing_useless_comments
**json_scope.py** - 11 violation(s)

[X] ERROR (line 12)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class JSONScope(JSONAdapter):
    """Serializes Scope to JSON - exposes all Scope properties."""
    
```

[X] ERROR (line 43)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_dict(self) -> dict:
        """Convert Scope to dict with filtered content for panel display."""
        # Start with basic scope criteria
```

[X] ERROR (line 89)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _enrich_with_links(self, epics: list, story_graph):
        """Enrich story graph epics with test file and document links."""
        if not self.scope.workspace_directory or not self.scope.bot_paths:
```

[X] ERROR (line 116)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _enrich_sub_epic_with_links(self, sub_epic: dict, test_dir: Path, docs_stories_map: Path, epic_name: str, parent_path: str = None):
        """Recursively enrich sub-epic with test file and document links."""
        # Build the document path (epic/sub-epic hierarchy)
```

[X] ERROR (line 158)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _enrich_story_with_links(self, story: dict, test_dir: Path, parent_doc_folder: Path, parent_test_file: str):
        """Enrich story with test file links (with #test_class anchor) and document links."""
        # Initialize links array
```

[X] ERROR (line 193)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _enrich_scenario_with_links(self, scenario: dict, test_dir: Path, story_test_file: str, story_test_class: str):
        """Enrich scenario with test file link (with #L<line_number> anchor for VS Code)."""
        test_method = scenario.get('test_method')
```

[X] ERROR (line 213)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def deserialize(self, data: str) -> dict:
        """Parse JSON string to dict."""
        return json.loads(data)
```

[X] ERROR (line 54)
Useless comment: "# Get filtered story graph" - delete it or improve the code instead

```python
        # Add filtered content based on scope type
        if self.scope.type.value in ('story', 'showAll'):
            # Get filtered story graph
            story_graph = self.scope._get_story_graph_results()
```

[X] ERROR (line 82)
Useless comment: "# Get filtered file list" - delete it or improve the code instead

```python
                        })
        elif self.scope.type.value == 'files':
            # Get filtered file list
            files = self.scope._get_file_results()
```

[X] ERROR (line 93)
Useless comment: "# Get the test directory from bot paths" - delete it or improve the code instead

```python
            return
        
        # Get the test directory from bot paths
        test_dir = self.scope.workspace_directory / self.scope.bot_paths.test_path
```

[X] ERROR (line 95)
Useless comment: "# Get the docs/stories/map directory for document links" - delete it or improve the code instead

```python
        # Get the test directory from bot paths
        test_dir = self.scope.workspace_directory / self.scope.bot_paths.test_path
        # Get the docs/stories/map directory for document links
        docs_stories_map = self.scope.workspace_directory / 'docs' / 'stories' / 'map'
```

---

## stop_writing_useless_comments
**json_scope_command_result.py** - 3 violation(s)

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class JSONScopeCommandResult(JSONAdapter):
    """Serializes ScopeCommandResult to JSON with full scope data."""
    
```

[X] ERROR (line 17)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_dict(self) -> dict:
        """Convert ScopeCommandResult to dict for JSON serialization."""
        from agile_bot.src.scope.json_scope import JSONScope
```

[X] ERROR (line 31)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def deserialize(self, data: str) -> dict:
        """Parse JSON string to dict."""
        return json.loads(data)
```

---

## stop_writing_useless_comments
**markdown_scope.py** - 4 violation(s)

[X] ERROR (line 10)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class MarkdownScope(MarkdownAdapter):
    """Serializes Scope to Markdown."""
    
```

[X] ERROR (line 17)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Scope to Markdown string - delegates to result domain adapters."""
        lines = []
```

[X] ERROR (line 71)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

[X] ERROR (line 32)
Useless comment: "# Get results from Scope and delegate to appropriate adapter" - delete it or improve the code instead

```python
        lines.append("")
        
        # Get results from Scope and delegate to appropriate adapter
        results = self.scope.results
```

---

## stop_writing_useless_comments
**markdown_scope_command_result.py** - 4 violation(s)

[X] ERROR (line 10)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class MarkdownScopeCommandResult(MarkdownAdapter):
    """Serializes ScopeCommandResult to markdown format."""
    
```

[X] ERROR (line 16)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert ScopeCommandResult to markdown string."""
        from agile_bot.src.scope.markdown_scope import MarkdownScope
```

[X] ERROR (line 27)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text into verb and params."""
        parts = text.split(maxsplit=1)
```

[X] ERROR (line 23)
Useless comment: "# Return the markdown representation" - delete it or improve the code instead

```python
        scope_markdown = scope_adapter.serialize()
        
        # Return the markdown representation
        return scope_markdown
```

---

## stop_writing_useless_comments
**scope.py** - 26 violation(s)

[X] ERROR (line 27)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
@dataclass
class StoryGraphFilter:
    """Filters content by story graph nodes (stories, epics, sub-epics).
    
    Used for filtering operations to specific parts of the story graph.
    Searches across ALL levels of the hierarchy (epic/sub-epic/story).
    """
    search_terms: List[str] = field(default_factory=list)
```

[X] ERROR (line 36)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def matches_node(self, node_name: str) -> bool:
        """Check if node (epic/sub-epic/story) matches filter."""
        if not self.search_terms:
```

[X] ERROR (line 42)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def filter_story_graph(self, story_graph: Dict[str, Any]) -> Dict[str, Any]:
        """Filter story graph to only nodes matching this filter.
        
        Searches ALL levels (epics, sub-epics, nested sub-epics, stories) regardless of where the term appears.
        Recursively handles nested sub-epics at any depth.
        """
        if not self.search_terms and not self.increments:
```

[X] ERROR (line 56)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
        
        def filter_sub_epic(sub_epic: Dict[str, Any]) -> Optional[Dict[str, Any]]:
            """Recursively filter a sub-epic and its nested sub-epics.
            
            Returns:
                Filtered sub-epic dict if it or any of its children match, None otherwise.
            """
            sub_epic_name = sub_epic.get('name', '')
```

[X] ERROR (line 133)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
@dataclass
class FileFilter:
    """Filters files by path patterns.
    
    Supports glob patterns for include/exclude.
    """
    include_patterns: List[str] = field(default_factory=list)
```

[X] ERROR (line 141)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def matches_file(self, file_path: Path) -> bool:
        """Check if file matches the filter.
        
        Note: This method performs simple substring matching. For full glob pattern
        matching, use filter_files() which implements complete glob pattern support.
        """
        if not self.include_patterns:
```

[X] ERROR (line 155)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def filter_files(self, file_list: List[Path]) -> List[Path]:
        """Filter file list to only files matching this filter."""
        if not self.include_patterns and not self.exclude_patterns:
```

[X] ERROR (line 208)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class Scope:
    """Scope for filtering bot operations to specific content.
    
    Scope is created once with workspace context and provides:
    - filter() method to set filter criteria
    - results property that returns filtered StoryGraph or file list
    - Persistence to bot state file
    """
    
```

[X] ERROR (line 217)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, workspace_directory: Path, bot_paths=None):
        """Initialize Scope with workspace context.
        
        Args:
            workspace_directory: Workspace directory path
            bot_paths: Optional BotPath for story graph loading
        """
        self.workspace_directory = Path(workspace_directory)
```

[X] ERROR (line 241)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def filter(self, type: ScopeType, value: List[str] = None, exclude: List[str] = None, skiprule: List[str] = None):
        """Set filter criteria.
        
        Args:
            type: Scope type (STORY, FILES, etc.)
            value: Filter values (story names, file patterns, etc.)
            exclude: Exclusion patterns
            skiprule: Rules to skip
        """
        self.type = type
```

[X] ERROR (line 262)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def clear(self):
        """Clear all filters."""
        self.filter(ScopeType.ALL, [], [], [])
```

[X] ERROR (line 266)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _rebuild_filters(self):
        """Rebuild internal filter objects from current criteria."""
        self._story_graph_filter = None
```

[X] ERROR (line 285)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def results(self) -> Union['StoryGraph', List[Path], None]:
        """Get filtered results as domain objects.
        
        Returns:
            - StoryGraph object for story/epic/increment scopes
            - List of Path objects for file scopes
            - None for ALL scope
        """
        if not self._results_dirty and self._cached_results is not None:
```

[X] ERROR (line 307)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _get_story_graph_results(self):
        """Get filtered story graph as StoryGraph object."""
        story_graph_path = self.workspace_directory / 'docs' / 'stories' / 'story-graph.json'
```

[X] ERROR (line 344)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _get_file_results(self) -> List[Path]:
        """Get filtered file list."""
        import glob as glob_module
```

[X] ERROR (line 386)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def filters_story_graph(self, story_graph: Dict[str, Any]) -> Dict[str, Any]:
        """Legacy method - filters story graph dict."""
        if self._story_graph_filter:
```

[X] ERROR (line 392)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def filters_files(self, file_list: List[Path]) -> List[Path]:
        """Legacy method - filters file list."""
        if self._file_filter:
```

[X] ERROR (line 398)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_dict(self) -> Dict[str, Any]:
        """Serialize scope criteria to dict for persistence."""
        return {
```

[X] ERROR (line 408)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @classmethod
    def from_dict(cls, data: Dict[str, Any], workspace_directory: Path, bot_paths=None) -> 'Scope':
        """Load scope from dict.
        
        Args:
            data: Scope data dict
            workspace_directory: Workspace directory
            bot_paths: Optional BotPath
        """
        scope = cls(workspace_directory, bot_paths)
```

[X] ERROR (line 443)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def save(self):
        """Save scope to scope.json file."""
        scope_file = self.workspace_directory / 'scope.json'
```

[X] ERROR (line 450)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def load(self):
        """Load scope from scope.json file."""
        scope_file = self.workspace_directory / 'scope.json'
```

[X] ERROR (line 482)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    # Legacy methods for backward compatibility
    def apply_to_bot(self, workspace_directory: Path = None):
        """Legacy method - save scope to state file."""
        self.save()
```

[X] ERROR (line 487)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @staticmethod
    def clear_from_bot(workspace_directory: Path) -> None:
        """Clear scope from bot state file."""
        state_file = workspace_directory / 'behavior_action_state.json'
```

[X] ERROR (line 314)
Useless comment: "# Load and filter graph data" - delete it or improve the code instead

```python
        
        try:
            # Load and filter graph data
            graph_data = json.loads(story_graph_path.read_text(encoding='utf-8'))
```

[X] ERROR (line 330)
Useless comment: "# Create minimal BotPath just for story graph" - delete it or improve the code instead

```python
                story_graph = StoryGraph(self.bot_paths, self.workspace_directory, require_file=False)
            else:
                # Create minimal BotPath just for story graph
                bot_path = BotPath(bot_directory=self.workspace_directory)
```

[X] ERROR (line 460)
Useless comment: "# Update this instance from loaded data" - delete it or improve the code instead

```python
            
            if scope_data:
                # Update this instance from loaded data
                scope_type_str = scope_data.get('type', 'all')
```

---

## stop_writing_useless_comments
**scope_command_result.py** - 2 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class ScopeCommandResult:
    """Result of a scope command - includes status, message, and the Scope object."""
    
```

[X] ERROR (line 12)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, status: str, message: str, scope: 'Scope'):
        """Initialize scope command result.
        
        Args:
            status: Status string (success, error, etc.)
            message: Human-readable message
            scope: The Scope domain object
        """
        self.status = status
```

---

## stop_writing_useless_comments
**scope_matcher.py** - 6 violation(s)

[X] ERROR (line 7)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

def find_scope_matches(graph_data: Dict[str, Any], scope_values: List[str], use_emoji: bool = False) -> List[str]:
    """Find and display scope matches from story graph.
    
    Args:
        graph_data: Story graph data with epics structure
        scope_values: List of scope values to match
        use_emoji: If True, use emoji formatting; if False, use bracket formatting
        
    Returns:
        List of formatted match lines
    """
    lines = []
```

[X] ERROR (line 31)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

def search_for_scope_match(epics: List[Dict], scope_val: str, use_emoji: bool = False) -> Optional[List[str]]:
    """Search for scope match and return formatted lines with full hierarchy."""
    for epic in epics:
```

[X] ERROR (line 44)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

def search_sub_epics(sub_epics: List[Dict], scope_val: str, use_emoji: bool = False) -> Optional[List[str]]:
    """Search sub-epics for scope match."""
    for sub_epic in sub_epics:
```

[X] ERROR (line 57)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

def search_stories(sub_epic: Dict, scope_val: str, use_emoji: bool = False) -> Optional[List[str]]:
    """Search stories for scope match."""
    for story_group in sub_epic.get('story_groups', []):
```

[X] ERROR (line 71)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

def matches_name(name: str, pattern: str) -> bool:
    """Check if pattern matches name (case-insensitive)."""
    return pattern.lower() in name.lower()
```

[X] ERROR (line 76)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

def format_node_with_children(node: Dict[str, Any], node_type: str, indent: int, use_emoji: bool = False) -> List[str]:
    """Format a node and its children recursively.
    
    Args:
        node: Node dictionary with name and children
        node_type: Type of node ('epic', 'sub epic', 'story')
        indent: Indentation level
        use_emoji: If True, use emoji formatting; if False, use bracket formatting
        
    Returns:
        List of formatted lines
    """
    lines = []
```

---

## stop_writing_useless_comments
**scoping_parameter.py** - 7 violation(s)

[X] ERROR (line 204)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _filter_increment_epic_by_story_names(self, epic: Dict[str, Any], story_name_set: Set[str]) -> Optional[Dict[str, Any]]:
        """Filter increment epic by story names.
        
        Only supports sub_epics format: epics[].sub_epics[].stories[]
        """
        # Handle sub_epics format
```

[X] ERROR (line 217)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _filter_increment_sub_epics_by_story_names(self, sub_epics: List[Dict[str, Any]], story_name_set: Set[str]) -> List[Dict[str, Any]]:
        """Filter sub_epics in increment by story names.
        
        Handles both direct stories and story_groups formats.
        """
        filtered = []
```

[X] ERROR (line 229)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _filter_increment_sub_epic_by_story_names(self, sub_epic: Dict[str, Any], story_name_set: Set[str]) -> Optional[Dict[str, Any]]:
        """Filter a single sub_epic in increment by story names.
        
        Handles both direct stories array and story_groups format.
        """
        # Filter direct stories array
```

[X] ERROR (line 284)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _extract_story_names_from_increment(self, increment: Dict[str, Any]) -> Set[str]:
        """Extract story names from increment.
        
        Increments can have:
        1. Direct stories array: increment.stories[]
        2. Epics with sub_epics: increment.epics[].sub_epics[].stories[] or story_groups[].stories[]
        """
        story_names = set()
```

[X] ERROR (line 298)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _add_direct_stories(self, increment: Dict[str, Any], story_names: Set[str]) -> None:
        """Add story names from increment's direct stories array."""
        for story in increment.get('stories', []):
```

[X] ERROR (line 303)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _add_epic_stories(self, increment: Dict[str, Any], story_names: Set[str]) -> None:
        """Extract story names from increment epics.
        
        Only supports sub_epics format: epics[].sub_epics[].stories[] or story_groups[].stories[]
        Does NOT support features format.
        """
        for epic in increment.get('epics', []):
```

[X] ERROR (line 208)
Useless comment: "# Handle sub_epics format" - delete it or improve the code instead

```python
        Only supports sub_epics format: epics[].sub_epics[].stories[]
        """
        # Handle sub_epics format
        epic['sub_epics'] = self._filter_increment_sub_epics_by_story_names(
```

---

## stop_writing_useless_comments
**tty_scope.py** - 5 violation(s)

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYScope(TTYAdapter):
    """Serializes Scope to TTY - delegates to result adapters (StoryGraph or file list)."""
    
```

[X] ERROR (line 14)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __init__(self, scope: Scope):
        """Initialize TTYScope.
        
        Args:
            scope: Scope domain object (already has workspace_directory)
        """
        self.scope = scope
```

[X] ERROR (line 22)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Scope to TTY string - delegates to result domain adapters."""
        lines = []
```

[X] ERROR (line 71)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

[X] ERROR (line 36)
Useless comment: "# Get results from Scope and delegate to appropriate adapter" - delete it or improve the code instead

```python
        lines.append("")
        
        # Get results from Scope and delegate to appropriate adapter
        results = self.scope.results
```

---

## stop_writing_useless_comments
**tty_scope_command_result.py** - 3 violation(s)

[X] ERROR (line 10)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYScopeCommandResult(TTYAdapter):
    """Serializes ScopeCommandResult to TTY format."""
    
```

[X] ERROR (line 16)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert ScopeCommandResult to TTY string."""
        from agile_bot.src.scope.tty_scope import TTYScope
```

[X] ERROR (line 38)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text into verb and params."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**json_story_graph.py** - 3 violation(s)

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class JSONStoryGraph(JSONAdapter):
    """Serializes StoryGraph to JSON - exposes all StoryGraph properties."""
    
```

[X] ERROR (line 42)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_dict(self) -> dict:
        """Convert StoryGraph to dict."""
        return {
```

[X] ERROR (line 53)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def deserialize(self, data: str) -> dict:
        """Parse JSON string to dict."""
        return json.loads(data)
```

---

## stop_writing_useless_comments
**markdown_story_graph.py** - 4 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class MarkdownStoryGraph(MarkdownAdapter):
    """Serializes StoryGraph to Markdown."""
    
```

[X] ERROR (line 15)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert StoryGraph to Markdown string."""
        lines = []
```

[X] ERROR (line 55)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _render_sub_epic(self, sub_epic: dict, lines: list, indent_level: int):
        """Recursively render a sub-epic and its nested sub-epics and stories.
        
        Args:
            sub_epic: Sub-epic dictionary from story graph
            lines: List to append output lines to
            indent_level: Current indentation level (0 = epic, 1 = first sub-epic, etc.)
        """
        sub_epic_name = sub_epic.get('name', 'Unknown')
```

[X] ERROR (line 85)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**tty_story_graph.py** - 4 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYStoryGraph(TTYAdapter):
    """Serializes StoryGraph to TTY - exposes all StoryGraph properties."""
    
```

[X] ERROR (line 40)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert StoryGraph to TTY string."""
        lines = []
```

[X] ERROR (line 73)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _render_sub_epic(self, sub_epic: dict, lines: list, indent_level: int):
        """Recursively render a sub-epic and its nested sub-epics and stories.
        
        Args:
            sub_epic: Sub-epic dictionary from story graph
            lines: List to append output lines to
            indent_level: Current indentation level (0 = epic, 1 = first sub-epic, etc.)
        """
        sub_epic_name = sub_epic.get('name', 'Unknown')
```

[X] ERROR (line 103)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**build_action.py** - 9 violation(s)

[X] ERROR (line 46)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _prepare_instructions(self, instructions, context: ScopeActionContext):
        """Prepare build instructions with story graph data, rules, and scope."""
        # Add story graph data instructions
```

[X] ERROR (line 116)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _replace_schema_placeholders(self, instructions) -> None:
        """Replace {{schema}} and {{description}} placeholders in base_instructions with template references."""
        base_instructions = instructions.get('base_instructions', [])
```

[X] ERROR (line 246)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _replace_content_with_file_references(self, instructions) -> None:
        """Replace full content (templates, configs, rules) with file path references."""
        bot_dir = self.behavior.bot_paths.bot_directory
```

[X] ERROR (line 50)
Useless comment: "# Handle scope" - delete it or improve the code instead

```python
        instructions.update(self.story_graph_data.instructions)
        
        # Handle scope
        action_scope = ActionScope.from_context(context, self.behavior.bot_paths)
```

[X] ERROR (line 127)
Useless comment: "# Create relative path reference: bot_name/behaviors/behavio" - delete it or improve the code instead

```python
            template_path = template.template_path
            if template_path:
                # Create relative path reference: bot_name/behaviors/behavior_name/content/story_graph/template_filename
                bot_dir = self.behavior.bot_paths.bot_directory
```

[X] ERROR (line 160)
Useless comment: "# Get output filename and path" - delete it or improve the code instead

```python
                            schema_explanation_lines.append(f"{key}: {str(value)}")
            
            # Get output filename and path
            output_filename = self.story_graph_spec.output_filename if self.story_graph_spec else 'story-graph.json'
```

[X] ERROR (line 164)
Useless comment: "# Create description text for template file and output instr" - delete it or improve the code instead

```python
            output_path = str(self.story_graph_spec.story_graph.path.parent) if self.story_graph_spec else ''
            
            # Create description text for template file and output instructions
            description_lines_list = [
```

[X] ERROR (line 209)
Useless comment: "# Get schema path for placeholder replacement" - delete it or improve the code instead

```python
        rules_section = []
        
        # Get schema path for placeholder replacement
        schema_path = self.behavior.bot_paths.workspace_directory / 'docs' / 'stories' / 'story-graph.json'
```

[X] ERROR (line 265)
Useless comment: "# Get the bots directory using python_workspace_root" - delete it or improve the code instead

```python
            all_rules = instructions._data['rules']
            rule_files = []
            # Get the bots directory using python_workspace_root
            bots_dir = self.behavior.bot_paths.python_workspace_root / 'agile_bot' / 'bots'
```

---

## stop_writing_useless_comments
**json_build_action.py** - 6 violation(s)

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class JSONBuildAction(JSONAdapter):
    """Serializes BuildStoryGraphAction to JSON - exposes all BuildStoryGraphAction properties."""
    
```

[X] ERROR (line 53)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def story_graph_data(self):
        """Build-specific property."""
        return self.action.story_graph_data
```

[X] ERROR (line 58)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def story_graph_spec(self):
        """Build-specific property."""
        return self.action.story_graph_spec
```

[X] ERROR (line 63)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def story_graph_template(self):
        """Build-specific property."""
        return self.action.story_graph_template
```

[X] ERROR (line 67)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_dict(self) -> dict:
        """Convert BuildStoryGraphAction to dict."""
        result = {
```

[X] ERROR (line 100)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def deserialize(self, data: str) -> dict:
        """Parse JSON string to dict."""
        return json.loads(data)
```

---

## stop_writing_useless_comments
**markdown_build_action.py** - 3 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class MarkdownBuildAction(MarkdownAction):
    """Serializes BuildStoryGraphAction to Markdown - uses base class for status display."""
    
```

[X] ERROR (line 15)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert BuildStoryGraphAction to Markdown string - uses base class for status display."""
        return super().serialize()
```

[X] ERROR (line 20)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**story_graph_data.py** - 1 violation(s)

[X] ERROR (line 19)
Useless comment: "# Return only file path references, not full content" - delete it or improve the code instead

```python
    @property
    def instructions(self) -> Dict[str, Any]:
        # Return only file path references, not full content
        config_path = str(self.story_graph_spec.config_path) if self.story_graph_spec.config_path else None
```

---

## stop_writing_useless_comments
**tty_build_action.py** - 6 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYBuildAction(TTYAction):
    """Serializes BuildStoryGraphAction to TTY - exposes all BuildStoryGraphAction properties."""
    
```

[X] ERROR (line 45)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def story_graph_data(self):
        """Build-specific property."""
        return self.action.story_graph_data
```

[X] ERROR (line 50)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def story_graph_spec(self):
        """Build-specific property."""
        return self.action.story_graph_spec
```

[X] ERROR (line 55)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def story_graph_template(self):
        """Build-specific property."""
        return self.action.story_graph_template
```

[X] ERROR (line 59)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert BuildStoryGraphAction to TTY string - uses base class for status display."""
        return super().serialize()
```

[X] ERROR (line 64)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**clarify_action.py** - 2 violation(s)

[X] ERROR (line 36)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _prepare_instructions(self, instructions, context: ClarifyActionContext):
        """Load required questions, evidence, and saved clarification data into instructions.
        
        Note: Strategy data (criteria templates + saved decisions) is loaded by the base class
        via _load_behavior_guardrails() -> _load_all_saved_guardrails(), so no need to load here.
        """
        instructions.set('guardrails', {'required_context': self.required_context.instructions})
```

[X] ERROR (line 58)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def do_execute(self, context: ClarifyActionContext = None):
        """Execute clarify action - get instructions and save if answers provided."""
        if context is None:
```

---

## stop_writing_useless_comments
**json_clarify_action.py** - 6 violation(s)

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class JSONClarifyAction(JSONAdapter):
    """Serializes ClarifyContextAction to JSON - exposes all ClarifyContextAction properties."""
    
```

[X] ERROR (line 53)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def required_context(self):
        """Clarify-specific property."""
        return self.action.required_context
```

[X] ERROR (line 58)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def key_questions(self):
        """Clarify-specific property."""
        return self.action.key_questions
```

[X] ERROR (line 63)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def evidence(self):
        """Clarify-specific property."""
        return self.action.evidence
```

[X] ERROR (line 67)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_dict(self) -> dict:
        """Convert ClarifyContextAction to dict."""
        result = {
```

[X] ERROR (line 97)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def deserialize(self, data: str) -> dict:
        """Parse JSON string to dict."""
        return json.loads(data)
```

---

## stop_writing_useless_comments
**markdown_clarify_action.py** - 3 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class MarkdownClarifyAction(MarkdownAction):
    """Serializes ClarifyContextAction to Markdown - uses base class for status display."""
    
```

[X] ERROR (line 15)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert ClarifyContextAction to Markdown string - uses base class for status display."""
        return super().serialize()
```

[X] ERROR (line 20)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**requirements_clarifications.py** - 3 violation(s)

[X] ERROR (line 18)
Useless comment: "# Get existing data for this behavior, or create new structu" - delete it or improve the code instead

```python
    def save(self):
        existing_data = self.load()
        # Get existing data for this behavior, or create new structure
        behavior_data = existing_data.get(self.behavior_name, {})
```

[X] ERROR (line 27)
Useless comment: "# Get required evidence from guardrails" - delete it or improve the code instead

```python
        merged_answers = {**existing_answers, **self.key_questions_answered}
        
        # Get required evidence from guardrails
        required_evidence = self.required_context.evidence.evidence_list if self.required_context else []
```

[X] ERROR (line 42)
Useless comment: "# Handle legacy string context - convert to list" - delete it or improve the code instead

```python
                final_context.extend(self.context)
            else:
                # Handle legacy string context - convert to list
                final_context = final_context if isinstance(final_context, list) else []
```

---

## stop_writing_useless_comments
**tty_clarify_action.py** - 6 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYClarifyAction(TTYAction):
    """Serializes ClarifyContextAction to TTY - exposes all ClarifyContextAction properties."""
    
```

[X] ERROR (line 45)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def required_context(self):
        """Clarify-specific property."""
        return self.action.required_context
```

[X] ERROR (line 50)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def key_questions(self):
        """Clarify-specific property."""
        return self.action.key_questions
```

[X] ERROR (line 55)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def evidence(self):
        """Clarify-specific property."""
        return self.action.evidence
```

[X] ERROR (line 59)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert ClarifyContextAction to TTY string - uses base class for status display."""
        return super().serialize()
```

[X] ERROR (line 64)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**tty_guardrails.py** - 3 violation(s)

[X] ERROR (line 8)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYGuardrails(TTYAdapter):
    """Serializes Guardrails to TTY - delegates to RequiredContext and Strategy adapters."""
    
```

[X] ERROR (line 14)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Guardrails to TTY string - delegates to sub-adapters."""
        from agile_bot.src.cli.adapter_factory import AdapterFactory
```

[X] ERROR (line 29)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text (not used for Guardrails)."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**tty_required_context.py** - 3 violation(s)

[X] ERROR (line 8)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYRequiredContext(TTYAdapter):
    """Serializes RequiredContext to TTY - formats key questions and evidence."""
    
```

[X] ERROR (line 14)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert RequiredContext to TTY string."""
        lines = []
```

[X] ERROR (line 44)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text (not used for RequiredContext)."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**tty_strategy.py** - 4 violation(s)

[X] ERROR (line 8)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYStrategy(TTYAdapter):
    """Serializes Strategy to TTY - formats decision criteria and assumptions."""
    
```

[X] ERROR (line 14)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert Strategy to TTY string."""
        lines = []
```

[X] ERROR (line 46)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _format_option(self, option) -> list:
        """Format a single decision criteria option for display."""
        lines = []
```

[X] ERROR (line 62)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text (not used for Strategy)."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**json_render_action.py** - 6 violation(s)

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class JSONRenderAction(JSONAdapter):
    """Serializes RenderOutputAction to JSON - exposes all RenderOutputAction properties."""
    
```

[X] ERROR (line 53)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def render_specs(self):
        """Render-specific property."""
        return self.action.render_specs
```

[X] ERROR (line 58)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def templates(self):
        """Render-specific property."""
        return self.action.templates
```

[X] ERROR (line 63)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def synchronizers(self):
        """Render-specific property."""
        return self.action.synchronizers
```

[X] ERROR (line 67)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_dict(self) -> dict:
        """Convert RenderOutputAction to dict."""
        result = {
```

[X] ERROR (line 100)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def deserialize(self, data: str) -> dict:
        """Parse JSON string to dict."""
        return json.loads(data)
```

---

## stop_writing_useless_comments
**markdown_render_action.py** - 3 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class MarkdownRenderAction(MarkdownAction):
    """Serializes RenderOutputAction to Markdown - uses base class for status display."""
    
```

[X] ERROR (line 15)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert RenderOutputAction to Markdown string - uses base class for status display."""
        return super().serialize()
```

[X] ERROR (line 20)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**render_action.py** - 7 violation(s)

[X] ERROR (line 32)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _execute_synchronizers(self, render_specs: List['RenderSpec']) -> None:
        """Execute synchronizers for all render specs."""
        for spec in render_specs:
```

[X] ERROR (line 44)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _prepare_instructions(self, instructions, context: ScopeActionContext):
        """Prepare render instructions with render specs and templates."""
        render_instructions = self._config_loader.load_render_instructions()
```

[X] ERROR (line 48)
Useless comment: "# Execute synchronizers during preparation" - delete it or improve the code instead

```python
        render_specs = self._render_specs
        
        # Execute synchronizers during preparation
        self._execute_synchronizers(render_specs)
```

[X] ERROR (line 62)
Useless comment: "# Update instructions with formatted data" - delete it or improve the code instead

```python
        template_specs = [spec for spec in render_specs if spec.requires_ai_handling and (not spec.is_executed)]
        
        # Update instructions with formatted data
        instructions._data['base_instructions'] = merged_data.get('base_instructions', [])
```

[X] ERROR (line 96)
Useless comment: "# Get the path prefix" - delete it or improve the code instead

```python
            # Add output file path (drawio, md, txt, etc.)
            if spec.output:
                # Get the path prefix
                path_prefix = spec.config_data.get('path', 'docs/stories')
```

[X] ERROR (line 117)
Useless comment: "# Get render instruction data and inject it" - delete it or improve the code instead

```python
        instructions = self.get_instructions(context)
        
        # Get render instruction data and inject it
        merged_data = {
```

[X] ERROR (line 124)
Useless comment: "# Update instructions object with merged data" - delete it or improve the code instead

```python
        self._instruction_formatter.inject_render_data(merged_data, render_instructions, render_specs)
        
        # Update instructions object with merged data
        instructions._data['base_instructions'] = merged_data.get('base_instructions', [])
```

---

## stop_writing_useless_comments
**render_instruction_builder.py** - 5 violation(s)

[X] ERROR (line 150)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _process_for_each_loops(self, instructions_list: List[str], render_specs: List['RenderSpec']) -> List[str]:
        """Process {{#for_each_render_config}}...{{/for_each_render_config}} loops."""
        new_instructions = []
```

[X] ERROR (line 188)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _expand_template_for_spec(self, template_lines: List[str], spec: 'RenderSpec') -> List[str]:
        """Expand template lines with render_config placeholders replaced."""
        # Handle instructions - can be string or list
```

[X] ERROR (line 19)
Useless comment: "# Process action_config.json placeholders with ALL render_sp" - delete it or improve the code instead

```python
        
        self._add_spec_instructions(base_instructions_list, executed_specs, template_specs)
        # Process action_config.json placeholders with ALL render_specs (for {{#for_each_render_config}} loops)
        self.inject_render_template_variables(base_instructions_list, render_instructions, template_specs, all_render_specs=render_specs)
```

[X] ERROR (line 124)
Useless comment: "# Create single instruction line" - delete it or improve the code instead

```python
            template_path = spec.config_data.get('template', 'N/A')
        
        # Create single instruction line
        formatted_parts.append(f'{index}. {config_name} > manually generate {output_path} by taking {input_path} and transform using {template_path}')
```

[X] ERROR (line 189)
Useless comment: "# Handle instructions - can be string or list" - delete it or improve the code instead

```python
    def _expand_template_for_spec(self, template_lines: List[str], spec: 'RenderSpec') -> List[str]:
        """Expand template lines with render_config placeholders replaced."""
        # Handle instructions - can be string or list
        instructions = spec.config_data.get('instructions', 'No instructions provided')
```

---

## stop_writing_useless_comments
**tty_render_action.py** - 6 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYRenderAction(TTYAction):
    """Serializes RenderOutputAction to TTY - exposes all RenderOutputAction properties."""
    
```

[X] ERROR (line 45)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def render_specs(self):
        """Render-specific property."""
        return self.action.render_specs
```

[X] ERROR (line 50)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def templates(self):
        """Render-specific property."""
        return self.action.templates
```

[X] ERROR (line 55)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def synchronizers(self):
        """Render-specific property."""
        return self.action.synchronizers
```

[X] ERROR (line 59)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert RenderOutputAction to TTY string - uses base class for status display."""
        return super().serialize()
```

[X] ERROR (line 64)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**assumptions.py** - 2 violation(s)

[X] ERROR (line 12)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _load_assumptions(self):
        """Lazy load assumptions from file."""
        if self._assumptions is None:
```

[X] ERROR (line 20)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def assumptions(self) -> List[str]:
        """Get assumptions, loading from file if needed."""
        self._load_assumptions()
```

---

## stop_writing_useless_comments
**json_strategy_action.py** - 7 violation(s)

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class JSONStrategyAction(JSONAdapter):
    """Serializes StrategyAction to JSON - exposes all StrategyAction properties."""
    
```

[X] ERROR (line 53)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def strategy(self):
        """Strategy-specific property."""
        return self.action.strategy
```

[X] ERROR (line 58)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def strategy_criteria(self):
        """Strategy-specific property."""
        return self.action.strategy_criteria
```

[X] ERROR (line 63)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def typical_assumptions(self):
        """Strategy-specific property."""
        return self.action.typical_assumptions
```

[X] ERROR (line 67)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_dict(self) -> dict:
        """Convert StrategyAction to dict."""
        # #region agent log
```

[X] ERROR (line 174)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def deserialize(self, data: str) -> dict:
        """Parse JSON string to dict."""
        return json.loads(data)
```

[X] ERROR (line 87)
Useless comment: "# Get saved decisions from strategy.json" - delete it or improve the code instead

```python
        # Add strategy-specific properties
        if self.action.strategy:
            # Get saved decisions from strategy.json
            from agile_bot.src.actions.strategy.strategy_decision import StrategyDecision
```

---

## stop_writing_useless_comments
**markdown_strategy_action.py** - 3 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class MarkdownStrategyAction(MarkdownAction):
    """Serializes StrategyAction to Markdown - uses base class for status display."""
    
```

[X] ERROR (line 15)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert StrategyAction to Markdown string - uses base class for status display."""
        return super().serialize()
```

[X] ERROR (line 20)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**strategy.py** - 1 violation(s)

[X] ERROR (line 16)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def instructions(self) -> Dict[str, Any]:
        """Get strategy data (criteria and assumptions).
        
        Note: Workflow instructions are now in base_actions/strategy/action_config.json.
        This method returns only the behavior-specific data (criteria and assumptions).
        """
        strategy_criteria_dict = {}
```

---

## stop_writing_useless_comments
**strategy_action.py** - 6 violation(s)

[X] ERROR (line 36)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _prepare_instructions(self, instructions, context: StrategyActionContext):
        """Add strategy data (criteria, assumptions) and saved decisions to instructions.
        
        Note: Workflow instructions come from base_actions/strategy/action_config.json.
        This method adds only the behavior-specific data.
        """
        strategy_data = self.strategy.instructions
```

[X] ERROR (line 104)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _format_instructions_for_display(self, instructions) -> str:
        """Format strategy data for REPL display."""
        # Get base formatting first (includes scope warning if set)
```

[X] ERROR (line 169)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _format_option(self, option) -> list:
        """Format a single decision criteria option for display."""
        lines = []
```

[X] ERROR (line 191)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def do_execute(self, context: StrategyActionContext = None):
        """Execute strategy action - get instructions and save if decisions provided."""
        if context is None:
```

[X] ERROR (line 52)
Useless comment: "# Get criteria template" - delete it or improve the code instead

```python
        
        if strategy_data:
            # Get criteria template
            criteria_template = strategy_data.get('strategy_criteria', {})
```

[X] ERROR (line 108)
Useless comment: "# Get the instruction data" - delete it or improve the code instead

```python
        output_lines = super()._format_instructions_for_display(instructions).split('\n')
        
        # Get the instruction data
        instructions_dict = instructions.to_dict()
```

---

## stop_writing_useless_comments
**strategy_criteria.py** - 3 violation(s)

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _format_options(self, options: List[Any]) -> List[Any]:
        """Format options, converting example arrays to formatted strings."""
        formatted_options = []
```

[X] ERROR (line 25)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _format_example(self, example_lines: List[str]) -> str:
        """Convert example array to properly formatted string."""
        return '\n'.join(example_lines)
```

[X] ERROR (line 53)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def to_dict(self) -> Dict[str, Any]:
        """Convert StrategyCriteria to a dictionary for JSON serialization."""
        return {
```

---

## stop_writing_useless_comments
**strategy_criterias.py** - 2 violation(s)

[X] ERROR (line 13)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _load_strategy_criterias(self):
        """Lazy load strategy criterias from files."""
        if self._strategy_criterias is None:
```

[X] ERROR (line 29)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def strategy_criterias(self) -> Dict[str, StrategyCriteria]:
        """Get strategy criterias, loading from files if needed."""
        self._load_strategy_criterias()
```

---

## stop_writing_useless_comments
**tty_strategy_action.py** - 6 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYStrategyAction(TTYAction):
    """Serializes StrategyAction to TTY - exposes all StrategyAction properties."""
    
```

[X] ERROR (line 45)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def strategy(self):
        """Strategy-specific property."""
        return self.action.strategy
```

[X] ERROR (line 50)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def strategy_criteria(self):
        """Strategy-specific property."""
        return self.action.strategy_criteria
```

[X] ERROR (line 55)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def typical_assumptions(self):
        """Strategy-specific property."""
        return self.action.typical_assumptions
```

[X] ERROR (line 59)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert StrategyAction to TTY string - uses base class for status display."""
        return super().serialize()
```

[X] ERROR (line 64)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**json_validate_action.py** - 4 violation(s)

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class JSONValidateAction(JSONAdapter):
    """Serializes ValidateRulesAction to JSON - exposes all ValidateRulesAction properties."""
    
```

[X] ERROR (line 53)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def rules(self):
        """Validate-specific property."""
        return self.action.rules
```

[X] ERROR (line 57)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_dict(self) -> dict:
        """Convert ValidateRulesAction to dict."""
        result = {
```

[X] ERROR (line 89)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def deserialize(self, data: str) -> dict:
        """Parse JSON string to dict."""
        return json.loads(data)
```

---

## stop_writing_useless_comments
**markdown_validate_action.py** - 3 violation(s)

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class MarkdownValidateAction(MarkdownAction):
    """Serializes ValidateRulesAction to Markdown - uses base class for status display."""
    
```

[X] ERROR (line 15)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert ValidateRulesAction to Markdown string - uses base class for status display."""
        return super().serialize()
```

[X] ERROR (line 20)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

---

## stop_writing_useless_comments
**tty_validate_action.py** - 5 violation(s)

[X] ERROR (line 10)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class TTYValidateAction(TTYAction):
    """Serializes ValidateRulesAction to TTY - exposes all ValidateRulesAction properties."""
    
```

[X] ERROR (line 46)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def rules(self):
        """Validate-specific property."""
        return self.action.rules
```

[X] ERROR (line 50)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Convert ValidateRulesAction to TTY string - uses base class for status display."""
        return super().serialize()
```

[X] ERROR (line 55)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
```

[X] ERROR (line 63)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @staticmethod
    def format_instructions_from_dict(instructions_dict: dict, bot_paths=None, scope=None) -> str:
        """Format instructions dict (from execute results) as text.
        
        This handles the case where validate.execute() returns {'instructions': {...}}
        and converts it to formatted text, consistent with how other actions format instructions.
        """
        # Convert dict to Instructions object
```

---

## stop_writing_useless_comments
**validate_action.py** - 9 violation(s)

[X] ERROR (line 33)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _prepare_instructions(self, instructions, context: ValidateActionContext):
        """Prepare validation instructions with rules and validation data."""
        # Get rules with file paths for AI to read
```

[X] ERROR (line 105)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _run_scanners_and_format_results(self, context: ValidateActionContext) -> str:
        """Run validation scanners and format results for display in instructions."""
        logger.info('Running scanners for instructions display...')
```

[X] ERROR (line 148)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _format_scope_description(self, context: ValidateActionContext) -> str:
        """Format scope description for validation instructions."""
        if context.scope:
```

[X] ERROR (line 165)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _format_rules_with_file_paths(self) -> str:
        """Format rules with file paths for AI to read and analyze."""
        rules_data = self.inject_behavior_specific_rules()
```

[X] ERROR (line 34)
Useless comment: "# Get rules with file paths for AI to read" - delete it or improve the code instead

```python
    def _prepare_instructions(self, instructions, context: ValidateActionContext):
        """Prepare validation instructions with rules and validation data."""
        # Get rules with file paths for AI to read
        rules_text = self._format_rules_with_file_paths()
```

[X] ERROR (line 37)
Useless comment: "# Get story graph schema path" - delete it or improve the code instead

```python
        rules_text = self._format_rules_with_file_paths()
        
        # Get story graph schema path
        schema_path = self.behavior.bot_paths.workspace_directory / 'docs' / 'stories' / 'story-graph.json'
```

[X] ERROR (line 40)
Useless comment: "# Get scope description" - delete it or improve the code instead

```python
        schema_path = self.behavior.bot_paths.workspace_directory / 'docs' / 'stories' / 'story-graph.json'
        
        # Get scope description
        scope_text = self._format_scope_description(context)
```

[X] ERROR (line 109)
Useless comment: "# Execute validation synchronously" - delete it or improve the code instead

```python
        
        try:
            # Execute validation synchronously
            result = self._executor.execute_synchronous(context)
```

[X] ERROR (line 112)
Useless comment: "# Get the report path from the result" - delete it or improve the code instead

```python
            result = self._executor.execute_synchronous(context)
            
            # Get the report path from the result
            instructions_dict = result.get('instructions', {})
```

---

## stop_writing_useless_comments
**validation_report_writer.py** - 1 violation(s)

[X] ERROR (line 20)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

def ensure_reports_directory(bot_paths: BotPath, workspace_directory: Path) -> Path:
    """Module-level helper to create and return the reports directory."""
    docs_path = bot_paths.documentation_path
```

---

## stop_writing_useless_comments
**validation_type.py** - 1 violation(s)

[X] ERROR (line 5)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class ValidationType(Enum):
    """Type of content a behavior validates by default."""
    STORY_GRAPH = 'story_graph'
```

---

## stop_writing_useless_comments
**validation_violations_builder.py** - 3 violation(s)

[X] ERROR (line 6)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class _MarkdownHelper:
    """Minimal markdown formatting helper for validation output."""
    
```

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def format_heading(self, text: str, level: int = 1) -> str:
        """Format markdown heading."""
        return f"{'#' * level} {text}"
```

[X] ERROR (line 13)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def format_bold(self, text: str) -> str:
        """Format bold text."""
        return f"**{text}**"
```

---

## stop_writing_useless_comments
**cursor_command_visitor.py** - 9 violation(s)

[X] ERROR (line 17)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class CursorCommandGenerator(BaseBehaviorsAdapter):
    """Generator that creates Cursor command files using the new CLI entry point."""
    
```

[X] ERROR (line 59)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _build_wrapped_hierarchy(self):
        """Override to create CursorBehaviorWrapper instead of generic adapters."""
        current_behavior_name = (
```

[X] ERROR (line 100)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _build_status_command(self) -> str:
        """Build a dedicated status command for quick access."""
        bot_dir_str = str(self.bot_directory).replace('\\', '\\')
```

[X] ERROR (line 203)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Generate Cursor commands by walking wrapped hierarchy."""
        self.commands_dir = self._ensure_commands_directory()
```

[X] ERROR (line 214)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def generate(self) -> Dict[str, Path]:
        """Generate command files and return commands dict."""
        self.serialize()
```

[X] ERROR (line 256)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class CursorBehaviorWrapper(BaseBehaviorAdapter):
    """Wrapper for generating behavior command files."""
    
```

[X] ERROR (line 267)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def format_behavior_name(self) -> str:
        """Not used for file generation."""
        return ""
```

[X] ERROR (line 271)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def serialize(self) -> str:
        """Not used - generate_command_file writes files directly."""
        return ""
```

[X] ERROR (line 275)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def generate_command_file(self, commands_dir: Path, commands: Dict[str, Path]):
        """Generate command file for this behavior."""
        behavior_command = self.generator_ref._build_behavior_command(self.behavior.name)
```

---

## use_clear_function_parameters
**rule.py** - 3 violation(s)

[!] WARNING (line 117)
Function "scan" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return issubclass(self._scanner, TestScanner) or issubclass(self._scanner, CodeScanner)

    def scan(self, story_graph: Dict[str, Any], files: Optional[Dict[str, List[Path]]]=None, on_file_scanned: Optional[Any]=None, skip_cross_file: bool=False, changed_files: Optional[Dict[str, List[Path]]]=None, status_writer: Optional[Any]=None, max_cross_file_comparisons: int=20) -> Dict[str, Any]:
        if not self.has_scanner:
            return {}
    # ... (truncated)
```

[!] WARNING (line 153)
Function "_execute_file_by_file_scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return scanner_instance

    def _execute_file_by_file_scan(self, scanner_instance, story_graph, test_files, code_files, on_file_scanned):
        violations_file_by_file = scanner_instance.scan(story_graph, rule_obj=self, test_files=test_files, code_files=code_files, on_file_scanned=on_file_scanned)
        if violations_file_by_file is not None:
    # ... (truncated)
```

[!] WARNING (line 165)
Function "_execute_cross_file_scan" has 9 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
            self._file_by_file_violations = []

    def _execute_cross_file_scan(self, scanner_instance, skip_cross_file, test_files, code_files, all_test_files, all_code_files, status_writer=None, max_cross_file_comparisons=20):
        if not skip_cross_file and self.requires_two_pass_scan and hasattr(scanner_instance, 'scan_cross_file'):
            violations_cross_file = scanner_instance.scan_cross_file(rule_obj=self, test_files=test_files, code_files=code_files, all_test_files=all_test_files, all_code_files=all_code_files, status_writer=status_writer, max_cross_file_comparisons=max_cross_file_comparisons)
    # ... (truncated)
```

---

## use_clear_function_parameters
**rules.py** - 5 violation(s)

[!] WARNING (line 389)
Function "_process_scanner_result" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
            return data

    def _process_scanner_result(self, rule, rule_result: dict, scanner_results: Any, scanner_path: str, scanner_name: str, logger) -> str:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        execution_status = rule.scanner_execution_status or 'SUCCESS'
    # ... (truncated)
```

[!] WARNING (line 405)
Function "_execute_scanner" has 9 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return f'  [OK] {rule.rule_file}: Scanner executed successfully ({violations_count} violations)'

    def _execute_scanner(self, rule, rule_result: dict, context: ValidationContext, scanner_path: str, logger, files: Dict, changed_files: Dict, all_files: Dict) -> str:
        scanner_name = scanner_path.split('.')[-1] if '.' in scanner_path else scanner_path
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # ... (truncated)
```

[!] WARNING (line 426)
Function "_process_rule" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
            raise

    def _process_rule(self, rule, rule_result: dict, context: ValidationContext, logger, files: Dict, changed_files: Dict, all_files: Dict) -> str:
        scanner_path = rule.scanner_path
        if not scanner_path:
    # ... (truncated)
```

[!] WARNING (line 438)
Function "validate" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return self._execute_scanner(rule, rule_result, context, scanner_path, logger, files, changed_files, all_files)

    def validate(self, context: ValidationContext, files: Optional[Dict[str, List[Path]]]=None, callbacks: Optional[ValidationCallbacks]=None, skiprule: Optional[List[str]]=None, exclude: Optional[List[str]]=None) -> List[Dict[str, Any]]:
        if isinstance(context, ValidationContext):
            return self._execute_validation(context)
    # ... (truncated)
```

[!] WARNING (line 443)
Function "_create_legacy_context" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return self._execute_validation(self._create_legacy_context(context, files, callbacks, skiprule, exclude))

    def _create_legacy_context(self, story_graph: Dict, files: Optional[Dict], callbacks: Optional[ValidationCallbacks], skiprule: Optional[List[str]], exclude: Optional[List[str]]) -> ValidationContext:
        return ValidationContext(story_graph=story_graph, files=files or {}, callbacks=callbacks or ValidationCallbacks(), skiprule=skiprule or [], exclude=exclude or [], skip_cross_file=True, all_files=False, behavior=self.behavior, bot_paths=getattr(self, 'bot_paths', None), working_dir=Path.cwd())

```

---

## use_clear_function_parameters
**active_language_scanner.py** - 1 violation(s)

[!] WARNING (line 184)
Function "_create_capability_noun_violation" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return None
    
    def _create_capability_noun_violation(self, name: str, node: StoryNode, node_type: str, rule_obj: Any, noun_type: str) -> Dict[str, Any]:
        location = node.map_location()
        message = f'{node_type.capitalize()} name "{name}" uses capability noun'
    # ... (truncated)
```

---

## use_clear_function_parameters
**business_readable_test_names_scanner.py** - 4 violation(s)

[!] WARNING (line 33)
Function "_check_test_function_node" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return violations
    
    def _check_test_function_node(self, node: Any, file_path: Path, rule_obj: Any, domain_language: set, violations: list) -> None:
        if not isinstance(node, ast.FunctionDef):
            return
    # ... (truncated)
```

[!] WARNING (line 114)
Function "_check_business_readable" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return set(words)
    
    def _check_business_readable(self, test_name: str, file_path: Path, node: ast.FunctionDef, rule_obj: Any, domain_language: set) -> Optional[Dict[str, Any]]:
        name_without_prefix = test_name[5:] if test_name.startswith('test_') else test_name
        
    # ... (truncated)
```

[!] WARNING (line 261)
Function "_extract_code_snippet" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return True
    
    def _extract_code_snippet(self, content: str, ast_node: Optional[ast.AST] = None, 
                             start_line: Optional[int] = None, end_line: Optional[int] = None,
                             context_before: int = 2, max_lines: int = 50) -> str:
    # ... (truncated)
```

[!] WARNING (line 301)
Function "_create_violation_with_snippet" has 12 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return code_snippet
    
    def _create_violation_with_snippet(
        self, 
        rule_obj: Any,
    # ... (truncated)
```

---

## use_clear_function_parameters
**class_based_organization_scanner.py** - 2 violation(s)

[!] WARNING (line 105)
Function "_check_method_name_matches_scenario" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return None
    
    def _check_method_name_matches_scenario(self, method_name: str, class_name: str, story_names: List[str], 
                                           story_graph: Dict[str, Any], file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        scenario_name_from_method = method_name[5:] if method_name.startswith('test_') else method_name
    # ... (truncated)
```

[!] WARNING (line 334)
Function "_check_file_name_matches_sub_epic" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return name.lower()
    
    def _check_file_name_matches_sub_epic(self, file_name: str, sub_epic_names: List[str], file_path: Path, rule_obj: Any, story_graph: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        name_without_prefix = file_name[5:] if file_name.startswith('test_') else file_name
        
    # ... (truncated)
```

---

## use_clear_function_parameters
**clear_parameters_scanner.py** - 2 violation(s)

[!] WARNING (line 20)
Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        self.story_graph = None
    
    def scan(self, story_graph: Dict[str, Any], rule_obj: Any = None, test_files: Optional[List['Path']] = None, code_files: Optional[List['Path']] = None, on_file_scanned: Optional[Any] = None) -> List[Dict[str, Any]]:
        self.story_graph = story_graph
        return super().scan(story_graph, rule_obj, test_files=test_files, code_files=code_files, on_file_scanned=on_file_scanned)
    # ... (truncated)
```

[!] WARNING (line 80)
Function "_check_parameters" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return False
    
    def _check_parameters(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any, domain_terms: set = None, content: str = None) -> Optional[Dict[str, Any]]:
        if domain_terms is None:
            domain_terms = set()
    # ... (truncated)
```

---

## use_clear_function_parameters
**code_scanner.py** - 4 violation(s)

[!] WARNING (line 13)
Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
class CodeScanner(Scanner):
    
    def scan(
        self, 
        story_graph: Dict[str, Any], 
    # ... (truncated)
```

[!] WARNING (line 177)
Function "scan_cross_file" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return False
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
    # ... (truncated)
```

[!] WARNING (line 206)
Function "_extract_code_snippet" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
            return None
    
    def _extract_code_snippet(self, content: str, ast_node: Optional[ast.AST] = None, 
                             start_line: Optional[int] = None, end_line: Optional[int] = None,
                             context_before: int = 2, max_lines: int = 50) -> str:
    # ... (truncated)
```

[!] WARNING (line 246)
Function "_create_violation_with_snippet" has 12 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return code_snippet
    
    def _create_violation_with_snippet(
        self, 
        rule_obj: Any,
    # ... (truncated)
```

---

## use_clear_function_parameters
**dead_code_scanner.py** - 2 violation(s)

[!] WARNING (line 23)
Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
    """Scanner for detecting dead/unused code."""
    
    def scan(
        self, 
        story_graph: Dict[str, Any], 
    # ... (truncated)
```

[!] WARNING (line 275)
Function "scan_cross_file" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return False
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
    # ... (truncated)
```

---

## use_clear_function_parameters
**dependency_chaining_code_scanner.py** - 2 violation(s)

[!] WARNING (line 124)
Function "_check_method_calls_for_instance_attrs" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return attrs
    
    def _check_method_calls_for_instance_attrs(
        self, func_node: ast.FunctionDef, class_name: str, file_path: Path, 
        rule_obj: Any, instance_attrs: Set[str]
    # ... (truncated)
```

[!] WARNING (line 143)
Function "_check_argument" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return violations
    
    def _check_argument(
        self, arg_node: ast.AST, method_name: str, class_name: str, file_path: Path, 
        rule_obj: Any, instance_attrs: Set[str], line_num: int
    # ... (truncated)
```

---

## use_clear_function_parameters
**domain_language_code_scanner.py** - 3 violation(s)

[!] WARNING (line 42)
Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return False
    
    def scan(self, story_graph: Dict[str, Any], rule_obj: Any = None, test_files: Optional[List['Path']] = None, code_files: Optional[List['Path']] = None, on_file_scanned: Optional[Any] = None) -> List[Dict[str, Any]]:
        self.story_graph = story_graph
        return super().scan(story_graph, rule_obj, test_files=test_files, code_files=code_files, on_file_scanned=on_file_scanned)
    # ... (truncated)
```

[!] WARNING (line 88)
Function "_check_domain_language" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return violations
    
    def _check_domain_language(self, class_node: ast.ClassDef, file_path: Path, rule_obj: Any, 
                               domain_terms: set, generic_names: set) -> List[Dict[str, Any]]:
        violations = []
    # ... (truncated)
```

[!] WARNING (line 115)
Function "_check_function_domain_language" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return violations
    
    def _check_function_domain_language(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any,
                                      domain_terms: set, generic_names: set, 
                                      enclosing_class: Optional[str] = None) -> List[Dict[str, Any]]:
    # ... (truncated)
```

---

## use_clear_function_parameters
**domain_scanner.py** - 1 violation(s)

[!] WARNING (line 17)
Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
    """
    
    def scan(
        self, 
        story_graph: Dict[str, Any], 
    # ... (truncated)
```

---

## use_clear_function_parameters
**duplication_scanner.py** - 1 violation(s)

[!] WARNING (line 1683)
Function "scan_cross_file" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return nearby_files
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
    # ... (truncated)
```

---

## use_clear_function_parameters
**excessive_guards_scanner.py** - 2 violation(s)

[!] WARNING (line 39)
Function "_check_function_guards" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return violations
    
    def _check_function_guards(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any, source_lines: List[str], content: str) -> List[Dict[str, Any]]:
        violations = []
        
    # ... (truncated)
```

[!] WARNING (line 226)
Function "_check_guard_pattern" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return False

    def _check_guard_pattern(self, guard_node: ast.If, file_path: Path, rule_obj: Any, source_lines: List[str], content: str) -> Optional[Dict[str, Any]]:
        test = guard_node.test
        
    # ... (truncated)
```

---

## use_clear_function_parameters
**function_size_scanner.py** - 1 violation(s)

[!] WARNING (line 37)
Function "_check_function_size" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return violations
    
    def _check_function_size(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any, source_lines: List[str], content: str) -> Optional[Dict[str, Any]]:
        # Calculate function size (end_lineno - lineno + 1)
        if not hasattr(func_node, 'end_lineno') or not func_node.end_lineno:
    # ... (truncated)
```

---

## use_clear_function_parameters
**generic_capability_scanner.py** - 1 violation(s)

[!] WARNING (line 41)
Function "_check_verb_pattern" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return 'unknown'
    
    def _check_verb_pattern(
        self, 
        name: str, 
    # ... (truncated)
```

---

## use_clear_function_parameters
**given_precondition_scanner.py** - 1 violation(s)

[!] WARNING (line 41)
Function "_check_given_is_functionality" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return steps
    
    def _check_given_is_functionality(self, step: str, node: StoryNode, scenario_idx: int, step_idx: int, rule_obj: Any) -> Optional[Dict[str, Any]]:
        step_lower = step.lower()
        
    # ... (truncated)
```

---

## use_clear_function_parameters
**given_state_not_actions_scanner.py** - 1 violation(s)

[!] WARNING (line 63)
Function "_check_given_is_action" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return steps
    
    def _check_given_is_action(self, step: str, node: StoryNode, scenario_idx: int, step_idx: int, rule_obj: Any) -> Optional[Dict[str, Any]]:
        # Common action verbs that should be in When, not Given
        action_verbs = [
    # ... (truncated)
```

---

## use_clear_function_parameters
**given_when_then_helpers_scanner.py** - 2 violation(s)

[!] WARNING (line 93)
Function "_check_test_method" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
            return None
    
    def _check_test_method(self, test_node: ast.FunctionDef, content: str, file_path: Path, 
                          rule_obj: Any, helper_functions: Set[str], tree: ast.AST) -> List[Dict[str, Any]]:
        violations = []
    # ... (truncated)
```

[!] WARNING (line 251)
Function "scan_cross_file" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return None, [], False, 0
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
    # ... (truncated)
```

---

## use_clear_function_parameters
**intention_revealing_names_scanner.py** - 3 violation(s)

[!] WARNING (line 21)
Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        self.story_graph = None
    
    def scan(self, story_graph: Dict[str, Any], rule_obj: Any = None, test_files: Optional[List['Path']] = None, code_files: Optional[List['Path']] = None, on_file_scanned: Optional[Any] = None) -> List[Dict[str, Any]]:
        self.story_graph = story_graph
        return super().scan(story_graph, rule_obj, test_files=test_files, code_files=code_files, on_file_scanned=on_file_scanned)
    # ... (truncated)
```

[!] WARNING (line 68)
Function "_check_variable_names" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return violations
    
    def _check_variable_names(self, tree: ast.AST, file_path: Path, rule_obj: Any, content: str, domain_terms: set = None, docstring_ranges: List[tuple] = None) -> List[Dict[str, Any]]:
        violations = []
        
    # ... (truncated)
```

[!] WARNING (line 128)
Function "_create_generic_name_violation" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return violations
    
    def _create_generic_name_violation(
        self, 
        rule_obj: Any, 
    # ... (truncated)
```

---

## use_clear_function_parameters
**parameterized_tests_scanner.py** - 1 violation(s)

[!] WARNING (line 9)
Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
class ParameterizedTestsScanner(Scanner):
    
    def scan(
        self, 
        story_graph: Dict[str, Any], 
    # ... (truncated)
```

---

## use_clear_function_parameters
**primitive_vs_object_scanner.py** - 1 violation(s)

[!] WARNING (line 144)
Function "_create_primitive_violation" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return False
    
    def _create_primitive_violation(
        self,
        rule_obj: Any,
    # ... (truncated)
```

---

## use_clear_function_parameters
**real_implementations_scanner.py** - 3 violation(s)

[!] WARNING (line 35)
Function "_check_test_methods_call_production_code" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return violations
    
    def _check_test_methods_call_production_code(
        self, content: str, lines: List[str], file_path: Path, rule_obj: Any, story_graph: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
    # ... (truncated)
```

[!] WARNING (line 345)
Function "_has_production_code_calls" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return not has_actual_code
    
    def _has_production_code_calls(
        self, method: ast.FunctionDef, imports: List[ast.Import | ast.ImportFrom],
        src_locations: List[str], project_path: Path, file_path: Path = None, tree: ast.AST = None
    # ... (truncated)
```

[!] WARNING (line 393)
Function "_helper_calls_production_code" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return False
    
    def _helper_calls_production_code(
        self, helper_name: str, file_path: Path, tree: ast.AST,
        src_locations: List[str], project_path: Path
    # ... (truncated)
```

---

## use_clear_function_parameters
**resource_oriented_code_scanner.py** - 1 violation(s)

[!] WARNING (line 28)
Function "scan_cross_file" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return []
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
    # ... (truncated)
```

---

## use_clear_function_parameters
**scanner.py** - 2 violation(s)

[!] WARNING (line 18)
Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
class Scanner(ABC):
    
    def scan(
        self, 
        story_graph: Dict[str, Any], 
    # ... (truncated)
```

[!] WARNING (line 63)
Function "scan_cross_file" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return self._empty_violation_list()
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
    # ... (truncated)
```

---

## use_clear_function_parameters
**scenarios_on_story_docs_scanner.py** - 1 violation(s)

[!] WARNING (line 96)
Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        self._in_scope_story_names: Optional[Set[str]] = None
    
    def scan(
        self, 
        story_graph: Dict[str, Any], 
    # ... (truncated)
```

---

## use_clear_function_parameters
**setup_similarity_scanner.py** - 1 violation(s)

[!] WARNING (line 25)
Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
    MIN_INTRA_DUP = 2  # within a single test

    def scan(
        self,
        story_graph: Dict[str, Any],
    # ... (truncated)
```

---

## use_clear_function_parameters
**specification_match_scanner.py** - 3 violation(s)

[!] WARNING (line 77)
Function "_create_violation_with_line_number" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return False
    
    def _create_violation_with_line_number(
        self,
        rule_obj: Any,
    # ... (truncated)
```

[!] WARNING (line 188)
Function "_check_specification_matches" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return ""
    
    def _check_specification_matches(self, tree: ast.AST, content: str, file_path: Path, 
                                    rule_obj: Any, story_graph: Dict[str, Any]) -> List[Dict[str, Any]]:
        violations = []
    # ... (truncated)
```

[!] WARNING (line 374)
Function "_check_variable_matches" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return None
    
    def _check_variable_matches(self, test_method: ast.FunctionDef, story: Dict[str, Any], 
                                domain_terms: set, rule_obj: Any, file_path: Path) -> List[Dict[str, Any]]:
        violations = []
    # ... (truncated)
```

---

## use_clear_function_parameters
**spine_optional_scanner.py** - 2 violation(s)

[!] WARNING (line 9)
Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
class SpineOptionalScanner(StoryScanner):
    
    def scan(
        self, 
        story_graph: Dict[str, Any], 
    # ... (truncated)
```

[!] WARNING (line 103)
Function "_check_all_stories_mandatory" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return violations
    
    def _check_all_stories_mandatory(self, all_stories: List[Story], sequential_stories: List[Story], optional_stories: List[Story], story_group: StoryGroup, rule_obj: Any) -> Optional[Dict[str, Any]]:
        if len(all_stories) < 2:
            return None
    # ... (truncated)
```

---

## use_clear_function_parameters
**story_scanner.py** - 1 violation(s)

[!] WARNING (line 10)
Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
class StoryScanner(Scanner):
    
    def scan(
        self, 
        story_graph: Dict[str, Any], 
    # ... (truncated)
```

---

## use_clear_function_parameters
**unnecessary_parameter_passing_scanner.py** - 3 violation(s)

[!] WARNING (line 38)
Function "_check_class" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return violations
    
    def _check_class(self, class_node: ast.ClassDef, file_path: Path, rule_obj: Any, lines: List[str], content: str) -> List[Dict[str, Any]]:
        violations = []
        
    # ... (truncated)
```

[!] WARNING (line 82)
Function "_check_method_parameters" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return attrs
    
    def _check_method_parameters(self, method_node: ast.FunctionDef, instance_attrs: set, 
                                file_path: Path, rule_obj: Any, lines: List[str], content: str) -> List[Dict[str, Any]]:
        violations = []
    # ... (truncated)
```

[!] WARNING (line 133)
Function "_check_property_extraction" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return True
    
    def _check_property_extraction(self, method_node: ast.FunctionDef, instance_attrs: set,
                                  file_path: Path, rule_obj: Any, lines: List[str], content: str) -> List[Dict[str, Any]]:
        violations = []
    # ... (truncated)
```

---

## use_clear_function_parameters
**validation_scanner_status_builder.py** - 3 violation(s)

[!] WARNING (line 37)
Function "_categorize_rule_by_status" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return result

    def _categorize_rule_by_status(self, status: str, rule_dict: Dict, rule_file: str, scanner_status: Dict, result: Dict):
        if status == 'EXECUTED':
            result['executed'].append(self._build_executed_rule_info(rule_dict, rule_file, scanner_status))
    # ... (truncated)
```

[!] WARNING (line 239)
Function "_get_rule_status_display" has vague parameter name "info" - use descriptive name

```python
        return lines

    def _get_rule_status_display(self, info: Dict) -> tuple:
        status, violations = (info.get('status', 'UNKNOWN'), info.get('violations', 0))
        if status in ('EXECUTION_FAILED', 'LOAD_FAILED'):
    # ... (truncated)
```

[!] WARNING (line 253)
Function "_format_rule_scanner_info" has vague parameter name "info" - use descriptive name

```python
        return ('🟨', f'{violations} VIOLATION(S)')

    def _format_rule_scanner_info(self, info: Dict) -> List[str]:
        lines = []
        status = info.get('status', 'UNKNOWN')
    # ... (truncated)
```

---

## use_clear_function_parameters
**vertical_slice_scanner.py** - 1 violation(s)

[!] WARNING (line 18)
Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return violations
    
    def scan(
        self, 
        story_graph: Dict[str, Any], 
    # ... (truncated)
```

---

## use_clear_function_parameters
**json_scope.py** - 1 violation(s)

[!] WARNING (line 115)
Function "_enrich_sub_epic_with_links" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
                    self._enrich_sub_epic_with_links(sub_epic, test_dir, docs_stories_map, epic['name'])
    
    def _enrich_sub_epic_with_links(self, sub_epic: dict, test_dir: Path, docs_stories_map: Path, epic_name: str, parent_path: str = None):
        """Recursively enrich sub-epic with test file and document links."""
        # Build the document path (epic/sub-epic hierarchy)
    # ... (truncated)
```

---

## use_clear_function_parameters
**render_instruction_builder.py** - 1 violation(s)

[!] WARNING (line 58)
Function "_update_instructions_dict" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
                base_instructions_list.insert(insert_position, line)

    def _update_instructions_dict(self, instructions: Dict[str, Any], base_instructions_list: List[str], render_instructions: Dict[str, Any], template_specs: List['RenderSpec'], executed_specs: List['RenderSpec'], render_specs: List['RenderSpec'], working_dir: Path) -> None:
        instructions['base_instructions'] = base_instructions_list
        instructions['render_instructions'] = render_instructions
    # ... (truncated)
```

---

## use_clear_function_parameters
**validation_executor.py** - 1 violation(s)

[!] WARNING (line 86)
Function "_process_scanner_status" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return {'counts': counts, 'lines': scanner_status_lines}

    def _process_scanner_status(self, status, counts, scanner_status_lines, rule_file, scanner_status):
        if status == 'EXECUTED':
            counts['executed'] += 1
    # ... (truncated)
```

---

## use_clear_function_parameters
**cursor_command_visitor.py** - 1 violation(s)

[!] WARNING (line 258)
Function "__init__" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
    """Wrapper for generating behavior command files."""
    
    def __init__(self, behavior, workspace_root: Path, bot_location: Path, bot_name: str, is_current: bool, bot, generator_ref):
        self.workspace_root = workspace_root
        self.bot_location = bot_location
    # ... (truncated)
```

---

## use_clear_function_parameters
**violation.py** - 1 violation(s)

[!] WARNING (line 60)
Function "create_from_rule_and_context" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
    
    @classmethod
    def create_from_rule_and_context(
        cls,
        rule: 'Rule',
    # ... (truncated)
```

---

## use_domain_language
**orchestrator.py** - 1 violation(s)

[!] WARNING (line 92)
Function "generate_for_all_actions" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").

---

## use_domain_language
**complexity_metrics.py** - 1 violation(s)

[!] WARNING (line 204)
Function "calculate_lcom" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").

---

## use_domain_language
**cursor_command_visitor.py** - 1 violation(s)

[!] WARNING (line 274)
Function "generate_command_file" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").

---

## use_domain_language
**block.py** - 1 violation(s)

[!] WARNING (line 72)
Function "calculate_complexity" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").

---

## use_explicit_dependencies
**utils.py** - 1 violation(s)

[!] WARNING (line 80)
Global variable usage detected - dependencies should be explicit (passed as parameters)

---

## use_natural_english
**business_readable_test_names_scanner.py** - 12 violation(s)

[i] INFO (line 269)
Variable "start_line_0" uses technical notation. Use natural English instead.

```python
        if ast_node is not None:
            # Use AST node to determine lines
            start_line_0 = ast_node.lineno - 1 if hasattr(ast_node, 'lineno') and ast_node.lineno else 0
            
```

[i] INFO (line 272)
Variable "end_line_0" uses technical notation. Use natural English instead.

```python
            
            if hasattr(ast_node, 'end_lineno') and ast_node.end_lineno:
                end_line_0 = ast_node.end_lineno  # end_lineno is 1-indexed, exclusive
            else:
```

[i] INFO (line 275)
Variable "end_line_0" uses technical notation. Use natural English instead.

```python
            else:
                # Estimate end by finding the maximum line number in the subtree
                end_line_0 = start_line_0 + 1
                for node in ast.walk(ast_node):
```

[i] INFO (line 281)
Variable "start_line_0" uses technical notation. Use natural English instead.

```python
        elif start_line is not None:
            # Use provided line numbers (1-indexed, convert to 0-indexed)
            start_line_0 = start_line - 1
            if end_line is not None:
```

[i] INFO (line 290)
Variable "start_line_0" uses technical notation. Use natural English instead.

```python
            return ""
        
        snippet_start = max(0, start_line_0 - context_before)
        snippet_end = min(len(lines), end_line_0 + 1)
```

[i] INFO (line 291)
Variable "end_line_0" uses technical notation. Use natural English instead.

```python
        
        snippet_start = max(0, start_line_0 - context_before)
        snippet_end = min(len(lines), end_line_0 + 1)
        code_snippet = '\n'.join(lines[snippet_start:snippet_end])
```

[i] INFO (line 275)
Variable "start_line_0" uses technical notation. Use natural English instead.

```python
            else:
                # Estimate end by finding the maximum line number in the subtree
                end_line_0 = start_line_0 + 1
                for node in ast.walk(ast_node):
```

[i] INFO (line 283)
Variable "end_line_0" uses technical notation. Use natural English instead.

```python
            start_line_0 = start_line - 1
            if end_line is not None:
                end_line_0 = end_line  # end_line is 1-indexed, exclusive (like end_lineno)
            else:
```

[i] INFO (line 285)
Variable "end_line_0" uses technical notation. Use natural English instead.

```python
                end_line_0 = end_line  # end_line is 1-indexed, exclusive (like end_lineno)
            else:
                end_line_0 = start_line_0 + 1
        else:
```

[i] INFO (line 278)
Variable "end_line_0" uses technical notation. Use natural English instead.

```python
                for node in ast.walk(ast_node):
                    if hasattr(node, 'lineno') and node.lineno:
                        end_line_0 = max(end_line_0, node.lineno)
        elif start_line is not None:
```

[i] INFO (line 285)
Variable "start_line_0" uses technical notation. Use natural English instead.

```python
                end_line_0 = end_line  # end_line is 1-indexed, exclusive (like end_lineno)
            else:
                end_line_0 = start_line_0 + 1
        else:
```

[i] INFO (line 278)
Variable "end_line_0" uses technical notation. Use natural English instead.

```python
                for node in ast.walk(ast_node):
                    if hasattr(node, 'lineno') and node.lineno:
                        end_line_0 = max(end_line_0, node.lineno)
        elif start_line is not None:
```

---

## use_natural_english
**code_scanner.py** - 12 violation(s)

[i] INFO (line 214)
Variable "start_line_0" uses technical notation. Use natural English instead.

```python
        if ast_node is not None:
            # Use AST node to determine lines
            start_line_0 = ast_node.lineno - 1 if hasattr(ast_node, 'lineno') and ast_node.lineno else 0
            
```

[i] INFO (line 217)
Variable "end_line_0" uses technical notation. Use natural English instead.

```python
            
            if hasattr(ast_node, 'end_lineno') and ast_node.end_lineno:
                end_line_0 = ast_node.end_lineno  # end_lineno is 1-indexed, exclusive
            else:
```

[i] INFO (line 220)
Variable "end_line_0" uses technical notation. Use natural English instead.

```python
            else:
                # Estimate end by finding the maximum line number in the subtree
                end_line_0 = start_line_0 + 1
                for node in ast.walk(ast_node):
```

[i] INFO (line 226)
Variable "start_line_0" uses technical notation. Use natural English instead.

```python
        elif start_line is not None:
            # Use provided line numbers (1-indexed, convert to 0-indexed)
            start_line_0 = start_line - 1
            if end_line is not None:
```

[i] INFO (line 235)
Variable "start_line_0" uses technical notation. Use natural English instead.

```python
            return ""
        
        snippet_start = max(0, start_line_0 - context_before)
        snippet_end = min(len(lines), end_line_0 + 1)
```

[i] INFO (line 236)
Variable "end_line_0" uses technical notation. Use natural English instead.

```python
        
        snippet_start = max(0, start_line_0 - context_before)
        snippet_end = min(len(lines), end_line_0 + 1)
        code_snippet = '\n'.join(lines[snippet_start:snippet_end])
```

[i] INFO (line 220)
Variable "start_line_0" uses technical notation. Use natural English instead.

```python
            else:
                # Estimate end by finding the maximum line number in the subtree
                end_line_0 = start_line_0 + 1
                for node in ast.walk(ast_node):
```

[i] INFO (line 228)
Variable "end_line_0" uses technical notation. Use natural English instead.

```python
            start_line_0 = start_line - 1
            if end_line is not None:
                end_line_0 = end_line  # end_line is 1-indexed, exclusive (like end_lineno)
            else:
```

[i] INFO (line 230)
Variable "end_line_0" uses technical notation. Use natural English instead.

```python
                end_line_0 = end_line  # end_line is 1-indexed, exclusive (like end_lineno)
            else:
                end_line_0 = start_line_0 + 1
        else:
```

[i] INFO (line 223)
Variable "end_line_0" uses technical notation. Use natural English instead.

```python
                for node in ast.walk(ast_node):
                    if hasattr(node, 'lineno') and node.lineno:
                        end_line_0 = max(end_line_0, node.lineno)
        elif start_line is not None:
```

[i] INFO (line 230)
Variable "start_line_0" uses technical notation. Use natural English instead.

```python
                end_line_0 = end_line  # end_line is 1-indexed, exclusive (like end_lineno)
            else:
                end_line_0 = start_line_0 + 1
        else:
```

[i] INFO (line 223)
Variable "end_line_0" uses technical notation. Use natural English instead.

```python
                for node in ast.walk(ast_node):
                    if hasattr(node, 'lineno') and node.lineno:
                        end_line_0 = max(end_line_0, node.lineno)
        elif start_line is not None:
```

---

## use_natural_english
**spine_optional_scanner.py** - 2 violation(s)

[i] INFO (line 89)
Variable "is_optional" uses technical notation. Use natural English instead.

```python
                continue
            
            is_optional = story.data.get('optional', False)
            sequential_order = story.sequential_order
```

[i] INFO (line 92)
Variable "is_optional" uses technical notation. Use natural English instead.

```python
            sequential_order = story.sequential_order
            
            if sequential_order == 0 and not is_optional:
                location = story.map_location('optional')
```

---

Completed: 2026-01-16 00:51:38
Total violations: 1398
Scanners executed: 31
