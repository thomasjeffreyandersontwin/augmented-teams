# Behavior Consistency Feature

The **Behavior Consistency** feature identifies and summarizes overlapping, inconsistent, or contradictory AI behaviors. It helps keep your AI's behavior library semantically coherent as it grows.

## Implementation

The behavior consistency is implemented according to `behavior-consistency-rule.mdc`:

### Rule Compliance

**Always:**
- ✅ Scan all active rules and commands for similar intent or wording
- ✅ Flag overlaps (same purpose, different approach)
- ✅ Flag contradictions (opposite guidance for the same context)
- ✅ Flag inconsistencies (naming, tone, or scope mismatch)
- ✅ Summarize issues for human review, not automatic enforcement
- ✅ Use OpenAI function calling for semantic analysis

**Never:**
- ✅ Edit, merge, or delete files automatically
- ✅ Treat stylistic differences as inconsistencies
- ✅ Override intentional divergence (e.g., feature-specific exceptions)

### Semantic Analysis

The consistency check uses OpenAI function calling to perform semantic analysis of behavior content. It compares behaviors for:

1. **Overlaps** - Behaviors with similar purpose but different approaches
2. **Contradictions** - Behaviors with opposite guidance for the same context
3. **Inconsistencies** - Behaviors with naming, tone, or scope mismatches

### Configuration

**Environment Setup:**
- Requires `OPENAI_API_KEY` environment variable
- Loads from `behaviors/.env`, `.env`, or system environment
- Install dependencies: `pip install openai python-dotenv`

### Usage

```bash
# Check all behaviors
python behavior-consistency-cmd.py

# Check specific feature
python behavior-consistency-cmd.py <feature>

# Watch mode (auto-check on file changes)
python behavior-consistency-cmd.py watch
```

### Watch Mode

Watch mode automatically runs consistency checks when behavior files change:
- Monitors all `behaviors/*/cursor/` directories
- Triggers check when `.mdc`, `.md`, or `.py` files change
- Debounces rapid changes (waits 2 seconds after last change)
- Shows notifications when checks run

Start watching:
```bash
python behavior-consistency-cmd.py watch
```

Stop watching: Press `Ctrl+C`

### Output

The script generates a markdown report with:
- Summary of behaviors analyzed
- List of overlaps with similarity descriptions
- List of contradictions with conflict descriptions
- List of inconsistencies with issue descriptions
- Recommendations for each issue

### When to Run

* After behaviors are created, updated, changed, or deleted
* As part of the behavior maintenance workflow (after `\behavior-sync` and `\behavior-index`)
* Before committing behavior changes to catch inconsistencies early

### Auto-Triggers

The consistency check runs automatically:
- **On workspace open** via VS Code task `"Behavior Consistency Check"` with `runOn: "folderOpen"`
- **On file changes** via watch mode (start manually or use `"Behavior Watch Mode"` task)

### Integration with Workflow

The consistency check integrates with your existing behavior workflow:

```
1. Edit behavior file → File watcher detects change
2. Run \behavior-sync → Syncs to .cursor/
3. Run \behavior-index → Updates index
4. Consistency check runs automatically → Validates consistency
```

## Related Files

- `behavior-consistency-rule.mdc` - The rule definition
- `behavior-consistency-cmd.md` - Command documentation
- `behavior-consistency-cmd.py` - Implementation
- `BEHAVIOR-WATCH-SETUP.md` - Setup guide for auto-triggers
