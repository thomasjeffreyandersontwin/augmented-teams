def behavior_structure(action="validate", feature=None, behavior_name=None):
    """
    Validate, fix, or create AI behaviors following structure and naming conventions.
    
    Actions:
    - validate: Check structure compliance
    - fix: Automatically fix structure issues
    - create: Scaffold a new behavior
    
    Rules:
    1. File names must follow <feature>-<type>.<ext> pattern
    2. Rules should have matching commands
    3. Commands should have matching implementation files
    4. Related files share consistent naming prefixes
    """
    from pathlib import Path
    import re
    import json
    import time

    src_root = Path("features")
    
    # Naming pattern: <feature>-<behavior-name>-<type>.<ext>
    # Types: rule, cmd, _cmd (for Python), mcp
    # For commands: can have optional verb suffix: <feature>-<behavior-name>-<verb>-cmd.md
    # Rules: <feature>-<behavior-name>-rule.mdc (no verb)
    # Commands: <feature>-<behavior-name>-cmd.md OR <feature>-<behavior-name>-<verb>-cmd.md
    # Extensions: .mdc, .md, .py, .json
    # Pattern allows: <feature>-<behavior-name>(-<verb>?)-(rule|cmd|_cmd|mcp).<ext>
    pattern = re.compile(r"^([a-z0-9\-]+)-([a-z0-9\-]+)(?:-([a-z0-9\-]+))?-(rule|cmd|_cmd|mcp)\.(mdc|md|py|json)$", re.I)

    def validate_structure(cursor_path):
        """Validate structure and naming for a feature."""
        issues = []
        fixes_needed = []
        files_found = {"rules": [], "commands": [], "implementations": [], "mcps": []}
        
        for file in cursor_path.rglob("*"):
            if file.is_dir():
                continue
            
            # Skip index files - they're not behavior files
            if file.name == "behavior-index.json":
                continue
            
            ext = file.suffix
            name = file.name
            
            # Check naming pattern
            match = pattern.match(name)
            if not match:
                issues.append({
                    "type": "invalid_name",
                    "file": file,
                    "message": f"Invalid name pattern: {name}. Expected: <feature>-<behavior-name>-<type>.<ext> or <feature>-<behavior-name>-<verb>-cmd.md for multiple commands"
                })
                continue
            
            groups = match.groups()
            feature_prefix = groups[0]
            behavior_name = groups[1]
            verb_suffix = groups[2]  # Optional verb (e.g., "validate", "fix", "create")
            file_type = groups[3]
            file_ext = groups[4]
            
            # Extract base behavior name (without verb suffix)
            base_behavior_name = behavior_name
            
            # Categorize files
            if file_type == "rule":
                # Rules must NOT have verb suffix
                if verb_suffix:
                    issues.append({
                        "type": "invalid_name",
                        "file": file,
                        "message": f"Rule {name} should not have verb suffix. Use: {feature_prefix}-{behavior_name}-rule.mdc"
                    })
                files_found["rules"].append((file, feature_prefix, base_behavior_name))
            elif file_type == "cmd" and ext == ".md":
                # Commands can have optional verb suffix
                files_found["commands"].append((file, feature_prefix, base_behavior_name, verb_suffix))
            elif file_type == "_cmd" and ext == ".py":
                # Python implementations can have optional verb suffix
                files_found["implementations"].append((file, feature_prefix, base_behavior_name, verb_suffix))
            elif file_type == "mcp":
                # MCP configs typically don't have verb suffixes
                files_found["mcps"].append((file, feature_prefix, base_behavior_name))
            
            # Check for matching files
            if file_type == "rule":
                # Rules can relate to multiple commands - check for any command files with same base prefix
                # Matches: <feature>-<behavior-name>-cmd.md OR <feature>-<behavior-name>-<verb>-cmd.md
                rule_prefix = f"{feature_prefix}-{base_behavior_name}"
                matching_cmds = list(cursor_path.glob(f"{rule_prefix}*-cmd.md"))
                if not matching_cmds:
                    issues.append({
                        "type": "missing_command",
                        "file": file,
                        "message": f"Rule {name} missing matching command files (expected: {rule_prefix}*-cmd.md or {rule_prefix}-cmd.md)",
                        "suggested_fix": cursor_path / f"{rule_prefix}-cmd.md"
                    })
            
            # Check documentation and relationship sections
            try:
                content = file.read_text(encoding='utf-8', errors='ignore')
                if not content.strip() or len(content.strip()) < 50:
                    issues.append({
                        "type": "missing_docs",
                        "file": file,
                        "message": f"File {name} is empty or lacks documentation"
                    })
                else:
                    content_lower = content.lower()
                    # Check relationship sections (documentation that links rules, commands, and code)
                    if file_type == "rule":
                        # Rules must start with "**When** <event> condition,"
                        if not content.strip().startswith("**When**"):
                            issues.append({
                                "type": "invalid_rule_format",
                                "file": file,
                                "message": f"Rule {name} must start with '**When** <event> condition,'"
                            })
                        # Rules must reference executing commands
                        if "**executing commands:**" not in content_lower and "executing commands:" not in content_lower:
                            issues.append({
                                "type": "missing_relationships",
                                "file": file,
                                "message": f"Rule {name} missing 'Executing Commands:' section (lists which commands execute this rule)"
                            })
                    elif file_type == "cmd" and ext == ".md":
                        # Commands should reference: rule they follow, implementation code, when to use AI, when to use code
                        missing_sections = []
                        if "**rule:**" not in content_lower and "rule:" not in content_lower:
                            missing_sections.append("Rule (which rule this command follows)")
                        if "**implementation:**" not in content_lower and "implementation:" not in content_lower:
                            missing_sections.append("Implementation (code functions this command calls)")
                        if "**ai usage:**" not in content_lower and "ai usage:" not in content_lower:
                            missing_sections.append("AI Usage (when to use AI assistance)")
                        if "**code usage:**" not in content_lower and "code usage:" not in content_lower:
                            missing_sections.append("Code Usage (when to use code execution)")
                        
                        if missing_sections:
                            issues.append({
                                "type": "missing_relationships",
                                "file": file,
                                "message": f"Command {name} missing relationship sections: {', '.join(missing_sections)}"
                            })
            except:
                pass
        
        return issues, fixes_needed

    def fix_structure(cursor_path):
        """Automatically fix structure issues."""
        fixed = []
        created = []
        
        issues, _ = validate_structure(cursor_path)
        
        for issue in issues:
            if issue["type"] == "missing_command" and "suggested_fix" in issue:
                # Create missing command file with governance sections
                cmd_file = issue["suggested_fix"]
                rule_file = issue["file"]
                rule_name = rule_file.stem.replace("-rule", "")
                feature_prefix, behavior_name = issue["file"].stem.split("-rule")[0].split("-", 1)
                function_name = behavior_name.replace("-", "_")
                
                content = f"""### Command: `{cmd_file.name}`

**Purpose:** [Describe the command purpose]

**Usage:**
* `\\{behavior_name}` — [description]

**Rule:**
* `\\{rule_name}-rule` — [description of rule this command follows]

**Implementation:**
* `{function_name}()` — [description of code function]

**AI Usage:**
* [When to use AI assistance - e.g., for complex reasoning, content generation, etc.]

**Code Usage:**
* [When to use code execution - e.g., for file operations, data processing, etc.]

**Steps:**
1. [Step 1]
2. [Step 2]
"""
                cmd_file.write_text(content, encoding='utf-8')
                created.append(cmd_file)
                fixed.append(issue)
            
            elif issue["type"] == "invalid_rule_format":
                # Fix rule format: must start with "**When** <event> condition,"
                file = issue["file"]
                try:
                    content = file.read_text(encoding='utf-8', errors='ignore')
                    updated = False
                    
                    if not content.strip().startswith("**When**"):
                        # Try to find existing When/Then pattern and reformat
                        when_match = re.search(r'\*\*When\*\*', content, re.IGNORECASE)
                        if when_match:
                            # Extract existing content and reformat
                            content = content[when_match.start():]
                            updated = True
                        else:
                            # No When found, prepend it
                            content = "**When** <event> condition,\n**then** [action].\n\n" + content
                            updated = True
                    
                    if updated:
                        file.write_text(content, encoding='utf-8')
                        fixed.append(issue)
                except Exception as e:
                    pass
            
            elif issue["type"] == "missing_relationships":
                # Add missing relationship sections
                file = issue["file"]
                try:
                    content = file.read_text(encoding='utf-8', errors='ignore')
                    updated = False
                    
                    if file.suffix == ".mdc":
                        # Fix rule format: must start with "**When** <event> condition,"
                        if not content.strip().startswith("**When**"):
                            # Try to find existing When/Then pattern and reformat
                            when_match = re.search(r'\*\*When\*\*', content, re.IGNORECASE)
                            if when_match:
                                # Extract existing content and reformat
                                content = content[when_match.start():]
                                if not content.strip().startswith("**When**"):
                                    # Create proper format from beginning
                                    first_line = content.split('\n')[0]
                                    if 'when' in first_line.lower() and not first_line.strip().startswith("**When**"):
                                        content = f"**When** {first_line}\n" + content[len(first_line):]
                                    else:
                                        content = "**When** <event> condition,\n**then** [action].\n\n" + content
                                    updated = True
                            else:
                                # No When found, prepend it
                                content = "**When** <event> condition,\n**then** [action].\n\n" + content
                                updated = True
                        
                        # Add Executing Commands section if missing
                        if "**executing commands:" not in content.lower():
                            behavior_name = file.stem.replace("-rule", "")
                            new_section = f"\n\n**Executing Commands:**\n* `\\{behavior_name}` — [what the command is] [when to call it]"
                            content += new_section
                            updated = True
                    
                    elif file.suffix == ".md":
                        # Add missing governance sections to command
                        behavior_name = file.stem.replace("-cmd", "")
                        rule_name = behavior_name.replace("-cmd", "")
                        function_name = behavior_name.replace("-", "_")
                        
                        additions = []
                        if "**rule:**" not in content.lower():
                            additions.append(f"**Rule:**\n* `\\{rule_name}-rule` — [description of rule this command follows]")
                        if "**implementation:**" not in content.lower():
                            additions.append(f"**Implementation:**\n* `{function_name}()` — [description of code function]")
                        if "**ai usage:**" not in content.lower():
                            additions.append(f"**AI Usage:**\n* [When to use AI assistance - e.g., for complex reasoning, content generation, etc.]")
                        if "**code usage:**" not in content.lower():
                            additions.append(f"**Code Usage:**\n* [When to use code execution - e.g., for file operations, data processing, etc.]")
                        
                        if additions:
                            new_section = "\n\n" + "\n\n".join(additions)
                            content += new_section
                            updated = True
                    
                    if updated:
                        file.write_text(content, encoding='utf-8')
                        fixed.append(issue)
                except Exception as e:
                    pass
            
            elif issue["type"] == "missing_implementation" and "suggested_fix" in issue:
                # Create missing implementation file
                impl_file = issue["suggested_fix"]
                feature_prefix, behavior_name = issue["file"].stem.split("-rule")[0].split("-", 1)
                function_name = behavior_name.replace("-", "_")
                content = f"""def {function_name}(feature=None):
    \"\"\"Implementation for {behavior_name} behavior.\"\"\"
    from pathlib import Path
    
    # TODO: Implement {behavior_name} functionality
    pass


if __name__ == "__main__":
    import sys
    feature = sys.argv[1] if len(sys.argv) > 1 else None
    {function_name}(feature)
"""
                impl_file.write_text(content, encoding='utf-8')
                created.append(impl_file)
                fixed.append(issue)
            
            elif issue["type"] == "invalid_name":
                # Suggest rename but don't auto-fix (too risky)
                fixed.append({
                    "file": issue["file"],
                    "message": f"⚠️  Manual rename needed: {issue['file'].name} → [suggested name]"
                })
        
        return fixed, created

    def create_behavior(cursor_path, behavior_name, create_implementation=True):
        """Scaffold a new behavior with all required files.
        
        Args:
            cursor_path: Path to cursor directory
            behavior_name: Name of the behavior
            create_implementation: If True, create Python implementation file (default: True)
                                   Set to False for AI-only behaviors that don't need code automation
        """
        feature_name = cursor_path.parent.name
        
        created_files = []
        
        # Create rule file
        rule_file = cursor_path / f"{feature_name}-{behavior_name}-rule.mdc"
        rule_content = f"""**When** <event> condition,
**then** [action].

**Always:**
* [Always rule 1]
* [Always rule 2]

**Never:**
* [Never rule 1]

**Executing Commands:**
* `\\{behavior_name}` — [what the command is] [when to call it]
"""
        rule_file.write_text(rule_content, encoding='utf-8')
        created_files.append(rule_file)
        
        # Create command file
        cmd_file = cursor_path / f"{feature_name}-{behavior_name}-cmd.md"
        function_name = behavior_name.replace("-", "_")
        rule_ref = f"{feature_name}-{behavior_name}-rule"
        
        if create_implementation:
            impl_section = f"* `{function_name}()` — [description of code function]"
            code_usage = "* [When to use code execution - e.g., for file operations, data processing, etc.]"
        else:
            impl_section = "* No Python implementation needed — This is entirely AI-driven during conversation"
            code_usage = "* Not applicable — This behavior is AI-driven only"
        
        cmd_content = f"""### Command: `{feature_name}-{behavior_name}-cmd.md`

**Purpose:** [Describe the {behavior_name} command purpose]

**Usage:**
* `\\{behavior_name}` — [description]

**Rule:**
* `\\{rule_ref}` — [description of rule this command follows]

**Implementation:**
{impl_section}

**AI Usage:**
* [When to use AI assistance - e.g., for complex reasoning, content generation, etc.]

**Code Usage:**
{code_usage}

**Steps:**
1. [Step 1]
2. [Step 2]
3. [Step 3]
"""
        cmd_file.write_text(cmd_content, encoding='utf-8')
        created_files.append(cmd_file)
        
        # Create implementation file only if automation serves a purpose
        if create_implementation:
            impl_file = cursor_path / f"{feature_name}-{behavior_name}-cmd.py"
            impl_content = f"""def {function_name}(feature=None):
    \"\"\"
    Implementation for {behavior_name} behavior.
    
    [Add description]
    \"\"\"
    from pathlib import Path
    import io
    import sys

    # TODO: Implement {behavior_name} functionality
    print(f"{{behavior_name}} command executed")
    
    return {{"status": "success"}}


if __name__ == "__main__":
    import sys
    
    # Fix Windows console encoding for emoji support
    if sys.platform == "win32":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    
    feature = sys.argv[1] if len(sys.argv) > 1 else None
    {function_name}(feature)
"""
            impl_file.write_text(impl_content, encoding='utf-8')
            created_files.append(impl_file)
        
        return created_files

    # Determine features to process
    if feature:
        cursor_path = src_root / feature / "cursor"
        features = [cursor_path] if cursor_path.exists() else []
    else:
        features = [p for p in src_root.glob("*/cursor") if p.is_dir()]

    if action == "validate":
        all_issues = []
        for cursor_path in features:
            issues, _ = validate_structure(cursor_path)
            for issue in issues:
                all_issues.append({
                    "feature": cursor_path.parent.name,
                    **issue
                })
        
        print("="*60)
        print("Behavior Structure Validation")
        print("="*60)
        
        if not all_issues:
            print("✅ All behaviors follow structure and naming conventions.")
        else:
            print(f"❌ Found {len(all_issues)} structure issues:\n")
            for issue in all_issues:
                print(f"[{issue['feature']}] {issue['message']}")
                if "suggested_fix" in issue:
                    print(f"  → Suggested: {issue['suggested_fix'].name}")
        
        return {"issues": len(all_issues), "features": len(features)}
    
    elif action == "fix":
        all_fixed = []
        all_created = []
        
        print("="*60)
        print("Behavior Structure Fix")
        print("="*60)
        
        for cursor_path in features:
            fixed, created = fix_structure(cursor_path)
            all_fixed.extend(fixed)
            all_created.extend(created)
        
        print(f"✅ Fixed: {len(all_fixed)} issues")
        print(f"📄 Created: {len(all_created)} files")
        
        if all_created:
            print("\nCreated files:")
            for f in all_created:
                print(f"  {f.relative_to(src_root.parent)}")
        
        if all_fixed:
            print("\nFixed issues:")
            for fix in all_fixed:
                if isinstance(fix, dict):
                    print(f"  {fix.get('message', 'Unknown')}")
        
        return {"fixed": len(all_fixed), "created": len(all_created)}
    
    elif action == "create":
        if not behavior_name:
            print("❌ Error: behavior_name required for create action")
            print("Usage: python behavior-structure-cmd.py create <feature> <behavior-name> [--no-implementation]")
            return {"error": "behavior_name required"}
        
        if not feature:
            print("❌ Error: feature required for create action")
            print("Usage: python behavior-structure-cmd.py create <feature> <behavior-name> [--no-implementation]")
            return {"error": "feature required"}
        
        # Check if --no-implementation flag is set
        create_impl = "--no-implementation" not in sys.argv
        
        cursor_path = src_root / feature / "cursor"
        if not cursor_path.exists():
            cursor_path.mkdir(parents=True, exist_ok=True)
        
        created_files = create_behavior(cursor_path, behavior_name, create_implementation=create_impl)
        
        print("="*60)
        print(f"Behavior Structure: Created {behavior_name}")
        print("="*60)
        print(f"✅ Created {len(created_files)} files:")
        for f in created_files:
            print(f"  {f.relative_to(src_root.parent)}")
        
        if not create_impl:
            print("\n💡 Note: No Python implementation created (--no-implementation flag used).")
            print("   This behavior is AI-driven only. Add a .py file later if automation is needed.")
        
        return {"created": len(created_files), "files": [str(f) for f in created_files]}
    
    else:
        print(f"❌ Unknown action: {action}")
        print("Available actions: validate, fix, create")
        return {"error": f"Unknown action: {action}"}


