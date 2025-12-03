"""
Planning Action

Handles decide_planning_criteria action including:
- Injecting planning guardrails (assumptions and decision criteria)
"""
from pathlib import Path
from typing import Dict, Any
from agile_bot.bots.base_bot.src.utils import read_json_file, find_behavior_folder


class PlanningAction:
    """Planning action implementation."""
    
    def __init__(self, bot_name: str, behavior: str, workspace_root: Path):
        """Initialize Planning action.
        
        Args:
            bot_name: Name of the bot
            behavior: Behavior name
            workspace_root: Root workspace directory
        """
        self.bot_name = bot_name
        self.behavior = behavior
        self.workspace_root = Path(workspace_root)
    
    def _find_action_folder(self, action_name: str) -> Path:
        """Find action folder handling numbered prefixes."""
        base_actions_dir = self.workspace_root / 'agile_bot' / 'bots' / 'base_bot' / 'base_actions'
        
        # Try to find folder with action name (with or without number prefix)
        for folder in base_actions_dir.glob(f'*{action_name}'):
            if folder.is_dir():
                return folder
        
        return base_actions_dir / action_name
    
    def inject_decision_criteria_and_assumptions(self) -> Dict[str, Any]:
        """Inject planning guardrails into instructions.
        
        Returns:
            Instructions with planning criteria and assumptions
        """
        # Find behavior folder (handles numbered prefixes)
        try:
            behavior_folder = find_behavior_folder(
                self.workspace_root,
                self.bot_name,
                self.behavior
            )
            planning_dir = behavior_folder / 'guardrails' / 'planning'
        except FileNotFoundError:
            planning_dir = None
        
        instructions = {}
        
        if not planning_dir or not planning_dir.exists():
            return {'assumptions': [], 'decision_criteria': {}}
        
        # Load assumptions
        assumptions_file = planning_dir / 'typical_assumptions.json'
        if assumptions_file.exists():
            assumptions_data = read_json_file(assumptions_file)
            instructions['assumptions'] = assumptions_data.get('assumptions', [])
        else:
            instructions['assumptions'] = []
        
        # Load decision criteria
        criteria_dir = planning_dir / 'decision_criteria'
        if criteria_dir.exists() and criteria_dir.is_dir():
            decision_criteria = {}
            for criteria_file in criteria_dir.glob('*.json'):
                criteria_data = read_json_file(criteria_file)
                decision_criteria.update(criteria_data)
            instructions['decision_criteria'] = decision_criteria
        else:
            instructions['decision_criteria'] = {}
        
        return instructions


