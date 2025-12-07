"""
Analyze story graph to find stories without tests.

A story is considered to have tests if:
1. It has a test_file field (mapping to a test file)
2. OR it has scenarios with test_method fields (mapping to test methods)
"""
import json
from pathlib import Path
from collections import defaultdict

def load_story_graph(story_graph_path):
    """Load and parse story graph JSON."""
    with open(story_graph_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_all_stories(story_graph):
    """Extract all stories from the story graph with their test mappings."""
    stories_without_tests = []
    stories_with_tests = []
    
    for epic in story_graph.get('epics', []):
        epic_name = epic.get('name', '')
        
        for sub_epic in epic.get('sub_epics', []):
            sub_epic_name = sub_epic.get('name', '')
            sub_epic_test_file = sub_epic.get('test_file', '')
            
            for story_group in sub_epic.get('story_groups', []):
                for story in story_group.get('stories', []):
                    story_name = story.get('name', '')
                    story_test_file = story.get('test_file', '')
                    
                    # Check if story has test_file
                    has_test_file = bool(story_test_file or sub_epic_test_file)
                    
                    # Check if story has scenarios with test_method
                    has_test_methods = False
                    scenarios = story.get('scenarios', [])
                    for scenario in scenarios:
                        if scenario.get('test_method'):
                            has_test_methods = True
                            break
                    
                    # Story has tests if it has either test_file or test_methods
                    has_tests = has_test_file or has_test_methods
                    
                    story_info = {
                        'epic': epic_name,
                        'sub_epic': sub_epic_name,
                        'story': story_name,
                        'story_type': story.get('story_type', 'unknown'),
                        'test_file': story_test_file or sub_epic_test_file or None,
                        'has_test_file': has_test_file,
                        'has_test_methods': has_test_methods,
                        'scenario_count': len(scenarios),
                        'scenarios_with_test_method': sum(1 for s in scenarios if s.get('test_method'))
                    }
                    
                    if has_tests:
                        stories_with_tests.append(story_info)
                    else:
                        stories_without_tests.append(story_info)
    
    return stories_without_tests, stories_with_tests

def analyze_stories():
    """Main analysis function."""
    workspace_root = Path(__file__).parent
    story_graph_path = workspace_root / 'agile_bot' / 'bots' / 'base_bot' / 'docs' / 'stories' / 'story-graph.json'
    
    if not story_graph_path.exists():
        print(f"ERROR: Story graph not found at {story_graph_path}")
        return None
    
    # Load story graph
    story_graph = load_story_graph(story_graph_path)
    stories_without_tests, stories_with_tests = extract_all_stories(story_graph)
    
    # Group by epic and sub-epic
    by_epic = defaultdict(lambda: defaultdict(list))
    for story in stories_without_tests:
        by_epic[story['epic']][story['sub_epic']].append(story)
    
    # Print results
    print("=" * 80)
    print("STORIES WITHOUT TESTS")
    print("=" * 80)
    print(f"\nTotal stories without tests: {len(stories_without_tests)}")
    print(f"Total stories with tests: {len(stories_with_tests)}")
    print(f"Total stories: {len(stories_without_tests) + len(stories_with_tests)}")
    print(f"Coverage: {len(stories_with_tests) / (len(stories_without_tests) + len(stories_with_tests)) * 100:.1f}%")
    
    print("\n" + "=" * 80)
    print("BREAKDOWN BY EPIC AND SUB-EPIC")
    print("=" * 80)
    
    for epic_name in sorted(by_epic.keys()):
        print(f"\n📚 Epic: {epic_name}")
        for sub_epic_name in sorted(by_epic[epic_name].keys()):
            stories = by_epic[epic_name][sub_epic_name]
            print(f"  📦 Sub-Epic: {sub_epic_name} ({len(stories)} stories without tests)")
            for story in stories:
                print(f"    - {story['story']} ({story['story_type']})")
                if story['scenario_count'] > 0:
                    print(f"      └─ {story['scenario_count']} scenarios, {story['scenarios_with_test_method']} with test_method")
    
    print("\n" + "=" * 80)
    print("DETAILED LIST")
    print("=" * 80)
    for story in stories_without_tests:
        print(f"\nStory: {story['story']}")
        print(f"  Epic: {story['epic']}")
        print(f"  Sub-Epic: {story['sub_epic']}")
        print(f"  Type: {story['story_type']}")
        print(f"  Test File: {story['test_file'] or 'NONE'}")
        print(f"  Scenarios: {story['scenario_count']} total, {story['scenarios_with_test_method']} with test_method")
    
    return {
        'stories_without_tests': stories_without_tests,
        'stories_with_tests': stories_with_tests,
        'total_without_tests': len(stories_without_tests),
        'total_with_tests': len(stories_with_tests),
        'total': len(stories_without_tests) + len(stories_with_tests)
    }

if __name__ == '__main__':
    import sys
    try:
        result = analyze_stories()
        if result:
            print(f"\n{'=' * 80}")
            print(f"SUMMARY: {result['total_without_tests']} stories without tests out of {result['total']} total stories")
            print("=" * 80)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

