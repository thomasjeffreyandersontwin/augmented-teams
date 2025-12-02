# Increment 2: Simplest MCP - Acceptance Criteria (DRAFT)

## Planning Decisions Applied
- **Granularity:** Inner System (technical interactions, system-to-system, internal behavior)
- **Count:** Stop at full back-and-forth (user-system-user) - atomic and testable slices
- **Consolidation:** Same logic/different data = consolidate; Different formulas = separate; Different validation = separate

---

## Epic: Build Agile Bots
### Sub-Epic: Generate Bot Server And Tools

---

## Story 1: Generate MCP Bot Server

**User:** MCP Server Generator  
**Sequential Order:** 3  
**Story Type:** system

### Acceptance Criteria

- **WHEN** MCP Server Generator receives Bot Config
- **THEN** Generator generates unique MCP Server instance with **Unique server name** from bot name (e.g., "story_bot_server", "bdd_bot_server")
  - THAT leverages**Server initialization code** to start in separate thread
- **AND** Generated server includes Bot Config reference
- **AND** Generated server leverages Specific Bot instantiation code


## Story 2: Generate Behavior Action Tools

**User:** MCP Server Generator  
**Sequential Order:** 1  
**Story Type:** system

### Acceptance Criteria
- **WHEN** Generator processes Bot Config
- **THEN** Generator creates tool code for each (behavior, action) pair:
    - **AND** Enumerates all behaviors and actions from Bot Config (2_gather_context, 3_decide_planning_criteria, 4_build_knowledge, 5_render_output, 6_correct_bot, 7_validate_rules)
    - **AND** For each pair, generates tool code that:
      - **AND** Has unique name: `{bot_name}_{behavior}_{action}`
      - **AND** Loads trigger words from `{bot}/behaviors/{behavior}/{action}/trigger_words.json`
      - **Example:** story_bot with 4 behaviors × 6 base actions = 24 tool instances to generate
      - **AND** Annotates tool with trigger words for lookup
      - **AND** Forwards invocation to Bot + Behavior + Action
      - **AND** Loads instructions and injects into AI Chat
  - **Tool catalog** prepared with all generated tool instances


## Story 3: Deploy MCP BOT Server

**User:** System  
**Sequential Order:** 3  
**Story Type:** system

### Acceptance Criteria

#### AC 1: Deploy and Publish Tool Catalog
- **WHEN** MCP Server code generated and all tools generated
- **THEN** Generator deploys/starts generated MCP Server
- **AND** Server initializes in separate thread
- **AND** Server registers itself with MCP Protocol Handler using unique server name
- **AND** Server publishes tool catalog to AI Chat containing all generated BaseBehavioralActionTools
- **AND** Each tool entry in catalog includes:
  - Unique tool name: `{bot_name}_{behavior}_{action}`
  - Description from instructions.json
  - Trigger patterns from trigger_words.json (for AI Chat to match against user input)
  - Parameters (behavior name, action name, optional user input)
- **AND** AI Chat can discover tools by trigger word pattern matching
- **AND** Server endpoint accessible to AI Chat client

- **WHEN** Tool code generation and deploy completes for each (behavior, action) pair
- **THEN** Generator adds tool to server's tool catalog:
  - **AND** Adds generated tool with unique tool name
  - **AND** Includes trigger word patterns for lookup
  - **AND** Includes tool description and parameters
- **AND** All generated tools added to catalog during server generation

## Story 4: Invoke MCP BOT Tool

**User:** AI Chat  
**Sequential Order:** 4  
**Story Type:** system

#### AC 3: Generated Server Self-Initialization
- **WHEN** Generated MCP Server starts up
- **THEN** Server initializes itself in separate thread
- **AND** Server instantiates Specific Bot class from Bot Config
- **AND** Specific Bot loads Behavior configuration from Bot Config

- **WHEN** Generated MCP Server initializes
- **THEN** Server preloads Specific Bot class from Bot Config
- **AND** Bot class remains in memory for duration of server lifecycle
- **AND** All tool invocations use same preloaded bot instance
- **Technical Constraint:** Preload bot once, reuse across all tool invocations

