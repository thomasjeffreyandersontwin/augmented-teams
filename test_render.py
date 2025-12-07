import sys
from pathlib import Path

sys.path.insert(0, r"c:\dev\augmented-teams\agile_bot\bots\story_bot\src\synchronizers\story_io")

from story_io.story_io_cli import render_outline_command
from story_io.story_io_cli import argparse

# Create args object
args = argparse.Namespace()
args.story_graph = Path(r"c:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\story-graph.json")
args.json = None
args.drawio_file = None
args.output = Path(r"c:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\story-map-outline.drawio")
args.layout = None

print("Starting render...")
try:
    result = render_outline_command(args)
    print(f"Result: {result}")
    print(f"File exists: {args.output.exists()}")
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc()
