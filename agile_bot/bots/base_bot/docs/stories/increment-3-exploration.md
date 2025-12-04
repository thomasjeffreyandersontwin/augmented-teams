# INCREMENT 3: Workflow

**Business Outcome:** Enable seamless transition from one stage to the next, allowing users to automatically pick up work at any stage without having to remember where they left off, with full auditing of what happened in the past.

## Stories with Acceptance Criteria

### Epic: Build Agile Bots
#### Feature: Generate Bot Server And Tools

##### Story: Generate Bot Tools
**Actor:** MCP Server Generator

**Acceptance Criteria:**
- (AC) WHEN MCP Server Generator scans base_actions/ folder
- (AC) THEN Generator discovers actions by reading each action folder
- (AC) AND Generator reads action configuration from each action folder
- (AC) AND action configuration specifies: name, workflow (true/false), order, next_action
- (AC) AND Generator creates tools for all discovered actions
- (AC) AND Tools include workflow state awareness based on action workflow configuration flag

---

##### Story: Generate Behavior Tools
**Actor:** MCP Server Generator

**Acceptance Criteria:**
- (AC) WHEN Generator enumerates behaviors from Bot Config
- (AC) THEN Generator creates behavior-specific tools for each action in base_actions/
- (AC) AND Generator loads action configuration from each action folder
- (AC) AND Workflow actions (workflow: true) get automatic transition logic using next_action field
- (AC) AND Independent actions (workflow: false) get no automatic transition logic
- (AC) AND Each behavior tool knows action sequence from ordered action configuration files

---

### Epic: Invoke MCP Bot Server
#### Feature: Invoke Bot Tool

##### Story: Route To MCP Behavior Tool
**Actor:** AI Chat

**Acceptance Criteria:**
- (AC) WHEN AI Chat invokes bot tool without specifying specific action
- (AC) THEN Router checks Workflow State for current behavior
- (AC) AND Router loads workflow state from {project_area}/workflow state
- (AC) AND Router extracts current_behavior from state
- (AC) AND Router routes to current behavior's MCP tool (not default/first behavior)
- (AC) AND Routing uses saved state to determine correct behavior dynamically

---

##### Story: Forward To Behavior and Current Action
**Actor:** AI Chat → Router

**Acceptance Criteria:**
- (AC) WHEN Router receives behavior tool invocation
- (AC) THEN Router loads Workflow State from persistent storage
- (AC) AND Router extracts current_behavior and current_action from state
- (AC) AND Router forwards call to Bot.Behavior[current_behavior].Action[current_action]
- (AC) AND Forwarding ensures user resumes at exact point they left off
- (AC) AND If workflow state file doesn't exist, defaults to first behavior/first action

---

#### Feature: Perform Behavior Action

##### Story: Inject Next Behavior-Action to Instructions
**Actor:** Base Action

**Acceptance Criteria:**
- (AC) WHEN Workflow action completes execution successfully (workflow: true in action configuration)
- (AC) THEN Action loads its action configuration and reads next_action field
- (AC) WHEN next_action is not null, THEN Action injects instructions: "When done, proceed to [next_action_name]"
- (AC) WHEN next_action is null, THEN Action indicates workflow is complete
- (AC) WHEN action is independent (workflow: false), THEN Action does NOT inject next action instructions
- (AC) AND User doesn't need to remember workflow sequence

---

##### Story: Saves Behavior State
**Actor:** Bot Behavior

**Acceptance Criteria:**
- (AC) WHEN Action execution starts
- (AC) THEN Behavior updates Workflow State with current_behavior, current_action, and action_state="started"
- (AC) WHEN Action execution completes
- (AC) THEN Behavior updates Workflow State with action_state="completed"
- (AC) AND State persisted to {project_area}/workflow state file
- (AC) AND State includes timestamp of last action execution
- (AC) AND State includes action_state (started, completed)
- (AC) AND State includes completed_actions list showing full history with timestamps and states
- (AC) AND State includes current_behavior name
- (AC) AND State includes current_action name
- (AC) AND Persistence ensures workflow can be resumed after interruption (crash, close chat, etc.)
- (AC) AND On resume, if action_state="started", user can choose to retry or continue from that action

---

### Epic: Execute Behavior Actions

#### Feature: Gather Context

##### Story: Track Activity for Gather Context Action
**Actor:** Behavior

**Acceptance Criteria:**
- (AC) WHEN GatherContextAction executes
- (AC) THEN Action creates activity entry with timestamp, action name, behavior name
- (AC) AND Activity entry appended to {project_area}/activity log

