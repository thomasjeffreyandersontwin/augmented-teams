### Command: `behavior-consistency-cmd.md`

**Purpose:** When behaviors are changed, deleted, updated, or created, validate for inconsistencies, overlaps, or inconsistent guidance, and surface potential contradictions or redundancies for review.

**Usage:**
* `\behavior-consistency` — check all behaviors
* `\behavior-consistency <feature>` — check one feature
* `python features/cursor-behavior/cursor/behavior-consistency-cmd.py watch` — watch for file changes and auto-check

**When to Run:**
* After behaviors are created, updated, changed, or deleted
* As part of the behavior maintenance workflow (after `\behavior-sync` and `\behavior-index`)
* Before committing behavior changes to catch inconsistencies early

**Steps:**
1. Read from `.cursor/behavior-index.json`.
2. Load behavior file contents from the index.
3. Use OpenAI function calling to analyze behaviors for:
   - Semantic overlaps (same purpose, different approach)
   - Contradictions (opposite guidance for same context)
   - Inconsistencies (naming, tone, or scope mismatch)
4. Group similar or conflicting entries.
5. Generate a summary report (`.cursor/behavior-consistency-report.md`).
6. Flag items for review by the AI or a human maintainer.

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

