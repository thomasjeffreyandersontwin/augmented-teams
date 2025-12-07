#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
from pathlib import Path

# Add the story_io module to path
sys.path.insert(0, r"c:\dev\augmented-teams\agile_bot\bots\story_bot\src\synchronizers\story_io")

print("Starting outline render...", flush=True)

try:
    from story_io.story_io_diagram import StoryIODiagram
    
    story_graph_path = Path(r"c:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\story-graph.json")
    output_path = Path(r"c:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\story-map-outline.drawio")
    
    print(f"Loading story graph from: {story_graph_path}", flush=True)
    print(f"Output will be written to: {output_path}", flush=True)
    
    # Load the story graph
    with open(story_graph_path, 'r', encoding='utf-8') as f:
        story_graph = json.load(f)
    
    print(f"Story graph loaded. Epics: {len(story_graph.get('epics', []))}", flush=True)
    
    # Create diagram and render
    diagram = StoryIODiagram()
    result = diagram.render_outline(output_path=output_path, story_graph=story_graph)
    
    print(f"Render complete!", flush=True)
    print(f"Output path: {result.get('output_path')}", flush=True)
    print(f"Summary: {result.get('summary')}", flush=True)
    print(f"File exists: {output_path.exists()}", flush=True)
    if output_path.exists():
        print(f"File size: {output_path.stat().st_size} bytes", flush=True)
    
except Exception as e:
    print(f"ERROR: {e}", file=sys.stderr, flush=True)
    import traceback
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)

print("Done!", flush=True)
