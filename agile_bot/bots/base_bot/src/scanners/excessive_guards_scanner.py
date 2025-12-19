"""Scanner for detecting excessive guard clauses in code."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import re
import logging
from .code_scanner import CodeScanner
from .violation import Violation

logger = logging.getLogger(__name__)


class ExcessiveGuardsScanner(CodeScanner):
    """Detects guard clauses that check for None/existence, adding cyclomatic complexity.
    
    Guards that only check if variables exist or are None make code harder to read
    and hide problems. Error handling should be centralized rather than scattered
    throughout the code. Let code fail fast with clear errors rather than silently
    handling missing components.
    
    Detects:
    - hasattr() checks before attribute access
    - File existence checks before file operations
    - Variable truthiness checks (if not X:, if X:)
    - None checks (if X is None:, if X is not None:)
    - Guard clauses that silently return None/empty
    """
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        if not file_path.exists():
            return violations
        
        try:
            content = file_path.read_text(encoding='utf-8')
            lines = content.split('\n')
            tree = ast.parse(content, filename=str(file_path))
            
            # Check for excessive guards using AST
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # Skip test functions (covered by NoGuardClausesScanner)
                    if node.name.startswith('test_'):
                        continue
                    
                    # Skip private methods (they might need guards for internal validation)
                    if node.name.startswith('_') and node.name != '__init__':
                        continue
                    
                    func_violations = self._check_function_guards(node, file_path, rule_obj, lines)
                    violations.extend(func_violations)
        
        except (SyntaxError, UnicodeDecodeError) as e:
            logger.debug(f'Skipping file {file_path} due to {type(e).__name__}: {e}')
        
        return violations
    
    def _check_function_guards(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any, source_lines: List[str]) -> List[Dict[str, Any]]:
        """Check a function for guard clauses that check for None/existence."""
        violations = []
        
        # Find all guard clause patterns in function
        for node in ast.walk(func_node):
            if isinstance(node, ast.If):
                if self._is_guard_clause(node, source_lines):
                    violation = self._check_guard_pattern(node, file_path, rule_obj, source_lines)
                    if violation:
                        violations.append(violation)
        
        return violations
    
    def _is_guard_clause(self, if_node: ast.If, source_lines: List[str]) -> bool:
        """Check if an if statement is a guard clause pattern."""
        # Guard clauses typically:
        # 1. Return early or set default values
        # 2. Check for None/existence/type
        # 3. Have simple bodies (return, continue, break, or single assignment)
        
        # Check if body is simple (return, continue, break, or single statement)
        body_is_simple = len(if_node.body) == 1
        if body_is_simple:
            first_stmt = if_node.body[0]
            is_early_exit = isinstance(first_stmt, (ast.Return, ast.Continue, ast.Break))
            is_simple_assign = isinstance(first_stmt, ast.Assign) and len(first_stmt.targets) == 1
            
            if is_early_exit or is_simple_assign:
                # Check if test is a guard pattern
                return self._is_guard_pattern(if_node.test)
        
        return False
    
    def _is_guard_pattern(self, test_node: ast.AST) -> bool:
        """Check if test expression matches guard clause patterns.
        
        Note: File existence checks are identified but not flagged (they're for optional files).
        """
        # hasattr() checks
        if isinstance(test_node, ast.Call):
            if isinstance(test_node.func, ast.Name):
                if test_node.func.id == 'hasattr':
                    return True
        
        # isinstance() checks (defensive, not polymorphic)
        if isinstance(test_node, ast.Call):
            if isinstance(test_node.func, ast.Name):
                if test_node.func.id == 'isinstance':
                    return True
        
        # File existence checks (identified but may not be flagged if optional)
        if isinstance(test_node, ast.Call):
            if isinstance(test_node.func, ast.Attribute):
                if test_node.func.attr == 'exists':
                    return True
        
        # Variable truthiness checks (if variable:, if not variable:)
        if isinstance(test_node, ast.Name):
            return True
        if isinstance(test_node, ast.UnaryOp) and isinstance(test_node.op, ast.Not):
            if isinstance(test_node.operand, ast.Name):
                return True
        
        # Comparison with None
        if isinstance(test_node, ast.Compare):
            for op in test_node.ops:
                if isinstance(op, (ast.Is, ast.IsNot, ast.Eq, ast.NotEq)):
                    for comparator in test_node.comparators:
                        if isinstance(comparator, ast.Constant) and comparator.value is None:
                            return True
                        if isinstance(comparator, ast.NameConstant) and comparator.value is None:
                            return True
        
        return False
    
    def _get_violation_message(self, rule_obj: Any, message_key: str, line_number: int, **format_args) -> str:
        """Get violation message from rule file or use default."""
        if rule_obj and hasattr(rule_obj, 'rule_content'):
            violation_messages = rule_obj.rule_content.get('violation_messages', {})
            if message_key in violation_messages:
                template = violation_messages[message_key]
                return template.format(line=line_number, **format_args)
        
        # Default messages if not in rule file
        defaults = {
            'hasattr_guard': f'Line {line_number}: hasattr() guard clause detected. Assume attributes exist - let AttributeError propagate if missing.',
            'file_existence_guard': f'Line {line_number}: File existence check detected. Let file operations fail if file missing - handle errors centrally.',
            'none_check_guard': f'Line {line_number}: None check guard clause detected. Assume variables are initialized - let code fail fast if None.',
            'truthiness_check_guard': f'Line {line_number}: Variable truthiness check detected (if {format_args.get("var", "variable")}:). Assume variable exists - let code fail fast if missing.',
            'truthiness_check_guard_not': f'Line {line_number}: Variable truthiness check detected (if not {format_args.get("var", "variable")}:). Assume variable exists - let code fail fast if missing.'
        }
        return defaults.get(message_key, f'Line {line_number}: Guard clause detected.')

    def _is_optional_config_check(self, guard_node: ast.If, source_lines: List[str]) -> bool:
        """Check if guard is checking for optional configuration (should not be flagged).
        
        These are legitimate cases where a guard is appropriate:
        - Checking if optional config value exists before using it
        - Checking if optional file/directory exists before processing
        - Early returns for empty collections (optimization)
        - Optional parameters with defaults
        - Optional return values from methods
        """
        # File existence checks - only flag if NOT followed by creation logic
        test = guard_node.test
        if isinstance(test, ast.Call) and isinstance(test.func, ast.Attribute) and test.func.attr == 'exists':
            # Check if followed by file creation logic (write_text, write_bytes, mkdir, etc.)
            if self._is_followed_by_creation_logic(guard_node, source_lines):
                return True  # Has creation logic, so it's legitimate - don't flag
            # No creation logic - flag it
            return False
        
        # hasattr() checks - these are for optional attributes, don't flag
        if isinstance(test, ast.Call) and isinstance(test.func, ast.Name) and test.func.id == 'hasattr':
            return True
        
        # Check if guard is an early return for empty collections (optimization)
        if guard_node.body:
            first_stmt = guard_node.body[0]
            if isinstance(first_stmt, ast.Return):
                # Check if returning empty list/dict/None (early return optimization)
                if first_stmt.value is None:
                    return True
                if isinstance(first_stmt.value, ast.Constant):
                    if first_stmt.value.value in ([], {}, None, ''):
                        return True
                if isinstance(first_stmt.value, (ast.List, ast.Dict)):
                    return True
        
        # Check if guard is checking for optional config/parameters/return values
        # Look for patterns like: if not config_value:, if not template_filename:, etc.
        if isinstance(test, ast.UnaryOp) and isinstance(test.op, ast.Not):
            if isinstance(test.operand, ast.Name):
                var_name = test.operand.id.lower()
                if self._check_optional_pattern(var_name):
                    return True  # Likely optional - don't flag
        
        # Check for truthiness checks on variables (if variable:, if not variable:)
        # These are often checking optional values
        if isinstance(test, ast.Name):
            var_name = test.id.lower()
            if self._check_optional_pattern(var_name):
                return True
        
        # Check for None comparisons on optional return values
        if isinstance(test, ast.Compare):
            for op in test.ops:
                if isinstance(op, (ast.Is, ast.IsNot, ast.Eq, ast.NotEq)):
                    for comparator in test.comparators:
                        if isinstance(comparator, ast.Constant) and comparator.value is None:
                            # Check if comparing a variable that might be optional
                            if isinstance(test.left, ast.Name):
                                var_name = test.left.id.lower()
                                if self._check_optional_pattern(var_name):
                                    return True
                        if isinstance(comparator, ast.NameConstant) and comparator.value is None:
                            if isinstance(test.left, ast.Name):
                                var_name = test.left.id.lower()
                                if self._check_optional_pattern(var_name):
                                    return True
        
        return False
    
    def _check_optional_pattern(self, var_name: str) -> bool:
        """Check if variable name matches optional pattern (config, template, etc.)."""
        optional_patterns = ['config', 'template', 'option', 'setting', 'file', 'dir', 'path',
                            'pattern', 'spec', 'rule', 'violation', 'action', 'behavior',
                            'trigger', 'command', 'desc', 'instruction', 'error', 'info',
                            'name', 'obj', 'instance', 'module', 'class', 'background']
        return any(pattern in var_name for pattern in optional_patterns)
    
    def _is_followed_by_creation_logic(self, guard_node: ast.If, source_lines: List[str]) -> bool:
        """Check if file existence check is followed by file/directory creation logic."""
        # Check the else branch if it exists
        if guard_node.orelse:
            for stmt in guard_node.orelse:
                if self._contains_creation_call(stmt):
                    return True
        
        # Check source lines after the if statement for creation patterns
        # Look at lines after the if statement (including else branch)
        start_line = guard_node.lineno - 1  # Convert to 0-based index
        end_line = guard_node.end_lineno if hasattr(guard_node, 'end_lineno') else start_line + len(guard_node.body) + 1
        
        # Check the else branch lines
        if guard_node.orelse:
            for stmt in guard_node.orelse:
                if hasattr(stmt, 'lineno'):
                    stmt_start = stmt.lineno - 1
                    stmt_end = stmt.end_lineno if hasattr(stmt, 'end_lineno') else stmt_start + 1
                    for i in range(stmt_start, min(stmt_end + 1, len(source_lines))):
                        line = source_lines[i].strip()
                        creation_patterns = ['.write_text', '.write_bytes', '.mkdir', '.touch', 'open(']
                        if any(pattern in line for pattern in creation_patterns):
                            return True
        
        # Check a few lines after the if statement ends
        for i in range(end_line, min(end_line + 5, len(source_lines))):
            line = source_lines[i].strip()
            # Skip empty lines and comments
            if not line or line.startswith('#'):
                continue
            # Check for file creation patterns
            creation_patterns = ['.write_text', '.write_bytes', '.mkdir', '.touch', 'open(']
            if any(pattern in line for pattern in creation_patterns):
                return True
        
        return False
    
    def _contains_creation_call(self, node: ast.AST) -> bool:
        """Check if AST node contains file/directory creation calls."""
        creation_methods = ['write_text', 'write_bytes', 'mkdir', 'touch']
        for child in ast.walk(node):
            if isinstance(child, ast.Call):
                if isinstance(child.func, ast.Attribute):
                    if child.func.attr in creation_methods:
                        return True
        return False

    def _check_guard_pattern(self, guard_node: ast.If, file_path: Path, rule_obj: Any, source_lines: List[str]) -> Optional[Dict[str, Any]]:
        """Check specific guard clause patterns and return violation if found.
        
        Only flags guards that check for misconfiguration, not legitimate business logic.
        File existence checks and optional config checks are not flagged.
        """
        test = guard_node.test
        
        # Skip file existence checks, optional config, hasattr(), early returns, etc.
        if self._is_optional_config_check(guard_node, source_lines):
            return None
        
        # None checks (if X is None:, if X is not None:)
        # Only flag if it's checking a required variable, not optional config
        if isinstance(test, ast.Compare):
            for op in test.ops:
                if isinstance(op, (ast.Is, ast.IsNot)):
                    for comparator in test.comparators:
                        if isinstance(comparator, ast.Constant) and comparator.value is None:
                            return Violation(
                                rule=rule_obj,
                                violation_message=self._get_violation_message(rule_obj, 'none_check_guard', guard_node.lineno),
                                location=str(file_path),
                                line_number=guard_node.lineno,
                                severity='warning'
                            ).to_dict()
                        if isinstance(comparator, ast.NameConstant) and comparator.value is None:
                            return Violation(
                                rule=rule_obj,
                                violation_message=self._get_violation_message(rule_obj, 'none_check_guard', guard_node.lineno),
                                location=str(file_path),
                                line_number=guard_node.lineno,
                                severity='warning'
                            ).to_dict()
        
        # Variable truthiness checks (if not X:, if X:)
        # Only flag if it's checking a required variable, not optional config
        if isinstance(test, ast.Name):
            var_name = self._get_variable_name(test)
            return Violation(
                rule=rule_obj,
                violation_message=self._get_violation_message(rule_obj, 'truthiness_check_guard', guard_node.lineno, var=var_name),
                location=str(file_path),
                line_number=guard_node.lineno,
                severity='warning'
            ).to_dict()
        
        if isinstance(test, ast.UnaryOp) and isinstance(test.op, ast.Not):
            if isinstance(test.operand, ast.Name):
                var_name = self._get_variable_name(test.operand)
                return Violation(
                    rule=rule_obj,
                    violation_message=self._get_violation_message(rule_obj, 'truthiness_check_guard_not', guard_node.lineno, var=var_name),
                    location=str(file_path),
                    line_number=guard_node.lineno,
                    severity='warning'
                ).to_dict()
        
        return None
    
    def _get_variable_name(self, node: ast.AST) -> str:
        """Extract variable name from AST node."""
        if isinstance(node, ast.Name):
            return node.id
        return 'variable'

