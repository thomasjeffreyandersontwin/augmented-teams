#!/usr/bin/env python3
"""Analyze files that might be slowing down Cursor indexing."""
import os
from pathlib import Path
from collections import Counter, defaultdict
import json

# Directories to exclude from analysis (already typically excluded)
EXCLUDE_DIRS = {
    '.git', '__pycache__', '.pytest_cache', 'node_modules', 
    '.venv', 'venv', 'env', 'dist', 'build', '.cache', 'cache'
}

def should_exclude(path_str):
    """Check if path should be excluded."""
    parts = Path(path_str).parts
    return any(part in EXCLUDE_DIRS for part in parts)

def analyze_codebase(root_path='.'):
    """Analyze codebase for indexing performance issues."""
    root = Path(root_path)
    
    # Count files by directory
    dir_counts = defaultdict(int)
    file_exts = Counter()
    large_files = []
    log_files = []
    json_files = []
    total_files = 0
    
    print("Scanning files...")
    for file_path in root.rglob('*'):
        if not file_path.is_file():
            continue
            
        path_str = str(file_path)
        
        # Skip excluded directories
        if should_exclude(path_str):
            continue
            
        total_files += 1
        size = file_path.stat().st_size
        
        # Track by directory
        dir_counts[str(file_path.parent)] += 1
        
        # Track by extension
        ext = file_path.suffix or '(no ext)'
        file_exts[ext] += 1
        
        # Track large files (>1MB)
        if size > 1024 * 1024:
            large_files.append((size, path_str))
        
        # Track log files
        if ext == '.log' or 'log' in file_path.name.lower():
            log_files.append((size, path_str))
        
        # Track JSON files (might be large configs)
        if ext == '.json':
            json_files.append((size, path_str))
    
    # Sort results
    large_files.sort(reverse=True)
    log_files.sort(reverse=True)
    json_files.sort(reverse=True)
    
    print(f"\n{'='*80}")
    print(f"ANALYSIS COMPLETE")
    print(f"{'='*80}\n")
    
    print(f"Total files scanned: {total_files:,}\n")
    
    # Top directories by file count
    print(f"{'='*80}")
    print("TOP 20 DIRECTORIES BY FILE COUNT:")
    print(f"{'='*80}")
    for path, count in sorted(dir_counts.items(), key=lambda x: x[1], reverse=True)[:20]:
        print(f"{count:6d} files  {path}")
    
    # File extensions
    print(f"\n{'='*80}")
    print("FILE EXTENSIONS BY COUNT:")
    print(f"{'='*80}")
    for ext, count in file_exts.most_common(20):
        print(f"{count:6d}  {ext}")
    
    # Large files
    print(f"\n{'='*80}")
    print(f"LARGE FILES (>1MB): {len(large_files)} found")
    print(f"{'='*80}")
    for size, path in large_files[:20]:
        size_mb = size / (1024 * 1024)
        print(f"{size_mb:8.2f} MB  {path}")
    
    # Log files
    print(f"\n{'='*80}")
    print(f"LOG FILES: {len(log_files)} found")
    print(f"{'='*80}")
    for size, path in log_files[:20]:
        size_kb = size / 1024
        print(f"{size_kb:8.2f} KB  {path}")
    
    # Large JSON files
    print(f"\n{'='*80}")
    print(f"LARGE JSON FILES (>100KB): {len([f for f in json_files if f[0] > 100*1024])} found")
    print(f"{'='*80}")
    large_json = [f for f in json_files if f[0] > 100*1024]
    for size, path in large_json[:20]:
        size_kb = size / 1024
        print(f"{size_kb:8.2f} KB  {path}")
    
    return {
        'total_files': total_files,
        'top_dirs': dict(sorted(dir_counts.items(), key=lambda x: x[1], reverse=True)[:20]),
        'file_exts': dict(file_exts.most_common(20)),
        'large_files': [(size, path) for size, path in large_files],
        'log_files': [(size, path) for size, path in log_files],
    }

if __name__ == '__main__':
    analyze_codebase()
