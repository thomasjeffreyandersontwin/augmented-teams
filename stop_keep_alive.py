#!/usr/bin/env python3
"""
Helper script to stop cursor_keep_alive_ui.py by creating the stop file.

Usage:
    python stop_keep_alive.py
"""

from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
STOP_FILE = SCRIPT_DIR / "stop_keep_alive.txt"

def stop_keep_alive():
    """Create the stop file to signal cursor_keep_alive_ui.py to stop."""
    try:
        STOP_FILE.touch()
        print(f"[OK] Stop file created: {STOP_FILE}")
        print("The keep-alive script should stop within the next second.")
    except Exception as e:
        print(f"[ERROR] Failed to create stop file: {e}")

if __name__ == "__main__":
    stop_keep_alive()















