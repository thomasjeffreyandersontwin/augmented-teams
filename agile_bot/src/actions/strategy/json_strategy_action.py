"""
JSON adapter for StrategyAction.
"""

import json
from agile_bot.src.cli.adapters import JSONAdapter
from agile_bot.src.actions.strategy.strategy_action import StrategyAction


class JSONStrategyAction(JSONAdapter):
    """Serializes StrategyAction to JSON - exposes all StrategyAction properties."""
    
    def __init__(self, action: StrategyAction, is_current: bool = False, is_completed: bool = False):
        self.action = action
        self.is_current = is_current
        self.is_completed = is_completed
    
    # Expose ALL domain properties
    @property
    def action_name(self):
        return self.action.action_name
    
    @property
    def description(self):
        return self.action.description
    
    @property
    def order(self):
        return self.action.order
    
    @property
    def next_action(self):
        return self.action.next_action
    
    @property
    def workflow(self):
        return self.action.workflow
    
    @property
    def auto_confirm(self):
        return self.action.auto_confirm
    
    @property
    def skip_confirm(self):
        return self.action.skip_confirm
    
    @property
    def behavior(self):
        return self.action.behavior
    
    @property
    def strategy(self):
        """Strategy-specific property."""
        return self.action.strategy
    
    @property
    def strategy_criteria(self):
        """Strategy-specific property."""
        return self.action.strategy_criteria
    
    @property
    def typical_assumptions(self):
        """Strategy-specific property."""
        return self.action.typical_assumptions
    
    def to_dict(self) -> dict:
        """Convert StrategyAction to dict."""
        result = {
            'action_name': self.action.action_name,
            'description': self.action.description,
            'order': self.action.order,
            'next_action': self.action.next_action,
            'workflow': self.action.workflow,
            'auto_confirm': self.action.auto_confirm,
            'skip_confirm': self.action.skip_confirm,
            'behavior': self.action.behavior.name if self.action.behavior else None,
        }
        
        # Add strategy-specific properties
        if self.action.strategy:
            result['strategy'] = {
                'criteria_count': len(self.action.strategy_criteria) if self.action.strategy_criteria else 0,
                'assumptions_count': len(self.action.typical_assumptions) if self.action.typical_assumptions else 0
            }
            
            if self.action.strategy_criteria:
                criteria_dict = self.action.strategy_criteria
                if isinstance(criteria_dict, dict):
                    result['strategy_criteria'] = [
                        {
                            'id': key,
                            'question': criteria.question if hasattr(criteria, 'question') else '',
                            'options': getattr(criteria, 'options', []) if hasattr(criteria, 'options') else [],
                            'criteria': getattr(criteria, 'question', '') if hasattr(criteria, 'question') else ''
                        }
                        for key, criteria in criteria_dict.items()
                    ]
                else:
                    result['strategy_criteria'] = [
                        {
                            'id': criteria.get('id', '') if isinstance(criteria, dict) else '',
                            'criteria': criteria.get('criteria', '') if isinstance(criteria, dict) else str(criteria),
                            'options': criteria.get('options', []) if isinstance(criteria, dict) else []
                        }
                        for criteria in criteria_dict
                    ]
            
            if self.action.typical_assumptions:
                result['typical_assumptions'] = self.action.typical_assumptions
        
        return result
    
    def deserialize(self, data: str) -> dict:
        """Parse JSON string to dict."""
        return json.loads(data)
