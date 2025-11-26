# Story Map: Manage Mobs in Foundry VTT

**Navigation:** [📊 Increments](../increments/mob-rule-story-map-increments.md)

**File Name**: `mob-rule-story-map.md`
**Location**: `mob_rule/docs/stories/map/mob-rule-story-map.md`

> **CRITICAL MARKDOWN FORMATTING**: All tree structure lines MUST end with TWO SPACES (  ) for proper line breaks. Without two spaces, markdown will wrap lines together into one long line, breaking the visual tree structure.

> **CRITICAL HIERARCHY FORMATTING**: The {epic_hierarchy} section MUST use tree structure characters to show hierarchy:
> - Use `│` (vertical line) for continuing branches
> - Use `├─` (branch) for items that have siblings below them
> - Use `└─` (end branch) for the last item in a group
> - Epic format: `🎯 **Epic Name** (X features, ~Y stories)  `
> - Feature format: `├─ ⚙️ **Feature Name** (~Z stories)  ` or `└─ ⚙️ **Feature Name** (~Z stories)  ` for last feature
> - Story format (when present): `│  ├─ 📝 Story: [Verb-Noun Name]  ` followed by `│  │  *[Component interaction description]*  ` on the next line, or `│  └─ 📝 Story: [Verb-Noun Name]  ` for last story
> - **MANDATORY STORY NAMING FORMAT**: All story names MUST follow Actor-Verb-Noun format:
>   - Story name: Concise Verb-Noun format (e.g., "Create Mob from Selected Tokens", "Display Mob Grouping in Combat Tracker", "Execute Mob Attack with Strategy")
>   - Description: Italicized component interaction description showing component-to-component interactions (e.g., "*GM selects multiple minion tokens on canvas and Mob manager creates mob with selected tokens and assigns random leader*")
> - Example structure:
>   ```
>   🎯 **Epic Name** (2 features, ~8 stories)  
>   │  
>   ├─ ⚙️ **Feature 1** (~5 stories)  
>   │  ├─ 📝 Story: Create Mob from Selected Tokens  
>   │  │  *GM selects multiple minion tokens on canvas and Mob manager creates mob*  
>   │  └─ 📝 Story: Display Mob Grouping  
>   │     *Combat Tracker receives mob creation notification and updates display*  
>   │  
>   └─ ⚙️ **Feature 2** (~3 stories)  
>      └─ 📝 Story: Execute Mob Attack  
>         *Combat Tracker moves to mob leader's turn and Mob manager forwards action*  
>   ```

## System Purpose
Enable Game Masters to group minions into mobs that act together, reducing churn and time in epic minion battles. Mobs execute coordinated actions based on selected strategies, allowing multiple mobs to act autonomously without constant intervention.

---

## Legend
- 🎯 **Epic** - High-level capability
- 📂 **Sub-Epic** - Sub-capability (when epic has > 9 features)
- ⚙️ **Feature** - Cohesive set of functionality
- 📝 **Story** - Small increment of behavior (3-12d)

---

## Story Map Structure

🎯 **Group Minions into Mobs** (4 features, ~15 stories)  
│  
├─ ⚙️ **Create Mobs from Canvas Tokens** (2 stories)  
│  ├─ 📝 Story: Create Mob from Selected Tokens  
│  │  *GM selects multiple tokens on canvas and Mob domain object creates mob with selected tokens and assigns random leader*  
│  └─ 📝 Story: Display Mob Grouping in Combat Tracker  
│     *Combat Tracker receives mob creation notification from Mob domain object and updates display to show mob membership*  
│  
├─ ⚙️ **View Mob Groupings in Combat Tracker** (~3 stories)  
│  
├─ ⚙️ **Modify Mob Membership** (~4 stories)  
│  
└─ ⚙️ **Spawn Mobs from Actors** (~4 stories)  

🎯 **Execute Mob Actions** (3 features, ~15 stories)  
│  
├─ ⚙️ **Select Mob Target** (~4 stories)  
│  
├─ ⚙️ **Execute Mob Attack** (2 stories)  
│  ├─ 📝 Story: Execute Mob Attack with Strategy  
│  │  *Combat Tracker moves to mob leader's turn, Mob domain object determines target from Select Target strategy, GM attacks with mob leader choosing attack and target, and Mob domain object forwards action to all members*  
│  └─ 📝 Story: Display Attack Results in Chat  
│     *Chat system receives attack result events from Combat system and displays formatted results for all mob members*  
│  
└─ ⚙️ **Determine Available Attacks** (~5 stories)  

