---
alwaysApply: true
---

# Cursor Behavior Pattern

## The Problem: Customizing Code Agents

**Goal:** Customize Cursor (and similar code agents) to our specific needs and provide proactive guidance to avoid common AI pitfalls:
- Inconsistent code style and patterns
- Ignoring project conventions
- Creating redundant solutions
- Missing edge cases and validation
- Poor test coverage
- Breaking existing patterns
- Writing code that doesn't align with our architecture

**Challenge:** Without a structured approach, agent customization becomes an unmaintainable mess.

## Customization Mechanisms in Cursor

Cursor provides multiple ways to customize agent behavior:

### 1. Rules (`*.mdc` files in `.cursor/rules/`)
- **Purpose:** Proactive guidance that shapes how AI thinks about problems
- **Scope:** Principles, patterns, checklists, conventions
- **Example:** "Always read file documentation first before writing tests"

### 2. Commands (`*.md` files in `.cursor/commands/`)
- **Purpose:** Executable workflows that AI can invoke
- **Scope:** Parameterized actions, multi-step processes
- **Example:** `@cursor-update-env` to sync feature-local behaviors to global environment

### 3. Code Functions (`*_cmd.py` files in `commands/`)
- **Purpose:** Automated execution of repetitive or complex operations
- **Scope:** Scripts that support commands, automations
- **Example:** `cursor-update-env_cmd.py` that scans features and syncs files

### 4. MCP Tools (Model Context Protocol servers)
- **Purpose:** External tools and services accessible to the agent
- **Scope:** GitHub operations, pipeline management, debugging tools
- **Example:** TDD Pipeline MCP with `get_current_step`, `start_next_step`

## The Problem: Without Structure, Chaos Ensues

When behaviors (rules, commands, code, MCP) are scattered and unorganized, you encounter:

### 1. Conflicting Rules
- Multiple rules stating contradictory approaches
- No clear precedence or resolution
- AI gets confused about which rule to follow
- **Example:** One rule says "use factories" while another says "create objects inline"

### 2. Inconsistent Patterns
- Same concept handled differently across features
- Duplicate but slightly different implementations
- AI can't learn from existing patterns
- **Example:** Test setup done three different ways in three different features

### 3. Overlap and Redundancy
- Same guidance repeated in multiple rules
- Duplicate commands doing similar things
- Confusion about which one to use
 forced duplication makes maintenance harder
- **Example:** Three different commands for "create a command"

### 4. Hard to Move and Share Behavior
- Behaviors are locked to specific locations
- Can't easily extract patterns for reuse
- Hard to version and evolve behaviors
- **Example:** TDD approach spread across multiple disconnected files

### 5. No Clear Ownership
- Don't know which feature a behavior belongs to
- Can't trace why a rule exists
- Hard to update or deprecate safely
- **Example:** Code documentation rules referenced everywhere but owned nowhere

### 6. Deployment Confusion
- Don't know what's actually active vs. stale
- Hard to see what's synced vs. orphaned
- Can't audit what the agent actually sees
- **Example:** Old rule files still in `.cursor/rules/` but source deleted

## The Solution: Treat Each Behavior as a First-Class Feature

**Core Principle:** Every behavior (rule, command, code function, MCP configuration) belongs to a feature and lives in that feature's domain.

### Features as Behavioral Domains

A "behavior" is a coherent set of guidance, automation, and tools that work together around a concept:

- **Test-Driven Development:** Rules for writing tests, commands for debugging, MCP tools for pipeline management
- **Code Documentation:** Rules for documenting code, commands for updating docs, validation
- **Cursor Behavior:** Rules for managing behaviors themselves, commands for syncing, indexing

### Localization: Author at Source

**Pattern:** All behaviors authored in `features/<feature>/cursor/`
- Rules: `features/<feature>/cursor/*.mdc`
- Commands: `features/<feature>/cursor/*-cmd.md`
- Command Functions: `features/<feature>/cursor/*_cmd.py`
- MCP Notes: `features/<feature>/cursor/*-mcp.json`

**Benefit:** Behaviors are co-located with the feature they support. Easy to find, easy to understand context.

### Synchronization: Single Source → Environment

**Pattern:** Feature-local behaviors sync to global Cursor environment
- Rules → `.cursor/rules/`
- Commands → `.cursor/commands/`
- Command Functions → `commands/`

**Benefit:** 
- Single source of truth (feature folder)
- Automatic deployment to where Cursor reads them
- Can track what's active vs. what's orphaned

### Versioning and Evolution

