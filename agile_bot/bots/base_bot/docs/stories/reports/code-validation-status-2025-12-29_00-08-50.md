# Validation Status - code
Started: 2025-12-29 00:08:50
Files: 265

## avoid_excessive_guards
**repl_session.py** - 1 violation(s)

[!] WARNING (line 1109)
Line 1109: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

```python
    def parse_command_parameters(self, args: str) -> Dict[str, Any]:
        params = {}
        if not args:
            return params
        
```

---

## avoid_excessive_guards
**cli_bot.py** - 2 violation(s)

[!] WARNING (line 44)
Line 44: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def help(self) -> REPLHelp:
        if self._help is None:
            self._help = REPLHelp(self._bot)
        return self._help
```

[!] WARNING (line 50)
Line 50: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

```python
    @property
    def status(self) -> REPLStatus:
        if self._status is None:
            self._status = REPLStatus(self, self._session, self._session.formatter)
        return self._status
```

---

## avoid_excessive_guards
**markdown_formatter.py** - 2 violation(s)

[!] WARNING (line 15)
Line 15: Variable truthiness check detected (if is_completed:). Assume variable exists - let code fail fast if missing.

```python
    
    def status_marker(self, is_current: bool, is_completed: bool) -> str:
        if is_completed:
            return "- ☑"
        elif is_current:
            return "- ➤"
        else:
            return "- ☐"
    
```

[!] WARNING (line 17)
Line 17: Variable truthiness check detected (if is_current:). Assume variable exists - let code fail fast if missing.

```python
        if is_completed:
            return "- ☑"
        elif is_current:
            return "- ➤"
        else:
            return "- ☐"
    
