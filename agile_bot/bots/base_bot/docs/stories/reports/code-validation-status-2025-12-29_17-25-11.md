# Validation Status - code
Started: 2025-12-29 17:25:11
Files: 274

## avoid_excessive_guards
**action_context.py** - 3 violation(s)

[!] WARNING (line 101)
Line 101: Variable truthiness check detected (if not matches_include:). Assume variable exists - let code fail fast if missing.

```python
                        break
                
                if not matches_include:
                    continue
            
```

[!] WARNING (line 117)
Line 117: Variable truthiness check detected (if matches_exclude:). Assume variable exists - let code fail fast if missing.

```python
                        break
                
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

[!] WARNING (line 1161)
Line 1161: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

```python
    def parse_command_parameters(self, args: str) -> Dict[str, Any]:
        params = {}
        if not args:
            return params
        
```

---

## avoid_excessive_guards
**vocabulary_helper.py** - 1 violation(s)

[!] WARNING (line 174)
Line 174: Variable truthiness check detected (if not synsets:). Assume variable exists - let code fail fast if missing.

```python
            synsets = wn.synsets(word_lower)
            
            if not synsets:
                return False
            
```

---

## eliminate_duplication
**action_context.py** - 1 violation(s)

[X] ERROR (line 88)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (filter_files:88-102):
```python
matches_include = False
for pattern in self.include_patterns:
    pattern_normalized = pattern.replace('\\', '/')
    if file_str == pattern_normalized or file_str.endswith(pattern_normalized) or fnma...
```

Location (filter_files:105-118):
```python
matches_exclude = False
for pattern in self.exclude_patterns:
    pattern_normalized = pattern.replace('\\', '/')
    if file_str == pattern_normalized or file_str.endswith(pattern_normalized) or fnma...
```

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

[X] ERROR (line 459)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (_handle_next_command:459-478):
```python
if not self.has_current_action:
    return REPLCommandResponse(output='ERROR: No current action', response='ERROR: No current action', status='error')
behavior = self.current_behavior
if not behavior:...
```

Location (_handle_back_command:495-514):
```python
if not self.has_current_action:
    return REPLCommandResponse(output='ERROR: No current action', response='ERROR: No current action', status='error')