🎯 **Handle Mob Strategies** (4 features, ~21 stories)  
│  
├─ ⚙️ **Select Mob Strategy** (3 stories)  
│  ├─ 📝 Story: Open Mob Configuration Panel  
│  │  *GM clicks on mob leader token or mob entry in Combat Tracker, and Mob Panel UI opens displaying mob configuration options*  
│  ├─ 📝 Story: Display Mob Configuration in Panel  
│  │  *Mob Panel UI receives mob configuration from Mob domain object and displays mob members, current strategy, and available strategy options*  
│  └─ 📝 Story: Select Mob Strategy from Panel  
│     *GM selects a strategy from Mob Panel UI dropdown, and Mob Panel UI sends strategy selection to Mob domain object which saves strategy configuration*  
│  
├─ ⚙️ **Choose Target by Strategy** (5 stories)  
│  ├─ 📝 Story: Apply Attack Common Target Strategy  
│  │  *GM selects Attack Common Target strategy for mob, and Mob domain object applies strategy when mob's turn begins by querying Combat Tracker for common target*  
│  ├─ 📝 Story: Display Selected Common Target  
│  │  *Combat Tracker receives target selection notification from Mob domain object and updates display to show mob's selected common target*  
│  ├─ 📝 Story: Apply Attack Most Powerful Strategy  
│  │  *When mob's turn begins, Mob domain object applies Attack Most Powerful strategy by querying Combat Tracker for all available targets, calculating power levels, and selecting most powerful target*  
│  ├─ 📝 Story: Display Selected Most Powerful Target  
│  │  *Combat Tracker receives target selection notification from Mob domain object and updates display to show mob's selected most powerful target*  
│  └─ 📝 Story: Apply Attack Weakest Strategy  
│     *When mob's turn begins, Mob domain object applies Attack Weakest strategy by querying Combat Tracker for all available targets, calculating power levels, and selecting weakest target*  
│  
├─ ⚙️ **Select Attack Effect by Strategy** (~4 stories)  
│  
└─ ⚙️ **AI-Assisted Behavior and Strategies** (~3 stories)  

🎯 **Auto-Flee Behavior** (1 feature, ~3 stories)  
│  
└─ ⚙️ **Auto Resist and Apply Effect** (~3 stories)  

---

## Source Material

- User journey maps: Diagram/image provided showing feature breakdown: Handle Mob Strategies, Edit Mobs, Choose Target, Select Attack Effect, Determine Available Attack, Auto - Flee
- Technical specifications: Foundry VTT system integration requirements. Mutants & Masterminds system integration (https://github.com/Ethaks/foundry-mm3). First increment scope: Basic mob creation with random leader assignment, click target = mob target, no strategy selection yet.

### Discovery Refinements

**Increment 1 Discovery (System /back office approach, System inner behavior granularity):**
- Enumerated all 6 stories for Increment 1 with component-level interactions:
  1. Create Mob from Selected Tokens (Epic: Group Minions into Mobs, Feature: Create Mobs from Canvas Tokens)
  2. Display Mob Grouping in Combat Tracker (Epic: Group Minions into Mobs, Feature: Create Mobs from Canvas Tokens)
  3. Execute Mob Attack with Strategy (Epic: Execute Mob Actions, Feature: Execute Mob Attack)
  4. Display Attack Results in Chat (Epic: Execute Mob Actions, Feature: Execute Mob Attack)
  5. Apply Attack Common Target Strategy (Epic: Handle Mob Strategies, Feature: Choose Target by Strategy)
  6. Display Selected Common Target (Epic: Handle Mob Strategies, Feature: Choose Target by Strategy)
- Stories expanded to show user → component → component flows
- Component interactions explicitly documented: Canvas System, Mob Domain Object, Combat Tracker, Token System, Combat System, Chat System
- Stories follow Actor-Verb-Noun format with italicized component interaction descriptions
- Terminology updated from "Mob manager" to "Mob domain object" throughout
