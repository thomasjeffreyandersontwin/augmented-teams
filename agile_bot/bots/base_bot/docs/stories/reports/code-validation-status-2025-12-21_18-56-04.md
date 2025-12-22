# Validation Status - code
Started: 2025-12-21 18:56:04
Files: 9


## Cross-File Duplication Analysis
Scanning 9 files...
Extracted 288 code blocks
Starting 41328 pairwise comparisons...
Comparing: 5% (2,067/41,328) - 0 violations - ETA: 18s  
Comparing: 10% (4,133/41,328) - 0 violations - ETA: 12s  
Comparing: 15% (6,200/41,328) - 0 violations - ETA: 9s  
Comparing: 20% (8,266/41,328) - 0 violations - ETA: 8s  
Comparing: 25% (10,332/41,328) - 0 violations - ETA: 8s  
Comparing: 30% (12,399/41,328) - 0 violations - ETA: 8s  
Comparing: 35% (14,465/41,328) - 0 violations - ETA: 7s  
Comparing: 40% (16,532/41,328) - 0 violations - ETA: 7s  
Comparing: 45% (18,598/41,328) - 0 violations - ETA: 7s  
Comparing: 50% (20,664/41,328) - 0 violations - ETA: 6s  
Comparing: 55% (22,731/41,328) - 0 violations - ETA: 6s  
Comparing: 60% (24,797/41,328) - 0 violations - ETA: 5s  
Comparing: 65% (26,864/41,328) - 0 violations - ETA: 5s  
Comparing: 70% (28,930/41,328) - 0 violations - ETA: 4s  
Comparing: 75% (30,996/41,328) - 0 violations - ETA: 3s  
Comparing: 80% (33,063/41,328) - 0 violations - ETA: 2s  
Comparing: 85% (35,129/41,328) - 0 violations - ETA: 2s  
Comparing: 90% (37,196/41,328) - 0 violations - ETA: 1s  
Comparing: 95% (39,262/41,328) - 0 violations - ETA: 0s  
Comparing: 100% (41,328/41,328) - 0 violations - ETA: 0s  
Complete: 41328 comparisons, 0 violations

## enforce_encapsulation
**cli_executor.py** - 1 violation(s)

[!] WARNING (line 73)
Method "_output_result" in class "CliExecutor" has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

---

## keep_functions_small_focused
**cli_parser_generator.py** - 1 violation(s)

[!] WARNING (line 35)
Function "generate_parsers_for_bot" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        self._generated_lines: List[str] = []
    
    def generate_parsers_for_bot(self, bot) -> str:
        self._generated_lines = []
        self._add_header()
        self._add_imports()
        
        # Collect all unique context classes
        context_classes_seen = set()
        action_mappings = []
        
        for behavior in bot.behaviors:
            for action in behavior.actions:
                context_class = action.context_class
                action_name = action.action_name
                
                if context_class not in context_classes_seen:
                    context_classes_seen.add(context_class)
                    self._generate_parser_function(context_class)
                
                # Record mapping
                action_mappings.append((behavior.name, action_name, context_class.__name__))
        
        self._add_blank_line()
        self._generate_context_builder_functions()
        self._add_blank_line()
        self._generate_action_parser_mapping(action_mappings)
        
        return '\n'.join(self._generated_lines)
    
```

---

## maintain_vertical_density
**business_readable_test_names_scanner.py** - 1 violation(s)

[i] INFO (line 107)
Function "_check_business_readable" is 71 lines - consider improving vertical density by declaring variables near usage

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

## never_swallow_exceptions
**behavior_matcher.py** - 1 violation(s)

[X] ERROR (line 86)
Except block only contains pass at line 86 - exceptions must be logged or rethrown, never swallowed

---

## provide_meaningful_context
**cli_parser_generator.py** - 1 violation(s)

[!] WARNING (line 248)
Line 248 uses numbered variable "s1" - use meaningful descriptive name

```python
        import re
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
```

---

## simplify_control_flow
**business_readable_test_names_scanner.py** - 1 violation(s)

[!] WARNING (line 16)
Function "scan_file" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
class BusinessReadableTestNamesScanner(TestScanner):
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
        
        content, lines, tree = parsed
        
        domain_language = self._extract_domain_language(knowledge_graph)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
    # ... (truncated)
```

---

## use_clear_function_parameters
**business_readable_test_names_scanner.py** - 1 violation(s)

[!] WARNING (line 107)
Function "_check_business_readable" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return set(words)
    
    def _check_business_readable(self, test_name: str, file_path: Path, node: ast.FunctionDef, rule_obj: Any, domain_language: set) -> Optional[Dict[str, Any]]:
        name_without_prefix = test_name[5:] if test_name.startswith('test_') else test_name
        
    # ... (truncated)
```

---

## use_domain_language
**cli_parser_generator.py** - 1 violation(s)

[!] WARNING (line 252)
Function "generate_parsers_for_story_bot" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").

---

Completed: 2025-12-21 18:56:22
Total violations: 8
Scanners executed: 30