behavior = self.current_behavior
if not behavior:...
```

---

## eliminate_duplication
**vocabulary_helper.py** - 1 violation(s)

[X] ERROR (line 40)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (is_verb:40-45):
```python
word_lower = word.lower()
synsets = wn.synsets(word_lower, pos=wn.VERB)
return len(synsets) > 0
```

Location (is_noun:50-55):
```python
word_lower = word.lower()
synsets = wn.synsets(word_lower, pos=wn.NOUN)
return len(synsets) > 0
```

---

## eliminate_duplication
**headless_session.py** - 1 violation(s)

[X] ERROR (line 79)
Duplicate code blocks detected (2 locations) - extract to helper function.

Location (invokes_action:79-94):
```python
result.blocked_operation = 'submit'
result.operations_executed = ['instructions', 'submit']
result.operations_status = {'instructions': 'completed', 'submit': 'blocked'}
```

Location (invokes_behavior:108-122):
```python
result.blocked_action = 'clarify'
result.actions_executed = ['clarify']
result.actions_status = {'clarify': 'blocked'}
```

---


## Cross-File Duplication Analysis
Scanning 27 changed file(s) against 274 total files...
Extracted 783 changed blocks, 4160 reference blocks
Starting 3,257,280 pairwise comparisons...
Comparing: 1% (35,594/3,257,280) - 0 violations - ETA: 905s  
Comparing: 2% (70,432/3,257,280) - 4 violations - ETA: 904s  
Comparing: 2% (96,367/3,257,280) - 8 violations - ETA: 984s  
Found 10 violations so far...
Comparing: 3% (122,212/3,257,280) - 12 violations - ETA: 1026s  
Comparing: 4% (153,425/3,257,280) - 12 violations - ETA: 1011s  
Comparing: 5% (186,841/3,257,280) - 12 violations - ETA: 986s  
Comparing: 6% (214,204/3,257,280) - 12 violations - ETA: 994s  
Comparing: 7% (254,258/3,257,280) - 12 violations - ETA: 944s  
Comparing: 8% (286,960/3,257,280) - 12 violations - ETA: 931s  
Comparing: 9% (315,359/3,257,280) - 12 violations - ETA: 932s  
Comparing: 10% (339,849/3,257,280) - 12 violations - ETA: 944s  
Comparing: 11% (382,494/3,257,280) - 12 violations - ETA: 901s  
Comparing: 12% (410,432/3,257,280) - 12 violations - ETA: 901s  
Comparing: 13% (430,627/3,257,280) - 12 violations - ETA: 919s  
Comparing: 14% (467,831/3,257,280) - 12 violations - ETA: 894s  
Comparing: 15% (492,881/3,257,280) - 12 violations - ETA: 897s  
Comparing: 15% (518,911/3,257,280) - 12 violations - ETA: 897s  
Comparing: 16% (551,674/3,257,280) - 12 violations - ETA: 882s  
Comparing: 17% (572,084/3,257,280) - 12 violations - ETA: 891s  
Comparing: 18% (598,409/3,257,280) - 12 violations - ETA: 888s  
Comparing: 19% (623,321/3,257,280) - 12 violations - ETA: 887s  
Comparing: 19% (646,601/3,257,280) - 12 violations - ETA: 888s  
Comparing: 20% (671,053/3,257,280) - 12 violations - ETA: 886s  
Comparing: 21% (695,485/3,257,280) - 12 violations - ETA: 884s  
Comparing: 22% (721,230/3,257,280) - 12 violations - ETA: 879s  
Comparing: 22% (744,190/3,257,280) - 12 violations - ETA: 878s  
Comparing: 23% (763,505/3,257,280) - 12 violations - ETA: 881s  
Comparing: 24% (785,666/3,257,280) - 12 violations - ETA: 880s  
Comparing: 24% (807,383/3,257,280) - 12 violations - ETA: 880s  
Comparing: 25% (824,021/3,257,280) - 12 violations - ETA: 885s  
Comparing: 25% (842,451/3,257,280) - 12 violations - ETA: 888s  
Comparing: 26% (859,471/3,257,280) - 12 violations - ETA: 892s  
Comparing: 26% (875,958/3,257,280) - 12 violations - ETA: 897s  
Comparing: 27% (895,045/3,257,280) - 12 violations - ETA: 897s  
Comparing: 28% (916,536/3,257,280) - 12 violations - ETA: 893s  
Comparing: 28% (938,031/3,257,280) - 12 violations - ETA: 890s  
Comparing: 29% (975,251/3,257,280) - 12 violations - ETA: 865s  
Comparing: 30% (994,763/3,257,280) - 12 violations - ETA: 864s  
Comparing: 31% (1,025,522/3,257,280) - 16 violations - ETA: 848s  
Found 20 violations so far...
Comparing: 32% (1,048,585/3,257,280) - 24 violations - ETA: 842s  
Found 30 violations so far...
Found 40 violations so far...
Comparing: 33% (1,077,558/3,257,280) - 43 violations - ETA: 829s  
Found 50 violations so far...
Found 60 violations so far...
Found 70 violations so far...
Comparing: 34% (1,109,372/3,257,280) - 72 violations - ETA: 813s  
Found 80 violations so far...
Found 90 violations so far...
Found 100 violations so far...
Comparing: 34% (1,136,296/3,257,280) - 102 violations - ETA: 802s  
Found 110 violations so far...
Comparing: 35% (1,158,287/3,257,280) - 111 violations - ETA: 797s  
Comparing: 36% (1,180,711/3,257,280) - 115 violations - ETA: 791s  
Comparing: 36% (1,200,295/3,257,280) - 116 violations - ETA: 788s  
Found 120 violations so far...
Found 130 violations so far...
Comparing: 37% (1,227,582/3,257,280) - 131 violations - ETA: 777s  
Found 140 violations so far...
Comparing: 38% (1,259,459/3,257,280) - 149 violations - ETA: 761s  
Found 150 violations so far...
Found 160 violations so far...
Comparing: 39% (1,289,764/3,257,280) - 169 violations - ETA: 747s  
Found 170 violations so far...
Comparing: 40% (1,316,410/3,257,280) - 172 violations - ETA: 737s  
Found 180 violations so far...
Comparing: 41% (1,342,038/3,257,280) - 189 violations - ETA: 727s  
Comparing: 41% (1,366,082/3,257,280) - 189 violations - ETA: 719s  
Found 190 violations so far...
Found 200 violations so far...
Comparing: 42% (1,391,011/3,257,280) - 201 violations - ETA: 711s  
Comparing: 43% (1,411,687/3,257,280) - 201 violations - ETA: 706s  
Comparing: 44% (1,433,974/3,257,280) - 208 violations - ETA: 699s  
Comparing: 44% (1,453,868/3,257,280) - 208 violations - ETA: 694s  
Comparing: 45% (1,472,132/3,257,280) - 208 violations - ETA: 691s  
Found 210 violations so far...
Comparing: 45% (1,490,972/3,257,280) - 210 violations - ETA: 687s  
Comparing: 46% (1,508,373/3,257,280) - 210 violations - ETA: 684s  
Comparing: 47% (1,547,207/3,257,280) - 210 violations - ETA: 663s  
Comparing: 48% (1,576,739/3,257,280) - 210 violations - ETA: 650s  
Comparing: 49% (1,606,775/3,257,280) - 210 violations - ETA: 636s  
Comparing: 49% (1,625,845/3,257,280) - 210 violations - ETA: 632s  
Comparing: 50% (1,650,509/3,257,280) - 210 violations - ETA: 623s  
Comparing: 51% (1,680,601/3,257,280) - 210 violations - ETA: 609s  
Comparing: 52% (1,706,451/3,257,280) - 210 violations - ETA: 599s  
Comparing: 53% (1,730,394/3,257,280) - 210 violations - ETA: 591s  
Comparing: 53% (1,752,443/3,257,280) - 210 violations - ETA: 583s  
Comparing: 54% (1,771,342/3,257,280) - 210 violations - ETA: 578s  
Comparing: 54% (1,790,352/3,257,280) - 210 violations - ETA: 573s  
Comparing: 55% (1,808,465/3,257,280) - 210 violations - ETA: 568s  
Comparing: 56% (1,824,779/3,257,280) - 210 violations - ETA: 565s  
Comparing: 56% (1,840,184/3,257,280) - 210 violations - ETA: 562s  
Comparing: 56% (1,856,268/3,257,280) - 210 violations - ETA: 558s  
Comparing: 58% (1,891,058/3,257,280) - 210 violations - ETA: 541s  
Comparing: 59% (1,925,962/3,257,280) - 210 violations - ETA: 525s  
Comparing: 59% (1,943,926/3,257,280) - 210 violations - ETA: 520s  
Comparing: 60% (1,959,368/3,257,280) - 210 violations - ETA: 516s  
Comparing: 60% (1,973,170/3,257,280) - 210 violations - ETA: 514s  
Comparing: 60% (1,985,126/3,257,280) - 210 violations - ETA: 512s  
Comparing: 61% (1,997,299/3,257,280) - 210 violations - ETA: 511s  
Comparing: 62% (2,021,546/3,257,280) - 210 violations - ETA: 501s  
Comparing: 62% (2,044,357/3,257,280) - 210 violations - ETA: 492s  
Comparing: 63% (2,063,819/3,257,280) - 210 violations - ETA: 485s  
Comparing: 64% (2,090,850/3,257,280) - 210 violations - ETA: 474s  
Comparing: 64% (2,109,364/3,257,280) - 210 violations - ETA: 468s  
Comparing: 65% (2,134,733/3,257,280) - 210 violations - ETA: 457s  
Comparing: 66% (2,164,860/3,257,280) - 210 violations - ETA: 444s  
Comparing: 67% (2,199,183/3,257,280) - 210 violations - ETA: 428s  
Comparing: 68% (2,240,073/3,257,280) - 210 violations - ETA: 408s  
Comparing: 69% (2,274,309/3,257,280) - 210 violations - ETA: 393s  
Comparing: 70% (2,304,624/3,257,280) - 210 violations - ETA: 380s  
Comparing: 71% (2,329,966/3,257,280) - 210 violations - ETA: 370s  
Comparing: 72% (2,354,234/3,257,280) - 210 violations - ETA: 360s  
Comparing: 73% (2,380,425/3,257,280) - 210 violations - ETA: 349s  
Comparing: 74% (2,420,056/3,257,280) - 210 violations - ETA: 332s  
Comparing: 75% (2,451,761/3,257,280) - 210 violations - ETA: 318s  
Comparing: 76% (2,480,911/3,257,280) - 210 violations - ETA: 306s  
Comparing: 77% (2,512,790/3,257,280) - 210 violations - ETA: 293s  
Comparing: 78% (2,545,389/3,257,280) - 210 violations - ETA: 279s  
Comparing: 79% (2,573,576/3,257,280) - 210 violations - ETA: 268s  
Comparing: 79% (2,597,811/3,257,280) - 210 violations - ETA: 258s  
Comparing: 80% (2,618,334/3,257,280) - 210 violations - ETA: 251s  
Comparing: 80% (2,637,224/3,257,280) - 210 violations - ETA: 244s  
Comparing: 81% (2,654,305/3,257,280) - 210 violations - ETA: 238s  
Comparing: 82% (2,676,720/3,257,280) - 219 violations - ETA: 229s  
Found 220 violations so far...
Comparing: 82% (2,697,834/3,257,280) - 227 violations - ETA: 221s  
Found 230 violations so far...
Comparing: 83% (2,714,335/3,257,280) - 230 violations - ETA: 216s  
Found 240 violations so far...
Comparing: 83% (2,730,287/3,257,280) - 242 violations - ETA: 210s  
Comparing: 84% (2,745,787/3,257,280) - 249 violations - ETA: 204s  
Comparing: 84% (2,757,571/3,257,280) - 249 violations - ETA: 201s  
Found 250 violations so far...
Comparing: 85% (2,773,516/3,257,280) - 253 violations - ETA: 195s  
Comparing: 85% (2,797,460/3,257,280) - 253 violations - ETA: 185s  
Comparing: 86% (2,816,336/3,257,280) - 253 violations - ETA: 178s  
Comparing: 87% (2,843,698/3,257,280) - 253 violations - ETA: 167s  
Comparing: 88% (2,869,139/3,257,280) - 253 violations - ETA: 156s  
Comparing: 88% (2,883,872/3,257,280) - 253 violations - ETA: 151s  
Comparing: 88% (2,897,024/3,257,280) - 253 violations - ETA: 146s  
Comparing: 89% (2,924,395/3,257,280) - 253 violations - ETA: 135s  
Comparing: 90% (2,953,660/3,257,280) - 253 violations - ETA: 123s  
Comparing: 91% (2,975,946/3,257,280) - 253 violations - ETA: 114s  
Comparing: 91% (2,994,759/3,257,280) - 253 violations - ETA: 106s  
Comparing: 92% (3,009,420/3,257,280) - 253 violations - ETA: 101s  
Comparing: 93% (3,037,802/3,257,280) - 253 violations - ETA: 89s  
Comparing: 94% (3,067,960/3,257,280) - 253 violations - ETA: 77s  
Comparing: 94% (3,091,134/3,257,280) - 253 violations - ETA: 67s  
Comparing: 95% (3,121,209/3,257,280) - 253 violations - ETA: 55s  
Comparing: 96% (3,147,072/3,257,280) - 253 violations - ETA: 44s  
Complete: 3154529 comparisons, 253 violations

## enforce_encapsulation
**repl_session.py** - 1 violation(s)

[!] WARNING (line 712)
Method "_handle_scope_command" in class "REPLSession" has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

---

## enforce_encapsulation
**strategy_action.py** - 1 violation(s)

[!] WARNING (line 74)
Method "_format_instructions_for_display" in class "StrategyAction" has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

---

## enforce_encapsulation
**validate_action.py** - 1 violation(s)

[!] WARNING (line 154)
Method "_format_rules_with_file_paths" in class "ValidateRulesAction" has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

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
Class "REPLSession" is 1276 lines - should be under 300 lines (extract related methods into separate classes)

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
**verb_noun_scanner.py** - 1 violation(s)

[!] WARNING (line 28)
Class "VerbNounScanner" is 414 lines - should be under 300 lines (extract related methods into separate classes)

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
        
        from fnmatch import fnmatch
        filtered = []
        
        for file_path in file_list:
            # Convert to string with forward slashes for consistent matching
            file_str = str(file_path).replace('\\', '/')
            
            # Check include patterns
            if self.include_patterns:
                matches_include = False
                for pattern in self.include_patterns:
                    pattern_normalized = pattern.replace('\\', '/')
                    # Try exact match, ends-with match, and glob match
                    if (file_str == pattern_normalized or 
                        file_str.endswith(pattern_normalized) or
                        fnmatch(file_str, pattern_normalized) or
                        fnmatch(file_str, f'*/{pattern_normalized}') or
                        fnmatch(file_str, f'**/{pattern_normalized}')):
                        matches_include = True
                        break
                
                if not matches_include:
                    continue
            
            # Check exclude patterns
            if self.exclude_patterns:
                matches_exclude = False
                for pattern in self.exclude_patterns:
                    pattern_normalized = pattern.replace('\\', '/')
                    if (file_str == pattern_normalized or 
                        file_str.endswith(pattern_normalized) or
                        fnmatch(file_str, pattern_normalized) or
                        fnmatch(file_str, f'*/{pattern_normalized}') or
                        fnmatch(file_str, f'**/{pattern_normalized}')):
                        matches_exclude = True
                        break
                
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
Function "display_current_state" is 78 lines - should be under 20 lines (extract complex logic to helper functions)

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
**resource_oriented_code_scanner.py** - 1 violation(s)

[!] WARNING (line 28)
Function "scan_cross_file" is 47 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return []
    
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
                suggested_name = loader_class_name[:-len(suffix)] if loader_class_name.endswith(suffix) else loader_class_name
    # ... (truncated)
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
**verb_noun_scanner.py** - 1 violation(s)

[!] WARNING (line 33)
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
**vocabulary_helper.py** - 2 violation(s)

[!] WARNING (line 58)
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

[!] WARNING (line 155)
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
**rules.py** - 2 violation(s)

[!] WARNING (line 137)
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

[!] WARNING (line 264)
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
**repl_session.py** - 9 violation(s)

[i] INFO (line 144)
Function "display_current_state" is 108 lines - consider improving vertical density by declaring variables near usage

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

[i] INFO (line 262)
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

[i] INFO (line 333)
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

[i] INFO (line 539)
Function "_handle_instructions_command" is 53 lines - consider improving vertical density by declaring variables near usage

```python
        )
    
    def _handle_instructions_command(self, args: str = "") -> REPLCommandResponse:
        """Handle instructions command"""
        if not self.has_current_action:
            return REPLCommandResponse(
                output="ERROR: No current action to get instructions for",
                response="ERROR: No current action",
                status="error"
            )
    # ... (truncated)