---

##### Story: Proceed To Decide Planning
**Actor:** Behavior

**Acceptance Criteria:**
- (AC) WHEN GatherContextAction completes execution
- (AC) THEN Action presents clarification questions and answers to user
- (AC) WHEN Human says action is done
- (AC) THEN GatherContextAction saves Workflow State (per "Saves Behavior State" story)
- (AC) AND GatherContextAction tracks activity (per "Track Activity for Action Execution" story)
- (AC) AND Workflow automatically proceeds to next action per action configuration

---

#### Feature: Decide Planning Criteria

##### Story: Track Activity for Planning Action
**Actor:** Behavior

**Acceptance Criteria:**
- (AC) WHEN PlanningAction executes
- (AC) THEN Action creates activity entry with timestamp, action name, behavior name
- (AC) AND Activity entry appended to {project_area}/activity log

---

##### Story: Proceed To Build Knowledge
**Actor:** Behavior

**Acceptance Criteria:**
- (AC) WHEN PlanningAction completes execution
- (AC) THEN Action presents assumptions and decision criteria to user
- (AC) WHEN Human says action is done
- (AC) THEN PlanningAction saves Workflow State (per "Saves Behavior State" story)
- (AC) AND PlanningAction tracks activity (per "Track Activity for Action Execution" story)
- (AC) AND Workflow automatically proceeds to next action per action configuration

---

#### Feature: Build Knowledge

##### Story: Track Activity for Build Knowledge Action
**Actor:** Behavior

**Acceptance Criteria:**
- (AC) WHEN BuildKnowledgeAction executes
- (AC) THEN Action creates activity entry with timestamp, action name, behavior name
- (AC) AND Activity entry appended to {project_area}/activity log

---

##### Story: Proceed To Render Output
**Actor:** Behavior

**Acceptance Criteria:**
- (AC) WHEN BuildKnowledgeAction completes execution
- (AC) THEN Action generates knowledge graph (structured JSON)
- (AC) WHEN Human says action is done
- (AC) THEN BuildKnowledgeAction saves Workflow State (per "Saves Behavior State" story)
- (AC) AND BuildKnowledgeAction tracks activity (per "Track Activity for Action Execution" story)
- (AC) AND BuildKnowledgeAction submits content for saving (per "Submit Content for Saving" story)
- (AC) AND Workflow automatically proceeds to render_output (auto_progress: true in action configuration)

---

#### Feature: Render Output

##### Story: Track Activity for Render Output Action
**Actor:** Behavior

**Acceptance Criteria:**
- (AC) WHEN RenderOutputAction executes
- (AC) THEN Action creates activity entry with timestamp, action name, behavior name
- (AC) AND Activity entry appended to {project_area}/activity log

---

##### Story: Proceed To Validate Rules
**Actor:** Behavior

**Acceptance Criteria:**
- (AC) WHEN RenderOutputAction completes execution
- (AC) THEN Action transforms knowledge graph to rendered documents
- (AC) WHEN Human says action is done
- (AC) THEN RenderOutputAction saves Workflow State (per "Saves Behavior State" story)
- (AC) AND RenderOutputAction tracks activity (per "Track Activity for Action Execution" story)
- (AC) AND RenderOutputAction submits content for saving (per "Submit Content for Saving" story)
- (AC) AND Workflow automatically proceeds to next action per action configuration

---

#### Feature: Validate Knowledge & Content Against Rules

##### Story: Track Activity for Validate Rules Action
**Actor:** Behavior

**Acceptance Criteria:**
- (AC) WHEN ValidateRulesAction executes
- (AC) THEN Action creates activity entry with timestamp, action name, behavior name, violations count
- (AC) AND Activity entry appended to {project_area}/activity log

---

##### Story: Complete Validate Rules Action
**Actor:** Behavior

**Acceptance Criteria:**
- (AC) WHEN ValidateRulesAction completes execution
- (AC) THEN Action presents validation results to user
- (AC) WHEN Human says action is done
- (AC) THEN ValidateRulesAction saves Workflow State (per "Saves Behavior State" story)
- (AC) AND ValidateRulesAction tracks activity (per "Track Activity for Action Execution" story)
- (AC) AND validate_rules is terminal action (next_action: null in action configuration)

---

##### Story: Track Activity for Validate Rules Action
**Actor:** ValidateRulesAction

