# Validation Status - code
Started: 2025-12-30 02:51:44
Files: 275


## Cross-File Duplication Analysis
Scanning 1 changed file(s) against 20 total files...
Extracted 13 changed blocks, 325 reference blocks
Starting 4,225 pairwise comparisons...
Comparing: 5% (212/4,225) - 0 violations - ETA: 18s  
Comparing: 10% (423/4,225) - 0 violations - ETA: 8s  
Comparing: 15% (634/4,225) - 1 violations - ETA: 5s  
Comparing: 20% (845/4,225) - 1 violations - ETA: 4s  
Comparing: 25% (1,057/4,225) - 1 violations - ETA: 2s  
Comparing: 30% (1,268/4,225) - 1 violations - ETA: 2s  
Comparing: 35% (1,479/4,225) - 1 violations - ETA: 1s  
Comparing: 40% (1,690/4,225) - 1 violations - ETA: 1s  
Comparing: 45% (1,902/4,225) - 1 violations - ETA: 1s  
Comparing: 50% (2,113/4,225) - 1 violations - ETA: 0s  
Comparing: 55% (2,324/4,225) - 1 violations - ETA: 0s  
Comparing: 60% (2,535/4,225) - 1 violations - ETA: 0s  
Comparing: 65% (2,747/4,225) - 1 violations - ETA: 0s  
Comparing: 70% (2,958/4,225) - 1 violations - ETA: 0s  
Comparing: 75% (3,169/4,225) - 2 violations - ETA: 0s  
Comparing: 80% (3,380/4,225) - 4 violations - ETA: 0s  
Comparing: 85% (3,592/4,225) - 4 violations - ETA: 0s  
Comparing: 90% (3,803/4,225) - 5 violations - ETA: 0s  
Comparing: 95% (4,014/4,225) - 7 violations - ETA: 0s  
Complete: 4056 comparisons, 7 violations

## keep_classes_small_with_single_responsibility
**code_scanner.py** - 1 violation(s)

[!] WARNING (line 11)
Class "CodeScanner" is 306 lines - should be under 300 lines (extract related methods into separate classes)

```python


class CodeScanner(Scanner):
    
    def scan(
        self, 
        knowledge_graph: Dict[str, Any], 
        rule_obj: Any = None,
        test_files: Optional[List['Path']] = None,
        code_files: Optional[List['Path']] = None,
    # ... (truncated)
```

---

## maintain_vertical_density
**code_scanner.py** - 1 violation(s)

[i] INFO (line 44)
Function "_extract_domain_terms" is 106 lines - consider improving vertical density by declaring variables near usage

```python
        return []
    
    def _extract_domain_terms(self, knowledge_graph: Dict[str, Any]) -> set:
        domain_terms = set()
        
        # These are domain concepts, not technical jargon
        common_domain_terms = {
            'json', 'data', 'param', 'params', 'parameter', 'parameters',
            'var', 'vars', 'variable', 'variables',
            'method', 'methods', 'class', 'classes', 'call', 'calls',
    # ... (truncated)
```

---

## provide_meaningful_context
**code_scanner.py** - 7 violation(s)

[!] WARNING (line 245)
Line 245 uses numbered variable "start_line_0" - use meaningful descriptive name

```python
            # Use AST node to determine lines
            start_line_0 = ast_node.lineno - 1 if hasattr(ast_node, 'lineno') and ast_node.lineno else 0
            
```

[!] WARNING (line 248)
Line 248 uses numbered variable "end_line_0" - use meaningful descriptive name

```python
            if hasattr(ast_node, 'end_lineno') and ast_node.end_lineno:
                end_line_0 = ast_node.end_lineno  # end_lineno is 1-indexed, exclusive
            else:
```

[!] WARNING (line 251)
Line 251 uses numbered variable "end_line_0" - use meaningful descriptive name

```python
                # Estimate end by finding the maximum line number in the subtree
                end_line_0 = start_line_0 + 1
                for node in ast.walk(ast_node):
```

[!] WARNING (line 257)
Line 257 uses numbered variable "start_line_0" - use meaningful descriptive name

```python
            # Use provided line numbers (1-indexed, convert to 0-indexed)
            start_line_0 = start_line - 1
            if end_line is not None:
```

[!] WARNING (line 259)
Line 259 uses numbered variable "end_line_0" - use meaningful descriptive name

