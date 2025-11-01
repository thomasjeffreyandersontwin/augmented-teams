### Command: `behavior-consistency-cmd.md`

**Purpose:** When behaviors are changed, deleted, updated, or created, validate for inconsistentencies, overlapping behaviors, or inconsistent guidance, and surface potential contradictions or redundancies for review.

**Usage:**
* `\behavior-consistency` — check all behaviors
* `\behavior-consistency <feature>` — check one feature
* `python features/code-agent-behavior/code-agent-behaviors/code-agent-behavior-consistency-cmd.py watch` — watch for file changes and auto-check

**When to Run:**
* After behaviors are created, updated, changed, or deleted
* As part of the behavior maintenance workflow (after `\behavior-sync` and `\behavior-index`)
* Before committing behavior changes to catch inconsistencies early

**Steps:**
1. The code function reads from the `.cursor/behavior-index.json`.
2. The code function loads behavior file contents from the index.
3. The code function uses OpenAI function calling to analyze behaviors for:
   - Semantic overlaps (same purpose, different approach)
   - Contradictions (opposite guidance for same context)
   - Inconsistencies (naming, tone, or scope mismatch)
4. The code function groups similar or conflicting entries.
5. The code function generates a summary report (`.cursor/behavior-consistency-report.md`).
6. The code function flags items for review by the AI agent or a human maintainer.

**Rule:**
* `\behavior-consistency-rule` — Rule that defines when and how to surface behavioral inconsistencies for review

**Implementation:**
* `behavior_consistency()` — Analyzes behaviors using OpenAI function calling for semantic analysis
* `behavior_consistency_watch()` — Watches for file changes and automatically triggers consistency checks

**AI Usage:**
* OpenAI performs semantic reasoning — analyzing intent, comparing meanings, and highlighting likely inconsistencies using function calling
* The AI identifies overlaps, contradictions, and inconsistencies that require human judgment

**Code Usage:**
* File I/O to read index and behavior files
* OpenAI API calls with structured function schemas for consistency analysis
* Report generation and writing

**Watcher Output Integration:**
* When `behavior_consistency_watch()` runs and generates `.cursor/behavior-consistency-report.md`, the AI should automatically:
  1. Check if the report file exists and has been recently updated (within last 5 minutes)
  2. Read the report content
  3. Present a summary of findings (overlaps, contradictions, inconsistencies) to the user in the chat window
  4. Highlight any critical issues that need immediate attention
* The AI should proactively check for this report when the watcher timestamp (`.cursor/watchers/last-run-consistency.txt`) indicates a recent run
