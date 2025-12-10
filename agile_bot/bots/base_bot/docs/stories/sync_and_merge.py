#!/usr/bin/env python3
"""Extract layout and merge Inject/Store Content stories from epics."""

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

from synchronizers.story_io.story_io_diagram import StoryIODiagram

def find_stories_in_epics(story_graph, story_names):
    """Find stories in epics section that match the given names."""
    found_stories = []
    
    for epic in story_graph.get("epics", []):
        for sub_epic in epic.get("sub_epics", []):
            for story_group in sub_epic.get("story_groups", []):
                for story in story_group.get("stories", []):
                    if story.get("name") in story_names:
                        # Make a copy to avoid modifying original
                        story_copy = json.loads(json.dumps(story))
                        found_stories.append(story_copy)
    
    return found_stories

def main():
    stories_dir = Path(__file__).parent
    drawio_path = stories_dir / "story-map-increments.drawio"
    story_graph_path = stories_dir / "story-graph.json"
    temp_extracted = stories_dir / "story-graph-temp-extracted.json"
    
    # Load current story graph
    print(f"Loading story graph from {story_graph_path}")
    with open(story_graph_path, 'r', encoding='utf-8') as f:
        story_graph = json.load(f)
    
    # Find stories in epics that should be in "Inject / Store Content" increment
    stories_to_merge = ["Store Context Files", "Stores Activity for Initialize Project Action"]
    print(f"\nLooking for stories in epics: {stories_to_merge}")
    found_stories = find_stories_in_epics(story_graph, stories_to_merge)
    print(f"Found {len(found_stories)} stories in epics section:")
    for story in found_stories:
        print(f"  - {story.get('name')}")
    
    # Extract from DrawIO to get layout (save to temp file)
    print(f"\nExtracting layout from DrawIO: {drawio_path}")
    diagram = StoryIODiagram.load_from_story_graph(story_graph_path, drawio_path)
    extracted_data = diagram.synchronize_increments(
        drawio_path=drawio_path,
        original_path=story_graph_path,
        output_path=temp_extracted
    )
    
    # Load the layout file that was created
    layout_file = temp_extracted.parent / f"{temp_extracted.stem}-layout.json"
    if layout_file.exists():
        print(f"Layout file created: {layout_file}")
        # Copy to the standard layout file name
        import shutil
        standard_layout = stories_dir / "story-map-increments-layout.json"
        shutil.copy2(layout_file, standard_layout)
        print(f"Layout saved to: {standard_layout}")
    
    # Now work with the original story_graph and add "Inject / Store Content" increment
    # Check if increment already exists
    inject_store_increment = None
    for increment in story_graph.get("increments", []):
        if increment.get("name") == "Inject / Store Content":
            inject_store_increment = increment
            break
    
    if not inject_store_increment:
        # Create the increment
        print("\nCreating 'Inject / Store Content' increment...")
        # Find highest priority
        max_priority = max([inc.get("priority", 0) for inc in story_graph.get("increments", [])], default=0)
        inject_store_increment = {
            "name": "Inject / Store Content",
            "priority": max_priority + 1,
            "epics": [
                {
                    "name": "Build Agile Bots",
                    "sequential_order": 1,
                    "sub_epics": [
                        {
                            "name": "Generate MCP Tools",
                            "sequential_order": 1,
                            "sub_epics": [],
                            "story_groups": [
                                {
                                    "type": "and",
                                    "stories": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "Invoke Bot",
                    "sequential_order": 2,
                    "sub_epics": [
                        {
                            "name": "Invoke MCP",
                            "sequential_order": 2,
                            "sub_epics": [],
                            "stories": [
                                {
                                    "name": "Save Through MCP",
                                    "sequential_order": 5,
                                    "connector": "or",
                                    "users": [],
                                    "story_type": "user"
                                }
                            ]
                        },
                        {
                            "name": "Invoke CLI",
                            "sequential_order": 3,
                            "sub_epics": [],
                            "stories": [
                                {
                                    "name": "Save Through CLI",
                                    "sequential_order": 5,
                                    "connector": "or",
                                    "users": [],
                                    "story_type": "user"
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "Execute Behavior Actions",
                    "sequential_order": 3,
                    "sub_epics": [
                        {
                            "name": "Gather Context",
                            "sequential_order": 1,
                            "sub_epics": [],
                            "stories": [
                                {
                                    "name": "Load + Inject  Guardrails",
                                    "sequential_order": 6,
                                    "connector": "or",
                                    "users": [],
                                    "story_type": "user"
                                },
                                {
                                    "name": "Gather Context Saves To Context Folder",
                                    "sequential_order": 7,
                                    "connector": "or",
                                    "users": [],
                                    "story_type": "user"
                                }
                            ]
                        },
                        {
                            "name": "Decide Planning Criteria Action",
                            "sequential_order": 2,
                            "sub_epics": [],
                            "stories": [
                                {
                                    "name": "Save Final Assumptions and Decisions",
                                    "sequential_order": 4,
                                    "connector": "or",
                                    "users": [],
                                    "story_type": "user"
                                }
                            ]
                        },
                        {
                            "name": "Build Knowledge",
                            "sequential_order": 3,
                            "sub_epics": [],
                            "stories": [
                                {
                                    "name": "Load + Inject Knolwedge Graph",
                                    "sequential_order": 6,
                                    "connector": "or",
                                    "users": [],
                                    "story_type": "user"
                                },
                                {
                                    "name": "Save Knowledge Graph",
                                    "sequential_order": 7,
                                    "connector": "or",
                                    "users": [],
                                    "story_type": "user"
                                }
                            ]
                        },
                        {
                            "name": "Render Output",
                            "sequential_order": 4,
                            "sub_epics": [],
                            "stories": [
                                {
                                    "name": "Load+ Inject Content Into Instructions",
                                    "sequential_order": 8,
                                    "connector": "or",
                                    "users": [],
                                    "story_type": "user"
                                },
                                {
                                    "name": "Save Content",
                                    "sequential_order": 9,
                                    "connector": "or",
                                    "users": [],
                                    "story_type": "user"
                                }
                            ]
                        },
                        {
                            "name": "Validate Knowledge & Content Against Rules",
                            "sequential_order": 5,
                            "sub_epics": [],
                            "stories": [
                                {
                                    "name": "Run Diagnostics + inject Results",
                                    "sequential_order": 5,
                                    "connector": "or",
                                    "users": [],
                                    "story_type": "user"
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        story_graph["increments"].append(inject_store_increment)
    
    # Merge found stories into the increment
    print("\nMerging stories into 'Inject / Store Content' increment...")
    for epic in inject_store_increment.get("epics", []):
        if epic.get("name") == "Build Agile Bots":
            for sub_epic in epic.get("sub_epics", []):
                if sub_epic.get("name") == "Generate MCP Tools":
                    story_group = sub_epic["story_groups"][0]
                    existing_names = [s.get("name") for s in story_group.get("stories", [])]
                    
                    for story in found_stories:
                        if story.get("name") not in existing_names:
                            story_group["stories"].append(story)
                            print(f"  Added: {story.get('name')}")
                        else:
                            print(f"  Already exists: {story.get('name')}")
    
    # Save updated story graph
    print(f"\nSaving updated story graph to: {story_graph_path}")
    with open(story_graph_path, 'w', encoding='utf-8') as f:
        json.dump(story_graph, f, indent=2, ensure_ascii=False)
    
    # Clean up temp file
    if temp_extracted.exists():
        temp_extracted.unlink()
    
    print("\n✓ Complete!")
    print(f"  Layout preserved from: {drawio_path}")
    print(f"  Stories merged from epics section")
    print(f"  Updated: {story_graph_path}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

