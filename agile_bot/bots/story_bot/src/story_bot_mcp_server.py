"""
Story Bot MCP Server Entry Point

Runnable MCP server for story_bot using FastMCP and base generator.
"""
from pathlib import Path
import sys
import os

# Prefer an explicit working directory (set by tools) to avoid embedding a
# hard-coded workspace path in multiple places. Tools should set the
# `WORKING_DIR` environment variable to point to the project's root when
# invoking MCP tools. If it's not set, fall back to behavior-relative path.
# Keep Python import root calculation unchanged so package imports resolve
# correctly. This value is solely for import-path resolution and should not
# be confused with the workspace root used for runtime content I/O.
python_workspace_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(python_workspace_root))

# Use the centralized workspace utility for runtime workspace resolution.
from agile_bot.bots.base_bot.src.state.workspace import get_workspace_directory

# Determine runtime workspace root (from WORKING_DIR env var, or fallback)
from agile_bot.bots.base_bot.src.mcp.mcp_server_generator import MCPServerGenerator


def main():
    """Main entry point for story_bot MCP server.

    Runtime workspace is determined from the environment (WORKING_AREA).
    The Python import root logic above remains unchanged for import resolution.
    """
    # Resolve workspace from environment (WORKING_AREA preferred)
    workspace_root = get_workspace_directory()

    generator = MCPServerGenerator(
        workspace_root=workspace_root,
        bot_location='agile_bot/bots/story_bot'
    )

    mcp_server = generator.create_server_instance()
    generator.register_all_behavior_action_tools(mcp_server)

    mcp_server.run()


if __name__ == '__main__':
    main()
