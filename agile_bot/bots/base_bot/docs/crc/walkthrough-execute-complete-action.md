# Walkthrough: Execute Complete Action In Headless Mode

**Scope:** Execute In Headless Mode.Execute In Headless Mode.Execute Complete Action.Execute complete action workflow in headless mode

**Story:** Human executes a complete action (instructions → submit → confirm) in headless mode with looping for each operation until completion

## Scenario: Execute complete action workflow in headless mode

**Steps:**
- Given AI has written headless-context.md
- And headless mode is configured
- And user is at shape.build action
- When human invokes CLI with --headless flag for complete action
- Then CLI executes instructions operation with persistence directive
- And AI loops until instructions operation indicates done
- And CLI detects instructions completion
- And CLI executes submit operation with persistence directive
- And AI loops until submit operation indicates done
- And CLI detects submit completion
- And CLI executes confirm operation with persistence directive
- And AI completes confirmation and indicates done
- And CLI detects confirm completion
- And CLI reports entire action completed successfully

---

## Walk 1 - Covers: Steps 1-3 (Setup and instructions operation execution)

### Realization:

```
# Step 1: Human invokes CLI with headless mode for complete action
result: ExecutionResult = HeadlessSession.invokes_complete_action(
    behavior: "shape",
    action: "build",
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

# Step 4: Execute instructions operation with persistence directive
  -> instructions_result: OperationResult = HeadlessSession.executes_operation_with_persistence_directive(
         operation: "instructions",
         behavior: "shape",
         action: "build",
         context: context
     )
     -> operation_instructions: str = HeadlessSession.retrieves_operation_instructions(
            behavior: "shape",
            action: "build",
            operation: "instructions"
        )
        return operation_instructions: "Build knowledge graph..."
     
     -> prepared_instructions: str = HeadlessSession.prepares_instructions_with_persistence_directive(
            instructions: operation_instructions,
            context: context
        )
        return prepared_instructions: "Keep doing this until 100% done or blocked:\n\n[instructions]"
     
     -> session_id_1: SessionId = HeadlessSession.executes_via_cursor_headless_api(
            instructions: prepared_instructions
        )
        return session_id_1: "session_instructions_123"
     
     -> loop_count_1: int = 0
     -> while True:
            -> api_response: Response = CursorHeadlessAPI.poll_session_status(
                   session_id: session_id_1
               )
               return api_response: {state: "running", progress: "..."}
            
            -> logged: bool = SessionLog.appends_response(
                   response: api_response,
                   loop_number: loop_count_1 + 1
               )
               return logged: True
            
            -> ai_status: SessionStatus = HeadlessSession.detects_completion_or_block()
               return ai_status: {state: "running", done: False}
            
            if ai_status.done:
                break
            
            -> loop_count_1: int = loop_count_1 + 1
            -> loop_instruction: str = Instructions.wraps_with_persistence_directive()
               return loop_instruction: "Keep doing this until 100% done or blocked:\n\n[instructions]"
            
            -> api_response: Response = CursorHeadlessAPI.send_instruction(
                   session_id: session_id_1,
                   instruction: loop_instruction
               )
               return api_response: {state: "running"}
     
     return instructions_result: {status: "completed", operation: "instructions", total_loops: 2}
```

---

## Walk 2 - Covers: Steps 4-5 (Submit operation execution)

### Realization:

