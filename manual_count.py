import json
from pathlib import Path

def extract_stories(data, epic_name="", sub_epic_name="", sub_epic_test_file=""):
    """Recursively extract all stories from epics and sub_epics."""
    stories_without_tests = []
    stories_with_tests = []
    
    # Handle top-level epics
    if 'epics' in data:
        for epic in data['epics']:
            epic_name = epic.get('name', '')
            for sub_epic in epic.get('sub_epics', []):
                sub_epic_name = sub_epic.get('name', '')
                sub_epic_test_file = sub_epic.get('test_file', '')
                
                # Process story_groups
                for story_group in sub_epic.get('story_groups', []):
                    for story in story_group.get('stories', []):
                        story_name = story.get('name', '')
                        story_test_file = story.get('test_file', '')
                        
                        # Check if story has test_file (either on story or sub_epic)
                        has_test_file = bool(story_test_file or sub_epic_test_file)
                        
                        # Check if story has scenarios with test_method
                        has_test_methods = any(sc.get('test_method') for sc in story.get('scenarios', []))
                        
                        # Story has tests if it has either test_file or test_methods
                        has_tests = has_test_file or has_test_methods
                        
                        story_info = (epic_name, sub_epic_name, story_name, has_tests)
                        
                        if has_tests:
                            stories_with_tests.append(story_info)
                        else:
                            stories_without_tests.append(story_info)
                
                # Handle nested sub_epics (recursive)
                if sub_epic.get('sub_epics'):
                    nested_no_test, nested_with_test = extract_stories(
                        {'epics': [{'sub_epics': sub_epic.get('sub_epics', [])}]},
                        epic_name,
                        sub_epic_name,
                        sub_epic_test_file
                    )
                    stories_without_tests.extend(nested_no_test)
                    stories_with_tests.extend(nested_with_test)
    
    return stories_without_tests, stories_with_tests

story_graph_path = Path('agile_bot/bots/base_bot/docs/stories/story-graph.json')

with open(story_graph_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

stories_without_tests, stories_with_tests = extract_stories(data)

# Write results
with open('manual_count_result.txt', 'w', encoding='utf-8') as f:
    f.write(f"Total stories: {len(stories_without_tests) + len(stories_with_tests)}\n")
    f.write(f"Stories WITH tests: {len(stories_with_tests)}\n")
    f.write(f"Stories WITHOUT tests: {len(stories_without_tests)}\n")
    f.write(f"\nCoverage: {len(stories_with_tests) / (len(stories_without_tests) + len(stories_with_tests)) * 100:.1f}%\n")
    f.write("\n" + "="*80 + "\n")
    f.write("STORIES WITHOUT TESTS:\n")
    f.write("="*80 + "\n\n")
    
    for epic, sub_epic, story, _ in stories_without_tests:
        f.write(f"{story}\n")
        f.write(f"  Epic: {epic}\n")
        f.write(f"  Sub-Epic: {sub_epic}\n\n")

print(f"Total stories: {len(stories_without_tests) + len(stories_with_tests)}")
print(f"Stories WITH tests: {len(stories_with_tests)}")
print(f"Stories WITHOUT tests: {len(stories_without_tests)}")
print(f"\nResults written to manual_count_result.txt")
