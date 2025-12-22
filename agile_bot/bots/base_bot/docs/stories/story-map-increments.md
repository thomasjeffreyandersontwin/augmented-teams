# Story Map Increments: Base Bot

**Navigation:** [📋 Story Map](../map/base-bot-story-map.md)

**File Name**: `base-bot-story-map-increments.md`
**Location**: `agile_bot/bots/base_bot/docs/stories/base-bot-story-map-increments.md`

> **CRITICAL MARKDOWN FORMATTING**: All tree structure lines MUST end with TWO SPACES (  ) for proper line breaks. Without two spaces, markdown will wrap lines together into one long line, breaking the visual tree structure.

## Increment Planning Philosophy

**🎯 VERTICAL SLICES - NOT Horizontal Layers**

Each increment should deliver a **thin end-to-end working flow** across multiple features/epics, NOT complete one feature/epic at a time.

- ✅ **DO**: Include PARTIAL features from MULTIPLE epics in each increment
- ✅ **DO**: Ensure each increment demonstrates complete flow: input → process → validate → persist → display
- ✅ **DO**: Layer complexity across increments (simple first, then add users/scenarios/edge cases)
- ❌ **DON'T**: Complete entire Epic A, then Epic B, then Epic C
- ❌ **DON'T**: Build increments that can't demonstrate working end-to-end flow

**Layering Strategy:**
- **Increment 1**: Simplest user + simplest scenario + happy path → Full end-to-end
- **Increment 2**: Add complexity (more options, validations) + Additional users → Full end-to-end  
- **Increment 3**: Add edge cases + Error handling + Advanced features → Full end-to-end

## Legend
- 🎯 **Epic** - High-level capability
- 📂 **Sub-Epic** - Sub-capability (when epic has > 9 features)
- ⚙️ **Feature** - Cohesive set of functionality
- 📝 **Story** - Small increment of behavior (3-12d)

---

## Increment 1: User Manually Drops Config In to AI Chat

Delivers prioritized stories for user manually drops config in to ai chat.

### Stories Included:

- 🎯 **Epic**: Build Agile Bots
  - ⚙️ **Feature**: Generate MCP Tools
    - 📝 Generate Bot Tools

---

## Increment 2: Simplest MCP

Delivers prioritized stories for simplest mcp.

### Stories Included:

- 🎯 **Epic**: Build Agile Bots
  - ⚙️ **Feature**: Generate MCP Tools
    - 📝 Generate MCP Bot Server
    - 📝 Generate Behavior Action Tools
    - 📝 Deploy MCP BOT Server
    - 📝 Restart MCP Server To Load Code Changes

- 🎯 **Epic**: Invoke Bot
  - ⚙️ **Feature**: Invoke MCP
    - 📝 Invoke Bot Tool

- 🎯 **Epic**: Unknown Epic
  - ⚙️ **Feature**: Unknown Sub-Epic
    - 📝 Inject Validation Rules for Validate Rules Action

---

## Increment 3: Workflow

Delivers prioritized stories for workflow.

### Stories Included:

- 🎯 **Epic**: Build Agile Bots
  - ⚙️ **Feature**: Generate MCP Tools
    - 📝 Generate Behavior Tools
    - 📝 Generate MCP Bot Server

- 🎯 **Epic**: Execute Behavior Actions
  - ⚙️ **Feature**: Gather Context
    - 📝 Track Activity for Gather Context Action
    - 📝 Proceed To Decide Planning

- 🎯 **Epic**: Invoke Bot
  - ⚙️ **Feature**: Init Project
    - 📝 Initialize Project Location
  - ⚙️ **Feature**: Invoke MCP
    - 📝 Forward To Current Action
    - 📝 Forward To Current Behavior and Current Action
    - 📝 Track Activity For Workspace
  - ⚙️ **Feature**: Perform Behavior Action
    - 📝 Close Current Action
    - 📝 Execute Behavior
    - 📝 Find Behavior Folder
    - 📝 Invoke Behavior Actions in Workflow Order
    - 📝 Invoke Behavior in Workflow Order

- 🎯 **Epic**: Unknown Epic
  - ⚙️ **Feature**: Unknown Sub-Epic
    - 📝 Inject Knowledge Graph Template and Builder Instructions
    - 📝 Track Activity for Build Knowledge Action
    - 📝 Proceed To Render Output
    - 📝 Load Render Configurations
    - 📝 Inject Template Instructions
    - 📝 Inject Synchronizer Instructions
    - 📝 Track Activity for Render Output Action
    - 📝 Track Activity for Validate Rules Action

---

## Increment 4: CLI

Delivers prioritized stories for cli.

### Stories Included:

- 🎯 **Epic**: Build Agile Bots
  - ⚙️ **Feature**: Generate CLI
    - 📝 Generate BOT CLI code
    - 📝 Generate Cursor Command Files

- 🎯 **Epic**: Invoke Bot
  - ⚙️ **Feature**: Invoke CLI
    - 📝 Invoke Bot CLI
    - 📝 Invoke Bot Behavior CLI
    - 📝 Invoke Bot Behavior Action CLI
    - 📝 Get Help for Command Line Functions

---

## Increment 6: Inject / Store Content

Delivers prioritized stories for inject / store content.

### Stories Included:

- 🎯 **Epic**: Execute Behavior Actions
  - ⚙️ **Feature**: Gather Context
    - 📝 Store Clarification Data
    - 📝 Inject Guardrails As Part Of Clarify Requirements

- 🎯 **Epic**: Invoke Bot
  - ⚙️ **Feature**: Init Project
    - 📝 Store Context Files
    - 📝 Stores Activity for Initialize Project Action
    - 📝 Guards Prevent Writes Without Project
    - 📝 Initialize Project Creates Context Folder
    - 📝 Input File Copied To Context Folder
  - ⚙️ **Feature**: Invoke MCP
    - 📝 Load And Merge Behavior Action Instructions
  - ⚙️ **Feature**: Perform Behavior Action
    - 📝 Inject Next Behavior Reminder

- 🎯 **Epic**: Unknown Epic
  - ⚙️ **Feature**: Unknown Sub-Epic
    - 📝 Load Story Graph Into Memory
    - 📝 Update Existing Knowledge Graph
    - 📝 Save Final Assumptions and Decisions

---

## Increment 7: Code Scanner

Delivers prioritized stories for code scanner.

### Stories Included:

- 🎯 **Epic**: Build Agile Bots
  - ⚙️ **Feature**: Generate LangGraph Framework
    - 📝 Handle Validate Rules Exceptions
    - 📝 Run All Scanners
    - 📝 Run Scanners Against Test Code
    - 📝 Run Scanners Against Code
    - 📝 Load Rules Collection
    - 📝 Find Rule By Name
    - 📝 Iterate Rules
    - 📝 Load Rule From File
    - 📝 Load Scanner For Rule
    - 📝 Get Rule Properties
    - 📝 Create Validation Scope
    - 📝 Load Scanner Class
    - 📝 Load Scanner Classes
    - 📝 Perform Incremental Validation
    - 📝 Validation With All Parameter Combinations
    - 📝 Inject Rules Into AI Chat Message
    - 📝 Example Story
    - 📝 Another Story

- 🎯 **Epic**: Unknown Epic
  - ⚙️ **Feature**: Unknown Sub-Epic
    - 📝 Inject Validation Rules for Validate Rules Action
    - 📝 Discovers Scanners
    - 📝 Run Scanners against Knowledge Graph
    - 📝 Track Activity for Validate Rules Action
    - 📝 Scope Based Parameter Handling

---

## Increment 8: Refactoring

Delivers prioritized stories for refactoring.

### Stories Included:

- 🎯 **Epic**: Build Agile Bots
  - ⚙️ **Feature**: Generate CLI
    - 📝 Generate Help
    - 📝 Generate Cursor Awareness Files
    - 📝 Generate Help Parameters From Action Context Classes

- 🎯 **Epic**: Invoke Bot
  - ⚙️ **Feature**: Init Project
    - 📝 Bootstrap Workspace

- 🎯 **Epic**: Unknown Epic
  - ⚙️ **Feature**: Unknown Sub-Epic
    - 📝 Create Build Scope
    - 📝 Filter Knowledge Graph
    - 📝 Inject Render Instructions And Configs
    - 📝 Get Render Instructions
    - 📝 Merge Base And Render Instructions
    - 📝 Render Output Using Synchronizers
    - 📝 Detect Trigger Words Through Extension
    - 📝 Get Trigger Priority
    - 📝 Match Text Against Triggers
    - 📝 CLI Accepts Scope With Python Dict Syntax
    - 📝 CLI Normalizes Python Dict To JSON
    - 📝 CLI Builds Parameters From Arguments
    - 📝 CLI Handles Scope In Real Usage
    - 📝 CLI Preserves Array Values In Scope
    - 📝 Scope Based Parameter Handling
    - 📝 Validation Parameter Variations
    - 📝 CLI Type Safe Action Context
    - 📝 CLI Context Builder Parses Typed Context
    - 📝 CLI Parser Generator Creates Action Parsers
    - 📝 Insert Context Into Instructions
    - 📝 Inject Status Update Breadcrumbs Into Instructions
    - 📝 Load Bot Configuration
    - 📝 Load Behavior Configuration
    - 📝 Load Bot Behaviors
    - 📝 Load Actions
    - 📝 Load Base Action Configuration
    - 📝 Access Bot Paths
    - 📝 Get Base Instructions
    - 📝 Load Behavior Config
    - 📝 Manage Behaviors Collection
    - 📝 Resolve Bot Paths
    - 📝 Filter Action Based On Scope
    - 📝 Inject Strategy Into Instructions
    - 📝 Store Strategy Data

---

## Increment 9: LangGraph Orchestration

Delivers prioritized stories for langgraph orchestration.

### Stories Included:

- 🎯 **Epic**: Build Agile Bots
  - ⚙️ **Feature**: Generate LangGraph Framework
    - 📝 Generate Base Action Node
    - 📝 Generate Behavior Graph Builder
    - 📝 Generate LangGraph Runner
    - 📝 Generate State Adapter
    - 📝 Build Workflow Graph from Behavior

- 🎯 **Epic**: Invoke Bot
  - ⚙️ **Feature**: Orchestrate Workflow
    - 📝 Route to LangGraph Workflow
    - 📝 Execute Workflow Nodes
    - 📝 Manage Checkpoints
    - 📝 Handle Execution Modes
    - 📝 Resume Workflow from Checkpoint

---

## Source Material

Generated from `story-graph.json`
