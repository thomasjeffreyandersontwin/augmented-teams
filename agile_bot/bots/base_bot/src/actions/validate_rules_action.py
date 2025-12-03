"""
Validate Rules Action

Handles validate_rules action including:
- Loading and merging common and behavior-specific validation rules
"""
from pathlib import Path
from typing import Dict, Any, List
from agile_bot.bots.base_bot.src.utils import read_json_file, find_behavior_folder


class ValidateRulesAction:
    """Validate Rules action implementation."""
    
    def __init__(self, bot_name: str, behavior: str, workspace_root: Path):
        """Initialize Validate Rules action.
        
        Args:
            bot_name: Name of the bot
            behavior: Behavior name
            workspace_root: Root workspace directory
        """
        self.bot_name = bot_name
        self.behavior = behavior
        self.workspace_root = Path(workspace_root)
    
    def inject_common_bot_rules(self) -> Dict[str, Any]:
        """Load common bot rules.
        
        Returns:
            Instructions with common rules
            
        Raises:
            FileNotFoundError: If common rules not found
        """
        # Try both potential paths for common rules
        rules_file = (
            self.workspace_root /
            'agile_bot' / 'bots' / 'base_bot' / 'rules' / 'common_rules.json'
        )
        if not rules_file.exists():
            rules_file = (
                self.workspace_root /
                'base_bot' / 'rules' / 'common_rules.json'
            )
        
        if not rules_file.exists():
            raise FileNotFoundError(
                f'Common bot rules not found at {rules_file}'
            )
        
        rules_data = read_json_file(rules_file)
        
        return {
            'validation_rules': rules_data.get('rules', [])
        }
    
    def inject_behavior_specific_and_bot_rules(self) -> Dict[str, Any]:
        """Load and merge behavior-specific and common bot rules.
        
        Returns:
            Instructions with merged validation rules
        """
        # Load common rules - try both paths
        common_rules = []
        common_file = (
            self.workspace_root /
            'agile_bot' / 'bots' / 'base_bot' / 'rules' / 'common_rules.json'
        )
        if not common_file.exists():
            common_file = (
                self.workspace_root /
                'base_bot' / 'rules' / 'common_rules.json'
            )
        
        if common_file.exists():
            common_data = read_json_file(common_file)
            common_rules = common_data.get('rules', [])
        
        # Load behavior-specific rules
        behavior_rules = []
        
        # Find behavior folder (handles numbered prefixes)
        try:
            behavior_folder = find_behavior_folder(
                self.workspace_root,
                self.bot_name,
                self.behavior
            )
            behavior_rules_dir = behavior_folder / 'rules'
        except FileNotFoundError:
            behavior_rules_dir = None
        
        # Check for single validation_rules.json file
        if behavior_rules_dir and behavior_rules_dir.exists():
            behavior_file = behavior_rules_dir / 'validation_rules.json'
            if behavior_file.exists():
                behavior_data = read_json_file(behavior_file)
                behavior_rules = behavior_data.get('rules', [])
            # Otherwise load all .json files from rules directory
            elif behavior_rules_dir.is_dir():
                for rule_file in behavior_rules_dir.glob('*.json'):
                    rule_data = read_json_file(rule_file)
                    # Add the rule file content with filename as identifier
                    behavior_rules.append({
                        'rule_file': rule_file.name,
                        'rule_content': rule_data
                    })
        
        # Merge rules
        all_rules = common_rules + behavior_rules
        
        return {
            'validation_rules': all_rules
        }


