"""
Test Helpers

Shared helper functions for reading TinyDB activity logs.
"""
from pathlib import Path
from tinydb import TinyDB


def read_activity_log(log_file: Path):
    """Read all entries from TinyDB activity log."""
    with TinyDB(log_file) as db:
        return db.all()

