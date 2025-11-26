"""
Clean code validation and refactoring for Python and JavaScript, using framework-specific rules (clean-code-python-rule.mdc and clean-code-js-rule.mdc) that extend base clean code principles (clean-code-rule.mdc). Provides validate command to check code quality and optionally apply automated fixes.

This runner implements commands for the clean-code feature.
"""

from pathlib import Path
from typing import Dict, Any, List, Optional
import json
import re
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from common_command_runner.common_command_runner import (
    Content, BaseRule, Command, CodeAugmentedCommand, RuleParser
)

# TABLE OF CONTENTS
# 1. CLEAN CODE COMMAND
#   1.1 Language Detection
#   1.2 Code Structure Extraction
#   1.3 Heuristics (Static Analysis)
#   1.4 Generate Violations Report
#   1.5 Validate Violations Report
#   1.6 Correct Violations Report


class CleanCodeCommand(CodeAugmentedCommand):
    """
    Clean Code Command: Analyze code quality using heuristics and AI-powered semantic analysis
    
    Purpose: Validate code against clean code principles and generate actionable violations report
    """
    
    def __init__(self, file_path: str, action: str = "generate"):
        """
        Initialize Clean Code Command
        
        Args:
            file_path: Path to code file to analyze
            action: Action to perform (generate, validate, correct)
        """
        self.file_path = Path(file_path)
        self.action = action
        self.language = self._detect_language()
        
        # Load base rule and specialized rule
        base_rule = BaseRule('clean-code-rule.mdc')
        specialized_rule = self._load_specialized_rule()
        
        # Create content object
        content = Content(str(self.file_path), self.file_path.suffix)
        
        # Create base command
        base_command = Command(content, base_rule)
        
        # Initialize CodeAugmentedCommand
        super().__init__(base_command, base_rule)
        
        # Store specialized rule for reference
        self.specialized_rule = specialized_rule
        
        # Code structure cache
        self._code_structure: Optional[Dict[str, Any]] = None
        
        # Violations report path
        self._violations_report_path = self.file_path.parent / f"{self.file_path.stem}-clean-code-violations.json"
        self._final_report_path = self.file_path.parent / f"{self.file_path.stem}-clean-code-violations-final.json"
    
    # 1.1 Language Detection
    
    def _detect_language(self) -> str:
        """
        Detect language from file extension
        
        Returns:
            Language name: 'python' or 'javascript'
        """
        ext = self.file_path.suffix.lower()
        python_exts = {'.py', '.pyi'}
        js_exts = {'.js', '.mjs', '.ts', '.tsx', '.jsx'}
        
        if ext in python_exts:
            return 'python'
        elif ext in js_exts:
            return 'javascript'
        else:
            # Default to python for unknown extensions
            return 'python'
    
    # 1.2 Code Structure Extraction
    
    def _extract_code_structure(self) -> Dict[str, Any]:
        """
        Extract code structure: functions, classes, line counts, etc.
        
        Returns:
            Dictionary with code structure information
        """
        if self._code_structure is not None:
            return self._code_structure
        
        if not self.content._ensure_content_loaded():
            return {"functions": [], "classes": [], "total_lines": 0}
        
        lines = self.content._content_lines
        total_lines = len(lines)
        
        if self.language == 'python':
            functions, classes = self._extract_python_structure(lines)
        else:
            functions, classes = self._extract_javascript_structure(lines)
        
        self._code_structure = {
            "functions": functions,
            "classes": classes,
            "total_lines": total_lines
        }
        
        return self._code_structure
    
    def _extract_python_structure(self, lines: List[str]) -> tuple:
        """Extract Python function and class structure"""
        functions = []
        classes = []
        
        for i, line in enumerate(lines, 1):
            # Match function definitions
            func_match = re.match(r'^\s*(?:async\s+)?def\s+(\w+)\s*\(', line)
            if func_match:
                func_name = func_match.group(1)
                # Count parameters
                params_match = re.search(r'\(([^)]*)\)', line)
                param_count = len([p for p in params_match.group(1).split(',') if p.strip()]) if params_match else 0
                # Find function end (next def/class at same or lower indentation, or end of file)
                func_end = self._find_python_block_end(lines, i, line)
                func_length = func_end - i + 1
                functions.append({
                    "name": func_name,
                    "line": i,
                    "length": func_length,
                    "parameters": param_count
                })
            
            # Match class definitions
            class_match = re.match(r'^\s*class\s+(\w+)', line)
            if class_match:
                class_name = class_match.group(1)
                # Find class end
                class_end = self._find_python_block_end(lines, i, line)
                class_length = class_end - i + 1
                # Count methods (functions inside class)
                methods = [f for f in functions if f["line"] > i and f["line"] <= class_end]
                classes.append({
                    "name": class_name,
                    "line": i,
                    "length": class_length,
                    "methods": len(methods)
                })
        
        return functions, classes
    
    def _extract_javascript_structure(self, lines: List[str]) -> tuple:
        """Extract JavaScript/TypeScript function and class structure"""
        functions = []
        classes = []
        
        for i, line in enumerate(lines, 1):
            # Match function definitions (function, arrow functions, methods)
            func_patterns = [
                r'^\s*(?:export\s+)?(?:async\s+)?function\s+(\w+)',
                r'^\s*const\s+(\w+)\s*=\s*(?:async\s+)?\([^)]*\)\s*=>',
                r'^\s*(\w+)\s*:\s*(?:async\s+)?\([^)]*\)\s*=>',
                r'^\s*(\w+)\s*:\s*(?:async\s+)?function',
            ]
            
            for pattern in func_patterns:
                func_match = re.match(pattern, line)
                if func_match:
                    func_name = func_match.group(1)
                    # Count parameters
                    params_match = re.search(r'\(([^)]*)\)', line)
                    param_count = len([p for p in params_match.group(1).split(',') if p.strip()]) if params_match else 0
                    # Find function end (simplified - look for closing brace)
                    func_end = self._find_javascript_block_end(lines, i)
                    func_length = func_end - i + 1
                    functions.append({
                        "name": func_name,
                        "line": i,
                        "length": func_length,
                        "parameters": param_count
                    })
                    break
            
            # Match class definitions
            class_match = re.match(r'^\s*(?:export\s+)?class\s+(\w+)', line)
            if class_match:
                class_name = class_match.group(1)
                # Find class end
                class_end = self._find_javascript_block_end(lines, i)
                class_length = class_end - i + 1
                # Count methods
                methods = [f for f in functions if f["line"] > i and f["line"] <= class_end]
                classes.append({
                    "name": class_name,
                    "line": i,
                    "length": class_length,
                    "methods": len(methods)
                })
        
        return functions, classes
    
    def _find_python_block_end(self, lines: List[str], start_line: int, definition_line: str) -> int:
        """Find end of Python block (function/class)"""
        start_indent = len(definition_line) - len(definition_line.lstrip())
        for i in range(start_line, len(lines)):
            line = lines[i]
            if not line.strip():  # Skip empty lines
                continue
            current_indent = len(line) - len(line.lstrip())
            if current_indent <= start_indent and (line.strip().startswith('def ') or line.strip().startswith('class ')):
                return i - 1
        return len(lines) - 1
    
    def _find_javascript_block_end(self, lines: List[str], start_line: int) -> int:
        """Find end of JavaScript block (function/class)"""
        brace_count = 0
        in_block = False
        for i in range(start_line - 1, len(lines)):
            line = lines[i]
            brace_count += line.count('{') - line.count('}')
            if brace_count > 0:
                in_block = True
            if in_block and brace_count == 0:
                return i
        return len(lines) - 1
    
    # 1.3 Heuristics (Static Analysis)
    
    def _run_heuristics(self) -> List[Dict[str, Any]]:
        """
        Run static analysis heuristics to find obvious violations
        
        Returns:
            List of violation dictionaries
        """
        violations = []
        
        if not self.content._ensure_content_loaded():
            return violations
        
        lines = self.content._content_lines
        code_structure = self._extract_code_structure()
        
        # Check for deep nesting
        violations.extend(self._check_deep_nesting(lines))
        
        # Check for magic numbers
        violations.extend(self._check_magic_numbers(lines))
        
        # Check for single-letter variables
        violations.extend(self._check_single_letter_variables(lines))
        
        # Check for commented code
        violations.extend(self._check_commented_code(lines))
        
        # Check for large functions
        violations.extend(self._check_large_functions(code_structure["functions"]))
        
        # Check for too many parameters
        violations.extend(self._check_too_many_parameters(code_structure["functions"]))
        
        # Check for large classes
        violations.extend(self._check_large_classes(code_structure["classes"]))
        
        return violations
    
    def _check_deep_nesting(self, lines: List[str]) -> List[Dict[str, Any]]:
        """Check for deep nesting (>=3 levels)"""
        violations = []
        for i, line in enumerate(lines, 1):
            indent = len(line) - len(line.lstrip())
            nesting_level = indent // 4  # Assuming 4 spaces per level
            if nesting_level >= 7:
                violations.append({
                    "line": i,
                    "severity": "critical",
                    "principle": "1.3 Control Flow",
                    "issue": f"Deep nesting detected: {nesting_level} levels",
                    "suggestion": "Extract nested logic into separate functions"
                })
            elif nesting_level >= 4:
                violations.append({
                    "line": i,
                    "severity": "important",
                    "principle": "1.3 Control Flow",
                    "issue": f"Deep nesting detected: {nesting_level} levels",
                    "suggestion": "Consider extracting nested logic into separate functions"
                })
            elif nesting_level == 3:
                violations.append({
                    "line": i,
                    "severity": "suggested",
                    "principle": "1.3 Control Flow",
                    "issue": f"Nesting level: {nesting_level}",
                    "suggestion": "Consider simplifying control flow"
                })
        return violations
    
    def _check_magic_numbers(self, lines: List[str]) -> List[Dict[str, Any]]:
        """Check for magic numbers (2+ digits, not version numbers or dates)"""
        violations = []
        for i, line in enumerate(lines, 1):
            # Find numeric literals (2+ digits)
            numbers = re.findall(r'\b\d{2,}\b', line)
            for num in numbers:
                # Skip common patterns (years, version numbers)
                if not (1900 <= int(num) <= 2100 or num in ['100', '200', '300', '500', '1000']):
                    violations.append({
                        "line": i,
                        "severity": "suggested",
                        "principle": "2.1 Meaningful Names",
                        "issue": f"Magic number found: {num}",
                        "suggestion": "Extract to named constant with descriptive name"
                    })
        return violations
    
    def _check_single_letter_variables(self, lines: List[str]) -> List[Dict[str, Any]]:
        """Check for single-letter variables (non-loop)"""
        violations = []
        for i, line in enumerate(lines, 1):
            # Match single-letter variable assignments (not in for loops)
            if 'for ' not in line and 'for(' not in line:
                matches = re.findall(r'\b([a-z])\s*=', line)
                for var in matches:
                    violations.append({
                        "line": i,
                        "severity": "suggested",
                        "principle": "2.1 Meaningful Names",
                        "issue": f"Single-letter variable: {var}",
                        "suggestion": "Use descriptive name that reveals intent"
                    })
        return violations
    
    def _check_commented_code(self, lines: List[str]) -> List[Dict[str, Any]]:
        """Check for commented-out code blocks"""
        violations = []
        in_comment_block = False
        comment_start = 0
        
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            # Check for code-like patterns in comments
            if stripped.startswith('#') or (stripped.startswith('//') and self.language == 'javascript'):
                comment_line = stripped.lstrip('#/').strip()
                # Look for code patterns (assignments, function calls, etc.)
                if re.search(r'\w+\s*[=\(]', comment_line):
                    if not in_comment_block:
                        in_comment_block = True
                        comment_start = i
                else:
                    if in_comment_block:
                        violations.append({
                            "line": comment_start,
                            "severity": "suggested",
                            "principle": "3.1 Comments",
                            "issue": "Commented-out code detected",
                            "suggestion": "Remove commented code (it's in git history)"
                        })
                        in_comment_block = False
            else:
                if in_comment_block:
                    in_comment_block = False
        
        return violations
    
    def _check_large_functions(self, functions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Check for large functions"""
        violations = []
        for func in functions:
            if func["length"] > 50:
                violations.append({
                    "line": func["line"],
                    "function": func["name"],
                    "severity": "critical",
                    "principle": "1.2 Small and Focused",
                    "issue": f"Function too large: {func['length']} lines",
                    "suggestion": "Break into smaller functions"
                })
            elif func["length"] > 20:
                violations.append({
                    "line": func["line"],
                    "function": func["name"],
                    "severity": "important",
                    "principle": "1.2 Small and Focused",
                    "issue": f"Function large: {func['length']} lines",
                    "suggestion": "Consider breaking into smaller functions"
                })
        return violations
    
    def _check_too_many_parameters(self, functions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Check for too many parameters"""
        violations = []
        for func in functions:
            if func["parameters"] > 3:
                violations.append({
                    "line": func["line"],
                    "function": func["name"],
                    "severity": "important",
                    "principle": "1.2 Small and Focused",
                    "issue": f"Too many parameters: {func['parameters']}",
                    "suggestion": "Use parameter object or split function"
                })
        return violations
    
    def _check_large_classes(self, classes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Check for large classes"""
        violations = []
        for cls in classes:
            if cls["length"] > 300:
                violations.append({
                    "line": cls["line"],
                    "function": cls["name"],
                    "severity": "critical",
                    "principle": "2.2 Classes",
                    "issue": f"Class too large: {cls['length']} lines",
                    "suggestion": "Split into smaller classes"
                })
            elif cls["length"] > 200:
                violations.append({
                    "line": cls["line"],
                    "function": cls["name"],
                    "severity": "important",
                    "principle": "2.2 Classes",
                    "issue": f"Class large: {cls['length']} lines",
                    "suggestion": "Consider splitting into smaller classes"
                })
        return violations
    
    # 1.4 Generate Violations Report
    
    def generate(self) -> str:
        """
        Generate violations report using heuristics and AI analysis
        
        Returns:
            Instructions for AI to perform deep semantic analysis
        """
        # Extract code structure
        code_structure = self._extract_code_structure()
        
        # Run heuristics
        heuristic_violations = self._run_heuristics()
        
        # Save violations report
        self.save_violations_report(heuristic_violations)
        
        # Build instructions for AI
        instructions = f"""Analyze the following code for clean code violations:

**File:** {self.file_path}
**Language:** {self.language}

**Code Structure:**
- Functions: {len(code_structure['functions'])}
- Classes: {len(code_structure['classes'])}
- Total Lines: {code_structure['total_lines']}

**Heuristics Found (with code examples):**
{self._format_heuristic_violations(heuristic_violations)}

**Instructions:**
1. Review the code structure and heuristic violations above. Each violation includes:
   - Line number with code snippet showing the problematic area
   - Severity level (critical/important/suggested)
   - Specific issue description
   - Actionable suggestion

2. Perform deep semantic analysis for:
   - Single Responsibility violations (functions/classes doing multiple things)
   - Side effects mixed with pure logic (calculations with hidden mutations)
   - Poor encapsulation (exposed internal state, missing abstraction)
   - Code duplication patterns (repeated logic that should be extracted)
   - Unclear naming (names that don't reveal intent)
   - Abstraction level mixing (high-level orchestration mixed with low-level details)

3. For EACH violation found, provide:
   - **Location**: Exact line number(s) and function/class name
   - **Severity**: critical (must fix), important (should fix), suggested (consider fixing)
   - **Principle**: Which clean code principle is violated (e.g., "1.2 Small and Focused", "1.3 Control Flow")
   - **Issue**: Specific description of what's wrong with code snippet showing the problem
   - **Recommendation**: Concrete example showing how to fix it, including:
     * Before/after code snippets with line numbers
     * Step-by-step refactoring approach
     * Why this change improves code quality

4. **Example Violation Format:**
   ```
   **Line 482-490** (critical) - Deep Nesting (7 levels)
   **Function:** `_deploy_to_global()`
   **Principle:** 1.3 Control Flow - Simple Control Flow
   
   **Current Code:**
   ```python
   480|    if condition1:
   481|        if condition2:
   482|            if condition3:
   483|                if condition4:
   484|                    if condition5:
   485|                        if condition6:
   486|                            if condition7:
   487|                                result = process()
   ```
   
   **Issue:** Deep nesting makes code hard to read and maintain. Each nested level increases cognitive load.
   
   **Recommendation:** Extract nested logic into separate functions with guard clauses:
   ```python
   def _should_process_deployment(self, condition1, condition2):
       if not condition1:
           return False
       if not condition2:
           return False
       return True
   
   def _deploy_to_global(self):
       if not self._should_process_deployment(condition1, condition2):
           return
       result = self._process_deployment()
   ```
   
   **Why:** Guard clauses flatten the structure, making the code easier to understand and test.
   ```

**Rules to Apply:**
{self._get_rules_summary()}

**Important:** Include actual code snippets from the file showing line numbers. Make recommendations concrete and actionable with before/after examples.
"""
        
        return instructions
    
    def _format_heuristic_violations(self, violations: List[Dict[str, Any]]) -> str:
        """Format heuristic violations for AI instructions with code snippets"""
        if not violations:
            return "No heuristic violations found."
        
        result = []
        # Group violations by type for better examples
        critical_violations = [v for v in violations if v.get('severity') == 'critical'][:5]
        important_violations = [v for v in violations if v.get('severity') == 'important'][:3]
        suggested_violations = [v for v in violations if v.get('severity') == 'suggested'][:2]
        
        example_violations = critical_violations + important_violations + suggested_violations
        
        for v in example_violations[:10]:  # Limit to first 10 for instructions
            line_num = v['line']
            code_snippet = self._get_code_snippet(line_num, context_lines=3)
            result.append(f"- **Line {line_num}** ({v['severity']}): {v['issue']}")
            result.append(f"  ```{self.language}")
            result.append(code_snippet)
            result.append(f"  ```")
            result.append(f"  **Suggestion:** {v.get('suggestion', 'Review and refactor')}")
            result.append("")
        
        return "\n".join(result)
    
    def _get_code_snippet(self, line_num: int, context_lines: int = 3) -> str:
        """Get code snippet around a specific line number"""
        if not self.content._ensure_content_loaded():
            return f"# Line {line_num} (code not available)"
        
        lines = self.content._content_lines
        start_line = max(0, line_num - context_lines - 1)
        end_line = min(len(lines), line_num + context_lines)
        
        snippet_lines = []
        for i in range(start_line, end_line):
            line_num_display = i + 1
            marker = ">>> " if line_num_display == line_num else "    "
            snippet_lines.append(f"{marker}{line_num_display:4d} | {lines[i]}")
        
        return "\n".join(snippet_lines)
    
    def _get_rules_summary(self) -> str:
        """Get summary of rules to apply"""
        if self.specialized_rule:
            return f"Apply {self.language}-specific clean code rules from {self.specialized_rule.rule_file_name}"
        return "Apply base clean code rules"
    
    def _load_specialized_rule(self) -> Optional[BaseRule]:
        """Load specialized rule based on language"""
        if self.language == 'python':
            rule_file = 'clean-code-python-rule.mdc'
        else:
            rule_file = 'clean-code-js-rule.mdc'
        
        try:
            return BaseRule(rule_file)
        except:
            return None
    
    def save_violations_report(self, violations: List[Dict[str, Any]], ai_analysis: str = ""):
        """
        Save violations report to JSON file
        
        Args:
            violations: List of violation dictionaries
            ai_analysis: Additional AI analysis text
        """
        code_structure = self._extract_code_structure()
        
        # Count violations by severity
        severity_counts = {"critical": 0, "important": 0, "suggested": 0}
        for v in violations:
            severity = v.get("severity", "suggested")
            severity_counts[severity] = severity_counts.get(severity, 0) + 1
        
        report = {
            "file": str(self.file_path),
            "language": self.language,
            "violations": violations,
            "summary": {
                "critical": severity_counts["critical"],
                "important": severity_counts["important"],
                "suggested": severity_counts["suggested"],
                "total": len(violations)
            },
            "code_structure": code_structure,
            "ai_analysis": ai_analysis
        }
        
        with open(self._violations_report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
    
    # 1.5 Validate Violations Report
    
    def validate(self) -> str:
        """
        Validate generated violations report for accuracy
        
        Returns:
            Instructions for AI to validate the report
        """
        if not self._violations_report_path.exists():
            return "No violations report found. Run generate first."
        
        with open(self._violations_report_path, 'r', encoding='utf-8') as f:
            report = json.load(f)
        
        # Get sample violations with code snippets for validation
        sample_violations = report.get('violations', [])[:5]
        sample_with_code = []
        for v in sample_violations:
            line_num = v.get('line', 0)
            # Try to get code snippet, but don't fail if content not loaded
            try:
                code_snippet = self._get_code_snippet(line_num, context_lines=5)
            except:
                code_snippet = f"# Line {line_num} (code snippet unavailable)"
            sample_with_code.append({
                **v,
                'code_snippet': code_snippet
            })
        
        instructions = f"""Validate the following clean code violations report:

**File:** {self.file_path}
**Total Violations:** {report.get('summary', {}).get('total', 0)}
**Critical:** {report.get('summary', {}).get('critical', 0)}
**Important:** {report.get('summary', {}).get('important', 0)}
**Suggested:** {report.get('summary', {}).get('suggested', 0)}

**Sample Violations (with code context):**
{json.dumps(sample_with_code, indent=2)}

**Instructions:**
1. Review each violation with its code context:
   - **Is it correctly identified?** Does the code snippet actually show the violation?
   - **Does it truly violate the stated principle?** Check against clean code rules
   - **Is severity appropriate?** Critical = must fix, Important = should fix, Suggested = consider fixing
   - **Is suggestion actionable?** Can the recommendation be implemented?

2. For violations that need correction, provide:
   - **Line numbers** where the violation occurs
   - **Code snippet** showing the problematic area (with line numbers)
   - **Corrected principle** if attribution is wrong
   - **Adjusted severity** if needed
   - **Improved suggestion** with before/after code examples if the original is unclear

3. Identify and flag:
   - **False positives** - Violations that don't actually exist
   - **Incorrect principle attribution** - Wrong principle cited
   - **Missing context** - Violations that need more code context to understand
   - **Severity mismatches** - Critical violations that should be important/suggested or vice versa
   - **Incomplete recommendations** - Suggestions that lack concrete examples

4. **Validation Format:**
   For each violation that needs correction, provide:
   ```
   **Violation at Line {line}** - {severity}
   **Issue:** {original issue description}
   **Validation:** {correct/incorrect/needs adjustment}
   **Correction:** {if needed, provide corrected version with code examples}
   ```

5. Generate validation feedback summary with:
   - Total violations reviewed
   - Number of false positives found
   - Number of violations needing severity adjustment
   - Number of violations needing better recommendations
   - Overall report quality assessment
"""
        
        return instructions
    
    # 1.6 Correct Violations Report
    
    def correct(self) -> str:
        """
        Apply corrections to violations report
        
        Returns:
            Instructions for AI to apply corrections
        """
        if not self._violations_report_path.exists():
            return "No violations report found. Run generate first."
        
        with open(self._violations_report_path, 'r', encoding='utf-8') as f:
            report = json.load(f)
        
        instructions = f"""Apply corrections to the following violations report:

**File:** {self.file_path}

**Original Report:**
{json.dumps(report, indent=2)}

**Instructions:**
1. Load validated violations and correction suggestions
2. Apply corrections:
   - Remove invalid violations (false positives)
   - Adjust severities as indicated
   - Improve suggestions where needed
   - Ensure correct principle attribution
3. Output final cleaned violations report as JSON
"""
        
        return instructions
    
    def save_corrected_report(self, corrected_violations: List[Dict[str, Any]]):
        """
        Save corrected violations report
        
        Args:
            corrected_violations: List of corrected violation dictionaries
        """
        code_structure = self._extract_code_structure()
        
        severity_counts = {"critical": 0, "important": 0, "suggested": 0}
        for v in corrected_violations:
            severity = v.get("severity", "suggested")
            severity_counts[severity] = severity_counts.get(severity, 0) + 1
        
        report = {
            "file": str(self.file_path),
            "language": self.language,
            "violations": corrected_violations,
            "summary": {
                "critical": severity_counts["critical"],
                "important": severity_counts["important"],
                "suggested": severity_counts["suggested"],
                "total": len(corrected_violations)
            },
            "code_structure": code_structure
        }
        
        with open(self._final_report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python clean-code_runner.py <action> <file_path>")
        print("Actions: generate, validate, correct")
        sys.exit(1)
    
    action = sys.argv[1]
    file_path = sys.argv[2]
    
    command = CleanCodeCommand(file_path, action)
    
    if action == "generate":
        result = command.generate()
        print(result)
    elif action == "validate":
        result = command.validate()
        print(result)
    elif action == "correct":
        result = command.correct()
        print(result)
    else:
        print(f"Unknown action: {action}")
        sys.exit(1)
