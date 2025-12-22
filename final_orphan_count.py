import json

# Read the story graph
with open('agile_bot/bots/base_bot/docs/stories/story-graph.json', 'r', encoding='utf-8') as f:
    story_graph = json.load(f)

# Extract all story names from epics - check all possible locations
all_stories_in_epics = set()

for epic in story_graph.get('epics', []):
    # Check sub_epics
    for sub_epic in epic.get('sub_epics', []):
        # Check story_groups in sub_epic
        for story_group in sub_epic.get('story_groups', []):
            for story in story_group.get('stories', []):
                story_name = story.get('name', '')
                if story_name:
                    all_stories_in_epics.add(story_name)
    
    # Also check if epic has direct story_groups (though unlikely)
    for story_group in epic.get('story_groups', []):
        for story in story_group.get('stories', []):
            story_name = story.get('name', '')
            if story_name:
                all_stories_in_epics.add(story_name)

# Extract all story names from increments
all_stories_in_increments = set()
for increment in story_graph.get('increments', []):
    for story in increment.get('stories', []):
        if story and story.strip():
            all_stories_in_increments.add(story.strip())

# Find orphaned stories (in epics but not in increments)
orphaned_stories = all_stories_in_epics - all_stories_in_increments

print(f"Total stories in epics: {len(all_stories_in_epics)}")
print(f"Total stories in increments: {len(all_stories_in_increments)}")
print(f"\nOrphaned stories (in epics but NOT in any increment): {len(orphaned_stories)}")

if orphaned_stories:
    print("\nOrphaned story names:")
    for story in sorted(orphaned_stories):
        print(f"  - {story}")

# Verify a few key stories exist
test_stories = [
    "Inject Knowledge Graph Template and Builder Instructions",
    "Load Story Graph Into Memory", 
    "Generate Base Action Node"
]
print("\nVerification - checking if these stories are in epics:")
for test_story in test_stories:
    status = "[FOUND]" if test_story in all_stories_in_epics else "[NOT FOUND]"
    print(f"  {status} {test_story}")

