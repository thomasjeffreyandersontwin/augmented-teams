# Domain Model Description: Mob Minion

**File Name**: `mob-minion-domain-model-description.md`
**Location**: `mob_minion/docs/stories/mob-minion-domain-model-description.md`

## Solution Purpose
Domain model for Mob Minion

---

## Domain Model Descriptions

### Action

**Key Responsibilities:**
- **represents combat action**: This responsibility involves collaboration with Mob, Target.
- **executed by all minions in mob**: This responsibility involves collaboration with Minion.

### Minion

**Key Responsibilities:**
- **represents individual token**: This responsibility involves collaboration with Foundry Token.
- **belongs to mob**: This responsibility involves collaboration with Mob.

### Mob

**Key Responsibilities:**
- **groups minions together**: This responsibility involves collaboration with Minion.
- **coordinates group actions**: This responsibility involves collaboration with Strategy, Action.

### Mob Template

**Key Responsibilities:**
- **defines preset mob configuration**: This responsibility involves collaboration with Mob.

### Strategy

**Key Responsibilities:**
- **determines target selection algorithm**: This responsibility involves collaboration with Target.
- **guides mob behavior**: This responsibility involves collaboration with Mob, Action.

### Target

**Key Responsibilities:**
- **represents entity being attacked**: This responsibility involves collaboration with Foundry Token.

---

## Source Material

**Primary Source:** `demo\mob_minion\input.txt`
**Date Generated:** 2025-01-27
**Context:** Shape phase - Domain model extracted from story-graph.json
