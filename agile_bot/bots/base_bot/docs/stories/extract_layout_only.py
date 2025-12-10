#!/usr/bin/env python3
"""Extract layout from DrawIO without overwriting story details."""

import sys
from pathlib import Path
import json

# Add story_bot src to path
script_dir = Path(__file__).parent
base_bot_dir = script_dir.parent.parent.parent
bots_dir = base_bot_dir.parent
story_bot_src = bots_dir / "story_bot" / "src"
if story_bot_src.exists():
    sys.path.insert(0, str(story_bot_src))
else:
    workspace_root = Path(__file__).resolve()
    while workspace_root.name != 'augmented-teams' and workspace_root.parent != workspace_root:
        workspace_root = workspace_root.parent
    story_bot_src = workspace_root / "agile_bot" / "bots" / "story_bot" / "src"
    sys.path.insert(0, str(story_bot_src))

from synchronizers.story_io.story_map_drawio_synchronizer import extract_layout_from_drawio

def main():
    stories_dir = Path(__file__).parent
    drawio_path = stories_dir / "story-map-increments.drawio"
    layout_output = stories_dir / "story-map-increments-layout.json"
    
    print(f"Extracting layout from: {drawio_path}")
    
    # Extract layout only
    layout_data = extract_layout_from_drawio(drawio_path)
    
    if layout_data:
        with open(layout_output, 'w', encoding='utf-8') as f:
            json.dump(layout_data, f, indent=2, ensure_ascii=False)
        print(f"✓ Layout extracted to: {layout_output}")
    else:
        print("No layout data extracted")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

