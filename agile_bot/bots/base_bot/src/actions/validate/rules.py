from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Iterator, Dict, Any, TYPE_CHECKING, Callable
from pathlib import Path
import fnmatch
from agile_bot.bots.base_bot.src.actions.validate.rule import Rule

if TYPE_CHECKING:
    pass


@dataclass
class ValidationCallbacks:
    """Callbacks for validation progress - groups on_scanner_start, on_scanner_complete, on_file_scanned."""
    on_scanner_start: Optional[Callable] = None
    on_scanner_complete: Optional[Callable] = None
    on_file_scanned: Optional[Callable] = None


@dataclass
class ValidationContext:
    """Represents the context for validating content against rules."""
    knowledge_graph: Dict[str, Any]
    files: Dict[str, List[Path]]
    callbacks: ValidationCallbacks
    skiprule: List[str]
    exclude: List[str]
    behavior: Any  # 'Behavior' - avoiding circular import
    bot_paths: Any  # 'BotPaths' - avoiding circular import
    working_dir: Path
    
    @classmethod
    def from_parameters(cls, behavior, parameters: Dict[str, Any],
                       callbacks: Optional[ValidationCallbacks] = None) -> 'ValidationContext':
        """Create ValidationContext from behavior and parameters.
        
        Builds knowledge graph, validation scope, and discovers files internally.
        """
        # Load knowledge graph
        from agile_bot.bots.base_bot.src.actions.build.knowledge import Knowledge
        knowledge = Knowledge(behavior)
        
        # Create story graph
        from agile_bot.bots.base_bot.src.actions.validate.story_graph import StoryGraph
        story_graph = StoryGraph(
            behavior.bot_paths,
            behavior.bot_paths.workspace_directory,
            knowledge_graph_spec=knowledge.knowledge_graph_spec
        )
        
        # Build validation scope
        from agile_bot.bots.base_bot.src.actions.validate.validation_scope import ValidationScope
        validation_scope = ValidationScope(
            parameters or {},
            behavior.bot_paths,
            behavior_name=behavior.name
        )
        
        # Apply validation scope to story graph if needed
        scope_config = validation_scope.scope
        scope_keys = {'story_names', 'increment_priorities', 'epic_names', 'all'}
        has_scope_in_params = any(key in scope_config for key in scope_keys)
        if has_scope_in_params:
            story_graph['_validation_scope'] = scope_config
        
        # Discover files to validate
        files = validation_scope.all_files()
        
        return cls(
            knowledge_graph=story_graph.content,
            files=files,
            callbacks=callbacks or ValidationCallbacks(),
            skiprule=parameters.get('skiprule', []),
            exclude=parameters.get('exclude', []),
            behavior=behavior,
            bot_paths=behavior.bot_paths,
            working_dir=behavior.bot_paths.workspace_directory
        )
    
    def should_skip_rule(self, rule_name: str) -> bool:
        """Check if a rule should be skipped."""
        return rule_name in self.skiprule
    
    def get_filtered_files(self, rules_instance: 'Rules') -> Dict[str, List[Path]]:
        """Get files after applying exclude patterns."""
        if not self.exclude:
            return self.files
        return rules_instance._filter_files(self.files, self.exclude)


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
    
    def _is_in_disabled_folder(self, file_path: Path) -> bool:
        """Check if a file path contains 'disabled' in any part of its path."""
        parts = file_path.parts
        return 'disabled' in parts
    
    def _load_bot_rules(self) -> List[Rule]:
        bot_rules = []
        bot_dir = self.bot_paths.bot_directory
        bot_rules_dir = bot_dir / 'rules'
        
        # Load direct rule files in rules/ folder
        for rule_file in bot_rules_dir.glob('*.json'):
            if not self._is_in_disabled_folder(rule_file):
                rule_obj = Rule(
                    rule_file_path=rule_file,
                    behavior_name='common',
                    bot_name=self.bot_name
                )
                bot_rules.append(rule_obj)
        
        # Load rules from specializations/ subfolder (recursively), skipping disabled
        specializations_dir = bot_rules_dir / 'specializations'
        if specializations_dir.exists() and specializations_dir.is_dir():
            for rule_file in specializations_dir.rglob('*.json'):
                if not self._is_in_disabled_folder(rule_file):
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
        """Load rules from a subdirectory, skipping already loaded rules and disabled folders."""
        rules = []
        for rule_file in subdir.rglob('*.json'):
            # Skip if in disabled folder
            if self._is_in_disabled_folder(rule_file):
                continue
            # Skip if already loaded from behavior_rules_dir
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
        
        # Load direct rule files, skipping disabled folders
        behavior_rules = []
        for rule_file in behavior_rules_dir.glob('*.json'):
            if not self._is_in_disabled_folder(rule_file):
                behavior_rules.append(self._create_rule(rule_file))
        
        # Load from subdirectories, skipping disabled folders
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
    
    def _is_file_in_folder(self, file_path: Path, folder_pattern: str) -> bool:
        """Check if a file is in a folder, handling both absolute and relative paths.
        
        Args:
            file_path: Path to the file (may be absolute or relative)
            folder_pattern: Folder path pattern (may be absolute or relative)
        
        Returns:
            True if file is in the folder, False otherwise
        """
        try:
            folder_path = Path(folder_pattern)
            
            # Try is_relative_to first (works for absolute paths)
            if folder_path.is_absolute() or file_path.is_absolute():
                try:
                    if file_path.is_relative_to(folder_path):
                        return True
                except ValueError:
                    pass
            
            # Fallback: normalize both paths and check if folder is a prefix
            # Convert to string and normalize separators
            file_str = str(file_path).replace('\\', '/')
            folder_str = str(folder_path).replace('\\', '/')
            
            # Check if folder path is a prefix of file path
            if file_str.startswith(folder_str):
                # Make sure it's actually a folder match (not just a prefix match)
                # Check if next character is a path separator or end of string
                remaining = file_str[len(folder_str):]
                if not remaining or remaining.startswith('/'):
                    return True
            
            return False
        except Exception:
            return False
    
    def _filter_files(self, files: Dict[str, List[Path]], exclude_patterns: Optional[List[str]] = None) -> Dict[str, List[Path]]:
        """Filter files based on exclude patterns.
        
        Args:
            files: Dict with 'test' and 'src' lists of Paths
            exclude_patterns: List of exclude patterns. Each pattern can be:
                - Folder path: "agile_bot/bots/base_bot/src" - excludes all files in this folder
                - File pattern: "*scanner*" - excludes files matching this pattern
                - Folder with include pattern: "agile_bot/bots/base_bot/src:*scanner*" 
                  - excludes folder but includes files matching the pattern (after colon)
        
        Returns:
            Filtered files dict with same structure
        """
        if not exclude_patterns:
            return files
        
        logger = logging.getLogger(__name__)
        filtered_files = {
            'test': [],
            'src': []
        }
        
        all_files = []
        if 'test' in files:
            all_files.extend([('test', f) for f in files['test']])
        if 'src' in files:
            all_files.extend([('src', f) for f in files['src']])
        
        excluded_count = 0
        for file_type, file_path in all_files:
            should_exclude = False
            
            for pattern in exclude_patterns:
                # Check for folder:pattern format (exclude folder but include matching files)
                if ':' in pattern:
                    folder_pattern, include_pattern = pattern.split(':', 1)
                    
                    # Check if file is in the folder
                    if self._is_file_in_folder(file_path, folder_pattern):
                        # File is in excluded folder, check if it matches include pattern
                        if not fnmatch.fnmatch(file_path.name, include_pattern):
                            # File is in excluded folder and doesn't match include pattern
                            should_exclude = True
                            break
                else:
                    # Normalize path separators for comparison
                    file_path_str = str(file_path).replace('\\', '/')
                    pattern_normalized = pattern.replace('\\', '/')
                    
                    # First try folder path check - try to resolve relative to workspace
                    folder_path = Path(pattern)
                    folder_match = False
                    
                    # Try to resolve relative path to workspace if we have bot_paths
                    if not folder_path.is_absolute() and hasattr(self, 'bot_paths') and self.bot_paths:
                        workspace_dir = self.bot_paths.workspace_directory
                        if workspace_dir:
                            resolved_folder = workspace_dir / folder_path
                            if resolved_folder.exists() and resolved_folder.is_dir():
                                folder_path = resolved_folder
                    
                    if folder_path.exists() and folder_path.is_dir():
                        # Pattern is a folder - check if file is in this folder
                        folder_match = self._is_file_in_folder(file_path, str(folder_path))
                    
                    # Also check substring match (works for both folder paths and patterns)
                    substring_match = pattern_normalized in file_path_str
                    
                    # Check file pattern matching (fnmatch with wildcards)
                    fnmatch_match = (fnmatch.fnmatch(file_path_str, pattern) or 
                                   fnmatch.fnmatch(file_path.name, pattern))
                    
                    # Exclude if any match succeeds
                    if folder_match or substring_match or fnmatch_match:
                        should_exclude = True
                        break
            
            if not should_exclude:
                filtered_files[file_type].append(file_path)
            else:
                excluded_count += 1
        
        if excluded_count > 0:
            logger.info(f"Excluded {excluded_count} files based on exclude patterns: {exclude_patterns}")
        
        return filtered_files
    
    def validate(self, validation_context_or_knowledge_graph, files: Optional[Dict[str, List[Path]]] = None, 
                 callbacks: Optional[ValidationCallbacks] = None,
                 skiprule: Optional[List[str]] = None,
                 exclude: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        """Validate knowledge graph and files against all rules.
        
        Args:
            validation_context_or_knowledge_graph: Either ValidationContext object or knowledge_graph Dict
            files: Dict with 'test' and 'src' lists of Paths (ignored if ValidationContext provided)
            callbacks: ValidationCallbacks (ignored if ValidationContext provided)
            skiprule: List of rule names to skip (ignored if ValidationContext provided)
            exclude: List of exclude patterns (ignored if ValidationContext provided)
        """
        # Support both ValidationContext and legacy parameters
        if isinstance(validation_context_or_knowledge_graph, ValidationContext):
            context = validation_context_or_knowledge_graph
        else:
            # Legacy mode - create context from individual parameters
            knowledge_graph = validation_context_or_knowledge_graph
            callbacks = callbacks or ValidationCallbacks()
            files = files or {}
            # Create minimal context for backward compatibility
            context = ValidationContext(
                knowledge_graph=knowledge_graph,
                files=files,
                callbacks=callbacks,
                skiprule=skiprule or [],
                exclude=exclude or [],
                behavior=self.behavior,
                bot_paths=self.bot_paths if hasattr(self, 'bot_paths') else None,
                working_dir=Path.cwd()
            )
        
        return self._execute_validation(context)
    
    def _execute_validation(self, context: ValidationContext) -> List[Dict[str, Any]]:
        """Execute validation with context object."""
        logger = logging.getLogger(__name__)
        logger.info("=== Starting rules validation ===")
        
        files = context.get_filtered_files(self)
        logger.info(f"Files to validate: {sum(len(f) for f in files.values())} files")
        
        processed_rules = []
        rules_list = list(self)
        logger.info(f"Loaded {len(rules_list)} rules")
        
        scanner_status_summary = []
        skiprule_set = set(context.skiprule)
        if skiprule_set:
            logger.info(f"Skipping rules: {skiprule_set}")
        
        for idx, rule in enumerate(rules_list, 1):
            rule_name = Path(rule.rule_file).stem
            if context.should_skip_rule(rule_name):
                logger.info(f"Skipping rule {idx}/{len(rules_list)}: {rule.rule_file} (--skiprule)")
                scanner_status_summary.append(f"  [SKIP] {rule.rule_file}: Skipped by --skiprule")
                continue
            
            logger.info(f"Processing rule {idx}/{len(rules_list)}: {rule.rule_file}")
            rule_result = {'rule_file': rule.rule_file, 'rule_content': rule.rule_content, 'scanner_status': {}}
            
            try:
                on_scanner_start = context.callbacks.on_scanner_start if context.callbacks else None
                on_file_scanned = context.callbacks.on_file_scanned if context.callbacks else None
                status_line = self._process_rule(rule, rule_result, context.knowledge_graph, files, on_scanner_start, on_file_scanned, logger)
                scanner_status_summary.append(status_line)
            except Exception:
                scanner_status_summary.append(f"  [ERROR] {rule.rule_file}: Scanner execution failed")
                raise
            
            processed_rules.append(rule_result)
            if context.callbacks.on_scanner_complete:
                context.callbacks.on_scanner_complete(rule_result)
        
        if scanner_status_summary:
            logger.info("=== SCANNER EXECUTION STATUS ===")
            for status_line in scanner_status_summary:
                logger.info(status_line)
            logger.info("=== END SCANNER STATUS ===")
        
        return processed_rules
