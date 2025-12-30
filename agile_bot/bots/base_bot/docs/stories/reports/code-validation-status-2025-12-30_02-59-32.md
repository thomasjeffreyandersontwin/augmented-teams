# Validation Status - code
Started: 2025-12-30 02:59:32
Files: 275

## avoid_excessive_guards
**action_context.py** - 3 violation(s)

[!] WARNING (line 102)
Line 102: Variable truthiness check detected (if not matches_include:). Assume variable exists - let code fail fast if missing.

```python
                            break
                
                if not matches_include:
                    continue
            
```

[!] WARNING (line 117)
Line 117: Variable truthiness check detected (if matches_exclude:). Assume variable exists - let code fail fast if missing.

```python
                        pass
                
                if matches_exclude:
                    continue
            
```

[!] WARNING (line 188)
Line 188: Variable truthiness check detected (if not data:). Assume variable exists - let code fail fast if missing.

```python
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Scope':
        if not data:
            return cls()
        
```

---

## avoid_excessive_guards
**repl_session.py** - 1 violation(s)

[!] WARNING (line 1467)
Line 1467: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

```python
    def parse_command_parameters(self, args: str) -> Dict[str, Any]:
        params = {}
        if not args:
            return params
        
```

---

## eliminate_duplication
**repl_session.py** - 2 violation(s)

