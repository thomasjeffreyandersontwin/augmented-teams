def behavior_sync(feature=None):
    """
    Sync feature-local AI behaviors from features/*/cursor/ folders.
    
    Sync Rules:
    1. All files in features/*/cursor/ folders are synced
    2. Files are routed to .cursor/ correct areas based on extension:
       - .mdc files → .cursor/rules/
       - .md files  → .cursor/commands/
       - .py files  → commands/ (root level, NOT .cursor/commands/)
       - .json files → .cursor/mcp/
    3. Merge MCP configs (*-mcp.json) if they already exist
    4. Overwrite only if the source is newer
    5. Log synced and merged files
    6. Never sync behaviors marked as "draft" or "experimental"
    """
    from pathlib import Path
    import shutil
    import json

    src_root = Path("features")
    # File extension to target directory mapping
    # NOTE: .py files go to root-level commands/, not .cursor/commands/
    targets = {
        ".mdc": Path(".cursor/rules"),      # Rules → .cursor/rules/
        ".md": Path(".cursor/commands"),     # Commands → .cursor/commands/
        ".py": Path("commands"),             # Python files → commands/ (root)
        ".json": Path(".cursor/mcp"),        # MCP configs → .cursor/mcp/
    }

    # Create target directories
    for t in targets.values():
        t.mkdir(parents=True, exist_ok=True)
    
    # Ensure .vscode directory exists for tasks.json merging
    Path(".vscode").mkdir(parents=True, exist_ok=True)

    # Determine features to sync
    if feature:
        cursor_path = src_root / feature / "cursor"
        features = [cursor_path] if cursor_path.exists() else []
    else:
        features = [p for p in src_root.glob("*/cursor") if p.is_dir()]

    synced_files = []
    merged_files = []
    skipped_files = []
    
    # Collect tasks.json files from features for merging
    feature_tasks_files = []

    for cursor_path in features:
        for file in cursor_path.rglob("*"):
            # Skip directories
            if file.is_dir():
                continue
            
            # Skip draft or experimental behaviors
            content = file.read_text(encoding='utf-8', errors='ignore')
            content_lower = content.lower()
            # Check for draft/experimental markers at start of file or start of lines
            # This avoids false positives from code that checks for these markers
            lines = content_lower.split('\n')
            has_draft_marker = False
            for line in lines[:10]:  # Check first 10 lines for markers
                stripped = line.strip()
                if stripped.startswith('#draft') or stripped.startswith('#experimental'):
                    has_draft_marker = True
                    break
                if stripped.startswith('draft:') or stripped.startswith('experimental:'):
                    has_draft_marker = True
                    break
            
            if has_draft_marker:
                skipped_files.append((file, "draft/experimental marker"))
                continue

            ext = file.suffix
            if ext not in targets:
                continue

            dest = targets[ext] / file.name
            
            # Handle MCP JSON configs - merge if exists (always merge, regardless of timestamp)
            if ext == ".json" and dest.exists() and file.name.endswith("-mcp.json"):
                try:
                    with open(dest, 'r', encoding='utf-8') as d1, open(file, 'r', encoding='utf-8') as d2:
                        existing = json.load(d1)
                        new_data = json.load(d2)
                        merged = {**existing, **new_data}
                    with open(dest, 'w', encoding='utf-8') as out:
                        json.dump(merged, out, indent=2, ensure_ascii=False)
                    merged_files.append((file, dest))
                    print(f"🔄 Merged {file.name} → {dest}")
                except (json.JSONDecodeError, Exception) as e:
                    print(f"⚠️  Error merging {file.name}: {e}")
                    skipped_files.append((file, f"merge error: {e}"))
            else:
                # For non-MCP files, check if source is newer (only overwrite if newer)
                if dest.exists():
                    source_mtime = file.stat().st_mtime
                    dest_mtime = dest.stat().st_mtime
                    if source_mtime <= dest_mtime:
                        skipped_files.append((file, "source not newer"))
                        continue
                
                # Copy file
                try:
                    shutil.copy2(file, dest)
                    synced_files.append((file, dest))
                    print(f"✅ Synced {file.name} → {dest}")
                except Exception as e:
                    print(f"❌ Error syncing {file.name}: {e}")
                    skipped_files.append((file, f"copy error: {e}"))
        
        # Look for tasks.json in feature's .vscode directory
        feature_path = cursor_path.parent
        feature_tasks = feature_path / ".vscode" / "tasks.json"
        if feature_tasks.exists():
            feature_tasks_files.append(feature_tasks)
    
    # Merge tasks.json files from all features into root .vscode/tasks.json
    if feature_tasks_files:
        root_tasks = Path(".vscode/tasks.json")
        all_tasks = []
        existing_tasks_by_label = {}
        
        # Load existing root tasks.json if it exists
        if root_tasks.exists():
            try:
                with open(root_tasks, 'r', encoding='utf-8') as f:
                    root_data = json.load(f)
                    all_tasks = root_data.get("tasks", [])
                    # Index existing tasks by label to avoid duplicates
                    existing_tasks_by_label = {task.get("label"): task for task in all_tasks}
            except (json.JSONDecodeError, Exception) as e:
                print(f"⚠️  Error reading existing tasks.json: {e}")
                all_tasks = []
        
        # Merge tasks from feature tasks.json files
        for feature_tasks_file in feature_tasks_files:
            try:
                with open(feature_tasks_file, 'r', encoding='utf-8') as f:
                    feature_data = json.load(f)
                    feature_tasks = feature_data.get("tasks", [])
                    
                    for task in feature_tasks:
                        task_label = task.get("label", "")
                        # Only add if label doesn't already exist (avoid duplicates)
                        if task_label and task_label not in existing_tasks_by_label:
                            all_tasks.append(task)
                            existing_tasks_by_label[task_label] = task
                            print(f"✅ Merged task: {task_label} from {feature_tasks_file.parent.parent.name}")
            except (json.JSONDecodeError, Exception) as e:
                print(f"⚠️  Error reading {feature_tasks_file}: {e}")
        
        # Write merged tasks.json
        if all_tasks:
            merged_tasks_data = {
                "version": "2.0.0",
                "tasks": all_tasks
            }
            try:
                with open(root_tasks, 'w', encoding='utf-8') as f:
                    json.dump(merged_tasks_data, f, indent=4, ensure_ascii=False)
                merged_files.append((Path("features/*/tasks.json"), root_tasks))
                print(f"🔄 Merged tasks.json → {root_tasks}")
            except Exception as e:
                print(f"❌ Error writing merged tasks.json: {e}")

    # Report results
    print("\n" + "="*60)
    print("Behavior Sync Report")
    print("="*60)
    print(f"✅ Synced: {len(synced_files)} files")
    print(f"🔄 Merged: {len(merged_files)} files")
    print(f"⏭️  Skipped: {len(skipped_files)} files")
    
    if synced_files:
        print("\nSynced files:")
        for src, dest in synced_files:
            print(f"  {src.relative_to(src_root)} → {dest}")
    
    if merged_files:
        print("\nMerged files:")
        for src, dest in merged_files:
            print(f"  {src.relative_to(src_root)} → {dest}")
    
    if skipped_files:
        print("\nSkipped files:")
        for src, reason in skipped_files:
            print(f"  {src.relative_to(src_root)} ({reason})")
    
    return {
        "synced": len(synced_files),
        "merged": len(merged_files),
        "skipped": len(skipped_files)
    }


