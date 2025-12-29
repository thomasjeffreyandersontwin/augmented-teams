# Walkthrough: Execute Single Operation In Headless Mode

**Scope:** Execute In Headless Mode.Execute In Headless Mode.Execute Single Operation.Execute instructions operation in headless mode

**Story:** Human executes a single operation (instructions, submit, or confirm) in headless mode with looping until completion

## Scenario: Execute instructions operation in headless mode

**Steps:**
- Given AI has written headless-context.md
- And headless mode is configured
- And user is at shape.build action
- When human invokes CLI with --headless flag for instructions operation
- Then CLI retrieves instructions for shape.build.instructions
- And CLI prepends headless-context.md content to instructions
- And CLI wraps with Keep doing this until 100% done or blocked directive
- And CLI sends to Cursor Headless API
- And AI executes instruction and indicates not done
- And CLI appends AI response to log file
- And CLI loops instruction again with persistence directive
- And AI executes instruction and indicates completion
- And CLI appends AI response to log file
- And CLI detects AI completion signal
- And CLI stops looping
- And CLI reports operation completion with log path

---

## Walk 1 - Covers: Steps 1-4 (CLI invocation through instruction retrieval and preparation)

### Realization:

```
# Step 1: Human invokes CLI with headless mode for instructions operation
result: ExecutionResult = HeadlessSession.invokes_operation(
    behavior: "shape",
    action: "build",
    operation: "instructions",
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

# Step 4: Retrieve instructions for operation
  -> operation_instructions: str = HeadlessSession.retrieves_operation_instructions()
     -> behavior_obj: Behavior = Behavior.find(name: "shape")
        return behavior_obj: <Behavior shape>
     
     -> action_obj: Action = behavior_obj.get_action(name: "build")
        return action_obj: <Action build>
     
     -> instructions_text: str = action_obj.get_instructions(operation: "instructions")
        return instructions_text: "Build knowledge graph for story map...\n\n1. Read story-graph.json...\n2. Generate nodes..."
     
     return operation_instructions: instructions_text

# Step 5: Prepare instructions with context and directive
  -> prepared_instructions: Instructions = HeadlessSession.prepares_instructions_with_persistence_directive()
     -> with_context: str = Instructions.prepends_context(
            instructions: operation_instructions,
            context: context
        )
        return with_context: "[context content]\n\nBuild knowledge graph for story map..."
     
     -> with_directive: str = Instructions.wraps_with_persistence_directive(
            instructions: with_context
        )
        return with_directive: "Keep doing this until 100% done or blocked:\n\n[instructions]"
     
     return prepared_instructions: with_directive
```

---

## Walk 2 - Covers: Steps 5-9 (API execution, looping, and logging)

### Realization:

```
# Step 6: Execute via Cursor Headless API
  -> response: Response = HeadlessSession.executes_via_cursor_headless_api()
     -> api: CursorHeadlessAPI = CursorHeadlessAPI.connect(
            api_key: config.api_key
        )
        return api: CursorHeadlessAPI(connected: True)
     
     -> session_id: SessionId = api.start_session(
            instructions: prepared_instructions
        )
        return session_id: "session_xyz789"
     
     return response: Response

# Step 7: Create session log
  -> log: SessionLog = HeadlessSession.get_session_log()
     -> log_path: Path = SessionLog.creates_with_timestamped_path(
            base_dir: "logs/"
        )
        return log_path: "logs/headless-2025-12-29-14-30-15.log"
     return log: SessionLog

# Step 8: Loop iteration 1 - AI indicates not done
  -> loop_count: int = 1
  -> api_response_1: Response = api.poll_session_status(
         session_id: session_id
     )
     return api_response_1: {state: "running", progress: "Reading story-graph.json and analyzing structure"}
  
  -> logged_1: bool = SessionLog.appends_response(
         response: api_response_1,
         loop_number: loop_count
     )
     return logged_1: True
  
  -> ai_status_1: SessionStatus = HeadlessSession.detects_completion_or_block()
     return ai_status_1: {state: "running", done: False}
  
  -> loop_instruction_1: str = Instructions.wraps_with_persistence_directive()
     return loop_instruction_1: "Keep doing this until 100% done or blocked:\n\n[instructions]"
  
  -> api_response_2: Response = api.send_instruction(
         session_id: session_id,
         instruction: loop_instruction_1
     )
     return api_response_2: {state: "running"}

# Step 9: Loop iteration 2 - AI indicates completion
  -> loop_count: int = 2
  -> api_response_2: Response = api.poll_session_status(
         session_id: session_id
     )
     return api_response_2: {state: "completed", progress: "Generated all nodes and relationships, knowledge graph complete"}
  
  -> logged_2: bool = SessionLog.appends_response(
         response: api_response_2,
         loop_number: loop_count
     )
     return logged_2: True
  
  -> ai_status_2: SessionStatus = HeadlessSession.detects_completion_or_block()
     return ai_status_2: {state: "completed", done: True}
  
  -> total_loops: int = 2
  -> loop_summary: str = SessionLog.appends_total_loops(
         count: total_loops
     )
     return loop_summary: "Total loops: 2"
```

