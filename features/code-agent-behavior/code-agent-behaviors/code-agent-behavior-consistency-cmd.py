def behavior_consistency(feature=None):
    """
    When behaviors are changed, deleted, updated, or created,
    validate for inconsistencies, overlaps, or inconsistent guidance,
    and surface potential contradictions or redundancies for review.
    
    Uses OpenAI function calling for semantic analysis.
    Generates a summary report for human and AI review.
    """
    import json
    import os
    from pathlib import Path
    from typing import List, Dict, Any
    
    try:
        from openai import OpenAI
    except ImportError:
        print("❌ OpenAI package not installed. Install with: pip install openai")
        return
    
    # Load .env file if python-dotenv is available
    try:
        from dotenv import load_dotenv
        # Try to load from features/.env first, then root .env
        features_env = Path("features/.env")
        root_env = Path(".env")
        if features_env.exists():
            load_dotenv(features_env, override=True)
        elif root_env.exists():
            load_dotenv(root_env, override=True)
        else:
            # Try to find any .env file in parent directories
            load_dotenv(override=True)
    except ImportError:
        # python-dotenv not installed, continue with system env vars only
        pass
    
    # Initialize OpenAI client
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ OPENAI_API_KEY environment variable not set")
        print("   Set it in features/.env or .env file, or with: export OPENAI_API_KEY='your-key'")
        return
    
    client = OpenAI(api_key=api_key)
    
    # Function schema for consistency analysis
    ANALYSIS_SCHEMA = {
        "name": "analyze_behavior_consistency",
        "description": "Analyze behaviors for overlaps, contradictions, and inconsistencies",
        "parameters": {
            "type": "object",
            "properties": {
                "overlaps": {
                    "type": "array",
                    "description": "Behaviors with similar purpose but different approaches",
                    "items": {
                        "type": "object",
                        "properties": {
                            "behavior1": {"type": "string", "description": "First behavior file/name"},
                            "behavior2": {"type": "string", "description": "Second behavior file/name"},
                            "similarity": {"type": "string", "description": "What makes them similar"},
                            "difference": {"type": "string", "description": "How they differ"},
                            "recommendation": {"type": "string", "description": "Suggested action"}
                        },
                        "required": ["behavior1", "behavior2", "similarity", "difference"]
                    }
                },
                "contradictions": {
                    "type": "array",
                    "description": "Behaviors with opposite guidance for the same context",
                    "items": {
                        "type": "object",
                        "properties": {
                            "behavior1": {"type": "string", "description": "First behavior file/name"},
                            "behavior2": {"type": "string", "description": "Second behavior file/name"},
                            "context": {"type": "string", "description": "The context where they contradict"},
                            "contradiction": {"type": "string", "description": "What contradicts"},
                            "recommendation": {"type": "string", "description": "Suggested resolution"}
                        },
                        "required": ["behavior1", "behavior2", "context", "contradiction"]
                    }
                },
                "inconsistencies": {
                    "type": "array",
                    "description": "Behaviors with naming, tone, or scope mismatches",
                    "items": {
                        "type": "object",
                        "properties": {
                            "behavior1": {"type": "string", "description": "First behavior file/name"},
                            "behavior2": {"type": "string", "description": "Second behavior file/name"},
                            "type": {"type": "string", "description": "Type of inconsistency (naming/tone/scope)"},
                            "issue": {"type": "string", "description": "What is inconsistent"},
                            "recommendation": {"type": "string", "description": "Suggested fix"}
                        },
                        "required": ["behavior1", "behavior2", "type", "issue"]
                    }
                },
                "summary": {
                    "type": "string",
                    "description": "Overall summary of consistency analysis"
                }
            },
            "required": ["overlaps", "contradictions", "inconsistencies", "summary"]
        }
    }
    
    src_root = Path("features")
    index_path = Path(".cursor/behavior-index.json")
    report_path = Path(".cursor/behavior-consistency-report.md")
    
    if not index_path.exists():
        print("❌ No behavior index found. Run \\behavior-index first.")
        return
    
    # Load index
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
    except Exception as e:
        print(f"❌ Error reading index: {e}")
        return
    
    # Collect behaviors
    behaviors = []
    
    # Process both deployed and features sections
    for section_name in ["deployed", "features"]:
        if section_name not in index_data:
            continue
            
        section_data = index_data[section_name]
        
        # Handle different section structures
        if isinstance(section_data, dict):
            # deployed section: {"location": [behaviors]}
            for location, items in section_data.items():
                for item in items:
                    if feature and item.get("feature") != feature:
                        continue
                    behaviors.append({
                        "feature": item.get("feature", "unknown"),
                        "file": item.get("file", ""),
                        "type": item.get("type", ""),
                        "path": item.get("source", item.get("path", "")),
                        "purpose": item.get("purpose", ""),
                        "location": location
                    })
        elif isinstance(section_data, list):
            # features section: [behaviors]
            for item in section_data:
                if feature and item.get("feature") != feature:
                    continue
                behaviors.append({
                    "feature": item.get("feature", "unknown"),
                    "file": item.get("file", ""),
                    "type": item.get("type", ""),
                    "path": item.get("source", item.get("path", "")),
                    "purpose": item.get("purpose", ""),
                    "location": "features"
                })
    
    if not behaviors:
        print(f"❌ No behaviors found" + (f" for feature '{feature}'" if feature else ""))
        return
    
    print(f"📊 Analyzing {len(behaviors)} behaviors for consistency...")
    
    # Load behavior file contents
    behavior_contents = []
    for behavior in behaviors:
        file_path = Path(behavior["path"])
        if not file_path.exists():
            # Try alternative path
            if behavior["location"] == "features":
                file_path = src_root / behavior["feature"] / "code-agent-behaviors" / behavior["file"]
            else:
                # Try deployed location
                if behavior["location"].startswith(".cursor/commands/"):
                    file_path = Path(behavior["location"].replace(".cursor/", ".cursor/")) / behavior["file"]
                elif behavior["location"].startswith("commands/"):
                    file_path = Path(behavior["location"]) / behavior["file"]
                else:
                    file_path = Path(behavior["location"]) / behavior["file"]
        
        if file_path.exists():
            try:
                content = file_path.read_text(encoding='utf-8', errors='ignore')
                behavior_contents.append({
                    **behavior,
                    "content": content[:5000]  # Limit content size
                })
            except Exception as e:
                print(f"⚠️  Could not read {file_path}: {e}")
                behavior_contents.append(behavior)
        else:
            behavior_contents.append(behavior)
    
    # Prepare prompt for OpenAI
    behaviors_text = "\n\n".join([
        f"**{b['file']}** ({b['feature']}/{b['type']})\n"
        f"Purpose: {b.get('purpose', 'N/A')}\n"
        f"Content preview: {b.get('content', 'N/A')[:500]}" 
        for b in behavior_contents
    ])
    
    prompt = f"""Analyze the following AI behaviors for semantic overlap, contradictions, and inconsistencies.

Behaviors to analyze:
{behaviors_text}

Look for:
1. **Overlaps**: Behaviors with similar purpose but different approaches
2. **Contradictions**: Behaviors that give opposite guidance for the same context
3. **Inconsistencies**: Behaviors with naming, tone, or scope mismatches

Be thorough but fair - only flag genuine issues that could cause confusion or conflicts."""
    
    # Call OpenAI with function calling
    try:
        print("🤖 Using OpenAI to analyze behaviors...")
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert at analyzing AI behavior definitions for consistency, overlaps, and contradictions."},
                {"role": "user", "content": prompt}
            ],
            functions=[ANALYSIS_SCHEMA],
            function_call={"name": "analyze_behavior_consistency"}
        )
        
        if response.choices[0].message.function_call:
            result = json.loads(response.choices[0].message.function_call.arguments)
            
            # Generate report
            report_lines = [
                "# Behavior Consistency Report",
                "",
                f"**Generated:** {Path.cwd()}",
                f"**Behaviors Analyzed:** {len(behaviors)}",
                "",
                "---",
                "",
                "## Summary",
                "",
                result.get("summary", "No summary provided."),
                "",
                "---",
                "",
            ]
            
            # Add overlaps
            overlaps = result.get("overlaps", [])
            if overlaps:
                report_lines.extend([
                    "## Overlaps (Similar Purpose, Different Approach)",
                    ""
                ])
                for i, overlap in enumerate(overlaps, 1):
                    report_lines.extend([
                        f"### Overlap {i}",
                        f"- **Behavior 1:** {overlap.get('behavior1', 'N/A')}",
                        f"- **Behavior 2:** {overlap.get('behavior2', 'N/A')}",
                        f"- **Similarity:** {overlap.get('similarity', 'N/A')}",
                        f"- **Difference:** {overlap.get('difference', 'N/A')}",
                        f"- **Recommendation:** {overlap.get('recommendation', 'Review manually')}",
                        ""
                    ])
            else:
                report_lines.extend([
                    "## Overlaps",
                    "",
                    "✅ No overlaps detected.",
                    ""
                ])
            
            # Add contradictions
            contradictions = result.get("contradictions", [])
            if contradictions:
                report_lines.extend([
                    "## Contradictions (Opposite Guidance)",
                    ""
                ])
                for i, contradiction in enumerate(contradictions, 1):
                    report_lines.extend([
                        f"### Contradiction {i}",
                        f"- **Behavior 1:** {contradiction.get('behavior1', 'N/A')}",
                        f"- **Behavior 2:** {contradiction.get('behavior2', 'N/A')}",
                        f"- **Context:** {contradiction.get('context', 'N/A')}",
                        f"- **Contradiction:** {contradiction.get('contradiction', 'N/A')}",
                        f"- **Recommendation:** {contradiction.get('recommendation', 'Review manually')}",
                        ""
                    ])
            else:
                report_lines.extend([
                    "## Contradictions",
                    "",
                    "✅ No contradictions detected.",
                    ""
                ])
            
            # Add inconsistencies
            inconsistencies = result.get("inconsistencies", [])
            if inconsistencies:
                report_lines.extend([
                    "## Inconsistencies (Naming, Tone, or Scope)",
                    ""
                ])
                for i, inconsistency in enumerate(inconsistencies, 1):
                    report_lines.extend([
                        f"### Inconsistency {i}",
                        f"- **Behavior 1:** {inconsistency.get('behavior1', 'N/A')}",
                        f"- **Behavior 2:** {inconsistency.get('behavior2', 'N/A')}",
                        f"- **Type:** {inconsistency.get('type', 'N/A')}",
                        f"- **Issue:** {inconsistency.get('issue', 'N/A')}",
                        f"- **Recommendation:** {inconsistency.get('recommendation', 'Review manually')}",
                        ""
                    ])
            else:
                report_lines.extend([
                    "## Inconsistencies",
                    "",
                    "✅ No inconsistencies detected.",
                    ""
                ])
            
            # Write report
            report_path.parent.mkdir(parents=True, exist_ok=True)
            report_path.write_text("\n".join(report_lines), encoding='utf-8')
            
            print(f"✅ Generated consistency report → {report_path}")
            print(f"   Found: {len(overlaps)} overlaps, {len(contradictions)} contradictions, {len(inconsistencies)} inconsistencies")
            
        else:
            print("⚠️  OpenAI did not return function call result")
            
    except Exception as e:
        print(f"❌ Error calling OpenAI: {e}")
        import traceback
        traceback.print_exc()
        return


