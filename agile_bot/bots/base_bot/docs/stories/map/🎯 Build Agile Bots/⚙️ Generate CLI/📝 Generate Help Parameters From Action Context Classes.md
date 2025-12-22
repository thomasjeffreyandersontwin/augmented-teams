# 📝 Generate Help Parameters From Action Context Classes

## Story

**As a** CLI Generator  
**I want to** generate help parameter documentation from action context classes  
**So that** parameter names are always correct and in sync with the typed context

## Acceptance Criteria

```gherkin
(AC) CLI Generator --> WHEN ActionFactory.get_action_class is called with action name
(AC) CLI Generator --> THEN Returns the action class for introspection
(AC) CLI Generator --> AND Action class has context_class attribute pointing to typed context

(AC) CLI Generator --> WHEN Parameters are extracted from context class
(AC) CLI Generator --> THEN Field names are converted from underscores to dashes
(AC) CLI Generator --> AND Parameter format is --field-name (not --field_name)

(AC) CLI Generator --> WHEN Help is generated for actions
(AC) CLI Generator --> THEN Parameters are dynamically extracted from context_class
(AC) CLI Generator --> AND No hardcoded parameter lists are used
(AC) CLI Generator --> AND Parameter documentation stays in sync with code

(AC) CLI Generator --> WHEN Unknown action name is provided
(AC) CLI Generator --> THEN ActionFactory.get_action_class returns None
```

## Implementation Notes

- `ActionFactory.get_action_class(action_name)` is a static method for introspection
- Dynamically inspects `context_class` dataclass fields using `dataclasses.fields()`
- Converts `field_name` to `--field-name` for CLI convention
- Used by `help_action.py`, `unified_help_generator.py`, `cursor_command_generator.py`

