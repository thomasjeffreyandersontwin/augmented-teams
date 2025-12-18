"""Bot reminders module - extracted to eliminate duplication.

This module contains reminder injection logic that was duplicated across:
- behaviors.py: _inject_next_behavior_reminder()
- action.py: _inject_reminders_if_final()
"""
from typing import Dict, Any, List


def inject_reminder_to_instructions(result: Dict[str, Any], reminder: str) -> Dict[str, Any]:
    """Inject a reminder into the result's base_instructions.
    
    Extracted to eliminate duplication between:
    - behaviors.py: _inject_next_behavior_reminder() lines 133-139
    - action.py: _inject_reminders_if_final() lines 554-559
    
    Args:
        result: The result dictionary containing 'instructions'
        reminder: The reminder text to inject
        
    Returns:
        The modified result dictionary with reminder appended to base_instructions
    """
    # Caller must provide valid reminder - fail fast if missing
    if 'instructions' not in result:
        result['instructions'] = {}
    
    instructions = result['instructions']
    
    if not isinstance(instructions, dict):
        if isinstance(instructions, list):
            instructions = {'base_instructions': instructions}
        else:
            instructions = {}
        result['instructions'] = instructions
    
    base_instructions = instructions.get('base_instructions', [])
    
    if not isinstance(base_instructions, list):
        base_instructions = []
    
    # Make a copy to avoid mutating the original
    base_instructions = list(base_instructions)
    base_instructions.append("")
    base_instructions.append("**NEXT BEHAVIOR REMINDER:**")
    base_instructions.append(reminder)
    
    instructions['base_instructions'] = base_instructions
    result['instructions'] = instructions
    
    return result