```

---

## avoid_unnecessary_parameter_passing
**render_action.py** - 2 violation(s)

[!] WARNING (line 50)
Instance property "self._render_specs" is extracted to variable "render_specs" and passed to internal method "_execute_synchronizers". Access via self._render_specs directly instead.

[!] WARNING (line 84)
Instance property "self._render_specs" is extracted to variable "render_specs" and passed to internal method "_execute_synchronizers". Access via self._render_specs directly instead.

---

## eliminate_duplication
**repl_session.py** - 2 violation(s)

[X] ERROR (line 192)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (display_current_state:192-205):
```python
lines.append(str(self.workspace_directory))
lines.append('```')
lines.append('')
lines.append('To change path:')
lines.append('```')
lines.append('path demo/mob_minion              # Change to specifi...
```

Location (display_current_state:220-228):
```python
lines.append(formatter.subsection_separator())
lines.append(f'## {formatter.position_icon()} **Progress**')
lines.append('**Current Position:**')
lines.append('```')
lines.append(f'{self.progress_path...
```

[X] ERROR (line 449)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_handle_next_command:449-468):
```python
if not self.has_current_action:
    return REPLCommandResponse(output='ERROR: No current action', response='ERROR: No current action', status='error')
behavior = self.current_behavior
if not behavior:...
```

Location (_handle_back_command:485-504):
```python
if not self.has_current_action:
    return REPLCommandResponse(output='ERROR: No current action', response='ERROR: No current action', status='error')
behavior = self.current_behavior
if not behavior:...
```

---

## eliminate_duplication
**render_action.py** - 1 violation(s)

[X] ERROR (line 46)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_prepare_instructions:46-61):
```python
render_instructions = self._config_loader.load_render_instructions()
render_specs = self._render_specs
self._execute_synchronizers(render_specs)
merged_instructions = MergedInstructions(base_instructi...
```

Location (do_execute:82-88):
```python
render_instructions = self._config_loader.load_render_instructions()
render_specs = self._render_specs
self._execute_synchronizers(render_specs)
instructions = MergedInstructions(base_instructions=sel...
```

---

## eliminate_duplication
**output_formatter.py** - 1 violation(s)

[X] ERROR (line 16)
Duplicate code detected: functions status_marker, list_item, highlight have identical bodies - extract to shared function

---


## Cross-File Duplication Analysis
Scanning 13 changed file(s) against 265 total files...
Extracted 854 changed blocks, 4079 reference blocks
Starting 3,483,466 pairwise comparisons...
Comparing: 0% (30,436/3,483,466) - 0 violations - ETA: 1134s  
Comparing: 1% (58,102/3,483,466) - 0 violations - ETA: 1179s  
Comparing: 2% (90,287/3,483,466) - 0 violations - ETA: 1127s  
Comparing: 3% (112,444/3,483,466) - 0 violations - ETA: 1199s  
Comparing: 3% (130,767/3,483,466) - 0 violations - ETA: 1282s  
Comparing: 4% (158,758/3,483,466) - 0 violations - ETA: 1256s  
Comparing: 5% (183,316/3,483,466) - 0 violations - ETA: 1260s  
Comparing: 5% (204,289/3,483,466) - 0 violations - ETA: 1284s  
Comparing: 6% (221,831/3,483,466) - 0 violations - ETA: 1323s  
Comparing: 6% (237,480/3,483,466) - 0 violations - ETA: 1366s  
Comparing: 7% (251,789/3,483,466) - 0 violations - ETA: 1411s  
Comparing: 7% (276,563/3,483,466) - 0 violations - ETA: 1391s  
Comparing: 8% (294,664/3,483,466) - 0 violations - ETA: 1406s  
Comparing: 8% (309,945/3,483,466) - 0 violations - ETA: 1433s  
Comparing: 9% (340,214/3,483,466) - 0 violations - ETA: 1385s  
Comparing: 10% (369,366/3,483,466) - 0 violations - ETA: 1349s  
Comparing: 11% (411,612/3,483,466) - 0 violations - ETA: 1268s  
Comparing: 12% (443,432/3,483,466) - 0 violations - ETA: 1234s  
Comparing: 13% (467,557/3,483,466) - 0 violations - ETA: 1225s  
Comparing: 14% (507,385/3,483,466) - 0 violations - ETA: 1173s  
Comparing: 15% (536,486/3,483,466) - 0 violations - ETA: 1153s  
Comparing: 16% (570,240/3,483,466) - 0 violations - ETA: 1124s  
Comparing: 17% (600,058/3,483,466) - 0 violations - ETA: 1105s  
Comparing: 18% (629,169/3,483,466) - 0 violations - ETA: 1088s  
Comparing: 18% (656,497/3,483,466) - 0 violations - ETA: 1076s  
Comparing: 19% (680,334/3,483,466) - 0 violations - ETA: 1071s  
Comparing: 20% (703,596/3,483,466) - 0 violations - ETA: 1066s  
Comparing: 20% (726,389/3,483,466) - 0 violations - ETA: 1062s  
Comparing: 21% (752,639/3,483,466) - 0 violations - ETA: 1052s  
Comparing: 22% (775,890/3,483,466) - 0 violations - ETA: 1046s  
Comparing: 23% (801,473/3,483,466) - 0 violations - ETA: 1037s  
Comparing: 23% (820,435/3,483,466) - 0 violations - ETA: 1038s  
Comparing: 24% (840,318/3,483,466) - 0 violations - ETA: 1038s  
Comparing: 24% (862,165/3,483,466) - 0 violations - ETA: 1033s  
Comparing: 25% (878,884/3,483,466) - 0 violations - ETA: 1037s  
Comparing: 25% (895,524/3,483,466) - 0 violations - ETA: 1040s  
Comparing: 26% (914,419/3,483,466) - 0 violations - ETA: 1039s  
Comparing: 26% (930,426/3,483,466) - 0 violations - ETA: 1042s  
Comparing: 27% (948,494/3,483,466) - 0 violations - ETA: 1042s  
Comparing: 27% (971,351/3,483,466) - 0 violations - ETA: 1034s  
Comparing: 28% (993,622/3,483,466) - 0 violations - ETA: 1027s  
Comparing: 29% (1,029,478/3,483,466) - 0 violations - ETA: 1001s  
Comparing: 30% (1,050,821/3,483,466) - 0 violations - ETA: 995s  
Comparing: 31% (1,084,824/3,483,466) - 8 violations - ETA: 972s  
Found 10 violations so far...
Comparing: 31% (1,107,549/3,483,466) - 12 violations - ETA: 965s  
Comparing: 32% (1,147,830/3,483,466) - 12 violations - ETA: 936s  
Comparing: 34% (1,187,534/3,483,466) - 12 violations - ETA: 908s  
Comparing: 35% (1,219,292/3,483,466) - 12 violations - ETA: 891s  
Comparing: 35% (1,244,809/3,483,466) - 12 violations - ETA: 881s  
Comparing: 36% (1,282,501/3,483,466) - 12 violations - ETA: 858s  
Comparing: 37% (1,319,530/3,483,466) - 12 violations - ETA: 836s  
Comparing: 38% (1,350,937/3,483,466) - 12 violations - ETA: 820s  
Comparing: 39% (1,390,709/3,483,466) - 12 violations - ETA: 797s  
Comparing: 40% (1,420,499/3,483,466) - 12 violations - ETA: 784s  
Comparing: 41% (1,450,209/3,483,466) - 12 violations - ETA: 771s  
Comparing: 42% (1,489,942/3,483,466) - 12 violations - ETA: 749s  
Comparing: 43% (1,508,454/3,483,466) - 12 violations - ETA: 746s  
Comparing: 44% (1,539,680/3,483,466) - 12 violations - ETA: 732s  
Comparing: 45% (1,579,628/3,483,466) - 12 violations - ETA: 711s  
Comparing: 45% (1,597,946/3,483,466) - 12 violations - ETA: 708s  
Comparing: 46% (1,616,310/3,483,466) - 12 violations - ETA: 704s  
Comparing: 47% (1,646,721/3,483,466) - 12 violations - ETA: 691s  
Comparing: 48% (1,674,788/3,483,466) - 12 violations - ETA: 680s  
Comparing: 48% (1,695,744/3,483,466) - 12 violations - ETA: 674s  
Comparing: 49% (1,724,850/3,483,466) - 12 violations - ETA: 662s  
Comparing: 50% (1,745,435/3,483,466) - 12 violations - ETA: 657s  
Comparing: 50% (1,769,744/3,483,466) - 12 violations - ETA: 648s  
Comparing: 51% (1,788,137/3,483,466) - 12 violations - ETA: 644s  
Comparing: 51% (1,805,854/3,483,466) - 12 violations - ETA: 641s  
Comparing: 52% (1,834,192/3,483,466) - 12 violations - ETA: 629s  
Comparing: 53% (1,858,342/3,483,466) - 12 violations - ETA: 620s  
Comparing: 53% (1,880,989/3,483,466) - 12 violations - ETA: 613s  
Comparing: 54% (1,900,061/3,483,466) - 12 violations - ETA: 608s  
Comparing: 55% (1,918,712/3,483,466) - 12 violations - ETA: 603s  
Comparing: 55% (1,934,090/3,483,466) - 12 violations - ETA: 600s  
Comparing: 55% (1,950,411/3,483,466) - 12 violations - ETA: 597s  
Comparing: 56% (1,965,558/3,483,466) - 12 violations - ETA: 594s  
Comparing: 56% (1,979,376/3,483,466) - 12 violations - ETA: 592s  
Comparing: 57% (1,993,228/3,483,466) - 12 violations - ETA: 590s  
Comparing: 57% (2,005,236/3,483,466) - 12 violations - ETA: 589s  
Comparing: 58% (2,025,302/3,483,466) - 12 violations - ETA: 583s  
Comparing: 58% (2,041,761/3,483,466) - 12 violations - ETA: 579s  
Comparing: 59% (2,064,116/3,483,466) - 12 violations - ETA: 570s  
Comparing: 59% (2,082,754/3,483,466) - 12 violations - ETA: 564s  
Comparing: 60% (2,106,243/3,483,466) - 12 violations - ETA: 555s  
Comparing: 60% (2,122,729/3,483,466) - 12 violations - ETA: 551s  
Comparing: 61% (2,142,697/3,483,466) - 12 violations - ETA: 544s  
Comparing: 62% (2,165,063/3,483,466) - 12 violations - ETA: 535s  
Comparing: 62% (2,185,737/3,483,466) - 12 violations - ETA: 528s  
Comparing: 63% (2,211,736/3,483,466) - 12 violations - ETA: 517s  
Comparing: 64% (2,237,686/3,483,466) - 12 violations - ETA: 506s  
Comparing: 64% (2,260,609/3,483,466) - 12 violations - ETA: 497s  
Comparing: 65% (2,280,428/3,483,466) - 12 violations - ETA: 490s  
Comparing: 66% (2,299,834/3,483,466) - 12 violations - ETA: 483s  
Comparing: 66% (2,317,602/3,483,466) - 12 violations - ETA: 477s  
Comparing: 67% (2,334,727/3,483,466) - 12 violations - ETA: 472s  
Comparing: 67% (2,351,289/3,483,466) - 12 violations - ETA: 467s  
Comparing: 67% (2,366,694/3,483,466) - 12 violations - ETA: 462s  
Comparing: 68% (2,380,701/3,483,466) - 12 violations - ETA: 458s  
Comparing: 68% (2,398,893/3,483,466) - 12 violations - ETA: 452s  
Comparing: 69% (2,434,020/3,483,466) - 12 violations - ETA: 435s  
Comparing: 70% (2,453,084/3,483,466) - 12 violations - ETA: 428s  
Comparing: 70% (2,469,630/3,483,466) - 12 violations - ETA: 422s  
Comparing: 71% (2,483,758/3,483,466) - 12 violations - ETA: 418s  
Comparing: 71% (2,495,034/3,483,466) - 12 violations - ETA: 415s  
Comparing: 71% (2,508,020/3,483,466) - 12 violations - ETA: 412s  
Comparing: 72% (2,523,833/3,483,466) - 12 violations - ETA: 406s  
Comparing: 73% (2,546,602/3,483,466) - 12 violations - ETA: 397s  
Comparing: 73% (2,566,554/3,483,466) - 12 violations - ETA: 389s  
Comparing: 74% (2,589,173/3,483,466) - 12 violations - ETA: 379s  
Comparing: 74% (2,608,538/3,483,466) - 12 violations - ETA: 372s  
Comparing: 75% (2,639,044/3,483,466) - 12 violations - ETA: 358s  
Comparing: 76% (2,672,883/3,483,466) - 12 violations - ETA: 342s  
Comparing: 77% (2,707,546/3,483,466) - 12 violations - ETA: 326s  
Comparing: 78% (2,738,525/3,483,466) - 12 violations - ETA: 312s  
Comparing: 79% (2,765,648/3,483,466) - 12 violations - ETA: 301s  
Comparing: 80% (2,789,799/3,483,466) - 12 violations - ETA: 290s  
Comparing: 80% (2,813,412/3,483,466) - 12 violations - ETA: 281s  
Comparing: 81% (2,838,882/3,483,466) - 12 violations - ETA: 270s  
Comparing: 82% (2,877,568/3,483,466) - 12 violations - ETA: 252s  
Comparing: 83% (2,908,929/3,483,466) - 12 violations - ETA: 238s  
Comparing: 84% (2,937,163/3,483,466) - 13 violations - ETA: 226s  
Comparing: 85% (2,968,681/3,483,466) - 13 violations - ETA: 213s  
Comparing: 86% (2,998,974/3,483,466) - 17 violations - ETA: 200s  
Found 20 violations so far...
Comparing: 86% (3,025,319/3,483,466) - 27 violations - ETA: 189s  
Found 30 violations so far...
Comparing: 87% (3,048,067/3,483,466) - 33 violations - ETA: 179s  
Comparing: 88% (3,068,202/3,483,466) - 35 violations - ETA: 171s  
Comparing: 88% (3,087,200/3,483,466) - 35 violations - ETA: 164s  
Comparing: 89% (3,104,328/3,483,466) - 35 violations - ETA: 157s  
Found 40 violations so far...
Comparing: 89% (3,128,058/3,483,466) - 44 violations - ETA: 147s  
Comparing: 90% (3,147,884/3,483,466) - 48 violations - ETA: 139s  
Found 50 violations so far...
Comparing: 90% (3,164,505/3,483,466) - 55 violations - ETA: 133s  
Found 60 violations so far...
Comparing: 91% (3,180,380/3,483,466) - 67 violations - ETA: 126s  
Found 70 violations so far...
Comparing: 91% (3,196,741/3,483,466) - 74 violations - ETA: 120s  
Comparing: 92% (3,208,800/3,483,466) - 74 violations - ETA: 115s  
Comparing: 92% (3,225,328/3,483,466) - 78 violations - ETA: 108s  
Comparing: 93% (3,249,450/3,483,466) - 78 violations - ETA: 98s  
Comparing: 93% (3,268,116/3,483,466) - 78 violations - ETA: 90s  
Comparing: 94% (3,279,260/3,483,466) - 79 violations - ETA: 86s  
Comparing: 94% (3,288,063/3,483,466) - 79 violations - ETA: 83s  
Comparing: 95% (3,310,621/3,483,466) - 79 violations - ETA: 73s  
Comparing: 95% (3,337,456/3,483,466) - 79 violations - ETA: 62s  
Complete: 3360070 comparisons, 79 violations

## enforce_encapsulation
**repl_session.py** - 1 violation(s)

[!] WARNING (line 669)
Method "_handle_scope_command" in class "REPLSession" has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

---

## enforce_encapsulation
**validate_action.py** - 1 violation(s)

[!] WARNING (line 154)
Method "_format_rules_with_file_paths" in class "ValidateRulesAction" has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

---

## keep_classes_small_with_single_responsibility
**behaviors.py** - 1 violation(s)

[!] WARNING (line 16)
Class "Behaviors" is 380 lines - should be under 300 lines (extract related methods into separate classes)

```python
logger = logging.getLogger(__name__)

class Behaviors:

    def __init__(self, bot_name: str, bot_paths: BotPaths):
        self.bot_name = bot_name
        self.bot_paths = bot_paths
        self._behaviors: List['Behavior'] = []
        self._discover_behaviors()
        self._current_index: Optional[int] = None
    # ... (truncated)
```

---

## keep_classes_small_with_single_responsibility
**repl_session.py** - 1 violation(s)

[!] WARNING (line 17)
Class "REPLSession" is 1225 lines - should be under 300 lines (extract related methods into separate classes)

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

## keep_classes_small_with_single_responsibility
**duplication_scanner.py** - 1 violation(s)

[!] WARNING (line 36)
Class "DuplicationScanner" is 1903 lines - should be under 300 lines (extract related methods into separate classes)

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

## keep_functions_small_focused
**behaviors.py** - 1 violation(s)

[!] WARNING (line 204)
Function "navigate_to" is 45 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return self.find_by_name(behavior_name) is not None

    def navigate_to(self, behavior_name: str):
        behavior = self.find_by_name(behavior_name)
        if behavior is None:
            raise ValueError(f"Behavior '{behavior_name}' not found")
        
        target_index = None
        for i, b in enumerate(self._behaviors):
            if b.name == behavior.name:
                target_index = i
                self._current_index = i
                break
        
        # When navigating to a behavior: mark all actions in previous behaviors as complete,
        # clear all actions in future behaviors
        if target_index is not None and self.bot_paths:
            workspace_dir = self.bot_paths.workspace_directory
            state_file = workspace_dir / 'behavior_action_state.json'
            
            import json
            if state_file.exists():
                state_data = json.loads(state_file.read_text(encoding='utf-8'))
            else:
                state_data = {}
            
            completed_actions = state_data.get('completed_actions', [])
            
            # Mark all actions in previous behaviors as complete
            for i in range(target_index):
                past_behavior = self._behaviors[i]
                for action_name in past_behavior.actions.names:
                    action_state = f"{self.bot_name}.{past_behavior.name}.{action_name}"
                    # Check if already completed
                    is_completed = any(a.get('action_state') == action_state for a in completed_actions if isinstance(a, dict))
                    if not is_completed:
                        from datetime import datetime
                        completed_actions.append({
                            'action_state': action_state,
                            'timestamp': datetime.now().isoformat()
                        })
            
            # Remove completed actions from future behaviors
            actions_to_remove = set()
            for i in range(target_index + 1, len(self._behaviors)):
                future_behavior = self._behaviors[i]
                for action_name in future_behavior.actions.names:
                    action_state = f"{self.bot_name}.{future_behavior.name}.{action_name}"
                    actions_to_remove.add(action_state)
            
    # ... (truncated)
```

---

## keep_functions_small_focused
**repl_session.py** - 1 violation(s)

[!] WARNING (line 144)
Function "display_current_state" is 69 lines - should be under 20 lines (extract complex logic to helper functions)

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
**duplication_scanner.py** - 3 violation(s)

[!] WARNING (line 108)
Function "scan_file" is 63 lines - should be under 20 lines (extract complex logic to helper functions)

```python
            logger.debug(f"Cache write failed for {file_path}: {e}")
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
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

[!] WARNING (line 1642)
Function "scan_cross_file" is 250 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        _safe_print("")  # Blank line after violations
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
        test_files: Optional[List[Path]] = None,
        code_files: Optional[List[Path]] = None,
        all_test_files: Optional[List[Path]] = None,
        all_code_files: Optional[List[Path]] = None,
        status_writer: Optional[Any] = None
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
        
        if len(changed_files) < len(all_files):
            _safe_print(f"\n[CROSS-FILE] Incremental scan: Checking {len(changed_files)} changed file(s) against {len(all_files)} total files...")
        else:
            _safe_print(f"\n[CROSS-FILE] Full scan: Scanning {len(all_files)} files for cross-file duplication...")
        import sys
        
        def write_status(msg: str):
            if status_writer and hasattr(status_writer, 'write_cross_file_progress'):
                try:
                    status_writer.write_cross_file_progress(msg)
                except Exception as e:
                    logger.debug(f'Could not write to status file: {type(e).__name__}: {e}')
        
        write_status(f"\n## Cross-File Duplication Analysis")
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
**rules.py** - 2 violation(s)

[!] WARNING (line 105)
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

[!] WARNING (line 225)
Function "formatted_rules_digest" is 24 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return '\n'.join(sections) if sections else 'No validation rules found.'

    def formatted_rules_digest(self) -> str:
        rules = self._load_rules()
        if not rules:
            return 'No validation rules found.'
        
        # Sort by priority (lower number = higher priority)
        rules = sorted(rules, key=lambda r: r.priority)
        
        lines = []
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
**behaviors.py** - 1 violation(s)

[i] INFO (line 204)
Function "navigate_to" is 57 lines - consider improving vertical density by declaring variables near usage

```python
        return self.find_by_name(behavior_name) is not None

    def navigate_to(self, behavior_name: str):
        behavior = self.find_by_name(behavior_name)
        if behavior is None:
            raise ValueError(f"Behavior '{behavior_name}' not found")
        
        target_index = None
        for i, b in enumerate(self._behaviors):
            if b.name == behavior.name:
    # ... (truncated)
```

---

## maintain_vertical_density
**repl_session.py** - 8 violation(s)

[i] INFO (line 144)
Function "display_current_state" is 98 lines - consider improving vertical density by declaring variables near usage

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

[i] INFO (line 252)
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

[i] INFO (line 323)
Function "_handle_simple_command" is 55 lines - consider improving vertical density by declaring variables near usage

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

[i] INFO (line 571)
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

[i] INFO (line 645)
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

[i] INFO (line 821)
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

[i] INFO (line 949)
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

[i] INFO (line 1017)
Function "_execute_action_with_args" is 65 lines - consider improving vertical density by declaring variables near usage

```python
            return args_str.split()
    
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

## maintain_vertical_density
**duplication_scanner.py** - 5 violation(s)

[i] INFO (line 108)
Function "scan_file" is 78 lines - consider improving vertical density by declaring variables near usage

```python
            logger.debug(f"Cache write failed for {file_path}: {e}")
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
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

[i] INFO (line 1584)
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

[i] INFO (line 1642)
Function "scan_cross_file" is 297 lines - consider improving vertical density by declaring variables near usage

```python
        _safe_print("")  # Blank line after violations
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
        test_files: Optional[List[Path]] = None,
        code_files: Optional[List[Path]] = None,
        all_test_files: Optional[List[Path]] = None,
        all_code_files: Optional[List[Path]] = None,
        status_writer: Optional[Any] = None
    # ... (truncated)
```

---

## never_swallow_exceptions
**repl_session.py** - 2 violation(s)

[X] ERROR (line 818)
Except block only contains pass at line 818 - exceptions must be logged or rethrown, never swallowed

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

[!] WARNING (line 1709)
Line 1709 contains magic number - replace with named constant

```python
                if file_size > 500_000:  # Skip files larger than 500KB
                    _safe_print(f"Skipping large file ({file_size/1024:.1f}KB): {file_path}")
                    continue
```

[!] WARNING (line 1778)
Line 1778 contains magic number - replace with named constant

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

[!] WARNING (line 1435)
Line 1435 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_ast_nodes_deep(self, node1: ast.AST, node2: ast.AST) -> float:
        if type(node1) != type(node2):
```

[!] WARNING (line 1435)
Line 1435 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_ast_nodes_deep(self, node1: ast.AST, node2: ast.AST) -> float:
        if type(node1) != type(node2):
```

[!] WARNING (line 1469)
Line 1469 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_assign_nodes(self, node1: ast.Assign, node2: ast.Assign) -> float:
        # Compare number of targets
```

[!] WARNING (line 1469)
Line 1469 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_assign_nodes(self, node1: ast.Assign, node2: ast.Assign) -> float:
        # Compare number of targets
```

[!] WARNING (line 1478)
Line 1478 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_augassign_nodes(self, node1: ast.AugAssign, node2: ast.AugAssign) -> float:
        if type(node1.op) != type(node2.op):
```

[!] WARNING (line 1478)
Line 1478 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_augassign_nodes(self, node1: ast.AugAssign, node2: ast.AugAssign) -> float:
        if type(node1.op) != type(node2.op):
```

[!] WARNING (line 1483)
Line 1483 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_call_nodes(self, node1: ast.Call, node2: ast.Call) -> float:
        arg_count1 = len(node1.args) + len(node1.keywords)
```

[!] WARNING (line 1483)
Line 1483 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_call_nodes(self, node1: ast.Call, node2: ast.Call) -> float:
        arg_count1 = len(node1.args) + len(node1.keywords)
```

[!] WARNING (line 1501)
Line 1501 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_assert_nodes(self, node1: ast.Assert, node2: ast.Assert) -> float:
        test_sim = self._compare_expr_structure(node1.test, node2.test)
```

[!] WARNING (line 1501)
Line 1501 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_assert_nodes(self, node1: ast.Assert, node2: ast.Assert) -> float:
        test_sim = self._compare_expr_structure(node1.test, node2.test)
```

[!] WARNING (line 1505)
Line 1505 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_return_nodes(self, node1: ast.Return, node2: ast.Return) -> float:
        if node1.value is None and node2.value is None:
```

[!] WARNING (line 1505)
Line 1505 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_return_nodes(self, node1: ast.Return, node2: ast.Return) -> float:
        if node1.value is None and node2.value is None:
```

[!] WARNING (line 1512)
Line 1512 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_if_nodes(self, node1: ast.If, node2: ast.If) -> float:
        test_sim = self._compare_expr_structure(node1.test, node2.test)
```

[!] WARNING (line 1512)
Line 1512 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_if_nodes(self, node1: ast.If, node2: ast.If) -> float:
        test_sim = self._compare_expr_structure(node1.test, node2.test)
```

[!] WARNING (line 1518)
Line 1518 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_for_nodes(self, node1: ast.For, node2: ast.For) -> float:
        body_sim = self._compare_ast_structures(node1.body, node2.body)
```

[!] WARNING (line 1518)
Line 1518 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_for_nodes(self, node1: ast.For, node2: ast.For) -> float:
        body_sim = self._compare_ast_structures(node1.body, node2.body)
```

[!] WARNING (line 1523)
Line 1523 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_while_nodes(self, node1: ast.While, node2: ast.While) -> float:
        test_sim = self._compare_expr_structure(node1.test, node2.test)
```

[!] WARNING (line 1523)
Line 1523 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_while_nodes(self, node1: ast.While, node2: ast.While) -> float:
        test_sim = self._compare_expr_structure(node1.test, node2.test)
```

[!] WARNING (line 1528)
Line 1528 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_with_nodes(self, node1: ast.With, node2: ast.With) -> float:
        if len(node1.items) != len(node2.items):
```

[!] WARNING (line 1528)
Line 1528 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_with_nodes(self, node1: ast.With, node2: ast.With) -> float:
        if len(node1.items) != len(node2.items):
```

[!] WARNING (line 1534)
Line 1534 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_try_nodes(self, node1: ast.Try, node2: ast.Try) -> float:
        body_sim = self._compare_ast_structures(node1.body, node2.body)
```

[!] WARNING (line 1534)
Line 1534 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_try_nodes(self, node1: ast.Try, node2: ast.Try) -> float:
        body_sim = self._compare_ast_structures(node1.body, node2.body)
```

[!] WARNING (line 1541)
Line 1541 uses numbered variable "node1" - use meaningful descriptive name

```python
    
    def _compare_raise_nodes(self, node1: ast.Raise, node2: ast.Raise) -> float:
        if node1.exc is None and node2.exc is None:
```

[!] WARNING (line 1541)
Line 1541 uses numbered variable "node2" - use meaningful descriptive name

```python
    
    def _compare_raise_nodes(self, node1: ast.Raise, node2: ast.Raise) -> float:
        if node1.exc is None and node2.exc is None:
```

[!] WARNING (line 1548)
Line 1548 uses numbered variable "expr1" - use meaningful descriptive name

```python
    
    def _compare_expr_structure(self, expr1: ast.expr, expr2: ast.expr) -> float:
        if type(expr1) != type(expr2):
```

[!] WARNING (line 1548)
Line 1548 uses numbered variable "expr2" - use meaningful descriptive name

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

[!] WARNING (line 1484)
Line 1484 uses numbered variable "arg_count1" - use meaningful descriptive name

```python
    def _compare_call_nodes(self, node1: ast.Call, node2: ast.Call) -> float:
        arg_count1 = len(node1.args) + len(node1.keywords)
        arg_count2 = len(node2.args) + len(node2.keywords)
```

[!] WARNING (line 1485)
Line 1485 uses numbered variable "arg_count2" - use meaningful descriptive name

```python
        arg_count1 = len(node1.args) + len(node1.keywords)
        arg_count2 = len(node2.args) + len(node2.keywords)
        
```

[!] WARNING (line 1494)
Line 1494 uses numbered variable "a1" - use meaningful descriptive name

```python
        arg_sims = []
        for a1, a2 in zip(node1.args, node2.args):
            arg_sims.append(self._compare_expr_structure(a1, a2))
```

[!] WARNING (line 1494)
Line 1494 uses numbered variable "a2" - use meaningful descriptive name

```python
        arg_sims = []
        for a1, a2 in zip(node1.args, node2.args):
            arg_sims.append(self._compare_expr_structure(a1, a2))
```

[!] WARNING (line 1840)
Line 1840 uses numbered variable "block1" - use meaningful descriptive name

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

[!] WARNING (line 1841)
Line 1841 uses numbered variable "block2" - use meaningful descriptive name

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

[!] WARNING (line 1893)
Line 1893 uses numbered variable "file1" - use meaningful descriptive name

```python
                    # Found duplicate across files
                    file1 = block1['file_path']
                    file2 = block2['file_path']
```

[!] WARNING (line 1894)
Line 1894 uses numbered variable "file2" - use meaningful descriptive name

```python
                    file1 = block1['file_path']
                    file2 = block2['file_path']
                    func1 = block1['func_name']
```

[!] WARNING (line 1895)
Line 1895 uses numbered variable "func1" - use meaningful descriptive name

```python
                    file2 = block2['file_path']
                    func1 = block1['func_name']
                    func2 = block2['func_name']
```

[!] WARNING (line 1896)
Line 1896 uses numbered variable "func2" - use meaningful descriptive name

```python
                    func1 = block1['func_name']
                    func2 = block2['func_name']
                    start1 = block1['start_line']
```

[!] WARNING (line 1897)
Line 1897 uses numbered variable "start1" - use meaningful descriptive name

```python
                    func2 = block2['func_name']
                    start1 = block1['start_line']
                    end1 = block1['end_line']
```

[!] WARNING (line 1898)
Line 1898 uses numbered variable "end1" - use meaningful descriptive name

```python
                    start1 = block1['start_line']
                    end1 = block1['end_line']
                    start2 = block2['start_line']
```

[!] WARNING (line 1899)
Line 1899 uses numbered variable "start2" - use meaningful descriptive name

```python
                    end1 = block1['end_line']
                    start2 = block2['start_line']
                    end2 = block2['end_line']
```

[!] WARNING (line 1900)
Line 1900 uses numbered variable "end2" - use meaningful descriptive name

```python
                    start2 = block2['start_line']
                    end2 = block2['end_line']
                    
```

[!] WARNING (line 1902)
Line 1902 uses numbered variable "preview1" - use meaningful descriptive name

```python
                    
                    preview1 = block1['preview']
                    preview2 = block2['preview']
```

[!] WARNING (line 1903)
Line 1903 uses numbered variable "preview2" - use meaningful descriptive name

```python
                    preview1 = block1['preview']
                    preview2 = block2['preview']
                    
```

[!] WARNING (line 1911)
Line 1911 uses numbered variable "location1" - use meaningful descriptive name

```python
                    
                    location1 = f"{file1.name}:{func1} (lines {start1}-{end1})"
                    location2 = f"{file2.name}:{func2} (lines {start2}-{end2})"
```

[!] WARNING (line 1912)
Line 1912 uses numbered variable "location2" - use meaningful descriptive name

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

[!] WARNING (line 1907)
Line 1907 uses numbered variable "preview1" - use meaningful descriptive name

```python
                    if len(preview1) > 300:
                        preview1 = preview1[:300] + '...'
                    if len(preview2) > 300:
```

[!] WARNING (line 1909)
Line 1909 uses numbered variable "preview2" - use meaningful descriptive name

```python
                    if len(preview2) > 300:
                        preview2 = preview2[:300] + '...'
                    
```

---

## provide_meaningful_context
**markdown_formatter.py** - 1 violation(s)

[!] WARNING (line 12)
Line 12 contains magic number - replace with named constant

```python
        """Light line for subsection breaks"""
        return "─" * 60
    
```

---

## refactor_completely_not_partially
**repl_session.py** - 2 violation(s)

[!] WARNING (line 72)
Fallback/legacy support code found (comment at line 72, code at line 73) - complete refactoring by removing old pattern support

[!] WARNING (line 1152)
Fallback/legacy support code found (comment at line 1152, code at line 1153) - complete refactoring by removing old pattern support

---

## refactor_completely_not_partially
**validate_action.py** - 1 violation(s)

[!] WARNING (line 104)
Fallback/legacy support code found (comment at line 104, code at line 105) - complete refactoring by removing old pattern support

---

## simplify_control_flow
**behaviors.py** - 1 violation(s)

[!] WARNING (line 204)
Function "navigate_to" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return self.find_by_name(behavior_name) is not None

    def navigate_to(self, behavior_name: str):
        behavior = self.find_by_name(behavior_name)
        if behavior is None:
            raise ValueError(f"Behavior '{behavior_name}' not found")
        
        target_index = None
        for i, b in enumerate(self._behaviors):
            if b.name == behavior.name:
                target_index = i
                self._current_index = i
                break
        
        # When navigating to a behavior: mark all actions in previous behaviors as complete,
    # ... (truncated)
```

---

## simplify_control_flow
**repl_session.py** - 3 violation(s)

[!] WARNING (line 418)
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

[!] WARNING (line 645)
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

[!] WARNING (line 821)
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

[!] WARNING (line 1407)
Function "_get_node_signature" has nesting depth of 11 - use guard clauses and extract nested blocks to reduce nesting

```python
        return "|".join(signatures)
    
    def _get_node_signature(self, node: ast.AST) -> str:
        node_type = type(node).__name__
        
        if isinstance(node, ast.Assign):
            return f"ASSIGN({len(node.targets)}_targets)"
        elif isinstance(node, ast.AugAssign):
            return f"AUGASSIGN({type(node.op).__name__})"
        elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            return "CALL"
        elif isinstance(node, ast.Assert):
            return "ASSERT"
        elif isinstance(node, ast.Return):
            return "RETURN"
    # ... (truncated)
```

[!] WARNING (line 1435)
Function "_compare_ast_nodes_deep" has nesting depth of 11 - use guard clauses and extract nested blocks to reduce nesting

```python
            return node_type
    
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

[!] WARNING (line 1548)
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

[!] WARNING (line 1584)
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

[!] WARNING (line 1642)
Function "scan_cross_file" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        _safe_print("")  # Blank line after violations
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
        test_files: Optional[List[Path]] = None,
        code_files: Optional[List[Path]] = None,
        all_test_files: Optional[List[Path]] = None,
        all_code_files: Optional[List[Path]] = None,
        status_writer: Optional[Any] = None
    ) -> List[Dict[str, Any]]:
        violations = []
        
        # If all_* not provided, fall back to regular behavior
        if all_test_files is None:
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

[!] WARNING (line 74)
Function "_run_scanners_and_format_results" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        instructions._data['base_instructions'] = new_instructions

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

[!] WARNING (line 117)
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

## stop_writing_useless_comments
**behaviors.py** - 5 violation(s)

[X] ERROR (line 66)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def completed_behaviors(self) -> List[str]:
        """Get list of completed behavior names."""
        completed = []
```

[X] ERROR (line 104)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def next(self) -> Optional['Behavior']:
        """Get the next behavior without changing current state."""
        next_index = self._current_index + 1
```

[X] ERROR (line 111)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def previous(self) -> Optional['Behavior']:
        """Get the previous behavior without changing current state."""
        if self._current_index is None or self._current_index <= 0:
```

[X] ERROR (line 120)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def advance(self) -> Dict[str, Any]:
        """Advance to the next action in the current behavior, or next behavior if at end.
        
        Returns:
            Dict with status and information about the advancement
        """
        if not self.current:
```

[X] ERROR (line 159)
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
**repl_session.py** - 22 violation(s)

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

[X] ERROR (line 244)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_context_header_for_ai(self) -> str:
        """Get status display as a string for AI context headers.
        
        This is a convenience method that extracts just the output string
        from display_current_state().
        """
        state_display = self.display_current_state()
```

[X] ERROR (line 253)
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

[X] ERROR (line 380)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_help_command(self, args: str = "") -> REPLCommandResponse:
        """Handle help command using bot.help"""
        if not args:
```

[X] ERROR (line 410)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_status_command(self) -> REPLCommandResponse:
        """Handle status command using bot.status"""
        state_display = self.display_current_state(full=True)
```

[X] ERROR (line 419)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_current_command(self) -> REPLCommandResponse:
        """Re-execute current operation based on progress state"""
        if not self.has_current_action:
```

[X] ERROR (line 448)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_next_command(self) -> REPLCommandResponse:
        """Handle next/advance navigation"""
        if not self.has_current_action:
```

[X] ERROR (line 484)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_back_command(self) -> REPLCommandResponse:
        """Handle back/previous navigation"""
        if not self.has_current_action:
```

[X] ERROR (line 530)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_instructions_command(self, args: str = "") -> REPLCommandResponse:
        """Handle instructions command"""
        if not self.has_current_action:
```

[X] ERROR (line 551)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_submit_command(self, args: str = "") -> REPLCommandResponse:
        """Handle submit command"""
        if not self.has_current_action:
```

[X] ERROR (line 572)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_confirm_command(self) -> REPLCommandResponse:
        """Handle confirm command"""
        if not self.has_current_action:
```

[X] ERROR (line 627)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_path_command(self, args: str = "") -> REPLCommandResponse:
        """Handle path/workspace command"""
        if not args:
```

[X] ERROR (line 646)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_scope_command(self, args: str = "") -> REPLCommandResponse:
        """Handle scope command"""
        if not args:
```

[X] ERROR (line 712)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_behavior_command(self, behavior_name: str) -> REPLCommandResponse:
        """Handle behavior navigation"""
        behavior = self.cli_bot.behaviors.domain_behaviors.find_by_name(behavior_name)
```

[X] ERROR (line 741)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def navigate_to_behavior_action(self, behavior_name: str, action_name: str):
        """Navigate to a specific behavior and action
        
        Raises:
            ValueError: If behavior or action not found
        """
        # Navigate to behavior
```

[X] ERROR (line 762)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _wrap_navigation_with_instructions(self) -> REPLCommandResponse:
        """After navigation, auto-execute instructions for new position"""
        return self._handle_instructions_command()
```

[X] ERROR (line 766)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _wrap_with_context_header(self, content: str, response_msg: str) -> REPLCommandResponse:
        """Wrap content with instructions header and CLI status section"""
        formatter = self.formatter
```

[X] ERROR (line 807)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _mark_behavior_complete(self, behavior_name: str) -> None:
        """Mark a behavior as complete in the state file"""
        state_file = self.workspace_directory / 'behavior_action_state.json'
```

[X] ERROR (line 822)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_dot_notation(self, command: str) -> REPLCommandResponse:
        """Handle dot notation commands (behavior.action.operation)"""
        # Parse dot notation: behavior.action.operation or action.operation or .operation
```

[X] ERROR (line 204)
Useless comment: "# Get scope display" - delete it or improve the code instead

```python
        lines.append(formatter.subsection_separator())
        
        # Get scope display
        scope_display = self.cli_bot.get_scope_display()
```

[X] ERROR (line 701)
Useless comment: "# Get the scope display lines" - delete it or improve the code instead

```python
        result = self.cli_bot.set_scope(scope)
        
        # Get the scope display lines
        output = self.cli_bot.get_scope_display()
```

[X] ERROR (line 748)
Useless comment: "# Get the behavior" - delete it or improve the code instead

```python
        # Navigate to behavior
        self.cli_bot.behaviors.domain_behaviors.navigate_to(behavior_name)
        # Get the behavior
        behavior = self.cli_bot.behaviors.domain_behaviors.find_by_name(behavior_name)
```

---

## stop_writing_useless_comments
**render_action.py** - 6 violation(s)

[X] ERROR (line 33)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _execute_synchronizers(self, render_specs: List['RenderSpec']) -> None:
        """Execute synchronizers for all render specs."""
        for spec in render_specs:
```

[X] ERROR (line 45)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _prepare_instructions(self, instructions, context: ScopeActionContext):
        """Prepare render instructions with render specs and templates."""
        render_instructions = self._config_loader.load_render_instructions()
```

[X] ERROR (line 74)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _do_submit(self, context: ScopeActionContext) -> Dict[str, Any]:
        """Render actions execute synchronizers during preparation - nothing to submit."""
        return {
```

[X] ERROR (line 81)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def do_execute(self, context: ScopeActionContext) -> Dict[str, Any]:
        """Legacy method for backwards compatibility."""
        render_instructions = self._config_loader.load_render_instructions()
```

[X] ERROR (line 49)
Useless comment: "# Execute synchronizers during preparation" - delete it or improve the code instead

```python
        render_specs = self._render_specs
        
        # Execute synchronizers during preparation
        self._execute_synchronizers(render_specs)
```

[X] ERROR (line 63)
Useless comment: "# Update instructions with properly formatted data from merg" - delete it or improve the code instead

```python
        template_specs = [spec for spec in render_specs if spec.requires_ai_handling and (not spec.is_executed)]
        
        # Update instructions with properly formatted data from merged_instructions dict
        instructions._data['base_instructions'] = merged_instructions.get('base_instructions', [])
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
**validate_action.py** - 11 violation(s)

[X] ERROR (line 33)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _prepare_instructions(self, instructions, context: ValidateActionContext):
        """Prepare validation instructions with rules and validation data."""
        # Get rules with file paths for AI to read
```

[X] ERROR (line 75)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _run_scanners_and_format_results(self, context: ValidateActionContext) -> str:
        """Run validation scanners and format results for display in instructions."""
        logger.info('Running scanners for instructions display...')
```

[X] ERROR (line 118)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _format_scope_description(self, context: ValidateActionContext) -> str:
        """Format scope description for validation instructions."""
        if context.scope:
```

[X] ERROR (line 135)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _format_rules_with_file_paths(self) -> str:
        """Format rules with file paths for AI to read and analyze."""
        rules_data = self.inject_behavior_specific_rules()
```

[X] ERROR (line 182)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _do_submit(self, context: ValidateActionContext) -> Dict[str, Any]:
        """Run validation scanners and generate reports."""
        logger.info('=== Starting validation ===')
```

[X] ERROR (line 196)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def do_execute(self, context: ValidateActionContext) -> Dict[str, Any]:
        """Legacy method for backwards compatibility."""
        logger.info('=== Starting validation ===')
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

[X] ERROR (line 79)
Useless comment: "# Execute validation synchronously" - delete it or improve the code instead

```python
        
        try:
            # Execute validation synchronously
            result = self._executor.execute_synchronous(context)
```

[X] ERROR (line 82)
Useless comment: "# Get the report path from the result" - delete it or improve the code instead

```python
            result = self._executor.execute_synchronous(context)
            
            # Get the report path from the result
            instructions_dict = result.get('instructions', {})
```

---

## stop_writing_useless_comments
**validation_report_writer.py** - 1 violation(s)

[X] ERROR (line 19)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

def ensure_reports_directory(bot_paths: BotPaths, workspace_directory: Path) -> Path:
    """Module-level helper to create and return the reports directory."""
    docs_path = bot_paths.documentation_path
```

---

## stop_writing_useless_comments
**cli_bot.py** - 5 violation(s)

[X] ERROR (line 55)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def change_path(self, new_path: str) -> dict:
        """Change the workspace path. Returns result dict with status and message."""
        import json
```

[X] ERROR (line 78)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def set_scope(self, scope) -> dict:
        """Set the scope filter. Scope manages its own persistence, ensuring only one scope exists."""
        # Scope object handles clearing old scope and storing itself
```

[X] ERROR (line 90)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def clear_scope(self) -> dict:
        """Clear the scope filter. Scope manages its own removal from state."""
        from agile_bot.bots.base_bot.src.actions.action_context import Scope
```

[X] ERROR (line 99)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_scope_display(self) -> str:
        """Get the current scope display formatted by CLIScope."""
        scope_data = self._session.get_stored_scope()
```

[X] ERROR (line 109)
Useless comment: "# Return formatted error with details for debugging" - delete it or improve the code instead

```python
                return cli_scope.to_formatted_display()
            except Exception as e:
                # Return formatted error with details for debugging
                return f"{self._session.formatter.scope_icon()} **Scope**\n{self._session.formatter.scope_icon()} Error loading scope: {str(e)}"
```

---

## stop_writing_useless_comments
**markdown_formatter.py** - 2 violation(s)

[X] ERROR (line 7)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def section_separator(self) -> str:
        """Heavy line for major section breaks"""
        return "━" * 90
```

[X] ERROR (line 11)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def subsection_separator(self) -> str:
        """Light line for subsection breaks"""
        return "─" * 60
```

---

## stop_writing_useless_comments
**output_formatter.py** - 9 violation(s)

[X] ERROR (line 8)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @abstractmethod
    def section_separator(self) -> str:
        """Heavy line for major section breaks"""
        pass
```

[X] ERROR (line 12)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def subsection_separator(self) -> str:
        """Light line for subsection breaks - defaults to same as section_separator"""
        return self.section_separator()
```

[X] ERROR (line 29)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    # Emoji/icon methods for different contexts
    def bot_icon(self) -> str:
        """Icon for bot/AI context"""
        return ""
```

[X] ERROR (line 33)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def workspace_icon(self) -> str:
        """Icon for workspace/folder context"""
        return ""
```

[X] ERROR (line 37)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def path_icon(self) -> str:
        """Icon for file path context"""
        return ""
```

[X] ERROR (line 41)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def scope_icon(self) -> str:
        """Icon for scope/target context"""
        return ""
```

[X] ERROR (line 45)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def position_icon(self) -> str:
        """Icon for current position/location"""
        return ""
```

[X] ERROR (line 49)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def currently_executing_icon(self) -> str:
        """Icon for currently executing action"""
        return ""
```

[X] ERROR (line 53)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def file_icon(self) -> str:
        """Icon for file references"""
        return ""
```

---

## use_clear_function_parameters
**duplication_scanner.py** - 1 violation(s)

[!] WARNING (line 1642)
Function "scan_cross_file" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        _safe_print("")  # Blank line after violations
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
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
**rules.py** - 5 violation(s)

[!] WARNING (line 292)
Function "_process_scanner_result" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
            return data

    def _process_scanner_result(self, rule, rule_result: dict, scanner_results: Any, scanner_path: str, scanner_name: str, logger) -> str:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        execution_status = rule.scanner_execution_status or 'SUCCESS'
    # ... (truncated)
```

[!] WARNING (line 308)
Function "_execute_scanner" has 9 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return f'  [OK] {rule.rule_file}: Scanner executed successfully ({violations_count} violations)'

    def _execute_scanner(self, rule, rule_result: dict, context: ValidationContext, scanner_path: str, logger, files: Dict, changed_files: Dict, all_files: Dict) -> str:
        scanner_name = scanner_path.split('.')[-1] if '.' in scanner_path else scanner_path
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # ... (truncated)
```

[!] WARNING (line 328)
Function "_process_rule" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
            raise

    def _process_rule(self, rule, rule_result: dict, context: ValidationContext, logger, files: Dict, changed_files: Dict, all_files: Dict) -> str:
        scanner_path = rule.scanner_path
        if not scanner_path:
    # ... (truncated)
```

[!] WARNING (line 340)
Function "validate" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return self._execute_scanner(rule, rule_result, context, scanner_path, logger, files, changed_files, all_files)

    def validate(self, context: ValidationContext, files: Optional[Dict[str, List[Path]]]=None, callbacks: Optional[ValidationCallbacks]=None, skiprule: Optional[List[str]]=None, exclude: Optional[List[str]]=None) -> List[Dict[str, Any]]:
        if isinstance(context, ValidationContext):
            return self._execute_validation(context)
    # ... (truncated)
```

[!] WARNING (line 345)
Function "_create_legacy_context" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return self._execute_validation(self._create_legacy_context(context, files, callbacks, skiprule, exclude))

    def _create_legacy_context(self, knowledge_graph: Dict, files: Optional[Dict], callbacks: Optional[ValidationCallbacks], skiprule: Optional[List[str]], exclude: Optional[List[str]]) -> ValidationContext:
        return ValidationContext(knowledge_graph=knowledge_graph, files=files or {}, callbacks=callbacks or ValidationCallbacks(), skiprule=skiprule or [], exclude=exclude or [], skip_cross_file=True, all_files=False, behavior=self.behavior, bot_paths=getattr(self, 'bot_paths', None), working_dir=Path.cwd())

```

---

Completed: 2025-12-29 00:33:01
Total violations: 224
Scanners executed: 30