```

[i] INFO (line 614)
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

[i] INFO (line 688)
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

[i] INFO (line 864)
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

[i] INFO (line 992)
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

[i] INFO (line 1060)
Function "_execute_action_with_args" is 73 lines - consider improving vertical density by declaring variables near usage

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
**resource_oriented_code_scanner.py** - 2 violation(s)

[i] INFO (line 28)
Function "scan_cross_file" is 59 lines - consider improving vertical density by declaring variables near usage

```python
        return []
    
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

[i] INFO (line 105)
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
**verb_noun_scanner.py** - 2 violation(s)

[i] INFO (line 247)
Function "_check_noun_verb_pattern" is 63 lines - consider improving vertical density by declaring variables near usage

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

[i] INFO (line 330)
Function "_check_noun_only" is 112 lines - consider improving vertical density by declaring variables near usage

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

## never_swallow_exceptions
**action_context.py** - 1 violation(s)

[X] ERROR (line 250)
Except block only contains pass at line 250 - exceptions must be logged or rethrown, never swallowed

```python
                del state_data['scope']
                state_file.write_text(json.dumps(state_data, indent=2))
        except (json.JSONDecodeError, IOError):
            pass
    
```

---

## never_swallow_exceptions
**repl_session.py** - 2 violation(s)

[X] ERROR (line 861)
Except block only contains pass at line 861 - exceptions must be logged or rethrown, never swallowed

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

## never_swallow_exceptions
**verb_noun_scanner.py** - 1 violation(s)

[X] ERROR (line 437)
Except block only contains pass at line 437 - exceptions must be logged or rethrown, never swallowed

```python
                ).to_dict()
        
        except Exception:
            # NLTK POS tagging failed - return None to avoid false positives
            pass
        
```

