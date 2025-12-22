import json

# Read the story graph
with open('agile_bot/bots/base_bot/docs/stories/story-graph.json', 'r', encoding='utf-8') as f:
    story_graph = json.load(f)

# Extract all story names from epics - more thorough check
all_stories_in_epics = set()
story_locations = {}

for epic_idx, epic in enumerate(story_graph.get('epics', [])):
    epic_name = epic.get('name', f'Epic {epic_idx}')
    
    # Check sub_epics
    for sub_epic_idx, sub_epic in enumerate(epic.get('sub_epics', [])):
        sub_epic_name = sub_epic.get('name', f'SubEpic {sub_epic_idx}')
        
        for story_group_idx, story_group in enumerate(sub_epic.get('story_groups', [])):
            for story_idx, story in enumerate(story_group.get('stories', [])):
                story_name = story.get('name', '')
                if story_name:
                    all_stories_in_epics.add(story_name)
                    story_locations[story_name] = f"{epic_name} -> {sub_epic_name}"

# Check a few specific stories
test_stories = [
    "Inject Knowledge Graph Template and Builder Instructions",
    "Load Story Graph Into Memory",
    "Generate Base Action Node",
    "Complete Validate Rules Action"
]

print("Checking if test stories exist in epics:")
for test_story in test_stories:
    if test_story in all_stories_in_epics:
        print(f"  [OK] {test_story} - Found at: {story_locations.get(test_story, 'Unknown')}")
    else:
        print(f"  [NOT FOUND] {test_story}")

print(f"\nTotal stories found in epics: {len(all_stories_in_epics)}")
print("\nFirst 10 stories:")
for story in sorted(list(all_stories_in_epics))[:10]:
    print(f"  - {story}")