def behavior_sync_watch():
    """Watch for file changes and automatically sync behaviors."""
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
    except ImportError:
        print("❌ watchdog package not installed.")
        print("   Install with: pip install watchdog")
        return
    
    from pathlib import Path
    import time
    import threading
    
    class BehaviorSyncHandler(FileSystemEventHandler):
        def __init__(self):
            self.last_change = 0
            self.debounce_time = 2  # Wait 2 seconds after last change
            self.timer = None
        
        def on_modified(self, event):
            if event.is_directory:
                return
            
            src_path = Path(event.src_path)
            # Only watch .mdc, .md, .py, .json files in cursor directories
            if src_path.suffix not in [".mdc", ".md", ".py", ".json"]:
                return
            
            if "cursor" not in str(src_path):
                return
            
            # Check for draft markers (skip if draft)
            try:
                content = src_path.read_text(encoding='utf-8', errors='ignore')
                content_lower = content.lower()
                lines = content_lower.split('\n')
                has_draft_marker = False
                for line in lines[:10]:
                    stripped = line.strip()
                    if stripped.startswith('#draft') or stripped.startswith('#experimental'):
                        has_draft_marker = True
                        break
                    if stripped.startswith('draft:') or stripped.startswith('experimental:'):
                        has_draft_marker = True
                        break
                
                if has_draft_marker:
                    return
            except Exception:
                pass
            
            self.last_change = time.time()
            
            # Cancel existing timer
            if self.timer:
                self.timer.cancel()
            
            # Set new timer to run sync after debounce
            self.timer = threading.Timer(self.debounce_time, self.run_sync)
            self.timer.start()
        
        def run_sync(self):
            if time.time() - self.last_change < self.debounce_time:
                return
            
            print("\n🔄 Behavior file changed, syncing...")
            behavior_sync(None)
            print("✅ Sync complete. Watching for changes...")
    
    # Watch all features/*/cursor/ directories
    src_root = Path("features")
    cursor_dirs = [p for p in src_root.glob("*/cursor") if p.is_dir()]
    
    if not cursor_dirs:
        print("❌ No cursor directories found in features/")
        return
    
    event_handler = BehaviorSyncHandler()
    observer = Observer()
    
    for cursor_dir in cursor_dirs:
        observer.schedule(event_handler, str(cursor_dir), recursive=True)
        print(f"👀 Watching: {cursor_dir}")
    
    observer.start()
    print("\n✅ Behavior sync watch mode active. Press Ctrl+C to stop.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 Watch mode stopped.")
    
    observer.join()


if __name__ == "__main__":
    import sys
    import io
    
    # Fix Windows console encoding for emoji support
    if sys.platform == "win32":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    
    # Check if watch mode requested
    if len(sys.argv) > 1 and sys.argv[1] == "watch":
        behavior_sync_watch()
    else:
        feature = sys.argv[1] if len(sys.argv) > 1 else None
        behavior_sync(feature)