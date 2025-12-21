# Inject Rules Into AI Chat Message

**Story:** Inject Rules Into AI Chat Message  
**Epic:** Validate with Rules  
**Status:** Planning

## Overview

Create a new `rules` action that loads and formats behavior rules as AI context. This allows users to invoke AI chat with a digested set of rules so the AI can reference them while working.

**Invocation:**
```bash
story_bot --behavior code --action rules --message "help me refactor this function"
```

## Key Design Decisions

1. **New action, not a parameter** - This is a standalone action like `help`, not a modification to `build` or `validate`
2. **`workflow: false`** - Not part of the ordered workflow sequence (clarify → strategy → build → validate → render)
3. **Rules as first-class module** - Move rules out of `validate/` into its own `rules/` module
4. **Keep Rule intact** - Don't split Rule into pure/scannable - validation IS what rules do
5. **Two-channel output** - Rules digest goes to BOTH display (user sees it) AND AI context (AI follows it)
6. **Digest vs Full format** - AI context gets compact digest (~60 lines), display gets full format with examples (~2000+ lines)

## Instructions Class Pattern

The `Instructions` class provides two output channels:

```
┌─────────────────────────────────────────────────────────────────┐
│                      Instructions Object                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  add("text")           →  base_instructions  →  AI CONTEXT      │
│                            (sent to AI)                          │
│                                                                  │
│  add_display("text")   →  display_content    →  USER DISPLAY    │
│                            (written to file)                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**How display works:**
1. `add_display()` appends to `_display_content` list
2. Base `Action._finalize_display_content()` writes to `.cursor/display/status.md`
3. Adds instruction for AI to read and show the file contents to user

**Reference implementation:** See `HelpAction` which uses `add_display()` extensively to show help content to users.

## Digest Format for AI Context

### Problem: Full Rules Are Too Large

- ~30 active rules in code behavior
- ~70 lines each with full examples
- = ~2,100 lines per request - **too much**

### Solution: Compact Digest Format

| Channel | Format | Size | Method |
|---------|--------|------|--------|
| AI Context | Digest | ~60 lines | `formatted_rules_digest()` |
| User Display | Full | ~2000 lines | `formatted_rules()` |

### Digest Format Example

```
**Rules to follow:**

- **delegate_to_lowest_level**: Code must delegate responsibilities to the lowest-level object that can handle them. If a collection class can do something, delegate to it rather than implementing it in the parent.
- **use_domain_language**: Code must use domain-specific language, not generic terms. Objects should expose properties representing what they contain.
- **avoid_excessive_guards**: Don't add unnecessary defensive code. Trust internal code and framework guarantees.
...
```

### New Method: `formatted_rules_digest()`

Add to `Rules` class:

```python
def formatted_rules_digest(self) -> str:
    """Return condensed rules digest - just name + description for AI context."""
    lines = ["**Rules to follow:**", ""]
    for rule in self._load_rules():
        lines.append(f"- **{rule.name}**: {rule.description}")
    return '\n'.join(lines)
