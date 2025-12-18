"""ValidateCodeFilesAction - validates source code files against rules.

This action extends ValidateRulesAction to handle code file validation.
It ensures that code files from the 'src' parameter are properly discovered
and passed to CodeScanner instances for validation.
"""

from typing import Dict, Any
from pathlib import Path
from agile_bot.bots.base_bot.src.actions.validate.validate_action import ValidateRulesAction


class ValidateCodeFilesAction(ValidateRulesAction):
    """Action for validating source code files against rules.
    
    This is a specialized version of ValidateRulesAction that ensures
    code files are properly handled. The ValidateRulesAction already
    handles the 'src' parameter through ValidationScope, so this class
    primarily exists to match the expected class name in behavior.json.
    """
    
    @property
    def action_name(self) -> str:
        """Action name is always 'validate' for ValidateCodeFilesAction."""
        return 'validate'
    
    @action_name.setter
    def action_name(self, value: str):
        raise AttributeError("action_name is read-only for ValidateCodeFilesAction")

