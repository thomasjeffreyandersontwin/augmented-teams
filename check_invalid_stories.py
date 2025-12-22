import json

# Read the story graph
with open('agile_bot/bots/base_bot/docs/stories/story-graph.json', 'r', encoding='utf-8') as f:
    story_graph = json.load(f)

# Extract all story names from epics
all_stories_in_epics = set()
for epic in story_graph.get('epics', []):
    for sub_epic in epic.get('sub_epics', []):
        for story_group in sub_epic.get('story_groups', []):
            for story in story_group.get('stories', []):
                story_name = story.get('name', '')
                if story_name:
                    all_stories_in_epics.add(story_name)

# Extract all story names from increments (with duplicates tracking)
all_stories_in_increments = []
stories_in_increments_set = set()
for increment in story_graph.get('increments', []):
    for story in increment.get('stories', []):
        if story:
            all_stories_in_increments.append(story)
            stories_in_increments_set.add(story)

# Find orphaned stories (in epics but not in increments)
orphaned_stories = all_stories_in_epics - stories_in_increments_set

# Find invalid stories (in increments but not in epics)
invalid_stories = stories_in_increments_set - all_stories_in_epics

# Find duplicates in increments
from collections import Counter
story_counts = Counter(all_stories_in_increments)
duplicates = {story: count for story, count in story_counts.items() if count > 1}

print(f"Total stories in epics: {len(all_stories_in_epics)}")
print(f"Total story entries in increments: {len(all_stories_in_increments)}")
print(f"Unique stories in increments: {len(stories_in_increments_set)}")
print(f"\nOrphaned stories (in epics but NOT in any increment): {len(orphaned_stories)}")
print(f"Invalid stories (in increments but NOT in epics): {len(invalid_stories)}")
print(f"Duplicate stories in increments: {len(duplicates)}")

if orphaned_stories:
    print("\n=== ORPHANED STORIES ===")
    for story in sorted(orphaned_stories):
        print(f"  - {story}")

if invalid_stories:
    print("\n=== INVALID STORIES (in increments but not in epics) ===")
    for story in sorted(invalid_stories):
        print(f"  - {story}")

if duplicates:
    print("\n=== DUPLICATE STORIES IN INCREMENTS ===")
    for story, count in sorted(duplicates.items()):
        print(f"  - {story} (appears {count} times)")

