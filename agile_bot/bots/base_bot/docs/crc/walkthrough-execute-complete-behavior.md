# Walkthrough: Execute Complete Behavior In Headless Mode

**Scope:** Execute In Headless Mode.Execute In Headless Mode.Execute Complete Behavior.Execute complete behavior workflow in headless mode

**Story:** Human executes a complete behavior (clarify → strategy → build → validate → render) in headless mode with looping for each action until completion

## Scenario: Execute complete behavior workflow in headless mode

**Steps:**
- Given AI has written headless-context.md
- And headless mode is configured
- And user wants to execute shape behavior
- When human invokes CLI with --headless flag for complete behavior
- Then CLI executes clarify action with persistence directive
- And AI loops until clarify action indicates done
- And CLI detects clarify completion
- And CLI executes strategy action with persistence directive
- And AI loops until strategy action indicates done
- And CLI detects strategy completion
- And CLI executes build action with persistence directive
- And AI loops until build action indicates done
- And CLI detects build completion
- And CLI executes validate action with persistence directive
- And AI loops until validate action indicates done
- And CLI detects validate completion
- And CLI executes render action with persistence directive
- And AI loops until render action indicates done
- And CLI detects render completion
- And CLI reports entire behavior completed successfully

---

## Walk 1 - Covers: Steps 1-3 (Setup and clarify action execution)

### Realization:

```
# Step 1: Human invokes CLI with headless mode for complete behavior
result: ExecutionResult = HeadlessSession.invokes_complete_behavior(
    behavior: "shape",
    context_file: "headless-context.md"
)

# Step 2: Get configuration
  -> config: HeadlessConfig = HeadlessSession.get_configuration()
     return config: {api_key: "sk-...", log_dir: "logs/"}

# Step 3: Load execution context
  -> context: ExecutionContext = HeadlessSession.get_execution_context()
     -> context_loaded: ExecutionContext = ExecutionContext.loads_from_context_file(
            path: "headless-context.md"
        )
        return context_loaded: ExecutionContext
     return context: ExecutionContext

# Step 4: Execute clarify action with persistence directive
  -> clarify_result: ActionResult = HeadlessSession.executes_action_with_persistence_directive(
         behavior: "shape",
         action: "clarify",
         context: context
     )
     -> action_instructions: str = HeadlessSession.retrieves_action_instructions(
            behavior: "shape",
            action: "clarify"
        )
        return action_instructions: "Clarify requirements for story mapping..."
     
     -> prepared_instructions: str = HeadlessSession.prepares_instructions_with_persistence_directive(
            instructions: action_instructions,
            context: context
        )
        return prepared_instructions: "Keep doing this until 100% done or blocked:\n\n[instructions]"
     
     -> session_id_clarify: SessionId = HeadlessSession.executes_via_cursor_headless_api(
            instructions: prepared_instructions
        )
        return session_id_clarify: "session_clarify_111"
     
     -> loop_count_clarify: int = 0
     -> while True:
            -> api_response: Response = CursorHeadlessAPI.poll_session_status(
                   session_id: session_id_clarify
               )
               return api_response: {state: "running", progress: "..."}
            
            -> logged: bool = SessionLog.appends_response(
                   response: api_response,
                   loop_number: loop_count_clarify + 1
               )
               return logged: True
            
            -> ai_status: SessionStatus = HeadlessSession.detects_completion_or_block()
               return ai_status: {state: "running", done: False}
            
            if ai_status.done:
                break
            
            -> loop_count_clarify: int = loop_count_clarify + 1
            -> loop_instruction: str = Instructions.wraps_with_persistence_directive()
               return loop_instruction: "Keep doing this until 100% done or blocked:\n\n[instructions]"
            
            -> api_response: Response = CursorHeadlessAPI.send_instruction(
                   session_id: session_id_clarify,
                   instruction: loop_instruction
               )
               return api_response: {state: "running"}
     
     return clarify_result: {status: "completed", action: "clarify", total_loops: 3}

# Step 5: Detect clarify completion
  -> clarify_completion: bool = HeadlessSession.detects_action_completion(
         result: clarify_result
     )
     return clarify_completion: True
```

---

## Walk 2 - Covers: Steps 4-6 (Strategy and build action execution)

### Realization:

