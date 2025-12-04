# 📝 Inject Next behavor-Action to Instructions

**Navigation:** [📋 Story Map](../../story-map.txt) | [⚙️ Feature Overview](../README.md)

**Epic:** Invoke MCP Bot Server
**Feature:** Perform Behavior Action

## Story Description

Workflow actions automatically inject next action instructions into AI context upon completion so that users don't need to remember workflow sequence and AI knows what to do next.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Workflow action completes execution successfully (workflow: true in action configuration), **then** Action loads its action configuration and reads next_action field
- **When** next_action is not null, **then** Action injects instructions: "When done, proceed to [next_action_name]"
- **When** next_action is null, **then** Action indicates workflow is complete
- **When** action is independent (workflow: false), **then** Action does NOT inject next action instructions
- **User doesn't need to remember workflow sequence**

## Background

**Common setup steps shared across all scenarios:**

```gherkin
Given action has access to its action configuration file
And action configuration schema includes: name, workflow, order, next_action
And Actions can inject instructions into AI context
```

## Scenarios

### Scenario: Workflow action injects next action instructions on completion

**Steps:**
```gherkin
Given current action is gather_context
And gather_context/action configuration has: workflow=true, order=1, next_action='decide_planning_criteria'
And gather_context action execution completes successfully
When gather_context finalizes execution
Then Action loads gather_context/action configuration
And Action reads next_action field='decide_planning_criteria'
And Action detects next_action is not null
And Action injects instructions into AI context: "When done, proceed to decide_planning_criteria"
And AI knows to invoke decide_planning_criteria tool next
And User does not need to remember that decide_planning_criteria comes after gather_context
```

### Scenario: Terminal action indicates workflow completion (next_action null)

**Steps:**
```gherkin
Given current action is validate_rules
And validate_rules/action configuration has: workflow=true, order=5, next_action=null
And validate_rules action execution completes successfully
When validate_rules finalizes execution
Then Action loads validate_rules/action configuration
And Action reads next_action field=null
And Action detects next_action is null (terminal action)
And Action injects instructions into AI context: "Workflow is complete. No further actions required."
And AI knows workflow has finished
And User is notified that all workflow steps are done
```

### Scenario: Independent action does NOT inject next action instructions

**Steps:**
```gherkin
Given current action is correct_bot
And correct_bot/action configuration has: workflow=false, order=null, next_action=null
And correct_bot action execution completes successfully
When correct_bot finalizes execution
Then Action loads correct_bot/action configuration
And Action reads workflow field=false
And Action detects this is independent action (not workflow action)
And Action does NOT inject next action instructions
And AI does NOT proceed to any specific next action
And User must explicitly invoke next action if desired
```

### Scenario: Action handles missing action configuration gracefully

**Steps:**
```gherkin
Given current action is gather_context
And gather_context/action configuration file does NOT exist
And gather_context action execution completes successfully
When gather_context finalizes execution
Then Action attempts to load action configuration
And Action detects file not found
And Action warns user in chat about missing configuration (non-blocking)
And Action does NOT inject next action instructions
And Workflow continues but without automatic transition guidance
```

### Scenario: Action handles malformed action configuration

**Steps:**
```gherkin
Given current action is decide_planning_criteria
And decide_planning_criteria/action configuration exists but contains invalid JSON
And decide_planning_criteria action execution completes successfully
When decide_planning_criteria finalizes execution
Then Action attempts to parse action configuration
And Action detects JSON parsing error
And Action warns user in chat about malformed configuration (non-blocking)
And Action does NOT inject next action instructions
And Workflow continues but without automatic transition guidance
```

### Scenario: Action injects next action for mid-workflow action

**Steps:**
```gherkin
Given current action is build_knowledge
And build_knowledge/action configuration has: workflow=true, order=3, next_action='render_output'
And build_knowledge is neither first nor last action in workflow
And build_knowledge action execution completes successfully
When build_knowledge finalizes execution
Then Action loads build_knowledge/action configuration
And Action reads next_action field='render_output'
And Action injects instructions: "When done, proceed to render_output"
And AI knows to invoke render_output tool next
And Seamless transition maintains workflow continuity
```

### Scenario: Action with auto_progress flag injects immediate transition

**Steps:**
```gherkin
Given current action is build_knowledge
And build_knowledge/action configuration has: workflow=true, order=3, next_action='render_output', auto_progress=true
And build_knowledge action execution completes successfully
When build_knowledge finalizes execution
Then Action loads build_knowledge/action configuration
And Action reads next_action='render_output' and auto_progress=true
And Action injects instructions: "Automatically proceed to render_output now (no human confirmation needed)"
And AI immediately invokes render_output tool without waiting for user input
And Workflow transitions seamlessly without user intervention
```

### Scenario: First action injects next action instructions

**Steps:**
```gherkin
Given current action is gather_context (first action in workflow)
And gather_context/action configuration has: workflow=true, order=1, next_action='decide_planning_criteria'
And gather_context action execution completes successfully
When gather_context finalizes execution
Then Action loads action configuration
And Action reads next_action='decide_planning_criteria'
And Action injects instructions: "When done, proceed to decide_planning_criteria"
And Workflow begins seamless transition chain from first action
```

## Generated Artifacts

### Injected AI Context Instructions
**Generated by:** Each workflow action on completion  
**Location:** Injected into AI Chat context (not persisted to file)  
**Content:**
- For workflow actions with next_action: "When done, proceed to [next_action_name]"
- For terminal actions (next_action=null): "Workflow is complete. No further actions required."
- For independent actions (workflow=false): No instructions injected

## Notes

- Instruction injection happens ONLY for workflow actions (workflow: true)
- Independent actions (workflow: false) never inject next action instructions
- Terminal actions (next_action=null) indicate workflow completion
- auto_progress flag enables immediate transition without human confirmation
- Missing/malformed configs are non-blocking: warn user but continue
- This feature enables "seamless transition" - users don't need to memorize workflow sequence

---

## Source Material

**Primary Source:** agile_bot/bots/base_bot/docs/stories/increment-3-exploration.txt  
**Sections Referenced:** Perform Behavior Action feature, Domain Concepts (Workflow Action, Independent Action, Seamless Transition, Automatic Next Step Injection)  
**Date Generated:** 2025-12-03  
**Context Note:** Scenarios generated from acceptance criteria and domain rules in increment 3 exploration document