---

## provide_meaningful_context
**error_recovery.py** - 1 violation(s)

[!] WARNING (line 8)
Line 8 contains magic number - replace with named constant

```python
DEFAULT_MAX_ATTEMPTS = 3
DEFAULT_WAIT_TIME_SECONDS = 60.0

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

[!] WARNING (line 233)
Fallback/legacy support code found (comment at line 233, code at line 234) - complete refactoring by removing old pattern support

[!] WARNING (line 1203)
Fallback/legacy support code found (comment at line 1203, code at line 1204) - complete refactoring by removing old pattern support

---

## refactor_completely_not_partially
**validate_action.py** - 1 violation(s)

[!] WARNING (line 104)
Fallback/legacy support code found (comment at line 104, code at line 105) - complete refactoring by removing old pattern support

---

## simplify_control_flow
**action_context.py** - 4 violation(s)

[!] WARNING (line 75)
Function "filter_files" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return False
    
    def filter_files(self, file_list: List[Path]) -> List[Path]:
        """Filter file list to only files matching this filter."""
        if not self.include_patterns and not self.exclude_patterns:
            return file_list
        
        from fnmatch import fnmatch
        filtered = []
        
        for file_path in file_list:
            # Convert to string with forward slashes for consistent matching
            file_str = str(file_path).replace('\\', '/')
            
            # Check include patterns
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
**repl_session.py** - 3 violation(s)

[!] WARNING (line 428)
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

[!] WARNING (line 688)
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

[!] WARNING (line 864)
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
        status_writer: Optional[Any] = None
    ) -> List[Dict[str, Any]]:
        violations = []
        
        all_files = []
        if code_files:
    # ... (truncated)
```

[!] WARNING (line 105)
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
**verb_noun_scanner.py** - 1 violation(s)