```
# Step 6: Execute strategy action with persistence directive
  -> strategy_result: ActionResult = HeadlessSession.executes_action_with_persistence_directive(
         behavior: "shape",
         action: "strategy",
         context: context
     )
     -> action_instructions: str = HeadlessSession.retrieves_action_instructions(
            behavior: "shape",
            action: "strategy"
        )
        return action_instructions: "Define strategy for story mapping approach..."
     
     -> prepared_instructions: str = HeadlessSession.prepares_instructions_with_persistence_directive(
            instructions: action_instructions,
            context: context
        )
        return prepared_instructions: "Keep doing this until 100% done or blocked:\n\n[instructions]"
     
     -> session_id_strategy: SessionId = HeadlessSession.executes_via_cursor_headless_api(
            instructions: prepared_instructions
        )
        return session_id_strategy: "session_strategy_222"
     
     -> loop_count_strategy: int = 0
     -> while True:
            -> api_response: Response = CursorHeadlessAPI.poll_session_status(
                   session_id: session_id_strategy
               )
               return api_response: {state: "running", progress: "..."}
            
            -> logged: bool = SessionLog.appends_response(
                   response: api_response,
                   loop_number: loop_count_strategy + 1
               )
               return logged: True
            
            -> ai_status: SessionStatus = HeadlessSession.detects_completion_or_block()
               return ai_status: {state: "running", done: False}
            
            if ai_status.done:
                break
            
            -> loop_count_strategy: int = loop_count_strategy + 1
            -> loop_instruction: str = Instructions.wraps_with_persistence_directive()
               return loop_instruction: "Keep doing this until 100% done or blocked:\n\n[instructions]"
            
            -> api_response: Response = CursorHeadlessAPI.send_instruction(
                   session_id: session_id_strategy,
                   instruction: loop_instruction
               )
               return api_response: {state: "running"}
     
     return strategy_result: {status: "completed", action: "strategy", total_loops: 2}

# Step 7: Detect strategy completion
  -> strategy_completion: bool = HeadlessSession.detects_action_completion(
         result: strategy_result
     )
     return strategy_completion: True

# Step 8: Execute build action with persistence directive
  -> build_result: ActionResult = HeadlessSession.executes_action_with_persistence_directive(
         behavior: "shape",
         action: "build",
         context: context
     )
     -> action_instructions: str = HeadlessSession.retrieves_action_instructions(
            behavior: "shape",
            action: "build"
        )
        return action_instructions: "Build knowledge graph for story map..."
     
     -> prepared_instructions: str = HeadlessSession.prepares_instructions_with_persistence_directive(
            instructions: action_instructions,
            context: context
        )
        return prepared_instructions: "Keep doing this until 100% done or blocked:\n\n[instructions]"
     
     -> session_id_build: SessionId = HeadlessSession.executes_via_cursor_headless_api(
            instructions: prepared_instructions
        )
        return session_id_build: "session_build_333"
     
     -> loop_count_build: int = 0
     -> while True:
            -> api_response: Response = CursorHeadlessAPI.poll_session_status(
                   session_id: session_id_build
               )
               return api_response: {state: "running", progress: "..."}
            
            -> logged: bool = SessionLog.appends_response(
                   response: api_response,
                   loop_number: loop_count_build + 1
               )
               return logged: True
            
            -> ai_status: SessionStatus = HeadlessSession.detects_completion_or_block()
               return ai_status: {state: "running", done: False}
            
            if ai_status.done:
                break
            
            -> loop_count_build: int = loop_count_build + 1
            -> loop_instruction: str = Instructions.wraps_with_persistence_directive()
               return loop_instruction: "Keep doing this until 100% done or blocked:\n\n[instructions]"
            
            -> api_response: Response = CursorHeadlessAPI.send_instruction(
                   session_id: session_id_build,
                   instruction: loop_instruction
               )
               return api_response: {state: "running"}
     
     return build_result: {status: "completed", action: "build", total_loops: 4}

# Step 9: Detect build completion
  -> build_completion: bool = HeadlessSession.detects_action_completion(
         result: build_result
     )
     return build_completion: True
```

---

## Walk 3 - Covers: Steps 7-9 (Validate and render action execution, final reporting)

### Realization:

