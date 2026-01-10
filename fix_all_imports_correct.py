import os
import re
from pathlib import Path

# Current structure:
# agile_bot/src/utils.py (file)
# agile_bot/src/bot_path/ (folder)
# agile_bot/src/actions/ (folder)
#   - Files directly in actions/ need TWO dots (..utils, ..bot_path)
#   - Files in actions/build/, actions/validate/, etc. need THREE dots (...utils, ...bot_path)

# Fix files in actions/ root (two dots)
actions_root_files = list(Path('agile_bot/src/actions').glob('*.py'))
for file_path in actions_root_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        # These files are directly in actions/, so they need TWO dots to reach src/
        content = re.sub(r'from \.\.\.utils import', 'from ..utils import', content)
        content = re.sub(r'from \.\.\.bot_path import', 'from ..bot_path import', content)
        content = re.sub(r'from \.\.\.story_graph', 'from ..story_graph', content)
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Fixed (root): {file_path}')
    except Exception as e:
        print(f'Error: {file_path}: {e}')

# Fix files in actions/ subfolders (three dots)
subfolder_patterns = [
    'agile_bot/src/actions/build/*.py',
    'agile_bot/src/actions/clarify/*.py',
    'agile_bot/src/actions/render/*.py',
    'agile_bot/src/actions/strategy/*.py',
    'agile_bot/src/actions/validate/*.py',
]

for pattern in subfolder_patterns:
    for file_path in Path('.').glob(pattern):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            # These files are in subfolders, so they need THREE dots to reach src/
            content = re.sub(r'from \.\.utils import', 'from ...utils import', content)
            content = re.sub(r'from \.\.bot_path import', 'from ...bot_path import', content)
            content = re.sub(r'from \.\.story_graph', 'from ...story_graph', content)
            
            if content != original:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f'Fixed (subfolder): {file_path}')
        except Exception as e:
            print(f'Error: {file_path}: {e}')

print('Done fixing imports!')
