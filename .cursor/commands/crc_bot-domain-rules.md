# crc_bot-domain-rules

Load domain behavior rules into AI context for guidance on writing new content.

## Command

python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior domain --action rules --message "${1:your question or request about domain rules}"

## What This Does

- Loads all domain behavior rules
- Displays numbered list of all rules in status.md
- Provides your message to AI with full rules context
- AI must read each rule file and apply them to your request
- AI helps you write new content following the rules

## Usage Examples

# Get guidance on writing domain content
python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior domain --action rules --message "Help me write a new story following our rules"

# Review work against rules
python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior domain --action rules --message "Does my scenario follow the rules?"