from typing import Dict, Any, Optional
from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
from agile_bot.bots.base_bot.src.actions.action_scope import ActionScope


class BuildScope(ActionScope):
    """
    Scope for build action.
    
    Extends ActionScope with build-specific behavior.
    Default scope is 'all' if not specified.
    """
    
    def __init__(self, parameters: Dict[str, Any], bot_paths: Optional[BotPaths] = None):
        super().__init__(parameters, bot_paths)
        # If no scope specified, default to 'all'
        if not self._scope_config or not any(key in self._scope_config for key in 
            ['story_names', 'increment_priorities', 'epic_names', 'increment_names', 'all']):
            self._scope_config['all'] = True













