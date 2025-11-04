def behavior_index(feature=None):
    """
    Detect changes to behavior files and update local/global indexes.
    
    Scans behaviors/*/cursor/ folders for behavior files and maintains:
    - Local indexes: behaviors/<feature>/behavior-index.json
    - Global index: .cursor/behavior-index.json
    
    Rules:
    1. Detect additions, updates, or deletions in behaviors/*/cursor/
    2. Record feature name, file type, path, and modification timestamp
    3. Skip draft or experimental behaviors
    4. Update both local and global indexes
    5. Log the number of behaviors detected and updated
    """
    from pathlib import Path
    import json
    import time
    import sys
    import importlib.util
    
    # Import module with hyphens using importlib
    common_path = Path(__file__).parent / "code-agent-common.py"
    spec = importlib.util.spec_from_file_location("code_agent_common", common_path)
    common = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(common)
    find_deployed_behaviors = common.find_deployed_behaviors

    global_index = Path(".cursor/behavior-index.json")
    
    # Behavior file extensions to index
    behavior_extensions = [".mdc", ".md", ".py", ".json"]
    
    # Determine features to index
    if feature:
        # Find specific feature directory with behavior.json
        behaviors_root = Path("behaviors")
        cursor_path = behaviors_root / feature
        if not (cursor_path / "behavior.json").exists():
            # Try to find it dynamically
            all_behaviors = find_deployed_behaviors()
            matching = [b for b in all_behaviors if b.name == feature]
            cursor_path = matching[0] if matching else cursor_path
        features = [cursor_path] if cursor_path.exists() else []
    else:
        # Find all deployed behaviors dynamically
        features = find_deployed_behaviors()

    index_data = []
    skipped_files = []
    
    for cursor_path in features:
        feature_name = cursor_path.parent.name
        
        for file in cursor_path.rglob("*"):
            # Skip directories
            if file.is_dir():
                continue
            
            # Skip files that aren't behavior files
            if file.suffix not in behavior_extensions:
                continue
            
            # Skip draft or experimental behaviors and extract purpose
            purpose = None
            try:
                content = file.read_text(encoding='utf-8', errors='ignore')
                content_lower = content.lower()
                lines = content_lower.split('\n')
                
                # Check for draft markers
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
                
                # Extract purpose one-liner
                lines_list = content.split('\n')
                for i, line in enumerate(lines_list):
                    line_lower = line.lower()
                    # Look for Purpose: or **Purpose:** (must be at start or after whitespace/markers)
                    if '**purpose:**' in line_lower:
                        # Extract text after **Purpose:**
                        parts = line_lower.split('**purpose:**', 1)
                        if len(parts) > 1:
                            purpose_text = parts[1].strip()
                            # Remove any trailing **
                            purpose_text = purpose_text.split('**', 1)[0].strip()
                            if purpose_text:
                                purpose = purpose_text
                                break
                            # Try next line if empty
                            if i + 1 < len(lines_list):
                                next_line = lines_list[i + 1].strip()
                                if next_line and not next_line.startswith('*') and not next_line.startswith('#') and not next_line.startswith('```'):
                                    purpose = next_line.strip('*').strip()
                                    break
                    elif line_lower.strip().startswith('**purpose:**') or (line_lower.count('purpose:') == 1 and 'purpose:' in line_lower):
                        # More precise match for Purpose: line
                        if '**purpose:**' in line_lower:
                            purpose_text = line_lower.split('**purpose:**', 1)[-1].strip()
                            purpose_text = purpose_text.split('**', 1)[0].strip()
                        else:
                            # Regular purpose: (not in code)
                            idx = line_lower.find('purpose:')
                            purpose_text = line[idx + 8:].strip()
                        
                        # Only use if it looks like a description (not code)
                        if purpose_text and not purpose_text.startswith('#') and not '=' in purpose_text[:20] and not '"' in purpose_text[:10]:
                            purpose = purpose_text.strip('*').strip()
                            if len(purpose) > 10 and len(purpose) < 200:
                                break
                        
                        # Try next line if current looks wrong
                        if i + 1 < len(lines_list):
                            next_line = lines_list[i + 1].strip()
                            if next_line and not next_line.startswith('*') and not next_line.startswith('#') and not next_line.startswith('```') and '=' not in next_line[:10]:
                                purpose = next_line.strip('*').strip()
                                if len(purpose) > 10 and len(purpose) < 200:
                                    break
                
                # Fallback: try to extract from docstring for Python files
                if not purpose and file.suffix == '.py':
                    import re
                    docstring_match = re.search(r'"""(.*?)"""', content, re.DOTALL)
                    if docstring_match:
                        docstring = docstring_match.group(1).strip()
                        # Get first sentence or first line
                        purpose = docstring.split('\n')[0].strip().split('.')[0].strip()
                
                # Fallback: extract from first meaningful line (not code)
                if not purpose:
                    for line in content.split('\n'):
                        stripped = line.strip()
                        # Skip code-like lines
                        if (stripped and 
                            not stripped.startswith('#') and 
                            not stripped.startswith('*') and 
                            not stripped.startswith('```') and
                            not stripped.startswith('def ') and
                            not stripped.startswith('import ') and
                            not '=' in stripped[:30] and
                            not stripped.startswith('"') and
                            len(stripped) > 10 and
                            len(stripped) < 200):
                            purpose = stripped[:150].strip()  # Limit to 150 chars
                            break
                
                if not purpose:
                    purpose = f"{file.stem} behavior"
                    
            except Exception as e:
                skipped_files.append((file, f"read error: {e}"))
                continue
            
            # Determine deployed location based on file type
            deployed_location = None
            deployed_file = None
            if file.suffix == ".mdc":
                deployed_location = ".cursor/rules/"
                deployed_file = f".cursor/rules/{file.name}"
            elif file.suffix == ".md":
                deployed_location = ".cursor/command-runners/"
                deployed_file = f".cursor/command-runners/{file.name}"
            elif file.suffix == ".py":
                deployed_location = "command-runners/"
                deployed_file = f"command-runners/{file.name}"
            elif file.suffix == ".json" and file.name.endswith("-mcp.json"):
                deployed_location = ".cursor/mcp/"
                deployed_file = f".cursor/mcp/{file.name}"
            else:
                deployed_location = None
                deployed_file = None
            
            # Get file stats
            try:
                stat = file.stat()
                behavior_entry = {
                    "feature": feature_name,
                    "file": file.name,
                    "type": file.suffix,
                    "path": str(file),
                    "purpose": purpose or f"{file.stem} behavior",
                    "deployed_location": deployed_location,
                    "deployed_file": deployed_file,
                    "modified": time.ctime(stat.st_mtime),
                    "modified_timestamp": stat.st_mtime
                }
                index_data.append(behavior_entry)
            except Exception as e:
                skipped_files.append((file, f"stat error: {e}"))
                continue
    
    # Organize into two sections: deployed and features
    deployed_section = {}
    features_section = {}
    
    for behavior in index_data:
        # Deployed section - organized by deployment location
        if behavior.get("deployed_location"):
            location = behavior["deployed_location"]
            if location not in deployed_section:
                deployed_section[location] = []
            deployed_section[location].append({
                "file": behavior["file"],
                "purpose": behavior["purpose"],
                "deployed_file": behavior["deployed_file"],
                "source": behavior["path"]
            })
        
        # Features section - organized by feature
        feature_name = behavior["feature"]
        if feature_name not in features_section:
            features_section[feature_name] = []
        
        # Group related files by behavior name (extract from filename)
        features_section[feature_name].append({
            "file": behavior["file"],
            "type": behavior["type"],
            "purpose": behavior["purpose"],
            "path": behavior["path"],
            "deployed_location": behavior.get("deployed_location"),
            "deployed_file": behavior.get("deployed_file")
        })
    
    # Update global index
    global_index.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(global_index, 'w', encoding='utf-8') as out:
            json.dump({
                "last_updated": time.ctime(),
                "last_updated_timestamp": time.time(),
                "total_behaviors": len(index_data),
                "features_count": len(features),
                "deployed": deployed_section,
                "features": features_section
            }, out, indent=2, ensure_ascii=False)
        print(f"✅ Global index updated: {global_index}")
    except Exception as e:
        print(f"❌ Error updating global index: {e}")
        return
    
    # Update local indexes for each feature
    for cursor_path in features:
        feature_name = cursor_path.parent.name
        local_index = cursor_path.parent / "behavior-index.json"
        
        # Get behaviors for this feature
        feature_behaviors = [b for b in index_data if b["feature"] == feature_name]
        
        # Organize local index similarly
        local_deployed = {}
        for behavior in feature_behaviors:
            if behavior.get("deployed_location"):
                location = behavior["deployed_location"]
                if location not in local_deployed:
                    local_deployed[location] = []
                local_deployed[location].append({
                    "file": behavior["file"],
                    "purpose": behavior["purpose"],
                    "deployed_file": behavior["deployed_file"]
                })
        
        try:
            with open(local_index, 'w', encoding='utf-8') as out:
                json.dump({
                    "feature": feature_name,
                    "last_updated": time.ctime(),
                    "last_updated_timestamp": time.time(),
                    "behavior_count": len(feature_behaviors),
                    "deployed": local_deployed,
                    "behaviors": feature_behaviors
                }, out, indent=2, ensure_ascii=False)
            try:
                print(f"✅ Local index updated: {local_index.relative_to(Path('behaviors'))}")
            except ValueError:
                print(f"✅ Local index updated: {local_index}")
        except Exception as e:
            print(f"⚠️  Error updating local index for {feature_name}: {e}")
    
    # Report results
    print("\n" + "="*60)
    print("Behavior Index Report")
    print("="*60)
    print(f"✅ Indexed: {len(index_data)} behaviors")
    print(f"📁 Features: {len(features)}")
    print(f"⏭️  Skipped: {len(skipped_files)} files")
    
    if index_data:
        print("\nBehavior counts by type:")
        type_counts = {}
        for item in index_data:
            file_type = item["type"]
            type_counts[file_type] = type_counts.get(file_type, 0) + 1
        for file_type, count in sorted(type_counts.items()):
            print(f"  {file_type}: {count}")
        
        print("\nBehavior counts by feature:")
        feature_counts = {}
        for item in index_data:
            feature = item["feature"]
            feature_counts[feature] = feature_counts.get(feature, 0) + 1
        for feature, count in sorted(feature_counts.items()):
            print(f"  {feature}: {count}")
    
    if skipped_files:
        print("\nSkipped files:")
        for file, reason in skipped_files:
            try:
                print(f"  {file.relative_to(Path('behaviors'))} ({reason})")
            except ValueError:
                print(f"  {file} ({reason})")
    
    return {
        "indexed": len(index_data),
        "features": len(features),
        "skipped": len(skipped_files)
    }


