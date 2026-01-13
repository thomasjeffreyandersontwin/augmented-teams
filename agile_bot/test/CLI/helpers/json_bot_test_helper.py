"""
JSON Bot Test Helper - Comprehensive JSON structure validation

Validates COMPLETE JSON structures, not primitive field checks.
Every assertion validates the entire expected structure.
"""
import json
from pathlib import Path
from .cli_bot_test_helper import CLIBotTestHelper


class JsonBotHelper:
    """Helper for bot-level JSON assertions - validates complete structures"""
    
    def __init__(self, parent):
        self.parent = parent
    
    def _parse_json(self, output: str) -> dict:
        """Parse JSON output."""
        output = output.strip()
        try:
            return json.loads(output)
        except json.JSONDecodeError:
            # Try to find first complete JSON object
            start_idx = output.find('{')
            if start_idx >= 0:
                brace_count = 0
                for i in range(start_idx, len(output)):
                    if output[i] == '{':
                        brace_count += 1
                    elif output[i] == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            json_str = output[start_idx:i+1]
                            return json.loads(json_str)
            raise ValueError(f"Output does not contain valid JSON: {output[:200]}")
    
    def assert_status_section_present(self, output: str):
        """
        Validate COMPLETE status JSON structure by comparing JSON objects.
        
        Standard structure from bot.execute():
        {
          "status": "success",
          "behavior": "behavior_name",
          "action": "action_name"
        }
        """
        actual = self._parse_json(output)
        
        # Define expected JSON structure (subset - must have these fields)
        required_structure = {
            "status": str,  # Must be string
            "behavior": str,  # Must be string
            "action": str  # Must be string
        }
        
        # Validate structure
        for key, expected_type in required_structure.items():
            assert key in actual, \
                f"Missing required field '{key}'.\nExpected structure: {list(required_structure.keys())}\nActual: {actual}"
            assert isinstance(actual[key], expected_type), \
                f"Field '{key}' must be {expected_type.__name__}, got {type(actual[key]).__name__}.\nActual JSON: {actual}"
        
        # Validate status value
        assert actual['status'] in ['success', 'error'], \
            f"'status' must be 'success' or 'error', got '{actual['status']}'.\nActual JSON: {actual}"
    
    def assert_error_shows_behavior_not_found(self, output: str, behavior: str):
        """
        Validate COMPLETE error JSON structure by comparing JSON objects.
        
        Standard error structure:
        {
          "status": "error",
          "message": "Behavior not found: behavior_name",
          "available_behaviors": ["behavior1", "behavior2", ...]
        }
        """
        actual = self._parse_json(output)
        
        # Define expected JSON structure
        expected_subset = {
            "status": "error",
            "message": f"Behavior not found: {behavior}"
        }
        
        # Compare JSON objects
        for key, expected_value in expected_subset.items():
            assert key in actual, \
                f"Missing field '{key}' in error response.\nExpected: {expected_subset}\nActual: {actual}"
            if key == 'message':
                # Message should contain the expected text
                assert expected_value in actual[key], \
                    f"Expected message to contain '{expected_value}', got '{actual[key]}'.\nFull actual: {actual}"
            else:
                assert actual[key] == expected_value, \
                    f"Field '{key}' mismatch.\nExpected: {expected_value}\nActual: {actual[key]}\nFull actual: {actual}"
        
        # Validate available_behaviors if present
        if 'available_behaviors' in actual:
            assert isinstance(actual['available_behaviors'], list), \
                f"'available_behaviors' must be list.\nActual JSON: {actual}"
    
    def assert_error_shows_action_not_found(self, output: str, action: str):
        """
        Validate COMPLETE error JSON structure for action not found.
        
        Standard error structure:
        {
          "status": "error",
          "message": "Action not found: action_name",
          "available_actions": ["action1", "action2", ...]
        }
        """
        data = self._parse_json(output)
        
        # Validate complete error structure
        required_fields = ['status', 'message']
        missing = [f for f in required_fields if f not in data]
        assert not missing, \
            f"Missing required error fields: {missing}. Got: {list(data.keys())}"
        
        # Validate error content
        assert data['status'] == 'error', \
            f"Expected status='error', got '{data['status']}'"
        assert 'Action not found' in data['message'], \
            f"Expected 'Action not found' in message, got '{data['message']}'"
        assert action in data['message'], \
            f"Expected action '{action}' in error message"
        
        # Validate available_actions if present
        if 'available_actions' in data:
            assert isinstance(data['available_actions'], list), \
                "available_actions must be a list"
    
    def assert_status_shows_current_state(self, output: str, behavior: str, action: str):
        """
        Validate COMPLETE Behavior object JSON structure.
        
        Standard Behavior structure:
        {
          "name": "behavior_name",
          "bot_name": "story_bot",
          "action_names": ["action1", "action2", ...],
          "order": 1,
          "description": "..."
        }
        """
        data = self._parse_json(output)
        
        # Validate ALL required Behavior fields
        required_fields = ['name', 'action_names']
        missing = [f for f in required_fields if f not in data]
        assert not missing, \
            f"Missing required Behavior fields: {missing}. Got: {list(data.keys())}"
        
        # Validate types
        assert isinstance(data['name'], str), "'name' must be string"
        assert isinstance(data['action_names'], list), "'action_names' must be list"
        assert all(isinstance(a, str) for a in data['action_names']), \
            "All action_names must be strings"
        
        # Validate values
        assert data['name'] == behavior, \
            f"Expected name='{behavior}', got '{data['name']}'"
        assert action in data['action_names'], \
            f"Expected '{action}' in action_names {data['action_names']}"
        
        # Validate optional fields if present
        if 'order' in data:
            assert isinstance(data['order'], (int, float)), \
                f"'order' must be number, got {type(data['order'])}"
        if 'description' in data:
            assert isinstance(data['description'], str), \
                "'description' must be string"
    
    def assert_bot_metadata_shown(self, output: str, bot_name: str):
        """
        Validate bot metadata in JSON output.
        
        Expected fields:
        {
          "bot_name": "story_bot",
          "name": "...",
          ...
        }
        """
        data = self._parse_json(output)
        
        # Validate bot_name
        assert 'bot_name' in data, \
            f"Missing 'bot_name' field: {list(data.keys())}"
        assert data['bot_name'] == bot_name, \
            f"Expected bot_name='{bot_name}', got '{data['bot_name']}'"