```
# Step 10: Execute validate action with persistence directive
  -> validate_result: ActionResult = HeadlessSession.executes_action_with_persistence_directive(
         behavior: "shape",
         action: "validate",
         context: context
     )
     -> action_instructions: str = HeadlessSession.retrieves_action_instructions(
            behavior: "shape",
            action: "validate"
        )
        return action_instructions: "Validate knowledge graph against rules..."
     
     -> prepared_instructions: str = HeadlessSession.prepares_instructions_with_persistence_directive(
            instructions: action_instructions,
            context: context
        )
        return prepared_instructions: "Keep doing this until 100% done or blocked:\n\n[instructions]"
     
     -> session_id_validate: SessionId = HeadlessSession.executes_via_cursor_headless_api(
            instructions: prepared_instructions
        )
        return session_id_validate: "session_validate_444"
     
     -> loop_count_validate: int = 0
     -> while True:
            -> api_response: Response = CursorHeadlessAPI.poll_session_status(
                   session_id: session_id_validate
               )
               return api_response: {state: "running", progress: "..."}
            
            -> logged: bool = SessionLog.appends_response(
                   response: api_response,
                   loop_number: loop_count_validate + 1
               )
               return logged: True
            
            -> ai_status: SessionStatus = HeadlessSession.detects_completion_or_block()
               return ai_status: {state: "running", done: False}
            
            if ai_status.done:
                break
            
            -> loop_count_validate: int = loop_count_validate + 1
            -> loop_instruction: str = Instructions.wraps_with_persistence_directive()
               return loop_instruction: "Keep doing this until 100% done or blocked:\n\n[instructions]"
            
            -> api_response: Response = CursorHeadlessAPI.send_instruction(
                   session_id: session_id_validate,
                   instruction: loop_instruction
               )
               return api_response: {state: "running"}
     
     return validate_result: {status: "completed", action: "validate", total_loops: 1}

# Step 11: Detect validate completion
  -> validate_completion: bool = HeadlessSession.detects_action_completion(
         result: validate_result
     )
     return validate_completion: True

# Step 12: Execute render action with persistence directive
  -> render_result: ActionResult = HeadlessSession.executes_action_with_persistence_directive(
         behavior: "shape",
         action: "render",
         context: context
     )
     -> action_instructions: str = HeadlessSession.retrieves_action_instructions(
            behavior: "shape",
            action: "render"
        )
        return action_instructions: "Render knowledge graph to markdown..."
     
     -> prepared_instructions: str = HeadlessSession.prepares_instructions_with_persistence_directive(
            instructions: action_instructions,
            context: context
        )
        return prepared_instructions: "Keep doing this until 100% done or blocked:\n\n[instructions]"
     
     -> session_id_render: SessionId = HeadlessSession.executes_via_cursor_headless_api(
            instructions: prepared_instructions
        )
        return session_id_render: "session_render_555"
     
     -> loop_count_render: int = 0
     -> while True:
            -> api_response: Response = CursorHeadlessAPI.poll_session_status(
                   session_id: session_id_render
               )
               return api_response: {state: "completed", progress: "Rendered all markdown files"}
            
            -> logged: bool = SessionLog.appends_response(
                   response: api_response,
                   loop_number: loop_count_render + 1
               )
               return logged: True
            
            -> ai_status: SessionStatus = HeadlessSession.detects_completion_or_block()
               return ai_status: {state: "completed", done: True}
            
            if ai_status.done:
                break
            
            -> loop_count_render: int = loop_count_render + 1
            -> loop_instruction: str = Instructions.wraps_with_persistence_directive()
               return loop_instruction: "Keep doing this until 100% done or blocked:\n\n[instructions]"
            
            -> api_response: Response = CursorHeadlessAPI.send_instruction(
                   session_id: session_id_render,
                   instruction: loop_instruction
               )
               return api_response: {state: "running"}
     
     return render_result: {status: "completed", action: "render", total_loops: 1}

# Step 13: Detect render completion
  -> render_completion: bool = HeadlessSession.detects_action_completion(
         result: render_result
     )
     return render_completion: True

# Step 14: Report entire behavior completed successfully
  -> behavior_summary: BehaviorSummary = HeadlessSession.aggregates_behavior_results(
         clarify_result: clarify_result,
         strategy_result: strategy_result,
         build_result: build_result,
         validate_result: validate_result,
         render_result: render_result
     )
     return behavior_summary: {
         behavior: "shape",
         actions_completed: ["clarify", "strategy", "build", "validate", "render"],
         total_loops: 11,
         status: "completed"
     }
  
  -> outcome: str = HeadlessSession.reports_behavior_completion()
     -> console_output: str = format_behavior_outcome(
            summary: behavior_summary,
            log_path: log_path
        )
        return console_output: "✓ Complete behavior completed successfully\n  Behavior: shape\n  Actions: clarify (3 loops), strategy (2 loops), build (4 loops), validate (1 loop), render (1 loop)\n  Total loops: 11\n  Log: logs/headless-2025-12-29-16-00-00.log"
     
     print(console_output)
     return outcome: "success"

return result: {status: "completed", behavior: "shape", log_path: "logs/headless-2025-12-29-16-00-00.log", total_loops: 11}
```

