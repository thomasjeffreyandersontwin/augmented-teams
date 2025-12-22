# Validation Status - code
Started: 2025-12-21 19:09:30
Files: 1

## chain_dependencies_properly
**prefer_object_model_over_config_scanner.py** - 1 violation(s)

[!] WARNING (line 36)
Method "scan_file" in class "PreferObjectModelOverConfigScanner" takes parameter "rule_obj" that is already injected in __init__. Use self.rule_obj instead.

---

## keep_functions_small_focused
**prefer_object_model_over_config_scanner.py** - 1 violation(s)

[!] WARNING (line 36)
Function "scan_file" is 39 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        ]
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Dict[str, Any] = None) -> List[Violation]:
        violations = []
        
        # Need rule_obj to create violations
        effective_rule_obj = rule_obj if rule_obj is not None else self.rule_obj
        if not effective_rule_obj:
            return violations
        
        # Store rule_obj and file_path for creating violations
        self.rule_obj = effective_rule_obj
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
    # ... (truncated)
```

---

## simplify_control_flow
**prefer_object_model_over_config_scanner.py** - 1 violation(s)

[!] WARNING (line 100)
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

Completed: 2025-12-21 19:09:31
Total violations: 3
Scanners executed: 30
