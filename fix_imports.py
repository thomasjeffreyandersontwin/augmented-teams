import os
import re
from pathlib import Path

# Find all Python files in agile_bot/src and agile_bot/test
src_files = list(Path('agile_bot/src').rglob('*.py'))
test_files = list(Path('agile_bot/test').rglob('*.py'))

all_files = src_files + test_files

replacements = [
    (r'from agile_bot\.bots\.base_bot\.src\.', 'from agile_bot.src.'),
    (r'from agile_bot\.bots\.base_bot\.test\.', 'from agile_bot.test.'),
    (r'import agile_bot\.bots\.base_bot\.src\.', 'import agile_bot.src.'),
    (r'import agile_bot\.bots\.base_bot\.test\.', 'import agile_bot.test.'),
]

for file_path in all_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        for pattern, replacement in replacements:
            content = re.sub(pattern, replacement, content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated: {file_path}')
    except Exception as e:
        print(f'Error processing {file_path}: {e}')

print('Done!')
