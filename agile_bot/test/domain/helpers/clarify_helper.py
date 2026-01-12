"""
Clarify Test Helper
Handles clarify action-specific methods and instruction assertions
"""
from .base_helper import BaseHelper


class ClarifyTestHelper(BaseHelper):
    """Helper for clarify action-specific testing"""
    
    def assert_clarify_context_instructions(self, instructions):
        """Assert ClarifyContextAction injected all required fields.
        
        Args:
            instructions: Instructions object from ClarifyContextAction
        """
        # Check base instructions exist
        base_instructions = instructions.get('base_instructions', [])
        assert base_instructions, "base_instructions should be present"
        
        # Check ClarifyContextAction-specific fields
        guardrails = instructions.get('guardrails')
        assert guardrails is not None, "guardrails should be set"
        assert 'required_context' in guardrails, "guardrails should contain required_context"
        
        required_context = guardrails['required_context']
        assert 'key_questions' in required_context, "required_context should have key_questions"
        assert 'evidence' in required_context, "required_context should have evidence"
