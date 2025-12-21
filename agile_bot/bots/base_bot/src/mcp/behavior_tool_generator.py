import json
from pathlib import Path
from typing import Dict, Any, List
from agile_bot.bots.base_bot.src.bot.bot import Bot, BotResult
from agile_bot.bots.base_bot.src.bot.workspace import get_workspace_directory, get_bot_directory

class BehaviorTool:

    def __init__(self, bot_name: str, behavior_name: str, config_path: Path):
        self.bot_name = bot_name
        self.behavior_name = behavior_name
        self.config_path = config_path
        self.name = f'{bot_name}_{behavior_name}_tool'

    def invoke(self, parameters: Dict[str, Any]=None):
        bot = self._create_bot()
        behavior = bot.behaviors.find_by_name(self.behavior_name)
        action = behavior.actions.forward_to_current()
        return self._execute_action(action, parameters)

    def _create_bot(self) -> Bot:
        bot_directory = get_bot_directory()
        return Bot(bot_name=self.bot_name, bot_directory=bot_directory, config_path=self.config_path)

    def _execute_action(self, action, parameters: Dict[str, Any]=None) -> BotResult:
        try:
            result_data = action.execute(parameters or {})
            return BotResult(status='completed', behavior=self.behavior_name, action=action.action_name, data=result_data)
        except Exception as e:
            return self._create_error_result(str(e), type(e).__name__, action.action_name)

    def _create_error_result(self, message: str, error: str, action_name: str) -> BotResult:
        return BotResult(status='error', behavior=self.behavior_name, action=action_name, data={'message': message, 'error': error})

class BehaviorToolGenerator:

    def __init__(self, bot_name: str, config_path: Path):
        self.bot_name = bot_name
        self.config_path = config_path
        self.config = json.loads(config_path.read_text(encoding='utf-8'))

    def create_behavior_tools(self) -> List[BehaviorTool]:
        tools = []
        config_dir = self.config_path.parent
        behaviors_dir = config_dir / 'behaviors'
        if behaviors_dir.exists():
            for behavior_dir in behaviors_dir.iterdir():
                if behavior_dir.is_dir() and (not behavior_dir.name.startswith('_')):
                    behavior_name = behavior_dir.name
                    tool = BehaviorTool(bot_name=self.bot_name, behavior_name=behavior_name, config_path=self.config_path)
                    tools.append(tool)
        return tools