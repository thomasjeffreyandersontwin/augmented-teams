# Bot Template Structure

This template structure is based on the evolved `story_bot` architecture.

## Root Level Files

```
{bot_name}/
├── config/
│   ├── config.json           # Runtime configuration (verbose_mode, etc.)
│   └── bot_config.json       # Bot metadata (name, behaviors list)
├── instructions.json         # Main bot entry point instructions
├── mcp.json                  # MCP server configuration
├── trigger_words.json        # Agent-level trigger patterns
└── rules/                    # Bot-level rules (apply across all behaviors)
    ├── sample_rule_1.json
    └── sample_rule_2.json
```

## Behavior Structure

Each behavior follows a numbered hierarchy with three main subfolders:

```
behaviors/
├── 1_{behavior_name}/
│   ├── instructions.json              # Behavior workflow instructions
│   ├── trigger_words.json             # Behavior-specific trigger patterns
│   ├── 1_guardrails/                  # Context gathering & planning
│   │   ├── instructions.json          # Combined guardrails instructions
│   │   ├── 1_required_context/        # Mandatory questions
│   │   │   ├── instructions.json
│   │   │   ├── key_questions.json
│   │   │   └── evidence.json
│   │   └── 2_planning/                # Decision criteria & assumptions
│   │       ├── instructions.json
│   │       ├── typical_assumptions.json
│   │       ├── recommended_human_activity.json
│   │       └── decision_criteria/
│   │           ├── example_decision_1.json
│   │           └── example_decision_2.json
│   ├── 2_content/                     # Knowledge building & rendering
│   │   ├── instructions.json          # Combined content instructions
│   │   ├── 1_knowledge_graph/         # Build structured knowledge
│   │   │   ├── build_{artifact}_graph.json
│   │   │   ├── {artifact}-graph-{type}.json
│   │   │   └── instructions.json
│   │   ├── 2_render/                  # Generate outputs
│   │   │   └── output.json
│   │   └── 3_synchronize/             # Sync artifacts back to knowledge graph
│   └── 3_rules/                       # Behavior-specific validation rules
│       └── {rule_files}.json
└── 2_{another_behavior}/
    └── (same structure as above)
```

## Key Evolution from Original Template

### 1. **Config Folder Structure** (NEW)
   - Split configuration into separate files
   - `config.json`: Runtime settings
   - `bot_config.json`: Bot metadata and behavior list

### 2. **Root-Level Instructions** (NEW)
   - `instructions.json` at bot root for entry point workflow
   - References base actions and behavior routing

### 3. **Numbered Hierarchy** (NEW)
   - Behaviors: `1_{name}`, `2_{name}`, etc.
   - Subfolders: `1_guardrails`, `2_content`, `3_rules`
   - Nested levels: `1_required_context`, `2_planning`, etc.
   - Shows execution order and priority

### 4. **Instructions at Multiple Levels** (NEW)
   - Bot level: Entry workflow
   - Behavior level: Behavior workflow
   - Subfolder level (guardrails, content): Combined step instructions
   - Provides clear guidance at each level

### 5. **Content Structure** (NEW)
   - Split into 3 sequential phases:
     - `1_knowledge_graph`: Build structured data
     - `2_render`: Generate output artifacts
     - `3_synchronize`: Sync changes back
   - Follows knowledge → rendering → sync pattern
   - Knowledge graph files directly in folder (no templates subfolder)
   - Each phase has its own `instructions.json`

### 6. **Planning Structure** (UPDATED)
   - Multiple decision criteria files in `decision_criteria/` folder
   - Each decision is a separate JSON file with question, options, and outcome
   - Added `typical_assumptions.json` for default assumptions
   - Added `recommended_human_activity.json` for human review guidance
   - Instructions reference these files dynamically

### 7. **Better Rule Organization**
   - Bot-level rules: Apply across all behaviors
   - Behavior-level rules: Specific to that behavior
   - Rules use do/dont format with examples

## Template Variables

The following variables should be replaced when generating a new bot:

### Bot-Level Variables
- `{bot_name}`: Name of the bot (e.g., story_bot, bdd_bot)
- `{bot_description}`: Brief description of bot purpose
- `{bot_goal}`: Main goal statement
- `{behavior_1}`, `{behavior_2}`: Names of behaviors in bot_config.json

### Behavior-Level Variables
- `{behavior_name}`: Name of behavior (e.g., shape, discovery)
- `{behavior_description}`: What the behavior does

### Knowledge Graph Variables
- `{artifact}`: Name of the artifact being built (e.g., story, domain)
- `{artifact}_graph`: Full name with graph suffix
- `{type}`: Type or variant of the artifact (e.g., outline, scenarios)
- `{output_path}`: Where output files are stored
- `{output_filename}`: Name of output file
- `{template_filename}`: Name of template file

### Planning Variables
- `{decision_name}`: Name of a decision criteria
- `{assumption_N}`: Individual assumption statements
- `{activity_N}`: Individual human activity recommendations
- `{option_N}`: Individual decision options

### General Variables
- `{artifact_folder}`: Where artifacts are stored
- `{workspace_path}`: Full path to workspace
- `{output_location}`: Where outputs are generated
- And other context-specific variables in template files

## Usage Pattern

1. **Entry Point**: Bot reads `instructions.json` at root
2. **Behavior Selection**: User confirms which behavior to run
3. **Behavior Execution**: Bot follows `behaviors/{N}_{name}/instructions.json`
4. **Action Sequence**:
   - Initialize Project
   - Gather Context (via 1_guardrails/1_required_context)
   - Decide Planning (via 1_guardrails/2_planning)
   - Build Knowledge (via 2_content/1_knowledge_graph)
   - Render Output (via 2_content/2_render)
   - Validate Rules (via 3_rules)
   - Correct Bot (apply fixes based on validation)

