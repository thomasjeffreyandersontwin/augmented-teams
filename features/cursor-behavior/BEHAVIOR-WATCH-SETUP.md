# Behavior Consistency Auto-Trigger Setup

This guide shows how to automatically trigger behavior consistency checks when behavior files change.

## Options

### Option 0: Auto-on-Start (VS Code/Cursor Workspace) ⭐⭐ Default & Recommended

The consistency check runs automatically when you open the workspace:

**How it works:**
- Configured in `.vscode/tasks.json` with `"runOn": "folderOpen"`
- Runs automatically when Cursor/VS Code opens the workspace
- Managed by `\behavior-sync` command (merges tasks.json from features)
- No manual setup required

**Status:** ✅ Already configured - runs automatically on workspace open

---

### Option 1: File Watcher (Real-Time Changes) - For Active Development

Watch for file changes and automatically run consistency checks:

```bash
# Install watchdog
pip install watchdog

# Start watching
python features/cursor-behavior/cursor/behavior-consistency-cmd.py watch
```

**How it works:**
- Monitors all `features/*/cursor/` directories
- Triggers consistency check when `.mdc`, `.md`, or `.py` files change
- Debounces rapid changes (waits 2 seconds after last change)
- Shows notifications when checks run

**Stop watching:** Press `Ctrl+C`

---

### Option 2: Git Pre-Commit Hook (Before Commits)

Run consistency check before each commit:

```bash
# Copy hook to .git/hooks/
cp features/cursor-behavior/.git-hooks-example.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

**How it works:**
- Runs automatically before `git commit`
- Can block commits if issues are found (modify script to exit 1)
- Or just warns and allows commit

**To disable:** Remove `.git/hooks/pre-commit`

---

### Option 3: GitHub Actions (CI/CD)

Automatically check consistency on push/PR:

```bash
# Copy workflow to .github/workflows/
cp features/cursor-behavior/.github-workflow-example.yml .github/workflows/behavior-consistency.yml

# Add OPENAI_API_KEY secret in GitHub repository settings
```

**How it works:**
- Triggers on push/PR when behavior files change
- Runs consistency check in CI
- Uploads report as artifact
- Can be manually triggered via `workflow_dispatch`

**To configure:**
1. Add `OPENAI_API_KEY` secret in GitHub repo settings
2. The workflow will run automatically

---

## Which Option Should I Use?

- **Default/Recommended**: Option 0 (Auto-on-Start) - Already configured, runs when workspace opens
- **Active Development**: Option 1 (File Watcher) - For real-time feedback on every file change
- **Team/CI**: Use Option 3 (GitHub Actions) - For automated checks on push/PR
- **Strict Control**: Use Option 2 (Git Hook) - To prevent commits with inconsistencies

**Note:** Auto-on-start (Option 0) is already set up via tasks.json. The other options provide additional coverage for specific workflows.

---

## Integration with Existing Workflow

The consistency check integrates with your existing behavior workflow:

```
1. Edit behavior file → File watcher detects change
2. Run \behavior-sync → Syncs to .cursor/
3. Run \behavior-index → Updates index
4. Consistency check runs automatically → Validates consistency
```

If using GitHub Actions, the workflow will:
1. Checkout code
2. Update index
3. Run consistency check
4. Upload report

---

## Troubleshooting

### File Watcher Not Working
- Ensure `watchdog` is installed: `pip install watchdog`
- Check that you're watching from the repository root
- Verify `features/*/cursor/` directories exist

### Git Hook Not Running
- Ensure hook is executable: `chmod +x .git/hooks/pre-commit`
- Check hook is in correct location: `.git/hooks/pre-commit`
- Test manually: `.git/hooks/pre-commit`

### GitHub Actions Not Triggering
- Check workflow file is in `.github/workflows/`
- Verify path patterns match your file structure
- Check `OPENAI_API_KEY` secret is set in repository settings

