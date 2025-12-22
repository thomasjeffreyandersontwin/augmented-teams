# Validation Status - tests
Started: 2025-12-22 13:23:51
Files: 1


## Cross-File Duplication Analysis
Scanning 1 files...
Extracted 56 code blocks
Starting 1540 pairwise comparisons...
Comparing: 5% (77/1,540) - 0 violations - ETA: 19s  
Comparing: 10% (154/1,540) - 0 violations - ETA: 9s  
Comparing: 15% (231/1,540) - 0 violations - ETA: 5s  
Comparing: 20% (308/1,540) - 0 violations - ETA: 4s  
Comparing: 25% (385/1,540) - 0 violations - ETA: 3s  
Comparing: 30% (462/1,540) - 0 violations - ETA: 2s  
Comparing: 35% (539/1,540) - 0 violations - ETA: 1s  
Comparing: 40% (616/1,540) - 0 violations - ETA: 1s  
Comparing: 45% (693/1,540) - 0 violations - ETA: 1s  
Comparing: 50% (770/1,540) - 0 violations - ETA: 1s  
Comparing: 55% (847/1,540) - 0 violations - ETA: 0s  
Comparing: 60% (924/1,540) - 0 violations - ETA: 0s  
Comparing: 65% (1,001/1,540) - 0 violations - ETA: 0s  
Comparing: 70% (1,078/1,540) - 0 violations - ETA: 0s  
Comparing: 75% (1,155/1,540) - 0 violations - ETA: 0s  
Comparing: 80% (1,232/1,540) - 0 violations - ETA: 0s  
Comparing: 85% (1,309/1,540) - 0 violations - ETA: 0s  
Comparing: 90% (1,386/1,540) - 0 violations - ETA: 0s  
Comparing: 95% (1,463/1,540) - 0 violations - ETA: 0s  
Comparing: 100% (1,540/1,540) - 0 violations - ETA: 0s  
Complete: 1540 comparisons, 0 violations

## no_fallbacks_in_tests
**class_based_organization_scanner.py** - 5 violation(s)

[X] ERROR (line 147)
Line 147 uses fallback/default value - tests should use explicit test data, not fallbacks

[X] ERROR (line 152)
Line 152 uses fallback/default value - tests should use explicit test data, not fallbacks

[X] ERROR (line 159)
Line 159 uses fallback/default value - tests should use explicit test data, not fallbacks

[X] ERROR (line 419)
Line 419 uses fallback/default value - tests should use explicit test data, not fallbacks

[X] ERROR (line 426)
Line 426 uses fallback/default value - tests should use explicit test data, not fallbacks

---

## production_code_small_functions
**class_based_organization_scanner.py** - 1 violation(s)

[!] WARNING (line 17)
Function "scan_file" is 29 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return []  # Test scanning happens in scan_test_file, not scan_story_node
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        if not file_path.exists():
            return violations
        
        sub_epic_names = self._extract_sub_epic_names(knowledge_graph)
        file_name = file_path.stem  # Without .py extension
        violation = self._check_file_name_matches_sub_epic(file_name, sub_epic_names, file_path, rule_obj, knowledge_graph)
        if violation:
            violations.append(violation)
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
        
        content, lines, tree = parsed
        
        story_names = self._extract_story_names(knowledge_graph)
        
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
                                    item.name, node.name, story_names, knowledge_graph, file_path, rule_obj
                                )
                                if violation:
                                    violations.append(violation)
        
        return violations
    
```

---

## use_class_based_organization
**class_based_organization_scanner.py** - 1 violation(s)

[X] ERROR
Test file name "class_based_organization_scanner" does not match any sub-epic name and test methods do not span multiple sub-epics - file should be named test_<sub_epic_name>.py.

---

Completed: 2025-12-22 13:23:52
Total violations: 7
Scanners executed: 25
