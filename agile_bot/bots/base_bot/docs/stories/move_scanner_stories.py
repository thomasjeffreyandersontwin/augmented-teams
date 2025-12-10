#!/usr/bin/env python3
"""Move code scanner stories from epics to Code Scanner increment and preserve layout."""

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

def find_scanner_stories_in_epics(story_graph):
    """Find all scanner-related stories in epics section."""
    scanner_stories = []
    scanner_story_names = [
        "System Discovers Scanners from rule.json",
        "System Loads Scanner Classes",
        "System Runs Scanners After Build Knowledge",
        "System Runs Scanners After Render Output",
        "System Runs Scanners Before AI Validation",
        "Scanner Detects Violations Using Regex Patterns",
        "Scanner Detects Violations Using AST Parsing",
        "Scanner Detects Violations Using File Structure Analysis",
        "System Collects Violations from All Scanners",
        "System Reports Violations with Location Context"
    ]
    
    for epic in story_graph.get("epics", []):
        for sub_epic in epic.get("sub_epics", []):
            if sub_epic.get("name") == "Validate Knowledge & Content Against Rules":
                for story_group in sub_epic.get("story_groups", []):
                    stories_to_remove = []
                    for story in story_group.get("stories", []):
                        if story.get("name") in scanner_story_names:
                            story_copy = json.loads(json.dumps(story))
                            scanner_stories.append(story_copy)
                            stories_to_remove.append(story)
                    
                    # Remove scanner stories from epics
                    for story in stories_to_remove:
                        story_group["stories"].remove(story)
    
    return scanner_stories

