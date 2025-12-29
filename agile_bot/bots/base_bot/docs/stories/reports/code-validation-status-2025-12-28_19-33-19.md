# Validation Status - code
Started: 2025-12-28 19:33:19
Files: 269


## Cross-File Duplication Analysis
Scanning 1 changed file(s) against 269 total files...
Extracted 115 changed blocks, 4088 reference blocks
Starting 470,120 pairwise comparisons...
Comparing: 4% (22,308/470,120) - 0 violations - ETA: 200s  
Comparing: 8% (41,126/470,120) - 0 violations - ETA: 208s  
Comparing: 12% (59,322/470,120) - 0 violations - ETA: 207s  
Comparing: 17% (79,921/470,120) - 0 violations - ETA: 187s  
Comparing: 21% (103,131/470,120) - 0 violations - ETA: 172s  
Comparing: 26% (122,232/470,120) - 0 violations - ETA: 162s  
Comparing: 30% (142,748/470,120) - 0 violations - ETA: 154s  
Comparing: 34% (161,521/470,120) - 0 violations - ETA: 147s  
Comparing: 38% (178,797/470,120) - 0 violations - ETA: 142s  
Comparing: 41% (195,384/470,120) - 0 violations - ETA: 136s  
Comparing: 44% (210,375/470,120) - 0 violations - ETA: 132s  
Comparing: 47% (224,641/470,120) - 0 violations - ETA: 128s  
Comparing: 50% (238,264/470,120) - 0 violations - ETA: 123s  
Comparing: 53% (250,671/470,120) - 0 violations - ETA: 120s  
Comparing: 55% (262,004/470,120) - 0 violations - ETA: 116s  
Comparing: 60% (282,072/470,120) - 0 violations - ETA: 102s  
Comparing: 65% (305,578/470,120) - 0 violations - ETA: 87s  
Comparing: 68% (322,714/470,120) - 0 violations - ETA: 78s  
Comparing: 71% (337,897/470,120) - 0 violations - ETA: 71s  
Comparing: 74% (350,446/470,120) - 0 violations - ETA: 65s  
Comparing: 76% (360,885/470,120) - 0 violations - ETA: 61s  
Comparing: 78% (370,881/470,120) - 0 violations - ETA: 56s  
Comparing: 81% (382,119/470,120) - 0 violations - ETA: 51s  
Comparing: 85% (400,632/470,120) - 0 violations - ETA: 40s  
Comparing: 89% (421,976/470,120) - 0 violations - ETA: 27s  
Comparing: 93% (439,588/470,120) - 0 violations - ETA: 17s  
Complete: 456895 comparisons, 0 violations

## keep_functions_small_focused
**rules.py** - 2 violation(s)

[!] WARNING (line 105)
Function "get_last_report_timestamp" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return rules_instance._rule_filter.filter_files(self.files, self.exclude)

    def get_last_report_timestamp(self) -> float:
        logger = logging.getLogger(__name__)
        docs_path = self.bot_paths.documentation_path
        reports_dir = self.bot_paths.workspace_directory / docs_path / 'reports'
        logger.info(f'Looking for previous reports in: {reports_dir}')
        if not reports_dir.exists():
            logger.info('Reports directory does not exist - returning 0.0')
            return 0.0
        
        report_files = list(reports_dir.glob(f'{self.behavior.name}-validation-status-*.md'))
        logger.info(f'Found {len(report_files)} report files')
        if not report_files:
            logger.info('No report files found - returning 0.0')
            return 0.0
        
        current_time = time.time()
        previous_run_files = [f for f in report_files if (current_time - f.stat().st_mtime) > 10]
        logger.info(f'Found {len(previous_run_files)} previous run files (excluding files < 10 seconds old)')
        
        if not previous_run_files:
            logger.info('No previous run files found - returning 0.0')
            return 0.0
        
        most_recent = max(previous_run_files, key=lambda p: p.stat().st_mtime)
        logger.info(f'Most recent previous report: {most_recent.name} (timestamp: {most_recent.stat().st_mtime})')
        return most_recent.stat().st_mtime