[!] WARNING (line 330)
Function "_check_noun_only" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return None
    
    def _check_noun_only(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        try:
            tokens, tags = self._get_tokens_and_tags(name)
            
            if not tags:
                return None
            
            has_verb = any(self._is_verb(tag[1]) for tag in tags)
            
            # If NLTK didn't find a verb, check if first word can be a verb using WordNet
            # (NLTK often tags capitalized verbs as proper nouns NNP)
            if not has_verb and tokens:
                # Strip punctuation from first word (e.g., "Load+" -> "Load")
    # ... (truncated)
```

---

## simplify_control_flow
**vocabulary_helper.py** - 2 violation(s)

[!] WARNING (line 58)
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

[!] WARNING (line 155)
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
**strategy_action.py** - 1 violation(s)

[!] WARNING (line 71)
Function "_format_instructions_for_display" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return {'status': 'submitted', 'message': 'No strategy data to save'}
    
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

## simplify_control_flow
**validation_scope.py** - 1 violation(s)

[!] WARNING (line 152)
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
**execution_context.py** - 1 violation(s)

[!] WARNING (line 42)
Function "processes_line" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        self._current_section = None
    
    def processes_line(self, line: str) -> None:
        if line.startswith('User Intent:'):
            self._current_section = 'user_message'
            self.user_message = line.replace('User Intent:', '').strip()
        elif line.startswith('Chat History:'):
            self._current_section = 'chat_history'
        elif line.startswith('File References:'):
            self._current_section = 'file_references'
        elif line.startswith('-'):
            self._appends_list_item(line[1:].strip())
    
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
**instructions.py** - 2 violation(s)

[X] ERROR (line 34)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def scope(self) -> Optional['Scope']:
        """Get the scope filter if set."""
        return self._scope
```

[X] ERROR (line 39)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @property
    def context_sources_text(self) -> List[str]:
        """Generate standard 'Look for context in the following locations' section with actual paths."""
        if not self._bot_paths:
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

[X] ERROR (line 254)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def get_context_header_for_ai(self) -> str:
        """Get status display as a string for AI context headers.
        
        This is a convenience method that extracts just the output string
        from display_current_state().
        """
        state_display = self.display_current_state()
```

[X] ERROR (line 263)
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

[X] ERROR (line 390)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_help_command(self, args: str = "") -> REPLCommandResponse:
        """Handle help command using bot.help"""
        if not args:
```

[X] ERROR (line 420)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_status_command(self) -> REPLCommandResponse:
        """Handle status command using bot.status"""
        state_display = self.display_current_state(full=True)
```

[X] ERROR (line 429)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_current_command(self) -> REPLCommandResponse:
        """Re-execute current operation based on progress state"""
        if not self.has_current_action:
```

[X] ERROR (line 458)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_next_command(self) -> REPLCommandResponse:
        """Handle next/advance navigation"""
        if not self.has_current_action:
```

[X] ERROR (line 494)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_back_command(self) -> REPLCommandResponse:
        """Handle back/previous navigation"""
        if not self.has_current_action:
```

[X] ERROR (line 540)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_instructions_command(self, args: str = "") -> REPLCommandResponse:
        """Handle instructions command"""
        if not self.has_current_action:
```

[X] ERROR (line 594)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_submit_command(self, args: str = "") -> REPLCommandResponse:
        """Handle submit command"""
        if not self.has_current_action:
```

[X] ERROR (line 615)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_confirm_command(self) -> REPLCommandResponse:
        """Handle confirm command"""
        if not self.has_current_action:
```

[X] ERROR (line 670)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_path_command(self, args: str = "") -> REPLCommandResponse:
        """Handle path/workspace command"""
        if not args:
```

[X] ERROR (line 689)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_scope_command(self, args: str = "") -> REPLCommandResponse:
        """Handle scope command"""
        if not args:
```

[X] ERROR (line 755)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _handle_behavior_command(self, behavior_name: str) -> REPLCommandResponse:
        """Handle behavior navigation"""
        behavior = self.cli_bot.behaviors.domain_behaviors.find_by_name(behavior_name)
```

[X] ERROR (line 784)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def navigate_to_behavior_action(self, behavior_name: str, action_name: str):
        """Navigate to a specific behavior and action
        
        Raises:
            ValueError: If behavior or action not found
        """
        # Navigate to behavior
```

[X] ERROR (line 805)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _wrap_navigation_with_instructions(self) -> REPLCommandResponse:
        """After navigation, auto-execute instructions for new position"""
        return self._handle_instructions_command()
```

[X] ERROR (line 809)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _wrap_with_context_header(self, content: str, response_msg: str) -> REPLCommandResponse:
        """Wrap content with instructions header and CLI status section"""
        formatter = self.formatter
```

[X] ERROR (line 850)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _mark_behavior_complete(self, behavior_name: str) -> None:
        """Mark a behavior as complete in the state file"""
        state_file = self.workspace_directory / 'behavior_action_state.json'
```

[X] ERROR (line 865)
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

[X] ERROR (line 744)
Useless comment: "# Get the scope display lines" - delete it or improve the code instead

```python
        result = self.cli_bot.set_scope(scope)
        
        # Get the scope display lines
        output = self.cli_bot.get_scope_display()
```

[X] ERROR (line 791)
Useless comment: "# Get the behavior" - delete it or improve the code instead

```python
        # Navigate to behavior
        self.cli_bot.behaviors.domain_behaviors.navigate_to(behavior_name)
        # Get the behavior
        behavior = self.cli_bot.behaviors.domain_behaviors.find_by_name(behavior_name)
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
**verb_noun_scanner.py** - 1 violation(s)

[X] ERROR (line 203)
Useless comment: "# Handle verbs ending in -es (e.g., "fixes" -> "fix", "watch" - delete it or improve the code instead

```python
        if verb_lower.endswith("ies") and len(verb_lower) > 3:
            base = verb_lower[:-3] + "y"
        # Handle verbs ending in -es (e.g., "fixes" -> "fix", "watches" -> "watch", "goes" -> "go")
        elif verb_lower.endswith("es") and len(verb_lower) > 2:
```

---

## stop_writing_useless_comments
**vocabulary_helper.py** - 12 violation(s)

[X] ERROR (line 29)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class VocabularyHelper:
    """Helper class for linguistic analysis using NLTK."""
    
```

[X] ERROR (line 39)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @staticmethod
    def is_verb(word: str) -> bool:
        """Check if word can function as a verb using WordNet."""
        try:
```

[X] ERROR (line 49)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @staticmethod
    def is_noun(word: str) -> bool:
        """Check if word can function as a noun using WordNet."""
        try:
```

[X] ERROR (line 59)
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

[X] ERROR (line 90)
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

[X] ERROR (line 128)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @staticmethod
    def get_pos_tags(text: str) -> List[tuple[str, str]]:
        """Get part-of-speech tags for text."""
        try:
```

[X] ERROR (line 138)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @staticmethod
    def is_verb_tag(tag: str) -> bool:
        """Check if POS tag indicates a verb."""
        verb_tags = ['VB', 'VBP', 'VBZ', 'VBD', 'VBG', 'VBN']
```

[X] ERROR (line 144)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @staticmethod
    def is_noun_tag(tag: str) -> bool:
        """Check if POS tag indicates a noun."""
        noun_tags = ['NN', 'NNS', 'NNP', 'NNPS']
```

[X] ERROR (line 150)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @staticmethod
    def is_proper_noun_tag(tag: str) -> bool:
        """Check if POS tag indicates a proper noun."""
        proper_noun_tags = ['NNP', 'NNPS']
```

[X] ERROR (line 156)
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

[X] ERROR (line 171)
Useless comment: "# Get all synsets for the word" - delete it or improve the code instead

```python
            word_lower = word.lower()
            
            # Get all synsets for the word
            synsets = wn.synsets(word_lower)
```

[X] ERROR (line 179)
Useless comment: "# Get all hypernyms (parent concepts)" - delete it or improve the code instead

```python
            # Get hypernym paths for all synsets
            for synset in synsets:
                # Get all hypernyms (parent concepts)
                hypernyms = set()
```

---

## stop_writing_useless_comments
**rules.py** - 3 violation(s)

[X] ERROR (line 68)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @classmethod
    def _get_files_for_validation(cls, behavior, context: 'ValidateActionContext') -> Dict[str, List[Path]]:
        """Get files to validate based on behavior and scope."""
        from agile_bot.bots.base_bot.src.actions.validate.file_discovery import FileDiscovery
```

[X] ERROR (line 47)
Useless comment: "# Get files - either from scope filter or discover all" - delete it or improve the code instead

```python
            knowledge_graph_content = validation_scope.filter_story_graph(knowledge_graph_content)
        
        # Get files - either from scope filter or discover all
        files = cls._get_files_for_validation(behavior, context)
```

[X] ERROR (line 208)
Useless comment: "# Load bot-level rules" - delete it or improve the code instead

```python
        all_rules = []
        
        # Load bot-level rules
        bot_rules = self._rule_loader.load_bot_rules()
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
**strategy_action.py** - 6 violation(s)

[X] ERROR (line 36)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _prepare_instructions(self, instructions, context: StrategyActionContext):
        """Add strategy data (criteria, assumptions, activities) to instructions."""
        instructions.update(self.strategy.instructions)
```

[X] ERROR (line 40)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _do_submit(self, context: StrategyActionContext) -> Dict[str, Any]:
        """Save strategy decisions and assumptions to strategy.json."""
        decisions = context.get_decisions()
```

[X] ERROR (line 72)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _format_instructions_for_display(self, instructions) -> str:
        """Format strategy data for REPL display."""
        # Get base formatting first (includes scope warning if set)
```

[X] ERROR (line 107)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

    def _format_option(self, option) -> list:
        """Format a single decision criteria option for display."""
        lines = []
```

[X] ERROR (line 58)
Useless comment: "# Get file path" - delete it or improve the code instead

```python
            saved_items = " and ".join(message_parts) if message_parts else "data"
            
            # Get file path
            saved_path = self.behavior.bot_paths.workspace_directory / 'docs' / 'stories' / 'strategy.json'
```

[X] ERROR (line 76)
Useless comment: "# Get the instruction data" - delete it or improve the code instead

```python
        output_lines = super()._format_instructions_for_display(instructions).split('\n')
        
        # Get the instruction data
        instructions_dict = instructions.to_dict()
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

## use_clear_function_parameters
**active_language_scanner.py** - 1 violation(s)

[!] WARNING (line 127)
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
**resource_oriented_code_scanner.py** - 1 violation(s)

[!] WARNING (line 28)
Function "scan_cross_file" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return []
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
    # ... (truncated)
```

---

## use_clear_function_parameters
**rules.py** - 5 violation(s)

[!] WARNING (line 331)
Function "_process_scanner_result" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
            return data

    def _process_scanner_result(self, rule, rule_result: dict, scanner_results: Any, scanner_path: str, scanner_name: str, logger) -> str:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        execution_status = rule.scanner_execution_status or 'SUCCESS'
    # ... (truncated)
```

[!] WARNING (line 347)
Function "_execute_scanner" has 9 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return f'  [OK] {rule.rule_file}: Scanner executed successfully ({violations_count} violations)'

    def _execute_scanner(self, rule, rule_result: dict, context: ValidationContext, scanner_path: str, logger, files: Dict, changed_files: Dict, all_files: Dict) -> str:
        scanner_name = scanner_path.split('.')[-1] if '.' in scanner_path else scanner_path
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # ... (truncated)
```

[!] WARNING (line 367)
Function "_process_rule" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
            raise

    def _process_rule(self, rule, rule_result: dict, context: ValidationContext, logger, files: Dict, changed_files: Dict, all_files: Dict) -> str:
        scanner_path = rule.scanner_path
        if not scanner_path:
    # ... (truncated)
```

[!] WARNING (line 379)
Function "validate" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return self._execute_scanner(rule, rule_result, context, scanner_path, logger, files, changed_files, all_files)

    def validate(self, context: ValidationContext, files: Optional[Dict[str, List[Path]]]=None, callbacks: Optional[ValidationCallbacks]=None, skiprule: Optional[List[str]]=None, exclude: Optional[List[str]]=None) -> List[Dict[str, Any]]:
        if isinstance(context, ValidationContext):
            return self._execute_validation(context)
    # ... (truncated)
```

[!] WARNING (line 384)
Function "_create_legacy_context" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return self._execute_validation(self._create_legacy_context(context, files, callbacks, skiprule, exclude))

    def _create_legacy_context(self, knowledge_graph: Dict, files: Optional[Dict], callbacks: Optional[ValidationCallbacks], skiprule: Optional[List[str]], exclude: Optional[List[str]]) -> ValidationContext:
        return ValidationContext(knowledge_graph=knowledge_graph, files=files or {}, callbacks=callbacks or ValidationCallbacks(), skiprule=skiprule or [], exclude=exclude or [], skip_cross_file=True, all_files=False, behavior=self.behavior, bot_paths=getattr(self, 'bot_paths', None), working_dir=Path.cwd())

```

---

## use_clear_function_parameters
**execution_result.py** - 2 violation(s)

[!] WARNING (line 53)
Function "creates_blocked" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
    
    @classmethod
    def creates_blocked(
        cls,
        log_path: Path,
    # ... (truncated)
```

[!] WARNING (line 80)
Function "creates_completed" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
    
    @classmethod
    def creates_completed(
        cls,
        log_path: Path,
    # ... (truncated)
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

[i] INFO (line 504)
Function "__post_init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**instructions.py** - 24 violation(s)

[i] INFO (line 9)
Class "Instructions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 11)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 11)
Function "__init__" uses parameter name "base_instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 11)
Function "__init__" uses parameter name "scope" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 18)
Function "add" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 23)
Function "add_display" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 29)
Function "display_content" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 33)
Function "scope" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 38)
Function "context_sources_text" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 76)
Function "set" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 76)
Function "set" uses parameter name "key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 82)
Function "update" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 92)
Function "to_dict" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 97)
Function "copy" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 104)
Function "get" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 104)
Function "get" uses parameter name "key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 104)
Function "get" uses parameter name "default" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 107)
Function "__getitem__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 107)
Function "__getitem__" uses parameter name "key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 110)
Function "__setitem__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 110)
Function "__setitem__" uses parameter name "key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 115)
Function "__contains__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 115)
Function "__contains__" uses parameter name "key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 118)
Function "__repr__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**repl_session.py** - 59 violation(s)

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

