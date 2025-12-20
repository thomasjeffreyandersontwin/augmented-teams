# Domain Model Description: Mob Minion

**File Name**: `mob-minion-domain-model-description.md`
**Location**: `mob_minion/docs/stories/mob-minion-domain-model-description.md`

## Solution Purpose
Domain model for Mob Minion

---

## Domain Model Descriptions

### ActorTemplate

**Key Responsibilities:**
- **Define minion type**: This responsibility involves collaboration with MinionMember, FoundryActor.

### BoardToken

**Key Responsibilities:**
- **Represent minion visually**: This responsibility involves collaboration with MinionMember, FoundryScene.

### CombatAction

**Key Responsibilities:**
- **Apply to target**: This responsibility involves collaboration with CombatTarget, MinionMember.

### CombatTarget

**Key Responsibilities:**
- **Receive mob attack**: This responsibility involves collaboration with BoardToken, CombatAction.

### MinionMember

**Key Responsibilities:**
- **Participate in mob**: This responsibility involves collaboration with Mob.
- **Perform individual action**: This responsibility involves collaboration with BoardToken, CombatAction.

### Mob

**Key Responsibilities:**
- **Group minions together**: This responsibility involves collaboration with MinionMember.
- **Execute collective actions**: This responsibility involves collaboration with CombatAction, TargetingStrategy.

### MobTemplate

**Key Responsibilities:**
- **Define mob composition**: This responsibility involves collaboration with Mob, ActorTemplate.
- **Spawn mob instances**: This responsibility involves collaboration with Mob, FoundryScene.

### MovementPath

**Key Responsibilities:**
- **Represent path waypoints**: This responsibility involves collaboration with PathfindingStrategy, FoundryScene.
- **Validate path accessibility**: This responsibility involves collaboration with Mob, BoardToken.

### PathfindingStrategy

**Key Responsibilities:**
- **Get movement path**: This responsibility involves collaboration with Mob, FoundryScene.
- **Identify obstacles**: This responsibility involves collaboration with FoundryScene, BoardToken.

### TargetingStrategy

**Key Responsibilities:**
- **Identify targets by criteria**: This responsibility involves collaboration with CombatTarget, Mob.

---

## Source Material

**Primary Source:** `demo\mob_minion\input.txt`
**Date Generated:** 2025-01-27
**Context:** Shape phase - Domain model extracted from story-graph.json