def behavior_structure_watch():
    """Watch for behavior file changes and automatically validate structure.
    
    Output goes to stderr to be visible in chat.
    """
    import sys
    import io
    
    # Fix Windows console encoding
    if sys.platform == "win32":
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
    except ImportError:
        print("❌ watchdog package not installed.", file=sys.stderr)
        print("   Install with: pip install watchdog", file=sys.stderr)
        print("   This enables automatic file watching for behavior structure validation.", file=sys.stderr)
        return
    
    from pathlib import Path
    import time
    import threading
    
    class BehaviorStructureHandler(FileSystemEventHandler):
        def __init__(self):
            self.last_change = 0
            self.debounce_time = 2  # Wait 2 seconds after last change
            self.timer = None
        
        def on_modified(self, event):
            if event.is_directory:
                return
            
            src_path = Path(event.src_path)
            # Only watch behavior files in cursor/ directories
            if src_path.suffix not in [".mdc", ".md", ".py"]:
                return
            
            if "cursor" not in str(src_path):
                return
            
            # Skip draft or experimental behaviors
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
            
            # Set new timer to run validation after debounce
            self.timer = threading.Timer(self.debounce_time, self.run_validation, args=(src_path,))
            self.timer.start()
        
        def run_validation(self, changed_file):
            if time.time() - self.last_change < self.debounce_time:
                return
            
            print(f"\n🔄 Behavior file changed: {changed_file.name}", file=sys.stderr)
            print("Running structure validation...", file=sys.stderr)
            sys.stderr.flush()
            
            # Determine which feature this file belongs to
            feature = None
            parts = changed_file.parts
            if "features" in parts:
                feature_idx = parts.index("features")
                if feature_idx + 1 < len(parts):
                    feature = parts[feature_idx + 1]
            
            # Run validation
            result = behavior_structure("validate", feature)
            
            if result.get("issues", 0) == 0:
                print("✅ Structure validation passed", file=sys.stderr)
            else:
                print(f"⚠️  Found {result.get('issues', 0)} structure issue(s)", file=sys.stderr)
                print("   Run 'behavior-structure fix' to auto-fix issues", file=sys.stderr)
            sys.stderr.flush()
    
    # Watch all features/*/cursor/ directories
    src_root = Path("features")
    cursor_dirs = [p for p in src_root.glob("*/cursor") if p.is_dir()]
    
    if not cursor_dirs:
        print("❌ No cursor directories found in features/")
        return
    
    event_handler = BehaviorStructureHandler()
    observer = Observer()
    
    # Watch all cursor/ directories
    for cursor_dir in cursor_dirs:
        observer.schedule(event_handler, str(cursor_dir), recursive=True)
        print(f"👀 Watching: {cursor_dir}", file=sys.stderr)
    
    observer.start()
    print("\n✅ Behavior structure watch mode active. Monitoring files for changes...", file=sys.stderr)
    print("   Press Ctrl+C to stop.", file=sys.stderr)
    sys.stderr.flush()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 Stopping file watcher...", file=sys.stderr)
        sys.stderr.flush()
    
    observer.join()
    print("✅ File watcher stopped", file=sys.stderr)
    sys.stderr.flush()


if __name__ == "__main__":
    import sys
    import io
    
    # Fix Windows console encoding for emoji support
    if sys.platform == "win32":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    
    # Check if watch mode requested
    if len(sys.argv) > 1 and sys.argv[1] == "watch":
        behavior_structure_watch()
    else:
        action = sys.argv[1] if len(sys.argv) > 1 else "validate"
        feature = sys.argv[2] if len(sys.argv) > 2 and sys.argv[1] != "create" else (sys.argv[2] if len(sys.argv) > 2 else None)
        behavior_name = sys.argv[3] if len(sys.argv) > 3 else None
        
        behavior_structure(action, feature, behavior_name)

