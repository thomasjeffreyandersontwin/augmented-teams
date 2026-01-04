# 📝 Invoke Behavior Actions in Workflow Order

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** Bot Behavior
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Perform Behavior Action](.)  
**Sequential Order:** 4
**Story Type:** user

## Story Description

Invoke Behavior Actions in Workflow Order functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** workflow starts at initialize_project

  **then** user can confirm and save to completed_actions

- **When** user forwards to gather_context

  **then** workflow executes gather_context and saves state

- **When** user closes gather_context

  **then** workflow transitions to decide_planning_criteria

- **When** user jumps to discovery.gather_context (out of order)

  **then** state correctly shows discovery.gather_context (not initialize_project)

- **When** user closes discovery action

  **then** workflow transitions properly

  **and** all completed actions tracked across both behaviors

## Scenarios

### Scenario: Complete end-to-end workflow test demonstrating all fixes working together (happy_path)

**Steps:**
```gherkin
Flow:
1. Start at initialize_project
2. Confirm Ã¢â€ â€™ Saves to completed_actions
3. Forward to gather_context
4. Close gather_context Ã¢â€ â€™ Transitions to decide_planning_criteria
5. Jump to discovery.gather_context (out of order)
6. Verify state shows discovery.gather_context (not initialize_project)
7. Close and verify proper transition
8. Verify all completed actions tracked across both behaviors
```

