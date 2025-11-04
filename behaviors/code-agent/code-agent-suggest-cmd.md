### Command: `behavior-suggest-cmd.md`

**Purpose:** When doing repetitive tasks, suggest creating new behaviors to capture patterns. Help users decide if suggestions belong in an existing behavior-feature, a new behavior-feature, or the current feature being worked on.

**Usage:**
* `\behavior-suggest` — Analyze current session for repetitive patterns and suggest new behaviors

**Rule:**
* `\behavior-suggest-rule` — Rule that triggers behavior suggestions when repetitive patterns are detected

**Implementation:**
* No Python implementation needed — This is entirely AI-driven during conversation

**AI Usage:**
* Analyze conversation history and code patterns to identify repetitive tasks
* Generate suggestions for behavior names, purposes, and placement
* Use natural language to present suggestions (e.g., "Hi, we're doing this a lot. Let's make a new behavior.")
* Help determine appropriate placement (existing behavior-feature, new behavior-feature, or current feature)

**Code Usage:**
* Track repetitive patterns in file operations, code generation, or structural patterns
* Scan existing behavior-features to suggest where new behaviors might belong
* Create behavior scaffolding after user confirmation using `\behavior-structure create`

**Steps:**
1. The AI agent analyzes current session/conversation for repetitive patterns
2. The AI agent identifies common tasks, code structures, or operations being repeated
3. The AI agent generates suggestion with context about the repetitive pattern
4. The AI agent presents suggestion to user in natural language
5. The user provides confirmation or rejection
6. The AI agent asks user where behavior should be placed (existing behavior-feature, new behavior-feature, or current feature)
7. After user confirmation, the AI agent uses `\behavior-structure create` to scaffold the new behavior
