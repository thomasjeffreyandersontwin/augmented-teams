"""Scanner for validating ubiquitous language consistency."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import logging
from .test_scanner import TestScanner
from .violation import Violation

logger = logging.getLogger(__name__)


class UbiquitousLanguageScanner(TestScanner):
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
        
        content, lines, tree = parsed
        
        domain_terms = self._extract_domain_terms(knowledge_graph)
        
        violations.extend(self._check_ubiquitous_language(content, domain_terms, file_path, rule_obj))
        
        return violations
    
    def _extract_domain_terms(self, knowledge_graph: Dict[str, Any]) -> List[str]:
        terms = []
        epics = knowledge_graph.get('epics', [])
        for epic in epics:
            epic_name = epic.get('name', '')
            if epic_name:
                terms.extend(epic_name.lower().split())
            
            domain_concepts = epic.get('domain_concepts', [])
            for concept in domain_concepts:
                if isinstance(concept, dict):
                    concept_name = concept.get('name', '')
                    if concept_name:
                        terms.extend(concept_name.lower().split())
        
        return list(set(terms))  # Unique terms
    
    def _check_ubiquitous_language(self, content: str, domain_terms: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        # This is a basic check - could be enhanced to check against domain model
        # For now, just ensure test uses domain terms consistently
        
        content_lower = content.lower()
        
        if domain_terms:
            uses_domain_terms = any(term in content_lower for term in domain_terms)
            
            if not uses_domain_terms and len(content) > 100:
                # Test doesn't use domain terms - might be using technical language
                violation = Violation(
                    rule=rule_obj,
                    violation_message='Test does not use domain terms from knowledge graph - use ubiquitous language consistently',
                    location=str(file_path),
                    severity='warning'
                ).to_dict()
                violations.append(violation)
        
        return violations

