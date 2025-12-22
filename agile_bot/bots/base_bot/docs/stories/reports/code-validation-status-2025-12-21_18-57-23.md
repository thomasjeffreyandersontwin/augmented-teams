# Validation Status - code
Started: 2025-12-21 18:57:23
Files: 9


## Cross-File Duplication Analysis
Scanning 9 files...
Extracted 288 code blocks
Starting 41328 pairwise comparisons...
Comparing: 5% (2,067/41,328) - 0 violations - ETA: 18s  
Comparing: 10% (4,133/41,328) - 0 violations - ETA: 10s  
Comparing: 15% (6,200/41,328) - 0 violations - ETA: 8s  
Comparing: 20% (8,266/41,328) - 0 violations - ETA: 7s  
Comparing: 25% (10,332/41,328) - 0 violations - ETA: 7s  
Comparing: 30% (12,399/41,328) - 0 violations - ETA: 7s  
Comparing: 35% (14,465/41,328) - 0 violations - ETA: 7s  
Comparing: 40% (16,532/41,328) - 0 violations - ETA: 7s  
Comparing: 45% (18,598/41,328) - 0 violations - ETA: 6s  
Comparing: 50% (20,664/41,328) - 0 violations - ETA: 6s  
Comparing: 55% (22,731/41,328) - 0 violations - ETA: 5s  
Comparing: 60% (24,797/41,328) - 0 violations - ETA: 5s  
Comparing: 65% (26,864/41,328) - 0 violations - ETA: 4s  
Comparing: 70% (28,930/41,328) - 0 violations - ETA: 4s  
Comparing: 75% (30,996/41,328) - 0 violations - ETA: 3s  
Comparing: 80% (33,063/41,328) - 0 violations - ETA: 2s  
Comparing: 85% (35,129/41,328) - 0 violations - ETA: 2s  
Comparing: 90% (37,196/41,328) - 0 violations - ETA: 1s  
Comparing: 95% (39,262/41,328) - 0 violations - ETA: 0s  
Comparing: 100% (41,328/41,328) - 0 violations - ETA: 0s  
Complete: 41328 comparisons, 0 violations

## maintain_vertical_density
**business_readable_test_names_scanner.py** - 1 violation(s)

[i] INFO (line 112)
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

## use_clear_function_parameters
**business_readable_test_names_scanner.py** - 2 violation(s)

[!] WARNING (line 31)
Function "_check_test_function_node" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return violations
    
    def _check_test_function_node(self, node: Any, file_path: Path, rule_obj: Any, domain_language: set, violations: list) -> None:
        if not isinstance(node, ast.FunctionDef):
            return
    # ... (truncated)
```

[!] WARNING (line 112)
Function "_check_business_readable" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return set(words)
    
    def _check_business_readable(self, test_name: str, file_path: Path, node: ast.FunctionDef, rule_obj: Any, domain_language: set) -> Optional[Dict[str, Any]]:
        name_without_prefix = test_name[5:] if test_name.startswith('test_') else test_name
        
    # ... (truncated)
```

---

Completed: 2025-12-21 18:57:36
Total violations: 3
Scanners executed: 30