```

[!] WARNING (line 225)
Function "formatted_rules_digest" is 24 lines - should be under 20 lines (extract complex logic to helper functions)

```python
        return '\n'.join(sections) if sections else 'No validation rules found.'

    def formatted_rules_digest(self) -> str:
        rules = self._load_rules()
        if not rules:
            return 'No validation rules found.'
        
        # Sort by priority (lower number = higher priority)
        rules = sorted(rules, key=lambda r: r.priority)
        
        lines = []
        for i, rule in enumerate(rules):
            description = rule.description or 'No description'
            lines.append(f"- **{rule.name}**: {description}")
            
            # Add DO description if present
            do_section = rule.rule_content.get('do', {})
            do_desc = do_section.get('description', '')
            if do_desc:
                lines.append(f"  DO: {do_desc}")
            
            # Add DON'T description if present
            dont_section = rule.rule_content.get('dont', {})
            dont_desc = dont_section.get('description', '')
            if dont_desc:
                lines.append(f"  DON'T: {dont_desc}")
            
            # Add blank line between rules, but not after the last rule
            if i < len(rules) - 1:
                lines.append("")
        
        return '\n'.join(lines)

```

---

## use_clear_function_parameters
**rules.py** - 5 violation(s)

[!] WARNING (line 292)
Function "_process_scanner_result" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
            return data

    def _process_scanner_result(self, rule, rule_result: dict, scanner_results: Any, scanner_path: str, scanner_name: str, logger) -> str:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        execution_status = rule.scanner_execution_status or 'SUCCESS'
    # ... (truncated)
```

[!] WARNING (line 308)
Function "_execute_scanner" has 9 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return f'  [OK] {rule.rule_file}: Scanner executed successfully ({violations_count} violations)'

    def _execute_scanner(self, rule, rule_result: dict, context: ValidationContext, scanner_path: str, logger, files: Dict, changed_files: Dict, all_files: Dict) -> str:
        scanner_name = scanner_path.split('.')[-1] if '.' in scanner_path else scanner_path
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # ... (truncated)
```

[!] WARNING (line 328)
Function "_process_rule" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
            raise

    def _process_rule(self, rule, rule_result: dict, context: ValidationContext, logger, files: Dict, changed_files: Dict, all_files: Dict) -> str:
        scanner_path = rule.scanner_path
        if not scanner_path:
    # ... (truncated)
```

[!] WARNING (line 340)
Function "validate" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return self._execute_scanner(rule, rule_result, context, scanner_path, logger, files, changed_files, all_files)

    def validate(self, context: ValidationContext, files: Optional[Dict[str, List[Path]]]=None, callbacks: Optional[ValidationCallbacks]=None, skiprule: Optional[List[str]]=None, exclude: Optional[List[str]]=None) -> List[Dict[str, Any]]:
        if isinstance(context, ValidationContext):
            return self._execute_validation(context)
    # ... (truncated)
```

[!] WARNING (line 345)
Function "_create_legacy_context" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

```python
        return self._execute_validation(self._create_legacy_context(context, files, callbacks, skiprule, exclude))

    def _create_legacy_context(self, knowledge_graph: Dict, files: Optional[Dict], callbacks: Optional[ValidationCallbacks], skiprule: Optional[List[str]], exclude: Optional[List[str]]) -> ValidationContext:
        return ValidationContext(knowledge_graph=knowledge_graph, files=files or {}, callbacks=callbacks or ValidationCallbacks(), skiprule=skiprule or [], exclude=exclude or [], skip_cross_file=True, all_files=False, behavior=self.behavior, bot_paths=getattr(self, 'bot_paths', None), working_dir=Path.cwd())

```

---

Completed: 2025-12-28 19:37:44
Total violations: 7
Scanners executed: 30
