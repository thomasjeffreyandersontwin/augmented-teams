#!/usr/bin/env python3
"""Fix scanner stories structure - add sub-epic under Validate and ensure they're in epics."""

import sys
from pathlib import Path
import json

def main():
    stories_dir = Path(__file__).parent
    story_graph_path = stories_dir / "story-graph.json"
    
    # Load current story graph
    print(f"Loading story graph from {story_graph_path}")
    with open(story_graph_path, 'r', encoding='utf-8') as f:
        story_graph = json.load(f)
    
    # Scanner stories that need to be in sub-epic structure
    scanner_stories = [
        {
            "name": "System Discovers Scanners from rule.json",
            "sequential_order": 1,
            "connector": "and",
            "users": ["Bot Behavior"],
            "story_type": "user"
        },
        {
            "name": "System Loads Scanner Classes",
            "sequential_order": 2,
            "connector": "and",
            "users": ["Bot Behavior"],
            "story_type": "user"
        },
        {
            "name": "System Runs Scanners After Build Knowledge",
            "sequential_order": 1,
            "connector": "and",
            "users": ["Bot Behavior"],
            "story_type": "user"
        },
        {
            "name": "System Runs Scanners After Render Output",
            "sequential_order": 2,
            "connector": "and",
            "users": ["Bot Behavior"],
            "story_type": "user"
        },
        {
            "name": "System Runs Scanners Before AI Validation",
            "sequential_order": 3,
            "connector": "and",
            "users": ["Bot Behavior"],
            "story_type": "user"
        },
        {
            "name": "Scanner Detects Violations Using Regex Patterns",
            "sequential_order": 1,
            "connector": "and",
            "users": ["Bot Behavior"],
            "story_type": "user"
        },
        {
            "name": "Scanner Detects Violations Using AST Parsing",
            "sequential_order": 2,
            "connector": "and",
            "users": ["Bot Behavior"],
            "story_type": "user"
        },
        {
            "name": "Scanner Detects Violations Using File Structure Analysis",
            "sequential_order": 3,
            "connector": "and",
            "users": ["Bot Behavior"],
            "story_type": "user"
        },
        {
            "name": "System Collects Violations from All Scanners",
            "sequential_order": 1,
            "connector": "and",
            "users": ["Bot Behavior"],
            "story_type": "user"
        },
        {
            "name": "System Reports Violations with Location Context",
            "sequential_order": 2,
            "connector": "and",
            "users": ["Bot Behavior"],
            "story_type": "user"
        }
    ]
    
    # Find Validate Knowledge & Content Against Rules in epics
    print("\nAdding scanner stories to epics section with sub-epic structure...")
    for epic in story_graph.get("epics", []):
        if epic.get("name") == "Execute Behavior Actions":
            for sub_epic in epic.get("sub_epics", []):
                if sub_epic.get("name") == "Validate Knowledge & Content Against Rules":
                    # Check if sub-epic already exists
                    scanner_sub_epic = None
                    for sub_sub_epic in sub_epic.get("sub_epics", []):
                        if sub_sub_epic.get("name") == "Integrate Code Scanners into Validation Workflow":
                            scanner_sub_epic = sub_sub_epic
                            break
                    
                    if not scanner_sub_epic:
                        # Create the sub-epic structure
                        print("  Creating 'Integrate Code Scanners into Validation Workflow' sub-epic...")
                        scanner_sub_epic = {
                            "name": "Integrate Code Scanners into Validation Workflow",
                            "sequential_order": 1,
                            "sub_epics": [
                                {
                                    "name": "Register and Load Code Scanners",
                                    "sequential_order": 1,
                                    "sub_epics": [],
                                    "stories": [
                                        scanner_stories[0],  # System Discovers Scanners
                                        scanner_stories[1]   # System Loads Scanner Classes
                                    ]
                                },
                                {
                                    "name": "Execute Code Scanners",
                                    "sequential_order": 2,
                                    "sub_epics": [],
                                    "stories": [
                                        scanner_stories[2],  # System Runs Scanners After Build Knowledge
                                        scanner_stories[3],  # System Runs Scanners After Render Output
                                        scanner_stories[4]   # System Runs Scanners Before AI Validation
                                    ]
                                },
                                {
                                    "name": "Detect Violations",
                                    "sequential_order": 3,
                                    "sub_epics": [],
                                    "stories": [
                                        scanner_stories[5],  # Scanner Detects Violations Using Regex Patterns
                                        scanner_stories[6],  # Scanner Detects Violations Using AST Parsing
                                        scanner_stories[7]   # Scanner Detects Violations Using File Structure Analysis
                                    ]
                                },
                                {
                                    "name": "Collect and Report Violations",
                                    "sequential_order": 4,
                                    "sub_epics": [],
                                    "stories": [
                                        scanner_stories[8],  # System Collects Violations from All Scanners
                                        scanner_stories[9]   # System Reports Violations with Location Context
                                    ]
                                }
                            ]
                        }
                        if "sub_epics" not in sub_epic:
                            sub_epic["sub_epics"] = []
                        sub_epic["sub_epics"].append(scanner_sub_epic)
                        print("  ✓ Added scanner sub-epic structure to epics")
                    else:
                        print("  Sub-epic already exists in epics")
                    break
    
    # Update Code Scanner increment to reference the sub-epic structure
    print("\nUpdating Code Scanner increment to use sub-epic structure...")
    for increment in story_graph.get("increments", []):
        if increment.get("name") == "Code Scanner":
            for epic in increment.get("epics", []):
                if epic.get("name") == "Execute Behavior Actions":
                    for sub_epic in epic.get("sub_epics", []):
                        if sub_epic.get("name") == "Validate Knowledge & Content Against Rules":
                            # Replace story_groups with sub_epics structure
                            print("  Updating Code Scanner increment structure...")
                            sub_epic["sub_epics"] = [
                                {
                                    "name": "Integrate Code Scanners into Validation Workflow",
                                    "sequential_order": 1,
                                    "sub_epics": [
                                        {
                                            "name": "Register and Load Code Scanners",
                                            "sequential_order": 1,
                                            "sub_epics": [],
                                            "stories": [
                                                scanner_stories[0],
                                                scanner_stories[1]
                                            ]
                                        },
                                        {
                                            "name": "Execute Code Scanners",
                                            "sequential_order": 2,
                                            "sub_epics": [],
                                            "stories": [
                                                scanner_stories[2],
                                                scanner_stories[3],
                                                scanner_stories[4]
                                            ]
                                        },
                                        {
                                            "name": "Detect Violations",
                                            "sequential_order": 3,
                                            "sub_epics": [],
                                            "stories": [
                                                scanner_stories[5],
                                                scanner_stories[6],
                                                scanner_stories[7]
                                            ]
                                        },
                                        {
                                            "name": "Collect and Report Violations",
                                            "sequential_order": 4,
                                            "sub_epics": [],
                                            "stories": [
                                                scanner_stories[8],
                                                scanner_stories[9]
                                            ]
                                        }
                                    ]
                                }
                            ]
                            # Remove story_groups if it exists
                            if "story_groups" in sub_epic:
                                del sub_epic["story_groups"]
                            print("  ✓ Updated Code Scanner increment structure")
                            break
    
    # Verify scanner stories are NOT in other increments
    print("\nVerifying scanner stories are only in Code Scanner increment...")
    scanner_story_names = [s["name"] for s in scanner_stories]
    for increment in story_graph.get("increments", []):
        if increment.get("name") != "Code Scanner":
            for epic in increment.get("epics", []):
                for sub_epic in epic.get("sub_epics", []):
                    # Check story_groups
                    for story_group in sub_epic.get("story_groups", []):
                        for story in story_group.get("stories", []):
                            if story.get("name") in scanner_story_names:
                                print(f"  WARNING: {story.get('name')} found in {increment.get('name')} increment!")
                    # Check direct stories
                    for story in sub_epic.get("stories", []):
                        if story.get("name") in scanner_story_names:
                            print(f"  WARNING: {story.get('name')} found in {increment.get('name')} increment!")
                    # Check sub_epics
                    for sub_sub_epic in sub_epic.get("sub_epics", []):
                        for story in sub_sub_epic.get("stories", []):
                            if story.get("name") in scanner_story_names:
                                print(f"  WARNING: {story.get('name')} found in {increment.get('name')} increment!")
    
    # Save updated story graph
    print(f"\nSaving updated story graph to: {story_graph_path}")
    with open(story_graph_path, 'w', encoding='utf-8') as f:
        json.dump(story_graph, f, indent=2, ensure_ascii=False)
    
    print("\n✓ Complete!")
    print("  Scanner stories added to epics with sub-epic structure")
    print("  Code Scanner increment updated to use sub-epic structure")
    print("  Scanner stories verified to be only in Code Scanner increment")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