```
# Step 5: Detect instructions completion
  -> instructions_completion: bool = HeadlessSession.detects_operation_completion(
         result: instructions_result
     )
     return instructions_completion: True

# Step 6: Execute submit operation with persistence directive
  -> submit_result: OperationResult = HeadlessSession.executes_operation_with_persistence_directive(
         operation: "submit",
         behavior: "shape",
         action: "build",
         context: context
     )
     -> operation_instructions: str = HeadlessSession.retrieves_operation_instructions(
            behavior: "shape",
            action: "build",
            operation: "submit"
        )
        return operation_instructions: "Save knowledge graph to story-graph.json..."
     
     -> prepared_instructions: str = HeadlessSession.prepares_instructions_with_persistence_directive(
            instructions: operation_instructions,
            context: context
        )
        return prepared_instructions: "Keep doing this until 100% done or blocked:\n\n[instructions]"
     
     -> session_id_2: SessionId = HeadlessSession.executes_via_cursor_headless_api(
            instructions: prepared_instructions
        )
        return session_id_2: "session_submit_456"
     
     -> loop_count_2: int = 0
     -> while True:
            -> api_response: Response = CursorHeadlessAPI.poll_session_status(
                   session_id: session_id_2
               )
               return api_response: {state: "running", progress: "..."}
            
            -> logged: bool = SessionLog.appends_response(
                   response: api_response,
                   loop_number: loop_count_2 + 1
               )
               return logged: True
            
            -> ai_status: SessionStatus = HeadlessSession.detects_completion_or_block()
               return ai_status: {state: "running", done: False}
            
            if ai_status.done:
                break
            
            -> loop_count_2: int = loop_count_2 + 1
            -> loop_instruction: str = Instructions.wraps_with_persistence_directive()
               return loop_instruction: "Keep doing this until 100% done or blocked:\n\n[instructions]"
            
            -> api_response: Response = CursorHeadlessAPI.send_instruction(
                   session_id: session_id_2,
                   instruction: loop_instruction
               )
               return api_response: {state: "running"}
     
     return submit_result: {status: "completed", operation: "submit", total_loops: 1}

# Step 7: Detect submit completion
  -> submit_completion: bool = HeadlessSession.detects_operation_completion(
         result: submit_result
     )
     return submit_completion: True
```

---

## Walk 3 - Covers: Steps 6-7 (Confirm operation execution and final reporting)

### Realization:

```
# Step 8: Execute confirm operation with persistence directive
  -> confirm_result: OperationResult = HeadlessSession.executes_operation_with_persistence_directive(
         operation: "confirm",
         behavior: "shape",
         action: "build",
         context: context
     )
     -> operation_instructions: str = HeadlessSession.retrieves_operation_instructions(
            behavior: "shape",
            action: "build",
            operation: "confirm"
        )
        return operation_instructions: "Confirm action completion and move to next..."
     
     -> prepared_instructions: str = HeadlessSession.prepares_instructions_with_persistence_directive(
            instructions: operation_instructions,
            context: context
        )
        return prepared_instructions: "Keep doing this until 100% done or blocked:\n\n[instructions]"
     
     -> session_id_3: SessionId = HeadlessSession.executes_via_cursor_headless_api(
            instructions: prepared_instructions
        )
        return session_id_3: "session_confirm_789"
     
     -> loop_count_3: int = 0
     -> while True:
            -> api_response: Response = CursorHeadlessAPI.poll_session_status(
                   session_id: session_id_3
               )
               return api_response: {state: "completed", progress: "Action confirmed, moving to next"}
            
            -> logged: bool = SessionLog.appends_response(
                   response: api_response,
                   loop_number: loop_count_3 + 1
               )
               return logged: True
            
            -> ai_status: SessionStatus = HeadlessSession.detects_completion_or_block()
               return ai_status: {state: "completed", done: True}
            
            if ai_status.done:
                break
            
            -> loop_count_3: int = loop_count_3 + 1
            -> loop_instruction: str = Instructions.wraps_with_persistence_directive()
               return loop_instruction: "Keep doing this until 100% done or blocked:\n\n[instructions]"
            
            -> api_response: Response = CursorHeadlessAPI.send_instruction(
                   session_id: session_id_3,
                   instruction: loop_instruction
               )
               return api_response: {state: "running"}
     
     return confirm_result: {status: "completed", operation: "confirm", total_loops: 1}

# Step 9: Detect confirm completion
  -> confirm_completion: bool = HeadlessSession.detects_operation_completion(
         result: confirm_result
     )
     return confirm_completion: True

# Step 10: Report entire action completed successfully
  -> action_summary: ActionSummary = HeadlessSession.aggregates_action_results(
         instructions_result: instructions_result,
         submit_result: submit_result,
         confirm_result: confirm_result
     )
     return action_summary: {
         action: "shape.build",
         operations_completed: ["instructions", "submit", "confirm"],
         total_loops: 4,
         status: "completed"
     }
  
  -> outcome: str = HeadlessSession.reports_action_completion()
     -> console_output: str = format_action_outcome(
            summary: action_summary,
            log_path: log_path
        )
        return console_output: "✓ Complete action completed successfully\n  Action: shape.build\n  Operations: instructions (2 loops), submit (1 loop), confirm (1 loop)\n  Total loops: 4\n  Log: logs/headless-2025-12-29-15-00-00.log"
     
     print(console_output)
     return outcome: "success"

return result: {status: "completed", action: "shape.build", log_path: "logs/headless-2025-12-29-15-00-00.log", total_loops: 4}
```

