# story_bot-discovery-rules

Load discovery behavior rules into AI context for guidance on story decomposition and flow

## Command

python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior discovery --action rules --message "${1:your question or request about discovery rules}"

## What This Does

- Loads all discovery behavior rules
- Displays numbered list of all rules in status.md
- Provides your message to AI with full rules context
- AI must read each rule file and apply them to your request
- AI helps you write new content following the rules

## Usage Examples

# Get guidance on writing discovery content
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior discovery --action rules --message "Help me write a new story following our rules"

# Review work against rules
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior discovery --action rules --message "Does my scenario follow the rules?"