[i] INFO (line 253)
Function "get_context_header_for_ai" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 262)
Function "_convert_domain_result_to_repl_response" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 262)
Function "_convert_domain_result_to_repl_response" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 320)
Function "read_and_execute_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 320)
Function "read_and_execute_command" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 333)
Function "_handle_simple_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 333)
Function "_handle_simple_command" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 389)
Function "_handle_help_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 389)
Function "_handle_help_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 419)
Function "_handle_status_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 428)
Function "_handle_current_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 457)
Function "_handle_next_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 493)
Function "_handle_back_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 539)
Function "_handle_instructions_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 539)
Function "_handle_instructions_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 593)
Function "_handle_submit_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 593)
Function "_handle_submit_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 614)
Function "_handle_confirm_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 669)
Function "_handle_path_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 688)
Function "_handle_scope_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 688)
Function "_handle_scope_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 804)
Function "_wrap_navigation_with_instructions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 808)
Function "_wrap_with_context_header" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 808)
Function "_wrap_with_context_header" uses parameter name "content" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 808)
Function "_wrap_with_context_header" uses parameter name "response_msg" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 864)
Function "_handle_dot_notation" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 864)
Function "_handle_dot_notation" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 992)
Function "_handle_action_shortcut" uses parameter name "args_str" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1053)
Function "_tokenize_cli_args" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1053)
Function "_tokenize_cli_args" uses parameter name "args_str" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1060)
Function "_execute_action_with_args" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1060)
Function "_execute_action_with_args" uses parameter name "operation" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1134)
Function "display_confirm_prompt" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1159)
Function "parse_command_parameters" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1173)
Function "parse_scope_from_string" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1173)
Function "parse_scope_from_string" uses parameter name "scope_str" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1182)
Function "get_stored_scope" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1192)
Function "_get_scope_display_lines" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1216)
Function "_find_scope_matches" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1216)
Function "_find_scope_matches" uses parameter name "scope_values" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1229)
Function "_search_for_scope_match" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1229)
Function "_search_for_scope_match" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1240)
Function "_search_sub_epics" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1251)
Function "_search_stories" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1251)
Function "_search_stories" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1263)
Function "_matches_name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1263)
Function "_matches_name" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1263)
Function "_matches_name" uses parameter name "pattern" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1266)
Function "_format_node_with_children" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1266)
Function "_format_node_with_children" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1266)
Function "_format_node_with_children" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 1266)
Function "_format_node_with_children" uses parameter name "indent" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**active_language_scanner.py** - 24 violation(s)

[i] INFO (line 18)
Function "scan_story_node" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 41)
Function "_check_actor_in_name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 41)
Function "_check_actor_in_name" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 41)
Function "_check_actor_in_name" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 41)
Function "_check_actor_in_name" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 75)
Function "_get_node_type" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 75)
Function "_get_node_type" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 84)
Function "_check_passive_voice" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 84)
Function "_check_passive_voice" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 84)
Function "_check_passive_voice" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 84)
Function "_check_passive_voice" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 96)
Function "_create_passive_voice_violation" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 96)
Function "_create_passive_voice_violation" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 96)
Function "_create_passive_voice_violation" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 96)
Function "_create_passive_voice_violation" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 105)
Function "_check_capability_nouns" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 105)
Function "_check_capability_nouns" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 105)
Function "_check_capability_nouns" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 105)
Function "_check_capability_nouns" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 127)
Function "_create_capability_noun_violation" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 127)
Function "_create_capability_noun_violation" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 127)
Function "_create_capability_noun_violation" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 127)
Function "_create_capability_noun_violation" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 127)
Function "_create_capability_noun_violation" uses parameter name "noun_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**resource_oriented_code_scanner.py** - 4 violation(s)

[i] INFO (line 24)
Function "scan_file" uses parameter name "knowledge_graph" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 28)
Function "scan_cross_file" uses parameter name "status_writer" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 88)
Function "_is_owned_by_domain_object" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 88)
Function "_is_owned_by_domain_object" uses parameter name "loader_node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**resource_oriented_design_scanner.py** - 2 violation(s)

[i] INFO (line 19)
Function "scan_domain_concept" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 19)
Function "scan_domain_concept" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**scanner_execution_error.py** - 2 violation(s)

[i] INFO (line 4)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 4)
Function "__init__" uses parameter name "original_error" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**story_map.py** - 34 violation(s)

