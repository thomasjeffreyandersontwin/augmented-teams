"""
Comprehensive project scope summary showing story-test mapping status.
"""
import json
from pathlib import Path
from collections import defaultdict

# Read story graph
story_graph = json.loads(Path('agile_bot/bots/base_bot/docs/stories/story-graph.json').read_text(encoding='utf-8'))

def analyze_stories(obj, results):
    """Recursively analyze all stories in the graph."""
    if isinstance(obj, dict):
        # Check if this is a story
        if 'name' in obj and obj.get('story_type') in ['user', 'system']:
            story_name = obj.get('name')
            test_file = obj.get('test_file')
            test_class = obj.get('test_class')
            scenarios = obj.get('scenarios', [])
            
            results['total_stories'] += 1
            
            if test_file:
                results['with_test_file'] += 1
                results['by_test_file'][test_file].append({
                    'name': story_name,
                    'test_class': test_class,
                    'scenario_count': len(scenarios)
                })
            
            if test_class:
                results['with_test_class'] += 1
            
            if scenarios:
                results['with_scenarios'] += 1
                results['total_scenarios'] += len(scenarios)
            else:
                if test_file:
                    results['missing_scenarios'].append({
                        'name': story_name,
                        'test_file': test_file,
                        'test_class': test_class
                    })
                else:
                    results['no_tests'].append(story_name)
        
        # Recurse through all dict values
        for value in obj.values():
            analyze_stories(value, results)
            
    elif isinstance(obj, list):
        for item in obj:
            analyze_stories(item, results)

# Analyze
results = {
    'total_stories': 0,
    'with_test_file': 0,
    'with_test_class': 0,
    'with_scenarios': 0,
    'total_scenarios': 0,
    'by_test_file': defaultdict(list),
    'missing_scenarios': [],
    'no_tests': []
}

analyze_stories(story_graph, results)

# Display results
print('=' * 80)
print('PROJECT SCOPE: STORY-TEST MAPPING STATUS')
print('=' * 80)
print()
print('OVERALL STATISTICS')
print('-' * 80)
print(f'Total Stories:                  {results["total_stories"]:>4}')
print(f'Stories with Test File:         {results["with_test_file"]:>4}  ({100*results["with_test_file"]//results["total_stories"]:>3}%)')
print(f'Stories with Test Class:        {results["with_test_class"]:>4}  ({100*results["with_test_class"]//results["total_stories"]:>3}%)')
print(f'Stories with Scenarios:         {results["with_scenarios"]:>4}  ({100*results["with_scenarios"]//results["total_stories"]:>3}%)')
print(f'Total Scenarios Documented:     {results["total_scenarios"]:>4}')
print()
print(f'Stories Missing Scenarios:      {len(results["missing_scenarios"]):>4}  (have tests, need scenarios)')
print(f'Stories Without Tests:          {len(results["no_tests"]):>4}  (need test implementation)')
print()

# Show breakdown by test file
print('=' * 80)
print('BREAKDOWN BY TEST FILE')
print('=' * 80)
test_files = sorted(results['by_test_file'].items(), key=lambda x: -len(x[1]))
for test_file, stories in test_files:
    total_scenarios = sum(s['scenario_count'] for s in stories)
    stories_with_scenarios = sum(1 for s in stories if s['scenario_count'] > 0)
    print(f'\n{test_file}')
    print(f'  Stories: {len(stories):>2}  |  With Scenarios: {stories_with_scenarios:>2}/{len(stories):>2}  |  Total Scenarios: {total_scenarios:>3}')

# Show stories missing scenarios (have tests but no scenarios yet)
if results['missing_scenarios']:
    print()
    print('=' * 80)
    print(f'STORIES WITH TESTS BUT MISSING SCENARIOS ({len(results["missing_scenarios"])})')
    print('=' * 80)
    for story in results['missing_scenarios'][:10]:  # Show first 10
        print(f'  - {story["name"]}')
        print(f'    Test: {story["test_file"]} :: {story["test_class"] or "No class"}')
    if len(results['missing_scenarios']) > 10:
        print(f'\n  ... and {len(results["missing_scenarios"]) - 10} more')

# Show stories without tests
if results['no_tests']:
    print()
    print('=' * 80)
    print(f'STORIES WITHOUT TEST IMPLEMENTATION ({len(results["no_tests"])})')
    print('=' * 80)
    for story_name in results['no_tests'][:10]:  # Show first 10
        print(f'  - {story_name}')
    if len(results['no_tests']) > 10:
        print(f'\n  ... and {len(results["no_tests"]) - 10} more')

print()
print('=' * 80)
print(f'TEST COVERAGE: {results["with_scenarios"]}/{results["total_stories"]} stories ({100*results["with_scenarios"]//results["total_stories"]}%)')
print('=' * 80)