---

## Walk 3 - Covers: Steps 10-11 (Completion detection and reporting)

### Realization:

```
# Step 10: Detect completion and stop looping
  -> completion_detected: bool = HeadlessSession.detects_completion_signal(
         status: ai_status_2
     )
     return completion_detected: True
  
  -> loop_stopped: bool = HeadlessSession.stops_looping()
     return loop_stopped: True

# Step 11: Report operation completion
  -> transcript: str = SessionLog.get_transcript()
     return transcript: "Session xyz789:\n  Loop 1: Reading story-graph.json and analyzing structure\n  Loop 2: Generated all nodes and relationships, knowledge graph complete\n  Total loops: 2"
  
  -> outcome: str = HeadlessSession.reports_operation_completion()
     -> console_output: str = format_operation_outcome(
            operation: "instructions",
            status: ai_status_2,
            transcript: transcript,
            log_path: log_path
        )
        return console_output: "✓ Instructions operation completed\n  Operation: shape.build.instructions\n  Log: logs/headless-2025-12-29-14-30-15.log"
     
     print(console_output)
     return outcome: "success"

return result: {status: "completed", operation: "instructions", log_path: "logs/headless-2025-12-29-14-30-15.log", total_loops: 2}
```

---

## Model Updates During Walkthrough

### Required Changes to Domain Model:

1. **HeadlessSession** - Operation execution entry point:
   - Public: `Invokes operation with behavior, action, operation, and context file: ExecutionResult, Behavior, Action, Operation, ContextFile`
   - Internal: `retrieves_operation_instructions()`, `executes_via_cursor_headless_api()`, `detects_completion_or_block()`, `stops_looping()`, `reports_operation_completion()`

2. **Behavior** - Collaborator for instruction retrieval:
   - `Gets action by name: Action, String`

3. **Action** - Collaborator for operation instructions:
   - `Gets instructions for operation: String, Operation`

### Design Principle Applied:
**Encapsulation** - HeadlessSession owns the complete operation execution flow including looping. Caller provides behavior, action, operation, and context file, receives result. All intermediate steps (context loading, instruction retrieval, preparation, API execution, looping, monitoring, logging) are internal implementation details.

## Coverage Summary

- ✓ Walk 1: CLI invocation through instruction retrieval and preparation (scenario steps 1-5)
- ✓ Walk 2: API execution, looping, and logging (scenario steps 6-9)
- ✓ Walk 3: Completion detection and reporting (scenario steps 10-11)
- ✓ Single entry point: `HeadlessSession.invokes_operation(behavior, action, operation, context_file)`
- ✓ All 11 scenario steps traced showing complete delegation chain including looping
- ✓ Caller only sees: input (behavior, action, operation, context_file) → output (result with operation and loop count)
- ✓ Implementation details (steps 2-11) hidden behind HeadlessSession interface



