"""
Base Bot Class

Provides core bot functionality including:
- Loading bot configuration
- Managing behaviors
- Routing tool invocations to behavior actions
"""
from pathlib import Path
from typing import Dict, Any
from agile_bot.bots.base_bot.src.utils import read_json_file


class BotResult:
    """Result from bot tool invocation."""
    
    def __init__(self, status: str, behavior: str, action: str, data: Dict[str, Any] = None):
        self.status = status
        self.behavior = behavior
        self.action = action
        self.data = data or {}
        self.executed_instructions_from = f'{behavior}/{action}'


class Behavior:
    """Behavior container that holds action methods."""
    
    def __init__(self, name: str, bot_name: str, workspace_root: Path):
        self.name = name
        self.bot_name = bot_name
        self.workspace_root = Path(workspace_root)
    
    def gather_context(self, parameters: Dict[str, Any] = None) -> BotResult:
        """Execute gather context action."""
        from agile_bot.bots.base_bot.src.actions.gather_context_action import GatherContextAction
        
        action = GatherContextAction(
            bot_name=self.bot_name,
            behavior=self.name,
            workspace_root=self.workspace_root
        )
        instructions = action.load_and_merge_instructions()
        
        return BotResult(
            status='completed',
            behavior=self.name,
            action='gather_context',
            data={'instructions': instructions}
        )
    
    def decide_planning_criteria(self, parameters: Dict[str, Any] = None) -> BotResult:
        """Execute decide planning criteria action."""
        from agile_bot.bots.base_bot.src.actions.planning_action import PlanningAction
        
        action = PlanningAction(
            bot_name=self.bot_name,
            behavior=self.name,
            workspace_root=self.workspace_root
        )
        instructions = action.inject_decision_criteria_and_assumptions()
        
        return BotResult(
            status='completed',
            behavior=self.name,
            action='decide_planning_criteria',
            data={'instructions': instructions}
        )
    
    def build_knowledge(self, parameters: Dict[str, Any] = None) -> BotResult:
        """Execute build knowledge action."""
        from agile_bot.bots.base_bot.src.actions.build_knowledge_action import BuildKnowledgeAction
        
        action = BuildKnowledgeAction(
            bot_name=self.bot_name,
            behavior=self.name,
            workspace_root=self.workspace_root
        )
        
        try:
            instructions = action.inject_knowledge_graph_template()
        except FileNotFoundError:
            # Template not required for all behaviors
            instructions = {}
        
        return BotResult(
            status='completed',
            behavior=self.name,
            action='build_knowledge',
            data={'instructions': instructions}
        )
    
    def render_output(self, parameters: Dict[str, Any] = None) -> BotResult:
        """Execute render output action."""
        return BotResult(
            status='completed',
            behavior=self.name,
            action='render_output'
        )
    
    def validate_rules(self, parameters: Dict[str, Any] = None) -> BotResult:
        """Execute validate rules action."""
        from agile_bot.bots.base_bot.src.actions.validate_rules_action import ValidateRulesAction
        
        action = ValidateRulesAction(
            bot_name=self.bot_name,
            behavior=self.name,
            workspace_root=self.workspace_root
        )
        instructions = action.inject_behavior_specific_and_bot_rules()
        
        return BotResult(
            status='completed',
            behavior=self.name,
            action='validate_rules',
            data={'instructions': instructions}
        )
    
    def correct_bot(self, parameters: Dict[str, Any] = None) -> BotResult:
        """Execute correct bot action."""
        return BotResult(
            status='completed',
            behavior=self.name,
            action='correct_bot'
        )


class Bot:
    """Base Bot class that manages behaviors and routes actions."""
    
    def __init__(self, bot_name: str, workspace_root: Path, config_path: Path):
        """Initialize Bot.
        
        Args:
            bot_name: Name of the bot
            workspace_root: Root workspace directory
            config_path: Path to bot_config.json
        """
        self.name = bot_name
        self.workspace_root = Path(workspace_root)
        self.config_path = Path(config_path)
        
        # Load config
        if not self.config_path.exists():
            raise FileNotFoundError(f'Bot config not found at {self.config_path}')
        
        # read_json_file already handles UTF-8 and raises appropriate errors
        self.config = read_json_file(self.config_path)
        
        # Initialize behaviors as attributes
        self.behaviors = self.config.get('behaviors', [])
        for behavior_name in self.behaviors:
            behavior_obj = Behavior(
                name=behavior_name,
                bot_name=self.name,
                workspace_root=self.workspace_root
            )
            setattr(self, behavior_name, behavior_obj)
    
    def invoke_tool(self, tool_name: str, parameters: Dict[str, Any]) -> BotResult:
        """Invoke a tool by routing to the correct behavior action.
        
        Args:
            tool_name: Name of the tool (e.g., 'test_bot_shape_gather_context')
            parameters: Parameters including 'behavior' and 'action'
            
        Returns:
            BotResult with execution details
            
        Raises:
            AttributeError: If behavior not found
            FileNotFoundError: If action not found in base actions
        """
        behavior = parameters.get('behavior')
        action = parameters.get('action')
        
        # Get behavior object
        behavior_obj = getattr(self, behavior, None)
        if behavior_obj is None:
            raise AttributeError(
                f'Behavior {behavior} not found in bot {self.name}. '
                f'Available behaviors: {", ".join(self.behaviors)}'
            )
        
        # Get action method
        action_method = getattr(behavior_obj, action, None)
        if action_method is None:
            raise FileNotFoundError(
                f'Action {action} not found in base actions'
            )
        
        # Execute action
        return action_method(parameters)

