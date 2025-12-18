#!/usr/bin/env python3
"""Test script to see what CLI outputs"""
import sys
from pathlib import Path

# Setup Python import path
python_workspace_root = Path(__file__).parent
if str(python_workspace_root) not in sys.path:
    sys.path.insert(0, str(python_workspace_root))

from agile_bot.bots.story_bot.src.story_bot_cli import main

if __name__ == '__main__':
    # Test with shape clarify action
    sys.argv = ['story_bot_cli.py', '--behavior', 'shape', '--action', 'clarify']
    try:
        result = main()
        print("\n=== RESULT ===")
        print(f"Result type: {type(result)}")
        if result:
            print(f"Result keys: {result.keys() if isinstance(result, dict) else 'Not a dict'}")
            if isinstance(result, dict):
                data = result.get('data', {})
                print(f"Data keys: {data.keys() if isinstance(data, dict) else 'Not a dict'}")
                instructions = data.get('instructions', {})
                print(f"Instructions type: {type(instructions)}")
                print(f"Instructions keys: {instructions.keys() if isinstance(instructions, dict) else 'Not a dict'}")
                base_instructions = instructions.get('base_instructions', []) if isinstance(instructions, dict) else []
                print(f"Base instructions count: {len(base_instructions) if isinstance(base_instructions, list) else 'Not a list'}")
    except Exception as e:
        print(f"\n=== ERROR ===")
        import traceback
        traceback.print_exc()