**Scope:** Execute In Headless Mode.Execute In Headless Mode.Execute Single Operation.Execute instructions operation in headless mode

**Story:** Human executes a single operation (instructions, submit, or confirm) in headless mode with looping until completion

## Scenario: Execute instructions operation in headless mode

**Steps:**
- Given AI has written headless-context.md
- And headless mode is configured
- And user is at shape.build action
- When human invokes CLI with --headless flag for instructions operation
- Then CLI retrieves instructions for shape.build.instructions
- And CLI prepends headless-context.md content to instructions
- And CLI wraps with Keep doing this until 100% done or blocked directive
- And CLI sends to Cursor Headless API
- And AI executes instruction and indicates not done
- And CLI appends AI response to log file
- And CLI loops instruction again with persistence directive
- And AI executes instruction and indicates completion
- And CLI appends AI response to log file
- And CLI detects AI completion signal
- And CLI stops looping
- And CLI reports operation completion with log path

---

## Walk 1 - Covers: Steps 1-4 (CLI invocation through instruction retrieval and preparation)

### Realization:

```
# Step 1: Human invokes CLI with headless mode for instructions operation
result: ExecutionResult = HeadlessSession.invokes_operation(
    behavior: "shape",
    action: "build",
    operation: "instructions",
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

# Step 4: Retrieve instructions for operation
  -> operation_instructions: str = HeadlessSession.retrieves_operation_instructions()
     -> behavior_obj: Behavior = Behavior.find(name: "shape")
        return behavior_obj: <Behavior shape>
     
     -> action_obj: Action = behavior_obj.get_action(name: "build")
        return action_obj: <Action build>
     
     -> instructions_text: str = action_obj.get_instructions(operation: "instructions")
        return instructions_text: "Build knowledge graph for story map...\n\n1. Read story-graph.json...\n2. Generate nodes..."
     
     return operation_instructions: instructions_text

# Step 5: Prepare instructions with context and directive
  -> prepared_instructions: Instructions = HeadlessSession.prepares_instructions_with_persistence_directive()
     -> with_context: str = Instructions.prepends_context(
            instructions: operation_instructions,
            context: context
        )
        return with_context: "[context content]\n\nBuild knowledge graph for story map..."
     
     -> with_directive: str = Instructions.wraps_with_persistence_directive(
            instructions: with_context
        )
        return with_directive: "Keep doing this until 100% done or blocked:\n\n[instructions]"
     
     return prepared_instructions: with_directive
```

---

## Walk 2 - Covers: Steps 5-9 (API execution, looping, and logging)

### Realization:

```
# Step 6: Execute via Cursor Headless API
  -> response: Response = HeadlessSession.executes_via_cursor_headless_api()
     -> api: CursorHeadlessAPI = CursorHeadlessAPI.connect(
            api_key: config.api_key
        )
        return api: CursorHeadlessAPI(connected: True)
     
     -> session_id: SessionId = api.start_session(
            instructions: prepared_instructions
        )
        return session_id: "session_xyz789"
     
     return response: Response

# Step 7: Create session log
  -> log: SessionLog = HeadlessSession.get_session_log()
     -> log_path: Path = SessionLog.creates_with_timestamped_path(
            base_dir: "logs/"
        )
        return log_path: "logs/headless-2025-12-29-14-30-15.log"
     return log: SessionLog

# Step 8: Loop iteration 1 - AI indicates not done
  -> loop_count: int = 1
  -> api_response_1: Response = api.poll_session_status(
         session_id: session_id
     )
     return api_response_1: {state: "running", progress: "Reading story-graph.json and analyzing structure"}
  
  -> logged_1: bool = SessionLog.appends_response(
         response: api_response_1,
         loop_number: loop_count
     )
     return logged_1: True
  
  -> ai_status_1: SessionStatus = HeadlessSession.detects_completion_or_block()
     return ai_status_1: {state: "running", done: False}
  
  -> loop_instruction_1: str = Instructions.wraps_with_persistence_directive()
     return loop_instruction_1: "Keep doing this until 100% done or blocked:\n\n[instructions]"
  
  -> api_response_2: Response = api.send_instruction(
         session_id: session_id,
         instruction: loop_instruction_1
     )
     return api_response_2: {state: "running"}

# Step 9: Loop iteration 2 - AI indicates completion
  -> loop_count: int = 2
  -> api_response_2: Response = api.poll_session_status(
         session_id: session_id
     )
     return api_response_2: {state: "completed", progress: "Generated all nodes and relationships, knowledge graph complete"}
  
  -> logged_2: bool = SessionLog.appends_response(
         response: api_response_2,
         loop_number: loop_count
     )
     return logged_2: True
  
  -> ai_status_2: SessionStatus = HeadlessSession.detects_completion_or_block()
     return ai_status_2: {state: "completed", done: True}
  
  -> total_loops: int = 2
  -> loop_summary: str = SessionLog.appends_total_loops(
         count: total_loops
     )
     return loop_summary: "Total loops: 2"
```

