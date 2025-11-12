# Story Code Agent Implementation Plan

## Overview
Build a complete story code agent feature following the code-agent pattern, with rules, commands, runners, templates, and heuristics based on the Story Writing Training PowerPoint content.

### Implementation Approach
This plan is organized by **phases** that align with the story writing workflow. Each phase contains:
- **Principles**: Rules and guidelines specific to this phase
- **Commands**: CLI commands that implement the phase
- **Templates**: Structural templates for artifacts
- **Runner & Heuristics**: Code implementation and validation

### Phases
1. **Phase 0: Foundation** - Universal principles, base rules, common infrastructure
2. **Phase 1: Shape** - Story shaping with increments (`/story-shape` creates decomposition + increment maps + folders)
3. **Phase 2: Discover** - Finalize stories for next increment (`/story-discovery`)
4. **Phase 3: Explore** - Write acceptance criteria into feature docs (`/story-explore`)
5. **Phase 4: Specification Scenarios** - Fill story template with scenarios (`/story-specification-scenarios`)
6. **Phase 5: Specification Examples** - Finish story template with examples (`/story-specification-examples`)

## PowerPoint Analysis Summary

### Major Stages Identified (3 stages):

1. **Story Shaping** (formerly "Idea Shaping")
   - Story Shaping in a Nutshell
   - Introduction To Story Mapping
   - Identifying Marketable Increments Of Value

2. **Discovery**
   - Discovery in a Nutshell
   - Refining Marketable Increments of Value on Your Story Map
   - Story Mapping Practices to Encourage & Avoid
   - Planning, Scheduling, & Forecasting

3. **Story Exploration**
   - Story Exploration in a Nutshell
   - Writing Story Acceptance Criteria
   - Refining Your Story Map During Story Exploration
   - Defining System Level Stories
   - Story Specification
   - Story Testing

## PowerPoint Content Extracted and Integrated

**Source Material**: `behaviors/stories/docs/story-training-content.md` (PowerPoint text extraction)
**Source Material**: `behaviors/stories/docs/ppt_full_extraction.txt` (Complete PowerPoint extraction with tables/images)
**Comprehensive Guide**: `behaviors/stories/docs/story-templates-and-heuristics.md` (Templates, Examples, Heuristics)

✅ **All semantic/structural patterns have been extracted from the PowerPoint and integrated into:**
1. **Templates** - 6 concrete templates for each command (story map, story, acceptance criteria, scenarios, examples)
2. **Real Examples** - Concrete examples from PowerPoint slides (Direct Pay, Pharmacy, Trading examples)
3. **Heuristics** - Specific detection patterns with regex for validation (StoryLanguageHeuristic, StoryMapHeuristic, etc.)
4. **Principles** - DO/DON'T examples with PowerPoint slide references throughout this document

---

---

## Implementation Overview

The implementation is organized into **phases** below. Each phase contains everything needed:

**Phase Structure:**
- **Overview** - What this phase accomplishes
- **Principles** - Rules and guidelines specific to this phase
- **Commands** - CLI commands that implement the phase
- **Templates** - Concrete templates for artifacts (with PowerPoint examples)
- **Heuristics** - Validation patterns with regex (Python classes)
- **Runner Implementation** - Code structure and methods
- **Examples** - Real examples from PowerPoint training material

All key concepts, patterns, templates, and heuristics are integrated into their respective phases below.

---

# IMPLEMENTATION PHASES

---

## Phase 0: Foundation (Universal & Cross-Phase)

### Overview
Foundation phase establishes universal principles, base rules, and common infrastructure that all subsequent phases depend on.

### 0.1 Universal Principles

These principles apply to **ALL commands across ALL phases**.

#### Principle 0.1: Stories Are Action-Oriented and Describe Interactions
- **Source**: Slides 12, 14, 15
- **[DO]** (Agent-Relevant):
  - Focus stories on user interactions and how the system behaves as observed by users
  - Describe interactions between users and systems
  - Write stories so they can be tested
  - Ensure stories can be developed and tested in a matter of days
  - Make stories action-oriented statements of user and system behavior
  - Use behavioral language: "submits", "views", "validates", "sends", "displays"
  - Describe observable behavior: "User submits order", "System validates payment"
