"""
Guardrails Test Helper
Handles all guardrails (clarify + strategy) - key questions, evidence, assumptions, criteria
"""
import json
from pathlib import Path
from .base_helper import BaseHelper


class GuardrailsTestHelper(BaseHelper):
    """Helper for creating and managing guardrails test data"""
    
    def create_minimal_guardrails_files(self, behavior_name: str):
        """Ensure guardrails directory structure exists for tests.
        
        This helper ensures directories exist for Guardrails class initialization.
        Tests always use production files from story_bot - no files are created.
        
        Args:
            behavior_name: Behavior name (e.g., 'exploration')
        """
        # Create behavior folder structure (directories only)
        behavior_dir = self.parent.bot_directory / 'behaviors' / behavior_name
        behavior_dir.mkdir(parents=True, exist_ok=True)
        
        # Ensure guardrails directory structure exists
        required_context_dir = behavior_dir / 'guardrails' / 'required_context'
        strategy_dir = behavior_dir / 'guardrails' / 'strategy'
        decision_criteria_dir = strategy_dir / 'decision_criteria'
        
        required_context_dir.mkdir(parents=True, exist_ok=True)
        strategy_dir.mkdir(parents=True, exist_ok=True)
        decision_criteria_dir.mkdir(parents=True, exist_ok=True)
        
        # Note: Files (key_questions.json, evidence.json, etc.) are always read from production story_bot
        # Tests never create these files - they use the existing production files
    
    def create_guardrails_files(self, behavior_name: str, questions: list = None, evidence: list = None):
        """Create guardrails files with content for a behavior.
        
        Args:
            behavior_name: Name of the behavior
            questions: Optional list of questions for key_questions.json
            evidence: Optional list of evidence items for evidence.json
        
        Returns:
            Tuple of (questions_file, evidence_file) paths, or None if no files created
        """
        guardrails_dir = self.parent.bot_directory / 'behaviors' / behavior_name / 'guardrails' / 'required_context'
        guardrails_dir.mkdir(parents=True, exist_ok=True)
        
        questions_file = None
        evidence_file = None
        
        if questions is not None:
            questions_file = guardrails_dir / 'key_questions.json'
            questions_file.write_text(json.dumps({'questions': questions}), encoding='utf-8')
        
        if evidence is not None:
            evidence_file = guardrails_dir / 'evidence.json'
            evidence_file.write_text(json.dumps({'evidence': evidence}), encoding='utf-8')
        
        if questions_file or evidence_file:
            return questions_file, evidence_file
        return None
    
    def create_malformed_guardrails_file(self, behavior_name: str) -> Path:
        """Create a malformed guardrails JSON file for testing error handling.
        
        Args:
            behavior_name: Name of the behavior
        
        Returns:
            Path to the created malformed questions file
        """
        guardrails_dir = self.parent.bot_directory / 'behaviors' / behavior_name / 'guardrails' / 'required_context'
        guardrails_dir.mkdir(parents=True, exist_ok=True)
        questions_file = guardrails_dir / 'key_questions.json'
        questions_file.write_text('invalid json {', encoding='utf-8')
        return questions_file
    
    def create_strategy_guardrails(self, behavior_name: str, assumptions: list, criteria: dict) -> tuple:
        """Create strategy guardrails in behavior folder.
        
        Args:
            behavior_name: Name of the behavior
            assumptions: List of assumptions
            criteria: Dict of criteria
        
        Returns:
            Tuple of (assumptions_file, criteria_file) paths
        """
        guardrails_dir = self.parent.bot_directory / 'behaviors' / behavior_name / 'guardrails' / 'strategy'
        guardrails_dir.mkdir(parents=True, exist_ok=True)
        
        assumptions_file = guardrails_dir / 'typical_assumptions.json'
        assumptions_file.write_text(json.dumps({'assumptions': assumptions}), encoding='utf-8')
        
        criteria_dir = guardrails_dir / 'strategy_criteria'
        criteria_dir.mkdir(exist_ok=True)
        criteria_file = criteria_dir / 'test_criteria.json'
        criteria_file.write_text(json.dumps(criteria), encoding='utf-8')
        
        return assumptions_file, criteria_file
