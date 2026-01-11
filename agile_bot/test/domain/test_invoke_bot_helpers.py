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
    
    # ========================================================================
    # State Manipulation Methods
    # ========================================================================
    
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
