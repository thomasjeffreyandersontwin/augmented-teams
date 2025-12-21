# story_bot-tests-rules

Load tests behavior rules into AI context for guidance on writing effective, well-structured tests

## Command

python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior tests --action rules --message "${1:your question or request about tests rules}"

## What This Does

- Loads all tests behavior rules
- Displays numbered list of all rules in status.md
- Provides your message to AI with full rules context
- AI must read each rule file and apply them to your request
- AI helps you write new content following the rules

## Usage Examples

# Write new tests following rules
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior tests --action rules --message "Help me write tests for the new ValidationContext class"

# Design test structure following rules
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior tests --action rules --message "How should I structure tests for the rules validation workflow?"

# Write parameterized tests
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior tests --action rules --message "Create parameterized tests for multiple rule validation scenarios"