```python
            if end_line is not None:
                end_line_0 = end_line  # end_line is 1-indexed, exclusive (like end_lineno)
            else:
```

[!] WARNING (line 261)
Line 261 uses numbered variable "end_line_0" - use meaningful descriptive name

```python
            else:
                end_line_0 = start_line_0 + 1
        else:
```

[!] WARNING (line 254)
Line 254 uses numbered variable "end_line_0" - use meaningful descriptive name

```python
                    if hasattr(node, 'lineno') and node.lineno:
                        end_line_0 = max(end_line_0, node.lineno)
        elif start_line is not None:
```

---

## simplify_control_flow
**code_scanner.py** - 2 violation(s)

[!] WARNING (line 44)
Function "_extract_domain_terms" has nesting depth of 12 - use guard clauses and extract nested blocks to reduce nesting

```python
        return []
    
    def _extract_domain_terms(self, knowledge_graph: Dict[str, Any]) -> set:
        domain_terms = set()
        
        # These are domain concepts, not technical jargon
        common_domain_terms = {
            'json', 'data', 'param', 'params', 'parameter', 'parameters',
            'var', 'vars', 'variable', 'variables',
            'method', 'methods', 'class', 'classes', 'call', 'calls',
            'config', 'configuration', 'configurations',
            'agent', 'bot', 'workflow', 'story', 'epic', 'scenario', 'action',
            'behavior', 'rule', 'rules', 'validation', 'validate', 'scanner',
            'file', 'files', 'directory', 'directories', 'path', 'paths',
            'state', 'states', 'tool', 'tools', 'server', 'catalog', 'metadata'
    # ... (truncated)
```

[!] WARNING (line 237)
Function "_extract_code_snippet" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

```python
        return parsed_files
    
    def _extract_code_snippet(self, content: str, ast_node: Optional[ast.AST] = None, 
                             start_line: Optional[int] = None, end_line: Optional[int] = None,
                             context_before: int = 2, max_lines: int = 50) -> str:
        lines = content.split('\n')
        
        # Determine start and end lines
        if ast_node is not None:
            # Use AST node to determine lines
            start_line_0 = ast_node.lineno - 1 if hasattr(ast_node, 'lineno') and ast_node.lineno else 0
            
            if hasattr(ast_node, 'end_lineno') and ast_node.end_lineno:
                end_line_0 = ast_node.end_lineno  # end_lineno is 1-indexed, exclusive
            else:
    # ... (truncated)
```

---

## use_clear_function_parameters
**code_scanner.py** - 4 violation(s)

[!] WARNING (line 13)
Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
class CodeScanner(Scanner):
    
    def scan(
        self, 
        knowledge_graph: Dict[str, Any], 
    # ... (truncated)
```

[!] WARNING (line 177)
Function "scan_cross_file" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return False
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
    # ... (truncated)
```

[!] WARNING (line 237)
Function "_extract_code_snippet" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return parsed_files
    
    def _extract_code_snippet(self, content: str, ast_node: Optional[ast.AST] = None, 
                             start_line: Optional[int] = None, end_line: Optional[int] = None,
                             context_before: int = 2, max_lines: int = 50) -> str:
    # ... (truncated)
```

[!] WARNING (line 277)
Function "_create_violation_with_snippet" has 12 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return code_snippet
    
    def _create_violation_with_snippet(
        self, 
        rule_obj: Any,
    # ... (truncated)
```

---

## use_domain_language
**code_scanner.py** - 27 violation(s)

[i] INFO (line 13)
Function "scan" uses parameter name "knowledge_graph" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 28)
Function "scan_file" uses parameter name "knowledge_graph" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 44)
Function "_extract_domain_terms" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 44)
Function "_extract_domain_terms" uses parameter name "knowledge_graph" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 151)
Function "_extract_words_from_text" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 151)
Function "_extract_words_from_text" uses parameter name "text" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 160)
Function "_matches_domain_term" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 160)
Function "_matches_domain_term" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 160)
Function "_matches_domain_term" uses parameter name "domain_terms" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 177)
Function "scan_cross_file" uses parameter name "status_writer" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 237)
Function "_extract_code_snippet" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 237)
Function "_extract_code_snippet" uses parameter name "content" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 237)
Function "_extract_code_snippet" uses parameter name "ast_node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 237)
Function "_extract_code_snippet" uses parameter name "start_line" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 237)
Function "_extract_code_snippet" uses parameter name "end_line" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 237)
Function "_extract_code_snippet" uses parameter name "context_before" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 237)
Function "_extract_code_snippet" uses parameter name "max_lines" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 277)
Function "_create_violation_with_snippet" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 277)
Function "_create_violation_with_snippet" uses parameter name "violation_message" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 277)
Function "_create_violation_with_snippet" uses parameter name "line_number" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 277)
Function "_create_violation_with_snippet" uses parameter name "severity" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 277)
Function "_create_violation_with_snippet" uses parameter name "content" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 277)
Function "_create_violation_with_snippet" uses parameter name "ast_node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 277)
Function "_create_violation_with_snippet" uses parameter name "start_line" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 277)
Function "_create_violation_with_snippet" uses parameter name "end_line" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 277)
Function "_create_violation_with_snippet" uses parameter name "context_before" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