[X] ERROR (line 191)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (display_current_state:191-202):
```python
lines.append('```')
lines.append(str(self.workspace_directory))
lines.append('```')
lines.append('')
lines.append('To change path:')
lines.append('```')
lines.append('path demo/mob_minion             ...
```

Location (display_current_state:226-234):
```python
lines.append(formatter.subsection_separator())
lines.append(f'## {formatter.position_icon()} **Progress**')
lines.append('**Current Position:**')
lines.append('```')
lines.append(f'{self.progress_path...
```

[X] ERROR (line 469)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_handle_next_command:469-488):
```python
if not self.has_current_action:
    return REPLCommandResponse(output='ERROR: No current action', response='ERROR: No current action', status='error')
behavior = self.current_behavior
if not behavior:...
```

Location (_handle_back_command:505-524):
```python
if not self.has_current_action:
    return REPLCommandResponse(output='ERROR: No current action', response='ERROR: No current action', status='error')
behavior = self.current_behavior
if not behavior:...
```

---


## Cross-File Duplication Analysis
Scanning 3 changed file(s) against 20 total files...
Extracted 408 changed blocks, 451 reference blocks
Starting 184,008 pairwise comparisons...
Comparing: 5% (9,201/184,008) - 0 violations - ETA: 56s  
Comparing: 10% (18,401/184,008) - 0 violations - ETA: 61s  
Comparing: 15% (27,602/184,008) - 0 violations - ETA: 54s  
Comparing: 20% (36,802/184,008) - 0 violations - ETA: 52s  
Comparing: 25% (46,002/184,008) - 0 violations - ETA: 49s  
Comparing: 30% (55,203/184,008) - 0 violations - ETA: 45s  
Comparing: 35% (64,403/184,008) - 0 violations - ETA: 43s  
Comparing: 40% (73,604/184,008) - 0 violations - ETA: 40s  
Comparing: 45% (82,804/184,008) - 0 violations - ETA: 38s  
Comparing: 50% (92,004/184,008) - 0 violations - ETA: 35s  
Comparing: 55% (101,205/184,008) - 0 violations - ETA: 33s  
Comparing: 60% (110,405/184,008) - 0 violations - ETA: 30s  
Comparing: 65% (119,606/184,008) - 0 violations - ETA: 26s  
Found 10 violations so far...
Comparing: 70% (128,806/184,008) - 12 violations - ETA: 22s  
Comparing: 75% (138,006/184,008) - 12 violations - ETA: 19s  
Comparing: 80% (147,207/184,008) - 12 violations - ETA: 15s  
Comparing: 85% (156,407/184,008) - 12 violations - ETA: 11s  
Comparing: 90% (165,608/184,008) - 12 violations - ETA: 7s  
Comparing: 95% (174,808/184,008) - 12 violations - ETA: 4s  
Complete: 183224 comparisons, 12 violations

## enforce_encapsulation
**repl_session.py** - 1 violation(s)

[!] WARNING (line 725)
Method "_handle_scope_command" in class "REPLSession" has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

---

## keep_classes_small_with_single_responsibility
**action_context.py** - 1 violation(s)

[!] WARNING (line 126)
Class "Scope" is 314 lines - should be under 300 lines (extract related methods into separate classes)

```python

@dataclass
class Scope:
    """Scope for filtering bot operations to specific content.
    
    Uses KnowledgeGraphFilter for story/epic/increment scoping
    and FileFilter for file-based scoping. Maintains backward compatibility
    with type/value/exclude API.
    
    The Scope object is responsible for its own persistence to the bot state file.
    # ... (truncated)
```

---

## keep_classes_small_with_single_responsibility
**repl_session.py** - 1 violation(s)

[!] WARNING (line 17)
Class "REPLSession" is 1582 lines - should be under 300 lines (extract related methods into separate classes)

```python


class REPLSession:
    def __init__(self, bot, workspace_directory: Path):
        self.cli_bot = CLIBot(bot, self)
        self.workspace_directory = Path(workspace_directory)
        tty_result = self.detect_tty()
        self.formatter = FormatterFactory.create_formatter(tty_detected=tty_result.tty_detected)
    
    @property
    # ... (truncated)
```

---

## keep_functions_small_focused
**action_context.py** - 2 violation(s)

[!] WARNING (line 75)
Function "filter_files" is 39 lines - should be under 20 lines (extract complex logic to helper functions)

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
                            file_path_obj.match(f'**/{pattern_normalized}')):
                            matches_exclude = True
                            break
                    except (ValueError, TypeError):
                        pass
                
                if matches_exclude:
                    continue
            
            filtered.append(file_path)
        
        return filtered
    # ... (truncated)
```

[!] WARNING (line 258)
Function "to_display_lines" is 43 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return workspace_directory / 'behavior_action_state.json'
    
    def to_display_lines(self, workspace_directory: 'Path') -> List[str]:
        """Render scope as display lines with hierarchical expansion.
        
        Returns plain text lines showing scope filter and matched items.
        """
        from pathlib import Path
        import json
        
        lines = []
        
        # Show the scope filter value
        filter_str = ', '.join(self.value) if isinstance(self.value, list) else str(self.value)
        lines.append(f"Scope Filter: {filter_str}")
        
        if self.type == ScopeType.STORY:
            story_graph_path = workspace_directory / 'docs' / 'stories' / 'story-graph.json'
            if story_graph_path.exists():
                try:
                    graph_data = json.loads(story_graph_path.read_text(encoding='utf-8'))
                    matched_items = self._find_scope_matches_in_graph(graph_data, self.value)
                    lines.extend(matched_items)
                except Exception:
                    # Fallback to simple list
                    for item in (self.value if isinstance(self.value, list) else [self.value]):
                        lines.append(f"  - {item}")
            else:
                for item in (self.value if isinstance(self.value, list) else [self.value]):
                    lines.append(f"  - {item}")
        elif self.type == ScopeType.FILES:
            # Expand file paths to show all actual files that will be scanned
            expanded_files = self._expand_file_paths(workspace_directory)
            if expanded_files:
                for file_path in sorted(expanded_files):
                    # Show relative path from workspace
                    try:
                        rel_path = file_path.relative_to(workspace_directory)
                        lines.append(f"  - {rel_path}")
                    except ValueError:
                        lines.append(f"  - {file_path}")
            else:
                # Fallback to showing the scope value if expansion fails
                for item in (self.value if isinstance(self.value, list) else [self.value]):
                    lines.append(f"  - {item} (no files found)")
        else:
            if isinstance(self.value, list):
                for item in self.value:
                    lines.append(f"  - {item}")
            else:
    # ... (truncated)
```

---

## keep_functions_small_focused
**repl_session.py** - 1 violation(s)

[!] WARNING (line 144)
Function "display_current_state" is 83 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return True
    
    def display_current_state(self, full=False) -> REPLStateDisplay:
        """Single source of truth for displaying current bot state.
        
        Returns REPLStateDisplay with formatted status output showing:
        - Bot name and paths
        - Current position header
        - Scope filter (if set)
        - Progress in workflow
        - Hierarchical behavior/action/operation tree
        """
        if not self.has_current_action:
            if not self._initialize_to_first_behavior_action():
                return REPLStateDisplay(
                    output="No behaviors available\n\n  help          - Show detailed help\n  exit          - Exit REPL",
                    state_loaded=False
                )
            return self.display_current_state(full=full)
        
        lines = []
        formatter = self.formatter
        
        # Get bot name from bot_directory
        if self.bot and hasattr(self.bot, 'bot_paths'):
            bot_name = self.bot.bot_paths.bot_directory.name
        else:
            bot_name = 'UNKNOWN'
        
        # THICK LINE at top
        lines.append(formatter.section_separator())
        lines.append("")
        
        # Bot section header
        lines.append(f"## {formatter.bot_icon()} Bot: {bot_name}")
        
        if self.bot:
            bot_path = self.bot.bot_paths.bot_directory if hasattr(self.bot, 'bot_paths') else 'Unknown'
            lines.append(f"**Bot Path:**")
            lines.append("```")
            lines.append(str(bot_path))
            lines.append("```")
        
        lines.append("")
        
        # Workspace section
        workspace_name = self.workspace_directory.name if hasattr(self.workspace_directory, 'name') else 'base_bot'
        lines.append(f"{formatter.workspace_icon()} **Workspace:** {workspace_name}")
        lines.append(f"**Path:**")
        lines.append("```")
    # ... (truncated)
```

---

## keep_functions_small_focused
**rules.py** - 2 violation(s)

[!] WARNING (line 151)
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

[!] WARNING (line 278)
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

## maintain_vertical_density
**action_context.py** - 1 violation(s)

[i] INFO (line 258)
Function "to_display_lines" is 51 lines - consider improving vertical density by declaring variables near usage

```python
        return workspace_directory / 'behavior_action_state.json'
    
    def to_display_lines(self, workspace_directory: 'Path') -> List[str]:
        """Render scope as display lines with hierarchical expansion.
        
        Returns plain text lines showing scope filter and matched items.
        """
        from pathlib import Path
        import json
        
    # ... (truncated)
```

---

## maintain_vertical_density
**repl_session.py** - 10 violation(s)

[i] INFO (line 144)
Function "display_current_state" is 114 lines - consider improving vertical density by declaring variables near usage

```python
        return True
    
    def display_current_state(self, full=False) -> REPLStateDisplay:
        """Single source of truth for displaying current bot state.
        
        Returns REPLStateDisplay with formatted status output showing:
        - Bot name and paths
        - Current position header
        - Scope filter (if set)
        - Progress in workflow
    # ... (truncated)
```

[i] INFO (line 268)
Function "_convert_domain_result_to_repl_response" is 57 lines - consider improving vertical density by declaring variables near usage

```python
        return state_display.output
    
    def _convert_domain_result_to_repl_response(self, result: Dict[str, Any], command: str) -> REPLCommandResponse:
        """Convert a domain method result to a REPL response.
        
        Args:
            result: Dict returned from domain method
            command: The command that was executed
        
        Returns:
    # ... (truncated)
```

[i] INFO (line 339)
Function "_handle_simple_command" is 59 lines - consider improving vertical density by declaring variables near usage

```python
        return self._handle_simple_command(command)
    
    def _handle_simple_command(self, command: str) -> REPLCommandResponse:
        parts = command.split(maxsplit=1)
        command_verb = parts[0].lower()
        command_args = parts[1] if len(parts) > 1 else ""
        
        # Meta commands
        if command_verb == 'help':
            return self._handle_help_command(command_args)
    # ... (truncated)
```

[i] INFO (line 549)
Function "_handle_instructions_command" is 56 lines - consider improving vertical density by declaring variables near usage

```python
        )
    
    def _handle_instructions_command(self, args: str = "") -> REPLCommandResponse:
        """Handle instructions command"""
        import sys
        print(f"[DEBUG] _handle_instructions_command called with args: '{args}'", file=sys.stderr)
        if not self.has_current_action:
            return REPLCommandResponse(
                output="ERROR: No current action to get instructions for",
                response="ERROR: No current action",
    # ... (truncated)
```

[i] INFO (line 627)
Function "_handle_confirm_command" is 54 lines - consider improving vertical density by declaring variables near usage

```python
            )
    
    def _handle_confirm_command(self) -> REPLCommandResponse:
        """Handle confirm command"""
        if not self.has_current_action:
            return REPLCommandResponse(
                output="ERROR: No current action to confirm",
                response="ERROR: No current action",
                status="error"
            )
    # ... (truncated)
```

[i] INFO (line 701)
Function "_handle_scope_command" is 65 lines - consider improving vertical density by declaring variables near usage

```python
        )
    
    def _handle_scope_command(self, args: str = "") -> REPLCommandResponse:
        """Handle scope command"""
        if not args:
            # Show current scope
            output = self.cli_bot.get_scope_display()
            return REPLCommandResponse(
                output=output,
                response=output,
    # ... (truncated)
```

[i] INFO (line 842)
Function "_execute_operation_locally" is 60 lines - consider improving vertical density by declaring variables near usage

```python
            return None, args.strip().strip('"').strip("'")
    
    def _execute_operation_locally(self, target: str, cli_args: str = "") -> str:
        """Execute a CLI operation locally and return its output.
        
        Args:
            target: CLI target (e.g., 'tests.build', 'tests.build.instructions', 'tests.build.submit')
            cli_args: CLI arguments like '--scope "X"'
        
        Returns:
    # ... (truncated)
```

[i] INFO (line 1133)
Function "_handle_dot_notation" is 127 lines - consider improving vertical density by declaring variables near usage

```python
            pass
    
    def _handle_dot_notation(self, command: str) -> REPLCommandResponse:
        """Handle dot notation commands (behavior.action.operation)"""
        # Parse dot notation: behavior.action.operation or action.operation or .operation
        parts = command.split()
        dot_path = parts[0]
        args = ' '.join(parts[1:]) if len(parts) > 1 else ""
        
        path_parts = dot_path.split('.')
    # ... (truncated)
```

[i] INFO (line 1261)
Function "_handle_action_shortcut" is 60 lines - consider improving vertical density by declaring variables near usage

```python
            )
    
    def _handle_action_shortcut(self, action_name: str, args_str: str) -> REPLCommandResponse:
        args_str = args_str.strip()
        
        # Parse CLI-style arguments (--message, --scope, etc.)
        cli_args = []
        subcommand = None
        
        if args_str:
    # ... (truncated)
```

[i] INFO (line 1366)
Function "_execute_action_with_args" is 73 lines - consider improving vertical density by declaring variables near usage

```python
        return converted_args
    
    def _execute_action_with_args(self, action_name: str, cli_args: list, operation: str = None) -> REPLCommandResponse:
        if not self.has_current_behavior:
            return REPLCommandResponse(
                output="ERROR: No current behavior set. Please select a behavior first.",
                response="ERROR: No current behavior set",
                status="error"
            )
        
    # ... (truncated)
```

---

## never_swallow_exceptions
**action_context.py** - 2 violation(s)

[X] ERROR (line 250)
Except block only contains pass at line 250 - exceptions must be logged or rethrown, never swallowed

```python
                del state_data['scope']
                state_file.write_text(json.dumps(state_data, indent=2))
        except (json.JSONDecodeError, IOError):
            pass
    
```

[X] ERROR (line 114)
Except block only contains pass at line 114 - exceptions must be logged or rethrown, never swallowed

```python
                            matches_exclude = True
                            break
                    except (ValueError, TypeError):
                        pass
                
```

---

## never_swallow_exceptions
**repl_session.py** - 2 violation(s)

[X] ERROR (line 1130)
Except block only contains pass at line 1130 - exceptions must be logged or rethrown, never swallowed

```python
            state_data['completed_behaviors'] = completed
            state_file.write_text(json.dumps(state_data, indent=2))
        except (json.JSONDecodeError, IOError):
            pass
    
```

[X] ERROR (line 78)
Except block only contains pass at line 78 - exceptions must be logged or rethrown, never swallowed

```python
                state_data = json.loads(state_file.read_text())
                return state_data.get('action_phase', 'not_started')
            except (json.JSONDecodeError, IOError):
                pass
        return 'not_started'
```

---

## refactor_completely_not_partially
**action_context.py** - 2 violation(s)

[!] WARNING (line 280)
Fallback/legacy support code found (comment at line 280, code at line 281) - complete refactoring by removing old pattern support

[!] WARNING (line 298)
Fallback/legacy support code found (comment at line 298, code at line 299) - complete refactoring by removing old pattern support

---

## refactor_completely_not_partially
**repl_session.py** - 3 violation(s)

[!] WARNING (line 72)
Fallback/legacy support code found (comment at line 72, code at line 73) - complete refactoring by removing old pattern support

[!] WARNING (line 239)
Fallback/legacy support code found (comment at line 239, code at line 240) - complete refactoring by removing old pattern support

[!] WARNING (line 1509)
Fallback/legacy support code found (comment at line 1509, code at line 1510) - complete refactoring by removing old pattern support

---

## simplify_control_flow
**action_context.py** - 4 violation(s)

[!] WARNING (line 75)
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

[!] WARNING (line 144)
Function "__post_init__" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
    _file_filter: Optional[FileFilter] = field(default=None, repr=False)
    
    def __post_init__(self):
        """Initialize filter objects from type/value/exclude."""
        # Create knowledge graph filter for story/epic/increment types
        if self.type in (ScopeType.STORY, ScopeType.EPIC, ScopeType.INCREMENT):
            if self.type == ScopeType.STORY:
                self._knowledge_graph_filter = KnowledgeGraphFilter(stories=self.value)
            elif self.type == ScopeType.EPIC:
                self._knowledge_graph_filter = KnowledgeGraphFilter(epics=self.value)
            elif self.type == ScopeType.INCREMENT:
                # Convert string values to integers
                increments = [int(v) if isinstance(v, str) and v.isdigit() else v for v in self.value]
                self._knowledge_graph_filter = KnowledgeGraphFilter(increments=increments)
        
    # ... (truncated)
```

[!] WARNING (line 258)
Function "to_display_lines" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return workspace_directory / 'behavior_action_state.json'
    
    def to_display_lines(self, workspace_directory: 'Path') -> List[str]:
        """Render scope as display lines with hierarchical expansion.
        
        Returns plain text lines showing scope filter and matched items.
        """
        from pathlib import Path
        import json
        
        lines = []
        
        # Show the scope filter value
        filter_str = ', '.join(self.value) if isinstance(self.value, list) else str(self.value)
        lines.append(f"Scope Filter: {filter_str}")
    # ... (truncated)
```

[!] WARNING (line 310)
Function "_expand_file_paths" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return lines
    
    def _expand_file_paths(self, workspace_directory: 'Path') -> List['Path']:
        """Expand file scope paths to actual files that will be scanned."""
        from pathlib import Path
        import glob as glob_module
        
        all_files = []
        # Ensure value is treated as a list
        paths = self.value if isinstance(self.value, list) else [self.value]
        
        for path_str in paths:
            # Check if path contains glob patterns
            has_glob = any(char in path_str for char in ['*', '?', '['])
            
    # ... (truncated)
```

---

## simplify_control_flow
**repl_session.py** - 5 violation(s)

[!] WARNING (line 438)
Function "_handle_current_command" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        )
    
    def _handle_current_command(self) -> REPLCommandResponse:
        """Re-execute current operation based on progress state"""
        if not self.has_current_action:
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
        
        # Extract operation from progress (behavior.action.operation)
        progress = self.get_progress_line()
        if '.' in progress and 'Progress: ' in progress:
            parts = progress.replace('Progress: ', '').split('.')
    # ... (truncated)