```

### Rule Description Quality Check

**CRITICAL:** Descriptions must be self-contained and actionable without examples.

Each description should answer:
1. **WHAT** is the rule? (the principle)
2. **WHY** does it matter? (the consequence)
3. **HOW** to apply it? (actionable guidance)

#### Rules Description Analysis

**GOOD - Self-contained and actionable:**

| Rule | Description | Rating |
|------|-------------|--------|
| `delegate_to_lowest_level` | "Code must delegate responsibilities to the lowest-level object that can handle them. If a collection class can do something, delegate to it rather than implementing it in the parent." | ✅ Excellent |
| `eliminate_duplication` | "CRITICAL: Every piece of knowledge should have a single, authoritative representation (DRY principle). Extract repeated logic into reusable functions..." | ✅ Excellent |
| `stop_writing_useless_comments` | "CRITICAL: Most comments are useless. Kill AI-generated docstrings that just repeat function names and parameters. Only write comments for complex non-obvious algorithms..." | ✅ Excellent |
| `avoid_unnecessary_parameter_passing` | "Don't pass parameters to internal methods when the value is already accessible through instance variables. Access instance properties directly..." | ✅ Good |
| `use_domain_language` | "CRITICAL: Code must use domain-specific language, not generic terms. Objects should expose properties representing what they contain..." | ✅ Good |
| `use_explicit_dependencies` | "CRITICAL: Make dependencies visible through constructor injection. Pass dependencies through constructors, make all dependencies explicit..." | ✅ Good |

**NEEDS OPTIMIZATION:**

| Rule | Current Description | Issue | Suggested Improvement |
|------|---------------------|-------|----------------------|
| `prefer_object_model_over_config` | "Use existing object model to access information instead of directly accessing configuration files" | Too vague - when? why? | "AVOID reading config files directly when object model already exposes the data. Use `bot.name` not `config['name']`. Objects encapsulate config access." |
| `hide_calculation_timing` | "CRITICAL: Code must hide calculations..." | Overlaps with `hide_business_logic_behind_properties` | Consider merging or clarifying distinction |
| `hide_business_logic_behind_properties` | "CRITICAL: Hide business logic behind properties..." | Overlaps with `hide_calculation_timing` | Consider merging or clarifying distinction |
| `use_consistent_indentation` | "Use consistent, meaningful indentation..." | Basic/obvious | May not need to be in AI context - standard tooling handles this |
| `place_imports_at_top` | "Place all import statements at the top..." | Basic/obvious | May not need to be in AI context - linters handle this |

**RECOMMENDATIONS:**

1. **Remove basic linting rules from digest** - Rules like `use_consistent_indentation`, `place_imports_at_top` are handled by linters/formatters. Don't waste AI context on them.

2. **Merge overlapping rules** - `hide_calculation_timing` and `hide_business_logic_behind_properties` seem to express the same principle.

3. **Add "trigger words"** - Help AI recognize when to apply: "When you see X, apply this rule"

4. **Pattern for good descriptions:**
   ```
   WHAT: [The principle in imperative form]
   TRIGGER: [When to apply - what code smell indicates violation]
   ACTION: [Specific refactoring action to take]
   ```

**TODO:** 
- [ ] Review and optimize rule descriptions for standalone clarity
- [ ] Consider adding `digest` field to rule JSON for custom short summaries
- [ ] Consider adding `priority` or `always_include` field to control which rules appear in digest
- [ ] Remove/disable basic linting rules that tools already handle

## Implementation Plan

### 1. Add `RulesActionContext` to `action_context.py`

```python
@dataclass
class RulesActionContext(ActionContext):
    """Context for rules action - getting rules digest with optional message.
    
    The behavior is already available via self.behavior in the action.
    The message is the user's actual request that should be processed with rules context.
    """
    message: Optional[str] = None
```

### 2. Create `actions/rules/` directory

**Move from `validate/`:**
- `rule.py`
- `rule_loader.py`  
- `rule_filter.py`
- `rules.py`

**Create new:**
- `__init__.py`
- `rules_action.py`

### 3. Create `rules_action.py`

The `Instructions` class provides two output channels:

| Method | Purpose | Destination |
|--------|---------|-------------|
| `add()` | AI context instructions | `base_instructions` - sent to AI |
| `add_display()` | User-visible output | `display_content` - written to `.cursor/display/status.md` and shown to user |

The base `Action` class automatically:
1. Writes `display_content` to `.cursor/display/status.md`
2. Adds instructions for AI to read and display that file to the user

**Implementation:**

```python
from typing import Dict, Any, Type
from agile_bot.bots.base_bot.src.actions.action import Action
from agile_bot.bots.base_bot.src.actions.action_context import ActionContext, RulesActionContext
from agile_bot.bots.base_bot.src.actions.rules.rules import Rules


class RulesAction(Action):
    context_class: Type[ActionContext] = RulesActionContext

    def do_execute(self, context: RulesActionContext) -> Dict[str, Any]:
        # Load rules for this behavior
        rules = Rules(behavior=self.behavior, bot_paths=self.behavior.bot_paths)
        
        instructions = self.instructions.copy()
        
        # =====================================================
        # DISPLAY CONTENT - Full format for user reference
        # Uses add_display() -> writes to .cursor/display/status.md
        # =====================================================
        instructions.add_display(f"## Rules Digest: {self.behavior.name}")
        instructions.add_display(f"_{len(rules)} rules loaded_")
        instructions.add_display("")
        instructions.add_display(rules.formatted_rules())  # FULL format with examples
        
        # =====================================================
        # AI CONTEXT - Compact digest only (~60 lines vs ~2000)
        # Uses add() -> goes into AI's context window
        # =====================================================
        
        # Add the user's message first
        if context.message:
            instructions.add("")
            instructions.add("**User Request:**")
            instructions.add(context.message)
            instructions.add("")
        
        # Add DIGEST to AI context (compact - name + description only)
        instructions.add("")
        instructions.add(rules.formatted_rules_digest())  # COMPACT format
        instructions.add("")
        instructions.add("CRITICAL: Follow the rules above when responding to the user request.")
        instructions.add("Cite specific rule names when making decisions.")
        
        return {'instructions': instructions.to_dict()}