[i] INFO (line 277)
Function "_create_violation_with_snippet" uses parameter name "max_lines" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

---

## use_natural_english
**code_scanner.py** - 12 violation(s)

[i] INFO (line 245)
Variable "start_line_0" uses technical notation. Use natural English instead.

```python
        if ast_node is not None:
            # Use AST node to determine lines
            start_line_0 = ast_node.lineno - 1 if hasattr(ast_node, 'lineno') and ast_node.lineno else 0
            
```

[i] INFO (line 248)
Variable "end_line_0" uses technical notation. Use natural English instead.

```python
            
            if hasattr(ast_node, 'end_lineno') and ast_node.end_lineno:
                end_line_0 = ast_node.end_lineno  # end_lineno is 1-indexed, exclusive
            else:
```

[i] INFO (line 251)
Variable "end_line_0" uses technical notation. Use natural English instead.

```python
            else:
                # Estimate end by finding the maximum line number in the subtree
                end_line_0 = start_line_0 + 1
                for node in ast.walk(ast_node):
```

[i] INFO (line 257)
Variable "start_line_0" uses technical notation. Use natural English instead.

```python
        elif start_line is not None:
            # Use provided line numbers (1-indexed, convert to 0-indexed)
            start_line_0 = start_line - 1
            if end_line is not None:
```

[i] INFO (line 266)
Variable "start_line_0" uses technical notation. Use natural English instead.

```python
            return ""
        
        snippet_start = max(0, start_line_0 - context_before)
        snippet_end = min(len(lines), end_line_0 + 1)
```

[i] INFO (line 267)
Variable "end_line_0" uses technical notation. Use natural English instead.

```python
        
        snippet_start = max(0, start_line_0 - context_before)
        snippet_end = min(len(lines), end_line_0 + 1)
        code_snippet = '\n'.join(lines[snippet_start:snippet_end])
```

[i] INFO (line 251)
Variable "start_line_0" uses technical notation. Use natural English instead.

```python
            else:
                # Estimate end by finding the maximum line number in the subtree
                end_line_0 = start_line_0 + 1
                for node in ast.walk(ast_node):
```

[i] INFO (line 259)
Variable "end_line_0" uses technical notation. Use natural English instead.

```python
            start_line_0 = start_line - 1
            if end_line is not None:
                end_line_0 = end_line  # end_line is 1-indexed, exclusive (like end_lineno)
            else:
```

[i] INFO (line 261)
Variable "end_line_0" uses technical notation. Use natural English instead.

```python
                end_line_0 = end_line  # end_line is 1-indexed, exclusive (like end_lineno)
            else:
                end_line_0 = start_line_0 + 1
        else:
```

[i] INFO (line 254)
Variable "end_line_0" uses technical notation. Use natural English instead.

```python
                for node in ast.walk(ast_node):
                    if hasattr(node, 'lineno') and node.lineno:
                        end_line_0 = max(end_line_0, node.lineno)
        elif start_line is not None:
```

[i] INFO (line 261)
Variable "start_line_0" uses technical notation. Use natural English instead.

```python
                end_line_0 = end_line  # end_line is 1-indexed, exclusive (like end_lineno)
            else:
                end_line_0 = start_line_0 + 1
        else:
```

[i] INFO (line 254)
Variable "end_line_0" uses technical notation. Use natural English instead.

```python
                for node in ast.walk(ast_node):
                    if hasattr(node, 'lineno') and node.lineno:
                        end_line_0 = max(end_line_0, node.lineno)
        elif start_line is not None:
```

---