**Pattern:** Behaviors evolve with the feature
- When a feature changes, its behaviors can be updated together
- Behaviors are versioned with the codebase (git)
- Can see behavioral changes in feature PRs

### Cross-References and Dependencies

**Pattern:** Behaviors explicitly reference each other
- Rules reference the commands they rely on
- Commands declare which rules motivate them
- MCP tools documented where they're used

**Benefit:** Clear dependencies, can trace impact of changes

## Principles of the Pattern

### 1. Feature Localization
- Every behavior belongs to a feature
- Behaviors live in that feature's `cursor/` folder
- Makes ownership and context clear

### 2. Single Source of Truth
- Author once in the feature
- Sync to deployment locations
- Index tracks what's active

### 3. Explicit Dependencies
- Rules reference commands
- Commands reference rules
- MCP tools documented where used
- Cross-references keep relationships visible

### 4. Self-Documenting Organization
- Feature name tells you the domain
- File names follow conventions (`-cmd.md`, `_cmd.py`)
- Index shows complete inventory

### 5. Change Detection
- Sync commands detect changes
- Index shows orphaned items
- Reference integrity checks prevent broken links

## Real Example: Test-Driven Development Feature

The `test-driven-development` feature demonstrates the pattern in action:

### Feature Structure
```
features/test-driven-development/cursor/
  ├── tdd-approach.mdc              # Rules for BDD testing patterns
  ├── tdd-mcp-delivery-approach.mdc # Rules for using TDD pipeline MCP
  ├── tdd-playwright-debug-rule.mdc # Rules for E2E debugging
  ├── tdd-mamba-debug-cmd.md        # Command for debugging mamba tests
  └── tdd-mcp.json                  # MCP configuration notes
```

### How Behaviors Work Together

**1. Rules Provide Guidance (`tdd-approach.mdc`)**
- Defines BDD patterns (nouns/states, "should" assertions)
- Specifies test organization principles
- Guides AI on what to test and how

**2. Commands Enable Workflows (`tdd-mamba-debug-cmd.md`)**
- Documents how to debug tests
- References the rules that motivate it
- Can invoke MCP tools for debugging

**3. MCP Tools Provide Infrastructure (`tdd-mcp.json`)**
- TDD Pipeline MCP with tools like `get_current_step`, `start_next_step`
- Enables automated workflow management
- Referenced in rules and commands

**4. Rules Reference Each Other**
- `tdd-mcp-delivery-approach.mdc` explains how to use MCP tools
- `tdd-approach.mdc` explains testing patterns
- Together they form a complete TDD approach

### Synchronization Flow

1. **Author in Feature:** Create `tdd-approach.mdc` in `features/test-driven-development/cursor/`
2. **Sync to Environment:** Run `cursor-update-env_cmd.py` → copies to `.cursor/rules/`
3. **Agent Uses It:** Cursor reads from `.cursor/rules/` when providing guidance
4. **Index Tracks It:** `cursor-behavior-index.mdc` shows it's active and where it came from

### Benefits Demonstrated

- **Clear Ownership:** All TDD behaviors live in `test-driven-development` feature
- **Contextual:** Rules about tests are near the test code
- **Composable:** Rules, commands, and MCP work together as a system
- **Traceable:** Can see all TDD-related behaviors in one place
- **Evolvable:** When TDD approach changes, update one feature folder

## Comparison: Before vs. After

### Before (Unstructured)
```
.cursor/rules/
  ├── testing-rules.mdc          # Some testing guidance
  ├── bdd-patterns.mdc           # Duplicate/overlapping content
  └── test-debugging.mdc         # Unclear ownership

.cursor/commands/
  └── debug-tests.md             # No clear feature connection

commands/
  └── debug_tests.py             # Orphaned, no docs

❌ Problems:
- Which rule is authoritative?
- Where do I update test patterns?
- Is this command still used?
- What belongs to TDD vs. other features?
```

### After (Feature-Based)
```
features/test-driven-development/cursor/
  ├── tdd-approach.mdc           # Complete TDD guidance
  ├── tdd-mamba-debug-cmd.md     # TDD-specific debugging
  └── ... (all TDD behaviors together)

.cursor/rules/                   # Synced from features
  └── tdd-approach.mdc           # Generated, don't edit directly

✅ Benefits:
- Single source of truth (feature folder)
- Clear ownership (TDD feature)
- All related behaviors together
- Easy to find, update, share
```

## See Also

- `cursor-behavior-governance.mdc` — How to implement the pattern (sync, references, maintenance)
- `cursor-behavior-index.mdc` — Inventory of all behaviors and their locations
- `cursor-command-creation.mdc` — How to create commands within this pattern