```

[!] WARNING (line 701)
Function "_handle_scope_command" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        )
    
    def _handle_scope_command(self, args: str = "") -> REPLCommandResponse:
        """Handle scope command"""
        if not args:
            # Show current scope
            output = self.cli_bot.get_scope_display()
            return REPLCommandResponse(
                output=output,
                response=output,
                status="success"
            )
        
        # Handle "all" - clears the scope filter
        if args.lower() == 'all':
    # ... (truncated)
```

[!] WARNING (line 842)
Function "_execute_operation_locally" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
            return None, args.strip().strip('"').strip("'")
    
    def _execute_operation_locally(self, target: str, cli_args: str = "") -> str:
        """Execute a CLI operation locally and return its output.
        
        Args:
            target: CLI target (e.g., 'tests.build', 'tests.build.instructions', 'tests.build.submit')
            cli_args: CLI arguments like '--scope "X"'
        
        Returns:
            Output from the operation (instructions, submit result, confirm result, etc.)
        """
        # Parse target
        parts = target.split('.')
        if len(parts) < 2:
    # ... (truncated)
```

[!] WARNING (line 1133)
Function "_handle_dot_notation" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

```python
            pass
    
    def _handle_dot_notation(self, command: str) -> REPLCommandResponse:
        """Handle dot notation commands (behavior.action.operation)"""
        # Parse dot notation: behavior.action.operation or action.operation or .operation
        parts = command.split()
        dot_path = parts[0]
        args = ' '.join(parts[1:]) if len(parts) > 1 else ""
        
        path_parts = dot_path.split('.')
        
        # . alone means current position
        if dot_path == '.':
            return self._handle_current_command()
        
    # ... (truncated)
