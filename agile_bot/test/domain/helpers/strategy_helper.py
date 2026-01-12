"""
Strategy Test Helper
Handles strategy action-specific methods and instruction assertions
"""
from .base_helper import BaseHelper


class StrategyTestHelper(BaseHelper):
    """Helper for strategy action-specific testing"""
    
    def assert_strategy_instructions(self, instructions):
        """Assert StrategyAction injected all required fields.
        
        Args:
            instructions: Instructions object from StrategyAction
        """
        # Check base instructions exist
        base_instructions = instructions.get('base_instructions', [])
        assert base_instructions, "base_instructions should be present"
        
        # Check StrategyAction-specific fields
        strategy_criteria = instructions.get('strategy_criteria')
        assert strategy_criteria is not None, "strategy_criteria should be set"
        assert isinstance(strategy_criteria, dict), "strategy_criteria should be a dict"
        
        assumptions = instructions.get('assumptions')
        assert assumptions is not None, "assumptions should be set"
        assert isinstance(assumptions, list), "assumptions should be a list"