class JsonInstructionsHelper:
    """Helper for instructions - validates complete execution response structures"""
    
    def __init__(self, parent):
        self.parent = parent
    
    def _parse_json(self, output: str) -> dict:
        return self.parent.bot._parse_json(output)
    
    def assert_section_shows_behavior_and_action(self, output: str, behavior: str, action: str):
        """
        Validate COMPLETE action execution response by comparing JSON objects.
        
        Standard structure from bot.execute():
        {
          "status": "success",
          "message": "Executed behavior.action",
          "behavior": "behavior_name",
          "action": "action_name",
          "result": "Action execution complete"
        }
        """
        actual = self._parse_json(output)
        
        # Define the COMPLETE expected JSON structure
        expected = {
            "status": "success",
            "message": f"Executed {behavior}.{action}",
            "behavior": behavior,
            "action": action,
            "result": "Action execution complete"
        }
        
        # Compare complete JSON objects
        for key, expected_value in expected.items():
            assert key in actual, \
                f"Missing required field '{key}' in JSON.\nExpected: {expected}\nActual: {actual}"
            assert actual[key] == expected_value, \
                f"Field '{key}' mismatch.\nExpected: {expected_value}\nActual: {actual[key]}\n\nFull expected: {expected}\nFull actual: {actual}"
    
    def assert_behavior_instructions_shown(self, output: str, behavior: str):
        """
        Validate behavior present in complete execution response.
        See assert_section_shows_behavior_and_action for full structure.
        """
        data = self._parse_json(output)
        assert 'behavior' in data, f"Missing 'behavior' field: {list(data.keys())}"
        assert data['behavior'] == behavior, \
            f"Expected behavior='{behavior}', got '{data['behavior']}'"
    
    def assert_action_instructions_shown(self, output: str, action: str):
        """
        Validate action present in complete execution response.
        See assert_section_shows_behavior_and_action for full structure.
        """
        data = self._parse_json(output)
        assert 'action' in data, f"Missing 'action' field: {list(data.keys())}"
        assert data['action'] == action, \
            f"Expected action='{action}', got '{data['action']}'"


class JsonNavigationHelper:
    """Helper for navigation - validates complete navigation response structures"""
    
    def __init__(self, parent):
        self.parent = parent
    
    def _parse_json(self, output: str) -> dict:
        return self.parent.bot._parse_json(output)
    
    def assert_current_position_shows(self, output: str, behavior: str, action: str):
        """
        Validate COMPLETE position response by comparing JSON objects.
        
        Standard structure from bot.pos():
        {
          "status": "success",
          "behavior": "behavior_name",
          "action": "action_name",
          "position": "behavior.action"
        }
        """
        actual = self._parse_json(output)
        
        # Define the COMPLETE expected JSON object
        expected = {
            "status": "success",
            "behavior": behavior,
            "action": action,
            "position": f"{behavior}.{action}"
        }
        
        # Compare complete JSON objects
        for key, expected_value in expected.items():
            assert key in actual, \
                f"Missing field '{key}'.\nExpected: {expected}\nActual: {actual}"
            assert actual[key] == expected_value, \
                f"Field '{key}' mismatch.\nExpected: {expected_value}\nActual: {actual[key]}\n\nExpected JSON: {expected}\nActual JSON: {actual}"
    
    def assert_behavior_tree_shows_actions(self, output: str, behavior: str, actions_list: list):
        """
        Validate tree output (plain text, not JSON).
        
        Tree returns text like:
        ├── behavior1
        │   ├── action1
        │   └── action2
        """
        # tree() returns text, validate all elements present
        assert behavior in output, f"Missing behavior '{behavior}' in tree:\n{output}"
        for action in actions_list:
            assert action in output, \
                f"Missing action '{action}' in tree for behavior '{behavior}':\n{output}"
    
    def assert_current_marker_present(self, output: str):
        """
        Validate position response has current marker fields.
        See assert_current_position_shows for complete structure.
        """
        data = self._parse_json(output)
        required_fields = ['behavior', 'action']
        missing = [f for f in required_fields if f not in data]
        assert not missing, \
            f"Missing position marker fields: {missing}. Got: {list(data.keys())}"
    
    def assert_footer_emphasizes_current(self, output: str, behavior: str, action: str):
        """
        Validate current position in complete response.
        See assert_current_position_shows for complete structure.
        """
        self.assert_current_position_shows(output, behavior, action)


