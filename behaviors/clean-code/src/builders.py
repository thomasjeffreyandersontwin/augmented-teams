"""
Clean Code Agent Builders

Builders for analyzing code and generating violations reports.
"""

from pathlib import Path
from typing import Dict, Any, List, Optional
import json
import re


class BaseBuilder:
    """Base builder class with common functionality"""
    
    def __init__(self, project_path: Path, structured_content_path: Optional[Path] = None):
        """
        Initialize builder with project path and optional structured content path.
        
        Args:
            project_path: Path to project root
            structured_content_path: Optional path to violations_report.json file
        """
        self.project_path = Path(project_path)
        self.structured_content_path = structured_content_path or self._find_structured_json()
    
    def _find_structured_json(self) -> Optional[Path]:
        """Find violations_report.json in docs/clean-code directory"""
        structured_path = self.project_path / "docs" / "clean-code" / "violations_report.json"
        if structured_path.exists():
            return structured_path
        return None
    
    def _load_violations_report(self) -> Dict[str, Any]:
        """Load violations report from structured.json"""
        if not self.structured_content_path or not self.structured_content_path.exists():
            raise FileNotFoundError(
                f"Violations report file not found: {self.structured_content_path}. "
                "Ensure build_structure phase has been completed."
            )
        
        with open(self.structured_content_path, 'r', encoding='utf-8') as f:
            return json.load(f)


