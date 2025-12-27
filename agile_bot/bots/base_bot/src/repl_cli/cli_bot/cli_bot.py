from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from agile_bot.bots.base_bot.src.bot.bot import Bot
    from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession

from agile_bot.bots.base_bot.src.repl_cli.cli_bot.cli_behaviors import CLIBehaviors


class CLIBot:
    
    def __init__(self, bot: Bot, session: REPLSession):
        self._bot = bot
        self._session = session
        self._behaviors = CLIBehaviors(bot.behaviors, session)
    
    @property
    def name(self) -> str:
        return self._bot.name
    
    @property
    def path(self) -> str:
        return str(self._bot.bot_paths.workspace_directory)
    
    @property
    def behaviors(self) -> CLIBehaviors:
        return self._behaviors
    
    @property
    def bot_directory(self) -> str:
        return str(self._bot.bot_paths.bot_directory)
    
    @property
    def domain_bot(self) -> Bot:
        return self._bot