---

## Model Updates During Walkthrough

### Required Changes to Domain Model:

1. **HeadlessSession** - Complete behavior execution entry point:
   - Public: `Invokes complete behavior with behavior name and context file: ExecutionResult, Behavior, ContextFile`
   - Internal: `executes_action_with_persistence_directive()`, `retrieves_action_instructions()`, `detects_action_completion()`, `aggregates_behavior_results()`, `reports_behavior_completion()`

2. **BehaviorSummary** - New concept for aggregating action results:
   - `Aggregates action results: BehaviorSummary, List[ActionResult]`
   - `Reports behavior completion: String, BehaviorSummary`

3. **Behavior** - Collaborator for action sequencing:
   - `Gets actions in sequence: List[Action]`

### Design Principle Applied:
**Encapsulation** - HeadlessSession owns the complete behavior execution flow including all actions and their looping. Caller provides behavior name and context file, receives result. All intermediate steps (action sequencing, looping, completion detection, aggregation) are internal implementation details.

## Coverage Summary

- ✓ Walk 1: Setup and clarify action execution (scenario steps 1-5)
- ✓ Walk 2: Strategy and build action execution (scenario steps 6-9)
- ✓ Walk 3: Validate and render action execution, final reporting (scenario steps 10-14)
- ✓ Single entry point: `HeadlessSession.invokes_complete_behavior(behavior, context_file)`
- ✓ All 14 scenario steps traced showing complete delegation chain including looping for each action
- ✓ Caller only sees: input (behavior, context_file) → output (result with behavior summary and total loops)
- ✓ Implementation details (steps 2-14) hidden behind HeadlessSession interface



**Scope:** Execute In Headless Mode.Execute In Headless Mode.Execute Complete Behavior.Execute complete behavior workflow in headless mode

**Story:** Human executes a complete behavior (clarify → strategy → build → validate → render) in headless mode with looping for each action until completion

## Scenario: Execute complete behavior workflow in headless mode

**Steps:**
- Given AI has written headless-context.md
- And headless mode is configured
- And user wants to execute shape behavior
- When human invokes CLI with --headless flag for complete behavior
- Then CLI executes clarify action with persistence directive
- And AI loops until clarify action indicates done
- And CLI detects clarify completion
- And CLI executes strategy action with persistence directive
- And AI loops until strategy action indicates done
- And CLI detects strategy completion
- And CLI executes build action with persistence directive
- And AI loops until build action indicates done
- And CLI detects build completion
- And CLI executes validate action with persistence directive
- And AI loops until validate action indicates done
- And CLI detects validate completion
- And CLI executes render action with persistence directive
- And AI loops until render action indicates done
- And CLI detects render completion
- And CLI reports entire behavior completed successfully

---

## Walk 1 - Covers: Steps 1-3 (Setup and clarify action execution)

### Realization:

```
# Step 1: Human invokes CLI with headless mode for complete behavior
result: ExecutionResult = HeadlessSession.invokes_complete_behavior(
    behavior: "shape",
    context_file: "headless-context.md"
)

# Step 2: Get configuration
  -> config: HeadlessConfig = HeadlessSession.get_configuration()
     return config: {api_key: "sk-...", log_dir: "logs/"}

# Step 3: Load execution context
  -> context: ExecutionContext = HeadlessSession.get_execution_context()
     -> context_loaded: ExecutionContext = ExecutionContext.loads_from_context_file(
            path: "headless-context.md"
        )
        return context_loaded: ExecutionContext
     return context: ExecutionContext

# Step 4: Execute clarify action with persistence directive
  -> clarify_result: ActionResult = HeadlessSession.executes_action_with_persistence_directive(
         behavior: "shape",
         action: "clarify",
         context: context
     )
     -> action_instructions: str = HeadlessSession.retrieves_action_instructions(
            behavior: "shape",
            action: "clarify"
        )
        return action_instructions: "Clarify requirements for story mapping..."
     
     -> prepared_instructions: str = HeadlessSession.prepares_instructions_with_persistence_directive(
            instructions: action_instructions,
            context: context
        )
        return prepared_instructions: "Keep doing this until 100% done or blocked:\n\n[instructions]"
     
     -> session_id_clarify: SessionId = HeadlessSession.executes_via_cursor_headless_api(
            instructions: prepared_instructions
        )
        return session_id_clarify: "session_clarify_111"
     
     -> loop_count_clarify: int = 0
     -> while True:
            -> api_response: Response = CursorHeadlessAPI.poll_session_status(
                   session_id: session_id_clarify
               )
               return api_response: {state: "running", progress: "..."}
            
            -> logged: bool = SessionLog.appends_response(
                   response: api_response,
                   loop_number: loop_count_clarify + 1
               )
               return logged: True
            
            -> ai_status: SessionStatus = HeadlessSession.detects_completion_or_block()
               return ai_status: {state: "running", done: False}
            
            if ai_status.done:
                break
            
            -> loop_count_clarify: int = loop_count_clarify + 1
            -> loop_instruction: str = Instructions.wraps_with_persistence_directive()
               return loop_instruction: "Keep doing this until 100% done or blocked:\n\n[instructions]"
            
            -> api_response: Response = CursorHeadlessAPI.send_instruction(
                   session_id: session_id_clarify,
                   instruction: loop_instruction
               )
               return api_response: {state: "running"}
     
     return clarify_result: {status: "completed", action: "clarify", total_loops: 3}

# Step 5: Detect clarify completion
  -> clarify_completion: bool = HeadlessSession.detects_action_completion(
         result: clarify_result
     )
     return clarify_completion: True
```

---

## Walk 2 - Covers: Steps 4-6 (Strategy and build action execution)

### Realization:

```
# Step 6: Execute strategy action with persistence directive
  -> strategy_result: ActionResult = HeadlessSession.executes_action_with_persistence_directive(
         behavior: "shape",
         action: "strategy",
         context: context
     )
     -> action_instructions: str = HeadlessSession.retrieves_action_instructions(
            behavior: "shape",
            action: "strategy"
        )
        return action_instructions: "Define strategy for story mapping approach..."
     
     -> prepared_instructions: str = HeadlessSession.prepares_instructions_with_persistence_directive(
            instructions: action_instructions,
            context: context
        )
        return prepared_instructions: "Keep doing this until 100% done or blocked:\n\n[instructions]"
     
     -> session_id_strategy: SessionId = HeadlessSession.executes_via_cursor_headless_api(
            instructions: prepared_instructions
        )
        return session_id_strategy: "session_strategy_222"
     
     -> loop_count_strategy: int = 0
     -> while True:
            -> api_response: Response = CursorHeadlessAPI.poll_session_status(
                   session_id: session_id_strategy
               )
               return api_response: {state: "running", progress: "..."}
            
            -> logged: bool = SessionLog.appends_response(
                   response: api_response,
                   loop_number: loop_count_strategy + 1
               )
               return logged: True
            
            -> ai_status: SessionStatus = HeadlessSession.detects_completion_or_block()
               return ai_status: {state: "running", done: False}
            
            if ai_status.done:
                break
            
            -> loop_count_strategy: int = loop_count_strategy + 1
            -> loop_instruction: str = Instructions.wraps_with_persistence_directive()
               return loop_instruction: "Keep doing this until 100% done or blocked:\n\n[instructions]"
            
            -> api_response: Response = CursorHeadlessAPI.send_instruction(
                   session_id: session_id_strategy,
                   instruction: loop_instruction
               )
               return api_response: {state: "running"}
     
     return strategy_result: {status: "completed", action: "strategy", total_loops: 2}

# Step 7: Detect strategy completion
  -> strategy_completion: bool = HeadlessSession.detects_action_completion(
         result: strategy_result
     )
     return strategy_completion: True

# Step 8: Execute build action with persistence directive
  -> build_result: ActionResult = HeadlessSession.executes_action_with_persistence_directive(
         behavior: "shape",
         action: "build",
         context: context
     )
     -> action_instructions: str = HeadlessSession.retrieves_action_instructions(
            behavior: "shape",
            action: "build"
        )
        return action_instructions: "Build knowledge graph for story map..."
     
     -> prepared_instructions: str = HeadlessSession.prepares_instructions_with_persistence_directive(
            instructions: action_instructions,
            context: context
        )
        return prepared_instructions: "Keep doing this until 100% done or blocked:\n\n[instructions]"
     
     -> session_id_build: SessionId = HeadlessSession.executes_via_cursor_headless_api(
            instructions: prepared_instructions
        )
        return session_id_build: "session_build_333"
     
     -> loop_count_build: int = 0
     -> while True:
            -> api_response: Response = CursorHeadlessAPI.poll_session_status(
                   session_id: session_id_build
               )
               return api_response: {state: "running", progress: "..."}
            
            -> logged: bool = SessionLog.appends_response(
                   response: api_response,
                   loop_number: loop_count_build + 1
               )
               return logged: True
            
            -> ai_status: SessionStatus = HeadlessSession.detects_completion_or_block()
               return ai_status: {state: "running", done: False}
            
            if ai_status.done:
                break
            
            -> loop_count_build: int = loop_count_build + 1
            -> loop_instruction: str = Instructions.wraps_with_persistence_directive()
               return loop_instruction: "Keep doing this until 100% done or blocked:\n\n[instructions]"
            
            -> api_response: Response = CursorHeadlessAPI.send_instruction(
                   session_id: session_id_build,
                   instruction: loop_instruction
               )
               return api_response: {state: "running"}
     
     return build_result: {status: "completed", action: "build", total_loops: 4}

# Step 9: Detect build completion
  -> build_completion: bool = HeadlessSession.detects_action_completion(
         result: build_result
     )
     return build_completion: True
```

