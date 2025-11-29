Epic
    Feature
        Story
            AC

Build Agile Bots
	Generate Bot Server And Tools
    	Provides Context of New Bot
    	Generate MCP Bot Server
            Human tells Bot to generate server
            Agile Bot triggers MCP Bot Server Generator
            MCP Bot Server Generator reads Bot Config from Bot Config file (agent.json)
            MCP Bot Server Generator creates MCP Bot Server Class from Bot Config
    	Drop Bot Builder Behavior into Chat
    	Create Bot Scaffolding
        Generate Bot Tools
            MCP Bot Server Generator reads Bot Config
            MCP Bot Server Generator creates Bot Tool with trigger words in tool description docstring, and tool name
			MCP Bot Server Generates code that routes to active or next behavior and action of agent
        Generate Behavior Tools
            MCP Bot Server Generator reads Bot Config
            MCP Bot Server Generator creates Behavior Tool for each Bot Behavior with trigger words in tool description docstring, and tool name
			MCP Bot Server Generates code that routes to active or next action of Bot Behavior
        Generate Behavior Action Tools
            MCP Bot Server Generator reads Bot Config
            MCP Bot Server Generator creates Behavior Action Tool for each Bot Behavior-Action combination with aggregated trigger words in tool description docstring, and tool name
			MCP Bot Server Generates code that routes to specific Bot Behavior and Bot Action
		Deploy MCP BOT Server
			 Bot MCP Server exposes Bot Tool via FastMCP
			 Bot MCP Server exposes Behavior Tools via FastMCP
			 Bot MCP Server exposes Behavior Action Tools via FastMCP
			 Bot MCP Server exposes Project State Tool via FastMCP

Invoke MCP Bot Server
    Init Project
        Shares Context and Project Location
            AI Chat presents discovered Project Location to Human
            Human confirms or provides different Project Location
        Speaks Trigger Words For Bot Tool
        Speaks Trigger Words For Bot Behavior Tool
        Speaks Trigger Words For Bot Behavior Action Tool
            Human speaks to AI Chat with trigger words including Bot Behavior and Bot Action (ex: "start shaping for project xx"), including context
            AI Chat detects trigger words and routes to Behavior Action Tool via Bot MCP Server
            Behavior Action Tool receives invocation with context
        Speaks Trigger Words For Project Tool
        Determines Working Area From Current Dir
        Intercepts Tool Call With Project Check
        Route To Project Tool
        Locates Existing Project Bot State
        Generates Project Scaffold
            Project creates project folder structure in project location
            Project creates Bot activity subfolder (docs/activity/{bot_name}/)
            Project Bot State stores Project Area and Bot Name to File System
            MCP Bot Server Routes to MCP Tool based on trigger words
        Confirm Location
        Move to Project
        Create Project Folder
        Saves Project State to Agent State File
        Updates Project Area and Creates Directory Structure
        Stores Activity for Initialize Project Action
        Provides addtnl Instructions
    Invoke Bot Tool
        Drops Behavior Folder in Chat w/ relevant Bot Config
        Speaks Trigger Words For Bot Behavior Action Tool
        Speaks Trigger Words For Bot Behavior Tool
        Speaks Trigger Words For Bot Tool
        Invokes Correct Behavior Action (We Hope)
        Route To Behavior Action
            Human speaks to AI Chat with trigger words including Bot Behavior but no Bot Action (ex: "start stories for project xx"), including context
            AI Chat routes request to Behavior Tool via Bot MCP Server
            Behavior Tool determines active or next Behavior/Action
            Behavior Tool receives invocation with context
        Route To MCP Behavior  Tool
        Route To MCP BotTool
            Human speaks to AI Chat with trigger words for Bot but no Bot Behavior (ex: "start stories for project xx"), including context
            AI Chat detects trigger words and routes to Bot Tool via Bot MCP Server
            Bot Tool receives invocation with context and determines active Bot Behavior from Workflow State
        Forward To Behavior Action
        Forward To Behavior and Current Action
        Forward To Current Behavior and Current Action
        Invoke Action In Behavior
    Perform Behavior Action
        Injects Instructions
        Inject Next behavor-Action to Instructions
        Folllows Instructions from Folder configs (We Hope)
        Folllows Injected Instructions
        Correct, Feedback, Proceed
        Proceeds to Instructions from next Action in Folder (We Hope)
        Calls Next MCP Behavior Action Tool
        Submit Content Changes to Tools for Saving
        Saves Content
        Saves Behavior State

Execute Behavior Actions
    Gather Context
        Displays Gather Context Instructions (we hope)
        Loads Questions and Evidence
        RetrievesQuestions And Evidence from Chat(hope)
        Injects Gather Context Instructions
        Answers Questions and Evidence from Context (hope)
        Answers Questions and Evidence from Context
        Pauses we hope
        Pauses
        Correct, Feedback, Proceed
        Updates Final Answers and Evidence (hope)
        Updates Final Answers and Evidence
        Submit Answers and Evidence to Tools for Saving
        Saves Answers and Evidence
        Proceeds to follow planning (we Hope)
        Calls Behavior Planning Tool
    Decide Planning Criteria
        Loads Next Behavior and Action from Workflow State
        Displays Planning Instructions from Conffig (we hope)
        Loads Decsion Criteria and Evidence
        Retrieves Decision Criteria and Evidence From Chat
        Injects Planning Instructions
        Makes Assumptions and Decisions from Context (hope)
        Makes Assumptions and Decisions from Context
        Pauses we hope
        Pauses
        Correct, Feedback, Proceed
        Updates Assumpions and Decisions (hopr)
        Updates Assumpions and Decisions
        Submits Final Assumptions andDecsions
        Proceeds to follow planning (we Hope)
        Saves Final Assumptions  and Decisions
        Proceeds to Build Knowledge (we Hope)
        Calls Build Knowledge Tool
    Build Knowledge
    Render Output Action
    Validate Rules Action
    Correct Bot Action

Manage Workflow State
    Determine Active Behavior and Action
    Validate Workflow State
    Transition Workflow State

Manage Project State
    Store Project State
    Store Workflow State
    Store Activity Data
    Store Output Data

Load Configuration
    Load Bot Config
    Load Behavior Configuration
    Load Action Instructions
    Load Templates and Rules

Generate Instructions
    Generate Action Instructions
    Generate Build Instructions
    Generate Transform Instructions
    Generate Validation Instructions
