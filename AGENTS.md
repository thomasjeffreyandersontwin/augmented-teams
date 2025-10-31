[tdd-pipeline-mcp]

You are given two tools from TDD Pipeline MCP server:

## 1. `get_current_step`
You `MUST` use this tool when:
+ Checking pipeline status for a feature
+ Understanding where we are in the TDD workflow
+ Getting information about what step is active
+ Checking what phase we're in

## 2. `execute_next_step`
You `MUST` use this tool when:
+ Continuing the pipeline for a feature
+ Moving to the next step
+ Executing the pipeline workflow
+ Running the next task in TDD

Input: feature_name (string, required)