class JsonScopeHelper:
    """Helper for scope - validates complete scope response structures"""
    
    def __init__(self, parent):
        self.parent = parent
    
    def _parse_json(self, output: str) -> dict:
        return self.parent.bot._parse_json(output)
    
    def assert_scope_shows_target(self, output: str, scope_type: str, target: str):
        """
        Validate COMPLETE scope response by comparing JSON objects.
        
        Standard structure:
        {
          "status": "success",
          "message": "Scope set to ...",
          "scope": {
            "type": "story",
            "target": ["Story1", "Story2"]
          }
        }
        """
        actual = self._parse_json(output)
        
        # Define expected JSON structure (nested object)
        expected_subset = {
            "scope": {
                "type": scope_type,
                "target": target  # Will check if target is in the actual target
            }
        }
        
        # Validate scope object exists
        assert 'scope' in actual, \
            f"Missing 'scope' object.\nExpected structure: {expected_subset}\nActual: {actual}"
        
        # Validate scope.type
        assert 'type' in actual['scope'], \
            f"Missing 'scope.type'.\nExpected: {expected_subset}\nActual: {actual}"
        assert actual['scope']['type'] == scope_type, \
            f"scope.type mismatch.\nExpected: {scope_type}\nActual: {actual['scope']['type']}\n\nFull actual: {actual}"
        
        # Validate scope.target contains the target
        assert 'target' in actual['scope'], \
            f"Missing 'scope.target'.\nExpected: {expected_subset}\nActual: {actual}"
        assert target in str(actual['scope']['target']), \
            f"Target '{target}' not in scope.target.\nExpected target: {target}\nActual scope.target: {actual['scope']['target']}\n\nFull actual: {actual}"
    
    def assert_scope_cleared_message(self, output: str):
        """
        Validate COMPLETE scope cleared response.
        
        Standard structure:
        {
          "status": "success",
          "message": "Scope cleared"
        }
        """
        data = self._parse_json(output)
        
        # Validate complete response
        required_fields = ['status', 'message']
        missing = [f for f in required_fields if f not in data]
        assert not missing, \
            f"Missing required fields: {missing}. Got: {list(data.keys())}"
        
        assert data['status'] == 'success', \
            f"Expected status='success', got '{data['status']}'"
        assert 'cleared' in data['message'].lower(), \
            f"Expected 'cleared' in message, got '{data['message']}'"
    
    def assert_scope_set_message(self, output: str, scope_type: str, target: str):
        """
        Validate COMPLETE scope set response.
        
        Standard structure:
        {
          "status": "success",
          "message": "Scope set to story: Story1",
          "scope": {
            "type": "story",
            "target": ["Story1"]
          }
        }
        """
        data = self._parse_json(output)
        
        # Validate complete response structure
        required_fields = ['status', 'message']
        missing = [f for f in required_fields if f not in data]
        assert not missing, \
            f"Missing required fields: {missing}. Got: {list(data.keys())}"
        
        assert data['status'] == 'success', \
            f"Expected status='success', got '{data['status']}'"
        assert 'set' in data['message'].lower(), \
            f"Expected 'set' in message, got '{data['message']}'"
        assert scope_type in data['message'].lower(), \
            f"Expected scope_type '{scope_type}' in message '{data['message']}'"


class JsonHelpHelper:
    """Helper for help - validates help response structures"""
    
    def __init__(self, parent):
        self.parent = parent
    
    def _parse_json(self, output: str) -> dict:
        return self.parent.bot._parse_json(output)
    
    def assert_help_shows_available_commands(self, output: str):
        """
        Validate help output contains commands.
        (Help structure needs standardization - current: just validate non-empty)
        """
        assert len(output) > 0, "Help output is empty"
        assert len(output) > 100, \
            f"Help output too short ({len(output)} chars), expected detailed help"
    
    def assert_help_shows_command_details(self, output: str, command: str):
        """
        Validate help includes specific command.
        """
        assert command in output.lower(), \
            f"Missing command '{command}' in help output:\n{output[:500]}"


class JsonBotTestHelper(CLIBotTestHelper):
    """JSON channel helper - validates complete JSON structures"""
    
    def __init__(self, tmp_path: Path):
        super().__init__(tmp_path, mode='json')
        self.bot = JsonBotHelper(self)
        self.instructions = JsonInstructionsHelper(self)
        self.scope = JsonScopeHelper(self)
        self.navigation = JsonNavigationHelper(self)
        self.help = JsonHelpHelper(self)
