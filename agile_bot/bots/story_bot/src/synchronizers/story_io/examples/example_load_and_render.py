"""
Example: Load and render from structured.json

This shows exactly how to:
1. Load story graph from file
2. Render to DrawIO
"""

import sys
from pathlib import Path

# Add parent directories to path so we can import from the package
# examples/ -> story_io/ -> synchronizers/ -> src/
_script_dir = Path(__file__).parent  # examples/
_story_io_dir = _script_dir.parent   # story_io/
_synchronizers_dir = _story_io_dir.parent  # synchronizers/
_src_dir = _synchronizers_dir.parent  # src/
sys.path.insert(0, str(_src_dir))

from synchronizers.story_io.story_io_diagram import StoryIODiagram
from synchronizers.story_io.examples.render_example import adapt_story_graph
import json


# Load from the structured.json file
# From examples/ -> story_io/ -> synchronizers/ -> src/ -> story_bot/ -> bots/ -> agile_bot/
workspace_root = Path(__file__).parent.parent.parent.parent.parent.parent
structured_path = workspace_root  / "base_bot" / "docs" / "stories" / "story-graph.json"

# Load the JSON
print(f"Loading story graph from: {structured_path}")
with open(structured_path, 'r', encoding='utf-8') as f:
    original_data = json.load(f)

print(f"Original epics count: {len(original_data.get('epics', []))}")
for i, epic in enumerate(original_data.get('epics', []), 1):
    sub_epic_count = len(epic.get('sub_epics', []))
    feature_count = len(epic.get('features', []))
    print(f"  Epic {i}: {epic['name']} (sub_epics: {sub_epic_count}, features: {feature_count})")

# Adapt format (converts behavioral_ac to Steps, handles empty users)
print("\nAdapting story graph format...")
adapted_data = adapt_story_graph(original_data)

print(f"Adapted epics count: {len(adapted_data.get('epics', []))}")
for i, epic in enumerate(adapted_data.get('epics', []), 1):
    sub_epic_count = len(epic.get('sub_epics', []))
    feature_count = len(epic.get('features', []))
    print(f"  Epic {i}: {epic['name']} (sub_epics: {sub_epic_count}, features: {feature_count})")

# Create empty diagram and load adapted data
print("\nLoading diagram from adapted data...")
diagram = StoryIODiagram(drawio_file=None)
diagram._load_from_story_graph_format(adapted_data)

print(f"Diagram epics loaded: {len([c for c in diagram._children if hasattr(c, 'name') and 'epic' in str(type(c)).lower()])}")

# Render outline
output_path = structured_path.parent / "story-map-outline.drawio"
print(f"\nRendering outline to: {output_path}")
result = diagram.render_outline(output_path=str(output_path))

print(f"\n✓ Rendered: {result['output_path']}")
print(f"✓ Epics rendered: {result['summary'].get('epics', 0)}")
print(f"✓ Features rendered: {result['summary'].get('features', 0)}")


# Option 2: Render directly from graph (simpler)
# result = StoryIODiagram.render_outline_from_graph(
#     story_graph=adapted_data,
#     output_path='demo/cheap_wealth_online/docs/stories/story-map-outline.drawio'
# )