---

## Walk 3 - Covers: Steps 7-9 (Validate and render action execution, final reporting)

### Realization:

```
# Step 10: Execute validate action with persistence directive
  -> validate_result: ActionResult = HeadlessSession.executes_action_with_persistence_directive(
         behavior: "shape",
         action: "validate",
         context: context
     )
     -> action_instructions: str = HeadlessSession.retrieves_action_instructions(
            behavior: "shape",
            action: "validate"
        )
        return action_instructions: "Validate knowledge graph against rules..."
     
     -> prepared_instructions: str = HeadlessSession.prepares_instructions_with_persistence_directive(
            instructions: action_instructions,
            context: context
        )
        return prepared_instructions: "Keep doing this until 100% done or blocked:\n\n[instructions]"
     
     -> session_id_validate: SessionId = HeadlessSession.executes_via_cursor_headless_api(
            instructions: prepared_instructions
        )
        return session_id_validate: "session_validate_444"
     
     -> loop_count_validate: int = 0
     -> while True:
            -> api_response: Response = CursorHeadlessAPI.poll_session_status(
                   session_id: session_id_validate
               )
               return api_response: {state: "running", progress: "..."}
            
            -> logged: bool = SessionLog.appends_response(
                   response: api_response,
                   loop_number: loop_count_validate + 1
               )
               return logged: True
            
            -> ai_status: SessionStatus = HeadlessSession.detects_completion_or_block()
               return ai_status: {state: "running", done: False}
            
            if ai_status.done:
                break
            
            -> loop_count_validate: int = loop_count_validate + 1
            -> loop_instruction: str = Instructions.wraps_with_persistence_directive()
               return loop_instruction: "Keep doing this until 100% done or blocked:\n\n[instructions]"
            
            -> api_response: Response = CursorHeadlessAPI.send_instruction(
                   session_id: session_id_validate,
                   instruction: loop_instruction
               )
               return api_response: {state: "running"}
     
     return validate_result: {status: "completed", action: "validate", total_loops: 1}

# Step 11: Detect validate completion
  -> validate_completion: bool = HeadlessSession.detects_action_completion(
         result: validate_result
     )
     return validate_completion: True

# Step 12: Execute render action with persistence directive
  -> render_result: ActionResult = HeadlessSession.executes_action_with_persistence_directive(
         behavior: "shape",
         action: "render",
         context: context
     )
     -> action_instructions: str = HeadlessSession.retrieves_action_instructions(
            behavior: "shape",
            action: "render"
        )
        return action_instructions: "Render knowledge graph to markdown..."
     
     -> prepared_instructions: str = HeadlessSession.prepares_instructions_with_persistence_directive(
            instructions: action_instructions,
            context: context
        )
        return prepared_instructions: "Keep doing this until 100% done or blocked:\n\n[instructions]"
     
     -> session_id_render: SessionId = HeadlessSession.executes_via_cursor_headless_api(
            instructions: prepared_instructions
        )
        return session_id_render: "session_render_555"
     
     -> loop_count_render: int = 0
     -> while True:
            -> api_response: Response = CursorHeadlessAPI.poll_session_status(
                   session_id: session_id_render
               )
               return api_response: {state: "completed", progress: "Rendered all markdown files"}
            
            -> logged: bool = SessionLog.appends_response(
                   response: api_response,
                   loop_number: loop_count_render + 1
               )
               return logged: True
            
            -> ai_status: SessionStatus = HeadlessSession.detects_completion_or_block()
               return ai_status: {state: "completed", done: True}
            
            if ai_status.done:
                break
            
            -> loop_count_render: int = loop_count_render + 1
            -> loop_instruction: str = Instructions.wraps_with_persistence_directive()
               return loop_instruction: "Keep doing this until 100% done or blocked:\n\n[instructions]"
            
            -> api_response: Response = CursorHeadlessAPI.send_instruction(
                   session_id: session_id_render,
                   instruction: loop_instruction
               )
               return api_response: {state: "running"}
     
     return render_result: {status: "completed", action: "render", total_loops: 1}

# Step 13: Detect render completion
  -> render_completion: bool = HeadlessSession.detects_action_completion(
         result: render_result
     )
     return render_completion: True

# Step 14: Report entire behavior completed successfully
  -> behavior_summary: BehaviorSummary = HeadlessSession.aggregates_behavior_results(
         clarify_result: clarify_result,
         strategy_result: strategy_result,
         build_result: build_result,
         validate_result: validate_result,
         render_result: render_result
     )
     return behavior_summary: {
         behavior: "shape",
         actions_completed: ["clarify", "strategy", "build", "validate", "render"],
         total_loops: 11,
         status: "completed"
     }
  
  -> outcome: str = HeadlessSession.reports_behavior_completion()
     -> console_output: str = format_behavior_outcome(
            summary: behavior_summary,
            log_path: log_path
        )
        return console_output: "✓ Complete behavior completed successfully\n  Behavior: shape\n  Actions: clarify (3 loops), strategy (2 loops), build (4 loops), validate (1 loop), render (1 loop)\n  Total loops: 11\n  Log: logs/headless-2025-12-29-16-00-00.log"
     
     print(console_output)
     return outcome: "success"

return result: {status: "completed", behavior: "shape", log_path: "logs/headless-2025-12-29-16-00-00.log", total_loops: 11}
```

