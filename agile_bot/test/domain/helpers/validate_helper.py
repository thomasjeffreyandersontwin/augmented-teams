"""
Validate Test Helper
Handles validate action, scanners, rules, violations + validate-specific instruction assertions
"""
import json
from pathlib import Path
from .base_helper import BaseHelper


class ValidateTestHelper(BaseHelper):
    """Helper for validate action, scanners, and rules testing"""
    
    def create_validation_rules(self, behavior: str, rules: list) -> Path:
        """Create validation rules in behavior folder.
        
        Args:
            behavior: Behavior name
            rules: List of rules
        
        Returns:
            Path to validation_rules.json file
        """
        rules_dir = self.parent.bot_directory / 'behaviors' / behavior / '3_rules'
        rules_dir.mkdir(parents=True, exist_ok=True)
        
        rules_file = rules_dir / 'validation_rules.json'
        rules_file.write_text(json.dumps({'rules': rules}), encoding='utf-8')
        return rules_file
    
    def assert_validate_instructions(self, instructions):
        """Assert ValidateRulesAction injected all required fields.
        
        Args:
            instructions: Instructions object from ValidateRulesAction
        """
        # Check base instructions exist
        base_instructions = instructions.get('base_instructions', [])
        assert base_instructions, "base_instructions should be present"
        
        # Check ValidateRulesAction-specific fields
        # Placeholders should be replaced in base_instructions
        base_text = ' '.join(base_instructions)
        
        # Validate that placeholders were replaced (should not contain {{}} anymore)
        assert '{{rules}}' not in base_text, "{{rules}} placeholder should be replaced"
        assert '{{scanner_output}}' not in base_text, "{{scanner_output}} placeholder should be replaced"
        assert '{{schema}}' not in base_text, "{{schema}} placeholder should be replaced"
        assert '{{description}}' not in base_text, "{{description}} placeholder should be replaced"
        
        # Check that rules field exists (may be empty list if no rules)
        assert instructions.get('rules') is not None, "rules should be set"
    
    def then_scanners_match(self, behavior, count=None, structure_valid=None):
        """Assert scanners match expected values.
        
        Args:
            behavior: Behavior instance to check scanners from
            count: Expected number of scanner classes (optional)
            structure_valid: Whether to validate scanner structure (default: True if count is provided)
        """
        rules = behavior.rules
        scanners = [rule.scanner_class for rule in rules if rule.scanner_class]
        
        if count is not None:
            assert len(scanners) == count, (
                f"Expected {count} scanner classes discovered, got {len(scanners)}"
            )
            assert len(rules) >= count, (
                f"Expected at least {count} rules, got {len(rules)}"
            )
        
        if structure_valid is None:
            structure_valid = count is not None
        
        if structure_valid:
            for scanner_class in scanners:
                assert isinstance(scanner_class, type), (
                    f"Discovered scanner must be a class, got: {type(scanner_class)}"
                )
            for rule in rules:
                assert rule.has_scanner, f"Rule {rule.name} should have a scanner attached"
                scanner = rule.scanner
                assert scanner is not None, f"Rule {rule.name} should have a scanner instance"
    
    def when_scanner_scans(self, scanner_instance, bad_example, rule_obj, scanner_type='auto'):
        """Scanner scans files/knowledge graph.
        
        Args:
            scanner_instance: Scanner instance (may be unused if scanner_type='auto' and using rule.scan())
            bad_example: Dict containing test_files, code_files, and/or knowledge_graph
            rule_obj: Rule object to scan with
            scanner_type: Type of scanner ('auto', 'test', 'code', 'story'). 'auto' uses rule.scan() (preferred)
        """
        if scanner_type == 'auto':
            kg = {}
            test_files = []
            code_files = []
            
            if bad_example:
                kg = {k: v for k, v in bad_example.items() if k not in ['test_files', 'code_files']}
                
                if 'test_files' in bad_example:
                    test_files = [Path(tf) for tf in bad_example['test_files']]
                
                if 'code_files' in bad_example:
                    code_files = [Path(cf) for cf in bad_example['code_files']]
            
            files_dict = {}
            if test_files:
                files_dict['test'] = test_files
            if code_files:
                files_dict['src'] = code_files
            
            scanner_results = rule_obj.scan(kg, files=files_dict if files_dict else None)
            
            violations = []
            if 'violations' in scanner_results:
                violations = scanner_results['violations']
            elif 'file_by_file' in scanner_results:
                violations.extend(scanner_results['file_by_file'].get('violations', []))
            if 'cross_file' in scanner_results:
                violations.extend(scanner_results['cross_file'].get('violations', []))
            
            return violations
        
        elif scanner_type == 'test':
            violations = []
            test_files_to_scan = []
            if bad_example and 'test_files' in bad_example:
                test_files_to_scan = [Path(tf) for tf in bad_example['test_files']]
            
            kg = {}
            if bad_example:
                kg = {k: v for k, v in bad_example.items() if k not in ['test_files', 'code_files']}
            
            for test_file_path in test_files_to_scan:
                file_violations = scanner_instance.scan_test_file(test_file_path, rule_obj, kg)
                violations.extend(file_violations)
            
            return violations
        
        elif scanner_type == 'code':
            violations = []
            if bad_example and 'code_files' in bad_example:
                for code_file_path in bad_example['code_files']:
                    file_path = Path(code_file_path)
                    file_violations = scanner_instance.scan_code_file(file_path, rule_obj)
                    violations.extend(file_violations)
            return violations
        
        elif scanner_type == 'story':
            kg = bad_example if bad_example else {}
            return scanner_instance.scan(kg, rule_obj)
        
        else:
            raise ValueError(f"Unknown scanner_type: {scanner_type}. Must be 'auto', 'test', 'code', or 'story'")
