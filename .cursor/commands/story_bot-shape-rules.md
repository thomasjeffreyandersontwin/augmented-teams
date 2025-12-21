# story_bot-shape-rules

Load shape behavior rules into AI context for guidance on story mapping and domain modeling

## Command

python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior shape --action rules --message "${1:your question or request about shape rules}"

## What This Does

- Loads all shape behavior rules
- Displays numbered list of all rules in status.md
- Provides your message to AI with full rules context
- AI must read each rule file and apply them to your request
- AI helps you write new content following the rules

## Usage Examples

# Get guidance on writing shape content
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior shape --action rules --message "Help me write a new story following our rules"

# Review work against rules
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior shape --action rules --message "Does my scenario follow the rules?"