---

## Model Updates During Walkthrough

### Required Changes to Domain Model:

1. **HeadlessSession** - Complete action execution entry point:
   - Public: `Invokes complete action with behavior, action, and context file: ExecutionResult, Behavior, Action, ContextFile`
   - Internal: `executes_operation_with_persistence_directive()`, `detects_operation_completion()`, `aggregates_action_results()`, `reports_action_completion()`

2. **ActionSummary** - New concept for aggregating operation results:
   - `Aggregates operation results: ActionSummary, List[OperationResult]`
   - `Reports action completion: String, ActionSummary`

### Design Principle Applied:
**Encapsulation** - HeadlessSession owns the complete action execution flow including all operations and their looping. Caller provides behavior, action, and context file, receives result. All intermediate steps (operation sequencing, looping, completion detection, aggregation) are internal implementation details.

## Coverage Summary

- ✓ Walk 1: Setup and instructions operation execution (scenario steps 1-4)
- ✓ Walk 2: Submit operation execution (scenario steps 5-6)
- ✓ Walk 3: Confirm operation execution and final reporting (scenario steps 7-10)
- ✓ Single entry point: `HeadlessSession.invokes_complete_action(behavior, action, context_file)`
- ✓ All 10 scenario steps traced showing complete delegation chain including looping for each operation
- ✓ Caller only sees: input (behavior, action, context_file) → output (result with action summary and total loops)
- ✓ Implementation details (steps 2-10) hidden behind HeadlessSession interface



**Scope:** Execute In Headless Mode.Execute In Headless Mode.Execute Complete Action.Execute complete action workflow in headless mode

**Story:** Human executes a complete action (instructions → submit → confirm) in headless mode with looping for each operation until completion

## Scenario: Execute complete action workflow in headless mode

**Steps:**
- Given AI has written headless-context.md
- And headless mode is configured
- And user is at shape.build action
- When human invokes CLI with --headless flag for complete action
- Then CLI executes instructions operation with persistence directive
- And AI loops until instructions operation indicates done
- And CLI detects instructions completion
- And CLI executes submit operation with persistence directive
- And AI loops until submit operation indicates done
- And CLI detects submit completion
- And CLI executes confirm operation with persistence directive
- And AI completes confirmation and indicates done
- And CLI detects confirm completion
- And CLI reports entire action completed successfully

---

## Walk 1 - Covers: Steps 1-3 (Setup and instructions operation execution)

### Realization:

```
# Step 1: Human invokes CLI with headless mode for complete action
result: ExecutionResult = HeadlessSession.invokes_complete_action(
    behavior: "shape",
    action: "build",
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

# Step 4: Execute instructions operation with persistence directive
  -> instructions_result: OperationResult = HeadlessSession.executes_operation_with_persistence_directive(
         operation: "instructions",
         behavior: "shape",
         action: "build",
         context: context
     )
     -> operation_instructions: str = HeadlessSession.retrieves_operation_instructions(
            behavior: "shape",
            action: "build",
            operation: "instructions"
        )
        return operation_instructions: "Build knowledge graph..."
     
     -> prepared_instructions: str = HeadlessSession.prepares_instructions_with_persistence_directive(
            instructions: operation_instructions,
            context: context
        )
        return prepared_instructions: "Keep doing this until 100% done or blocked:\n\n[instructions]"
     
     -> session_id_1: SessionId = HeadlessSession.executes_via_cursor_headless_api(
            instructions: prepared_instructions
        )
        return session_id_1: "session_instructions_123"
     
     -> loop_count_1: int = 0
     -> while True:
            -> api_response: Response = CursorHeadlessAPI.poll_session_status(
                   session_id: session_id_1
               )
               return api_response: {state: "running", progress: "..."}
            
            -> logged: bool = SessionLog.appends_response(
                   response: api_response,
                   loop_number: loop_count_1 + 1
               )
               return logged: True
            
            -> ai_status: SessionStatus = HeadlessSession.detects_completion_or_block()
               return ai_status: {state: "running", done: False}
            
            if ai_status.done:
                break
            
            -> loop_count_1: int = loop_count_1 + 1
            -> loop_instruction: str = Instructions.wraps_with_persistence_directive()
               return loop_instruction: "Keep doing this until 100% done or blocked:\n\n[instructions]"
            
            -> api_response: Response = CursorHeadlessAPI.send_instruction(
                   session_id: session_id_1,
                   instruction: loop_instruction
               )
               return api_response: {state: "running"}
     
     return instructions_result: {status: "completed", operation: "instructions", total_loops: 2}
```

---

## Walk 2 - Covers: Steps 4-5 (Submit operation execution)

### Realization:

```
# Step 5: Detect instructions completion
  -> instructions_completion: bool = HeadlessSession.detects_operation_completion(
         result: instructions_result
     )
     return instructions_completion: True

# Step 6: Execute submit operation with persistence directive
  -> submit_result: OperationResult = HeadlessSession.executes_operation_with_persistence_directive(
         operation: "submit",
         behavior: "shape",
         action: "build",
         context: context
     )
     -> operation_instructions: str = HeadlessSession.retrieves_operation_instructions(
            behavior: "shape",
            action: "build",
            operation: "submit"
        )
        return operation_instructions: "Save knowledge graph to story-graph.json..."
     
     -> prepared_instructions: str = HeadlessSession.prepares_instructions_with_persistence_directive(
            instructions: operation_instructions,
            context: context
        )
        return prepared_instructions: "Keep doing this until 100% done or blocked:\n\n[instructions]"
     
     -> session_id_2: SessionId = HeadlessSession.executes_via_cursor_headless_api(
            instructions: prepared_instructions
        )
        return session_id_2: "session_submit_456"
     
     -> loop_count_2: int = 0
     -> while True:
            -> api_response: Response = CursorHeadlessAPI.poll_session_status(
                   session_id: session_id_2
               )
               return api_response: {state: "running", progress: "..."}
            
            -> logged: bool = SessionLog.appends_response(
                   response: api_response,
                   loop_number: loop_count_2 + 1
               )
               return logged: True
            
            -> ai_status: SessionStatus = HeadlessSession.detects_completion_or_block()
               return ai_status: {state: "running", done: False}
            
            if ai_status.done:
                break
            
            -> loop_count_2: int = loop_count_2 + 1
            -> loop_instruction: str = Instructions.wraps_with_persistence_directive()
               return loop_instruction: "Keep doing this until 100% done or blocked:\n\n[instructions]"
            
            -> api_response: Response = CursorHeadlessAPI.send_instruction(
                   session_id: session_id_2,
                   instruction: loop_instruction
               )
               return api_response: {state: "running"}
     
     return submit_result: {status: "completed", operation: "submit", total_loops: 1}

# Step 7: Detect submit completion
  -> submit_completion: bool = HeadlessSession.detects_operation_completion(
         result: submit_result
     )
     return submit_completion: True
```

---

## Walk 3 - Covers: Steps 6-7 (Confirm operation execution and final reporting)

### Realization:

