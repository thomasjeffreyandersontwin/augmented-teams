import os
import re
from pathlib import Path

# Find all Python files in agile_bot/src/actions subfolders (not actions/ itself)
actions_subfolders = [
    Path('agile_bot/src/actions/build'),
    Path('agile_bot/src/actions/clarify'),
    Path('agile_bot/src/actions/render'),
    Path('agile_bot/src/actions/strategy'),
    Path('agile_bot/src/actions/validate'),
]

all_files = []
for folder in actions_subfolders:
    if folder.exists():
        all_files.extend(list(folder.glob('*.py')))

# Fix imports - from actions subfolders, need 3 dots to reach src/
fixes = [
    (r'from \.\.utils import', 'from ...utils import'),
    (r'from \.\.bot_path import', 'from ...bot_path import'),
]

for file_path in all_files:
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