```

[!] WARNING (line 1329)
Function "_convert_repl_scope_to_cli_format" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
            return args_str.split()
    
    def _convert_repl_scope_to_cli_format(self, cli_args: list) -> list:
        import json
        converted_args = []
        i = 0
        while i < len(cli_args):
            arg = cli_args[i]
            if arg == '--scope' and i + 1 < len(cli_args):
                scope_value = cli_args[i + 1]
                if scope_value.startswith(('file:', 'files:')):
                    prefix = 'file:' if scope_value.startswith('file:') else 'files:'
                    paths = scope_value[len(prefix):].split(',')
                    paths = [p.strip() for p in paths if p.strip()]
                    json_scope = json.dumps({"type": "files", "value": paths})
    # ... (truncated)
```

---

## stop_writing_useless_comments
**action_context.py** - 28 violation(s)

[X] ERROR (line 26)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
@dataclass
class KnowledgeGraphFilter:
    """Filters content by knowledge graph nodes (stories, epics, increments).
    
    Used for filtering operations to specific parts of the story graph.
    """
    stories: List[str] = field(default_factory=list)
```

[X] ERROR (line 35)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def matches_story(self, story_name: str) -> bool:
        """Check if story matches filter."""
        if not self.stories:
```

[X] ERROR (line 41)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def matches_epic(self, epic_name: str) -> bool:
        """Check if epic matches filter."""
        if not self.epics:
```

[X] ERROR (line 47)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def filter_knowledge_graph(self, knowledge_graph: Dict[str, Any]) -> Dict[str, Any]:
        """Filter knowledge graph to only nodes matching this filter."""
        # For now, return full graph if no filters specified
```

[X] ERROR (line 57)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
@dataclass
class FileFilter:
    """Filters files by path patterns.
    
    Supports glob patterns for include/exclude.
    """
    include_patterns: List[str] = field(default_factory=list)
```

[X] ERROR (line 65)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def matches_file(self, file_path: Path) -> bool:
        """Check if file matches the filter."""
        if not self.include_patterns:
```

[X] ERROR (line 76)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def filter_files(self, file_list: List[Path]) -> List[Path]:
        """Filter file list to only files matching this filter."""
        if not self.include_patterns and not self.exclude_patterns:
```

[X] ERROR (line 127)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
@dataclass
class Scope:
    """Scope for filtering bot operations to specific content.
    
    Uses KnowledgeGraphFilter for story/epic/increment scoping
    and FileFilter for file-based scoping. Maintains backward compatibility
    with type/value/exclude API.
    
    The Scope object is responsible for its own persistence to the bot state file.
    """
    type: ScopeType = ScopeType.ALL
```

[X] ERROR (line 145)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __post_init__(self):
        """Initialize filter objects from type/value/exclude."""
        # Create knowledge graph filter for story/epic/increment types
```

[X] ERROR (line 166)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def knowledge_graph_filter(self) -> Optional[KnowledgeGraphFilter]:
        """Get knowledge graph filter (lazy init if needed)."""
        return self._knowledge_graph_filter
```

[X] ERROR (line 171)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def file_filter(self) -> Optional[FileFilter]:
        """Get file filter (lazy init if needed)."""
        return self._file_filter
```

[X] ERROR (line 175)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def filters_knowledge_graph(self, knowledge_graph: Dict[str, Any]) -> Dict[str, Any]:
        """Filter knowledge graph using knowledge graph filter."""
        if self._knowledge_graph_filter:
```

[X] ERROR (line 181)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def filters_files(self, file_list: List[Path]) -> List[Path]:
        """Filter file list using file filter."""
        if self._file_filter:
```

[X] ERROR (line 213)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def apply_to_bot(self, workspace_directory: 'Path') -> None:
        """Clear old scope and store this scope to the bot state file.
        
        The Scope object is responsible for its own persistence.
        """
        import json
```

[X] ERROR (line 238)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @staticmethod
    def clear_from_bot(workspace_directory: 'Path') -> None:
        """Remove scope from the bot state file."""
        import json
```

[X] ERROR (line 255)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @staticmethod
    def _get_state_file_path(workspace_directory: 'Path') -> 'Path':
        """Get path to the bot state file."""
        return workspace_directory / 'behavior_action_state.json'
```

[X] ERROR (line 259)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def to_display_lines(self, workspace_directory: 'Path') -> List[str]:
        """Render scope as display lines with hierarchical expansion.
        
        Returns plain text lines showing scope filter and matched items.
        """
        from pathlib import Path
```

[X] ERROR (line 311)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _expand_file_paths(self, workspace_directory: 'Path') -> List['Path']:
        """Expand file scope paths to actual files that will be scanned."""
        from pathlib import Path
```

[X] ERROR (line 353)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _find_scope_matches_in_graph(self, graph_data: Dict[str, Any], scope_values: List[str]) -> List[str]:
        """Find and display scope matches from story graph."""
        lines = []
```

[X] ERROR (line 367)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _search_for_scope_match(self, epics: List[Dict], scope_val: str) -> Optional[List[str]]:
        """Search for scope match and return formatted lines with full hierarchy."""
        for epic in epics:
```

[X] ERROR (line 379)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _search_sub_epics(self, sub_epics: List[Dict], scope_val: str) -> Optional[List[str]]:
        """Search sub-epics for scope match."""
        for sub_epic in sub_epics:
```

[X] ERROR (line 391)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _search_stories(self, sub_epic: Dict, scope_val: str) -> Optional[List[str]]:
        """Search stories for scope match."""
        for story_group in sub_epic.get('story_groups', []):
```

[X] ERROR (line 404)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _matches_name(self, name: str, pattern: str) -> bool:
        """Check if pattern matches name (case-insensitive)."""
        return pattern.lower() in name.lower()
```

[X] ERROR (line 408)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _format_node_with_children(self, node: Dict[str, Any], node_type: str, indent: int) -> List[str]:
        """Format a node and its children recursively."""
        lines = []
```

[X] ERROR (line 466)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def __post_init__(self):
        """Normalize strategy context fields and keep backward compatibility."""
        # Default collections to empty to simplify downstream checks
```

[X] ERROR (line 477)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_decisions(self) -> Dict[str, Any]:
        """Get all decision attributes (exclude assumption fields and internals)."""
        excluded = {'assumptions', 'assumptions_made', 'decisions_made'}
```

[X] ERROR (line 488)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def assumptions_list(self) -> Optional[List[str]]:
        """Alias to keep existing code using context.assumptions working."""
        return self.assumptions or self.assumptions_made
```

[X] ERROR (line 324)
Useless comment: "# Handle glob patterns" - delete it or improve the code instead

```python
            
            if has_glob:
                # Handle glob patterns
                # If not absolute, make it relative to workspace
```

---

## stop_writing_useless_comments
**repl_session.py** - 31 violation(s)

[X] ERROR (line 145)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def display_current_state(self, full=False) -> REPLStateDisplay:
        """Single source of truth for displaying current bot state.
        
        Returns REPLStateDisplay with formatted status output showing:
        - Bot name and paths
        - Current position header
        - Scope filter (if set)
        - Progress in workflow
        - Hierarchical behavior/action/operation tree
        """
        if not self.has_current_action:
```