[i] INFO (line 18)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 28)
Function "children" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 32)
Function "name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 35)
Function "map_location" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 35)
Function "map_location" uses parameter name "field" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 60)
Function "children" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 76)
Function "all_stories" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 93)
Function "children" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 113)
Function "children" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 127)
Function "steps" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 145)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 151)
Function "name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 155)
Function "type" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 159)
Function "background" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 166)
Function "map_location" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 166)
Function "map_location" uses parameter name "field" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 173)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 179)
Function "name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 183)
Function "type" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 187)
Function "background" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 191)
Function "examples" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 195)
Function "examples_columns" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 199)
Function "examples_rows" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 206)
Function "map_location" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 206)
Function "map_location" uses parameter name "field" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 214)
Function "sizing" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 218)
Function "users" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 226)
Function "connector" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 230)
Function "sequential_order" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 261)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 261)
Function "__init__" uses parameter name "knowledge_graph" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 265)
Function "from_bot" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 299)
Function "walk" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 299)
Function "walk" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**technical_abstraction_scanner.py** - 2 violation(s)

[i] INFO (line 24)
Function "scan_domain_concept" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 24)
Function "scan_domain_concept" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**verb_noun_scanner.py** - 45 violation(s)

[i] INFO (line 30)
Function "scan_domain_concept" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 30)
Function "scan_domain_concept" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 33)
Function "scan_story_node" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 72)
Function "_get_node_type" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 72)
Function "_get_node_type" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 81)
Function "_get_tokens_and_tags" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 81)
Function "_get_tokens_and_tags" uses parameter name "text" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 90)
Function "_is_verb" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 90)
Function "_is_verb" uses parameter name "tag" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 94)
Function "_is_noun" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 94)
Function "_is_noun" uses parameter name "tag" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 98)
Function "_is_proper_noun" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 98)
Function "_is_proper_noun" uses parameter name "tag" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 102)
Function "_can_be_verb" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 102)
Function "_can_be_verb" uses parameter name "word" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 119)
Function "_check_verb_noun_order" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 119)
Function "_check_verb_noun_order" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 119)
Function "_check_verb_noun_order" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 119)
Function "_check_verb_noun_order" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 137)
Function "_check_gerund_ending" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 137)
Function "_check_gerund_ending" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 137)
Function "_check_gerund_ending" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 137)
Function "_check_gerund_ending" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 158)
Function "_check_third_person_singular" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 158)
Function "_check_third_person_singular" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 158)
Function "_check_third_person_singular" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 158)
Function "_check_third_person_singular" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 183)
Function "_convert_to_base_form" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 183)
Function "_convert_to_base_form" uses parameter name "verb" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 217)
Function "_check_noun_verb_noun_pattern" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 217)
Function "_check_noun_verb_noun_pattern" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 217)
Function "_check_noun_verb_noun_pattern" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 217)
Function "_check_noun_verb_noun_pattern" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 247)
Function "_check_noun_verb_pattern" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 247)
Function "_check_noun_verb_pattern" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 247)
Function "_check_noun_verb_pattern" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 247)
Function "_check_noun_verb_pattern" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 311)
Function "_check_actor_prefix" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 311)
Function "_check_actor_prefix" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 311)
Function "_check_actor_prefix" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 311)
Function "_check_actor_prefix" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 330)
Function "_check_noun_only" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 330)
Function "_check_noun_only" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 330)
Function "_check_noun_only" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 330)
Function "_check_noun_only" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**vocabulary_helper.py** - 18 violation(s)

[i] INFO (line 28)
Class "VocabularyHelper" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 38)
Function "is_verb" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 38)
Function "is_verb" uses parameter name "word" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 48)
Function "is_noun" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 48)
Function "is_noun" uses parameter name "word" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 58)
Function "is_agent_noun" uses parameter name "word" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 89)
Function "is_gerund" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 89)
Function "is_gerund" uses parameter name "word" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 127)
Function "get_pos_tags" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 127)
Function "get_pos_tags" uses parameter name "text" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 137)
Function "is_verb_tag" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 137)
Function "is_verb_tag" uses parameter name "tag" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 143)
Function "is_noun_tag" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 143)
Function "is_noun_tag" uses parameter name "tag" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 149)
Function "is_proper_noun_tag" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 149)
Function "is_proper_noun_tag" uses parameter name "tag" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 155)
Function "is_actor_or_role" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 155)
Function "is_actor_or_role" uses parameter name "word" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**rules.py** - 36 violation(s)

[i] INFO (line 38)
Function "from_action_context" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 38)
Function "from_action_context" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 67)
Function "_get_files_for_validation" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 67)
Function "_get_files_for_validation" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 98)
Function "from_parameters" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 137)
Function "get_last_report_timestamp" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 183)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 220)
Function "find_by_name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 227)
Function "__iter__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 232)
Function "__len__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 235)
Function "add_violations" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 235)
Function "add_violations" uses parameter name "violations" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 239)
Function "violations" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 243)
Function "violation_summary" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 295)
Function "_has_scanner_error" uses parameter name "execution_status" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 305)
Function "_extract_error_message" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 305)
Function "_extract_error_message" uses parameter name "execution_status" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 317)
Function "_flush_logger_handlers" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 317)
Function "_flush_logger_handlers" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 321)
Function "_convert_violations_to_dicts" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 331)
Function "_process_scanner_result" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 347)
Function "_execute_scanner" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 347)
Function "_execute_scanner" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 367)
Function "_process_rule" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 367)
Function "_process_rule" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 379)
Function "validate" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 379)
Function "validate" uses parameter name "exclude" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 384)
Function "_create_legacy_context" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 384)
Function "_create_legacy_context" uses parameter name "knowledge_graph" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 384)
Function "_create_legacy_context" uses parameter name "exclude" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 387)
Function "_execute_validation" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 393)
Function "_log_validation_start" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 393)
Function "_log_validation_start" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 408)
Function "_process_all_rules" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 408)
Function "_process_all_rules" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 434)
Function "_log_scanner_status_summary" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**rule_loader.py** - 3 violation(s)

[i] INFO (line 10)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 52)
Function "_load_rules_from_subdir" uses parameter name "subdir" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 67)
Function "_is_in_disabled_folder" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**strategy_action.py** - 17 violation(s)

[i] INFO (line 11)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 24)
Function "strategy" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 28)
Function "strategy_criteria" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 32)
Function "typical_assumptions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 35)
Function "_prepare_instructions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 35)
Function "_prepare_instructions" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 35)
Function "_prepare_instructions" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 39)
Function "_do_submit" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 39)
Function "_do_submit" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 71)
Function "_format_instructions_for_display" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 71)
Function "_format_instructions_for_display" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 106)
Function "_format_option" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 106)
Function "_format_option" uses parameter name "option" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 128)
Function "do_execute" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 128)
Function "do_execute" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 136)
Function "save_strategy" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 136)
Function "save_strategy" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**validate_action.py** - 13 violation(s)

[i] INFO (line 15)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 32)
Function "_prepare_instructions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 32)
Function "_prepare_instructions" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 32)
Function "_prepare_instructions" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 74)
Function "_run_scanners_and_format_results" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 117)
Function "_format_scope_description" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 117)
Function "_format_scope_description" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 181)
Function "_do_submit" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 181)
Function "_do_submit" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 195)
Function "do_execute" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 195)
Function "do_execute" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 222)
Function "finalize_and_transition" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 226)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**validation_report_writer.py** - 40 violation(s)

