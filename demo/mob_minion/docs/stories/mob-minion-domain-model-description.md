# Domain Model Description: Mob Minion

**File Name**: `mob-minion-domain-model-description.md`
**Location**: `demo/mob_minion/docs/stories/mob-minion-domain-model-description.md`

## Solution Purpose

This system enables Game Masters to efficiently manage minions in Foundry Virtual Tabletop (VTT) by grouping them into coordinated mobs. Mobs allow GMs to control multiple minions as a single unit, applying strategies for target selection and executing coordinated actions. The system integrates with Foundry VTT's existing actor/token, combat, movement, and template systems.

---

## Domain Model Descriptions

### Mob

A **Mob** is a collection of minions that act together as a coordinated unit. The Mob groups minions together for coordinated action, allowing a Game Master to control all minions in the mob by selecting any single minion token. The Mob maintains a collection of minion tokens and associates a strategy with mob behavior to determine how the mob selects targets and executes actions.

**Key Responsibilities:**
- Groups minions together for coordinated action
- Maintains collection of minion tokens
- Associates strategy with mob behavior

**Relationships:**
- Contains multiple **Minion** tokens
- Uses a **Strategy** to determine behavior
- Can be spawned from a **Template**

### Minion

A **Minion** represents an individual token/actor in Foundry VTT that can be grouped into a mob. Each Minion belongs to a mob for coordinated control, allowing the Game Master to command all minions in a mob by selecting any single minion.

**Key Responsibilities:**
- Represents individual token/actor in Foundry VTT
- Belongs to a mob for coordinated control

**Relationships:**
- Belongs to a **Mob** (many minions to one mob)
- Represents a Foundry VTT actor/token

### Strategy

A **Strategy** defines behavioral rules for how a mob selects targets and executes actions. Strategies determine target selection behavior for the mob, defining how the mob chooses which enemy to attack. Common strategies include: attack the most powerful target, attack the weakest target, defend the leader, and attack the most damaged target.

**Key Responsibilities:**
- Determines target selection behavior for mob
- Defines how mob chooses which enemy to attack

**Relationships:**
- Used by **Mob** to determine behavior
- Evaluates **Target** options for selection

### Target

A **Target** represents an enemy token/actor that the mob can attack. Targets are evaluated by the strategy for selection, allowing the mob to choose the appropriate enemy based on the selected strategy.

**Key Responsibilities:**
- Represents enemy token/actor to attack
- Evaluated by strategy for selection

**Relationships:**
- Evaluated by **Strategy** for selection
- Represents a Foundry VTT actor/token (enemy)

### Action

An **Action** represents what the mob does, such as move, attack, or area attack. Actions respect range and positioning constraints, ensuring that mob actions are valid within the game's movement and combat rules.

**Key Responsibilities:**
- Represents mob action (move, attack, area attack)
- Respects range and positioning constraints

**Relationships:**
- Executed by **Mob**
- Constrained by **Range** limitations
- Can target **Target** enemies

### Range

**Range** defines distance constraints for actions, determining valid targets and movement. Range ensures that mob actions respect the game system's movement and combat rules, preventing invalid actions that exceed distance limitations.

**Key Responsibilities:**
- Defines distance constraints for actions
- Determines valid targets and movement

**Relationships:**
- Constrains **Action** execution
- Determines valid **Target** selection

### Template

A **Template** defines a predefined actor configuration for spawning mobs. Templates enable quick mob creation from saved configurations, allowing Game Masters to quickly spawn mobs with predefined minion compositions and settings.

**Key Responsibilities:**
- Defines predefined actor configuration for spawning
- Enables quick mob creation from saved configurations

**Relationships:**
- Used to spawn **Mob** instances
- Contains Foundry VTT actor configurations

---

## Source Material

- **Input Document**: `demo/mob_minion/input.txt` - Project vision and requirements
- **Clarification**: `demo/mob_minion/docs/stories/clarification.json` - Domain understanding and user context
- **Story Graph**: `demo/mob_minion/docs/stories/story-graph.json` - Structured story map with domain concepts