[X] ERROR (line 260)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_context_header_for_ai(self) -> str:
        """Get status display as a string for AI context headers.
        
        This is a convenience method that extracts just the output string
        from display_current_state().
        """
        state_display = self.display_current_state()
```

[X] ERROR (line 269)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _convert_domain_result_to_repl_response(self, result: Dict[str, Any], command: str) -> REPLCommandResponse:
        """Convert a domain method result to a REPL response.
        
        Args:
            result: Dict returned from domain method
            command: The command that was executed
        
        Returns:
            REPLCommandResponse with appropriate formatting
        """
        status = result.get('status', 'success')
```

[X] ERROR (line 400)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_help_command(self, args: str = "") -> REPLCommandResponse:
        """Handle help command using bot.help"""
        if not args:
```

[X] ERROR (line 430)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_status_command(self) -> REPLCommandResponse:
        """Handle status command using bot.status"""
        state_display = self.display_current_state(full=True)
```

[X] ERROR (line 439)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_current_command(self) -> REPLCommandResponse:
        """Re-execute current operation based on progress state"""
        if not self.has_current_action:
```

[X] ERROR (line 468)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_next_command(self) -> REPLCommandResponse:
        """Handle next/advance navigation"""
        if not self.has_current_action:
```

[X] ERROR (line 504)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_back_command(self) -> REPLCommandResponse:
        """Handle back/previous navigation"""
        if not self.has_current_action:
```

[X] ERROR (line 550)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_instructions_command(self, args: str = "") -> REPLCommandResponse:
        """Handle instructions command"""
        import sys
```

[X] ERROR (line 607)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_submit_command(self, args: str = "") -> REPLCommandResponse:
        """Handle submit command"""
        if not self.has_current_action:
```

[X] ERROR (line 628)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_confirm_command(self) -> REPLCommandResponse:
        """Handle confirm command"""
        if not self.has_current_action:
```

[X] ERROR (line 683)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_path_command(self, args: str = "") -> REPLCommandResponse:
        """Handle path/workspace command"""
        if not args:
```

[X] ERROR (line 702)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_scope_command(self, args: str = "") -> REPLCommandResponse:
        """Handle scope command"""
        if not args:
```

[X] ERROR (line 768)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _validate_headless_ready(self, args: str) -> tuple[bool, REPLCommandResponse | None, any]:
        """Validate that headless mode is ready to execute.
        
        Returns:
            Tuple of (is_valid, error_response, config)
            - If is_valid is False, error_response contains the error to return
            - If is_valid is True, config contains the loaded configuration
        """
        from agile_bot.bots.base_bot.src.repl_cli.headless.headless_config import HeadlessConfig
```

[X] ERROR (line 809)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _parse_headless_args(self, args: str) -> tuple[str | None, str]:
        """Parse headless command args into target and message.
        
        Args:
            args: Raw argument string (e.g., 'test.build "message" --scope "X"')
        
        Returns:
            Tuple of (target, message) where:
            - target is the CLI target (e.g., 'test.build') or None
            - message is the rest (message + CLI args)
        """
        import shlex
```

[X] ERROR (line 843)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _execute_operation_locally(self, target: str, cli_args: str = "") -> str:
        """Execute a CLI operation locally and return its output.
        
        Args:
            target: CLI target (e.g., 'tests.build', 'tests.build.instructions', 'tests.build.submit')
            cli_args: CLI arguments like '--scope "X"'
        
        Returns:
            Output from the operation (instructions, submit result, confirm result, etc.)
        """
        # Parse target
```

[X] ERROR (line 904)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _prepare_headless_message(self, target: str | None, message: str) -> str:
        """Prepare the final message for headless execution.
        
        If a target is provided (behavior.action), gets instructions and combines with message.
        
        Args:
            target: Optional CLI target (e.g., 'tests.build')
            message: User message (may include CLI args like --scope)
        
        Returns:
            Final message to send to headless session
        """
        if target:
```