```

**Flow:**
1. User invokes: `story_bot --behavior code --action rules --message "help me refactor"`
2. Action loads rules and formats digest
3. Digest added to **both**:
   - `display_content` → written to `.cursor/display/status.md` → AI reads and shows to user
   - `base_instructions` → AI context for guidance
4. User sees the rules digest printed
5. AI has rules in context and references them while responding

### 4. Create `base_actions/rules/action_config.json`

```json
{
  "name": "rules",
  "description": "Display digested rules for the current behavior as AI context",
  "workflow": false,
  "action_class": "agile_bot.bots.base_bot.src.actions.rules.rules_action.RulesAction",
  "instructions": [
    "Display rules digest for the current behavior",
    "Include user message with rules context for AI guidance"
  ]
}
```

### 5. Update imports in `validate/`

Update `validate_action.py` and other validate files to import from new location:

```python
# Before
from agile_bot.bots.base_bot.src.actions.validate.rules import Rules

# After
from agile_bot.bots.base_bot.src.actions.rules.rules import Rules
```

### 6. Add Test Class

Add to `test_validate_knowledge_and_content_against_rules.py`:

```python
# ============================================================================
# STORY: Inject Rules Into AI Chat Message
# Epic: Validate with Rules
# ============================================================================

class TestInjectRulesIntoAIChatMessage:
    """Story: Inject Rules Into AI Chat Message - Load and format behavior rules for AI context."""

    def test_rules_action_loads_rules_for_behavior(self, bot_directory, workspace_directory):
        """
        SCENARIO: Rules action loads rules for behavior
        GIVEN: behavior is 'code' with rules defined
        WHEN: rules action executes
        THEN: rules are loaded from behavior rules directory
        """
        # Given: Setup behavior with rules
        bootstrap_env(bot_directory, workspace_directory)
        given_test_bot_directory_created(bot_directory, 'story_bot', 'code')
        rules_dir = bot_directory / 'behaviors' / 'code' / 'rules'
        rules_dir.mkdir(parents=True, exist_ok=True)
        (rules_dir / 'test_rule.json').write_text(json.dumps({
            'description': 'Test rule description',
            'examples': []
        }), encoding='utf-8')
        
        action = given_action_initialized('rules', bot_directory, 'story_bot', 'code', workspace_directory=workspace_directory)
        
        # When: Execute rules action
        from agile_bot.bots.base_bot.src.actions.action_context import RulesActionContext
        context = RulesActionContext()
        result = action.do_execute(context)
        
        # Then: Rules are loaded
        assert 'instructions' in result
        instructions = result['instructions']
        assert 'base_instructions' in instructions

    def test_rules_action_includes_message_in_context(self, bot_directory, workspace_directory):
        """
        SCENARIO: Rules action includes user message in context
        GIVEN: behavior is 'code' and message is 'help me refactor'
        WHEN: rules action executes with message
        THEN: instructions include user message
        """
        # Given: Setup behavior
        bootstrap_env(bot_directory, workspace_directory)
        given_test_bot_directory_created(bot_directory, 'story_bot', 'code')
        
        action = given_action_initialized('rules', bot_directory, 'story_bot', 'code', workspace_directory=workspace_directory)
        
        # When: Execute with message
        from agile_bot.bots.base_bot.src.actions.action_context import RulesActionContext
        context = RulesActionContext(message='help me refactor this function')
        result = action.do_execute(context)
        
        # Then: Message is in instructions
        instructions = result['instructions']
        base_instructions = instructions.get('base_instructions', [])
        instructions_text = '\n'.join(str(i) for i in base_instructions)
        assert 'help me refactor' in instructions_text

    def test_rules_action_displays_rules_digest(self, bot_directory, workspace_directory):
        """
        SCENARIO: Rules action displays rules digest to user
        GIVEN: behavior has 2 rules defined
        WHEN: rules action executes
        THEN: display content shows formatted rules digest
        """
        # Given: Setup behavior with multiple rules
        bootstrap_env(bot_directory, workspace_directory)
        given_test_bot_directory_created(bot_directory, 'story_bot', 'code')
        rules_dir = bot_directory / 'behaviors' / 'code' / 'rules'
        rules_dir.mkdir(parents=True, exist_ok=True)
        (rules_dir / 'rule_one.json').write_text(json.dumps({
            'description': 'First rule',
            'examples': []
        }), encoding='utf-8')
        (rules_dir / 'rule_two.json').write_text(json.dumps({
            'description': 'Second rule',
            'examples': []
        }), encoding='utf-8')
        
        action = given_action_initialized('rules', bot_directory, 'story_bot', 'code', workspace_directory=workspace_directory)
        
        # When: Execute rules action
        from agile_bot.bots.base_bot.src.actions.action_context import RulesActionContext
        context = RulesActionContext()
        result = action.do_execute(context)
        
        # Then: Display content has rules digest
        instructions = result['instructions']
        display_content = instructions.get('display_content', [])
        display_text = '\n'.join(display_content)
        assert 'Rules Digest' in display_text or len(display_content) > 0

    def test_rules_action_is_not_workflow_action(self, bot_directory, workspace_directory):
        """
        SCENARIO: Rules action is not part of workflow
        GIVEN: rules action is initialized
        WHEN: action properties are checked
        THEN: workflow property is False
        """
        # Given: Setup
        bootstrap_env(bot_directory, workspace_directory)
        given_test_bot_directory_created(bot_directory, 'story_bot', 'code')
        
        action = given_action_initialized('rules', bot_directory, 'story_bot', 'code', workspace_directory=workspace_directory)
        
        # Then: Not a workflow action
        assert action.workflow == False
