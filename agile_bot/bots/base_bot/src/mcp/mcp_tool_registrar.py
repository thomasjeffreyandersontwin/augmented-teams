import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, Any
from fastmcp import FastMCP
from agile_bot.bots.base_bot.src.bot.bot import Bot, BotResult
from agile_bot.bots.base_bot.src.bot.workspace import get_workspace_directory
from agile_bot.bots.base_bot.src.mcp.server_restart import restart_mcp_server
from agile_bot.bots.base_bot.src.bot.workspace import get_python_workspace_root
from agile_bot.bots.base_bot.src.utils import read_json_file
logger = logging.getLogger(__name__)

class MCPToolRegistrar:

    def __init__(self, bot: Bot, bot_name: str, bot_directory: Path, registered_tools: list):
        self.bot = bot
        self.bot_name = bot_name
        self.bot_directory = bot_directory
        self.registered_tools = registered_tools

    def register_all_tools(self, mcp_server: FastMCP, behaviors: list, load_trigger_words_fn):
        self.register_bot_tool(mcp_server)
        self.register_get_working_dir_tool(mcp_server)
        self.register_set_working_dir_tool(mcp_server)
        self.register_close_current_action_tool(mcp_server)
        self.register_confirm_out_of_order_tool(mcp_server)
        self.register_restart_server_tool(mcp_server)
        for behavior in behaviors:
            self.register_behavior_tool(mcp_server, behavior, load_trigger_words_fn)

    def register_bot_tool(self, mcp_server: FastMCP):
        tool_name = 'tool'

        @mcp_server.tool(name=tool_name, description=f'Bot tool for {self.bot_name} - routes to current behavior and action.')
        async def bot_tool(parameters: dict=None):
            current_behavior = self.bot.behaviors.current
            if current_behavior is None:
                if self.bot.behaviors.first:
                    self.bot.behaviors.navigate_to(self.bot.behaviors.first.name)
                    current_behavior = self.bot.behaviors.current
                else:
                    raise ValueError('No behaviors available')
            if current_behavior is None:
                raise ValueError('No current behavior')
            action = current_behavior.actions.forward_to_current()
            result_data = action.execute(parameters or {})
            result = BotResult(status='completed', behavior=current_behavior.name, action=action.action_name, data=result_data)
            return {'status': result.status, 'behavior': result.behavior, 'action': result.action, 'data': result.data}
        self.registered_tools.append({'name': tool_name, 'type': 'bot_tool', 'description': f'Routes to current behavior and action'})

    def register_get_working_dir_tool(self, mcp_server: FastMCP):
        tool_name = 'get_working_dir'

        @mcp_server.tool(name=tool_name, description=f"Get the current working directory from WORKING_AREA. Triggers: where are we working, what's my location, show working directory")
        async def get_working_dir(input_file: str=None, project_dir: str=None):
            working_dir = get_workspace_directory()
            return {'working_dir': str(working_dir), 'message': f'Working directory from WORKING_AREA: {working_dir}'}
        self.registered_tools.append({'name': tool_name, 'type': 'get_working_dir_tool', 'description': f'Get current working directory'})

    def register_set_working_dir_tool(self, mcp_server: FastMCP):
        tool_name = 'set_working_dir'

        @mcp_server.tool(name=tool_name, description="Update the working directory (WORKING_AREA/WORKING_DIR). Triggers: update working directory, change working path, change working folder, set workspace")
        async def set_working_dir(new_path: str, persist: bool=True):
            if not new_path:
                return {'error': 'missing_path', 'message': 'new_path is required'}
            try:
                previous = str(self.bot.bot_paths.workspace_directory)
            except Exception:
                previous = None
            try:
                resolved = str(self.bot.bot_paths.update_workspace_directory(new_path, persist=persist))
                return {'working_dir': resolved, 'previous_working_dir': previous, 'persisted': bool(persist), 'message': f'Working directory updated to {resolved}'}
            except Exception as e:
                logger.error(f'Failed to set working directory: {e}', exc_info=True)
                return {'error': 'failed_to_set_working_dir', 'message': str(e)}
        self.registered_tools.append({'name': tool_name, 'type': 'set_working_dir_tool', 'description': 'Update working directory (WORKING_AREA/WORKING_DIR)'})

    def register_close_current_action_tool(self, mcp_server: FastMCP):
        tool_name = 'close_current_action'
        registrar = self

        @mcp_server.tool(name=tool_name, description=f'Close current action tool for {self.bot_name} - marks current action complete and transitions to next')
        async def close_current_action(parameters: dict=None):
            return registrar._handle_close_current_action()
        self.registered_tools.append({'name': tool_name, 'type': 'close_action_tool', 'description': f'Marks current action complete and transitions to next'})

    def _handle_close_current_action(self) -> dict:
        state_file = self.bot.bot_paths.workspace_directory / 'behavior_action_state.json'
        if not state_file.exists():
            return {'error': 'No active state found', 'message': 'No behavior_action_state.json exists. Start a behavior first.'}
        try:
            return self._perform_close_action()
        except Exception as e:
            return {'error': 'Failed to close current action', 'message': str(e)}

    def _perform_close_action(self) -> dict:
        current_behavior = self.bot.behaviors.current
        current_behavior.actions.load_state()
        current_action = current_behavior.actions.current
        action_name = current_action.action_name
        action_names = current_behavior.actions.names
        is_final_action = action_name == action_names[-1] if action_names else False
        current_behavior.actions.close_current()
        new_action = current_behavior.actions.current
        behavior_complete = new_action is None or (is_final_action and new_action.action_name == action_name)
        if behavior_complete:
            return self._handle_behavior_complete(current_behavior, action_name)
        return self._handle_action_transition(current_behavior, action_name)

    def _handle_behavior_complete(self, current_behavior, action_name: str) -> dict:
        next_behavior = self.bot.behaviors.next()
        if next_behavior:
            self.bot.behaviors.navigate_to(next_behavior.name)
            next_behavior.actions.load_state()
            first_action = next_behavior.actions.current.action_name if next_behavior.actions.current else 'clarify'
            return {'status': 'completed', 'completed_action': action_name, 'completed_behavior': current_behavior.name, 'next_behavior': next_behavior.name, 'next_action': first_action, 'message': f"Behavior '{current_behavior.name}' complete. Transitioned to behavior '{next_behavior.name}', action '{first_action}'."}
        return {'status': 'completed', 'completed_action': action_name, 'completed_behavior': current_behavior.name, 'message': f"Action '{action_name}' marked complete. All behaviors complete."}

    def _handle_action_transition(self, current_behavior, action_name: str) -> dict:
        new_action_name = current_behavior.actions.current.action_name if current_behavior.actions.current else None
        return {'status': 'completed', 'completed_action': action_name, 'next_action': new_action_name, 'message': f"Action '{action_name}' marked complete. Transitioned to '{new_action_name}'."}

    def register_confirm_out_of_order_tool(self, mcp_server: FastMCP):
        tool_name = 'confirm_out_of_order'

        @mcp_server.tool(name=tool_name, description=f'Confirm out-of-order behavior execution for {self.bot_name} - MUST be called explicitly by HUMAN USER, NOT by AI assistant. AI must ask user to call this tool, never call it directly.')
        async def confirm_out_of_order(behavior: str):
            working_dir = get_workspace_directory()
            state_file = working_dir / 'behavior_action_state.json'
            try:
                state_data = json.loads(state_file.read_text(encoding='utf-8'))
                if 'out_of_order_confirmations' not in state_data:
                    state_data['out_of_order_confirmations'] = {}
                state_data['out_of_order_confirmations'][behavior] = {'confirmed_at': datetime.now().isoformat(), 'confirmed_by': 'human'}
                state_file.write_text(json.dumps(state_data, indent=2), encoding='utf-8')
                return {'status': 'confirmed', 'behavior': behavior, 'message': f"Out-of-order execution confirmed for behavior '{behavior}'. You may now execute this behavior.", 'confirmed_at': state_data['out_of_order_confirmations'][behavior]['confirmed_at']}
            except Exception as e:
                return {'error': 'Failed to confirm out-of-order execution', 'message': str(e)}
        self.registered_tools.append({'name': tool_name, 'type': 'confirm_out_of_order_tool', 'description': f'Confirm out-of-order behavior execution (must be called explicitly by human)'})

    def register_restart_server_tool(self, mcp_server: FastMCP):
        tool_name = 'restart_server'

        @mcp_server.tool(name=tool_name, description=f'Restart MCP server for {self.bot_name} - terminates processes, clears cache, and restarts to load code changes')
        async def restart_server(parameters: dict=None):
            try:
                workspace_root = get_python_workspace_root()
                bot_location = str(self.bot_directory.relative_to(workspace_root))
                result = restart_mcp_server(workspace_root=workspace_root, bot_name=self.bot_name, bot_location=bot_location)
                return result
            except Exception as e:
                logger.error(f'Failed to restart MCP server: {e}', exc_info=True)
                return {'status': 'error', 'error': 'Failed to restart server', 'message': str(e)}
        self.registered_tools.append({'name': tool_name, 'type': 'restart_server_tool', 'description': f'Restarts MCP server to load code changes'})

    def register_behavior_tool(self, mcp_server: FastMCP, behavior: str, load_trigger_words_fn):
        tool_name = behavior
        trigger_patterns = load_trigger_words_fn(behavior=behavior)
        description = self._build_behavior_tool_description(behavior, trigger_patterns)
        registrar = self

        @mcp_server.tool(name=tool_name, description=description)
        async def behavior_tool(action: str=None, parameters: dict=None):
            return registrar._execute_behavior_tool(behavior, action, parameters)
        self.registered_tools.append({'name': tool_name, 'behavior': behavior, 'type': 'behavior_tool', 'trigger_patterns': trigger_patterns, 'description': description})

    def _build_behavior_tool_description(self, behavior: str, trigger_patterns: list) -> str:
        description = f'{behavior} behavior for {self.bot_name}. Accepts optional action parameter and parameters dict.'
        if trigger_patterns:
            description += f"\nTrigger patterns: {', '.join(trigger_patterns[:5])}"
        return description

    def _execute_behavior_tool(self, behavior: str, action: str=None, parameters: dict=None) -> dict:
        try:
            behavior_obj = self.bot.behaviors.find_by_name(behavior)
            result = self._run_behavior_action(behavior_obj, behavior, action, parameters)
            return {'status': result.status, 'behavior': result.behavior, 'action': result.action, 'data': result.data}
        except Exception as e:
            return {'error': f'Failed to execute behavior: {e}'}

    def _run_behavior_action(self, behavior_obj, behavior: str, action: str=None, parameters: dict=None) -> BotResult:
        if action:
            action_obj = behavior_obj.actions.find_by_name(action)
            result_data = action_obj.execute(parameters or {})
            return BotResult(status='completed', behavior=behavior, action=action, data=result_data)
        behavior_obj.actions.load_state()
        current_action = behavior_obj.actions.current
        result_data = current_action.execute(parameters or {})
        return BotResult(status='completed', behavior=behavior, action=current_action.action_name, data=result_data)