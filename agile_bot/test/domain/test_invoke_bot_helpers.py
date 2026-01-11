"""
Common Test Helpers for Invoke Bot Tests

Provides BotTestHelper class for bot setup and testing.
"""
import json
from pathlib import Path

from agile_bot.src.bot.bot import Bot
from agile_bot.test.domain.test_helpers import bootstrap_env


class BotTestHelper:
    """
    Test helper that provides production story_bot and workspace.
    
    Usage:
        helper = BotTestHelper(tmp_path)
        helper.set_state('shape', 'clarify')
        helper.assert_at_behavior_action('shape', 'clarify')
    """
    
    def __init__(self, tmp_path: Path):
        """Initialize with production story_bot and temp workspace."""
        # Get the actual story_bot directory (always the same)
        repo_root = Path(__file__).parent.parent.parent.parent
        self.bot_directory = repo_root / 'agile_bot' / 'bots' / 'story_bot'
        
        # Create temp workspace directory for state files
        self.workspace = tmp_path / 'workspace'
        self.workspace.mkdir(parents=True, exist_ok=True)

        # Bootstrap environment
        bootstrap_env(self.bot_directory, self.workspace)
        
        # Load the actual bot (always story_bot with all behaviors)
        config_path = self.bot_directory / 'bot_config.json'
        if not config_path.exists():
            config_path = self.bot_directory / 'config' / 'bot_config.json'
        
        self.bot = Bot(
            bot_name='story_bot',
            bot_directory=self.bot_directory,
            config_path=config_path
        )
    

    def set_state(self, behavior: str, action: str, completed_actions: list = None):
        """Set bot state to specific behavior/action."""
        from datetime import datetime
        
        state_data = {
            'current_behavior': f'story_bot.{behavior}',
            'current_action': f'story_bot.{behavior}.{action}',
            'operation': 'instructions',
            'working_directory': str(self.workspace),
            'timestamp': datetime.now().isoformat()
        }
        
        if completed_actions:
            state_data['completed_actions'] = [
                {'action_state': action_state, 'timestamp': datetime.now().isoformat()}
                for action_state in completed_actions
            ]
        
        state_file = self.workspace / 'behavior_action_state.json'
        state_file.write_text(json.dumps(state_data, indent=2), encoding='utf-8')
        return state_file
    
    def get_state(self) -> dict:
        """Read current bot state from workspace."""
        state_file = self.workspace / 'behavior_action_state.json'
        if not state_file.exists():
            return {}
        return json.loads(state_file.read_text(encoding='utf-8'))
    
    def add_completed(self, action_state: str):
        """Add action to completed list."""
        from datetime import datetime
        
        state = self.get_state()
        if 'completed_actions' not in state:
            state['completed_actions'] = []
        
        if not any(a.get('action_state') == action_state for a in state['completed_actions']):
            state['completed_actions'].append({
                'action_state': action_state,
                'timestamp': datetime.now().isoformat()
            })
        
        state_file = self.workspace / 'behavior_action_state.json'
        state_file.write_text(json.dumps(state, indent=2), encoding='utf-8')
    
    def clear_state(self):
        """Clear/delete behavior_action_state.json file."""
        state_file = self.workspace / 'behavior_action_state.json'
        if state_file.exists():
            state_file.unlink()
    
    # ========================================================================
    # Test Data Creation Methods
    # ========================================================================
    
    def create_story_graph(self, graph_data: dict) -> Path:
        """Create test story-graph.json in workspace."""
        docs_dir = self.workspace / 'docs' / 'stories'
        docs_dir.mkdir(parents=True, exist_ok=True)
        
        story_graph_file = docs_dir / 'story-graph.json'
        story_graph_file.write_text(json.dumps(graph_data, indent=2), encoding='utf-8')
        return story_graph_file
    
    def get_activity_log(self) -> list:
        """Read and parse activity_log.json."""
        activity_log_file = self.workspace / 'activity_log.json'
        if not activity_log_file.exists():
            return []
        return json.loads(activity_log_file.read_text(encoding='utf-8'))

    def sample_story_graph(self) -> dict:
        """Return a reusable sample story graph for scope filtering tests (matches legacy shape)."""
        return {
            'epics': [
                {
                    'name': 'Epic A',
                    'sub_epics': [
                        {
                            'name': 'Sub-Epic A1',
                            'story_groups': [
                                {
                                    'type': 'and',
                                    'connector': None,
                                    'stories': [
                                        {'name': 'Story A1'},
                                        {'name': 'Story A2'}
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    'name': 'Epic B',
                    'sub_epics': [
                        {
                            'name': 'Sub-Epic B1',
                            'story_groups': [
                                {
                                    'type': 'and',
                                    'connector': None,
                                    'stories': [
                                        {'name': 'Story B1'},
                                        {'name': 'Story B2'}
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ],
            'increments': [
                {
                    'name': 'Increment 1',
                    'priority': 1,
                    'epics': [
                        {
                            'name': 'Epic A',
                            'sub_epics': [
                                {
                                    'name': 'Sub-epic A1',
                                    'stories': [
                                        {'name': 'Story A1'},
                                        {'name': 'Story A2'}
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    'name': 'Increment 2',
                    'priority': 2,
                    'epics': [
                        {
                            'name': 'Epic B',
                            'sub_epics': [
                                {
                                    'name': 'Sub-epic B1',
                                    'stories': [
                                        {'name': 'Story B1'},
                                        {'name': 'Story B2'}
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }

    def filter_story_graph(self, scope_kind: str, scope_type: str, scope_value=None, behavior_name: str = None, story_graph: dict = None):
        """Filter a story graph using build/validate/action scopes without standalone helpers."""
        graph = story_graph or self.sample_story_graph()
        parameters = {'scope': {'type': scope_type}}
        if scope_value is not None:
            parameters['scope']['value'] = scope_value

        if scope_kind == 'build':
            from agile_bot.src.actions.build.build_scope import BuildScope
            return BuildScope(parameters, self.bot.bot_paths).filter_story_graph(graph)
        if scope_kind == 'validate':
            from agile_bot.src.actions.validate.validation_scope import ValidationScope
            return ValidationScope(parameters, self.bot.bot_paths, behavior_name).filter_story_graph(graph)
        if scope_kind in {'action', 'render'}:
            from agile_bot.src.scope.action_scope import ActionScope
            return ActionScope(parameters, self.bot.bot_paths).filter_story_graph(graph)

        raise ValueError(f"Unsupported scope_kind '{scope_kind}'")
    
    # ========================================================================
    # Assertion Methods
    # ========================================================================
    
    def assert_at_behavior_action(self, behavior_name: str, action_name: str):
        """Assert bot is at specified behavior and action."""
        assert self.bot.behaviors.current.name == behavior_name
        assert self.bot.behaviors.current.actions.current_action_name == action_name
    
    def assert_state_shows(self, behavior: str, action: str):
        """Assert state file shows expected behavior and action."""
        state = self.get_state()
        assert state['current_behavior'] == f'story_bot.{behavior}'
        assert state['current_action'].startswith(f'story_bot.{behavior}.{action}')
    
    def assert_action_completed(self, action_state: str):
        """Assert action appears in completed_actions list."""
        state = self.get_state()
        completed = [a.get('action_state') for a in state.get('completed_actions', [])]
        assert action_state in completed, f"Action {action_state} not in completed list: {completed}"
    
    def assert_action_not_completed(self, action_state: str):
        """Assert action does NOT appear in completed_actions list."""
        state = self.get_state()
        completed = [a.get('action_state') for a in state.get('completed_actions', [])]
        assert action_state not in completed, f"Action {action_state} should not be in completed list"
    
    def assert_scope_is_set(self, scope_type: str, scope_value: list):
        """Assert bot scope is set with specified type and value."""
        assert self.bot.scope.type == scope_type
        assert self.bot.scope.value == scope_value
        assert self.bot.scope.is_active()
    
    def assert_scope_is_cleared(self):
        """Assert bot scope is cleared (not active)."""
        assert not self.bot.scope.is_active()
        assert self.bot.scope.type is None
    
    def assert_activity_logged(self, action_state: str, event_type: str):
        """Assert action is logged in activity log with specified event type."""
        activity_log = self.get_activity_log()
        matching_entries = [
            entry for entry in activity_log
            if entry.get('action_state') == action_state 
            and entry.get('event') == event_type
        ]
        assert len(matching_entries) > 0, \
            f"No {event_type} event found for {action_state} in activity log"
    
    def assert_bot_result_success(self, result: dict, behavior: str, action: str):
        """
        Assert bot execute result has complete success structure.
        
        Validates EVERY field in the result, not just checking one word.
        """
        # Assert all required keys exist
        assert 'status' in result, "Missing 'status' key in result"
        assert 'message' in result, "Missing 'message' key in result"
        assert 'behavior' in result, "Missing 'behavior' key in result"
        assert 'action' in result, "Missing 'action' key in result"
        assert 'result' in result, "Missing 'result' key in result"
        
        # Assert exact values
        assert result['status'] == 'success', \
            f"Expected status='success', got '{result['status']}'"
        
        assert result['behavior'] == behavior, \
            f"Expected behavior='{behavior}', got '{result['behavior']}'"
        
        assert result['action'] == action, \
            f"Expected action='{action}', got '{result['action']}'"
        
        assert result['message'] == f'Executed {behavior}.{action}', \
            f"Expected message='Executed {behavior}.{action}', got '{result['message']}'"
        
        assert result['result'] == 'Action execution complete', \
            f"Expected result='Action execution complete', got '{result['result']}'"
    
    def assert_bot_result_error_behavior_not_found(self, result: dict, behavior: str):
        """Assert bot execute result shows behavior not found error."""
        assert result['status'] == 'error', f"Expected status='error', got '{result['status']}'"
        assert result['message'] == f'Behavior not found: {behavior}', \
            f"Expected message='Behavior not found: {behavior}', got '{result['message']}'"
        assert 'available_behaviors' in result, "Missing 'available_behaviors' key"
        assert isinstance(result['available_behaviors'], list), \
            "available_behaviors should be a list"
    
    def assert_bot_result_error_action_not_found(self, result: dict, action: str):
        """Assert bot execute result shows action not found error."""
        assert result['status'] == 'error', f"Expected status='error', got '{result['status']}'"
        assert result['message'] == f'Action not found: {action}', \
            f"Expected message='Action not found: {action}', got '{result['message']}'"
        assert 'available_actions' in result, "Missing 'available_actions' key"
        assert isinstance(result['available_actions'], list), \
            "available_actions should be a list"
    
    def assert_bot_result_error_no_actions(self, result: dict, behavior: str):
        """Assert bot execute result shows no actions error."""
        assert result['status'] == 'error', f"Expected status='error', got '{result['status']}'"
        assert result['message'] == f'Behavior {behavior} has no actions', \
            f"Expected message='Behavior {behavior} has no actions', got '{result['message']}'"
    
    def assert_shape_behavior_structure(self):
        """
        Assert shape behavior is loaded with correct complete structure.
        
        Shape has exactly 5 actions in specific order with specific configurations.
        """
        shape = self.bot.behaviors.find_by_name('shape')
        assert shape is not None, "Shape behavior not found"
        assert shape.name == 'shape'
        assert shape.order == 1
        assert shape.description == "Create a story map that captures the user's journey through epics, features, and stories"
        
        # Assert exact action count and names
        action_names = shape.actions.names
        assert len(action_names) == 5, f"Expected 5 actions, got {len(action_names)}: {action_names}"
        assert action_names == ['clarify', 'strategy', 'build', 'validate', 'render'], \
            f"Expected ['clarify', 'strategy', 'build', 'validate', 'render'], got {action_names}"
    
    def assert_discovery_behavior_structure(self):
        """
        Assert discovery behavior is loaded with correct complete structure.
        
        Discovery has exactly 5 actions in specific order.
        """
        discovery = self.bot.behaviors.find_by_name('discovery')
        assert discovery is not None, "Discovery behavior not found"
        assert discovery.name == 'discovery'
        assert discovery.order == 3
        
        # Assert exact action count and names
        action_names = discovery.actions.names
        assert len(action_names) == 5, f"Expected 5 actions, got {len(action_names)}: {action_names}"
        assert action_names == ['clarify', 'strategy', 'build', 'validate', 'render'], \
            f"Expected ['clarify', 'strategy', 'build', 'validate', 'render'], got {action_names}"
    
    def assert_current_behavior_and_action(self, behavior: str, action: str):
        """
        Assert bot is at specific behavior and action - comprehensive check.
        
        Checks both bot's current state AND state file for consistency.
        """
        # Check bot's in-memory state
        assert self.bot.behaviors.current is not None, "No current behavior set"
        assert self.bot.behaviors.current.name == behavior, \
            f"Expected current behavior '{behavior}', got '{self.bot.behaviors.current.name}'"
        
        assert self.bot.behaviors.current.actions.current is not None, "No current action set"
        assert self.bot.behaviors.current.actions.current.action_name == action, \
            f"Expected current action '{action}', got '{self.bot.behaviors.current.actions.current.action_name}'"
        
        # Check state file matches
        state = self.get_state()
        if state:  # Only check if state file exists
            assert state['current_behavior'] == f'story_bot.{behavior}', \
                f"State file current_behavior mismatch: expected 'story_bot.{behavior}', got '{state['current_behavior']}'"
            assert f'story_bot.{behavior}.{action}' in state['current_action'], \
                f"State file current_action mismatch: expected to contain 'story_bot.{behavior}.{action}', got '{state['current_action']}'"