def main():
    stories_dir = Path(__file__).parent
    drawio_path = stories_dir / "story-map-increments.drawio"
    story_graph_path = stories_dir / "story-graph.json"
    temp_extracted = stories_dir / "story-graph-temp-extracted.json"
    
    # Load current story graph
    print(f"Loading story graph from {story_graph_path}")
    with open(story_graph_path, 'r', encoding='utf-8') as f:
        story_graph = json.load(f)
    
    # Find scanner stories in epics
    print("\nLooking for scanner stories in epics section...")
    scanner_stories = find_scanner_stories_in_epics(story_graph)
    print(f"Found {len(scanner_stories)} scanner stories in epics:")
    for story in scanner_stories:
        print(f"  - {story.get('name')}")
    
    # Extract from DrawIO to preserve layout (using Story I/O synchronize_increments)
    print(f"\nExtracting from DrawIO with preserve layout: {drawio_path}")
    diagram = StoryIODiagram.load_from_story_graph(story_graph_path, drawio_path)
    extracted_data = diagram.synchronize_increments(
        drawio_path=drawio_path,
        original_path=story_graph_path,
        output_path=temp_extracted  # This automatically preserves layout
    )
    
    # Load the layout file that was created
    layout_file = temp_extracted.parent / f"{temp_extracted.stem}-layout.json"
    if layout_file.exists():
        print(f"Layout file created: {layout_file}")
        import shutil
        standard_layout = stories_dir / "story-map-increments-layout.json"
        shutil.copy2(layout_file, standard_layout)
        print(f"Layout saved to: {standard_layout}")
    
    # Load extracted data to find scanner stories
    print("\nLoading extracted data to find scanner stories...")
    with open(temp_extracted, 'r', encoding='utf-8') as f:
        extracted_graph = json.load(f)
    
    # Create scanner stories based on merge report (they exist in DrawIO but need to be added)
    # These stories are shown in the merge report as new stories from DrawIO
    scanner_stories_to_add = [
        {
            "name": "System Discovers Scanners from rule.json",
            "sequential_order": 4,
            "connector": "and",
            "users": ["Bot Behavior"],
            "story_type": "user"
        },
        {
            "name": "System Loads Scanner Classes",
            "sequential_order": 5,
            "connector": "and",
            "users": ["Bot Behavior"],
            "story_type": "user"
        },
        {
            "name": "System Runs Scanners After Build Knowledge",
            "sequential_order": 6,
            "connector": "and",
            "users": ["Bot Behavior"],
            "story_type": "user"
        },
        {
            "name": "System Runs Scanners After Render Output",
            "sequential_order": 7,
            "connector": "and",
            "users": ["Bot Behavior"],
            "story_type": "user"
        },
        {
            "name": "System Runs Scanners Before AI Validation",
            "sequential_order": 8,
            "connector": "and",
            "users": ["Bot Behavior"],
            "story_type": "user"
        },
        {
            "name": "Scanner Detects Violations Using Regex Patterns",
            "sequential_order": 9,
            "connector": "and",
            "users": ["Bot Behavior"],
            "story_type": "user"
        },
        {
            "name": "Scanner Detects Violations Using AST Parsing",
            "sequential_order": 10,
            "connector": "and",
            "users": ["Bot Behavior"],
            "story_type": "user"
        },
        {
            "name": "Scanner Detects Violations Using File Structure Analysis",
            "sequential_order": 11,
            "connector": "and",
            "users": ["Bot Behavior"],
            "story_type": "user"
        },
        {
            "name": "System Collects Violations from All Scanners",
            "sequential_order": 12,
            "connector": "and",
            "users": ["Bot Behavior"],
            "story_type": "user"
        },
        {
            "name": "System Reports Violations with Location Context",
            "sequential_order": 13,
            "connector": "and",
            "users": ["Bot Behavior"],
            "story_type": "user"
        }
    ]
    
    print(f"Prepared {len(scanner_stories_to_add)} scanner stories to add:")
    for story in scanner_stories_to_add:
        print(f"  - {story.get('name')}")
    
    # Use scanner stories from epics (if any) plus the ones to add from DrawIO
    all_scanner_stories = scanner_stories + scanner_stories_to_add
    # Remove duplicates by name
    seen_names = set()
    unique_scanner_stories = []
    for story in all_scanner_stories:
        if story.get("name") not in seen_names:
            seen_names.add(story.get("name"))
            unique_scanner_stories.append(story)
    
    # Find or create Code Scanner increment
    code_scanner_increment = None
    for increment in story_graph.get("increments", []):
        if increment.get("name") == "Code Scanner":
            code_scanner_increment = increment
            break
    
    if not code_scanner_increment:
        print("\nCreating 'Code Scanner' increment...")
        # Find highest priority
        max_priority = max([inc.get("priority", 0) for inc in story_graph.get("increments", [])], default=0)
        code_scanner_increment = {
            "name": "Code Scanner",
            "priority": max_priority + 1,
            "epics": [
                {
                    "name": "Execute Behavior Actions",
                    "sequential_order": 3,
                    "sub_epics": [
                        {
                            "name": "Validate Knowledge & Content Against Rules",
                            "sequential_order": 5.0,
                            "sub_epics": [],
                            "story_groups": [
                                {
                                    "type": "and",
                                    "stories": []
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        story_graph["increments"].append(code_scanner_increment)
    
    # Add scanner stories to Code Scanner increment
    print("\nAdding scanner stories to Code Scanner increment...")
    for epic in code_scanner_increment.get("epics", []):
        if epic.get("name") == "Execute Behavior Actions":
            for sub_epic in epic.get("sub_epics", []):
                if sub_epic.get("name") == "Validate Knowledge & Content Against Rules":
                    story_group = sub_epic["story_groups"][0]
                    existing_names = [s.get("name") for s in story_group.get("stories", [])]
                    
                    for story in unique_scanner_stories:
                        if story.get("name") not in existing_names:
                            story_group["stories"].append(story)
                            print(f"  Added: {story.get('name')}")
                        else:
                            print(f"  Already exists: {story.get('name')}")
    
    # Verify scanner stories are removed from epics
    print("\nVerifying scanner stories removed from epics...")
    remaining_scanner_stories = find_scanner_stories_in_epics(story_graph)
    if remaining_scanner_stories:
        print(f"  WARNING: {len(remaining_scanner_stories)} scanner stories still in epics!")
        for story in remaining_scanner_stories:
            print(f"    - {story.get('name')}")
    else:
        print("  ✓ All scanner stories removed from epics section")
    
    # Save updated story graph
    print(f"\nSaving updated story graph to: {story_graph_path}")
    with open(story_graph_path, 'w', encoding='utf-8') as f:
        json.dump(story_graph, f, indent=2, ensure_ascii=False)
    
    # Clean up temp file
    if temp_extracted.exists():
        temp_extracted.unlink()
    
    print("\n✓ Complete!")
    print(f"  Layout preserved from: {drawio_path}")
    print(f"  Scanner stories moved to Code Scanner increment")
    print(f"  Scanner stories removed from epics section")
    print(f"  Updated: {story_graph_path}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