```

## Architecture After Implementation

### Directory Structure

```
actions/
├── rules/                     # NEW - First-class rules module
│   ├── __init__.py
│   ├── rule.py               # Rule: name, description, examples, scanning, violations
│   ├── rule_loader.py        # Loads rules from disk
│   ├── rule_filter.py        # Filters files for rules
│   ├── rules.py              # Rules collection with validate() method
│   └── rules_action.py       # RulesAction: displays digested rules
│
├── validate/
│   ├── validate_action.py    # Uses Rules from rules module
│   ├── validation_executor.py
│   └── ...other validation files...
│
└── build/
    └── (can import rules/ for context injection)
```

### Dependency Graph

```
                    ┌──────────────┐
                    │    rules/    │  ← First-class concept
                    │              │
                    └──────┬───────┘
                           │
           ┌───────────────┼───────────────┐
           │               │               │
           ▼               ▼               ▼
    ┌──────────┐    ┌──────────┐    ┌──────────┐
    │ validate │    │  build   │    │  rules   │
    │  action  │    │  action  │    │  action  │
    └──────────┘    └──────────┘    └──────────┘
```

## Implementation Checklist

### Phase 1: Core Infrastructure
- [ ] Add `RulesActionContext` to `action_context.py`
- [ ] Create `actions/rules/` directory
- [ ] Move `rule.py` from validate to rules
- [ ] Move `rule_loader.py` from validate to rules
- [ ] Move `rule_filter.py` from validate to rules
- [ ] Move `rules.py` from validate to rules
- [ ] Create `actions/rules/__init__.py`
- [ ] Add `formatted_rules_digest()` method to `Rules` class
- [ ] Create `actions/rules/rules_action.py`
- [ ] Create `base_actions/rules/action_config.json`
- [ ] Update imports in `validate/validate_action.py`
- [ ] Update imports in `validate/validation_executor.py`
- [ ] Update imports in `build/build_action.py`
- [ ] Update any other files importing from validate/rule*
- [ ] Add test class `TestInjectRulesIntoAIChatMessage`
- [ ] Run tests to verify nothing is broken

### Phase 2: Rule Description Optimization
- [ ] Review all rule descriptions for standalone clarity
- [ ] Optimize descriptions that need improvement (see analysis above)
- [ ] Consider merging overlapping rules (`hide_calculation_timing` / `hide_business_logic_behind_properties`)
- [ ] Disable basic linting rules that tools already handle (`use_consistent_indentation`, `place_imports_at_top`)
- [ ] Add `priority` or `always_include` field to rule JSON schema (optional)
- [ ] Add `digest` field to rule JSON for custom short summaries (optional)