```
# Step 8: Execute confirm operation with persistence directive
  -> confirm_result: OperationResult = HeadlessSession.executes_operation_with_persistence_directive(
         operation: "confirm",
         behavior: "shape",
         action: "build",
         context: context
     )
     -> operation_instructions: str = HeadlessSession.retrieves_operation_instructions(
            behavior: "shape",
            action: "build",
            operation: "confirm"
        )
        return operation_instructions: "Confirm action completion and move to next..."
     
     -> prepared_instructions: str = HeadlessSession.prepares_instructions_with_persistence_directive(
            instructions: operation_instructions,
            context: context
        )
        return prepared_instructions: "Keep doing this until 100% done or blocked:\n\n[instructions]"
     
     -> session_id_3: SessionId = HeadlessSession.executes_via_cursor_headless_api(
            instructions: prepared_instructions
        )
        return session_id_3: "session_confirm_789"
     
     -> loop_count_3: int = 0
     -> while True:
            -> api_response: Response = CursorHeadlessAPI.poll_session_status(
                   session_id: session_id_3
               )
               return api_response: {state: "completed", progress: "Action confirmed, moving to next"}
            
            -> logged: bool = SessionLog.appends_response(
                   response: api_response,
                   loop_number: loop_count_3 + 1
               )
               return logged: True
            
            -> ai_status: SessionStatus = HeadlessSession.detects_completion_or_block()
               return ai_status: {state: "completed", done: True}
            
            if ai_status.done:
                break
            
            -> loop_count_3: int = loop_count_3 + 1
            -> loop_instruction: str = Instructions.wraps_with_persistence_directive()
               return loop_instruction: "Keep doing this until 100% done or blocked:\n\n[instructions]"
            
            -> api_response: Response = CursorHeadlessAPI.send_instruction(
                   session_id: session_id_3,
                   instruction: loop_instruction
               )
               return api_response: {state: "running"}
     
     return confirm_result: {status: "completed", operation: "confirm", total_loops: 1}

# Step 9: Detect confirm completion
  -> confirm_completion: bool = HeadlessSession.detects_operation_completion(
         result: confirm_result
     )
     return confirm_completion: True

# Step 10: Report entire action completed successfully
  -> action_summary: ActionSummary = HeadlessSession.aggregates_action_results(
         instructions_result: instructions_result,
         submit_result: submit_result,
         confirm_result: confirm_result
     )
     return action_summary: {
         action: "shape.build",
         operations_completed: ["instructions", "submit", "confirm"],
         total_loops: 4,
         status: "completed"
     }
  
  -> outcome: str = HeadlessSession.reports_action_completion()
     -> console_output: str = format_action_outcome(
            summary: action_summary,
            log_path: log_path
        )
        return console_output: "✓ Complete action completed successfully\n  Action: shape.build\n  Operations: instructions (2 loops), submit (1 loop), confirm (1 loop)\n  Total loops: 4\n  Log: logs/headless-2025-12-29-15-00-00.log"
     
     print(console_output)
     return outcome: "success"

return result: {status: "completed", action: "shape.build", log_path: "logs/headless-2025-12-29-15-00-00.log", total_loops: 4}
```

---

## Model Updates During Walkthrough

### Required Changes to Domain Model:

1. **HeadlessSession** - Complete action execution entry point:
   - Public: `Invokes complete action with behavior, action, and context file: ExecutionResult, Behavior, Action, ContextFile`
   - Internal: `executes_operation_with_persistence_directive()`, `detects_operation_completion()`, `aggregates_action_results()`, `reports_action_completion()`

2. **ActionSummary** - New concept for aggregating operation results:
   - `Aggregates operation results: ActionSummary, List[OperationResult]`
   - `Reports action completion: String, ActionSummary`

### Design Principle Applied:
**Encapsulation** - HeadlessSession owns the complete action execution flow including all operations and their looping. Caller provides behavior, action, and context file, receives result. All intermediate steps (operation sequencing, looping, completion detection, aggregation) are internal implementation details.

## Coverage Summary

- ✓ Walk 1: Setup and instructions operation execution (scenario steps 1-4)
- ✓ Walk 2: Submit operation execution (scenario steps 5-6)
- ✓ Walk 3: Confirm operation execution and final reporting (scenario steps 7-10)
- ✓ Single entry point: `HeadlessSession.invokes_complete_action(behavior, action, context_file)`
- ✓ All 10 scenario steps traced showing complete delegation chain including looping for each operation
- ✓ Caller only sees: input (behavior, action, context_file) → output (result with action summary and total loops)
- ✓ Implementation details (steps 2-10) hidden behind HeadlessSession interface