[i] INFO (line 28)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 28)
Function "__init__" uses parameter name "timestamp" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 43)
Function "start" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 63)
Function "on_file_scanned" uses parameter name "violations" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 76)
Function "_write_file_violations_header" uses parameter name "count" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 81)
Function "_write_violations" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 81)
Function "_write_violations" uses parameter name "violations" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 85)
Function "_extract_violation_fields" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 85)
Function "_extract_violation_fields" uses parameter name "violation" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 96)
Function "_write_single_violation" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 96)
Function "_write_single_violation" uses parameter name "violation" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 115)
Function "_handle_executed_status" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 125)
Function "_check_for_errors" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 134)
Function "finish" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 134)
Function "finish" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 145)
Function "_write_line" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 145)
Function "_write_line" uses parameter name "line" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 149)
Function "_flush" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 153)
Function "write_cross_file_progress" uses parameter name "message" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 163)
Function "timestamp" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 168)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 168)
Function "__init__" uses parameter name "timestamp" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 184)
Function "_check_violation_severities" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 199)
Function "_check_violations_in_key" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 212)
Function "write" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 212)
Function "write" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 222)
Function "_write_report_file" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 237)
Function "_write_section" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 237)
Function "_write_section" uses parameter name "lines" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 241)
Function "_log_write_error" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 254)
Function "get_report_hyperlink" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 271)
Function "_build_report_lines" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 271)
Function "_build_report_lines" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 284)
Function "_build_scanned_files_section" uses parameter name "section_title" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 299)
Function "_format_violation_line" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 299)
Function "_format_violation_line" uses parameter name "violation" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 324)
Function "_extract_test_info" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 324)
Function "_extract_test_info" uses parameter name "message" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 324)
Function "_extract_test_info" uses parameter name "location" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 324)
Function "_extract_test_info" uses parameter name "line_number" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**validation_scope.py** - 11 violation(s)

[i] INFO (line 16)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 29)
Function "from_context" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 29)
Function "from_context" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 29)
Function "from_context" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 63)
Function "_build_scope" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 71)
Function "_handle_scope_parameter" uses parameter name "scope_value" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 98)
Function "files" uses parameter name "key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 105)
Function "_auto_discover_if_needed" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 105)
Function "_auto_discover_if_needed" uses parameter name "key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 200)
Function "_discover_files_from_directory" uses parameter name "dir_name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 203)
Function "_auto_discover_files" uses parameter name "key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**error_recovery.py** - 14 violation(s)

[i] INFO (line 11)
Class "ErrorRecovery" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 13)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 13)
Function "__init__" uses parameter name "max_attempts" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 13)
Function "__init__" uses parameter name "current_attempts" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 13)
Function "__init__" uses parameter name "wait_time" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 24)
Function "can_retry" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 27)
Function "increment_attempt" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 30)
Function "wait_before_retry" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 30)
Function "wait_before_retry" uses parameter name "duration" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 33)
Function "is_recoverable" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 33)
Function "is_recoverable" uses parameter name "error" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 36)
Function "determines_if_error_is_recoverable" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 36)
Function "determines_if_error_is_recoverable" uses parameter name "error" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 39)
Function "raise_if_max_attempts_exceeded" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**execution_context.py** - 10 violation(s)

[i] INFO (line 7)
Class "ExecutionContext" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 13)
Function "loads_from_context_file" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 21)
Function "_parses_content" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 21)
Function "_parses_content" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 21)
Function "_parses_content" uses parameter name "content" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 34)
Class "_ContextSections" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 36)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 42)
Function "processes_line" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 42)
Function "processes_line" uses parameter name "line" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 53)
Function "_appends_list_item" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**execution_result.py** - 20 violation(s)

[i] INFO (line 7)
Class "ExecutionResult" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 37)
Function "had_not_done_responses" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 40)
Function "set_blocked_at_operation" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 40)
Function "set_blocked_at_operation" uses parameter name "operation" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 40)
Function "set_blocked_at_operation" uses parameter name "operations_executed" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 53)
Function "creates_blocked" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 53)
Function "creates_blocked" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 53)
Function "creates_blocked" uses parameter name "session_id" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 53)
Function "creates_blocked" uses parameter name "context_loaded" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 53)
Function "creates_blocked" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 53)
Function "creates_blocked" uses parameter name "loop_count" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 53)
Function "creates_blocked" uses parameter name "loop_responses" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 80)
Function "creates_completed" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 80)
Function "creates_completed" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 80)
Function "creates_completed" uses parameter name "session_id" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 80)
Function "creates_completed" uses parameter name "context_loaded" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 80)
Function "creates_completed" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 80)
Function "creates_completed" uses parameter name "loop_count" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 80)
Function "creates_completed" uses parameter name "loop_responses" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 80)
Function "creates_completed" uses parameter name "completed" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**headless_config.py** - 6 violation(s)

[i] INFO (line 9)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 9)
Function "__init__" uses parameter name "api_key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 9)
Function "__init__" uses parameter name "log_dir" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 14)
Function "load" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 14)
Function "load" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 33)
Function "api_key_prefix" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**headless_session.py** - 17 violation(s)

[i] INFO (line 13)
Class "HeadlessSession" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 15)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 21)
Function "invokes" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 21)
Function "invokes" uses parameter name "message" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 45)
Function "invokes_operation" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 45)
Function "invokes_operation" uses parameter name "operation" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 120)
Function "_load_context" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 125)
Function "_prepare_instructions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 125)
Function "_prepare_instructions" uses parameter name "message" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 125)
Function "_prepare_instructions" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 153)
Function "_execute_with_monitoring" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 153)
Function "_execute_with_monitoring" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 153)
Function "_execute_with_monitoring" uses parameter name "context_loaded" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 153)
Function "_execute_with_monitoring" uses parameter name "should_block" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 201)
Function "_simulate_ai_execution" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 201)
Function "_simulate_ai_execution" uses parameter name "loop_count" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 201)
Function "_simulate_ai_execution" uses parameter name "should_block" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**non_recoverable_error.py** - 3 violation(s)

[i] INFO (line 1)
Class "NonRecoverableError" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 3)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 3)
Function "__init__" uses parameter name "message" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**recoverable_error.py** - 3 violation(s)

[i] INFO (line 1)
Class "RecoverableError" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 3)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 3)
Function "__init__" uses parameter name "message" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**session_log.py** - 9 violation(s)

[i] INFO (line 6)
Class "SessionLog" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 8)
Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 15)
Function "creates_with_timestamped_path" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 15)
Function "creates_with_timestamped_path" uses parameter name "base_dir" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 20)
Function "appends_response" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 20)
Function "appends_response" uses parameter name "response" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 34)
Function "appends_total_loops" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 34)
Function "appends_total_loops" uses parameter name "total_loops" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 39)
Function "get_transcript" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

Completed: 2025-12-29 17:46:54
Total violations: 621
Scanners executed: 29
