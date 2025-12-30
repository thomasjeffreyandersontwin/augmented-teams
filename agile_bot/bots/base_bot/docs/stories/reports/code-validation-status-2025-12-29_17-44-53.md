# Validation Status - code
Started: 2025-12-29 17:44:53
Files: 274

## avoid_excessive_guards
**resource_oriented_code_scanner.py** - 1 violation(s)

[!] WARNING (line 66)
Line 66: Variable truthiness check detected (if is_agent:). Assume variable exists - let code fail fast if missing.

```python
                    # Check if class name is an agent noun using NLTK
                    is_agent, base_verb, suffix = VocabularyHelper.is_agent_noun(cls.node.name)
                    if is_agent:
                        loader_classes[cls.node.name] = (file_path, cls.node, suffix)
            except (SyntaxError, UnicodeDecodeError) as e:
```

---


## Cross-File Duplication Analysis
Scanning 5 changed file(s) against 274 total files...
Extracted 64 changed blocks, 4166 reference blocks
Starting 266,624 pairwise comparisons...
Comparing: 5% (13,332/266,624) - 0 violations - ETA: 53s  
Comparing: 10% (26,663/266,624) - 0 violations - ETA: 50s  
Comparing: 15% (39,994/266,624) - 0 violations - ETA: 55s  
Comparing: 20% (53,325/266,624) - 0 violations - ETA: 58s  
Comparing: 25% (66,656/266,624) - 0 violations - ETA: 59s  
Comparing: 30% (79,988/266,624) - 0 violations - ETA: 59s  
Comparing: 35% (93,319/266,624) - 0 violations - ETA: 59s  
Comparing: 40% (106,650/266,624) - 0 violations - ETA: 59s  
Comparing: 45% (119,981/266,624) - 0 violations - ETA: 58s  
Comparing: 50% (133,312/266,624) - 0 violations - ETA: 51s  
Comparing: 55% (146,644/266,624) - 0 violations - ETA: 44s  
Comparing: 60% (159,975/266,624) - 0 violations - ETA: 39s  
Comparing: 65% (173,306/266,624) - 0 violations - ETA: 34s  
Comparing: 70% (186,637/266,624) - 0 violations - ETA: 30s  
Comparing: 75% (199,968/266,624) - 0 violations - ETA: 25s  
Comparing: 80% (213,300/266,624) - 0 violations - ETA: 20s  
Comparing: 85% (226,631/266,624) - 0 violations - ETA: 15s  
Comparing: 90% (239,962/266,624) - 0 violations - ETA: 10s  
Comparing: 95% (253,293/266,624) - 0 violations - ETA: 5s  
Complete: 263438 comparisons, 0 violations

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

## provide_meaningful_context
**error_recovery.py** - 1 violation(s)

[!] WARNING (line 8)
Line 8 contains magic number - replace with named constant

```python
DEFAULT_MAX_ATTEMPTS = 3
DEFAULT_WAIT_TIME_SECONDS = 60.0

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

Completed: 2025-12-29 17:46:40
Total violations: 12
Scanners executed: 30
