# Refactor Code Agent to Common Command Runner - Complete Plan

## Overview
Refactor the code-agent feature to use the new `common_command_runner` framework. This will create a reusable pattern for building commands and establish the code-agent as the foundational example. Follow BDD pattern: extend only when adding new data/behavior; otherwise instantiate and set properties. Use test-first development with human-in-the-loop checkpoints.

## Phase 0: Archive Legacy Runner (CRITICAL FIRST STEP)

### 0.1 Archive Legacy Code Agent Runner
- Create archive folder: `behaviors/code-agent/archive/`
- Move `behaviors/code-agent/code-agent-runner.py` to `behaviors/code-agent/archive/code-agent-runner.py`
- Move `behaviors/code-agent/code-agent-runner-test.py` to `behaviors/code-agent/archive/code-agent-runner-test.py` (if keeping for reference)
- Update `behaviors/code-agent/behavior.json` to set `"deployed": false` (or remove the deployed flag entirely)
- Verify sync no longer picks up the legacy runner by running sync and confirming it's not processed

**STOP POINT:** Confirm legacy runner is archived and no longer deployed before proceeding to Phase 1

## Phase 1: Create Command Creation Meta-Command (Generate Everything)

### 1.1 Analyze Current Command Structure
- Review `behaviors/code-agent/structure/code-agent-structure-create-cmd.md` to understand current creation process
- Review archived `behaviors/code-agent/archive/code-agent-runner.py` `Feature.create()` method (lines 879-898) for reference
- Review BDD pattern in `behaviors/bdd/bdd-runner.py` to understand extension patterns
- Document the current file generation patterns

**STOP POINT:** Review current structure analysis before proceeding

### 1.2 Design Command Creation Command (Generate Everything)
- Design `behaviors/code-agent/create/code-agent-create-command-cmd.md`
- Command should generate:
  - Rule files (`.mdc`) with proper structure, When/Then, Always/Never, Executing Commands
  - Command files (`.md`) with Purpose, Usage, Rule, Runner, Steps (with clear performers)
  - Runner function stubs (`.py`) if needed
  - Related files (MCP configs, behavior.json updates, etc.)
- Define the command interface:
  - Input: feature name, behavior name, command type(s), rule content, command steps
  - Output: All generated files following structure patterns

**STOP POINT:** Get approval on command creation command design before creating file

### 1.3 Create Command File
- Create `behaviors/code-agent/create/code-agent-create-command-cmd.md`
- Include proper structure: Purpose, Usage, Rule, Runner, Steps
- Define steps with clear performer (User, Code, AI Agent)

**STOP POINT:** Review command file before proceeding

### 1.4 Design Support Code for Command Creation
- Determine what support code is needed:
  - File generation functions
  - Template processing
  - Validation logic
  - Integration with structure rules
- Determine if we extend `Command` or instantiate and set properties (per BDD pattern)

**STOP POINT:** Get approval on support code design before implementing

### 1.5 Implement Command Creation Using Common Command Runner (Test-First)
- Write tests first for command creation functionality
- Create command class - determine if extending `Command` or instantiating (per BDD pattern)
- Use `BaseRule` to load `code-agent-structure-rule.mdc` for validation
- Implement file generation logic following naming patterns
- Add validation to ensure generated files comply with structure rules

**STOP POINT:** Review test approach, then review implementation after tests pass

### 1.6 Extend Command if Needed
- If new data/behavior needed, extend appropriate base class
- Otherwise, use composition (instantiate and set properties)
- Follow BDD pattern from `bdd-runner.py`

**STOP POINT:** Review command extension/composition approach

## Phase 2: Create Code Agent Runner Extension

### 2.1 Design Code Agent Runner Architecture
- Determine how `code_agent_runner` should use `common_command_runner`:
  - Which base classes to use (Command, CodeAugmentedCommand, IncrementalCommand, etc.)
  - When to extend vs instantiate (per BDD pattern)
  - How to map existing archived `code-agent-runner.py` functions to new structure
  - How to handle consolidated runner pattern vs individual commands

**STOP POINT:** Review architecture design

### 2.2 Design Rule for Code Agent Commands
- Review `behaviors/code-agent/structure/code-agent-structure-rule.mdc`
- Determine what needs to be in the rule
- Identify validation patterns that should become heuristics
- Design heuristics for command structure validation:
  - Do commands have right steps?
  - Are steps specific about who's doing what (AI vs Code vs Human)?
  - Other command-specific validations

**STOP POINT:** Get approval on rule design before creating/updating rule file

### 2.3 Create/Update Rule File
- Create or update rule file with heuristics specifications
- Add DO/DON'T examples for each heuristic
- Ensure rule follows proper structure

**STOP POINT:** Review rule file before proceeding

### 2.4 Design Heuristic Support Code
- Design `CodeAgentHeuristic` classes extending `CodeHeuristic`:
  - `CommandStepsHeuristic` - validates steps have proper performers
  - `CommandStructureHeuristic` - validates command file structure
  - `RuleCommandLinkageHeuristic` - validates rule-command linkages
  - Other command-specific heuristics
- Determine implementation approach

**STOP POINT:** Get approval on heuristic design before implementing

### 2.5 Implement Heuristics (Test-First)
- Write tests first for each heuristic
- Implement heuristic classes extending `CodeHeuristic`
- Each heuristic uses code to detect violations (scanning command files, checking structure, etc.)

**STOP POINT:** Review test approach, then review implementation after tests pass