[X] ERROR (line 952)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _format_headless_result(self, execution_result) -> REPLCommandResponse:
        """Format headless execution result as a REPL response.
        
        Args:
            execution_result: Result from HeadlessSession.invokes()
        
        Returns:
            REPLCommandResponse with formatted output
        """
        output_lines = [
```

[X] ERROR (line 979)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_headless_command(self, args: str = "") -> REPLCommandResponse:
        """Handle headless command - execute instruction in headless mode"""
        from agile_bot.bots.base_bot.src.repl_cli.headless.headless_session import HeadlessSession
```

[X] ERROR (line 1024)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_behavior_command(self, behavior_name: str) -> REPLCommandResponse:
        """Handle behavior navigation"""
        behavior = self.cli_bot.behaviors.domain_behaviors.find_by_name(behavior_name)
```

[X] ERROR (line 1053)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def navigate_to_behavior_action(self, behavior_name: str, action_name: str):
        """Navigate to a specific behavior and action
        
        Raises:
            ValueError: If behavior or action not found
        """
        # Navigate to behavior
```

[X] ERROR (line 1074)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _wrap_navigation_with_instructions(self) -> REPLCommandResponse:
        """After navigation, auto-execute instructions for new position"""
        return self._handle_instructions_command()
```

[X] ERROR (line 1078)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _wrap_with_context_header(self, content: str, response_msg: str) -> REPLCommandResponse:
        """Wrap content with instructions header and CLI status section"""
        formatter = self.formatter
```

[X] ERROR (line 1119)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _mark_behavior_complete(self, behavior_name: str) -> None:
        """Mark a behavior as complete in the state file"""
        state_file = self.workspace_directory / 'behavior_action_state.json'
```

[X] ERROR (line 1134)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_dot_notation(self, command: str) -> REPLCommandResponse:
        """Handle dot notation commands (behavior.action.operation)"""
        # Parse dot notation: behavior.action.operation or action.operation or .operation
```

[X] ERROR (line 210)
Useless comment: "# Get scope display" - delete it or improve the code instead

```python
        lines.append(formatter.subsection_separator())
        
        # Get scope display
        scope_display = self.cli_bot.get_scope_display()
```

[X] ERROR (line 757)
Useless comment: "# Get the scope display lines" - delete it or improve the code instead

```python
        result = self.cli_bot.set_scope(scope)
        
        # Get the scope display lines
        output = self.cli_bot.get_scope_display()
```

[X] ERROR (line 938)
Useless comment: "# Execute the target operation locally to get output" - delete it or improve the code instead

```python
            cli_args = ' '.join(cli_args_parts)
            
            # Execute the target operation locally to get output
            operation_output = self._execute_operation_locally(target, cli_args)
```

[X] ERROR (line 991)
Useless comment: "# Execute in headless mode" - delete it or improve the code instead

```python
        target, message = self._parse_headless_args(args)
        
        # Execute in headless mode
        try:
```

[X] ERROR (line 1005)
Useless comment: "# Execute in headless mode" - delete it or improve the code instead

```python
                final_message = message
            
            # Execute in headless mode
            execution_result = session.invokes(message=final_message, context_file=None)
```

[X] ERROR (line 1060)
Useless comment: "# Get the behavior" - delete it or improve the code instead

```python
        # Navigate to behavior
        self.cli_bot.behaviors.domain_behaviors.navigate_to(behavior_name)
        # Get the behavior
        behavior = self.cli_bot.behaviors.domain_behaviors.find_by_name(behavior_name)
```

---

## stop_writing_useless_comments
**rules.py** - 3 violation(s)

[X] ERROR (line 70)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @classmethod
    def _get_files_for_validation(cls, behavior, context: 'ValidateActionContext') -> Dict[str, List[Path]]:
        """Get files to validate based on behavior and scope."""
        from agile_bot.bots.base_bot.src.actions.validate.file_discovery import FileDiscovery
```

[X] ERROR (line 48)
Useless comment: "# Get files - either from scope filter or discover all" - delete it or improve the code instead

```python
            knowledge_graph_content = validation_scope.filter_story_graph(knowledge_graph_content)
        
        # Get files - either from scope filter or discover all
        files = cls._get_files_for_validation(behavior, context)
```

[X] ERROR (line 222)
Useless comment: "# Load bot-level rules" - delete it or improve the code instead

```python
        all_rules = []
        
        # Load bot-level rules
        bot_rules = self._rule_loader.load_bot_rules()
```

---

## use_clear_function_parameters
**rules.py** - 5 violation(s)

[!] WARNING (line 345)
Function "_process_scanner_result" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
            return data

    def _process_scanner_result(self, rule, rule_result: dict, scanner_results: Any, scanner_path: str, scanner_name: str, logger) -> str:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        execution_status = rule.scanner_execution_status or 'SUCCESS'
    # ... (truncated)
```

[!] WARNING (line 361)
Function "_execute_scanner" has 9 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return f'  [OK] {rule.rule_file}: Scanner executed successfully ({violations_count} violations)'

    def _execute_scanner(self, rule, rule_result: dict, context: ValidationContext, scanner_path: str, logger, files: Dict, changed_files: Dict, all_files: Dict) -> str:
        scanner_name = scanner_path.split('.')[-1] if '.' in scanner_path else scanner_path
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # ... (truncated)
```

[!] WARNING (line 382)
Function "_process_rule" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
            raise

    def _process_rule(self, rule, rule_result: dict, context: ValidationContext, logger, files: Dict, changed_files: Dict, all_files: Dict) -> str:
        scanner_path = rule.scanner_path
        if not scanner_path:
    # ... (truncated)
```

[!] WARNING (line 394)
Function "validate" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return self._execute_scanner(rule, rule_result, context, scanner_path, logger, files, changed_files, all_files)

    def validate(self, context: ValidationContext, files: Optional[Dict[str, List[Path]]]=None, callbacks: Optional[ValidationCallbacks]=None, skiprule: Optional[List[str]]=None, exclude: Optional[List[str]]=None) -> List[Dict[str, Any]]:
        if isinstance(context, ValidationContext):
            return self._execute_validation(context)
    # ... (truncated)
```

[!] WARNING (line 399)
Function "_create_legacy_context" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return self._execute_validation(self._create_legacy_context(context, files, callbacks, skiprule, exclude))

    def _create_legacy_context(self, knowledge_graph: Dict, files: Optional[Dict], callbacks: Optional[ValidationCallbacks], skiprule: Optional[List[str]], exclude: Optional[List[str]]) -> ValidationContext:
        return ValidationContext(knowledge_graph=knowledge_graph, files=files or {}, callbacks=callbacks or ValidationCallbacks(), skiprule=skiprule or [], exclude=exclude or [], skip_cross_file=True, all_files=False, behavior=self.behavior, bot_paths=getattr(self, 'bot_paths', None), working_dir=Path.cwd())

```

---

## use_domain_language
**action_context.py** - 32 violation(s)

[i] INFO (line 16)
Class "ScopeType" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 25)
Class "KnowledgeGraphFilter" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 46)
Function "filter_knowledge_graph" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 46)
Function "filter_knowledge_graph" uses parameter name "knowledge_graph" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 126)
Class "Scope" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 144)
Function "__post_init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 165)
Function "knowledge_graph_filter" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 174)
Function "filters_knowledge_graph" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 174)
Function "filters_knowledge_graph" uses parameter name "knowledge_graph" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 187)
Function "from_dict" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 187)
Function "from_dict" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 204)
Function "to_dict" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 258)
Function "to_display_lines" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 352)
Function "_find_scope_matches_in_graph" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 352)
Function "_find_scope_matches_in_graph" uses parameter name "scope_values" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 366)
Function "_search_for_scope_match" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 366)
Function "_search_for_scope_match" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 378)
Function "_search_sub_epics" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 390)
Function "_search_stories" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 390)
Function "_search_stories" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 403)
Function "_matches_name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 403)
Function "_matches_name" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 403)
Function "_matches_name" uses parameter name "pattern" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 407)
Function "_format_node_with_children" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 407)
Function "_format_node_with_children" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 407)
Function "_format_node_with_children" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 407)
Function "_format_node_with_children" uses parameter name "indent" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 465)
Function "__post_init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 476)
Function "get_decisions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 487)
Function "assumptions_list" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 492)
Function "assumptions_list" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 505)
Function "__post_init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**repl_session.py** - 73 violation(s)

