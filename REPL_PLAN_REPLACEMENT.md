## Interaction Flow

Shows objects sending messages to each other. Format: `object.message(params) -> return`

### Execute Instructions with Scope

```
User: "code.validate.instructions scope='Story1'"

repl_session.execute_command(input="code.validate.instructions scope='Story1'")
  -> command_parser.parse(input="code.validate.instructions scope='Story1'")
    <- behavior="code", action="validate", operation="instructions", args="scope='Story1'"
  
  -> cli_bot.behaviors.navigate_to(name="code")
    -> bot.behaviors.get(name="code")
      <- behavior: Behavior
    <- cli_behavior: CLIBehavior
  
  -> cli_behavior.actions.navigate_to(name="validate")
    -> behavior.actions.get(name="validate")
      <- action: ValidateRulesAction
    <- cli_action: CLIAction
  
  -> cli_action.instructions(args="scope='Story1'")
    -> cli_action._parse_args_to_context(args="scope='Story1'")
      -> scope = Scope(type=STORY, value=["Story1"])
        -> scope.__post_init__()
          -> filter = KnowledgeGraphFilter(scope=scope)
        <- filter: KnowledgeGraphFilter
      <- context: ValidateActionContext(scope=scope)
    
    -> action.get_instructions(context=context)
      -> scope.filter_graph(graph=knowledge_graph)
        -> filter.apply_graph(graph=knowledge_graph)
        <- filtered_graph: Dict
      <- instructions_dict: Dict(template=..., rules=..., scope_info=...)
    
    -> cli_action._format_result(result=instructions_dict)
    <- formatted_output: str
  
  <- output: str

Display: output
```

### Submit with Domain Action

```
User: "submit"

repl_session.execute_command(input="submit")
  -> cli_action = cli_bot.behaviors.current.actions.current
  
  -> cli_action.submit(args="")
    -> cli_action._parse_args_to_context(args="")
    <- context: ValidateActionContext()
    
    -> action.submit(context=context)
      -> validator.run_validation()
      -> bot.behavior_action_state.mark_submitted()
      <- result: Dict(status="success", violations=0)
    
    -> cli_action._format_result(result=result)
    <- output: str
  
  <- output: str

Display: output
```

### Navigate Using Properties

```
User: "next"

repl_session.execute_command(input="next")
  -> cli_bot.behaviors.current
    -> bot.behavior_action_state.current_behavior
    <- "code"
    -> bot.behaviors.get(name="code")
    <- cli_behavior: CLIBehavior
  
  -> cli_behavior.actions.next
    -> bot.behavior_action_state.current_action
    <- "validate"
    -> behavior.actions.get_next(current="validate")
    <- action: Action or None
  
  -> bot.behavior_action_state.set_current(behavior="code", action="render") if action
  
  <- message: str

Display: message
```

---

## Key Decisions

1. **CLI Mirror Pattern**: CLI wraps domain with string interfaces
2. **CLIAction owns parsing**: Each subclass implements `_parse_args_to_context()`
3. **Domain owns state**: Bot.behavior_action_state handles persistence
4. **Scope in domain**: Not CLI responsibility

## File Structure

```
repl_cli/
├── repl_session.py
├── cli_model/
│   ├── cli_bot.py
│   ├── cli_behaviors.py
│   ├── cli_behavior.py
│   ├── cli_actions.py
│   └── cli_action.py
├── cli_display.py
└── command_parser.py
```

**Changes from original:**
- No `state/` package - Bot owns behavior_action_state and scope
- No display sub-packages - one `cli_display.py` with StatusDisplay
- No `interaction/` package - `command_parser.py` at top level
- **3 packages total**: repl_cli root, cli_model, done

