# Validation Status - code
Started: 2025-12-29 17:45:58
Files: 1

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
Scanning 1 changed file(s) against 1 total files...
Extracted 7 changed blocks, 7 reference blocks
Starting 49 pairwise comparisons...
Complete: 0 comparisons, 0 violations

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

Completed: 2025-12-29 17:46:01
Total violations: 8
Scanners executed: 30
