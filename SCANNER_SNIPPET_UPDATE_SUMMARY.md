# Scanner Code Snippet Update Summary

## What Was Done

Updated the base `CodeScanner` class and key scanners to automatically include code snippets in all validation violations. This makes it much easier to understand and fix violations by showing the actual problematic code.

## Scanners Updated (with code snippets now working)

### High-Impact Scanners (Most Violations)
1. ✅ **simplify_control_flow_scanner.py** (159 violations) - Shows nested code
2. ✅ **meaningful_context_scanner.py** (106 violations) - Shows magic numbers and numbered variables
3. ✅ **vertical_density_scanner.py** (59 violations) - Shows long functions
4. ✅ **clear_parameters_scanner.py** (59 violations) - Shows function signatures with too many params
5. ✅ **class_size_scanner.py** (13 violations) - Shows large classes

### Already Had Snippets
- function_size_scanner.py
- type_safety_scanner.py
- separate_concerns_scanner.py
- abstraction_levels_scanner.py

## The Pattern

All scanners should follow this pattern (borrowed from `function_size_scanner.py`):

### Step 1: Get content from `_read_and_parse_file()`

```python
def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    violations = []
    
    parsed = self._read_and_parse_file(file_path)
    if not parsed:
        return violations
    
    content, lines, tree = parsed  # ← Get content here
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            violation = self._check_something(node, file_path, rule_obj, content)  # ← Pass content
            if violation:
                violations.append(violation)
    
    return violations
```

### Step 2: Pass content to helper methods

```python
def _check_something(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any, content: str) -> Optional[Dict[str, Any]]:
    # ↑ Add content parameter
```

### Step 3: Replace `Violation()` with `_create_violation_with_snippet()`

**OLD (no snippet):**
```python
return Violation(
    rule=rule_obj,
    violation_message=f'Problem description',
    location=str(file_path),
    line_number=line_number,
    severity='warning'
).to_dict()
```

**NEW (with snippet):**
```python
return self._create_violation_with_snippet(
    rule_obj=rule_obj,
    violation_message=f'Problem description',
    file_path=file_path,
    line_number=line_number,
    severity='warning',
    content=content,
    ast_node=func_node,  # Or use start_line/end_line for line-based checks
    max_lines=10  # Adjust based on what makes sense
)
```

## Remaining Scanners to Update

90 scanners still need updating. They all follow the same pattern - just need to:
1. Pass `content` from `_read_and_parse_file()` to helper methods
2. Replace `Violation(...).to_dict()` with `self._create_violation_with_snippet(...)`
3. Add `content=content` and either `ast_node=node` or `start_line/end_line` parameters

### Priority Scanners (Most Violations)
- excessive_guards_scanner.py (18 violations)
- import_placement_scanner.py (7 violations)
- encapsulation_scanner.py (6 violations)
- dependency_chaining_code_scanner.py (5 violations)
- delegation_code_scanner.py (3 violations)

## Benefits

- **Before**: Violations just showed line numbers and messages
- **After**: Violations show the actual code causing the problem with context

Example output now includes:
```
Function "parse_complex_data" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

```python
def parse_complex_data(self, data: Dict[str, Any]) -> Result:
    if data:
        if 'items' in data:
            for item in data['items']:
                if item.get('valid'):
                    if item['type'] == 'special':
                        # ... deeply nested code ...
```

This makes it immediately clear what needs to be fixed!




