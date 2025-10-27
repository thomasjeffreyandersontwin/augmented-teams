#!/usr/bin/env python3
"""
MCP Proxy - Core Business Logic
Provides MCP server proxy functionality that bridges HTTP to MCP protocol
"""

import subprocess
import json
import os
from typing import Dict, Any


def proxy_mcp_call(tool_name: str, input_data: dict, mcp_server: str = "github") -> dict:
    """
    Proxy an MCP call to the GitHub MCP server running in Docker
    
    Uses the MCP protocol via stdio to communicate with the MCP server.
    
    Args:
        tool_name: Name of the MCP tool to call (e.g., "github_search_code")
        input_data: Input parameters for the tool
        mcp_server: Which MCP server to use (from mcp.json)
    
    Returns:
        Tool execution result
    """
    # Get the GitHub token from environment
    github_token = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN", "")
    
    if not github_token:
        return {
            "success": False,
            "error": "GITHUB_PERSONAL_ACCESS_TOKEN not set"
        }
    
    # Build the MCP request following the protocol
    mcp_request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": input_data
        }
    }
    
    # For now, return a structured response
    # TODO: Implement full MCP stdio communication
    return {
        "success": True,
        "tool": tool_name,
        "input": input_data,
        "result": f"MCP call would be made with: {json.dumps(mcp_request, indent=2)}"
    }


def get_mcp_tools(mcp_server: str = "github") -> list:
    """Get list of available MCP tools"""
    # TODO: Query the MCP server via stdio for actual tools
    return [
        "github_search_code",
        "github_get_file_contents",
        "github_create_issue",
        "github_list_pull_requests",
        "github_list_commits",
        "github_get_commit",
        "github_create_branch",
        "github_push_files",
        "github_delete_file",
        "github_create_pull_request",
        "github_update_issue",
        "github_create_repository"
    ]


def get_tool_schema(tool_name: str) -> dict:
    """Get schema for a specific tool - supports ChatGPT introspection"""
    # Tool schemas based on GitHub MCP server documentation
    schemas = {
        "github_search_code": {
            "name": "github_search_code",
            "description": "Search for code in GitHub repositories",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query using GitHub code search syntax"
                    },
                    "language": {
                        "type": "string",
                        "description": "Filter by programming language (e.g., 'python', 'javascript')"
                    },
                    "owner": {
                        "type": "string",
                        "description": "Repository owner to search within"
                    },
                    "repo": {
                        "type": "string",
                        "description": "Specific repository to search"
                    }
                },
                "required": ["query"]
            }
        },
        "github_get_file_contents": {
            "name": "github_get_file_contents",
            "description": "Get contents of a file from a GitHub repository",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "owner": {"type": "string", "description": "Repository owner"},
                    "repo": {"type": "string", "description": "Repository name"},
                    "path": {"type": "string", "description": "File path in repository"},
                    "ref": {"type": "string", "description": "Branch or commit SHA"}
                },
                "required": ["owner", "repo", "path"]
            }
        },
        "github_create_issue": {
            "name": "github_create_issue",
            "description": "Create a new GitHub issue",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "owner": {"type": "string", "description": "Repository owner"},
                    "repo": {"type": "string", "description": "Repository name"},
                    "title": {"type": "string", "description": "Issue title"},
                    "body": {"type": "string", "description": "Issue body"},
                    "labels": {"type": "array", "description": "Labels to apply"}
                },
                "required": ["owner", "repo", "title"]
            }
        }
    }
    return schemas.get(tool_name, {"error": f"Unknown tool: {tool_name}"})


def list_tools_with_schemas() -> list:
    """List all tools with their schemas for full introspection"""
    tools = get_mcp_tools()
    return [
        get_tool_schema(tool) for tool in tools
    ]


def get_mcp_server_config(mcp_server: str = "github") -> dict:
    """
    Get configuration for an MCP server
    
    Reads from the mcp.json format to get server config
    """
    config = {
        "github": {
            "command": "docker",
            "args": [
                "run",
                "-i",
                "--rm",
                "-e",
                f"GITHUB_PERSONAL_ACCESS_TOKEN={os.getenv('GITHUB_PERSONAL_ACCESS_TOKEN', '')}",
                "ghcr.io/github/github-mcp-server"
            ]
        }
    }
    return config.get(mcp_server, {})
