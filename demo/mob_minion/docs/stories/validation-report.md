# Validation Report - 1 Shape

**Generated:** 2025-12-10 23:57:11
**Project:** mob_minion
**Behavior:** 1_shape
**Action:** validate_rules

## Summary

Validated story map and domain model against **32 validation rules**.

## Content Validated

- **Rendered Outputs:**
  - `story-graph.json`

## Validation Rules Checked

### Rule: Maintain Verb Noun Consistency
**Description:** Maintain verb-noun consistency from epic to feature to story to scenario

### Rule: Map Sequential Spine Vs Optional Paths
**Description:** When mapping stories, carefully distinguish between sequential spine (essential path) and optional paths, alternate routes, or additional functionality that is not strictly essential. Sequential stories form the mandatory flow; optional stories are alternatives, enhancements, or non-essential features.

### Rule: Stories Developed And Tested In Days
**Description:** Write stories that can be developed and tested in a matter of days

### Rule: Stories Follow Invest Principles
**Description:** Ensure stories follow INVEST principles (Independent, Negotiable, Valuable, Estimable, Small, Testable)

### Rule: Story Names Must Follow Verb Noun Format
**Description:** CRITICAL: Story names MUST follow Verb-Noun format (e.g., 'Move To Mob Leaders Turn', 'Determines Target from Strategy', 'Initiate Mob Attack'), and include italicized description showing component interactions (e.g., '*Combat Tracker moves to any mob member's turn, auto moves to mob leader's turn*'). The story name should be concise and action-oriented, while the description shows the component-to-component interactions.

### Rule: Use Active Behavioral Language
**Description:** Use active behavioral language with action verbs. Describe behaviors, not tasks or capabilities.

### Rule: Use Verb Noun Format For Story Elements
**Description:** Use verb-noun format for all story elements (epic names, feature names, story titles)

### Rule: Apply 7 Plus Minus 2 Hierarchy
**Description:** Apply 7±2 rule for hierarchy: epics contain 4-9 sub-epics, sub-epics contain 4-9 stories. Split when exceeding, merge when below minimum.

### Rule: Avoid Noun Redundancy
**Description:** When shaping stories, avoid noun redundancy in domain and concept names

### Rule: Avoid Technical Implementation Language
**Description:** When shaping stories, avoid technical implementation language in user-facing story elements

### Rule: Avoid Technical Stories
**Description:** Technical stories represent implementation tasks that do not describe system behavior. They are normally avoided in favor of user stories and system stories. When technical stories are necessary, they should be marked with story_type: 'technical' and kept minimal.

### Rule: Balance Fine Grained Testable Stories
**Description:** Balance fine-grained stories with testable and valuable independent units. Stories must deliver value and be independently testable.

### Rule: Create Lightweight Precise Docs
**Description:** Create lightweight but precise documentation during shaping. Focus on structure and scope, not detailed specifications.

### Rule: Discover Relationships From Story Map
**Description:** Domain Discovery determines relationships and responsibilities between core domain objects by walking through the story map, then suggests story refinements to rebuild the story map to complement the domain model.

### Rule: Enforce Behavioral Journey Flow
**Description:** When shaping stories, CRITICAL: Stories must show user/system journey flow, not just list operations. Stories must include context (when/why actions happen) and connect logically. Order by user journey, not technical sequential_order.

### Rule: Enforce Functional Accomplishment
**Description:** CRITICAL: Stories must represent complete functional accomplishments, not data access operations or implementation steps. Stories must deliver value independently.

### Rule: Enforce Specificity In Stories
**Description:** CRITICAL: Stories must be specific about what, when, why, and who. Generic operations like 'Add Sub-Epic' or 'Read Epics' are insufficient - stories must include context and specificity.