**Acceptance Criteria:**
- (AC) WHEN ValidateRulesAction executes
- (AC) THEN Action creates activity entry with timestamp, action name, behavior name, violations count
- (AC) AND Activity entry appended to {project_area}/activity log
- (AC) AND Activity log provides audit trail showing what was validated, when, and results

---

##### Story: Submit Content to Tool for Saving
**Actor:** Base Action

**Acceptance Criteria:**
- (AC) WHEN Action generates or modifies content (knowledge graph, rendered output)
- (AC) THEN Content saved to appropriate location in {project_area}
- (AC) AND Content includes metadata (timestamp, behavior, action that generated it)
- (AC) AND Activity entry created linking action to saved content file path

---

## Domain Concepts (Increment Level)

### Core Concepts:
- **Action Configuration**: Each action folder contains action configuration specifying: name, workflow (true/false), order, next_action, and optional auto_progress flag
- **Workflow Action**: Action with workflow: true in action configuration. Has order number, next_action defined, triggers automatic transitions
- **Independent Action**: Action with workflow: false in action configuration (e.g., correct_bot). No order, no next_action, invoked independently by user, doesn't trigger automatic transitions
- **Workflow State**: Tracks current_behavior, current_action, action_state (started/completed), completed_actions, timestamp, providing the basis for workflow resumption
- **Action Execution State**: Tracks whether action is "started" or "completed", enabling detection of interrupted workflows and allowing user to retry or continue
- **Activity Log**: Audit trail of all action executions with timestamps, inputs, outputs, and results
- **Router**: Routes MCP tool calls to current behavior/action based on Workflow State, not hardcoded defaults
- **State Persistence**: Saves workflow state after every action to enable resumption at any point
- **Action Discovery**: Generator scans base_actions/ folder and reads action configuration from each folder to discover workflow vs independent actions

### Domain Behaviors:
- **Seamless Transition**: System automatically determines next action without user needing to remember workflow sequence
- **Auto Resume**: User can pick up work at exact point they left off by loading Workflow State from persistent storage
- **Audit Trail**: Complete history of what happened (actions executed, content generated, validations performed, timestamps)
- **Sequential Flow**: Actions execute in defined sequence within each behavior
- **State-Based Routing**: Router uses Workflow State to forward to current behavior/action, not hardcoded default behavior
- **Automatic Next Step Injection**: Each action completion injects explicit instructions about next step into AI context

### Domain Rules:
- Each action folder MUST contain action configuration with: name, workflow, order, next_action
- Generator MUST read action configuration from each action folder to determine action type
- Workflow actions (workflow: true) MUST have order and can have next_action
- Independent actions (workflow: false) MUST have workflow: false, order: null, next_action: null
- Workflow State MUST be persisted when action starts (action_state="started") and when action completes (action_state="completed")
- Router MUST check Workflow State before routing to behavior/action
- Activity Log MUST record every action execution with timestamp
- Next action instructions MUST be injected automatically ONLY for workflow actions where next_action is not null
- Independent actions do NOT inject next action instructions
- State file location: {project_area}/workflow state
- Activity log location: {project_area}/activity log
- Action config location: base_actions/{action_name}/action configuration
- If workflow state doesn't exist, default to first behavior's first action
- Workflow State must include: current_behavior, current_action, action_state, completed_actions[], timestamp
- Action state must be one of: "started", "completed"
- If workflow resumes with action_state="started", prompt user to retry or continue that action
- Activity Log entries must include: timestamp, behavior, action, action_state, inputs, outputs, duration
- Each action start and completion must update both Workflow State AND Activity Log
- **CRITICAL: correct_bot has workflow: false - it is NOT part of workflow sequence and has nothing to do with validate_rules**
- **CRITICAL: validate_rules has next_action: null - it is the terminal workflow action**

---

## Source Material

**Exploration Phase:**
- **Primary Source**: agile_bot/bots/base_bot/domain_graph.json - Domain model showing Behavior Workflow, Workflow State, Router, and action concepts
- **Primary Source**: agile_bot/bots/base_bot/docs/stories/story-graph.json - Increment 3 stories (9 stories across 3 epics)
- **Primary Source**: agile_bot/bots/base_bot/docs/stories/increment-2-exploration.txt - Style reference for AC format
- **Date Generated**: 2025-12-03
- **Context**: Exploration of Increment 3: Workflow for base bot, focusing on seamless workflow transitions, auto-resume capability, and complete auditing of workflow execution

