# Code Agent Behavior Feature Outline

## Overview
This Behavior Feature contains behaviors for managing AI behavior files themselves - the behaviors that govern how behaviors are structured, validated, indexed, synced, and maintained. These behaviors enable the self-managing behavior system.

## Main Behaviors

**Behavior Consistency** - When behaviors are changed, deleted, updated, or created, validate for inconsistencies, overlapping behaviors, or inconsistent guidance, and surface potential contradictions or redundancies for review.

**Behavior Index** - Maintain a searchable index of all AI behaviors across features, tracking file locations, purposes, and modification timestamps. The index enables discovery and consistency checking.

**Behavior Structure** - Validate, fix, and create AI behaviors following structure and naming conventions. Ensures all behaviors follow consistent patterns for modularity, consistency, and discoverability.

**Behavior Suggest** - Analyze conversation patterns and suggest creating new behaviors when repetitive tasks are detected, helping users create reusable behavior definitions.

**Behavior Sync** - Keep AI behaviors up to date across all features by syncing files from `features/*/code-agent-behaviors/` folders to `.cursor/` directories, merging MCP configs and tasks.json files.

## Tools

**Orchestrator:** Watcher processes managed via Task configs (`code-agent-behavior-tasks.json`) merged into `.vscode/tasks.json` - auto-start watchers on IDE launch using PID files in `.cursor/watchers/`.

**MCP:** MCP configs (`*-mcp.json`) synced to `.cursor/mcp/` and merged when multiple configs exist.

## Related Features
This feature manages itself and all the lifecycle of all other behavior features.