- **WHEN** AI Chat invokes any generated tool
- **THEN** Tool uses inherited BaseTool logic to invoke correct behavior action on preloaded bot
- **AND** Invocation completes in < 50ms (lookup + forward to bot)
- **AND** Instructions loaded and injected into AI Chat context
- **AND** Total round-trip time < 200ms
- **Technical Constraint:** Cache instructions in memory, minimize I/O

- **WHEN** MCP tool is called for a (behavior, action) pair
  - **THEN** tool directly routes to behavior action method ofpreloaded Bot class
  - **AND** Calls Bot.Behavior.Action with correct parameters
  - **AND** Bot.Behavior compiles and returns instructions 
  - **AND**  MCP tool Injects instructions into AI Chat context

---

## Story 5: Inject Behavior Action Instructions

**User:** Bot Behavior  
**Sequential Order:** 5  
**Story Type:** system

### Acceptance Criteria
- **WHEN** Tool invokes Bot.Behavior.Action method
- **THEN** Behavior Action loads instructions from `{bot}/behaviors/{behavior}/{action}/instructions.json`
- **AND** Behavior Action loads instructions from `base_bot/base_actions/{action}/instructions.json`
- **AND** Action merges base instructions with behavior-specific instructions
- **AND** Compiled instructions returned for injection into AI Chat
- **AND** Behavior Action compiles instructions with behavior-specific context
- **AND** Behavior Action returns compiled instructions to tool

---

## Story 6: Inject Guardrails as Part of Clarify Requirements

**User:** Bot Behavior  
**Sequential Order:** 6  
**Story Type:** system

### Acceptance Criteria

- **WHEN** MCP Specifc Behavior Action Tool invokes Gather Context Action (2_gather_context)
- **THEN** Action checks for guardrails in `{bot}/behaviors/{behavior}/guardrails/required_context/`
- **WHEN** guardrails exist, 
- **THEN**Action loads key_questions.json and evidence.json
- **AND** Action injects guardrails into clarify requirements section of compiled instructions
- **WHEN** no guardrails exist, 
- **THEN** Action injects base clarification instructions only

---

## Story 7: Inject Planning Criteria Into Instructions

**User:** Bot Behavior  
**Sequential Order:** 7  
**Story Type:** system

### Acceptance Criteria