---

## Model Updates During Walkthrough

### Required Changes to Domain Model:

1. **HeadlessSession** - Complete behavior execution entry point:
   - Public: `Invokes complete behavior with behavior name and context file: ExecutionResult, Behavior, ContextFile`
   - Internal: `executes_action_with_persistence_directive()`, `retrieves_action_instructions()`, `detects_action_completion()`, `aggregates_behavior_results()`, `reports_behavior_completion()`

2. **BehaviorSummary** - New concept for aggregating action results:
   - `Aggregates action results: BehaviorSummary, List[ActionResult]`
   - `Reports behavior completion: String, BehaviorSummary`

3. **Behavior** - Collaborator for action sequencing:
   - `Gets actions in sequence: List[Action]`

### Design Principle Applied:
**Encapsulation** - HeadlessSession owns the complete behavior execution flow including all actions and their looping. Caller provides behavior name and context file, receives result. All intermediate steps (action sequencing, looping, completion detection, aggregation) are internal implementation details.

## Coverage Summary

- ✓ Walk 1: Setup and clarify action execution (scenario steps 1-5)
- ✓ Walk 2: Strategy and build action execution (scenario steps 6-9)
- ✓ Walk 3: Validate and render action execution, final reporting (scenario steps 10-14)
- ✓ Single entry point: `HeadlessSession.invokes_complete_behavior(behavior, context_file)`
- ✓ All 14 scenario steps traced showing complete delegation chain including looping for each action
- ✓ Caller only sees: input (behavior, context_file) → output (result with behavior summary and total loops)
- ✓ Implementation details (steps 2-14) hidden behind HeadlessSession interface