- **[DON'T]** (Agent-Relevant):
  - Focus on delivery or development tasks required to build a system
  - Focus on system internals (technical stories)
  - Write stories that don't represent a small increment of system behavior in response to an end user action
  - Use development task language: "implement", "create", "refactor", "optimize", "fix", "build", "set up"
  - Use technical implementation details: "query database", "call API", "update table", "refactor code"
  - Write technical stories that describe low-level internal behavior we don't care about

#### Principle 0.2: INVEST Principles
- **Source**: Slide 12
- **[DO]** (Agent-Relevant):
  - Ensure stories are Negotiable, Testable, Valuable, Estimate-able, Small, and Independent
  - Write stories that are a unit of scope and value
  - Deliver stories in features and increments
  - Write stories so they can be tested
  - Ensure stories can be developed and tested in a matter of days
- **[DON'T]** (Agent-Relevant):
  - Create stories that violate INVEST principles
  - Write stories that are too large or interdependent
- **[Structural Patterns]**:
  - **Small**: 3-12 day effort range, complete interaction flow, 2-5 acceptance criteria
  - **Independent**: Can be delivered without other stories, no blocking dependencies
  - **Testable**: Has acceptance criteria in behavior form, observable outcomes
  - **Valuable**: Delivers measurable value independently

### 0.2 Document Content Rules

**Critical**: Different document levels have different content:
- **Story Map Document** (`story-map-decomposition.md` or `story-map-increments.md`): NO acceptance criteria, hierarchy and counts only
- **Epic Document** (`epic-doc.md`): NO acceptance criteria, epic description and feature list
- **Feature Document** (`feature-doc.md`): **HAS acceptance criteria** (When...then) under each story (filled during Explore phase)
- **Story Document** (`story-doc.md`): Full story spec template, progressively filled:
  - Acceptance criteria (copied from feature-doc or written here)
  - **Scenario Phase** → Fills in scenarios section
  - **Examples Phase** → Fills in examples section

**Note**: During **Explore phase**, acceptance criteria go into **Feature documents** under each story. Story documents can reference or include them for full specification.

### 0.3 Base Story Rule Creation

#### File: `behaviors/stories/stories-rule.mdc`
- **Structure**: Follow `code-agent-rule.mdc` pattern with frontmatter, conventions, 5 major principle sections
- **Content**: 
  - **Section 0: Universal Principles** (⚠️ **Universal**)
    - Principle 0.1: Action-oriented stories
    - Principle 0.2: INVEST principles
  - **Section 0.5: All Phases Principles** (⚠️ **All Phases**)
    - Principle 0.5.1: Epic/Feature/Story hierarchy
  - **Section 1: Story Shaping principles** (⚠️ **Stage: Story Shaping**)
  - **Section 2: Discovery principles** (⚠️ **Stage: Discovery**)
  - **Section 3: Story Exploration principles** (⚠️ **Stage: Story Exploration**)

#### Command Applicability Format
- Universal principles: ⚠️ **Universal**
- All phases/stages: ⚠️ **All Phases**
- Stage-specific: ⚠️ **Stage: Story Shaping**
- Command-specific: ⚠️ **Commands: story-shape, story-market-increments**

### 0.4 Rule Command Files
- `behaviors/stories/rule/stories-rule-cmd.md` - Main command
- `behaviors/stories/rule/stories-rule-generate-cmd.md` - Generate delegate
- `behaviors/stories/rule/stories-rule-validate-cmd.md` - Validate delegate

### 0.5 Common Runner Enhancement

#### Add Prompting Questions Concept
- **File**: `behaviors/common_command_runner/common_command_runner.py`
- **New Concept**: Prompting Questions - Prerequisite context validation
- **Purpose**: Ensure required context is available before plan/generate runs
- **Implementation**:
  - Add `prompting_questions` attribute to `Command` class (list of question strings)
  - Add `check_prompting_questions()` method to `CodeAugmentedCommand` class
  - Method checks if questions are answered in the provided context
  - If not answered: AI generates prompts to ask user those questions
  - If answered: Proceeds with normal flow
  - **Workflow Integration**:
    - `generate()` and `plan()` methods check prompting questions FIRST
    - Only proceed if questions are answered (or after asking them)

### 0.6 Stories Runner Base
- **File**: `behaviors/stories/stories_runner.py`
- **Base**: Extend from `common_command_runner` framework
- **Structure**: Follow `behaviors/bdd/bdd-runner.py` pattern
- **No OperationCommand needed** - using standard Command pattern

### 0.7 Universal Templates

#### Story Map Template
- **File**: `behaviors/stories/map/story-map-template.md`
- **Purpose**: Standard structure for story maps (used across all phases)

#### Story Template
- **File**: `behaviors/stories/write/story-template.md`
- **Purpose**: Standard structure for individual stories (used across all phases)

#### Acceptance Criteria Template
- **File**: `behaviors/stories/acceptance/acceptance-criteria-template.md`
- **Purpose**: Standard structure for acceptance criteria (used in Explore phase)

---

## Phase 1: Shape

### Overview
Shape phase creates the initial story map with hierarchical decomposition AND identifies marketable value increments. These are combined because increments are identified during shaping.

**Artifacts Created by `/story-shape`:**
- ✅ `story-map-decomposition.md` - Hierarchical decomposition (Epic > Sub-Epic > Feature > Story)
- ✅ `story-map-increments.md` - Reorganized by marketable value increments (MVI as top level)
- ✅ Folder structure matching hierarchy: `/[system]/[epic]/[feature]/[story]/`
- ✅ Epic documents (`epic-doc.md`) - NO acceptance criteria
- ✅ Feature documents (`feature-doc.md`) - NO acceptance criteria
- ✅ Story placeholders (only 10-20% to highlight critical/unique/architecturally critical functionality)
- ✅ Story counts (~X stories) for unexplored areas
- ✅ Story effort estimates (Xd) - **Inputted by AI and human together**
  - AI analyzes patterns and **recommends splitting** stories > 12d
  - Human provides domain knowledge for estimates
  - AI validates against 3-12d range
- ❌ NO detailed stories beyond 10-20% highlights
- ❌ NO acceptance criteria at any level during shaping

**Principles from Phase 0 that apply here:**
- Principle 0.1: Action-Oriented Stories (Universal)
- Principle 0.2: INVEST Principles (Universal)

### 1.1 Phase-Specific Principles (⚠️ Stage: Story Shaping)

#### Principle 1.1: Epic/Feature/Story Hierarchy
- **Source**: Slides 1, 119, 187-189
- **[DO]** (Agent-Relevant):
  - Use Epic, Feature, Story hierarchy structure
  - Organize stories within features and features within epics
  - Apply hierarchy during shaping, increments, discovery, and exploration
- **[DON'T]** (Agent-Relevant):
  - Skip hierarchy levels without justification
  - Mix hierarchy levels inconsistently
- **[Structural Patterns]**:
  - **Format**: Epic → Feature → Story (nested hierarchy)
  - **Epic**: High-level business capability or initiative
  - **Feature**: Cohesive set of functionality within epic
  - **Story**: Small increment of behavior within feature
- **[Phase Applicability]**: Shaping, Market Increments, Discover, Explore (NOT in Specification Scenarios/Examples)

#### Principle 1.2: Focus Story Maps on User AND System Activities
- **Source**: Slides 1, 4
- **[DO]** (Agent-Relevant):
  - Focus story maps on both user AND system activities
  - Use story maps to outline user and system behavior
  - Break/group stories so that most fall into a 3-12 day effort range
  - Enable frequent feedback by decomposing the work into smaller items
  - Enable high quality feedback by grouping work into meaningful chunks
  - Include both user activity patterns ("User submits", "Customer places") AND system activity patterns ("System validates", "System sends")
- **[DON'T]** (Agent-Relevant):
  - Arbitrarily decompose stories to a functional level, regardless of size
  - Focus only on user activities (ignore system activities)
  - Focus only on tasks (instead of activities)
- **[Structural Patterns]**:
  - **User Activity Detection**: Contains patterns like `^(User|Customer|Admin|\w+)\s+\w+` with user actions (submits, views, places)
  - **System Activity Detection**: Contains patterns like `^(System|\w+)\s+(validates|sends|processes|displays|notifies)`
  - **Task Detection** (avoid): Contains `\b(implement|create|build|set up|write|develop)\b`
  - **Validation**: Story map must contain BOTH user activity patterns AND system activity patterns
- **[Examples from PowerPoint]**:
  - ✅ Slide 119 (Direct Pay): "Generate Customer Bill", "Render Bill According to Preferences"
  - ✅ Slide 187-189 (Pharmacy): "Login", "RX Intake", "Validate Renewal", "Notify Prescriber"
  - ❌ "Implement billing system" (task, not activity)
  - ❌ "Set up RX database" (infrastructure, not activity)

#### Principle 1.2: Balance Fine-Grained with Testable/Valuable
- **Source**: Slide 2
- **[DO]** (Agent-Relevant):
  - Balance fine-grained stories with testable/valuable stories
  - Ensure stories are fine-grained enough to enable frequent feedback
  - Ensure stories are grouped into meaningful chunks for high quality feedback
  - Validate that a business expert can understand the language of most of the stories
  - Focus the language on the business domain
  - Create a common artifact that serves a wide variety of stakeholders
  - Create lightweight but precise documentation over a tome of illegible content
- **[DON'T]** (Agent-Relevant):
  - Create stories that are too fine-grained without being testable or valuable
  - Create stories that are too large to be testable or deliverable quickly
  - Use generic function, verbs, nouns without context
  - Use overly technical, IT concepts, unless core to domain being discussed
- **[Examples from PowerPoint]**:
  - ✅ Slide 1: 7d, 5d stories (appropriate size)
  - ❌ Slide 1: 15d story (too large, should be split)

#### Principle 1.3: Use Business Language That is Specific and Precise
- **Source**: Slide 3
- **[DO]** (Agent-Relevant):
  - Ground the map in business language that is specific and precise
  - Focus the language on the business domain
  - Use verb/noun language
  - Use language that emphasizes performing an operation on an explicit thing
  - Use domain-specific terms: "order", "customer", "payment", "inventory"
  - Use specific verb/noun combinations: "[Actor] [specific verb] [specific noun]"
- **[DON'T]** (Agent-Relevant):
  - Use generic functions, verbs, nouns without context
  - Use overly technical IT concepts, unless core to domain being discussed
  - Use static functional concepts
- **[Examples from PowerPoint]**:
  - ✅ "Customer places order" (specific verb/noun)
  - ✅ "System validates payment" (specific action)
  - ❌ "Process order" (generic verb)
  - ❌ "Order Management" (static functional concept)

#### Principle 1.4: Use Active Behavioral Language
- **[DO]** (Agent-Relevant):
  - Favor active behavioral language over functional/capability breakup
  - Use story maps to outline user and system behavior (NOT tasks)
  - Use action verbs: "submits", "views", "validates", "sends", "displays"
  - Describe behaviors: "[Actor] [action] [object]"
- **[DON'T]** (Agent-Relevant):
  - Use functional or capability-based language instead of behavioral language
  - Focus on tasks instead of behaviors
  - Use capability nouns: "Management", "Processing", "Administration"
  - Use task verbs: "implement", "create", "build", "set up"
- **[Examples from PowerPoint]**:
  - ✅ "Place order" (active behavior)
  - ✅ "Validate payment" (active behavior)
  - ❌ "Order Management" (capability)
  - ❌ "Payment Processing" (capability)

### 1.2 Commands (2 commands - run together)

#### Command 1.2A: `/story-shape`

**Purpose**: Create story map shell and elaborate/extrapolate scope.

**Command Files**:
- `behaviors/stories/shape/story-shape-cmd.md` (+ generate, validate)

**Prompting Questions**:
- What is the product or feature vision?
- Who are the target users or stakeholders?
- What are the main user goals or outcomes?
- What is the scope boundary (what's in/out)?
 - What are the business priorities or strategic goals?
- What are the market constraints or deadlines?
- Are there any dependencies between increments?

**Creates**:
- Story map decomposition with hierarchy
- Epic/Sub-Epic/Feature structure with counts
- Story placeholders (10-20% for critical/unique/architecturally critical)
- NO acceptance criteria
- Use ~X stories for unexplored areas
: `story-map-decomposition-template.md` map organized by epic / feature/story
- `story-map-increments.md` - Map reorganized with increments as top level
- Increment folder structure (filtered hierarchy)
- Increment documents with priority and relative sizing
- Can have partial epics/features in increments
- NO acceptance criteria

### 1.3 Templates: Story Map Decomposition

#### Template 1A: `story-map-decomposition-template.md`

**File**: `behaviors/stories/map/story-map-decomposition-template.md`

**Structure**: Hierarchical decomposition during shaping (detail may be missing, use counts)

```markdown
# Story Map: [Product/Feature Name]

## System Purpose
[High-level description of what this system/product does]

---

## Epic: [Verb] [Noun] *[optional clarifier] (6 features, 20 stories)
**Description**: [Business capability]

### Sub-Epic: [Actor] [Noun] *[optional clarifier] (3 features, 12 stories)
**Description**: [Sub-capability within epic]

#### Feature: [Verb] [Noun] *[optional clarifier] (approx 7 stories)
**Description**: [Cohesive functionality]

##### Story: [Verb] [Noun]
##### Story: [Verb] [Noun]
##### Story: [Verb] [Noun]
... [4 more stories - extrapolated]

#### Feature: [Verb] [Noun] *[optional clarifier] (approx 4 stories)
**Description**: [Cohesive functionality - not yet decomposed]

### Sub-Epic: [Actor] [Noun] (2 features, 8 stories)
[Not yet decomposed]

---

## Epic: [Verb] [Noun] (4 features, 15 stories)
[Not yet decomposed - estimated based on similar epics]

---

## Notes
- During shaping, detail will be missing - use story counts
- Format: Epic/Sub-Epic/Feature with (X features, Y stories) counts
- Explored areas show actual stories
- Unexplored areas show counts only
- NO acceptance criteria at this level
```

**PowerPoint Example (Slide 119 - Direct Pay, adapted with counts)**:
```markdown
# Story Map: Direct Pay System

## System Purpose
Enable direct billing and payment processing for customer transactions with configurable pricing

---

## Epic: Manage Direct Pay Billing (2 features, 10 stories)

### Feature: Generate Customer Billing (5 stories) - EXPLORED

#### Story: Generate Customer Bill (7d)
#### Story: Render Bill According to Preferences (5d)
#### Story: Calculate Bill Totals (3d)
#### Story: Apply Tax Rules (4d)
#### Story: Send Bill Notification (3d)

### Feature: Configure Pricing (approx 5 stories)
[Not yet decomposed - similar complexity to Customer Billing]

---

## Epic: Process Payments (approx 3 features, 15 stories)
[Not yet decomposed - estimated based on similar payment systems]
```

#### Template 1B: Folder Structure with Documents

**Folder Structure Created During Shaping**:
```
/story-maps/
  /direct-pay-system/
    story-map-decomposition.md          # Top-level map (NO acceptance criteria)
    
    /epic-manage-direct-pay-billing/
      epic-doc.md                        # Epic-level document (NO acceptance criteria)
      
      /feature-generate-customer-billing/
        feature-doc.md                   # Feature document (HAS acceptance criteria under each story)
        
        /story-generate-customer-bill/
          story-doc.md                   # Story spec (filled in explore phase)
        
        /story-render-bill-preferences/
          story-doc.md
      
      /feature-configure-pricing/
        feature-doc.md                   # Feature document (when explored)
    
    /epic-process-payments/
      epic-doc.md                        # Epic-level document
```

**Document Content Rules:**
- **Story Map Document** (`story-map-decomposition.md`): NO acceptance criteria, hierarchy and counts only
- **Epic Document** (`epic-doc.md`): NO acceptance criteria, epic description and feature list
- **Feature Document** (`feature-doc.md`): HAS acceptance criteria (When...then) under each story when explored
- **Story Document** (`story-doc.md`): Full story spec (title, AC, scenarios, examples)

#### Template 1C: Feature Document with Acceptance Criteria

**File**: `behaviors/stories/feature/feature-doc-template.md`

```markdown
# Feature: [Verb] [Noun] *[optional clarifier]

**Epic**: [Epic Name]
**Story Count**: 5 stories
**Status**: Explored / In Progress / Complete

## Feature Description
[What this feature does]

---

## Domain Acceptance Criteria
**Purpose**: Identify domain concepts, constraints, and relationships that span multiple stories.
**Source**: PowerPoint Slide 121

### Domain Concepts

#### Concept: [Concept Name]
**Responsibilities**: [What this concept is responsible for]
**Relationships**: [How it relates to other concepts]
**Constraints**: [Business rules, validations, limits]

**Examples**:
- A Customer Bill **is generated from** Chargeable Activities
- A Price Item **is configured for** a specific Type of Chargeable Activity
- A Bill **must include** all relevant Chargeable Activities for the Billing Period

---

## Stories
**Behavioral Acceptance Criteria (When...then) under each story**

### Story: Generate Customer Bill (7d)

**When** a Billing Period is completed
**Then** the System will generate a Customer Bill for all relevant Chargeable Activity

**When** a Customer requests a Customer Bill from their Product Home page
**Then** the system will render the Customer Bill according to their Bill Preferences

---

### Story: Render Bill According to Preferences (5d)

**When** Customer requests bill
**Then** system renders bill according to their preferences

**When** bill format is PDF
**Then** system generates PDF format

**When** bill format is HTML
**Then** system displays HTML format

---

### Story: Calculate Bill Totals (3d)

**When** bill is generated
**Then** system calculates total from all chargeable activities

---

## Notes
- Feature-level document includes TWO types of acceptance criteria:
  1. **Domain AC**: Domain concepts, constraints, relationships (feature level)
  2. **Behavioral AC**: When...then format under each story (story level)
- Used during discovery/explore phases
- Links to individual story documents for full specifications
```

**PowerPoint Example (Slide 119 - with acceptance criteria)**:
```markdown
# Feature: Generate Customer Billing

**Epic**: Direct Pay Billing
**Story Count**: 5 stories
**Status**: Explored

## Stories

### Story: Generate Customer Bill (7d)

**When** a Billing Period is completed
**Then** the System will generate a Customer Bill for all relevant Chargeable Activity

**When** a Customer requests a Customer Bill from their Product Home page
**Then** the system will render the Customer Bill according to their Bill Preferences

### Story: Render Bill According to Preferences (5d)

[Acceptance criteria to be added during explore phase]
```

### 1.4 Heuristics: Story Map Validation

**Class**: `StoryMapHeuristic`

```python
class StoryMapHeuristic:
    """Validates story map structure and content"""
    
    BEHAVIORAL_VERBS = ['submit', 'view', 'place', 'receive', 'validate', 'send', 
                        'display', 'notify', 'process', 'calculate', 'generate',
                        'render', 'configure', 'link', 'store', 'retrieve', 'dispense',
                        'intake', 'renew']
    
    TASK_VERBS = ['implement', 'create', 'build', 'develop', 'write', 'code',
                  'refactor', 'optimize', 'fix', 'set up', 'install', 'deploy']
    
    GENERIC_VERBS = ['process', 'handle', 'manage', 'get', 'set', 'do', 'make']
    
    def validate_story_map(self, story_map_content: str) -> dict:
        """
        Validate story map structure (Slides 1, 4, 119, 187-189)
        
        Returns:
        {
            'has_hierarchy': bool,
            'has_user_activities': bool,
            'has_system_activities': bool,
            'story_sizing_appropriate': bool,
            'uses_business_language': bool,
            'violations': [list of violation dicts]
        }
        """
        violations = []
        
        # Check for Epic/Feature/Story hierarchy
        has_epic = bool(re.search(r'\bEpic:', story_map_content, re.IGNORECASE))
        has_feature = bool(re.search(r'\bFeature:', story_map_content, re.IGNORECASE))
        has_story = bool(re.search(r'\bStory:', story_map_content, re.IGNORECASE))
        has_hierarchy = has_epic and has_feature and has_story
        
        if not has_hierarchy:
            violations.append({
                'type': 'MISSING_HIERARCHY',
                'severity': 'ERROR',
                'message': 'Story map missing Epic/Feature/Story hierarchy',
                'suggestion': 'Use Epic → Feature → Story hierarchy structure',
                'slide_reference': 'Slide 1, 119, 187-189'
            })
        
        # Check for user activities (Slide 1, 187-189)
        user_patterns = [
            r'\bUser\s+\w+',
            r'\bCustomer\s+\w+',
            r'\bAdmin\s+\w+',
            r'\bStaff\s+\w+',
            r'\b[A-Z]\w+\s+(submits|views|places|selects|requests|confirms|login)'
        ]
        has_user_activities = any(re.search(p, story_map_content, re.IGNORECASE) for p in user_patterns)
        
        # Check for system activities (Slide 1, 187-189)
        system_patterns = [
            r'\bSystem\s+(validates|sends|processes|displays|generates|calculates)',
            r'\b\w+\s+service\s+(validates|sends|processes|displays)',
            r'\b(validates|sends|processes|generates|calculates|renders|dispenses|notifies)\s+\w+'
        ]
        has_system_activities = any(re.search(p, story_map_content, re.IGNORECASE) for p in system_patterns)
        
        if not has_user_activities:
            violations.append({
                'type': 'MISSING_USER_ACTIVITIES',
                'severity': 'ERROR',
                'message': 'Story map missing user activities',
                'suggestion': 'Add stories describing user actions (e.g., "User submits order", "Customer places order")',
                'slide_reference': 'Slide 1, 4, 187'
            })
        
        if not has_system_activities:
            violations.append({
                'type': 'MISSING_SYSTEM_ACTIVITIES',
                'severity': 'ERROR',
                'message': 'Story map missing system activities',
                'suggestion': 'Add stories describing system behavior (e.g., "System validates payment", "System sends confirmation")',
                'slide_reference': 'Slide 1, 4, 187'
            })
        
        # Check for task-oriented language (Slide 14, 134)
        for verb in self.TASK_VERBS:
            if re.search(rf'\b{verb}\s+\w+', story_map_content, re.IGNORECASE):
                violations.append({
                    'type': 'TASK_ORIENTED',
                    'severity': 'ERROR',
                    'message': f'Story map contains task-oriented language: "{verb}"',
                    'suggestion': 'Replace tasks with user/system behaviors',
                    'slide_reference': 'Slide 14, 109, 134'
                })
                break
        
        # Check story sizing (Slide 1)
        story_sizes = re.findall(r'(\d+)d', story_map_content, re.IGNORECASE)
        too_large = [int(s) for s in story_sizes if int(s) > 12]
        
        if too_large:
            violations.append({
                'type': 'STORY_TOO_LARGE',
                'severity': 'WARNING',
                'message': f'Stories exceed 12-day maximum: {too_large}',
                'suggestion': 'Split large stories into smaller increments (3-12 day range)',
                'slide_reference': 'Slide 1'
            })
        
        return {
            'has_hierarchy': has_hierarchy,
            'has_user_activities': has_user_activities,
            'has_system_activities': has_system_activities,
            'story_sizing_appropriate': len(too_large) == 0,
            'uses_business_language': len([v for v in violations if v['type'] == 'TASK_ORIENTED']) == 0,
            'violations': violations
        }
```

### 1.5 Runner Implementation

#### Inner Class: `StoryShapeCommand(Command)`
- **Location**: `behaviors/stories/stories_runner.py`
- **Methods**:
  - `generate()` - Generate story map shell with elaboration
  - `validate()` - Validate against Story Shaping principles
  - `prompting_questions` - List of prerequisite questions

#### CLI Wrapper: `StoryShapeCodeAugmentedCommand(CodeAugmentedCommand)`
- **Wraps**: `StoryShapeCommand`
- **CLI Entry Points**:
  - `generate` - Create/elaborate story map
  - `validate` - Validate story map structure
  - `execute` - Combined generate + validate

#### Principle 1.5: Identifying Marketable Increments of Value
- **Source**: Slide 10
- **[DO]:**
  - Identify marketable increments of value during Story Shaping
  - Do just enough story mapping to extrapolate how many epics, features, and stories make up an increment
  - Continually identify and refine marketable increments
  - During Idea Shaping and Discovery, continually identify and refine Marketable Increments
- **[DON'T]:**
  - Over-elaborate story mapping during shaping
  - Skip increment identification

#### Principle 1.6: Relative Sizing Upstream
- **Source**: Slide 10
- **[DO]:**
  - Use relative sizing upstream for larger buckets of scope
  - Compare and contrast new work against previously completed work
  - Relatively size increments and initiatives against each other
  - Relatively size against previously delivered increments of value that are similar in platform and team skills
  - Conduct relative sizing where size actually matters (upstream and for larger buckets of scope)
  - At any point, assess work by comparing and contrasting it to work previously completed
- **[DON'T]:**
  - Use relative sizing only at story level (should be upstream at initiative/increment level)
  - Size work without comparing to similar previously completed work

### 1.7 Template: Story Map with Increments

#### Template 1B: `story-map-increments-template.md`

**File**: `behaviors/stories/map/story-map-increments-template.md`

**Structure**: Top level is increments ordered by delivery priority. Can have stories, features, epics (may not be complete epic/feature, but put them here anyway in same hierarchy).

```markdown
# Story Map with Increments: [Product/Feature Name]

## System Purpose
[High-level description]

---

## MVI 1: [Increment Name] - NOW
**Relative Size**: Compared to [Previously delivered increment X]
**Description**: [What value this increment delivers]

### Epic: [Verb] [Noun] *[clarifier] (PARTIAL - 1 of 2 features)

#### Feature: [Verb] [Noun] - EXPLORED

##### Story: [Verb] [Noun]
##### Story: [Verb] [Noun]
##### Story: [Verb] [Noun]

### Epic: [Verb] [Noun] (COMPLETE - all 3 features)

#### Feature: [Verb] [Noun]

##### Story: [Verb] [Noun]
##### Story: [Verb] [Noun]

#### Feature: [Verb] [Noun]

##### Story: [Verb] [Noun]
##### Story: [Verb] [Noun]

#### Feature: [Verb] [Noun]

##### Story: [Verb] [Noun]

---

## MVI 2: [Increment Name] - NEXT
**Relative Size**: Compared to MVI 1
**Description**: [What value this increment delivers]

### Epic: [Verb] [Noun] (PARTIAL - remaining features from Epic in MVI 1)

#### Feature: [Verb] [Noun] (approx 5 stories)
[Not yet explored]

---

## Notes
- Increments are top level, ordered by priority
- Can have partial epics/features in an increment
- Same hierarchy structure (Epic > Feature > Story)
- NO acceptance criteria at this level
- Folder structure mirrors this organization
```

#### Template 1C: Increment Folder Structure

**Folder Structure Created During Market Increments Phase**:
```
/story-maps/
  /direct-pay-system/
    story-map-increments.md                    # Increment-organized map
    
    /mvi-1-basic-billing/                      # Increment folder (top level)
      increment-doc.md                         # Increment document
      
      /epic-manage-direct-pay-billing/         # Epic folder (filtered to increment)
        epic-doc.md
        
        /feature-generate-customer-billing/
          feature-doc.md
          
          /story-generate-customer-bill/
            story-doc.md
          
          /story-render-bill-preferences/
            story-doc.md
      
      /epic-process-payments/                  # Another epic in this increment
        epic-doc.md
        
        /feature-payment-validation/
          feature-doc.md
    
    /mvi-2-advanced-features/
      increment-doc.md
      
      /epic-manage-direct-pay-billing/         # Same epic, remaining features
        epic-doc.md
        
        /feature-configure-pricing/
          feature-doc.md
```

**Note**: Increment folder structure is filtered view of the complete story map, organized by delivery priority.

### 1.8 Heuristics: Story Map and Increment Validation

**Class**: `StoryMapHeuristic` (validates decomposition)
**Class**: `MarketIncrementHeuristic` (validates increments)

```python
class MarketIncrementHeuristic:
    """Validates marketable increment identification (Slide 10)"""
    
    def validate_increments(self, story_map_content: str) -> dict:
        """Validate increment markers and structure"""
        violations = []
        
        # Check for increment markers
        increment_patterns = [
            r'Increment\s+\d+:',
            r'MVI\s+\d+:',
            r'Marketable\s+Value\s+Increment\s+\d+:'
        ]
        has_increments = any(re.search(p, story_map_content, re.IGNORECASE) for p in increment_patterns)
        
        if not has_increments:
            violations.append({
                'type': 'MISSING_INCREMENTS',
                'severity': 'ERROR',
                'message': 'Story map missing marketable increment markers',
                'suggestion': 'Add increment markers (e.g., "MVI 1: [Increment Name]")',
                'slide_reference': 'Slide 10'
            })
        
        # Check for prioritization
        priority_patterns = [r'Priority:\s*(High|Medium|Low)', r'P\d+']
        has_prioritization = any(re.search(p, story_map_content, re.IGNORECASE) for p in priority_patterns)
        
        if not has_prioritization:
            violations.append({
                'type': 'MISSING_PRIORITIZATION',
                'severity': 'WARNING',
                'message': 'Increments missing prioritization',
                'suggestion': 'Add priority levels to increments (High/Medium/Low)'
            })
        
        # Check for relative sizing
        relative_size_patterns = [
            r'Relative\s+Size:',
            r'Compared\s+to:',
            r'Similar\s+to:'
        ]
        has_relative_sizing = any(re.search(p, story_map_content, re.IGNORECASE) for p in relative_size_patterns)
        
        if not has_relative_sizing:
            violations.append({
                'type': 'MISSING_RELATIVE_SIZING',
                'severity': 'INFO',
                'message': 'Increments missing relative sizing information',
                'suggestion': 'Compare increment size to previously delivered work (Slide 10 principle)',
                'slide_reference': 'Slide 10'
            })
        
        return {
            'has_increments': has_increments,
            'has_prioritization': has_prioritization,
            'has_relative_sizing': has_relative_sizing,
            'violations': violations
        }
```

**Note**: Market increment logic integrated into `StoryShapeCommand` - no separate command needed.

---

## Phase 2: Discover

### Overview
Discover phase refines marketable increments, applies story mapping practices, and grooms stories for next increment.

**Principles from Phase 0 that apply here:**
- Principle 0.1: Action-Oriented Stories (Universal)
- Principle 0.2: INVEST Principles (Universal)
- Principle 0.5.1 (from Phase 1): Epic/Feature/Story Hierarchy (carries forward for map refinement)

**Principles from Phase 1 that apply here:**
- Principle 1.1: User AND System Activities
- Principle 1.2: Balance Fine-Grained with Testable/Valuable
- Principle 1.3: Business Language
- Principle 1.4: Active Behavioral Language

### 2.1 Phase-Specific Principles (⚠️ Stage: Discovery)

#### Principle 2.1: Refining Marketable Increments on Story Map
- **[DO]:**
  - Refine marketable increments on story map during Discovery
  - Update story map based on discovery insights
  - Ensure increments are well-defined
  - Continually identify and refine marketable increments
- **[DON'T]:**
  - Skip increment refinement during discovery
  - Ignore discovery insights when updating story map

#### Principle 2.2: Story Mapping Estimation and Counting
- **Source**: Slides 5, 6, 7, 8, 9, 11
- **[DO]** (Agent-Relevant - Mapping Context):
  - Add story counts to epics and features where exact stories are unknown (extrapolation)
  - Use story counts instead of detailed story lists when completing the full map is not desired
  - Mark extrapolated story counts (e.g., "~X stories" or "Extrapolated: ~[X stories")
  - Switch from estimating story details to simply counting stories in the map
  - Add story counts to help understand scope without fully decomposing every story
- **[DON'T]** (Agent-Relevant - Mapping Context):
  - Require complete story decomposition before adding counts to the map
  - Estimate only at story level (should add counts upstream at epic/feature level)
  - Focus on detailed story estimation when mapping (use counts instead)
  - **IGNORE**: Point-based estimation, velocity tracking, sprint planning, throughput calculations, forecasting formulas

#### Principle 2.3: Story Refinement
- **Source**: Slide 11
- **[DO]** (Agent-Relevant):
  - Identify stories that are too ambiguous
  - Split work into smaller stories before accepting
  - Ensure stories are small (can be completed quickly)
  - Identify stories that can be completed quickly
- **[DON'T]** (Agent-Relevant):
  - Accept stories that are too ambiguous
  - Accept stories that are too large

### 2.2 Command: `/story-discovery`

#### Purpose
Guide through discovery stage for next market increment.

#### Command Files
- **Main**: `behaviors/stories/discovery/story-discovery-cmd.md`
- **Delegates**: `story-discovery-generate-cmd.md`, `story-discovery-validate-cmd.md`

#### Prompting Questions
- Which market increment are we focusing on for discovery?
- What new information or insights have been discovered?
- Are there any changes to business priorities or constraints?
- What is the target delivery timeline for this increment?

#### Content
- Refine marketable increments on story map
- Update story map based on discovery insights
- Ensure increments are well-defined
- Continually identify and refine marketable increments
- Apply story mapping practices (from principles)
- Groom stories for next increment

### 2.3 Template: Refined Story Map with Story Counts

**Uses base Story Map Template with additions for story counting**:

```markdown
### Feature: Order Processing
**Description**: Complete order lifecycle management
**Story Count**: ~15 stories

#### Story: Customer places order (5d)
#### Story: System validates payment (3d)
#### Story: System sends confirmation (3d)
... [12 more stories - extrapolated, not yet decomposed]

**Note**: Extrapolated story count based on similar features delivered previously
```

### 2.4 Heuristics: Discovery Validation

**Class**: `StoryDiscoveryHeuristic`

```python
class StoryDiscoveryHeuristic:
    """Validates discovery refinements (Slides 5-11)"""
    
    def validate_discovery(self, refined_map: str, original_map: str) -> dict:
        """Validate refinement occurred and story analysis applied"""
        violations = []
        
        # Check for refinement (content changed)
        content_changed = refined_map != original_map
        
        if not content_changed:
            violations.append({
                'type': 'NO_REFINEMENT',
                'severity': 'WARNING',
                'message': 'Story map appears unchanged during discovery',
                'suggestion': 'Refine increments based on discovery insights',
                'slide_reference': 'Slide 10, 11'
            })
        
        # Check for story counts (extrapolation)
        has_story_counts = bool(re.search(r'~\d+\s+stories', refined_map, re.IGNORECASE))
        has_extrapolation = bool(re.search(r'extrapolat', refined_map, re.IGNORECASE))
        
        if not (has_story_counts or has_extrapolation):
            violations.append({
                'type': 'MISSING_STORY_COUNTS',
                'severity': 'INFO',
                'message': 'Story map missing story count extrapolations for unexplored areas',
                'suggestion': 'Add story counts (e.g., "~15 stories") to features not yet decomposed',
                'slide_reference': 'Slide 8, 9, 10'
            })
        
        return {
            'refinement_occurred': content_changed,
            'has_story_counts': has_story_counts or has_extrapolation,
            'violations': violations
        }
```

### 2.5 Runner Implementation

#### Inner Class: `StoryDiscoveryCommand(Command)`
- **Location**: `behaviors/stories/stories_runner.py`
- **Methods**:
  - `generate()` - Refine increments and groom stories
  - `validate()` - Validate discovery refinements
  - `prompting_questions` - List of prerequisite questions

#### CLI Wrapper: `StoryDiscoveryCodeAugmentedCommand(CodeAugmentedCommand)`
- **Wraps**: `StoryDiscoveryCommand`
- **CLI Entry Points**:
  - `generate` - Perform discovery
  - `validate` - Validate refinements
  - `execute` - Combined generate + validate

---

## Phase 3: Explore

### Overview
Explore phase writes acceptance criteria (into Feature documents), refines story map during exploration, and defines system level stories.

**Artifacts Created by `/story-explore`:**
- ✅ Feature documents updated with **Domain Acceptance Criteria** (domain concepts, constraints, relationships)
- ✅ Feature documents updated with **Behavioral Acceptance Criteria** (When...then format) under each story
- ✅ Story document templates created (empty - filled in Phases 4 & 5)
- ✅ Story map refined (split/merge stories as needed)
- ❌ NO scenarios yet (added in Phase 4)
- ❌ NO examples yet (added in Phase 5)

**Principles from Phase 0 that apply here:**
- Principle 0.1: Action-Oriented Stories (Universal)
- Principle 0.2: INVEST Principles (Universal)
- Principle 0.5.1 (from Phase 1): Epic/Feature/Story Hierarchy (minor - only for map refinement if needed)

**Principles from Phase 1 that apply here:**
- Principle 1.1: User AND System Activities
- Principle 1.2: Balance Fine-Grained with Testable/Valuable
- Principle 1.3: Business Language
- Principle 1.4: Active Behavioral Language

### 3.1 Phase-Specific Principles (⚠️ Stage: Story Exploration)

#### Principle 4.1: Writing Story Acceptance Criteria (Behavioral and Domain)
- **Source**: Slides 13, 16, 119, 121
- **[DO]** (Agent-Relevant):
  - Write **behavioral acceptance criteria** for every story in When...then format
  - Write **domain acceptance criteria** for feature identifying major concepts, constraints, relationships
  - Use "When...then..." format for behavioral AC
  - Use "[Concept] [relationship] [Concept]" format for domain AC (Slide 121)
  - Identify domain concepts that span multiple stories
  - Describe concept responsibilities, information, constraints, relationships
  - Make acceptance criteria the main focus (story summary provides context)
  - Write acceptance criteria that describe conditions story must meet to be accepted as complete by Product Owner
- **[DON'T]** (Agent-Relevant):
  - Skip acceptance criteria for stories
  - Skip domain acceptance criteria for features
  - Write acceptance criteria in technical or task-oriented language
  - Make story summary the main focus (acceptance criteria should be primary)
- **[Domain AC Format]** (Slide 121):
  - "A [Concept] [interaction/relationship] [Another Concept]"
  - Example: "A Customer Bill is generated from Chargeable Activities"
  - Example: "A Price Item is configured for a Type of Chargeable Activity"
  - Example: "A Billing Period must have at least one Chargeable Activity"
- **[Structural Patterns]**:
  - **Format**: `When [condition], then [outcome]` or `Given [context], When [action], Then [outcome]`
  - **Behavior Form**: Uses behavioral language, describes user/system interactions, observable outcomes
  - **Technical Form** (avoid): Uses code patterns, implementation details, function calls
  - **Required Elements**: Condition (trigger), Outcome (observable result), Testability
- **[Examples from PowerPoint]**:
  - ✅ Slide 119: "When a Billing Period is completed, then the System will generate a Customer Bill for all relevant Chargeable Activity"
  - ✅ Slide 119: "When a Customer requests a Customer Bill from their Product Home page, then the system will render the Customer Bill according to their Bill Preferences"
  - ❌ "When payment.validate() is called, then return true" (code pattern)

#### Principle 3.2: Refining Story Map During Exploration
- **Source**: Slide 16, 124
- **[DO]:**
  - Refine/merge/split stories as necessary during exploration
  - Ensure stories expressed at small/similar level of details
  - Update story map based on exploration insights
  - Keep focus on completeness from user/system behavior perspective
- **[DON'T]:**
  - Skip story refinement during exploration
  - Leave stories at inconsistent levels of detail
  - Lose focus on user/system behavior completeness

#### Principle 3.3: Defining System Level Stories
- **Source**: Slides 132-138
- **[DO]:**
  - Identify and define system-level stories (not just user-facing)
  - Ensure system behavior is captured
  - Focus on how system behaves in response to user interactions
  - Document system activities alongside user activities
- **[DON'T]:**
  - Focus only on user-facing stories
  - Ignore system behavior
  - Skip system-level story definition

#### Principle 3.4: Story Format and Structure
- **Source**: Slide 15, 136
- **[DO]** (Agent-Relevant):
  - Use simple title to convey meaning (when story maps are in place)
  - Make acceptance criteria the main focus
  - Use story summary only to provide context
  - Write stories that represent a small increment of system behavior in response to an end user action
- **[DON'T]** (Agent-Relevant):
  - Use typical agile story template without understanding its purpose
  - Write "stories" that don't represent a small increment of system behavior in response to an end user action
  - Make story summary the main focus (acceptance criteria should be primary)
- **[Structural Patterns]**:
  - **With Story Maps**: Simple title format: `[Verb] [Noun]` (e.g., "Place order")
  - **Without Story Maps**: Full format: `As a [User] I want to [Action] So that [Value]`
  - **Required Fields**: Title (verb/noun), Acceptance Criteria (behavior form)
  - **Optional Fields**: Summary/Description (provides context only)

### 3.5 Command: `/story-explore`

#### Purpose
Guide through story exploration stage - writing acceptance criteria, refining map, defining system stories.

#### Command Files
- **Main**: `behaviors/stories/explore/story-explore-cmd.md`
- **Delegates**: `story-explore-generate-cmd.md`, `story-explore-validate-cmd.md`

#### Prompting Questions
- Which feature or slice are we exploring?
- Which stories need acceptance criteria?
- Are there any system-level concerns or technical constraints?
- Who are the stakeholders that need to share understanding?

#### Content
- Write **behavioral acceptance criteria** for each story (When...then format)
- Write **domain acceptance criteria** for feature (domain concepts, constraints, relationships)
- Refine story map during exploration
- Define system level stories
- Ensure acceptance criteria are in behavior form
- Share common understanding of next feature/slice

**Two Types of Acceptance Criteria:**
1. **Behavioral AC** (under each story): When...then format describing user/system interactions
2. **Domain AC** (at feature level): Domain concepts, constraints, relationships that span multiple stories

### 3.6 Template: Story Document (Spec Template)

#### Template 3A: `story-doc-template.md`

**File**: `behaviors/stories/write/story-doc-template.md`

**Location**: `/story-maps/[system]/[epic]/[feature]/[story]/story-doc.md`

**Purpose**: Story-level document is the spec template that gets progressively filled in:
- **Scenario Phase**: Fills in scenarios section (`/story-specification-scenarios`)
- **Examples Phase**: Fills in examples section (`/story-specification-examples`)

**Note**: Acceptance criteria are already in the Feature document (filled during Explore phase). Story doc references or includes them.

```markdown
# Story: [Verb] [Noun]

## Story Information
**Feature**: [Feature Name]
**Epic**: [Epic Name]
**Type**: User Activity / System Activity
**Estimated Effort**: [X]d
**Status**: Not Started / In Progress / Complete

## Story Summary (Optional - only when story maps not present)
As a [User/Actor]
I want to [Perform Action]
So that [I Receive Value]

---

## Acceptance Criteria
**Source**: From Feature document (filled during Explore phase)

### AC1: [Brief Description]
**When** [user/system action or condition]
**Then** [expected outcome/behavior]

### AC2: [Brief Description]
**When** [user/system action or condition]
**Then** [expected outcome/behavior]

### AC3: [Brief Description]
**Given** [context]
**When** [action]
**Then** [outcome]

---

## Scenarios
**Status**: TO BE FILLED in Phase 5 (`/story-specification-scenarios`)

[Scenarios will be added here - including Background, Scenario Outline, etc.]

---

## Examples  
**Status**: TO BE FILLED in Phase 6 (`/story-specification-examples`)

[Examples will be added here - including Normal Examples, Scenario Outline with Examples table, etc.]

---

## Notes
- Story doc is the complete spec template
- **Phase 4 (Explore)**: Creates this template with AC section
- **Phase 5 (Spec Scenarios)**: Fills in Scenarios section
- **Phase 6 (Spec Examples)**: Fills in Examples section
- Each phase builds on the previous
```

**PowerPoint Example (Slide 119 - Generate Customer Bill)**:
```markdown
# Story: Generate Customer Bill

## Story Information
**Feature**: Customer Billing
**Epic**: Direct Pay Billing
**Type**: System Activity
**Estimated Effort**: 7d

## Acceptance Criteria

### AC1: Bill generation for chargeable activities
**When** a Billing Period is completed
**Then** the System will generate a Customer Bill for all relevant Chargeable Activity

### AC2: Bill rendering based on preferences
**When** a Customer requests a Customer Bill from their Product Home page
**Then** the system will render the Customer Bill according to their Bill Preferences
```

**PowerPoint Example (Slide 136 - Store Image Scan)**:
```markdown
# Story: Successfully Store an Image Scan

## Story Summary
As a Staff user
I want to store a scan of an image in the cloud
So that it can be accessed from any location

## Acceptance Criteria

### AC1: Successful transmission confirmation
**When** image transmission is successful
**Then** system displays confirmation message "Image Scan Successful"

### AC2: Image persisted in database
**When** image scan is complete
**Then** scanned image is present in database
```

### 3.7 Heuristics: Story Exploration Validation

**Class**: `StoryExploreHeuristic`

```python
class StoryExploreHeuristic:
    """Validates story exploration artifacts (Slides 13, 15, 16, 119, 136)"""
    
    def validate_story_with_acceptance_criteria(self, story_content: str) -> dict:
        """Validate story has proper acceptance criteria"""
        violations = []
        
        # Check for acceptance criteria section
        has_ac_section = bool(re.search(r'Acceptance\s+Criteria', story_content, re.IGNORECASE))
        
        if not has_ac_section:
            violations.append({
                'type': 'MISSING_ACCEPTANCE_CRITERIA',
                'severity': 'ERROR',
                'message': 'Story missing acceptance criteria section',
                'suggestion': 'Add acceptance criteria in When...then format',
                'slide_reference': 'Slide 13, 15, 119'
            })
            return {'has_acceptance_criteria': False, 'violations': violations}
        
        # Check for When...then pattern
        when_then_pattern = re.search(r'when\b.*\bthen\b', story_content, re.IGNORECASE | re.DOTALL)
        given_when_then = re.search(r'given\b.*\bwhen\b.*\bthen\b', story_content, re.IGNORECASE | re.DOTALL)
        
        if not (when_then_pattern or given_when_then):
            violations.append({
                'type': 'MISSING_BEHAVIOR_PATTERN',
                'severity': 'ERROR',
                'message': 'Acceptance criteria missing "When...then..." pattern',
                'suggestion': 'Use "When [condition], then [outcome]" format (Slide 13, 119)',
                'slide_reference': 'Slide 13, 119'
            })
        
        # Check for code patterns in AC (technical language)
        if re.search(r'\w+\([^\)]*\)', story_content):
            violations.append({
                'type': 'CODE_IN_AC',
                'severity': 'ERROR',
                'message': 'Acceptance criteria contains code patterns (function calls)',
                'suggestion': 'Describe behavior, not implementation. Use "when user submits" not "when submit() is called"',
                'slide_reference': 'Slide 13, 14'
            })
        
        # Check for technical implementation details
        tech_terms = ['database', 'API', 'endpoint', 'query', 'execute', 'call']
        for term in tech_terms:
            if re.search(rf'\b{term}\b', story_content, re.IGNORECASE):
                violations.append({
                    'type': 'TECHNICAL_AC',
                    'severity': 'WARNING',
                    'message': f'Acceptance criteria contains technical term: "{term}"',
                    'suggestion': 'Focus on observable behavior, not implementation details',
                    'slide_reference': 'Slide 14'
                })
                break
        
        # Count acceptance criteria
        ac_count = len(re.findall(r'###?\s+AC\d+', story_content))
        if ac_count == 0:
            ac_count = len(re.findall(r'when\b.*\bthen\b', story_content, re.IGNORECASE))
        
        if ac_count > 6:
            violations.append({
                'type': 'TOO_MANY_AC',
                'severity': 'WARNING',
                'message': f'Story has {ac_count} acceptance criteria (typically 2-5)',
                'suggestion': 'Consider splitting story - too many AC often indicates story is too large',
                'slide_reference': 'Slide 1, 2'
            })
        
        return {
            'has_acceptance_criteria': has_ac_section,
            'has_behavior_form': when_then_pattern or given_when_then,
            'ac_count': ac_count,
            'violations': violations
        }
```

### 3.8 Runner Implementation

#### Inner Class: `StoryExploreCommand(Command)`
- **Location**: `behaviors/stories/stories_runner.py`
- **Methods**:
  - `generate()` - Write acceptance criteria, refine map, define system stories
  - `validate()` - Validate exploration artifacts
  - `prompting_questions` - List of prerequisite questions

#### CLI Wrapper: `StoryExploreCodeAugmentedCommand(CodeAugmentedCommand)`
- **Wraps**: `StoryExploreCommand`
- **CLI Entry Points**:
  - `generate` - Perform exploration
  - `validate` - Validate criteria and refinements
  - `execute` - Combined generate + validate

---

## Phase 4: Specification Scenarios

### Overview
Specification Scenarios phase fills in the Scenarios section of story documents. Creates detailed Given/When/Then scenarios including Background and Scenario Outline.

**Artifacts Created by `/story-specification-scenarios`:**
- ✅ Story documents with **Scenarios section filled in**
- ✅ Background (optional - for repeated Given steps)
- ✅ Scenarios with Given/When/Then/But/And
- ✅ Scenario Outline (optional - for parameterized scenarios)
- ✅ Covers happy path, edge cases, error cases
- ❌ NO examples yet (added in Phase 5)

**Principles from Phase 0 that apply here:**
- Principle 0.1: Action-Oriented Stories (Universal)
- Principle 0.2: INVEST Principles (Universal)

**Principles from Phase 3 that apply here:**
- Principle 3.1: Writing Acceptance Criteria (scenarios build on these)

### 4.1 Phase-Specific Principles (⚠️ Commands: story-specification-scenarios)

#### Principle 4.1: Story Specification with Scenarios
- **Source**: Slides 16, 149-154
- **[DO]** (Agent-Relevant):
  - Create specification scenarios that describe detailed interactions between users and system
  - Link scenarios to stories (one story can have multiple scenarios)
  - Cover happy path, edge cases, and error cases in scenarios
  - Use Background for repeated Given steps across scenarios
  - Use Scenario Outline for parameterized scenarios
  - Use Given/When/Then/But/And keywords
  - Explore remaining key risks/unknowns/assumptions
- **[DON'T]** (Agent-Relevant):
  - Skip documenting scenarios
  - Skip scenarios for stories (scenarios provide detailed context)
  - Create scenarios without proper Given/When/Then structure
  - Add examples yet (examples come in Phase 5)
- **[Structural Patterns]**:
  - **Story → Scenario Relationship**: One story can have multiple scenarios (happy path, edge cases, error cases)
  - **Scenario Format**: Background (optional) + Given/When/Then/But/And structure
  - **Scenario Outline**: Parameterized scenarios with <parameter> placeholders and Examples table

### 4.2 Command: `/story-specification-scenarios`

#### Purpose
Create story specification scenarios (fills Scenarios section in story documents).

#### Command Files
- **Main**: `behaviors/stories/specification-scenarios/story-specification-scenarios-cmd.md`
- **Delegates**: `story-specification-scenarios-generate-cmd.md`, `story-specification-scenarios-validate-cmd.md`

#### Prompting Questions
- Which stories need scenario-based specifications?
- What are the main user flows or system flows to document?
- Are there any edge cases or alternative paths to consider?

#### Content
- Fill in Scenarios section of story documents
- Use Given/When/Then/But/And structure
- Add Background for repeated Given steps
- Add Scenario Outline for parameterized scenarios
- Cover happy path, edge cases, error cases

### 4.3 Template: Scenario Specification

**File**: `behaviors/stories/specification-scenarios/scenario-template.md`

```markdown
# Story Specification: [Story Title]

## Story
[Story title and summary]

## Background (Optional)
**Use when**: Same Given steps repeat in all scenarios
**Purpose**: Move repeated Given steps to background section

**Given** [common context that applies to all scenarios]
**And** [additional common context]

**Note**: Background runs before each scenario, provides shared context

---

## Scenarios

### Scenario 1: [Scenario Name - Happy Path]

**Given** [initial context/state]
**And** [additional context]
**And** [yet another context]
**When** [user/system action]
**Then** [expected outcome]
**And** [additional outcome]
**But** [should NOT happen - negative assertion]

### Scenario 2: [Scenario Name - Edge Case]

**Given** [context]
**When** [action]
**Then** [outcome]
**But** [should NOT happen]

### Scenario 3: [Scenario Name - Error Case]

**Given** [context]
**When** [error condition]
**Then** [error handling outcome]

---

### Scenario Outline: [Scenario Name - Parameterized]
**Use when**: Same scenario with different value combinations

**Given** there are <start> [items]
**When** [action] <value> [items]
**Then** [outcome] should be <expected> [items]

**Examples**:

| start | value | expected |
|-------|-------|----------|
| 12    | 5     | 7        |
| 20    | 5     | 15       |
| 100   | 25    | 75       |

**Note**: Scenario Outline runs once for each row in Examples table, substituting <parameter> values

---

## Gherkin Keywords

- **Given**: Set up initial context/state
- **And**: Additional context (same level as previous step)
- **When**: Action or event that triggers behavior
- **Then**: Expected outcome
- **But**: Negative assertion (should NOT happen)
- **Background**: Shared Given steps for all scenarios
- **Scenario Outline**: Parameterized scenario (runs multiple times with Examples table)

## Scenario Guidelines
- Cover happy path, edge cases, and error cases
- Use Given/When/Then/But structure consistently
- Use Background for repeated Given steps across scenarios
- Use Scenario Outline for parameterized scenarios with multiple value combinations
- Each scenario describes a specific interaction flow
- Scenarios are narrative descriptions (not code)
- Link scenarios to acceptance criteria
```

**PowerPoint Example (Slide 154 - Purchase Textbook)**:
```markdown
# Story Specification: Purchase Textbook

## Scenarios

### Scenario 1: Successful textbook purchase

**Given** a student is logged in to the system
**And** a particular textbook exists
**And** that textbook is not out of stock
**When** the student selects that textbook for purchase
**And** the student specifies shipping information (shipping method, billing address, shipping address)
**And** the student confirms his purchase
**Then** the system sends the payment information to the 3rd party
**And** the system sends the Order Details to the bookstore application
**And** a message is displayed to the student that the book was successfully purchased and is on its way
```

### 4.4 Heuristics: Scenario Validation

**Class**: `StorySpecificationScenariosHeuristic`

(See heuristics section for validation logic - validates Background, Scenario Outline, Given/When/Then/But structure)

### 4.5 Runner Implementation

#### Inner Class: `StorySpecificationScenariosCommand(Command)`
- **Location**: `behaviors/stories/stories_runner.py`
- **Methods**:
  - `generate()` - Fill in Scenarios section
  - `validate()` - Validate scenario completeness
  - `prompting_questions` - List of prerequisite questions

#### CLI Wrapper: `StorySpecificationScenariosCodeAugmentedCommand(CodeAugmentedCommand)`
- **Wraps**: `StorySpecificationScenariosCommand`
- **CLI Entry Points**:
  - `generate` - Create scenarios
  - `validate` - Validate scenarios
  - `execute` - Combined generate + validate

---

## Phase 5: Specification Examples

### Overview
Specification Examples phase fills in the Examples section of story documents. Adds concrete examples (normal and Scenario Outline) that complete the story specification.

**Artifacts Created by `/story-specification-examples`:**
- ✅ Story documents with **Examples section filled in**
- ✅ Normal Examples (concrete values)
- ✅ Scenario Outline Examples (parameterized with Examples table)
- ✅ Background (optional - if not in scenarios)
- ✅ Uses Given/When/Then/But/And
- ✅ **COMPLETES STORY SPECIFICATION**

**Principles from Phase 0 that apply here:**
- Principle 0.1: Action-Oriented Stories (Universal)
- Principle 0.2: INVEST Principles (Universal)

**Principles from Phase 3 that apply here:**
- Principle 3.1: Writing Acceptance Criteria (examples demonstrate these)

**Principles from Phase 4 that apply here:**
- Principle 4.1: Scenarios (examples are added to scenarios)

### 5.1 Phase-Specific Principles (⚠️ Commands: story-specification-examples)

#### Principle 5.1: Story Specification with Examples
- **Source**: Slides 206
- **[DO]** (Agent-Relevant):
  - Add concrete examples to scenarios
  - Use normal examples for single, specific use cases
  - Use Scenario Outline for multiple similar cases with different data
  - Link examples to scenarios
  - Cover edge cases and boundary conditions with examples
  - Complete the story specification
- **[DON'T]** (Agent-Relevant):
  - Create examples without linking to scenarios
  - Use Scenario Outline when normal examples would be clearer
  - Skip examples (examples are critical for complete specification)
- **[Structural Patterns]**:
  - **Scenario → Example Relationship**: Scenarios can have normal examples and/or Scenario Outline
  - **Normal Example Format**: Concrete values, specific data points
  - **Scenario Outline Format**: `<parameter>` placeholders with Examples table

### 5.2 Command: `/story-specification-examples`

#### Purpose
Create story specification examples (fills Examples section, completes specification).

#### Command Files
- **Main**: `behaviors/stories/specification-examples/story-specification-examples-cmd.md`
- **Delegates**: `story-specification-examples-generate-cmd.md`, `story-specification-examples-validate-cmd.md`

#### Prompting Questions
- Which stories need example-based specifications?
- What are the key examples or test cases to document?
- Are there boundary conditions or edge cases to cover?

#### Content
- Fill in Examples section of story documents  
- Add normal examples (concrete values)
- Add Scenario Outline examples (parameterized with table)
- Link examples to scenarios
- Complete the story specification

### 5.3 Template: Example Specification

**File**: `behaviors/stories/specification-examples/examples-template.md`

**Purpose**: Adds concrete examples to scenarios (completes the story specification)

```markdown
# Story Examples: [Story Title]

## Background (Optional - if not in scenario doc)
**Given** [common context for all examples]
**And** [additional common context]

---

## Normal Examples (Concrete, Specific Values)

### Example 1: [Example Name]

**Given** [specific context with concrete values]
**And** [additional specific context]
**And** [yet another specific context]
**When** [action with specific inputs]
**Then** [expected outcome with specific values]
**And** [additional verification]
**But** [should NOT happen - negative assertion]

**Data**:
- Input: [concrete value]
- Expected Output: [concrete result]

---

## Scenario Outline Examples (Parameterized with Table)

### Scenario Outline: [Example Name]
**Use when**: Testing same behavior with multiple value combinations (3+ cases)

**Given** there are <start> [items]
**And** [context with <parameter>]
**When** I [action] <value> [items]
**Then** I should have <expected> [items]
**But** I should not have <invalid> [items]

**Examples**:

| start | value | expected | invalid |
|-------|-------|----------|---------|
| 12    | 5     | 7        | 5       |
| 20    | 5     | 15       | 5       |
| 100   | 25    | 75       | 25      |

**Note**: Scenario Outline runs once for each row, substituting <parameter> values from table

---

## When to Use Each Type

**Normal Examples** (✅): 
- Single, specific use case with concrete values
- Clear demonstration of specific behavior
- Happy path and critical paths
- When exact values matter for understanding

**Scenario Outline Examples** (✅): 
- Multiple similar cases that differ only in data values
- Testing variations of same behavior
- Edge cases and boundary conditions
- Validation rules with 3+ different value combinations
- When pattern is more important than specific values

---

## Gherkin Keywords in Examples

- **Given**: Set up specific context with concrete values (or <parameters>)
- **And**: Additional context at same level
- **When**: Specific action with concrete inputs (or <parameters>)
- **Then**: Expected outcome with specific values (or <parameters>)
- **But**: Negative assertion - what should NOT happen
- **Background**: Shared context for all examples
- **Scenario Outline**: Parameterized example that runs multiple times with Examples table
- **Examples**: Table of values for Scenario Outline (uses | column | format)
```

**PowerPoint Example (Slide 206 - Trading Alert with Gherkin)**:
```markdown
# Story Examples: Trading Status Alert

## Normal Example Format

### Example 1: Trader is not alerted below threshold

**Given** a stock of symbol STK1
**And** a threshold of 10.0
**When** the stock is traded at 5.0
**Then** the alert status should be OFF
**But** no alert message should be sent

### Example 2: Trader is alerted above threshold

**Given** a stock of symbol STK1
**And** a threshold of 10.0
**When** the stock is traded at 11.0
**Then** the alert status should be ON
**And** alert message should be sent to trader
**But** alert should not be sent to other traders

---

## Scenario Outline Format (Same examples as parameterized)

### Scenario Outline: Trading alert threshold behavior

**Given** a stock of symbol <symbol>
**And** a threshold of <threshold>
**When** the stock is traded at <price>
**Then** the alert status should be <status>

**Examples**:

| symbol | threshold | price | status |
|--------|-----------|-------|--------|
| STK1   | 10.0      | 5.0   | OFF    |
| STK1   | 10.0      | 11.0  | ON     |
| STK2   | 15.0      | 14.0  | OFF    |
| STK2   | 15.0      | 16.0  | ON     |
```

### 5.4 Heuristics: Example Validation

**Class**: `StorySpecificationExamplesHeuristic`

```python
class StorySpecificationExamplesHeuristic:
    """Validates example specifications (Slide 206)"""
    
    def validate_scenarios(self, spec_content: str) -> dict:
        """Validate scenarios have proper structure"""
        violations = []
        
        # Check for scenarios
        has_scenarios = bool(re.search(r'Scenario\s*\d*:', spec_content, re.IGNORECASE))
        
        if not has_scenarios:
            violations.append({
                'type': 'MISSING_SCENARIOS',
                'severity': 'ERROR',
                'message': 'Specification missing scenario definitions',
                'suggestion': 'Add scenarios with Given/When/Then structure',
                'slide_reference': 'Slide 149-154'
            })
            return {'has_scenarios': False, 'violations': violations}
        
        # Check for Given/When/Then structure
        scenarios = re.findall(r'Scenario[^:]*:.*?(?=Scenario|$)', spec_content, re.IGNORECASE | re.DOTALL)
        
        for scenario in scenarios:
            has_given = bool(re.search(r'\bGiven\b', scenario, re.IGNORECASE))
            has_when = bool(re.search(r'\bWhen\b', scenario, re.IGNORECASE))
            has_then = bool(re.search(r'\bThen\b', scenario, re.IGNORECASE))
            
            if not (has_when and has_then):
                violations.append({
                    'type': 'INCOMPLETE_SCENARIO',
                    'severity': 'ERROR',
                    'message': 'Scenario missing When...Then structure',
                    'suggestion': 'Ensure each scenario has When [action] Then [outcome]',
                    'slide_reference': 'Slide 154, 206'
                })
                break
        
        return {
            'has_scenarios': True,
            'scenario_count': len(scenarios),
            'violations': violations
        }
```

**Class**: `StorySpecificationExamplesHeuristic`

```python
class StorySpecificationExamplesHeuristic:
    """Validates example specifications (Slide 206)"""
    
    def validate_examples(self, examples_content: str) -> dict:
        """Validate examples are properly structured"""
        violations = []
        
        # Check for examples
        has_examples = bool(re.search(r'Example\s*\d*:', examples_content, re.IGNORECASE))
        
        if not has_examples:
            violations.append({
                'type': 'MISSING_EXAMPLES',
                'severity': 'ERROR',
                'message': 'Specification missing example definitions',
                'suggestion': 'Add concrete examples for scenarios',
                'slide_reference': 'Slide 206'
            })
            return {'has_examples': False, 'violations': violations}
        
        # Check for parameterized examples with tables
        has_parameters = bool(re.search(r'<\w+>', examples_content))
        has_table = bool(re.search(r'\|.*\|.*\|', examples_content))
        
        if has_parameters and not has_table:
            violations.append({
                'type': 'PARAMETERIZED_WITHOUT_TABLE',
                'severity': 'ERROR',
                'message': 'Parameterized example missing Examples table',
                'suggestion': 'Add Examples table with | parameter | expected | format'
            })
        
        return {
            'has_examples': True,
            'has_parameterized': has_parameters,
            'has_tables': has_table,
            'violations': violations
        }
```

### 5.5 Runner Implementation

#### Inner Class: `StorySpecificationExamplesCommand(Command)`
- **Location**: `behaviors/stories/stories_runner.py`
- **Methods**:
  - `generate()` - Fill in Examples section
  - `validate()` - Validate example completeness
  - `prompting_questions` - List of prerequisite questions

#### CLI Wrapper: `StorySpecificationExamplesCodeAugmentedCommand(CodeAugmentedCommand)`
- **Wraps**: `StorySpecificationExamplesCommand`
- **CLI Entry Points**:
  - `generate` - Create examples
  - `validate` - Validate examples
  - `execute` - Combined generate + validate

---

## Integration & Combined Workflows

### Overview
Integration phase combines workflows and provides configuration for the complete story writing system.

### 7.1 Combined Workflow Command: `/story-discovery-explore`

#### Purpose
Combined discovery and exploration workflow for teams that want a streamlined process.

#### Command Files
- **Main**: `behaviors/stories/discovery-explore/story-discovery-explore-cmd.md`
- **Delegates**: `story-discovery-explore-generate-cmd.md`, `story-discovery-explore-validate-cmd.md`

#### Prompting Questions
- Which market increment are we focusing on?
- What new information or insights have been discovered?
- Which feature or slice are we exploring?
- Are there any system-level concerns or technical constraints?

#### Content
- Combines discovery and exploration activities
- Refines increments and explores stories in one workflow
- Applies discovery principles (refinement, practices, story analysis)
- Applies exploration principles (acceptance criteria, system stories)

#### Runner Implementation
- **Inner Class**: `StoryDiscoveryExploreCommand(Command)`
- **CLI Wrapper**: `StoryDiscoveryExploreCodeAugmentedCommand(CodeAugmentedCommand)`
- **Heuristics**: `StoryDiscoveryExploreHeuristic` - Combines discovery and exploration checks

### 7.2 Configuration Files

#### behavior.json
- **File**: `behaviors/stories/behavior.json`
- **Content**:
  - `deployed: true`
  - `description`: "Story writing practices and standards for agile teams"
  - `workflows`: Define sequential and iterative workflows

#### code-agent-index.json
- **File**: `behaviors/stories/code-agent-index.json`
- **Content**:
  - List all story artifacts (rules, commands, runners)
  - Follow pattern from `behaviors/bdd/code-agent-index.json`

#### feature-outline.md
- **File**: `behaviors/stories/feature-outline.md`
- **Content**:
  - Document all 7 commands and their purposes
  - List commands and their relationships to phases
  - Document workflow patterns (sequential and iterative)
  - Document command-to-heuristic mapping

### 7.3 Verification Process

#### Source Material Review
- **File to Review**: `behaviors/stories/docs/story-training-content.md` (PowerPoint extraction)
- **Check**: All principles, practices, and guidance from PowerPoint are covered

#### Implementation Alignment
- **Rules**: All PowerPoint principles captured in `stories-rule.mdc`
- **Commands**: All major activities from PowerPoint have corresponding commands
- **Heuristics**: All criteria mentioned in PowerPoint are validated
- **Templates**: Templates match PowerPoint guidance on structure

#### Completeness Verification
- All stages from PowerPoint supported (Shape, Market Increments, Discover, Explore, Specification)
- All practices and principles from PowerPoint enforced
- End-to-end workflow matches PowerPoint guidance

---

# IMPLEMENTATION ORDER

---

## Overview

Implement phase by phase. Within each phase, follow this order:
1. **Define** - Rules, commands, templates, prompts
2. **Sync** - Deploy to .cursor/
3. **Run manually** - Test with no code (user tries commands)
4. **Code** - Heuristics and runners using BDD workflow
5. **Test** - Sync and validate
6. **Next phase** - Move to next phase

---

## Phase 1: Shape

### Step 1.1: Define Rules
**Action**: Create rule files with principles

**Files to create**:
- `behaviors/stories/stories-rule.mdc`
  - Section 0: Universal Principles (0.1 Action-Oriented, 0.2 INVEST)
  - Section 0.5: Hierarchy Principle
  - Section 1: Story Shaping Principles (1.1-1.6 from this plan)
- `behaviors/stories/rule/stories-rule-cmd.md`
- `behaviors/stories/rule/stories-rule-generate-cmd.md`
- `behaviors/stories/rule/stories-rule-validate-cmd.md`

### Step 1.2: Define Commands
**Action**: Create command plan files

**Files to create**:
- `behaviors/stories/shape/story-shape-cmd.md`
- `behaviors/stories/shape/story-shape-generate-cmd.md`
- `behaviors/stories/shape/story-shape-validate-cmd.md`

**Content**: Copy from Phase 1 section of this plan (command purpose, prompting questions, what it creates)

### Step 1.3: Define Templates
**Action**: Create artifact templates

**Files to create**:
- `behaviors/stories/map/story-map-decomposition-template.md`
- `behaviors/stories/map/story-map-increments-template.md`
- `behaviors/stories/epic/epic-doc-template.md`
- `behaviors/stories/feature/feature-doc-template.md`
- `behaviors/stories/write/story-doc-template.md` (shell only, filled in later phases)

**Content**: Copy templates from Phase 1 section of this plan

### Step 1.4: Define Prompts
**Action**: Create prompts file per action

**File to create**:
- `behaviors/stories/shape/story-shape-prompts.md`

**Content**:
```markdown
# Story Shape Prompts

## Generate Action Prompts
- What is the product or feature vision?
- Who are the target users or stakeholders?
- What are the main user goals or outcomes?
- What is the scope boundary (what's in/out)?
- What are the business priorities for increments?
- What are the market constraints or deadlines?
- Are there any dependencies between increments?

## Validate Action Prompts
- Review the story map for completeness
- Check for user AND system activities
- Verify business language (not tasks)
- Confirm story sizing (3-12d range)
```

### Step 1.5: Sync
**Action**: Deploy to `.cursor/` directory

**Command**: Run sync behavior to deploy stories behavior

### Step 1.6: Run Manually (No Code)
**Action**: Let user test commands without runner code

**User tries**:
- `/story-shape` - AI uses rules and templates to generate story map
- User reviews output
- User validates concepts work
- **DO NOT write runner code yet**

### Step 1.7: Code - Heuristics and Runners
**Action**: Implement runner code using BDD workflow

**BDD Workflow for `stories_runner.py`**:

#### 1.7.1: Domain Models
```bash
/ddd-structure stories_runner.py
# Review and edit: behaviors/stories/docs/stories_runner-domain-map.txt

/ddd-interaction stories_runner.py
# Review and edit: behaviors/stories/docs/stories_runner-domain-interactions.txt
```

#### 1.7.2: Domain Scaffold
```bash
/bdd-scaffold stories_runner_test.py
# Review and edit: behaviors/stories/docs/stories_runner_test-hierarchy.txt
```

#### 1.7.3: Build Test Signatures
```bash
/bdd-signature stories_runner_test.py mamba
# Review: behaviors/stories/stories_runner_test.py
```

#### 1.7.4: Write Tests (RED)
```bash
/bdd-test stories_runner_test.py mamba
# Implement test bodies - tests should FAIL
```

#### 1.7.5: Write Code (GREEN)
```bash
/bdd-code stories_runner.py
# Implement:
# - StoryShapeCommand class
# - StoryMapHeuristic class
# - MarketIncrementHeuristic class
# - StoryShapeCodeAugmentedCommand wrapper
# Tests should PASS
```

### Step 1.8: Sync and Test
**Action**: Deploy and validate

```bash
# Sync to .cursor/
/code-agent-sync

# Test manually
/story-shape [with actual project]
# Verify it works end-to-end

# Run automated tests
python behaviors/stories/stories_runner_test.py
```

### Step 1.9: Ready for Phase 2
**Action**: Confirm Phase 1 complete before moving on

**Checklist**:
- ✅ Rules defined and synced
- ✅ Commands defined
- ✅ Templates created
- ✅ Prompts documented
- ✅ Runner code implemented (BDD workflow)
- ✅ Tests passing
- ✅ Manual testing successful
- ✅ User can successfully run `/story-shape`

---

## Phase 2: Discover

### Step 2.1: Define Commands
- `behaviors/stories/discovery/story-discovery-cmd.md` (+ generate, validate)

### Step 2.2: Define Templates
- Updates to existing story-map templates (add "FINALIZED" markers)

### Step 2.3: Define Prompts
- `behaviors/stories/discovery/story-discovery-prompts.md`

### Step 2.4: Sync
- Deploy discovery behavior

### Step 2.5: Run Manually
- User tests `/story-discovery` with AI only (no code)

### Step 2.6: Code - BDD Workflow
- Add `StoryDiscoveryCommand` to `stories_runner.py`
- Add `StoryDiscoveryHeuristic` class
- Follow BDD: domain → scaffold → signatures → tests → code

### Step 2.7: Sync and Test
- Deploy and validate manually
- Run automated tests

### Step 2.8: Ready for Phase 3

---

## Phase 3: Explore

### Step 3.1: Define Commands
- `behaviors/stories/explore/story-explore-cmd.md` (+ generate, validate)

### Step 3.2: Update Templates
- Update `feature-doc-template.md` (add Domain AC + Behavioral AC sections)
- Create `story-doc-template.md` (shell with AC, empty Scenarios/Examples)

### Step 3.3: Define Prompts
- `behaviors/stories/explore/story-explore-prompts.md`

### Step 3.4: Sync
- Deploy explore behavior

### Step 3.5: Run Manually
- User tests `/story-explore` with AI only (no code)
- Verify Domain AC + Behavioral AC get added to feature docs

### Step 3.6: Code - BDD Workflow
- Add `StoryExploreCommand` to `stories_runner.py`
- Add `StoryExploreHeuristic` class
- Follow BDD: domain → scaffold → signatures → tests → code

### Step 3.7: Sync and Test
- Deploy and validate
- Run automated tests

### Step 3.8: Ready for Phase 4

---

## Phase 4: Specification Scenarios

### Step 4.1: Define Commands
- `behaviors/stories/specification-scenarios/story-specification-scenarios-cmd.md` (+ generate, validate)

### Step 4.2: Define Templates
- `behaviors/stories/specification-scenarios/scenario-template.md`
  - Include: Background, Scenario Outline, Given/When/Then/But/And

### Step 4.3: Define Prompts
- `behaviors/stories/specification-scenarios/story-specification-scenarios-prompts.md`

### Step 4.4: Sync
- Deploy specification-scenarios behavior

### Step 4.5: Run Manually
- User tests `/story-specification-scenarios` with AI only
- Verify Scenarios section gets filled in story docs

### Step 4.6: Code - BDD Workflow
- Add `StorySpecificationScenariosCommand` to `stories_runner.py`
- Add `StorySpecificationScenariosHeuristic` class
- Follow BDD: domain → scaffold → signatures → tests → code

### Step 4.7: Sync and Test
- Deploy and validate
- Run automated tests

### Step 4.8: Ready for Phase 5

---

## Phase 5: Specification Examples

### Step 5.1: Define Commands
- `behaviors/stories/specification-examples/story-specification-examples-cmd.md` (+ generate, validate)

### Step 5.2: Define Templates
- `behaviors/stories/specification-examples/examples-template.md`
  - Include: Normal Examples, Scenario Outline with Examples table

### Step 5.3: Define Prompts
- `behaviors/stories/specification-examples/story-specification-examples-prompts.md`

### Step 5.4: Sync
- Deploy specification-examples behavior

### Step 5.5: Run Manually
- User tests `/story-specification-examples` with AI only
- Verify Examples section gets filled, completes story spec

### Step 5.6: Code - BDD Workflow
- Add `StorySpecificationExamplesCommand` to `stories_runner.py`
- Add `StorySpecificationExamplesHeuristic` class
- Follow BDD: domain → scaffold → signatures → tests → code

### Step 5.7: Sync and Test
- Deploy and validate
- Run automated tests

### Step 5.8: Complete!

---

## Quick Reference: Implementation Steps Per Phase

```
FOR EACH PHASE:
  1. Define rules (if phase-specific principles)
  2. Define commands (cmd.md files)
  3. Define templates (template.md files)
  4. Define prompts (prompts.md files)
  5. Sync (deploy to .cursor/)
  6. Run manually (user tests with AI, no code)
  7. Code heuristics and runners:
     a. /ddd-structure → domain map
     b. /ddd-interaction → interactions
     c. /bdd-scaffold → test hierarchy
     d. /bdd-signature → test signatures
     e. /bdd-test → write tests (RED)
     f. /bdd-code → write code (GREEN)
  8. Sync and test (deploy + run automated tests)
  9. Move to next phase
```

---

## Why This Order?

1. **Define first** - Know what you're building
2. **Sync early** - Get rules into AI context
3. **Run manually** - Validate concepts work without code
4. **Code with BDD** - Test-driven development ensures quality
5. **Test thoroughly** - Both manual and automated
6. **One phase at a time** - Reduces complexity, enables iteration

---

# APPENDICES

---

## A. Command Summary

### All Commands (7 total)
1. **`/story-shape`** - Create story map shell and elaborate/extrapolate scope (Phase 1: Shape)
2. **`/story-market-increments`** - Identify marketable increments of value (Phase 2: Market Increments)
3. **`/story-discovery`** - Refine increments, apply practices, groom stories (Phase 3: Discover)
4. **`/story-explore`** - Write acceptance criteria, refine map, define system stories (Phase 4: Explore)
5. **`/story-specification-scenarios`** - Create scenario-based specifications (Phase 5: Specification)
6. **`/story-specification-examples`** - Create example-based specifications (Phase 5: Specification)
7. **`/story-discovery-explore`** - Combined discovery and exploration workflow (Integration)

### Heuristic Mapping
- Each command has its own heuristic class
- Heuristics validate command-specific content
- Standard `CodeAugmentedCommand` pattern for heuristic application

### Rule File Markers
- ⚠️ **Universal** - applies to all commands
- ⚠️ **All Phases** - applies to commands across Shape, Discover, and Explore
- ⚠️ **Stage: [stage-name]** - applies to commands within a specific phase/stage
- ⚠️ **Commands: [command-list]** - applies to specific commands

---

## B. Files to Create

### Rules
- `behaviors/stories/stories-rule.mdc`
- `behaviors/stories/rule/stories-rule-cmd.md`
- `behaviors/stories/rule/stories-rule-generate-cmd.md`
- `behaviors/stories/rule/stories-rule-validate-cmd.md`

### Commands (7 commands × 3 files = 21 files)
1. `behaviors/stories/shape/story-shape-cmd.md` (+ generate, validate)
2. `behaviors/stories/market-increments/story-market-increments-cmd.md` (+ generate, validate)
3. `behaviors/stories/discovery/story-discovery-cmd.md` (+ generate, validate)
4. `behaviors/stories/explore/story-explore-cmd.md` (+ generate, validate)
5. `behaviors/stories/specification-scenarios/story-specification-scenarios-cmd.md` (+ generate, validate)
6. `behaviors/stories/specification-examples/story-specification-examples-cmd.md` (+ generate, validate)
7. `behaviors/stories/discovery-explore/story-discovery-explore-cmd.md` (+ generate, validate)

### Runner
- `behaviors/stories/stories_runner.py` (full implementation with 8 command classes: rule + 7 commands)
  - 7 command classes (one per command)
  - 7 heuristic classes (one per command)
  - Standard Command pattern (no OperationCommand decorator needed)

### Templates
- `behaviors/stories/map/story-map-template.md`
- `behaviors/stories/write/story-template.md`
- `behaviors/stories/acceptance/acceptance-criteria-template.md`
- `behaviors/stories/specification-scenarios/scenario-template.md`
- `behaviors/stories/specification-examples/examples-template.md`

### Configuration
- `behaviors/stories/behavior.json` (update)
- `behaviors/stories/code-agent-index.json` (create/update)
- `behaviors/stories/feature-outline.md` (update)

---

## C. Dependencies

### Common Runner Enhancement Required
- **File**: `behaviors/common_command_runner/common_command_runner.py`
- **Enhancement**: Add Prompting Questions concept
  - Add `prompting_questions` attribute to `Command` class
  - Add `check_prompting_questions()` method to `CodeAugmentedCommand` class
  - Workflow integration in `generate()` and `plan()` methods

### Existing Dependencies
- `common_command_runner` framework
- Existing code-agent patterns and templates
- PowerPoint content analysis (DONE)
- Command structure analysis (DONE - 7 commands identified)

---

## D. Implementation Complexity

### Complexity Level
Low-Medium

### Why Simplified
- Using standard Command pattern (no decorator needed)
- Each command is self-contained
- No operation state tracking or ordering enforcement
- No heuristic filtering complexity
- Standard CodeAugmentedCommand wrapper pattern
- Each command has its own heuristic class

### Components Needed
1. **Command Classes**: 7 command classes extending Command
2. **Heuristic Classes**: 7 heuristic classes (one per command)
3. **CLI Wrappers**: 7 CodeAugmentedCommand wrappers
4. **CLI Entry Points**: Standard generate/validate/execute handlers

### Reusability
Standard pattern - follows existing code-agent command structure

---

## E. Naming Conventions

### Rules
- **Main feature rule**: `stories-rule.mdc` (e.g., `behaviors/stories/stories-rule.mdc`)
- **Rule command files**: `stories-rule-cmd.md`, `stories-rule-generate-cmd.md`, `stories-rule-validate-cmd.md`
- **Rule file location**: `behaviors/stories/stories-rule.mdc`

### Commands
- **Main command**: `<command-name>-cmd.md` (e.g., `story-shape-cmd.md`)
- **Delegate commands**: `<command-name>-generate-cmd.md`, `<command-name>-validate-cmd.md`
- **Command directory**: `behaviors/stories/<command-name>/` (e.g., `behaviors/stories/shape/`)
- **Command file locations**:
  - Main: `behaviors/stories/<command-name>/<command-name>-cmd.md`
  - Generate: `behaviors/stories/<command-name>/<command-name>-generate-cmd.md`
  - Validate: `behaviors/stories/<command-name>/<command-name>-validate-cmd.md`

### Runners
- **Runner file**: `behaviors/stories/stories_runner.py`
- **Test file**: `behaviors/stories/stories_runner_test.py`
- **Command class**: `<CommandName>Command` (PascalCase, e.g., `StoryShapeCommand`)
- **Wrapper class**: `CodeAugmented<CommandName>Command` (e.g., `CodeAugmentedStoryShapeCommand`)
- **Config class**: `<CommandName>Config` (e.g., `StoryShapeConfig`)

### Templates
- **Story-specific templates**: `behaviors/stories/<template-type>/<template-name>.md`
- **Common templates**: `behaviors/stories/feature/<template-name>.md` (if shared)

---

## F. File Structure Requirements

### Rule File Structure (`stories-rule.mdc`)
1. **Frontmatter** (YAML):
   - `description`: Story writing practices and standards for agile teams
   - `globs`: List of file patterns this rule applies to
   - `alwaysApply`: false (or true if needed)
2. **When/then statement**: `**When** writing user stories for agile development, **then** follow these principles...`
3. **Executing Commands section**: Quick reference to commands that use this rule
4. **Conventions section**: Naming conventions, file locations, structural conventions (before principles)
5. **Principles section**: Numbered principles (## 1. Principle Name) with DO/DON'T examples
6. **Templates section** (if applicable): Templates used for generating files
7. **Commands section** (at end): Detailed list of commands that implement or use this rule

### Command File Structure (`<command-name>-cmd.md`)
1. **Header**: `### Command: /<command-name>`
2. **Purpose section**: `**[Purpose]:**` - What the command does
3. **Rule section**: `**[Rule]:**` - Reference to rule file (`stories-rule.mdc`)
4. **Runner section**: `**Runner:**` - CLI commands and runner path
5. **Action 1: GENERATE** - Steps with performers (User, AI Agent, Runner, Code)
6. **Action 2: GENERATE FEEDBACK** - User review steps
7. **Action 3: VALIDATE** - Validation steps with performers
8. **Action 4: VALIDATE FEEDBACK** - User review of validation results

### Runner File Structure (`stories_runner.py`)
1. **Imports**: From `common_command_runner` and feature-specific modules
2. **Inner Command Classes**: One per command, extends `Command` or `CodeAgentCommand`
   - Implements `generate()` and `validate()` methods
   - Uses templates for generation
   - Contains core business logic
3. **Outer Wrapper Classes**: One per command, extends `CodeAugmentedCommand`
   - Wraps inner command instance
   - Implements `handle_cli()` class method
   - Adds AI validation with heuristics
4. **CLI Entry Point**: `main()` function with command handlers
   - Registers all commands in handler dictionary
   - Maps command names to wrapper's `handle_cli()` method

---

## G. Test-Driven Development Workflow

**CRITICAL**: All implementation must follow BDD TDD workflow using the BDD behavior commands: **Domain Models → Domain Scaffold → Build Test Signatures → Write Tests → Write Code**

### Phase -1: Domain Models (DDD Analysis)

**Purpose**: Generate domain structure and interaction models that will be used by BDD scaffold command  
**Location**: All domain model files go in `behaviors/stories/docs/` folder  
**DDD Commands**: `/ddd-structure` and `/ddd-interaction`

**Process**:
1. **Generate Domain Structure**:
   - Run `/ddd-structure stories_runner.py`
   - **Output**: `behaviors/stories/docs/stories_runner-domain-map.txt`
   
2. **Generate Domain Interactions**:
   - Run `/ddd-interaction stories_runner.py`
   - **Output**: `behaviors/stories/docs/stories_runner-domain-interactions.txt`

3. **Proceed to BDD workflow**

### BDD Workflow Phases
1. **Phase 0: Domain Scaffold** - `/bdd-scaffold stories_runner_test.py`
2. **Phase 1: Build Test Signatures** - `/bdd-signature stories_runner_test.py mamba`
3. **Phase 2: Write Tests** - `/bdd-test stories_runner_test.py mamba`
4. **Phase 3: Write Code** - `/bdd-code stories_runner.py`

---

## H. Story Counting Pattern (No Planning/Sizing/Forecasting)

**From Slides 8, 9, 10, 11 - What We Include:**

✅ **Story Counting**: Extrapolate story counts for unexplored areas of the map
✅ **Counting Format**: "~[X] stories" or "Extrapolated: ~[X] stories"
✅ **Counting Purpose**: Understand scope without detailed decomposition
✅ **Counting Level**: At Epic/Feature level where exact stories unknown

**What We DON'T Include:**
❌ **Point-Based Estimation**: No story points (1, 2, 3, 5, 8, etc.)
❌ **Velocity Tracking**: No velocity calculations or tracking
❌ **Sprint Planning Math**: No capacity/velocity calculations
❌ **Throughput Calculations**: No detailed throughput analysis
❌ **Forecasting Formulas**: No bucket/water metaphor calculations
❌ **Detailed Scheduling**: No sprint-by-sprint planning

**Story Counting Example**:
```markdown
Epic: Order Management (~45 stories)
  Feature: Order Placement (~15 stories)
    Story: Customer places order (5d)
    Story: System validates payment (3d)
    Story: System sends confirmation (3d)
    ... [12 more stories - extrapolated]
    
  Feature: Order Fulfillment (~20 stories - extrapolated)
    [Stories not yet decomposed]
    
  Feature: Order History (~10 stories - extrapolated)
    [Stories not yet decomposed]
```

