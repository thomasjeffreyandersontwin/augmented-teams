import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agile_bot.src.bot.bot_factory import BotFactory
from agile_bot.src.actions.strategy.json_strategy_action import JSONStrategyAction
import json

# Create bot and navigate to strategy
bot = BotFactory.create_bot('story_bot', 'C:/dev/augmented-teams/agile_bot')
bot.navigate('/story_bot/shape/strategy')

# Get the action
action = bot.behavior.current_action

# Create JSON adapter
adapter = JSONStrategyAction(action)

# Print the JSON output
result = adapter.to_dict()
print(json.dumps(result, indent=2))
