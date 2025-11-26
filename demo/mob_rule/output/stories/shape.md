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
> - Story format (when present): `│  ├─ 📝 Story: Story name  ` or `│  └─ 📝 Story: Story name  ` for last story
> - Example structure:
>   ```
>   🎯 **Epic Name** (2 features, ~8 stories)  
>   │  
>   ├─ ⚙️ **Feature 1** (~5 stories)  
>   │  ├─ 📝 Story: Story 1  
>   │  └─ 📝 Story: Story 2  
>   │  
>   └─ ⚙️ **Feature 2** (~3 stories)  
>      └─ 📝 Story: Story 3  
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
│  ├─ 📝 Story: GM selects multiple minion tokens on canvas and Mob manager creates mob  
│  └─ 📝 Story: Combat Tracker displays mob grouping  
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
├─ ⚙️ **Execute Mob Attack** (5 stories)  
│  ├─ 📝 Story: Move To Mob Leaders Turn  
│  │  *Combat Tracker moves to any mob member's turn, auto moves to mob leader's turn*  
│  ├─ 📝 Story: Determines Target from Strategy  
│  │  *Mob manager determines target from Select Target strategy, if no attack or target has been selected, nothing happens*  
│  ├─ 📝 Story: Initiate Mob Attack  
│  │  *GM attacks a target with the mob leader, choosing the attack and the target and Mob manager repeats the same attack action for all mob members*  
│  ├─ 📝 Story: Store Mob Attack Details for Select Target Strategy  
│  └─ 📝 Story: Chat system displays attack results for all mob members  
│  
└─ ⚙️ **Determine Available Attacks** (~5 stories)  

🎯 **Handle Mob Strategies** (4 features, ~21 stories)  
│  
├─ ⚙️ **Select Mob Strategy** (~6 stories)  
│  
├─ ⚙️ **Choose Target by Strategy** (2 stories)  
│  ├─ 📝 Story: GM selects Attack Common Target strategy and Mob manager applies strategy when mob's turn begins  
│  └─ 📝 Story: Combat Tracker displays selected common target for mob  
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