def sync_purposes_from_global(feature=None):
    """
    Copy purposes from global index to local index files.
    Use this after manually updating purposes in the global index.
    """
    from pathlib import Path
    import json
    import sys
    import importlib.util
    
    # Import module with hyphens using importlib
    common_path = Path(__file__).parent / "code-agent-common.py"
    spec = importlib.util.spec_from_file_location("code_agent_common", common_path)
    common = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(common)
    find_deployed_behaviors = common.find_deployed_behaviors
    
    global_index = Path(".cursor/behavior-index.json")
    
    if not global_index.exists():
        print("❌ Global index not found. Run behavior-index first.")
        return
    
    # Load global index
    try:
        with open(global_index, 'r', encoding='utf-8') as f:
            global_data = json.load(f)
    except Exception as e:
        print(f"❌ Error reading global index: {e}")
        return
    
    # Create purpose lookup from global index
    purpose_lookup = {}
    if "features" in global_data:
        for feature_name, behaviors in global_data["features"].items():
            for behavior in behaviors:
                key = f"{feature_name}:{behavior['file']}"
                purpose_lookup[key] = behavior.get("purpose")
    
    # Update local indexes
    if feature:
        # Find specific feature directory
        behaviors_root = Path("behaviors")
        feature_path = behaviors_root / feature
        if not (feature_path / "behavior.json").exists():
            all_behaviors = find_deployed_behaviors()
            matching = [b for b in all_behaviors if b.name == feature]
            feature_path = matching[0] if matching else feature_path
        features_to_update = [(feature, feature_path)]
    else:
        # Find all deployed behaviors
        all_behaviors = find_deployed_behaviors()
        features_to_update = [(b.name, b) for b in all_behaviors]
    
    updated_count = 0
    
    for feature_name, feature_path in features_to_update:
        local_index = feature_path / "behavior-index.json"
        
        if not local_index.exists():
            continue
        
        try:
            with open(local_index, 'r', encoding='utf-8') as f:
                local_data = json.load(f)
            
            # Update purposes in local index from global
            updated = False
            if "behaviors" in local_data:
                for behavior in local_data["behaviors"]:
                    key = f"{feature_name}:{behavior['file']}"
                    if key in purpose_lookup:
                        new_purpose = purpose_lookup[key]
                        if behavior.get("purpose") != new_purpose:
                            behavior["purpose"] = new_purpose
                            updated = True
            
            # Update purposes in deployed section
            if "deployed" in local_data:
                for location, items in local_data["deployed"].items():
                    for item in items:
                        key = f"{feature_name}:{item['file']}"
                        if key in purpose_lookup:
                            new_purpose = purpose_lookup[key]
                            if item.get("purpose") != new_purpose:
                                item["purpose"] = new_purpose
                                updated = True
            
            if updated:
                with open(local_index, 'w', encoding='utf-8') as f:
                    json.dump(local_data, f, indent=2, ensure_ascii=False)
                try:
                    print(f"✅ Updated purposes in {local_index.relative_to(Path('behaviors'))}")
                except ValueError:
                    print(f"✅ Updated purposes in {local_index}")
                updated_count += 1
        
        except Exception as e:
            print(f"⚠️  Error updating {feature_name}: {e}")
    
    if updated_count > 0:
        print(f"\n✅ Synced purposes from global to {updated_count} local index(es)")
    else:
        print("ℹ️  No local indexes needed updating")


if __name__ == "__main__":
    import sys
    import io
    
    # Fix Windows console encoding for emoji support
    if sys.platform == "win32":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    
    if len(sys.argv) > 1 and sys.argv[1] == "sync-purposes":
        feature = sys.argv[2] if len(sys.argv) > 2 else None
        sync_purposes_from_global(feature)
    else:
        feature = sys.argv[1] if len(sys.argv) > 1 else None
        behavior_index(feature)