def behavior_consistency_watch():
    """
    Watch for behavior file changes and automatically run consistency checks.
    
    Monitors features/*/code-agent-behaviors/ directories for changes to:
    - .mdc files (rules)
    - .md files (commands)
    - .py files (implementations)
    
    When changes are detected, automatically runs behavior_consistency()
    Output goes to notification file and stderr to be visible in chat.
    """
    from pathlib import Path
    import time
    import sys
    import io
    
    # Setup notification file for chat visibility
    notif_dir = Path(".cursor/watchers/notifications")
    notif_dir.mkdir(parents=True, exist_ok=True)
    notif_file = notif_dir / "behavior-consistency-cmd.txt"
    
    def notify(msg):
        """Write to notification file (and stderr if available)"""
        # Always write to notification file
        try:
            with open(notif_file, 'a', encoding='utf-8') as f:
                f.write(msg + '\n')
                f.flush()
        except Exception:
            pass
        
        # Try to write to stderr if available, but don't fail if it's closed
        try:
            if sys.stderr and not sys.stderr.closed:
                print(msg, file=sys.stderr)
                sys.stderr.flush()
        except (ValueError, AttributeError, OSError):
            # stderr is closed or unavailable - that's OK, we have notification file
            pass
    
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
    except ImportError:
        print("❌ watchdog package not installed.", file=sys.stderr)
        print("   Install with: pip install watchdog", file=sys.stderr)
        print("   This enables automatic file watching for behavior changes.", file=sys.stderr)
        return
    
    class BehaviorChangeHandler(FileSystemEventHandler):
        """Handler for behavior file changes"""
        
        def __init__(self, notify_func):
            self.last_check = 0
            self.debounce_seconds = 2  # Wait 2 seconds after last change
            self.notify = notify_func
            
        def on_modified(self, event):
            if event.is_directory:
                return
            
            file_path = Path(event.src_path)
            
            # Only watch behavior files in code-agent-behaviors/ directories
            if file_path.suffix in ['.mdc', '.md', '.py']:
                if 'cursor' in file_path.parts:
                    # Debounce: wait for file operations to complete
                    current_time = time.time()
                    if current_time - self.last_check < self.debounce_seconds:
                        return
                    
                    self.last_check = current_time
                    notify(f"\n🔍 Detected change: {file_path.name}")
                    notify("   Running behavior consistency check...")
                    
                    # Extract feature name from path
                    feature = None
                    if 'features' in file_path.parts:
                        features_idx = file_path.parts.index('features')
                        if len(file_path.parts) > features_idx + 1:
                            feature = file_path.parts[features_idx + 1]
                    
                    behavior_consistency(feature)
                    notify("✅ Consistency check completed\n")
        
        def on_created(self, event):
            self.on_modified(event)
        
        def on_deleted(self, event):
            if event.is_directory:
                return
            
            file_path = Path(event.src_path)
            if file_path.suffix in ['.mdc', '.md', '.py']:
                if 'cursor' in file_path.parts:
                    notify(f"\n🗑️  Detected deletion: {file_path.name}")
                    notify("   Running behavior consistency check...")
                    
                    behavior_consistency()
                    notify("✅ Consistency check completed\n")
    
    # Set up watcher
    src_root = Path("features")
    if not src_root.exists():
        print("❌ features/ directory not found")
        return
    
    event_handler = BehaviorChangeHandler(notify)
    observer = Observer()
    
    # Watch all cursor/ directories
    cursor_dirs = list(src_root.glob("*/cursor"))
    if not cursor_dirs:
        print("⚠️  No cursor/ directories found in features/")
        return
    
    for cursor_dir in cursor_dirs:
        observer.schedule(event_handler, str(cursor_dir), recursive=True)
        notify(f"👀 Watching: {cursor_dir}")
    
    observer.start()
    notify("\n✅ File watcher started. Monitoring behavior files for changes...")
    notify("   Press Ctrl+C to stop\n")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        notify("\n🛑 Stopping file watcher...")
    
    observer.join()
    notify("✅ File watcher stopped")


if __name__ == "__main__":
    import sys
    import io
    
    # Fix Windows console encoding for emoji support
    if sys.platform == "win32":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    
    # Check if watch mode requested
    if len(sys.argv) > 1 and sys.argv[1] == "watch":
        behavior_consistency_watch()
    else:
        feature = sys.argv[1] if len(sys.argv) > 1 else None
        behavior_consistency(feature)