[i] INFO (line 17)
Class "REPLSession" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 18)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 82)
Function "set_action_phase" uses parameter name "phase" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 96)
Function "stage_name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 120)
Function "detect_tty" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 127)
Function "get_progress_line" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 144)
Function "display_current_state" uses parameter name "full" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 259)
Function "get_context_header_for_ai" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 268)
Function "_convert_domain_result_to_repl_response" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 268)
Function "_convert_domain_result_to_repl_response" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 326)
Function "read_and_execute_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 326)
Function "read_and_execute_command" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 339)
Function "_handle_simple_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 339)
Function "_handle_simple_command" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 399)
Function "_handle_help_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 399)
Function "_handle_help_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 429)
Function "_handle_status_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 438)
Function "_handle_current_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 467)
Function "_handle_next_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 503)
Function "_handle_back_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 549)
Function "_handle_instructions_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 549)
Function "_handle_instructions_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 606)
Function "_handle_submit_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 606)
Function "_handle_submit_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 627)
Function "_handle_confirm_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 682)
Function "_handle_path_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 701)
Function "_handle_scope_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 701)
Function "_handle_scope_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 767)
Function "_validate_headless_ready" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 808)
Function "_parse_headless_args" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 808)
Function "_parse_headless_args" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 842)
Function "_execute_operation_locally" uses parameter name "target" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 842)
Function "_execute_operation_locally" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 903)
Function "_prepare_headless_message" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 903)
Function "_prepare_headless_message" uses parameter name "target" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 903)
Function "_prepare_headless_message" uses parameter name "message" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 951)
Function "_format_headless_result" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 951)
Function "_format_headless_result" uses parameter name "execution_result" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 978)
Function "_handle_headless_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 978)
Function "_handle_headless_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1073)
Function "_wrap_navigation_with_instructions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1077)
Function "_wrap_with_context_header" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1077)
Function "_wrap_with_context_header" uses parameter name "content" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1077)
Function "_wrap_with_context_header" uses parameter name "response_msg" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1133)
Function "_handle_dot_notation" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1133)
Function "_handle_dot_notation" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1261)
Function "_handle_action_shortcut" uses parameter name "args_str" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1322)
Function "_tokenize_cli_args" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1322)
Function "_tokenize_cli_args" uses parameter name "args_str" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1329)
Function "_convert_repl_scope_to_cli_format" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1329)
Function "_convert_repl_scope_to_cli_format" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1366)
Function "_execute_action_with_args" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1366)
Function "_execute_action_with_args" uses parameter name "operation" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1440)
Function "display_confirm_prompt" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1465)
Function "parse_command_parameters" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1479)
Function "parse_scope_from_string" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1479)
Function "parse_scope_from_string" uses parameter name "scope_str" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1488)
Function "get_stored_scope" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1498)
Function "_get_scope_display_lines" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1522)
Function "_find_scope_matches" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1522)
Function "_find_scope_matches" uses parameter name "scope_values" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1535)
Function "_search_for_scope_match" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1535)
Function "_search_for_scope_match" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1546)
Function "_search_sub_epics" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1557)
Function "_search_stories" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1557)
Function "_search_stories" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1569)
Function "_matches_name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1569)
Function "_matches_name" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1569)
Function "_matches_name" uses parameter name "pattern" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1572)
Function "_format_node_with_children" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1572)
Function "_format_node_with_children" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1572)
Function "_format_node_with_children" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1572)
Function "_format_node_with_children" uses parameter name "indent" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**rules.py** - 36 violation(s)

[i] INFO (line 39)
Function "from_action_context" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 39)
Function "from_action_context" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 69)
Function "_get_files_for_validation" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 69)
Function "_get_files_for_validation" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 112)
Function "from_parameters" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 151)
Function "get_last_report_timestamp" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 197)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 234)
Function "find_by_name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 241)
Function "__iter__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 246)
Function "__len__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 249)
Function "add_violations" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 249)
Function "add_violations" uses parameter name "violations" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 253)
Function "violations" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 257)
Function "violation_summary" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 309)
Function "_has_scanner_error" uses parameter name "execution_status" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 319)
Function "_extract_error_message" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 319)
Function "_extract_error_message" uses parameter name "execution_status" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 331)
Function "_flush_logger_handlers" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 331)
Function "_flush_logger_handlers" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 335)
Function "_convert_violations_to_dicts" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 345)
Function "_process_scanner_result" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 361)
Function "_execute_scanner" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 361)
Function "_execute_scanner" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 382)
Function "_process_rule" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 382)
Function "_process_rule" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 394)
Function "validate" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 394)
Function "validate" uses parameter name "exclude" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 399)
Function "_create_legacy_context" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 399)
Function "_create_legacy_context" uses parameter name "knowledge_graph" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 399)
Function "_create_legacy_context" uses parameter name "exclude" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 402)
Function "_execute_validation" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 408)
Function "_log_validation_start" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 408)
Function "_log_validation_start" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 423)
Function "_process_all_rules" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 423)
Function "_process_all_rules" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 449)
Function "_log_scanner_status_summary" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

Completed: 2025-12-30 03:01:16
Total violations: 251
Scanners executed: 30