---

## Walk 3 - Covers: Steps 10-11 (Completion detection and reporting)

### Realization:

```
# Step 10: Detect completion and stop looping
  -> completion_detected: bool = HeadlessSession.detects_completion_signal(
         status: ai_status_2
     )
     return completion_detected: True
  
  -> loop_stopped: bool = HeadlessSession.stops_looping()
     return loop_stopped: True

# Step 11: Report operation completion
  -> transcript: str = SessionLog.get_transcript()
     return transcript: "Session xyz789:\n  Loop 1: Reading story-graph.json and analyzing structure\n  Loop 2: Generated all nodes and relationships, knowledge graph complete\n  Total loops: 2"
  
  -> outcome: str = HeadlessSession.reports_operation_completion()
     -> console_output: str = format_operation_outcome(
            operation: "instructions",
            status: ai_status_2,
            transcript: transcript,
            log_path: log_path
        )
        return console_output: "✓ Instructions operation completed\n  Operation: shape.build.instructions\n  Log: logs/headless-2025-12-29-14-30-15.log"
     
     print(console_output)
     return outcome: "success"

return result: {status: "completed", operation: "instructions", log_path: "logs/headless-2025-12-29-14-30-15.log", total_loops: 2}
```

---

## Model Updates During Walkthrough

### Required Changes to Domain Model:

1. **HeadlessSession** - Operation execution entry point:
   - Public: `Invokes operation with behavior, action, operation, and context file: ExecutionResult, Behavior, Action, Operation, ContextFile`
   - Internal: `retrieves_operation_instructions()`, `executes_via_cursor_headless_api()`, `detects_completion_or_block()`, `stops_looping()`, `reports_operation_completion()`

2. **Behavior** - Collaborator for instruction retrieval:
   - `Gets action by name: Action, String`

3. **Action** - Collaborator for operation instructions:
   - `Gets instructions for operation: String, Operation`

### Design Principle Applied:
**Encapsulation** - HeadlessSession owns the complete operation execution flow including looping. Caller provides behavior, action, operation, and context file, receives result. All intermediate steps (context loading, instruction retrieval, preparation, API execution, looping, monitoring, logging) are internal implementation details.

## Coverage Summary

- ✓ Walk 1: CLI invocation through instruction retrieval and preparation (scenario steps 1-5)
- ✓ Walk 2: API execution, looping, and logging (scenario steps 6-9)
- ✓ Walk 3: Completion detection and reporting (scenario steps 10-11)
- ✓ Single entry point: `HeadlessSession.invokes_operation(behavior, action, operation, context_file)`
- ✓ All 11 scenario steps traced showing complete delegation chain including looping
- ✓ Caller only sees: input (behavior, action, operation, context_file) → output (result with operation and loop count)
- ✓ Implementation details (steps 2-11) hidden behind HeadlessSession interface

