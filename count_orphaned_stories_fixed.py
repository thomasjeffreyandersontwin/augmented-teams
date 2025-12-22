import json

# Read the story graph
with open('agile_bot/bots/base_bot/docs/stories/story-graph.json', 'r', encoding='utf-8') as f:
    story_graph = json.load(f)

# Extract all story names from epics - check both sub_epics and direct story_groups
all_stories_in_epics = set()
for epic in story_graph.get('epics', []):
    # Check sub_epics
    for sub_epic in epic.get('sub_epics', []):
        for story_group in sub_epic.get('story_groups', []):
            for story in story_group.get('stories', []):
                story_name = story.get('name', '')
                if story_name:
                    all_stories_in_epics.add(story_name)
    
    # Also check if epic has direct story_groups (though unlikely based on structure)
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

# Find invalid stories (in increments but not in epics)
invalid_stories = all_stories_in_increments - all_stories_in_epics

print(f"Total stories in epics: {len(all_stories_in_epics)}")
print(f"Total stories in increments: {len(all_stories_in_increments)}")
print(f"\nOrphaned stories (in epics but NOT in any increment): {len(orphaned_stories)}")

if orphaned_stories:
    print("\n=== ORPHANED STORIES ===")
    for story in sorted(orphaned_stories):
        print(f"  - {story}")

if invalid_stories:
    print(f"\nInvalid stories (in increments but NOT in epics): {len(invalid_stories)}")
    print("(These should be removed from increments)")
    for story in sorted(invalid_stories):
        print(f"  - {story}")