### 2.6 Create Base Code Agent Command Classes
- Create `behaviors/code-agent/code_agent_runner.py` (new file)
- Implement base command classes following BDD pattern:
  - Determine if extending or instantiating base classes
  - `CodeAgentCommand` - base for all code-agent commands (if needed)
  - `StructureCommand` - for structure validation/fix/create
  - `SyncCommand` - for sync operations
  - `IndexCommand` - for index generation
  - `ConsistencyCommand` - for consistency analysis
- Each should use appropriate `common_command_runner` base classes

**STOP POINT:** Review base command structure

### 2.7 Migrate Structure Command First (Test-First)
- Write tests first for `StructureCommand`
- Refactor archived `Feature.validate()`, `Feature.repair()`, `Feature.create()` logic to use new command structure
- Map existing validation logic to `CodeAugmentedCommand` with heuristics
- Integrate heuristics into `StructureCommand`
- Ensure backward compatibility with existing CLI interface

**STOP POINT:** Review test approach, then review implementation after tests pass

### 2.8 Extend Structure Command if Needed
- If new data/behavior needed, extend appropriate base class
- Otherwise, use composition
- Follow BDD pattern

**STOP POINT:** Review command extension/composition approach

## Phase 3: Implement Sync Command

### 3.1 Design Sync Command
- Review `behaviors/code-agent/sync/code-agent-sync-cmd.md`
- Map sync logic to `common_command_runner` pattern
- Determine if sync should be incremental or full
- Determine if extending or instantiating base classes

**STOP POINT:** Review sync command design

### 3.2 Implement Sync Command (Test-First)
- Write tests first for `SyncCommand`
- Create `SyncCommand` using appropriate base class (extend or instantiate)
- Migrate archived `Feature.sync()` logic to new command structure
- Handle file routing, merging, and conflict resolution
- Maintain backward compatibility

**STOP POINT:** Review test approach, then review implementation after tests pass

### 3.3 Extend Sync Command if Needed
- If new data/behavior needed, extend appropriate base class
- Otherwise, use composition

**STOP POINT:** Review command extension/composition approach

## Phase 4: Implement Index Command

### 4.1 Design Index Command
- Review `behaviors/code-agent/index/code-agent-index-cmd.md`
- Map index generation logic to `common_command_runner` pattern
- Determine if indexing should be incremental
- Determine if extending or instantiating base classes

**STOP POINT:** Review index command design

### 4.2 Implement Index Command (Test-First)
- Write tests first for `IndexCommand`
- Create `IndexCommand` using appropriate base class
- Migrate archived `Feature.generate_index()` logic to new command structure
- Handle purpose management (code preserves, AI updates)
- Maintain backward compatibility

**STOP POINT:** Review test approach, then review implementation after tests pass

### 4.3 Extend Index Command if Needed
- If new data/behavior needed, extend appropriate base class
- Otherwise, use composition

**STOP POINT:** Review command extension/composition approach

## Phase 5: Implement Consistency Command

### 5.1 Design Consistency Command
- Review `behaviors/code-agent/consistency/code-agent-consistency-cmd.md`
- Map consistency analysis logic to `common_command_runner` pattern
- Determine analysis approach (heuristics vs AI analysis)
- Determine if extending or instantiating base classes

**STOP POINT:** Review consistency command design

### 5.2 Implement Consistency Command (Test-First)
- Write tests first for `ConsistencyCommand`
- Create `ConsistencyCommand` using appropriate base class
- Migrate archived `Feature.analyze_consistency()` logic to new command structure
- Integrate with heuristics if applicable
- Maintain backward compatibility

**STOP POINT:** Review test approach, then review implementation after tests pass

### 5.3 Extend Consistency Command if Needed
- If new data/behavior needed, extend appropriate base class
- Otherwise, use composition

**STOP POINT:** Review command extension/composition approach

## Phase 6: Complete Framework and Documentation

### 6.1 Update Documentation
- Update `behaviors/code-agent/docs/code-agent-structure.md` with new approach
- Document how to create new commands using the framework
- Create examples showing the pattern
- Document extension vs instantiation guidelines

### 6.2 Migration Guide
- Document migration path from old runner to new runner
- Create compatibility layer if needed
- Update all command references

### 6.3 Final Testing
- Test all commands end-to-end
- Verify backward compatibility
- Ensure all existing functionality works

**STOP POINT:** Final review before marking complete

## Key Principles

1. **Archive legacy runner first** - Move to archive folder and set deployed: false to avoid sync conflicts
2. **Generate everything** - Rules, commands, runners, related files
3. **Extend only when needed** - Only extend when adding new data/behavior; otherwise instantiate and set properties (BDD pattern)
4. **Heuristics are rule-specific** - Use code to detect violations (e.g., command structure validation)
5. **Test-first** - Write tests before implementation
6. **Human-in-the-loop** - Stop after every meaningful increment for review/approval

## Files to Create/Modify

### Archive (Phase 0):
- `behaviors/code-agent/archive/code-agent-runner.py` (moved from root)
- `behaviors/code-agent/archive/code-agent-runner-test.py` (moved from root, optional)

### New Files:
- `behaviors/code-agent/create/code-agent-create-command-cmd.md`
- `behaviors/code-agent/code_agent_runner.py` (new implementation)
- `behaviors/code-agent/code_agent_heuristics.py` (heuristic classes)

### Modified Files:
- `behaviors/code-agent/behavior.json` (set deployed: false in Phase 0)
- `behaviors/code-agent/structure/code-agent-structure-rule.mdc` (add heuristics)
- `behaviors/code-agent/docs/code-agent-structure.md` (update documentation)

