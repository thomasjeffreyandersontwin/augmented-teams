# Walkthrough: Execute Direct Instructions In Headless Mode

**Scope:** Execute In Headless Mode.Execute In Headless Mode.Execute Direct Instructions.Execute direct message in headless mode

**Story:** Human sends direct instructions to headless mode for immediate execution

## Scenario: Execute direct message in headless mode

**Steps:**
- Given AI has written headless-context.md with user intent and chat history
- And headless mode is configured with API key
- When human invokes CLI with --headless flag and --message Implement user authentication
- Then CLI reads headless-context.md file
- And CLI prepends message before context content
- And CLI wraps instructions with Keep doing this until 100% done or blocked directive
- And CLI sends combined instructions to Cursor Headless API
- And CLI creates timestamped log file in logs directory
- And AI executes instruction and indicates not done
- And CLI appends AI response to log file
- And CLI loops instruction again with persistence directive
- And AI continues work and indicates not done
- And CLI appends AI response to log file
- And CLI loops instruction again with persistence directive
- And AI completes work and indicates done
- And CLI appends AI response to log file
- And CLI detects AI completion signal
- And CLI stops looping
- And CLI reports success with log file path

---

## Walk 1 - Covers: Steps 1-4 (CLI invocation through instruction preparation)

### Realization:

```
# Step 1: Human invokes CLI with headless mode
result: ExecutionResult = HeadlessSession.invokes(
    message: "Implement user authentication",
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
        -> user_message: UserMessage = ExecutionContext.get_user_message()
           return user_message: "Please implement authentication with JWT tokens"
        
        -> history: ChatHistory = ExecutionContext.get_chat_history()
           return history: ["User: We need secure login", "AI: I'll implement JWT..."]
        
        -> refs: List[FileReference] = ExecutionContext.get_file_references()
           return refs: ["src/auth/login.py", "src/models/user.py"]
        
        return context_loaded: ExecutionContext
     return context: ExecutionContext

# Step 4: Prepare instructions with message and context
  -> instructions: Instructions = HeadlessSession.prepares_instructions_with_persistence_directive()
     -> with_message: str = Instructions.prepends_message_parameter(
            message: "Implement user authentication"
        )
        return with_message: "Implement user authentication\n\n"
     
     -> with_context: str = Instructions.prepends_context(
            context: context
        )
        return with_context: "[message]\n\nUser: Please implement...\nHistory: ...\nFiles: ..."
     
     -> with_directive: str = Instructions.wraps_with_persistence_directive()
        return with_directive: "Keep doing this until 100% done or blocked:\n\n[instructions]"
     
     -> final: str = Instructions.appends_block_reporting_directive()
        return final: "[instructions]\n\nIf blocked, report reason clearly."
     
     return instructions: final
```

---

## Walk 2 - Covers: Steps 5-9 (API execution, looping, and logging)

### Realization:

