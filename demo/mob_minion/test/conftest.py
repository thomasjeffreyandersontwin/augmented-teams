"""Pytest configuration for mob_minion tests."""
import sys
from pathlib import Path

# Add src directory to Python path for clean imports
# This allows imports like: from domain.mob import Mob
# instead of: from src.domain.mob import Mob
test_dir = Path(__file__).parent
src_dir = test_dir.parent / 'src'
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))