### Rule: Establish Spine Vs Optional Enhanced Behavior
**Description:** Establish mandatory spine stories vs optional/enhanced behavior stories. When mapping stories, carefully distinguish between sequential spine (essential path) and optional paths, alternate routes, or additional functionality that is not strictly essential. Mandatory stories form the sequential spine (story AND story AND story). Optional stories are alternatives or enhancements (story OR story) that branch from the spine and can return to it. Sequential stories form the mandatory flow; optional stories are alternatives, enhancements, or non-essential sub-epics.

### Rule: Extract Story Map Checklist
**Description:** Quick checklist for extracting story maps from code. Follow this process step-by-step.

### Rule: Extract Story Map From Code
**Description:** CRITICAL: When creating story maps from code, analyze the outermost layer showing end-to-end journey. Locate acceptance tests, human code engagement points (CLI/UI), MCP server definitions, WSDL, API contracts. Analyze operations and domain for major/minor concepts. Create epics/sub-epics based on higher-order goals. Look at distinct behaviors and typical execution order to lay out story journey.

*... and 12 more rules*

## Violations Found

**Total Violations:** 45

### Use Verb Noun Format For Story Elements: 14 violation(s)

- 🔴 **ERROR** - `epics[0].sub_epics[1].name`: Sub_epic name "Change Mob" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - `epics[0].sub_epics[3].story_groups[0].stories[1].name`: Story name "Confirm deletion" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - `epics[1].sub_epics[0].story_groups[0].stories[3].name`: Story name "Confirm assignment" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - `epics[1].sub_epics[1].story_groups[0].stories[2].name`: Story name "Prioritize targets by strategy rules" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - `epics[1].sub_epics[1].story_groups[0].stories[3].name`: Story name "Confirm selection" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - `epics[1].sub_epics[2].name`: Sub_epic name "Set Strategy Options" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - `epics[1].sub_epics[2].story_groups[0].stories[0].name`: Story name "Set attack most powerful target" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - `epics[1].sub_epics[2].story_groups[0].stories[1].name`: Story name "Set attack weakest target" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - `epics[1].sub_epics[2].story_groups[0].stories[3].name`: Story name "Set defend leader strategy" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - `epics[2].sub_epics[1].story_groups[0].stories[4].name`: Story name "Verify completion" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - `epics[2].sub_epics[2].name`: Sub_epic name "Coordinate Actions" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - `epics[2].sub_epics[2].story_groups[0].stories[0].name`: Story name "Coordinate actions" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - `epics[2].sub_epics[2].story_groups[0].stories[1].name`: Story name "Complete sequence" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - `epics[2].sub_epics[2].story_groups[0].stories[3].name`: Story name "Notify completion" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")

### Apply 7 Plus Minus 2 Hierarchy: 6 violation(s)

- 🟡 **WARNING** - `epics[0].name`: Epic "Manage Mobs in Foundry VTT" has 4 4 sub-epics/story groups (should be 5-9)
- 🟡 **WARNING** - `epics[0].sub_epics[3].name`: Sub-epic "Remove Mobs from Foundry VTT" has 3 3 nested sub-epics/stories (should be 5-9)
- 🟡 **WARNING** - `epics[1].name`: Epic "Select Strategies for Mob Behavior" has 3 3 sub-epics/story groups (should be 5-9)
- 🟡 **WARNING** - `epics[1].sub_epics[2].name`: Sub-epic "Set Strategy Options" has 4 4 nested sub-epics/stories (should be 5-9)
- 🟡 **WARNING** - `epics[2].name`: Epic "Execute Mob Actions in Combat" has 3 3 sub-epics/story groups (should be 5-9)
- 🟡 **WARNING** - `epics[2].sub_epics[2].name`: Sub-epic "Coordinate Actions" has 4 4 nested sub-epics/stories (should be 5-9)

### Enforce Specificity In Stories: 9 violation(s)

