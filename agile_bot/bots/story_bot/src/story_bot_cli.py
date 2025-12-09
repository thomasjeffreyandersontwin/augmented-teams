#!/usr/bin/env python3
"""
Story Bot CLI Entry Point

Command-line interface for story_bot using BaseBotCli.

Usage:
    story_bot [behavior] [action] [--options]
    story_bot --help          # Show help/usage documentation
    story_bot --list          # List available behaviors
    story_bot <behavior> --list  # List available actions for behavior
    story_bot --close         # Close current action

Examples:
    story_bot                          # Route to current behavior/action from workflow state
    story_bot exploration               # Route to exploration behavior, auto-forward to current action
    story_bot exploration gather_context  # Route directly to exploration.gather_context action
    story_bot exploration gather_context --increment_file=increment.txt  # With parameters
"""
from pathlib import Path
import sys
import os

# Use explicit working directory when invoked by tools. Tools should set
# the `WORKING_DIR` env var. If not set, fall back to the behavior-relative
# workspace root (development fallback).
# Preserve the Python import root for package imports so imports continue
# to work as before. This name makes the purpose clear and separates import
# resolution from runtime workspace I/O paths.
python_workspace_root = Path(__file__).parent.parent.parent.parent.parent
if str(python_workspace_root) not in sys.path:
    sys.path.insert(0, str(python_workspace_root))

# Use centralized helper for resolving the runtime workspace root
from agile_bot.bots.base_bot.src.state.workspace import get_workspace_directory

from agile_bot.bots.base_bot.src.cli.base_bot_cli import BaseBotCli


def main():
    """Main CLI entry point.

    Runtime workspace is determined from the environment (WORKING_AREA).
    """

    # No CLI workspace parameter — resolve from environment
    workspace_root = get_workspace_directory()

    bot_name = 'story_bot'
    bot_config_path = workspace_root / 'agile_bot' / 'bots' / bot_name / 'config' / 'bot_config.json'

    cli = BaseBotCli(
        bot_name=bot_name,
        bot_config_path=bot_config_path,
        workspace_root=workspace_root,
    )

    cli.main()


if __name__ == '__main__':
    main()
