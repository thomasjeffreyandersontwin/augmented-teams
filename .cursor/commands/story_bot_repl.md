# Story Bot Interactive REPL

Launch the Story Bot interactive REPL session in the background and act as an intermediary between the user and the REPL.

## Usage

```
/story_bot_repl
```

## Behavior

When this command is invoked:

1. **Launch REPL in Background**: Start the Story Bot REPL in a background terminal process
   - Use PowerShell script: `agile_bot\bots\story_bot\repl.ps1`
   - Keep the process running throughout the session

2. **Act as Intermediary**: Interpret all user requests related to Story Bot workflows and translate them into REPL commands
   - Read REPL output to understand current state and instructions
   - Follow the three-step workflow for each action:
     - **instructions**: Get what needs to be done (questions, evidence needed)
     - **submit**: Submit answers and evidence  
     - **confirm**: Mark complete and auto-advance to next action

3. **Workflow Management**:
   - Track current behavior and action state
   - When action gives instructions, help user complete the work before submitting
   - When ready, submit on behalf of user
   - Confirm when user is satisfied with results
   - Follow the instructions provided by each action

4. **Command Translation**:
   - User says "start shape behavior" → Send: `shape`
   - User says "begin clarify" → Send: `clarify` (gets instructions)
   - User provides answers → Send: `clarify` again (submits)
   - User approves → Send: `clarify` again (confirms and advances)
   - User says "help with build" → Send: `help build`
   - User says "go back" → Send: `back`
   - User says "show status" → Send: `status`

5. **Communication Style**:
   - Report what the REPL says (instructions, questions, confirmations)
   - Ask user for input when REPL requests it
   - Confirm before advancing to next action
   - Keep user informed of workflow progress

## Available Commands

### Behaviors
- `shape`, `prioritization`, `discovery`, `exploration`, `scenarios`, `tests`, `code`

### Actions (within a behavior)
- `clarify`, `strategy`, `build`, `validate`, `render`
- Each action has 3 steps: instructions → submit → confirm
- Calling action name repeatedly cycles through steps

### Navigation
- `help [action]` - Show help or detailed action help
- `status` - Show current workflow state  
- `current` - Show current action
- `back` - Move back to previous action
- `confirm` - Mark current action complete and advance
- `exit` - Exit REPL

### Action Subcommands (explicit)
- `<action> instructions` - Get instructions for action
- `<action> submit` - Submit answers/evidence
- `<action> confirm` - Mark complete and advance

## Example Session

```
User: "Let's work on the shape behavior"
AI: *sends 'shape' to REPL*
AI: "Started shape behavior. Currently on clarify action."

User: "What do I need to do?"
AI: *sends 'clarify' to REPL*
AI: "The clarify action needs you to:
     - Review context and requirements  
     - Answer key questions
     - Provide necessary evidence
     
     What questions do you have?"

User: "I've completed the work"
AI: *sends 'clarify' again to submit*
AI: "Submitted. Everything looks good. Ready to confirm and move to next action?"

User: "Yes"
AI: *sends 'clarify' again to confirm*
AI: "Confirmed! Moving to strategy action...
     Strategy instructions: ..."
```

## Important Notes

- The REPL maintains state between commands
- Each action automatically advances to the next after confirmation
- The AI should read and interpret REPL output before responding to user
- Always confirm with user before confirming actions in the REPL
- If REPL encounters errors, report them clearly to user

