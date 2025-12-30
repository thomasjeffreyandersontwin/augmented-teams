# Validation Status - code
Started: 2025-12-30 02:52:21
Files: 275

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


## Cross-File Duplication Analysis
Scanning 2 changed file(s) against 20 total files...
Extracted 32 changed blocks, 325 reference blocks
Starting 10,400 pairwise comparisons...
Comparing: 5% (520/10,400) - 3 violations - ETA: 19s  
Comparing: 10% (1,040/10,400) - 3 violations - ETA: 9s  
Comparing: 15% (1,560/10,400) - 3 violations - ETA: 5s  
Comparing: 20% (2,080/10,400) - 3 violations - ETA: 4s  
Comparing: 25% (2,600/10,400) - 3 violations - ETA: 3s  
Comparing: 30% (3,120/10,400) - 3 violations - ETA: 2s  
Comparing: 35% (3,640/10,400) - 3 violations - ETA: 2s  
Comparing: 40% (4,160/10,400) - 4 violations - ETA: 1s  
Comparing: 45% (4,680/10,400) - 4 violations - ETA: 1s  
Comparing: 50% (5,200/10,400) - 4 violations - ETA: 1s  
Comparing: 55% (5,720/10,400) - 4 violations - ETA: 1s  
Comparing: 60% (6,240/10,400) - 4 violations - ETA: 1s  
Comparing: 65% (6,760/10,400) - 4 violations - ETA: 1s  
Comparing: 70% (7,280/10,400) - 4 violations - ETA: 0s  
Comparing: 75% (7,800/10,400) - 4 violations - ETA: 0s  
Comparing: 80% (8,320/10,400) - 4 violations - ETA: 0s  
Comparing: 85% (8,840/10,400) - 4 violations - ETA: 0s  
Comparing: 90% (9,360/10,400) - 4 violations - ETA: 0s  
Comparing: 95% (9,880/10,400) - 4 violations - ETA: 0s  
Comparing: 100% (10,400/10,400) - 4 violations - ETA: 0s  
Complete: 10400 comparisons, 4 violations

## keep_classes_small_with_single_responsibility
**given_when_then_helpers_scanner.py** - 1 violation(s)

[!] WARNING (line 12)
Class "GivenWhenThenHelpersScanner" is 313 lines - should be under 300 lines (extract related methods into separate classes)

```python


class GivenWhenThenHelpersScanner(TestScanner):
    
    # Minimum number of consecutive non-helper lines to flag as violation
    # Only flag 4+ lines to optimize for reusable functions, not exact step names
    MIN_INLINE_LINES = 4
    
    # Helper function name patterns (these are OK - code calling these is not a violation)
    HELPER_PATTERNS = [
    # ... (truncated)
```

---

## keep_functions_small_focused
**given_when_then_helpers_scanner.py** - 1 violation(s)

[!] WARNING (line 270)
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

## maintain_vertical_density
**given_when_then_helpers_scanner.py** - 2 violation(s)

[i] INFO (line 168)
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

[i] INFO (line 270)
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

## simplify_control_flow
**given_when_then_helpers_scanner.py** - 4 violation(s)

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

[!] WARNING (line 82)
Function "_get_helper_calls_in_file" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

```python
        return helpers
    
    def _get_helper_calls_in_file(self, tree: ast.AST, content: str) -> Set[str]:
        helper_calls = set()
        helper_functions = self._get_helper_functions(tree, content)
        
        # Walk through all call nodes to find helper function calls
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                func_name = None
                if isinstance(node.func, ast.Name):
                    func_name = node.func.id
                elif isinstance(node.func, ast.Attribute):
                    if isinstance(node.func.value, ast.Name) and node.func.value.id == 'self':
                        func_name = node.func.attr
    # ... (truncated)
```

[!] WARNING (line 168)
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
**given_when_then_helpers_scanner.py** - 2 violation(s)

[!] WARNING (line 112)
Function "_check_test_method" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
            return None
    
    def _check_test_method(self, test_node: ast.FunctionDef, content: str, file_path: Path, 
                          rule_obj: Any, helper_functions: Set[str], tree: ast.AST) -> List[Dict[str, Any]]:
        violations = []
    # ... (truncated)
```

[!] WARNING (line 270)
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

## use_domain_language
**given_when_then_helpers_scanner.py** - 28 violation(s)

[i] INFO (line 27)
Function "scan_file" uses parameter name "knowledge_graph" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 48)
Function "_get_helper_functions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 48)
Function "_get_helper_functions" uses parameter name "tree" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 48)
Function "_get_helper_functions" uses parameter name "content" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 69)
Function "_get_defined_helper_functions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 69)
Function "_get_defined_helper_functions" uses parameter name "tree" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 82)
Function "_get_helper_calls_in_file" uses parameter name "tree" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 82)
Function "_get_helper_calls_in_file" uses parameter name "content" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 112)
Function "_check_test_method" uses parameter name "test_node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 112)
Function "_check_test_method" uses parameter name "content" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 112)
Function "_check_test_method" uses parameter name "helper_functions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 112)
Function "_check_test_method" uses parameter name "tree" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 146)
Function "_get_docstring_line_range" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 146)
Function "_get_docstring_line_range" uses parameter name "test_node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 168)
Function "_find_inline_code_blocks" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 168)
Function "_find_inline_code_blocks" uses parameter name "test_node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 168)
Function "_find_inline_code_blocks" uses parameter name "test_body_lines" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 168)
Function "_find_inline_code_blocks" uses parameter name "helper_functions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 168)
Function "_find_inline_code_blocks" uses parameter name "tree" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 243)
Function "_is_helper_function_call" uses parameter name "line" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 243)
Function "_is_helper_function_call" uses parameter name "helper_functions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 243)
Function "_is_helper_function_call" uses parameter name "tree" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 264)
Function "_end_current_block" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 264)
Function "_end_current_block" uses parameter name "blocks" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 264)
Function "_end_current_block" uses parameter name "current_block_start" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 264)
Function "_end_current_block" uses parameter name "end_line" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 264)
Function "_end_current_block" uses parameter name "current_block_lines" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 270)
Function "scan_cross_file" uses parameter name "status_writer" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_domain_language
**resource_oriented_code_scanner.py** - 4 violation(s)

[i] INFO (line 24)
Function "scan_file" uses parameter name "knowledge_graph" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 28)
Function "scan_cross_file" uses parameter name "status_writer" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 89)
Function "_is_owned_by_domain_object" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 89)
Function "_is_owned_by_domain_object" uses parameter name "loader_node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

Completed: 2025-12-30 02:52:27
Total violations: 50
Scanners executed: 30
