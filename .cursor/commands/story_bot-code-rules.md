# story_bot-code-rules

Load code behavior rules into AI context for guidance on writing clean, maintainable production code

## Command

python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action rules --message "${1:your question or request about code rules}"

## What This Does

- Loads all code behavior rules
- Displays numbered list of all rules in status.md
- Provides your message to AI with full rules context
- AI must read each rule file and apply them to your request
- AI helps you write new content following the rules

## Usage Examples

# Write new production code following rules
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action rules --message "Help me write a new ValidationContext class that encapsulates validation parameters"

# Refactor existing code to follow rules
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action rules --message "Refactor the _execute_scanner method to reduce parameters from 10 to 3"

# Design API following rules
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action rules --message "Design a clean API for loading and filtering rules"