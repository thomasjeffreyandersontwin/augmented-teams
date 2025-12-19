from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Iterator, Dict, Any, TYPE_CHECKING, Callable
from pathlib import Path
from agile_bot.bots.base_bot.src.actions.validate.rule import Rule

if TYPE_CHECKING:
    pass


@dataclass
class ValidationCallbacks:
    """Callbacks for validation progress - groups on_scanner_start, on_scanner_complete, on_file_scanned."""
    on_scanner_start: Optional[Callable] = None
    on_scanner_complete: Optional[Callable] = None
    on_file_scanned: Optional[Callable] = None


class Rules:
    def __init__(self, behavior=None, bot_config=None, bot_paths=None):
        self.behavior = behavior
        self.bot_config = bot_config
        
        if behavior:
            if not bot_paths:
                raise ValueError("bot_paths is required when behavior is provided")
            self.bot_name = behavior.bot_name
            self.behavior_name = behavior.name
            self.bot_paths = bot_paths
        elif bot_config:
            self.bot_name = bot_config.name
            self.behavior_name = 'common'
            self.bot_paths = bot_paths
        else:
            raise ValueError("Either behavior or bot_config must be provided")
        
        self._rules: Optional[List[Rule]] = None
        self._all_violations: List[Dict[str, Any]] = []
    
    def _load_rules(self) -> List[Rule]:
        if self._rules is not None:
            return self._rules
        
        all_rules = []
        bot_rules = self._load_bot_rules()
        all_rules.extend(bot_rules)
        
        if self.behavior:
            behavior_rules = self._load_behavior_rules()
            all_rules.extend(behavior_rules)
        
        self._rules = all_rules
        return self._rules
    
    def _load_bot_rules(self) -> List[Rule]:
        bot_rules = []
        bot_dir = self.bot_paths.bot_directory
        bot_rules_dir = bot_dir / 'rules'
        for rule_file in bot_rules_dir.glob('*.json'):
            rule_obj = Rule(
                rule_file_path=rule_file,
                behavior_name='common',
                bot_name=self.bot_name
            )
            bot_rules.append(rule_obj)
        
        return bot_rules
    
    def _create_rule(self, rule_file: Path) -> Rule:
        """Create a Rule object from a rule file path."""
        return Rule(
            rule_file_path=rule_file,
            behavior_name=self.behavior_name,
            bot_name=self.bot_name
        )
    
    def _load_rules_from_subdir(self, subdir: Path, behavior_rules_dir: Path) -> List[Rule]:
        """Load rules from a subdirectory, skipping already loaded rules."""
        rules = []
        for rule_file in subdir.rglob('*.json'):
            if behavior_rules_dir.exists() and rule_file.is_relative_to(behavior_rules_dir):
                continue
            try:
                rules.append(self._create_rule(rule_file))
            except Exception:
                continue
        return rules
    
    def _load_behavior_rules(self) -> List[Rule]:
        behavior_folder = self.bot_paths.bot_directory / 'behaviors' / self.behavior_name
        behavior_rules_dir = behavior_folder / 'rules'
        
        behavior_rules = [self._create_rule(f) for f in behavior_rules_dir.glob('*.json')]
        
        for subdir_name in ['3_rules', 'rules']:
            subdir = behavior_folder / subdir_name
            if subdir != behavior_rules_dir:
                behavior_rules.extend(self._load_rules_from_subdir(subdir, behavior_rules_dir))
        
        return behavior_rules
    
    def find_by_name(self, rule_name: str) -> Optional[Rule]:
        rules = self._load_rules()
        for rule in rules:
            if rule.name == rule_name:
                return rule
        return None
    
    def __iter__(self) -> Iterator[Rule]:
        rules = self._load_rules()
        for rule in rules:
            yield rule
    
    def __len__(self) -> int:
        return len(self._load_rules())
    
    def add_violations(self, violations: List[Dict[str, Any]]) -> None:
        self._all_violations.extend(violations)
    
    @property
    def violations(self) -> List[Dict[str, Any]]:
        return self._all_violations
    
    @property
    def violation_summary(self) -> List[str]:
        summary = []
        for rule in self._load_rules():
            if rule.has_scanner and rule.violations:
                file_by_file_count = len(rule.file_by_file_violations)
                cross_file_count = len(rule.cross_file_violations)
                if file_by_file_count > 0 or cross_file_count > 0:
                    summary.append(
                        f"Rule {rule.rule_file}: "
                        f"{file_by_file_count} file-by-file, {cross_file_count} cross-file violations"
                    )
        return summary
    
    def formatted_rules(self) -> str:
        rules = self._load_rules()
        if not rules:
            return "No validation rules found."
        
        formatted_sections = []
        bot_rules = []
        behavior_rules = []
        
        for rule in rules:
            rule_file = rule.rule_file
            
            if 'base_bot/rules' in rule_file or (not 'behaviors' in rule_file and '/rules/' in rule_file):
                bot_rules.append(rule)
            else:
                behavior_rules.append(rule)
        
        if bot_rules:
            formatted_sections.append("**Bot-level rules:**")
            for rule in bot_rules:
                formatted_sections.extend(rule.formatted_text())
        
        if behavior_rules:
            formatted_sections.append("**Behavior-level rules:**")
            for rule in behavior_rules:
                formatted_sections.extend(rule.formatted_text())
        
        if not formatted_sections:
            return "No validation rules found."
        
        return "\n".join(formatted_sections)
    
    def _extract_error_message(self, execution_status: str, scanner_results: Any) -> str:
        """Extract error message from scanner results."""
        if execution_status.startswith('EXECUTION_FAILED'):
            return execution_status
        if not isinstance(scanner_results, dict):
            return f"Scanner execution failed: {execution_status}"
        if 'error' in scanner_results:
            return scanner_results['error']
        file_by_file = scanner_results.get('file_by_file', {})
        if isinstance(file_by_file, dict) and 'error' in file_by_file:
            return file_by_file['error']
        return f"Scanner execution failed: {execution_status}"
    
    def _has_scanner_error(self, execution_status: str, scanner_results: Any) -> bool:
        """Check if scanner execution had an error."""
        if execution_status.startswith('EXECUTION_FAILED') or execution_status.startswith('EXECUTION_SKIPPED'):
            return True
        if not isinstance(scanner_results, dict):
            return False
        if 'error' in scanner_results:
            return True
        file_by_file = scanner_results.get('file_by_file', {})
        return isinstance(file_by_file, dict) and 'error' in file_by_file
    
    def _flush_logger_handlers(self, logger) -> None:
        """Flush all logger handlers."""
        for handler in logger.handlers:
            handler.flush()
    
    def _process_scanner_result(self, rule, rule_result: dict, scanner_results: Any, scanner_path: str, scanner_name: str, logger) -> str:
        """Process scanner result and return status summary line."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        execution_status = rule.scanner_execution_status or 'SUCCESS'
        
        if self._has_scanner_error(execution_status, scanner_results):
            error_msg = self._extract_error_message(execution_status, scanner_results)
            logger.info(f"[{timestamp}] Completed scanner: {scanner_name} (rule: {rule.rule_file}) - FAILED: {error_msg}")
            self._flush_logger_handlers(logger)
            rule_result['scanner_status'] = {'status': 'EXECUTION_FAILED', 'scanner_path': scanner_path, 'error': error_msg}
            return f"  [ERROR] {rule.rule_file}: {error_msg}"
        
        violations_count = len(rule.violations)
        logger.info(f"[{timestamp}] Completed scanner: {scanner_name} (rule: {rule.rule_file}) - SUCCESS ({violations_count} violations)")
        self._flush_logger_handlers(logger)
        rule_result['scanner_status'] = {'status': 'EXECUTED', 'scanner_path': scanner_path, 'execution_status': execution_status, 'violations_found': violations_count}
        self.add_violations(rule.violations)
        return f"  [OK] {rule.rule_file}: Scanner executed successfully ({violations_count} violations)"
    
    def _execute_scanner(self, rule, rule_result: dict, knowledge_graph: Dict, files: Dict, scanner_path: str, on_scanner_start, on_file_scanned, logger) -> str:
        """Execute a scanner and return status summary line."""
        scanner_name = scanner_path.split('.')[-1] if '.' in scanner_path else scanner_path
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logger.info(f"[{timestamp}] Starting scanner: {scanner_name} (rule: {rule.rule_file})")
        self._flush_logger_handlers(logger)
        
        if on_scanner_start:
            on_scanner_start(rule.rule_file, scanner_path)
        
        try:
            scanner_results = rule.scan(knowledge_graph, files, on_file_scanned=on_file_scanned)
            rule_result['scanner_results'] = scanner_results
            return self._process_scanner_result(rule, rule_result, scanner_results, scanner_path, scanner_name, logger)
        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            error_msg = f"Scanner execution failed: {str(e)}"
            logger.error(f"[{timestamp}] Completed scanner: {scanner_name} (rule: {rule.rule_file}) - EXCEPTION: {error_msg}")
            self._flush_logger_handlers(logger)
            logger.error(f"Scanner execution failed for rule {rule.rule_file}: {e}", exc_info=True)
            rule_result['scanner_status'] = {'status': 'EXECUTION_FAILED', 'scanner_path': scanner_path, 'error': error_msg}
            raise
    
    def _process_rule(self, rule, rule_result: dict, knowledge_graph: Dict, files: Dict, on_scanner_start, on_file_scanned, logger) -> str:
        """Process a single rule and return status summary line."""
        scanner_path = rule.scanner_path
        
        if not scanner_path:
            rule_result['scanner_status'] = {'status': 'NO_SCANNER', 'scanner_path': None}
            return f"  [SKIP] {rule.rule_file}: No scanner defined"
        
        if not rule.has_scanner:
            load_error = rule.scanner_load_error or "Unknown error - scanner class is None"
            rule_result['scanner_status'] = {'status': 'LOAD_FAILED', 'scanner_path': scanner_path, 'error': load_error}
            logger.error(f"Scanner failed to load for rule {rule.rule_file}: {load_error}")
            return f"  [FAILED] {rule.rule_file}: Scanner failed to load - {load_error}"
        
        return self._execute_scanner(rule, rule_result, knowledge_graph, files, scanner_path, on_scanner_start, on_file_scanned, logger)
    
    def validate(self, knowledge_graph: Dict[str, Any], files: Optional[Dict[str, List[Path]]] = None, 
                 callbacks: Optional[ValidationCallbacks] = None,
                 skiprule: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        """Validate knowledge graph and files against all rules.
        
        Args:
            knowledge_graph: The story graph data to validate against
            files: Dict with 'test_files' and 'code_files' lists of Paths
            callbacks: ValidationCallbacks with on_scanner_start, on_scanner_complete, on_file_scanned
            skiprule: List of rule names to skip
        """
        logger = logging.getLogger(__name__)
        logger.info("=== Starting rules validation ===")
        logger.info(f"Files to validate: {sum(len(f) for f in (files or {}).values())} files")
        
        callbacks = callbacks or ValidationCallbacks()
        files = files or {}
        processed_rules = []
        rules_list = list(self)
        logger.info(f"Loaded {len(rules_list)} rules")
        
        scanner_status_summary = []
        skiprule_set = set(skiprule) if skiprule else set()
        if skiprule_set:
            logger.info(f"Skipping rules: {skiprule_set}")
        
        for idx, rule in enumerate(rules_list, 1):
            rule_name = Path(rule.rule_file).stem
            if rule_name in skiprule_set:
                logger.info(f"Skipping rule {idx}/{len(rules_list)}: {rule.rule_file} (--skiprule)")
                scanner_status_summary.append(f"  [SKIP] {rule.rule_file}: Skipped by --skiprule")
                continue
            
            logger.info(f"Processing rule {idx}/{len(rules_list)}: {rule.rule_file}")
            rule_result = {'rule_file': rule.rule_file, 'rule_content': rule.rule_content, 'scanner_status': {}}
            
            try:
                status_line = self._process_rule(rule, rule_result, knowledge_graph, files, callbacks, logger)
                scanner_status_summary.append(status_line)
            except Exception:
                scanner_status_summary.append(f"  [ERROR] {rule.rule_file}: Scanner execution failed")
                raise
            
            processed_rules.append(rule_result)
            if callbacks.on_scanner_complete:
                callbacks.on_scanner_complete(rule_result)
        
        if scanner_status_summary:
            logger.info("=== SCANNER EXECUTION STATUS ===")
            for status_line in scanner_status_summary:
                logger.info(status_line)
            logger.info("=== END SCANNER STATUS ===")
        
        return processed_rules
