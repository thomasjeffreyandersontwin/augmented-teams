import json
import re

# Read the story graph
with open('agile_bot/bots/base_bot/docs/stories/story-graph.json', 'r', encoding='utf-8') as f:
    story_graph = json.load(f)

# Read the increments file
with open('agile_bot/bots/base_bot/docs/stories/increments/story-map-increments.txt', 'r', encoding='utf-8') as f:
    increments_text = f.read()

# Extract all story names from epics
all_stories = {}
for epic in story_graph.get('epics', []):
    for sub_epic in epic.get('sub_epics', []):
        for story_group in sub_epic.get('story_groups', []):
            for story in story_group.get('stories', []):
                story_name = story.get('name', '')
                if story_name:
                    all_stories[story_name] = story

print("=== ALL STORIES IN EPICS ===")
for name in sorted(all_stories.keys()):
    print(name)
print(f"\nTotal stories in epics: {len(all_stories)}\n")

# Parse increments from text
increments_map = {}
current_increment = None
current_epic = None
current_sub_epic = None

for line in increments_text.split('\n'):
    line = line.strip()
    if not line:
        continue
    
    # Check for increment header
    increment_match = re.match(r'##\s*Increment\s+(\d+):\s*(.+)', line)
    if increment_match:
        inc_num = increment_match.group(1)
        inc_name = increment_match.group(2)
        current_increment = f"Increment {inc_num}: {inc_name}"
        increments_map[current_increment] = {
            'name': inc_name,
            'priority': int(inc_num),
            'stories': []
        }
        current_epic = None
        current_sub_epic = None
        continue
    
    # Check for epic (E)
    epic_match = re.match(r'\(E\)\s+(.+)', line)
    if epic_match:
        current_epic = epic_match.group(1)
        current_sub_epic = None
        continue
    
    # Check for sub-epic (E) with indentation
    sub_epic_match = re.match(r'\s+\(E\)\s+(.+)', line)
    if sub_epic_match:
        current_sub_epic = sub_epic_match.group(1)
        continue
    
    # Check for story (S)
    story_match = re.match(r'\s+\(S\)\s+(.+)', line)
    if story_match:
        story_text = story_match.group(1)
        # Remove prefixes like "MCP Server Generator -->", "Bot Behavior -->", "System -->"
        story_name = re.sub(r'^[^>]+-->\s*', '', story_text).strip()
        
        if current_increment:
            increments_map[current_increment]['stories'].append(story_name)

print("=== STORIES FROM INCREMENTS.TXT ===")
for inc_name, inc_data in sorted(increments_map.items(), key=lambda x: x[1]['priority']):
    print(f"\n{inc_name} (Priority {inc_data['priority']}):")
    for story in inc_data['stories']:
        print(f"  - {story}")
print()

# Find stories in increments that don't exist in epics
print("=== STORIES IN INCREMENTS BUT NOT IN EPICS ===")
missing_stories = []
for inc_name, inc_data in increments_map.items():
    for story in inc_data['stories']:
        if story not in all_stories:
            missing_stories.append((inc_name, story))
            print(f"  {inc_name}: {story}")

if not missing_stories:
    print("  None!")

# Find stories in epics that aren't in any increment
print("\n=== STORIES IN EPICS BUT NOT IN ANY INCREMENT ===")
stories_in_increments = set()
for inc_data in increments_map.values():
    stories_in_increments.update(inc_data['stories'])

orphaned_stories = []
for story_name in all_stories.keys():
    if story_name not in stories_in_increments:
        orphaned_stories.append(story_name)
        print(f"  {story_name}")

if not orphaned_stories:
    print("  None!")

# Now let's try to match stories with fuzzy matching
print("\n=== FUZZY MATCHING ATTEMPTS ===")
for inc_name, inc_data in increments_map.items():
    for story in inc_data['stories']:
        if story not in all_stories:
            # Try to find similar story names
            for epic_story in all_stories.keys():
                if story.lower() in epic_story.lower() or epic_story.lower() in story.lower():
                    print(f"  '{story}' might match '{epic_story}'")

