from pathlib import Path
from typing import Dict, Any, List, Optional, Callable
from datetime import datetime
import logging
import re
import sys
from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths

logger = logging.getLogger(__name__)


class StreamingValidationReportWriter:
    """Writes a simple status file incrementally as violations are found.
    
    This writer provides real-time feedback during scanning by:
    1. Writing to a simple status file (separate from the main report)
    2. Printing progress to console
    
    The main formatted report is written by ValidationReportWriter at the end.
    """
    
    def __init__(self, behavior_name: str, bot_paths: BotPaths):
        self.behavior_name = behavior_name
        self.bot_paths = bot_paths
        self.workspace_directory = bot_paths.workspace_directory
        self._status_file = None
        self._files_scanned: Dict[str, List[Path]] = {}
        self._scanner_results: List[Dict[str, Any]] = []
        self._total_violations = 0
        self._executed_count = 0
        self._current_rule_name = ""
        self._total_files = 0
        self._files_processed = 0
        self._status_path = ""
    
    def start(self, files: Dict[str, List[Path]]) -> None:
        """Start the status file - write minimal header."""
        self._files_scanned = files
        status_path = self._get_status_path()
        
        # Ensure directory exists
        Path(status_path).parent.mkdir(parents=True, exist_ok=True)
        
        # Open status file for writing
        self._status_file = open(status_path, 'w', encoding='utf-8')
        
        test_files = files.get('test', [])
        src_files = files.get('src', [])
        total_files = len(src_files) + len(test_files)
        
        # Simple header
        self._write_line(f"# Validation Status - {self.behavior_name}")
        self._write_line(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self._write_line(f"Files: {total_files}")
        self._write_line("")
        self._flush()
        
        # Console output
        print(f"\n[VALIDATION] Scanning {total_files} files...", file=sys.stderr)
        sys.stderr.flush()
    
    def on_scanner_start(self, rule_file: str, scanner_path: str) -> None:
        """Called when a scanner starts execution."""
        self._current_rule_name = Path(rule_file).stem if rule_file else 'unknown'
        print(f"[SCANNING] {self._current_rule_name}", file=sys.stderr, end="", flush=True)
    
    def on_file_scanned(self, file_path: 'Path', violations: List[Dict[str, Any]], rule_obj: Any) -> None:
        """Called after each file is scanned - write violations immediately."""
        # Print dot for progress
        print(".", file=sys.stderr, end="", flush=True)
        
        if not violations:
            return
        
        self._total_violations += len(violations)
        file_name = file_path.name if file_path else 'unknown'
        rule_name = rule_obj.name if rule_obj else self._current_rule_name
        
        # Write rule header if this is first violation for this rule in this file
        self._write_line(f"## {rule_name}")
        self._write_line(f"**{file_name}** - {len(violations)} violation(s)")
        self._write_line("")
        
        for violation in violations:
            message = violation.get('violation_message', 'No message')
            severity = violation.get('severity', 'error')
            line_number = violation.get('line_number')
            
            severity_icon = '[X]' if severity == 'error' else '[!]' if severity == 'warning' else '[i]'
            line_info = f" (line {line_number})" if line_number else ""
            
            self._write_line(f"{severity_icon} {severity.upper()}{line_info}")
            self._write_line(f"{message}")
            self._write_line("")
        
        self._write_line("---")
        self._write_line("")
        self._flush()
    
    def on_scanner_complete(self, rule_result: Dict[str, Any]) -> None:
        """Called when a scanner completes - print console summary."""
        self._scanner_results.append(rule_result)
        
        scanner_status = rule_result.get('scanner_status', {})
        status = scanner_status.get('status', 'UNKNOWN')
        
        if status == 'EXECUTED':
            self._executed_count += 1
            violations_count = scanner_status.get('violations_found', 0)
            
            # Check severity for console output
            scanner_results = rule_result.get('scanner_results', {})
            has_errors = any(
                v.get('severity') == 'error' 
                for v in scanner_results.get('file_by_file', {}).get('violations', [])
            ) or any(
                v.get('severity') == 'error'
                for v in scanner_results.get('cross_file', {}).get('violations', [])
            )
            
            if violations_count > 0:
                if has_errors:
                    print(f" [X] {violations_count}", file=sys.stderr, flush=True)
                else:
                    print(f" [!] {violations_count}", file=sys.stderr, flush=True)
            else:
                print(f" [OK]", file=sys.stderr, flush=True)
                
        elif status == 'LOAD_FAILED':
            print(f" [LOAD FAILED]", file=sys.stderr, flush=True)
        elif status == 'EXECUTION_FAILED':
            print(f" [EXEC FAILED]", file=sys.stderr, flush=True)
        # NO_SCANNER rules - silent
    
    def finish(self, instructions: Dict[str, Any], validation_rules: List[Dict[str, Any]]) -> None:
        """Finish the status file."""
        if not self._status_file:
            return
        
        # Write completion line
        self._write_line(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self._write_line(f"Total violations: {self._total_violations}")
        self._write_line(f"Scanners executed: {self._executed_count}")
        
        self._status_file.close()
        self._status_file = None
        
        # Console summary
        print(f"\n[COMPLETE] {self._total_violations} violations, {self._executed_count} scanners", file=sys.stderr)
        sys.stderr.flush()
    
    def _write_line(self, line: str) -> None:
        """Write a line to the status file."""
        if self._status_file:
            self._status_file.write(line + '\n')
    
    def _flush(self) -> None:
        """Flush the status file to disk."""
        if self._status_file:
            self._status_file.flush()
    
    def _get_status_path(self) -> str:
        """Get the status file path (separate from main report)."""
        docs_path = self.bot_paths.documentation_path
        docs_dir = self.workspace_directory / docs_path
        status_file = docs_dir / f'{self.behavior_name}-validation-status.md'
        return str(status_file)


class ValidationReportWriter:
    def __init__(self, behavior_name: str, bot_paths: BotPaths):
        self.behavior_name = behavior_name
        self.bot_paths = bot_paths
        self.workspace_directory = bot_paths.workspace_directory
    
    def write(self, instructions: Dict[str, Any], validation_rules: List[Dict[str, Any]], files: Dict[str, List[Path]]) -> None:
        report_path = self._get_report_path()
        
        logger.info("=== _write_validation_report START ===")
        logger.info(f"Report path: {report_path}")
        logger.info(f"Number of validation rules: {len(validation_rules)}")
        
        try:
            report_file = Path(report_path)
            report_file.parent.mkdir(parents=True, exist_ok=True)
            
            lines = self._build_report_lines(instructions, validation_rules, files, report_path)
            
            logger.info("Step 4: Writing report to file...")
            logger.info(f"Report file path: {report_file}")
            logger.info(f"Number of lines to write: {len(lines)}")
            report_file.write_text('\n'.join(lines), encoding='utf-8')
            logger.info("Report file written successfully")
            logger.info("=== _write_validation_report COMPLETE ===")
        except Exception as e:
            import traceback
            logger.error("=== ERROR in _write_validation_report ===")
            logger.error(f"Error type: {type(e).__name__}")
            logger.error(f"Error message: {e}")
            logger.error(f"Report path: {report_path}")
            logger.error(f"Full traceback:\n{traceback.format_exc()}")
            raise
    
    def get_report_path(self) -> Path:
        docs_path = self.bot_paths.documentation_path
        docs_dir = self.workspace_directory / docs_path
        report_file = docs_dir / f'{self.behavior_name}-validation-report.md'
        return report_file
    
    def _get_report_path(self) -> str:
        return str(self.get_report_path())
    
    def get_report_hyperlink(self) -> str:
        report_path = self.get_report_path()
        try:
            resolved_path = report_path.resolve() if report_path.exists() else report_path
            file_str = str(resolved_path).replace('\\', '/')
            if len(file_str) >= 2 and file_str[1] == ':':
                file_str = file_str[0].upper() + ':' + file_str[2:]
            vscode_uri = f"vscode://file/{file_str}"
            
            try:
                rel_path = str(report_path.relative_to(self.workspace_directory))
            except ValueError:
                rel_path = str(report_path)
            
            return f"[{rel_path}]({vscode_uri})"
        except Exception as e:
            logger.warning(f"Could not create report hyperlink: {e}")
            return str(report_path)
    
    def _build_report_lines(self, instructions: Dict[str, Any], validation_rules: List[Dict[str, Any]], files: Dict[str, List[Path]], report_path: str) -> List[str]:
        lines = []
        lines.extend(self._build_header())
        lines.extend(self._build_metadata())
        lines.extend(self._build_summary(validation_rules))
        lines.extend(self._build_content_validated(files))
        lines.extend(self._build_scanner_status(validation_rules))
        lines.extend(self._build_validation_rules(validation_rules))
        lines.extend(self._build_violations(validation_rules))
        lines.extend(self._build_instructions(instructions))
        lines.extend(self._build_report_location(report_path))
        return lines
    
    def _build_header(self) -> List[str]:
        return [
            f"# Validation Report - {self.behavior_name.replace('_', ' ').title()}",
            ""
        ]
    
    def _build_metadata(self) -> List[str]:
        return [
            f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Project:** {self.workspace_directory.name}",
            f"**Behavior:** {self.behavior_name}",
            f"**Action:** validate",
            ""
        ]
    
    def _build_summary(self, validation_rules: List[Dict[str, Any]]) -> List[str]:
        total_rules = len(validation_rules)
        return [
            "## Summary",
            "",
            f"Validated story map and domain model against **{total_rules} validation rules**.",
            ""
        ]
    
    def _build_content_validated(self, files: Dict[str, List[Path]]) -> List[str]:
        lines = [
            "## Content Validated",
            ""
        ]
        
        clarification_file, planning_file, rendered_outputs = self._find_content_files()
        
        if clarification_file:
            lines.append(f"- **Clarification:** `{clarification_file.name}`")
        if planning_file:
            lines.append(f"- **Planning:** `{planning_file.name}`")
        if rendered_outputs:
            lines.append("- **Rendered Outputs:**")
            for output in rendered_outputs:
                lines.append(f"  - `{output.name}`")
        
        test_files_scanned = [str(fp) for fp in files.get('test', [])]
        code_files_scanned = [str(fp) for fp in files.get('src', [])]
        
        lines.extend(self._build_scanned_files_section('test', test_files_scanned, 'Test Files Scanned'))
        lines.extend(self._build_scanned_files_section('src', code_files_scanned, 'Code Files Scanned'))
        
        lines.append("")
        return lines
    
    def _find_content_files(self) -> tuple:
        docs_path = self.bot_paths.documentation_path
        docs_dir = self.workspace_directory / docs_path
        
        clarification_file = docs_dir / 'clarification.json'
        planning_file = docs_dir / 'planning.json'
        
        clarification = clarification_file if clarification_file.exists() else None
        planning = planning_file if planning_file.exists() else None
        
        rendered_outputs = []
        rendered_patterns = [
            '*-story-map.md',
            '*-domain-model-description.md',
            '*-domain-model-diagram.md',
            'story-graph.json',
            '*-increments.md'
        ]
        for pattern in rendered_patterns:
            for file_path in docs_dir.glob(pattern):
                rendered_outputs.append(file_path)
        
        return clarification, planning, rendered_outputs
    
    def _build_scanned_files_section(self, file_type: str, files_scanned: List[str], section_title: str) -> List[str]:
        lines = []
        if files_scanned:
            logger.info(f"{section_title} from content_info: {len(files_scanned)} files")
            lines.append(f"- **{section_title}:**")
            for file_str in sorted(files_scanned):
                file_path = Path(file_str)
                rel_path = self._get_relative_path(file_path)
                lines.append(f"  - `{rel_path}`")
            lines.append(f"  - **Total:** {len(files_scanned)} {file_type} file(s)")
        return lines
    
    def _get_relative_path(self, file_path: Path) -> str:
        try:
            if file_path.is_absolute() and self.workspace_directory:
                return str(file_path.relative_to(self.workspace_directory))
            elif self.workspace_directory and not file_path.is_absolute():
                try:
                    resolved = (self.workspace_directory / file_path).resolve()
                    return str(resolved.relative_to(self.workspace_directory))
                except (ValueError, AttributeError):
                    return file_path.name
            else:
                return file_path.name
        except (ValueError, AttributeError) as e:
            logger.warning(f"Could not create relative path for {file_path}: {e}")
            return file_path.name
    
    def _rule_name_to_anchor(self, rule_name: str) -> str:
        """Convert rule name to markdown anchor link.
        
        Converts rule name like 'use_class_based_organization' to anchor '#use-class-based-organization'
        """
        # Replace underscores with hyphens, convert to lowercase
        anchor = rule_name.replace('_', '-').lower()
        return f"#{anchor}"
    
    def _build_scanner_status(self, validation_rules: List[Dict[str, Any]]) -> List[str]:
        lines = [
            "## Scanner Execution Status",
            ""
        ]
        
        executed_count = 0
        load_failed_count = 0
        execution_failed_count = 0
        no_scanner_count = 0
        
        executed_rules = []
        load_failed_rules = []
        execution_failed_rules = []
        no_scanner_rules = []
        
        # Track violation counts for status indicators
        total_violations = 0
        rules_with_errors = 0
        rules_with_warnings = 0
        rules_clean = 0
        
        for rule_dict in validation_rules:
            rule_file = rule_dict.get('rule_file', 'unknown')
            scanner_status = rule_dict.get('scanner_status', {})
            status = scanner_status.get('status', 'UNKNOWN')
            
            if status == 'EXECUTED':
                executed_count += 1
                violations = scanner_status.get('violations_found', 0)
                exec_status = scanner_status.get('execution_status', 'SUCCESS')
                total_violations += violations
                
                # Check violation severities
                scanner_results = rule_dict.get('scanner_results', {})
                has_errors = False
                has_warnings = False
                if 'file_by_file' in scanner_results:
                    for v in scanner_results['file_by_file'].get('violations', []):
                        if v.get('severity') == 'error':
                            has_errors = True
                        elif v.get('severity') == 'warning':
                            has_warnings = True
                if 'cross_file' in scanner_results:
                    for v in scanner_results['cross_file'].get('violations', []):
                        if v.get('severity') == 'error':
                            has_errors = True
                        elif v.get('severity') == 'warning':
                            has_warnings = True
                
                if has_errors:
                    rules_with_errors += 1
                elif has_warnings:
                    rules_with_warnings += 1
                elif violations == 0:
                    rules_clean += 1
                
                executed_rules.append({
                    'rule': rule_file,
                    'violations': violations,
                    'execution_status': exec_status,
                    'scanner_path': scanner_status.get('scanner_path', 'unknown'),
                    'has_errors': has_errors,
                    'has_warnings': has_warnings
                })
            elif status == 'LOAD_FAILED':
                load_failed_count += 1
                load_failed_rules.append({
                    'rule': rule_file,
                    'scanner_path': scanner_status.get('scanner_path', 'unknown'),
                    'error': scanner_status.get('error', 'Unknown error')
                })
            elif status == 'EXECUTION_FAILED':
                execution_failed_count += 1
                execution_failed_rules.append({
                    'rule': rule_file,
                    'scanner_path': scanner_status.get('scanner_path', 'unknown'),
                    'error': scanner_status.get('error', 'Unknown error')
                })
            elif status == 'NO_SCANNER':
                no_scanner_count += 1
                no_scanner_rules.append(rule_file)
        
        total_with_scanners = executed_count + load_failed_count + execution_failed_count
        
        # Build visual status summary
        lines.extend(self._build_status_summary(
            len(validation_rules), total_with_scanners, executed_count, 
            load_failed_count, execution_failed_count, no_scanner_count,
            total_violations, rules_clean, rules_with_warnings, rules_with_errors,
            executed_rules
        ))
        lines.append("")
        
        if executed_rules:
            lines.append("### ✅ Successfully Executed Scanners")
            lines.append("")
            # Sort by violations (most violations first) then by name
            executed_rules.sort(key=lambda x: (-x['violations'], x['rule']))
            
            for rule_info in executed_rules:
                violations = rule_info['violations']
                rule_name = Path(rule_info['rule']).stem if rule_info['rule'] else 'unknown'
                
                # Determine status indicator
                if rule_info['has_errors']:
                    status_indicator = "🔴"
                    status_text = "ERRORS"
                elif rule_info['has_warnings']:
                    status_indicator = "🟡"
                    status_text = "WARNINGS"
                elif violations == 0:
                    status_indicator = "🟢"
                    status_text = "CLEAN"
                else:
                    status_indicator = "🟡"
                    status_text = "VIOLATIONS"
                
                violations_text = f"{violations} violation(s)" if violations > 0 else "0 violations"
                exec_status = rule_info.get('execution_status', 'SUCCESS')
                
                # Create anchor link to detailed rule section
                anchor_link = self._rule_name_to_anchor(rule_name)
                rule_display_name = rule_name.replace('_', ' ').title()
                
                # Add "View Details" link if there are violations
                details_link = ""
                if violations > 0:
                    violations_anchor = f"#{rule_name.replace('_', '-').lower()}-violations"
                    details_link = f" - [View Details]({violations_anchor})"
                
                if exec_status != 'SUCCESS':
                    lines.append(f"- {status_indicator} **[{rule_display_name}]({anchor_link})** - {violations_text} ({exec_status}){details_link}")
                else:
                    lines.append(f"- {status_indicator} **[{rule_display_name}]({anchor_link})** - {violations_text} ({status_text}){details_link}")
                lines.append(f"  - Scanner: `{rule_info['scanner_path']}`")
            lines.append("")
        
        if load_failed_rules:
            lines.append("### 🔴 Scanner Load Failures")
            lines.append("")
            for rule_info in load_failed_rules:
                rule_name = Path(rule_info['rule']).stem if rule_info['rule'] else 'unknown'
                anchor_link = self._rule_name_to_anchor(rule_name)
                rule_display_name = rule_name.replace('_', ' ').title()
                lines.append(f"- 🔴 **[{rule_display_name}]({anchor_link})** - LOAD FAILED")
                lines.append(f"  - Scanner Path: `{rule_info['scanner_path']}`")
                lines.append(f"  - Error: `{rule_info['error']}`")
            lines.append("")
        
        if execution_failed_rules:
            lines.append("### 🔴 Scanner Execution Failures")
            lines.append("")
            for rule_info in execution_failed_rules:
                rule_name = Path(rule_info['rule']).stem if rule_info['rule'] else 'unknown'
                anchor_link = self._rule_name_to_anchor(rule_name)
                rule_display_name = rule_name.replace('_', ' ').title()
                lines.append(f"- 🔴 **[{rule_display_name}]({anchor_link})** - EXECUTION FAILED")
                lines.append(f"  - Scanner Path: `{rule_info['scanner_path']}`")
                lines.append(f"  - Error: `{rule_info['error']}`")
            lines.append("")
        
        if no_scanner_rules:
            lines.append("### ⚪ Rules Without Scanners")
            lines.append("")
            for rule_file in no_scanner_rules[:10]:  # Show first 10
                rule_name = Path(rule_file).stem if rule_file else 'unknown'
                anchor_link = self._rule_name_to_anchor(rule_name)
                rule_display_name = rule_name.replace('_', ' ').title()
                lines.append(f"- ⚪ **[{rule_display_name}]({anchor_link})** - No scanner configured")
            if len(no_scanner_rules) > 10:
                lines.append(f"- *... and {len(no_scanner_rules) - 10} more rules without scanners*")
            lines.append("")
        
        return lines
    
    def _build_status_summary(self, total_rules: int, total_with_scanners: int, 
                             executed_count: int, load_failed_count: int, 
                             execution_failed_count: int, no_scanner_count: int,
                             total_violations: int, rules_clean: int, 
                             rules_with_warnings: int, rules_with_errors: int,
                             executed_rules: List[Dict[str, Any]]) -> List[str]:
        """Build a visual status summary at the top of scanner status section."""
        lines = []
        
        # Overall status indicator
        if execution_failed_count > 0 or load_failed_count > 0:
            overall_status = "🔴"
            overall_text = "CRITICAL ISSUES"
        elif total_violations > 0:
            if rules_with_errors > 0:
                overall_status = "🔴"
                overall_text = "VIOLATIONS FOUND"
            elif rules_with_warnings > 0:
                overall_status = "🟡"
                overall_text = "WARNINGS FOUND"
            else:
                overall_status = "🟡"
                overall_text = "VIOLATIONS FOUND"
        else:
            overall_status = "🟢"
            overall_text = "ALL CLEAN"
        
        lines.append(f"### {overall_status} Overall Status: {overall_text}")
        lines.append("")
        
        # Summary table
        lines.append("| Status | Count | Description |")
        lines.append("|--------|-------|-------------|")
        
        # Execution status
        if executed_count > 0:
            if rules_clean > 0:
                lines.append(f"| 🟢 Executed Successfully | {executed_count} | Scanners ran without errors |")
            else:
                lines.append(f"| ✅ Executed Successfully | {executed_count} | Scanners executed |")
        
        if rules_clean > 0:
            lines.append(f"| 🟢 Clean Rules | {rules_clean} | No violations found |")
        
        if rules_with_warnings > 0:
            warning_count = sum(r['violations'] for r in executed_rules if r.get('has_warnings') and not r.get('has_errors'))
            lines.append(f"| 🟡 Rules with Warnings | {rules_with_warnings} | Found {warning_count} warning violation(s) |")
        
        if rules_with_errors > 0:
            error_count = sum(r['violations'] for r in executed_rules if r.get('has_errors'))
            lines.append(f"| 🔴 Rules with Errors | {rules_with_errors} | Found {error_count} error violation(s) |")
        
        if load_failed_count > 0:
            lines.append(f"| 🔴 Load Failed | {load_failed_count} | Scanner could not be loaded |")
        
        if execution_failed_count > 0:
            lines.append(f"| 🔴 Execution Failed | {execution_failed_count} | Scanner crashed during execution |")
        
        if no_scanner_count > 0:
            lines.append(f"| ⚪ No Scanner | {no_scanner_count} | Rule has no scanner configured |")
        
        lines.append("")
        lines.append(f"**Total Rules:** {total_rules}")
        lines.append(f"- **Rules with Scanners:** {total_with_scanners}")
        lines.append(f"  - ✅ **Executed Successfully:** {executed_count}")
        if load_failed_count > 0:
            lines.append(f"  - 🔴 **Load Failed:** {load_failed_count}")
        if execution_failed_count > 0:
            lines.append(f"  - 🔴 **Execution Failed:** {execution_failed_count}")
        if no_scanner_count > 0:
            lines.append(f"- ⚪ **Rules without Scanners:** {no_scanner_count}")
        
        return lines
    
    def _build_validation_rules(self, validation_rules: List[Dict[str, Any]]) -> List[str]:
        lines = [
            "## Validation Rules Checked",
            ""
        ]
        
        total_rules = len(validation_rules)
        
        # Build a lookup of rule status for quick access
        rule_status_lookup = {}
        for rule_dict in validation_rules:
            rule_file = rule_dict.get('rule_file', 'unknown')
            scanner_status = rule_dict.get('scanner_status', {})
            status = scanner_status.get('status', 'UNKNOWN')
            violations = scanner_status.get('violations_found', 0)
            
            # Check violation severities
            has_errors = False
            has_warnings = False
            if status == 'EXECUTED':
                scanner_results = rule_dict.get('scanner_results', {})
                if 'file_by_file' in scanner_results:
                    for v in scanner_results['file_by_file'].get('violations', []):
                        if v.get('severity') == 'error':
                            has_errors = True
                        elif v.get('severity') == 'warning':
                            has_warnings = True
                if 'cross_file' in scanner_results:
                    for v in scanner_results['cross_file'].get('violations', []):
                        if v.get('severity') == 'error':
                            has_errors = True
                        elif v.get('severity') == 'warning':
                            has_warnings = True
            
            rule_status_lookup[rule_file] = {
                'status': status,
                'violations': violations,
                'has_errors': has_errors,
                'has_warnings': has_warnings,
                'scanner_path': scanner_status.get('scanner_path', 'unknown'),
                'execution_status': scanner_status.get('execution_status', 'SUCCESS'),
                'error': scanner_status.get('error', None)
            }
        
        # Sort rules: errors first, then warnings, then clean, then no scanner
        def sort_key(rule_dict):
            rule_file = rule_dict.get('rule_file', 'unknown')
            status_info = rule_status_lookup.get(rule_file, {})
            status = status_info.get('status', 'UNKNOWN')
            has_errors = status_info.get('has_errors', False)
            has_warnings = status_info.get('has_warnings', False)
            violations = status_info.get('violations', 0)
            
            if status == 'EXECUTION_FAILED' or status == 'LOAD_FAILED':
                return (0, 0, 0)  # Failures first
            elif has_errors:
                return (1, -violations, rule_file)  # Errors next, sorted by violation count
            elif has_warnings:
                return (2, -violations, rule_file)  # Warnings next
            elif violations == 0 and status == 'EXECUTED':
                return (3, 0, rule_file)  # Clean rules
            else:
                return (4, 0, rule_file)  # No scanner last
        
        sorted_rules = sorted(validation_rules, key=sort_key)
        
        for rule_dict in sorted_rules[:20]:
            rule_file = rule_dict.get('rule_file', 'unknown')
            rule_content = rule_dict.get('rule_content', rule_dict)
            description = rule_content.get('description', 'No description')
            rule_name = Path(rule_file).stem if rule_file else 'unknown'
            
            status_info = rule_status_lookup.get(rule_file, {})
            status = status_info.get('status', 'UNKNOWN')
            violations = status_info.get('violations', 0)
            has_errors = status_info.get('has_errors', False)
            has_warnings = status_info.get('has_warnings', False)
            scanner_path = status_info.get('scanner_path', 'unknown')
            execution_status = status_info.get('execution_status', 'SUCCESS')
            error = status_info.get('error', None)
            
            # Determine status indicator and text
            if status == 'EXECUTION_FAILED' or status == 'LOAD_FAILED':
                status_indicator = "🔴"
                status_text = "FAILED"
            elif status == 'NO_SCANNER':
                status_indicator = "⚪"
                status_text = "NO SCANNER"
            elif has_errors:
                status_indicator = "🔴"
                status_text = f"{violations} ERROR(S)"
            elif has_warnings:
                status_indicator = "🟡"
                status_text = f"{violations} WARNING(S)"
            elif violations == 0:
                status_indicator = "🟢"
                status_text = "CLEAN (0 violations)"
            else:
                status_indicator = "🟡"
                status_text = f"{violations} VIOLATION(S)"
            
            # Add explicit anchor ID for linking from summary section
            anchor_id = rule_name.replace('_', '-').lower()
            rule_title = rule_name.replace('_', ' ').title()
            
            # Add link to violations section if there are violations
            violations_link = ""
            if violations > 0:
                violations_anchor = f"#{rule_name.replace('_', '-').lower()}-violations"
                violations_link = f" - [View Details]({violations_anchor})"
            
            lines.append(f"### {status_indicator} Rule: <span id=\"{anchor_id}\">{rule_title}</span> - {status_text}{violations_link}")
            lines.append(f"**Description:** {description}")
            
            if status == 'EXECUTED':
                if scanner_path != 'unknown':
                    lines.append(f"**Scanner:** `{scanner_path}`")
                if execution_status != 'SUCCESS':
                    lines.append(f"**Execution Status:** {execution_status}")
            elif status == 'LOAD_FAILED' or status == 'EXECUTION_FAILED':
                if scanner_path != 'unknown':
                    lines.append(f"**Scanner:** `{scanner_path}`")
                if error:
                    lines.append(f"**Error:** `{error}`")
            elif status == 'NO_SCANNER':
                lines.append("**Scanner:** Not configured")
            
            lines.append("")
        
        if total_rules > 20:
            lines.append(f"*... and {total_rules - 20} more rules*")
            lines.append("")
        
        return lines
    
    def _build_violations(self, validation_rules: List[Dict[str, Any]]) -> List[str]:
        lines = [
            "## Violations Found",
            ""
        ]
        
        file_by_file_violations_by_rule, cross_file_violations_by_rule = self._organize_violations(validation_rules)
        total_file_by_file = sum(len(v) for v in file_by_file_violations_by_rule.values())
        total_cross_file = sum(len(v) for v in cross_file_violations_by_rule.values())
        total_violations = total_file_by_file + total_cross_file
        
        if total_violations == 0:
            lines.append("✅ **No violations found.** All rules passed validation.")
            lines.append("")
        else:
            lines.append(f"**Total Violations:** {total_violations}")
            lines.append(f"- **File-by-File Violations:** {total_file_by_file}")
            lines.append(f"- **Cross-File Violations:** {total_cross_file}")
            lines.append("")
            
            if file_by_file_violations_by_rule:
                lines.extend(self._build_violations_by_type(file_by_file_violations_by_rule, "File-by-File Violations (Pass 1)", 
                    "These violations were detected by scanning each file individually."))
            
            if cross_file_violations_by_rule:
                lines.extend(self._build_violations_by_type(cross_file_violations_by_rule, "Cross-File Violations (Pass 2)",
                    "These violations were detected by analyzing all files together to find patterns that span multiple files."))
        
        return lines
    
    def _organize_violations(self, validation_rules: List[Dict[str, Any]]) -> tuple:
        file_by_file_violations_by_rule = {}
        cross_file_violations_by_rule = {}
        
        for rule_dict in validation_rules:
            rule_file = rule_dict.get('rule_file', 'unknown')
            scanner_results = rule_dict.get('scanner_results', {})
            rule_name = Path(rule_file).stem if rule_file else 'unknown'
            
            if 'file_by_file' in scanner_results or 'cross_file' in scanner_results:
                file_by_file_violations = scanner_results.get('file_by_file', {}).get('violations', [])
                cross_file_violations = scanner_results.get('cross_file', {}).get('violations', [])
                
                if file_by_file_violations:
                    file_by_file_violations_by_rule[rule_name] = file_by_file_violations
                if cross_file_violations:
                    cross_file_violations_by_rule[rule_name] = cross_file_violations
            elif 'violations' in scanner_results:
                violations = scanner_results.get('violations', [])
                if violations:
                    file_by_file_violations_by_rule[rule_name] = violations
        
        return file_by_file_violations_by_rule, cross_file_violations_by_rule
    
    def _build_violations_by_type(self, violations_by_rule: Dict[str, List[Dict[str, Any]]], title: str, description: str) -> List[str]:
        lines = [
            f"### {title}",
            "",
            description,
            ""
        ]
        
        for rule_name, violations in violations_by_rule.items():
            # Add anchor ID for linking from summary section
            violations_anchor_id = f"{rule_name.replace('_', '-').lower()}-violations"
            rule_display_name = rule_name.replace('_', ' ').title()
            lines.append(f"#### <span id=\"{violations_anchor_id}\">{rule_display_name}: {len(violations)} violation(s)</span>")
            lines.append("")
            
            for violation in violations:
                location = violation.get('location', 'unknown')
                message = violation.get('violation_message', 'No message')
                severity = violation.get('severity', 'error')
                line_number = violation.get('line_number')
                severity_icon = '🔴' if severity == 'error' else '🟡' if severity == 'warning' else '🔵'
                
                location_link = self._create_file_link(location, line_number)
                test_info = self._extract_test_info(message, location, line_number)
                
                # Format message - if it contains code blocks, preserve them
                formatted_message = self._format_violation_message(message)
                
                if test_info:
                    lines.append(f"- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}")
                else:
                    # If message contains code blocks or multiple lines, format it properly
                    if '\n' in formatted_message:
                        # Split message into parts
                        parts = formatted_message.split('\n')
                        # First line goes on the bullet point
                        first_line = parts[0] if parts else formatted_message
                        remaining_parts = parts[1:] if len(parts) > 1 else []
                        
                        lines.append(f"- {severity_icon} **{severity.upper()}** - {location_link}: {first_line}")
                        # Add remaining parts - code blocks need proper indentation in markdown lists
                        in_code_block = False
                        for part in remaining_parts:
                            # Code blocks in markdown lists need 4-space indentation
                            if part.strip().startswith('```'):
                                in_code_block = not in_code_block
                                lines.append(f"    {part}")
                            elif in_code_block:
                                # Inside code block, preserve indentation
                                lines.append(f"    {part}")
                            elif part.strip() == '':
                                lines.append("")
                            else:
                                lines.append(f"  {part}")
                    else:
                        lines.append(f"- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}")
            
            lines.append("")
        
        return lines
    
    def _build_instructions(self, instructions: Dict[str, Any]) -> List[str]:
        lines = [
            "## Validation Instructions",
            ""
        ]
        
        base_instructions = instructions.get('base_instructions', [])
        if base_instructions:
            lines.append("The following validation steps were performed:")
            lines.append("")
            for i, instruction in enumerate(base_instructions[:10], 1):
                lines.append(f"{i}. {instruction}")
            if len(base_instructions) > 10:
                lines.append(f"*... and {len(base_instructions) - 10} more instructions*")
        lines.append("")
        
        return lines
    
    def _build_report_location(self, report_path: str) -> List[str]:
        return [
            "## Report Location",
            "",
            f"This report was automatically generated and saved to:",
            f"`{report_path}`",
            ""
        ]
    
    def _create_file_link(self, location: str, line_number: Optional[int] = None) -> str:
        if location == 'unknown' or not location:
            return f"`{location}`"
        
        try:
            file_path = Path(location)
            
            is_absolute = file_path.is_absolute() or (len(location) > 1 and location[1] == ':') or location.startswith('\\\\')
            
            if is_absolute:
                if self.workspace_directory:
                    try:
                        rel_path = file_path.relative_to(self.workspace_directory)
                        file_uri = self._get_file_uri(location, line_number)
                        return f"[`{rel_path}`]({file_uri})"
                    except ValueError:
                        file_uri = self._get_file_uri(location, line_number)
                        return f"[`{Path(location).name}`]({file_uri})"
                else:
                    file_uri = self._get_file_uri(location, line_number)
                    return f"[`{Path(location).name}`]({file_uri})"
            else:
                return f"[`{location}`]({self._get_file_uri(location, line_number)})"
        except Exception:
            try:
                file_uri = self._get_file_uri(location, line_number)
                return f"[`{Path(location).name if location else location}`]({file_uri})"
            except Exception:
                if line_number:
                    return f"`{location}:{line_number}`"
                return f"`{location}`"
    
    def _format_violation_message(self, message: str) -> str:
        """Format violation message, preserving code blocks."""
        return message
    
    def _extract_test_info(self, message: str, location: str, line_number: Optional[int] = None) -> Optional[str]:
        test_method_patterns = [
            r'Test\s+method\s+["\']([^"\']+)["\']',
            r'Test\s+["\']([^"\']+)["\']',
            r'test\s+method\s+["\']([^"\']+)["\']',
        ]
        
        test_class_patterns = [
            r'Test\s+class\s+["\']([^"\']+)["\']',
            r'class\s+["\']([^"\']+)["\']',
        ]
        
        test_method_match = None
        for pattern in test_method_patterns:
            test_method_match = re.search(pattern, message, re.IGNORECASE)
            if test_method_match:
                break
        
        test_class_match = None
        for pattern in test_class_patterns:
            test_class_match = re.search(pattern, message, re.IGNORECASE)
            if test_class_match:
                break
        
        if not test_method_match and not test_class_match:
            return None
        
        file_uri = self._get_file_uri(location, line_number)
        
        try:
            if test_method_match:
                test_method_name = test_method_match.group(1)
                replacement = f'Test method [{test_method_name}]({file_uri})'
                message = message.replace(f'Test method "{test_method_name}"', replacement)
                message = message.replace(f"Test method '{test_method_name}'", replacement)
                message = message.replace(f'Test "{test_method_name}"', replacement)
                message = message.replace(f"Test '{test_method_name}'", replacement)
                message = message.replace(f'test method "{test_method_name}"', replacement)
                message = message.replace(f"test method '{test_method_name}'", replacement)
            
            if test_class_match:
                test_class_name = test_class_match.group(1)
                replacement = f'Test class [{test_class_name}]({file_uri})'
                message = message.replace(f'Test class "{test_class_name}"', replacement)
                message = message.replace(f"Test class '{test_class_name}'", replacement)
                message = message.replace(f'class "{test_class_name}"', replacement)
                message = message.replace(f"class '{test_class_name}'", replacement)
        except Exception as e:
            logger.warning(f"Failed to create test info links: {e}, returning original message")
            return None
        
        return message
    
    def _get_file_uri(self, location: str, line_number: Optional[int] = None) -> str:
        try:
            file_path = Path(location)
            if file_path.is_absolute():
                resolved_path = file_path.resolve() if file_path.exists() else file_path
            else:
                if self.workspace_directory:
                    resolved_path = (self.workspace_directory / file_path).resolve()
                else:
                    resolved_path = Path(location)
            
            file_str = str(resolved_path).replace('\\', '/')
            if len(file_str) >= 2 and file_str[1] == ':':
                file_str = file_str[0].upper() + ':' + file_str[2:]
            
            vscode_uri = f"vscode://file/{file_str}"
            
            if line_number:
                vscode_uri = f"{vscode_uri}:{line_number}"
            
            return vscode_uri
        except Exception:
            file_str = location.replace('\\', '/')
            if len(file_str) >= 2 and file_str[1] == ':':
                file_str = file_str[0].upper() + ':' + file_str[2:]
            vscode_uri = f"vscode://file/{file_str}"
            if line_number:
                vscode_uri = f"{vscode_uri}:{line_number}"
            return vscode_uri
