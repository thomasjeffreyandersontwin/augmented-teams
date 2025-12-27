"""
Pytest configuration and fixtures for REPL CLI tests

This file must be loaded FIRST to set up environment variables
before any other modules are imported.
"""
import os
import sys
import pytest
from pathlib import Path

# Set required environment variables BEFORE any other imports
if 'PYTHONPATH' not in os.environ:
    repo_root = Path(__file__).parent.parent.parent.parent.parent
    os.environ['PYTHONPATH'] = str(repo_root)

if 'WORKING_AREA' not in os.environ:
    # Set to a test workspace directory
    os.environ['WORKING_AREA'] = str(Path(__file__).parent / '.test_workspace')

if 'BOT_DIRECTORY' not in os.environ:
    # Set to story_bot for testing
    repo_root = Path(__file__).parent.parent.parent.parent.parent
    os.environ['BOT_DIRECTORY'] = str(repo_root / 'agile_bot' / 'bots' / 'story_bot')


@pytest.fixture(autouse=True)
def setup_test_env_vars(bot_directory, workspace_directory, monkeypatch):
    """
    Automatically set environment variables to point to the test-specific temp directories.
    This ensures that the Bot uses the same workspace directory as the test.
    """
    if hasattr(bot_directory, '__fspath__'):  # Check if it's a Path object
        monkeypatch.setenv('BOT_DIRECTORY', str(bot_directory))
    if hasattr(workspace_directory, '__fspath__'):  # Check if it's a Path object
        monkeypatch.setenv('WORKING_AREA', str(workspace_directory))
