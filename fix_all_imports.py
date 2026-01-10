import os
import re
from pathlib import Path

# Find all Python files in agile_bot/src
src_files = list(Path('agile_bot/src').rglob('*.py'))

# Common import fixes
fixes = [
    # Fix story_graph imports
    (r'from \.\.\.bot_path import', 'from ..bot_path import'),
    (r'from \.\.\.utils import', 'from ..utils import'),
    (r'from \.\.\.story_graph import', 'from ..story_graph import'),
    
    # Fix actions imports
    (r'from \.\.\.actions\.validate\.story_graph import', 'from ...story_graph.story_graph import'),
    
    # Fix bot imports
    (r'from \.bot\.reminders import', 'from ..instructions.reminders import'),
    (r'from \.\.bot\.reminders import', 'from ..instructions.reminders import'),
    
    # Fix instructions imports
    (r'from \.instructions import Instructions', 'from ..instructions.instructions import Instructions'),
]

for file_path in src_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        for pattern, replacement in fixes:
            content = re.sub(pattern, replacement, content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated: {file_path}')
    except Exception as e:
        print(f'Error processing {file_path}: {e}')

print('Done!')
