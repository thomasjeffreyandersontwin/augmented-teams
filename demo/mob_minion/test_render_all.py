"""Test all render configurations."""
import sys
from pathlib import Path

# Add story_bot src to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'agile_bot' / 'bots' / 'story_bot' / 'src'))

project_path = Path(__file__).parent
story_graph_path = project_path / 'docs' / 'stories' / 'story-graph.json'

print("Testing all render configurations...\n")

# 1. Domain Model Description Synchronizer
print("1. Testing DomainModelDescriptionSynchronizer...")
from synchronizers.domain_model import DomainModelDescriptionSynchronizer
sync1 = DomainModelDescriptionSynchronizer()
result1 = sync1.render(
    str(story_graph_path),
    str(project_path / 'docs' / 'stories' / 'mob-minion-domain-model-description.md'),
    project_path=str(project_path)
)
print(f"   Generated: {result1['output_path']}")

# 2. Domain Model Diagram Synchronizer
print("\n2. Testing DomainModelDiagramSynchronizer...")
from synchronizers.domain_model import DomainModelDiagramSynchronizer
sync2 = DomainModelDiagramSynchronizer()
result2 = sync2.render(
    str(story_graph_path),
    str(project_path / 'docs' / 'stories' / 'mob-minion-domain-model-diagram.md'),
    project_path=str(project_path)
)
print(f"   Generated: {result2['output_path']}")

# 3. Domain Model Outline Synchronizer
print("\n3. Testing DomainModelOutlineSynchronizer...")
from synchronizers.domain_model import DomainModelOutlineSynchronizer
sync3 = DomainModelOutlineSynchronizer()
result3 = sync3.render(
    str(story_graph_path),
    str(project_path / 'src' / 'domain_outline.md'),
    project_path=str(project_path)
)
print(f"   Generated: {result3['output_path']}")

# 4. Story Map Builder Script
print("\n4. Testing render_story_map_txt.py builder...")
import subprocess
builder_script = Path(__file__).parent.parent.parent / 'agile_bot' / 'bots' / 'story_bot' / 'behaviors' / 'shape' / 'content' / 'render' / 'templates' / 'render_story_map_txt.py'
result4 = subprocess.run([
    'python', str(builder_script),
    str(story_graph_path),
    str(project_path / 'docs' / 'stories' / 'story-map.txt')
], capture_output=True, text=True)
if result4.returncode == 0:
    print(f"   Generated: {project_path / 'docs' / 'stories' / 'story-map.txt'}")
else:
    print(f"   Error: {result4.stderr}")

# 5. DrawIO Synchronizer
print("\n5. Testing DrawIOSynchronizer...")
from synchronizers.story_io import DrawIOSynchronizer
sync5 = DrawIOSynchronizer()
result5 = sync5.render(
    str(story_graph_path),
    str(project_path / 'docs' / 'stories' / 'story-map-outline.drawio'),
    renderer_command='render-outline',
    force_outline=True
)
print(f"   Generated: {result5['output_path']}")

print("\nAll render configurations executed successfully!")