- **WHEN** MCP Specific Behavior Action Tool invokes Planning Action (3_decide_planning_criteria)
- **THEN** Action checks for guardrails in `{bot}/behaviors/{behavior}/guardrails/planning/`
- **WHEN** guardrails exist,
- **THEN** Action loads typical_assumptions.json and decision_criteria/*.json files
- **AND** Action injects planning guardrails into planning section of compiled instructions
- **WHEN** no guardrails exist,
- **THEN** Action injects base planning instructions only

---

## Story 8: Inject Knowledge Graph Template for Build Knowledge

**User:** Bot Behavior  
**Sequential Order:** 8  
**Story Type:** system

### Acceptance Criteria

- **WHEN** MCP Specific Behavior Action Tool invokes Build Knowledge Action (4_build_knowledge)
- **THEN** Action loads knowledge graph template from `{bot}/behaviors/{behavior}/content/knowledge_graph/`
- **AND** Action loads build instructions from knowledge graph spec files
- **AND** Action injects knowledge graph template path and build instructions into compiled instructions
- **AND** Action injects validation rules reference (see Story 10: Inject Validation Rules)

---

## Story 9: Inject Render Templates and Transformers

**User:** Bot Behavior  
**Sequential Order:** 9  
**Story Type:** system

### Acceptance Criteria

- **WHEN** MCP Specific Behavior Action Tool invokes Render Output Action (5_render_output)
- **THEN** Action loads render templates from `{bot}/behaviors/{behavior}/content/render/templates/`
- **AND** Action loads transformer methods from `{bot}/behaviors/{behavior}/content/render/transformers/`
- **AND** Action loads render spec from behavior content configuration
- **AND** Action injects template path, transformer path, and spec path into compiled instructions

---

## Story 10: Inject Validation Rules for Validate Rules Action

**User:** Bot Behavior  
**Sequential Order:** 10  
**Story Type:** system

### Acceptance Criteria

- **WHEN** MCP Specific Behavior Action Tool invokes Validate Rules Action (7_validate_rules)
- **THEN** Action loads common bot rules from `base_bot/rules/`
- **AND** Action loads behavior-specific rules from `{bot}/behaviors/{behavior}/rules/`
- **AND** Action merges common and behavior-specific rules
- **AND** Action injects rules into validation section of compiled instructions
- **AND** Rules define validation criteria for generated content

---

## Story 11: Load Correct Bot Instructions

**User:** Bot Behavior  
**Sequential Order:** 11  
**Story Type:** system

### Acceptance Criteria

- **WHEN** MCP Specific Behavior Action Tool invokes Correct Bot Action (6_correct_bot)
- **THEN** Action loads correct bot instructions from `base_bot/base_actions/6_correct_bot/instructions.json`
- **AND** Action injects correction instructions into compiled instructions
- **AND** Instructions guide how to review and correct generated content

---

## Folder Structure

```
agile_bot/bots/
├── base_bot/
│   ├── src/
│   │   ├── generator.py          # MCP Server Generator code
│   │   ├── base_mcp_server.py    # Base MCP Server implementation
│   │   ├── base_tool.py          # BaseTool inheritance logic
│   │   └── base_bot.py           # Base Bot class
│   ├── config/
│   │   └── mcp_config.json       # General MCP configuration
│   ├── lib/
│   │   ├── fastmcp/              # FastMCP library
│   │   └── [other dependencies]
│   └── docs/
│
├── story_bot/                    # Example specific bot
│   ├── src/
│   │   ├── story_bot_server.py   # Generated specific MCP server
│   │   ├── story_bot.py          # Specific Bot class
│   │   └── tools/                # Generated tool code
│   │       ├── story_bot_shape_gather_context.py
│   │       ├── story_bot_shape_decide_planning_criteria.py
│   │       ├── [etc... N×6 tools]
│   ├── config/
│   │   └── tool_config.json      # Specific tool configuration
│   └── behaviors/
│       ├── 1_shape/
│       ├── 2_discovery/
│       ├── [etc...]
│
└── [other specific bots: bdd_bot, domain_bot, etc.]
```

## Tool Catalog Structure per Bot

For each bot, Generator creates tool catalog:

```
Generated MCP Server (e.g., "story_bot_server")
├── Unique Server Name: "story_bot_server"
├── Tool Catalog containing BaseBehavioralActionTools:
│   ├── story_bot_shape_gather_context
│   ├── story_bot_shape_decide_planning_criteria
│   ├── story_bot_shape_build_knowledge
│   ├── story_bot_shape_render_output
│   ├── story_bot_shape_validate_rules
│   ├── story_bot_shape_correct_bot
│   ├── (repeat for each behavior: discovery, exploration, specification)
│   └── Total: N behaviors × 6 base actions = N×6 tools
└── Each tool inherits from base_bot/src/base_tool.py
```

---

## File Locations

**Base Bot (agile_bot/bots/base_bot/):**
- Generator code: `src/generator.py`
- Base MCP Server: `src/base_mcp_server.py`
- Base Tool: `src/base_tool.py`
- Base Bot class: `src/base_bot.py`
- General MCP config: `config/mcp_config.json`
- Dependencies: `lib/fastmcp/` and other libs

**Specific Bot (e.g., agile_bot/bots/story_bot/):**
- Generated server: `src/story_bot_server.py`
- Specific bot class: `src/story_bot.py`
- Generated tools: `src/tools/story_bot_{behavior}_{action}.py`
- Tool config: `config/tool_config.json`
- Behaviors: `behaviors/{behavior}/` folders

---

## Out of Scope for Increment 2

The following are explicitly **OUT OF SCOPE** for this increment:
- **Project State Manager** - state persistence
- **Workflow State** - tracking current behavior/action
- **Workflow** - orchestrating behavior-action sequences
- **State management** - will be added in future increments

This increment focuses ONLY on:
- MCP Server generation and deployment (in base_bot/src/)
- Tool generation (in <specific_bot>/src/tools/)
- Basic invocation and instruction injection
- NO state persistence or workflow management

---

## Notes for Editing

- Add/remove/modify acceptance criteria as needed
- Adjust timing constraints if too aggressive/lenient
- Clarify domain responsibilities if ambiguous
- Add edge cases or error scenarios if missing
- Flag any consolidation opportunities I missed
- Verify tool hierarchy aligns with implementation plan
- Ensure no workflow/state management leaked into acceptance criteria