```
# Step 5: Execute via Cursor Headless API
  -> response: Response = HeadlessSession.executes_via_cursor_headless_api()
     -> api: CursorHeadlessAPI = CursorHeadlessAPI.connect(
            api_key: config.api_key
        )
        return api: CursorHeadlessAPI(connected: True)
     
     -> session_id: SessionId = api.start_session(
            instructions: instructions
        )
        return session_id: "session_abc123"
     
     return response: Response

# Step 6: Create session log
  -> log: SessionLog = HeadlessSession.get_session_log()
     -> log_path: Path = SessionLog.creates_with_timestamped_path(
            base_dir: "logs/"
        )
        return log_path: "logs/headless-2025-12-29-13-18-26.log"
     return log: SessionLog

# Step 7: Loop iteration 1 - AI indicates not done
  -> loop_count: int = 1
  -> api_response_1: Response = api.poll_session_status(
         session_id: session_id
     )
     return api_response_1: {state: "running", progress: "Created user model and login endpoint"}
  
  -> logged_1: bool = SessionLog.appends_response(
         response: api_response_1
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

# Step 8: Loop iteration 2 - AI indicates not done
  -> loop_count: int = 2
  -> api_response_2: Response = api.poll_session_status(
         session_id: session_id
     )
     return api_response_2: {state: "running", progress: "Added JWT token generation and validation"}
  
  -> logged_2: bool = SessionLog.appends_response(
         response: api_response_2
     )
     return logged_2: True
  
  -> ai_status_2: SessionStatus = HeadlessSession.detects_completion_or_block()
     return ai_status_2: {state: "running", done: False}
  
  -> loop_instruction_2: str = Instructions.wraps_with_persistence_directive()
     return loop_instruction_2: "Keep doing this until 100% done or blocked:\n\n[instructions]"
  
  -> api_response_3: Response = api.send_instruction(
         session_id: session_id,
         instruction: loop_instruction_2
     )
     return api_response_3: {state: "running"}

# Step 9: Loop iteration 3 - AI indicates done
  -> loop_count: int = 3
  -> api_response_3: Response = api.poll_session_status(
         session_id: session_id
     )
     return api_response_3: {state: "completed", progress: "Added tests and documentation, authentication complete"}
  
  -> logged_3: bool = SessionLog.appends_response(
         response: api_response_3
     )
     return logged_3: True
  
  -> ai_status_3: SessionStatus = HeadlessSession.detects_completion_or_block()
     return ai_status_3: {state: "completed", done: True}
  
  -> total_loops: int = 3
  -> loop_summary: str = SessionLog.appends_total_loops(
         count: total_loops
     )
     return loop_summary: "Total loops: 3"
```

---

## Walk 3 - Covers: Steps 10-11 (Completion detection and reporting)

### Realization:

```
# Step 10: Detect completion and stop looping
  -> completion_detected: bool = HeadlessSession.detects_completion_signal(
         status: ai_status_3
     )
     return completion_detected: True
  
  -> loop_stopped: bool = HeadlessSession.stops_looping()
     return loop_stopped: True

# Step 11: Report success
  -> transcript: str = SessionLog.get_transcript()
     return transcript: "Session abc123:\n  Loop 1: Created user model and login endpoint\n  Loop 2: Added JWT token generation and validation\n  Loop 3: Added tests and documentation, authentication complete\n  Total loops: 3"
  
  -> outcome: str = HeadlessSession.reports_outcome_to_console()
     -> console_output: str = format_outcome(
            status: ai_status_3,
            transcript: transcript,
            log_path: log_path
        )
        return console_output: "✓ Headless execution completed\n  Log: logs/headless-2025-12-29-13-18-26.log"
     
     print(console_output)
     return outcome: "success"

return result: {status: "completed", log_path: "logs/headless-2025-12-29-13-18-26.log", total_loops: 3}
```

---

## Model Updates During Walkthrough

### Required Changes to Domain Model:

1. **HeadlessSession** - Single entry point with internal looping:
   - Public: `Invokes with message and context file: ExecutionResult, Message, ContextFile`
   - Internal: `executes_via_cursor_headless_api()`, `detects_completion_or_block()`, `stops_looping()`, `reports_outcome_to_console()`

2. **SessionLog** - Enhanced with loop tracking:
   - `Appends response: Response` - logs each API response
   - `Appends total loops: int` - logs final loop count

3. **Instructions** - Internal to HeadlessSession:
   - `wraps_with_persistence_directive()` - creates loop instruction

### Design Principle Applied:
**Encapsulation** - HeadlessSession owns the complete headless execution flow including looping. Caller provides message and context file, receives result. All intermediate steps (context loading, instruction preparation, API execution, looping, monitoring, logging) are internal implementation details.

## Coverage Summary

- ✓ Walk 1: CLI invocation through instruction preparation (scenario steps 1-4)
- ✓ Walk 2: API execution, looping, and logging (scenario steps 5-9)
- ✓ Walk 3: Completion detection and reporting (scenario steps 10-11)
- ✓ Single entry point: `HeadlessSession.invokes(message, context_file)`
- ✓ All 11 scenario steps traced showing complete delegation chain including looping
- ✓ Caller only sees: input (message, context_file) → output (result with loop count)
- ✓ Implementation details (steps 2-11) hidden behind HeadlessSession interface