class CodeStructureBuilder(BaseBuilder):
    """Builder for extracting code structure from source files"""
    
    def build(self, file_path: Path, language: str) -> Dict[str, Any]:
        """
        Build code structure from source file.
        
        Args:
            file_path: Path to source code file
            language: Language name ('python' or 'javascript')
        
        Returns:
            Dictionary with code structure information
        """
        if not file_path.exists():
            raise FileNotFoundError(f"Source file not found: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        total_lines = len(lines)
        
        if language == 'python':
            functions, classes = self._extract_python_structure(lines)
        else:
            functions, classes = self._extract_javascript_structure(lines)
        
        return {
            "functions": functions,
            "classes": classes,
            "total_lines": total_lines,
            "functions_detail": functions,
            "classes_detail": classes
        }
    
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
                # Calculate nesting depth
                nesting_depth = self._calculate_nesting_depth(lines, i, func_end)
                functions.append({
                    "name": func_name,
                    "line": i,
                    "length": func_length,
                    "parameters": param_count,
                    "nesting_depth": nesting_depth
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
                    # Calculate nesting depth
                    nesting_depth = self._calculate_nesting_depth_js(lines, i, func_end)
                    functions.append({
                        "name": func_name,
                        "line": i,
                        "length": func_length,
                        "parameters": param_count,
                        "nesting_depth": nesting_depth
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
    
    def _calculate_nesting_depth(self, lines: List[str], start_line: int, end_line: int) -> int:
        """Calculate maximum nesting depth in Python code block"""
        max_depth = 0
        start_indent = len(lines[start_line - 1]) - len(lines[start_line - 1].lstrip())
        
        for i in range(start_line, min(end_line + 1, len(lines))):
            line = lines[i]
            if not line.strip():
                continue
            current_indent = len(line) - len(line.lstrip())
            depth = (current_indent - start_indent) // 4  # Assuming 4 spaces per level
            max_depth = max(max_depth, depth)
        
        return max_depth
    
    def _calculate_nesting_depth_js(self, lines: List[str], start_line: int, end_line: int) -> int:
        """Calculate maximum nesting depth in JavaScript code block"""
        max_depth = 0
        current_depth = 0
        
        for i in range(start_line - 1, min(end_line, len(lines))):
            line = lines[i]
            # Count opening braces
            current_depth += line.count('{')
            max_depth = max(max_depth, current_depth)
            # Count closing braces
            current_depth -= line.count('}')
        
        return max_depth


class ViolationsReportBuilder(BaseBuilder):
    """Builder for creating violations report from code analysis"""
    
    def build(self, file_path: Path, language: str, code_structure: Dict[str, Any], 
              violations: List[Dict[str, Any]], heuristics: Dict[str, List[Dict[str, Any]]],
              ai_analysis: str = "") -> Dict[str, Any]:
        """
        Build violations report from analysis results.
        
        Args:
            file_path: Path to analyzed source file
            language: Language name
            code_structure: Code structure information
            violations: List of violation dictionaries
            heuristics: Dictionary of heuristic results
            ai_analysis: Additional AI analysis text
        
        Returns:
            Dictionary with violations report structure
        """
        # Count violations by severity
        severity_counts = {"critical": 0, "important": 0, "suggested": 0}
        for v in violations:
            severity = v.get("severity", "suggested")
            severity_counts[severity] = severity_counts.get(severity, 0) + 1
        
        return {
            "file": str(file_path),
            "language": language,
            "violations": violations,
            "summary": {
                "critical": severity_counts["critical"],
                "important": severity_counts["important"],
                "suggested": severity_counts["suggested"],
                "total": len(violations)
            },
            "code_structure": code_structure,
            "heuristics": heuristics,
            "ai_analysis": ai_analysis
        }


def clean_code_agent_build_violations_report(project_path: Path, file_path: Path, 
                                            language: str, violations: List[Dict[str, Any]],
                                            heuristics: Dict[str, List[Dict[str, Any]]],
                                            ai_analysis: str = "") -> Dict[str, Any]:
    """
    Build violations report from code analysis.
    
    This is the main builder function called by the agent.
    
    Args:
        project_path: Path to project root
        file_path: Path to analyzed source file
        language: Language name ('python' or 'javascript')
        violations: List of violation dictionaries
        heuristics: Dictionary of heuristic results
        ai_analysis: Additional AI analysis text
    
    Returns:
        Dictionary with violations report structure
    """
    # Extract code structure
    structure_builder = CodeStructureBuilder(project_path)
    code_structure = structure_builder.build(file_path, language)
    
    # Build violations report
    report_builder = ViolationsReportBuilder(project_path)
    return report_builder.build(file_path, language, code_structure, violations, heuristics, ai_analysis)


def clean_code_agent_transform_violations_to_markdown(
    project_path: Path,
    structured_content_path: Optional[Path] = None,
    template_path: Optional[Path] = None
) -> str:
    """
    Transform violations report to markdown using template.
    
    This function is called by the agent when executing the render_output action.
    
    Args:
        project_path: Path to project root
        structured_content_path: Optional path to violations_report.json (auto-detected if not provided)
        template_path: Optional path to template file (auto-detected if not provided)
    
    Returns:
        Rendered markdown string
    """
    from datetime import datetime
    
    # Load violations report
    builder = ViolationsReportBuilder(
        project_path=project_path,
        structured_content_path=structured_content_path
    )
    report = builder._load_violations_report()
    
    # Load template
    if template_path is None:
        template_path = project_path / "behaviors" / "clean-code" / "templates" / "violations-report-template.md"
    
    if not template_path.exists():
        # Fallback: generate simple markdown without template
        return _generate_simple_markdown(report)
    
    template_content = template_path.read_text(encoding='utf-8')
    
    # Simple template replacement (basic implementation)
    # In production, would use a proper templating engine
    markdown = template_content
    markdown = markdown.replace("{{file}}", report.get("file", ""))
    markdown = markdown.replace("{{language}}", report.get("language", ""))
    markdown = markdown.replace("{{generated_date}}", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    markdown = markdown.replace("{{summary.critical}}", str(report.get("summary", {}).get("critical", 0)))
    markdown = markdown.replace("{{summary.important}}", str(report.get("summary", {}).get("important", 0)))
    markdown = markdown.replace("{{summary.suggested}}", str(report.get("summary", {}).get("suggested", 0)))
    markdown = markdown.replace("{{summary.total}}", str(report.get("summary", {}).get("total", 0)))
    markdown = markdown.replace("{{code_structure.total_lines}}", str(report.get("code_structure", {}).get("total_lines", 0)))
    markdown = markdown.replace("{{code_structure.functions}}", str(len(report.get("code_structure", {}).get("functions_detail", []))))
    markdown = markdown.replace("{{code_structure.classes}}", str(len(report.get("code_structure", {}).get("classes_detail", []))))
    
    # Add violations sections
    violations = report.get("violations", [])
    critical_violations = [v for v in violations if v.get("severity") == "critical"]
    important_violations = [v for v in violations if v.get("severity") == "important"]
    suggested_violations = [v for v in violations if v.get("severity") == "suggested"]
    
    # Replace violations sections
    critical_section = _format_violations_section(critical_violations, report.get("language", ""))
    important_section = _format_violations_section(important_violations, report.get("language", ""))
    suggested_section = _format_violations_section(suggested_violations, report.get("language", ""))
    
    # Simple replacement for violations (would need proper templating engine for loops)
    markdown = markdown.replace("{{critical_violations}}", critical_section)
    markdown = markdown.replace("{{important_violations}}", important_section)
    markdown = markdown.replace("{{suggested_violations}}", suggested_section)
    
    # Add AI analysis
    ai_analysis = report.get("ai_analysis", "")
    markdown = markdown.replace("{{ai_analysis}}", ai_analysis)
    
    return markdown


def _format_violations_section(violations: List[Dict[str, Any]], language: str) -> str:
    """Format violations list as markdown"""
    if not violations:
        return "No violations found.\n"
    
    result = []
    for v in violations:
        line_info = f"**Line {v.get('line', '?')}**"
        if v.get('function'):
            line_info += f" ({v['function']}"
            if v.get('class'):
                line_info += f" in {v['class']}"
            line_info += ")"
        
        result.append(f"- {line_info}: {v.get('issue', '')}")
        result.append(f"  - **Principle:** {v.get('principle', '')}")
        result.append(f"  - **Suggestion:** {v.get('suggestion', '')}")
        
        if v.get('code_snippet'):
            result.append(f"  ```{language}")
            result.append(v['code_snippet'])
            result.append("  ```")
        
        result.append("")
    
    return "\n".join(result)


def _generate_simple_markdown(report: Dict[str, Any]) -> str:
    """Generate simple markdown without template"""
    from datetime import datetime
    
    violations = report.get("violations", [])
    summary = report.get("summary", {})
    
    markdown = f"# Clean Code Violations Report\n\n"
    markdown += f"**File:** {report.get('file', '')}\n"
    markdown += f"**Language:** {report.get('language', '')}\n"
    markdown += f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    markdown += f"## Summary\n\n"
    markdown += f"- **Critical Violations:** {summary.get('critical', 0)}\n"
    markdown += f"- **Important Violations:** {summary.get('important', 0)}\n"
    markdown += f"- **Suggested Improvements:** {summary.get('suggested', 0)}\n"
    markdown += f"- **Total Violations:** {summary.get('total', 0)}\n\n"
    
    if violations:
        markdown += "## Violations\n\n"
        for v in violations:
            markdown += f"- **Line {v.get('line', '?')}** ({v.get('function', 'unknown')}): {v.get('issue', '')}\n"
            markdown += f"  - **Severity:** {v.get('severity', 'unknown')}\n"
            markdown += f"  - **Principle:** {v.get('principle', '')}\n"
            markdown += f"  - **Suggestion:** {v.get('suggestion', '')}\n\n"
    
    ai_analysis = report.get("ai_analysis", "")
    if ai_analysis:
        markdown += f"## AI Analysis\n\n{ai_analysis}\n"
    
    return markdown