- 🔴 **ERROR** - `epics[0].sub_epics[1].name`: Sub_epic name "Change Mob" is too generic - add context (e.g., "Process Order Payment" not "Process Payment")
- 🔴 **ERROR** - `epics[0].sub_epics[3].story_groups[0].stories[1].name`: Story name "Confirm deletion" is too generic - add context (e.g., "Process Order Payment" not "Process Payment")
- 🔴 **ERROR** - `epics[1].sub_epics[0].story_groups[0].stories[3].name`: Story name "Confirm assignment" is too generic - add context (e.g., "Process Order Payment" not "Process Payment")
- 🔴 **ERROR** - `epics[1].sub_epics[1].story_groups[0].stories[3].name`: Story name "Confirm selection" is too generic - add context (e.g., "Process Order Payment" not "Process Payment")
- 🔴 **ERROR** - `epics[2].sub_epics[1].story_groups[0].stories[4].name`: Story name "Verify completion" is too generic - add context (e.g., "Process Order Payment" not "Process Payment")
- 🔴 **ERROR** - `epics[2].sub_epics[2].name`: Sub_epic name "Coordinate Actions" is too generic - add context (e.g., "Process Order Payment" not "Process Payment")
- 🔴 **ERROR** - `epics[2].sub_epics[2].story_groups[0].stories[0].name`: Story name "Coordinate actions" is too generic - add context (e.g., "Process Order Payment" not "Process Payment")
- 🔴 **ERROR** - `epics[2].sub_epics[2].story_groups[0].stories[1].name`: Story name "Complete sequence" is too generic - add context (e.g., "Process Order Payment" not "Process Payment")
- 🔴 **ERROR** - `epics[2].sub_epics[2].story_groups[0].stories[3].name`: Story name "Notify completion" is too generic - add context (e.g., "Process Order Payment" not "Process Payment")

### Establish Spine Vs Optional Enhanced Behavior: 10 violation(s)

- 🟡 **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- 🟡 **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- 🟡 **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- 🟡 **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- 🟡 **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- 🟡 **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- 🟡 **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- 🟡 **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- 🟡 **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- 🟡 **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements

### Size Stories 3 To 12 Days: 6 violation(s)

- 🟡 **WARNING** - `epics[0].name`: Epic "Manage Mobs in Foundry VTT" has 4 4 sub-epics/story groups (should be 5-9)
- 🟡 **WARNING** - `epics[0].sub_epics[3].name`: Sub-epic "Remove Mobs from Foundry VTT" has 3 3 nested sub-epics/stories (should be 5-9)
- 🟡 **WARNING** - `epics[1].name`: Epic "Select Strategies for Mob Behavior" has 3 3 sub-epics/story groups (should be 5-9)
- 🟡 **WARNING** - `epics[1].sub_epics[2].name`: Sub-epic "Set Strategy Options" has 4 4 nested sub-epics/stories (should be 5-9)
- 🟡 **WARNING** - `epics[2].name`: Epic "Execute Mob Actions in Combat" has 3 3 sub-epics/story groups (should be 5-9)
- 🟡 **WARNING** - `epics[2].sub_epics[2].name`: Sub-epic "Coordinate Actions" has 4 4 nested sub-epics/stories (should be 5-9)

## Validation Instructions

The following validation steps were performed:

1. **MANDATORY: Before validating any content, you MUST load and review the project's context files:**
2. 1. Load `{project_area}/docs/stories/clarification.json` - Contains key questions and evidence (generated file)
3. 2. Load `{project_area}/docs/stories/planning.json` - Contains assumptions and decisions (generated file)
4. 3. Load `{project_area}/docs/context/input.txt` (or similar) - Original input/source material if needed for validation (original context)
5. 
6. **CRITICAL: File locations:**
7. - **Generated files:** `{project_area}/docs/stories/clarification.json`, `{project_area}/docs/stories/planning.json`
8. - **Original input:** `{project_area}/docs/context/input.txt` and other original context files
9. 
10. These files contain critical requirements, decisions, and context that MUST be checked against during validation.
*... and 47 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\demo\mob_minion\docs\stories\validation-report.md`
