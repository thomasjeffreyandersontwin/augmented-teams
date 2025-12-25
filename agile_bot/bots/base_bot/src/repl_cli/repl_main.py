#!/usr/bin/env python3
"""
Interactive REPL for Base Bot

Usage:
    python repl_main.py
    
The REPL will:
1. Load existing workflow state if present
2. Display current position in workflow
3. Accept commands interactively
4. Save state after each command

Available Commands:
    behavior <name>     - Switch to a behavior
    action <name>       - Navigate to an action
    current             - Show current action status
    run                 - Execute current action (mock)
    y / yes             - Confirm and advance to next action
    close               - Complete current action and advance
    back                - Move back to previous action
    status              - Show current status
    help                - Show available actions
    help <action>       - Show detailed help for action
    exit                - Exit REPL
"""
import sys
import os
import json
from pathlib import Path

# Calculate paths from this file's location
# This file is at: agile_bot/bots/base_bot/src/repl_cli/repl_main.py
# Must resolve() first to handle relative paths with ".." components
script_path = Path(__file__).resolve()
# Go up to workspace root: repl_main.py -> repl_cli -> src -> base_bot -> bots -> agile_bot -> workspace_root
workspace_root = script_path.parent.parent.parent.parent.parent.parent

if str(workspace_root) not in sys.path:
    sys.path.insert(0, str(workspace_root))

# Bot directory is ALWAYS story_bot (where behaviors are loaded from)
bot_directory = workspace_root / 'agile_bot' / 'bots' / 'story_bot'
os.environ['BOT_DIRECTORY'] = str(bot_directory)

# Bootstrap WORKING_AREA from bot config if not already set
if 'WORKING_AREA' not in os.environ and 'WORKING_DIR' not in os.environ:
    config_path = bot_directory / 'bot_config.json'
    if config_path.exists():
        try:
            bot_config = json.loads(config_path.read_text(encoding='utf-8'))
            if 'mcp' in bot_config and 'env' in bot_config['mcp']:
                mcp_env = bot_config['mcp']['env']
                if 'WORKING_AREA' in mcp_env:
                    os.environ['WORKING_AREA'] = mcp_env['WORKING_AREA']
            elif 'WORKING_AREA' in bot_config:
                os.environ['WORKING_AREA'] = bot_config['WORKING_AREA']
        except:
            pass
    
    # If still not set, default to workspace root
    if 'WORKING_AREA' not in os.environ:
        os.environ['WORKING_AREA'] = str(workspace_root)

from agile_bot.bots.base_bot.src.bot.bot import Bot
from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
from agile_bot.bots.base_bot.src.bot.workspace import get_bot_directory, get_workspace_directory


def main():
    """Launch interactive REPL session"""
    
    # Bot directory was set at module level to always be story_bot
    # (where behaviors are loaded from)
    bot_name = 'story_bot'
    
    # Get workspace directory (where your stories/documents are)
    workspace_directory = get_workspace_directory()
    
    # Create bot instance
    bot_config_path = bot_directory / 'bot_config.json'
    
    if not bot_config_path.exists():
        print(f"ERROR: Bot config not found at {bot_config_path}")
        print("Please ensure you're running from the correct directory.")
        sys.exit(1)
    
    try:
        bot = Bot(
            bot_name=bot_name,
            bot_directory=bot_directory,
            config_path=bot_config_path
        )
    except Exception as e:
        print(f"ERROR: Failed to initialize bot: {e}")
        sys.exit(1)
    
    # Create REPL session
    repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
    
    # Check TTY before printing header
    tty_result = repl_session.detect_tty()
    is_pipe_mode = not tty_result.tty_detected
    
    # Print header
    print("=" * 60)
    print(f"{bot_name.upper()} CLI")
    
    # Add explicit instruction when in piped mode
    if is_pipe_mode:
        print("")
        print("=" * 60)
        print("AI AGENT INSTRUCTIONS - PIPED MODE")
        print("=" * 60)
        print("")
        print("*** THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND ***")
        print("This is NORMAL and EXPECTED behavior in piped mode.")
        print("")
        print("HOW TO RUN COMMANDS (PowerShell):")
        print("-" * 60)
        print("Commands must be PIPED via echo, NOT passed as arguments!")
        print("")
        print("  # Set environment and pipe command:")
        print("  cd C:\\dev\\augmented-teams")
        print("  $env:PYTHONPATH = 'C:\\dev\\augmented-teams'")
        print("  $env:BOT_DIRECTORY = 'C:\\dev\\augmented-teams\\agile_bot\\bots\\story_bot'")
        print("  $env:WORKING_AREA = '<project_path>'  # e.g. demo\\mob_minion")
        print("  echo '<command>' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py")
        print("")
        print("WHAT DOES NOT WORK:")
        print("-" * 60)
        print("  [X] python repl_main.py instructions        # No args!")
        print("  [X] python repl_main.py --command instructions  # No flags!")
        print("")
        print("WHAT WORKS:")
        print("-" * 60)
        print("  [OK] echo 'instructions' | python repl_main.py  # Piped input")
        print("  [OK] echo 'next' | python repl_main.py")
        print("  [OK] echo 'status' | python repl_main.py")
        print("")
        print("PIPED MODE WORKFLOW:")
        print("-" * 60)
        print("1. Pipe command -> REPL runs -> shows output -> EXITS")
        print("2. Read output, do work (create files, etc.)")
        print("3. Pipe next command -> REPL runs -> shows output -> EXITS")
        print("4. Repeat for each step in workflow")
        print("")
        print("CRITICAL RULES:")
        print("-" * 60)
        print("  - ALWAYS pipe commands: echo <cmd> | python repl_main.py")
        print("  - DO NOT manipulate behavior_action_state.json directly")
        print("  - Each command starts fresh REPL session (this is normal)")
        print("")
    
    print("-" * 60)
    print(f"Bot Path: {bot_directory}")
    print(f"Work Path: {workspace_directory}")
    print("-" * 60)
    
    # Display rest of state (commands menu)
    state_display = repl_session.display_current_state()
    print(state_display.output)
    
    # Main REPL loop
    try:
        while True:
            # Prompt for command
            try:
                if is_pipe_mode:
                    # Pipe mode: read from stdin without prompt
                    command = input().strip()
                else:
                    # Interactive mode: show prompt
                    command = input(f"[{bot_name}] > ").strip()
            except EOFError:
                if not is_pipe_mode:
                    print("\nExiting REPL...")
                break
            
            if not command:
                continue
            
            # Execute command
            response = repl_session.read_and_execute_command(command)
            
            # Display response (sanitize Unicode for Windows console)
            safe_output = response.output.encode('ascii', errors='replace').decode('ascii')
            print(safe_output)
            if not is_pipe_mode:
                print()
            
            # Check if should exit
            if response.repl_terminated:
                break
    
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Exiting REPL...")
        sys.exit(0)
    
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

