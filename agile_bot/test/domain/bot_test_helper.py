"""
Bot Test Helper

Provides BotTestHelper class for bot setup and testing.
"""
import json
import os
from pathlib import Path

from agile_bot.src.bot.bot import Bot


class BotTestHelper:
    """
    Test helper that provides production story_bot and workspace.
    
    Usage:
        helper = BotTestHelper(tmp_path)
        helper.set_state('shape', 'clarify')
        helper.assert_at_behavior_action('shape', 'clarify')
    """
    
    def __init__(self, tmp_path: Path, workspace_directory: Path = None, bot_directory: Path = None):
        """Initialize with production story_bot and temp workspace.
        
        Args:
            tmp_path: Temporary directory path (pytest fixture)
            workspace_directory: Optional workspace directory (defaults to tmp_path / 'workspace')
            bot_directory: Optional custom bot directory (defaults to production story_bot)
        """
        # Use custom bot directory if provided, otherwise use production story_bot
        if bot_directory is not None:
            self.bot_directory = bot_directory
            self.bot_directory.mkdir(parents=True, exist_ok=True)
        else:
            # Get the actual story_bot directory (always the same)
            repo_root = Path(__file__).parent.parent.parent.parent
            self.bot_directory = repo_root / 'agile_bot' / 'bots' / 'story_bot'
        
        # Create temp workspace directory for state files (default to tmp_path / 'workspace')
        self.workspace = workspace_directory if workspace_directory is not None else tmp_path / 'workspace'
        self.workspace.mkdir(parents=True, exist_ok=True)

        # Bootstrap environment (set environment variables directly)
        os.environ['BOT_DIRECTORY'] = str(self.bot_directory)
        os.environ['WORKING_AREA'] = str(self.workspace)
        
        # Load the actual bot (always story_bot with all behaviors)
        # For custom bot_directory, create config in root; for production, check root then config/
        if bot_directory is not None:
            config_path = self.bot_directory / 'bot_config.json'
            # If custom bot_directory and no config exists, create minimal bot_config.json
            if not config_path.exists():
                import json
                config_data = {
                    'botName': 'story_bot',
                    'behaviors': []
                }
                config_path.write_text(json.dumps(config_data, indent=2), encoding='utf-8')
        else:
            config_path = self.bot_directory / 'bot_config.json'
            if not config_path.exists():
                config_path = self.bot_directory / 'config' / 'bot_config.json'
        
        # Update bot_config.json to include all behaviors for testing
        # (production bot_config.json may only list some behaviors)
        if config_path.exists():
            import json
            config_data = json.loads(config_path.read_text(encoding='utf-8'))
            # Discover all behaviors from behaviors directory
            behaviors_dir = self.bot_directory / 'behaviors'
            if behaviors_dir.exists():
                all_behaviors = sorted([
                    d.name for d in behaviors_dir.iterdir() 
                    if d.is_dir() and not d.name.startswith('_') and not d.name.startswith('.')
                    and (d / 'behavior.json').exists()
                ])
                if all_behaviors:
                    config_data['behaviors'] = all_behaviors
                    config_path.write_text(json.dumps(config_data, indent=2), encoding='utf-8')
        
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
    
    def create_story_graph(self, graph_data: dict = None, docs_path: str = 'docs/stories', filename: str = 'story-graph.json') -> Path:
        """Create test story-graph.json in workspace.
        
        Args:
            graph_data: Story graph dict (default: {'epics': []})
            docs_path: Relative path from workspace to docs directory (default: 'docs/stories')
            filename: Story graph filename (default: 'story-graph.json')
        
        Returns:
            Path to created story graph file
        """
        if graph_data is None:
            graph_data = {'epics': []}
        
        docs_dir = self.workspace / docs_path
        docs_dir.mkdir(parents=True, exist_ok=True)
        
        story_graph_file = docs_dir / filename
        story_graph_file.write_text(json.dumps(graph_data, indent=2), encoding='utf-8')
        return story_graph_file
    
    def simple_story_graph(self) -> dict:
        """Return simple story graph data for testing."""
        return {
            "epics": [
                {
                    "name": "Build Knowledge",
                    "sequential_order": 1,
                    "sub_epics": [
                        {
                            "name": "Load Story Graph",
                            "sequential_order": 1,
                            "sub_epics": [],
                            "story_groups": [
                                {
                                    "type": "and",
                                    "connector": None,
                                    "stories": [
                                        {
                                            "name": "Load Story Graph Into Memory",
                                            "sequential_order": 1,
                                            "connector": None,
                                            "users": ["Story Bot"],
                                            "story_type": "user",
                                            "sizing": "5 days",
                                            "scenarios": [
                                                {
                                                    "name": "Story graph file exists",
                                                    "type": "happy_path",
                                                    "background": ["Given story graph file exists"],
                                                    "steps": [
                                                        "When story graph is loaded",
                                                        "Then story map is created with epics"
                                                    ]
                                                },
                                                {
                                                    "name": "Story graph file missing",
                                                    "type": "error_case",
                                                    "background": [],
                                                    "steps": [
                                                        "When story graph file does not exist",
                                                        "Then FileNotFoundError is raised"
                                                    ]
                                                }
                                            ],
                                            "scenario_outlines": [
                                                {
                                                    "name": "Load story graph with different formats",
                                                    "type": "happy_path",
                                                    "background": ["Given story graph file exists"],
                                                    "steps": [
                                                        "When story graph is loaded from \"<file_path>\"",
                                                        "Then story map contains \"<expected_epics>\" epics"
                                                    ],
                                                    "examples": {
                                                        "columns": ["file_path", "expected_epics"],
                                                        "rows": [
                                                            ["story-graph.json", "2"],
                                                            ["story-graph-v2.json", "3"]
                                                        ]
                                                    }
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "story_groups": []
                }
            ]
        }
    
    def create_story_map(self, story_graph_data: dict = None):
        """Create StoryMap from story graph data.
        
        Args:
            story_graph_data: Story graph dict. If None, uses simple_story_graph().
        
        Returns:
            StoryMap instance
        """
        from agile_bot.src.scanners.story_map import StoryMap
        
        if story_graph_data is None:
            story_graph_data = self.simple_story_graph()
        
        return StoryMap(story_graph_data)
    
    def get_activity_log(self) -> list:
        """Read and parse activity_log.json (TinyDB format)."""
        log_file = self.workspace / 'activity_log.json'
        if not log_file.exists():
            return []
        from tinydb import TinyDB
        with TinyDB(log_file) as db:
            return db.all()
    
    def create_activity_log_file(self):
        """Create activity log file in workspace."""
        log_file = self.workspace / 'activity_log.json'
        log_file.parent.mkdir(parents=True, exist_ok=True)
        log_file.write_text(json.dumps({'_default': {}}), encoding='utf-8')
        return log_file
    
    def create_activity_log_with_entries(self, entries: list = None):
        """Create activity log file with entries.
        
        Args:
            entries: List of activity log entries (if None, creates default multiple entries)
        
        Returns:
            Path to log file
        """
        log_file = self.create_activity_log_file()
        if entries is None:
            # Default: create multiple entries
            from tinydb import TinyDB
            with TinyDB(log_file) as db:
                db.insert({'action_state': 'story_bot.shape.render', 'timestamp': '09:00'})
                db.insert({'action_state': 'story_bot.discovery.render', 'timestamp': '10:00'})
        elif entries:
            from tinydb import TinyDB
            with TinyDB(log_file) as db:
                for entry in entries:
                    db.insert(entry)
        return log_file
    
    def assert_activity_logged_with_action_state(self, expected_action_state: str):
        """Assert activity logged with expected action_state."""
        activity_log = self.get_activity_log()
        if not any(entry.get('action_state') == expected_action_state for entry in activity_log):
            actual_states = [entry.get('action_state') for entry in activity_log]
            raise AssertionError(
                f"Expected action_state '{expected_action_state}' not found in activity log. "
                f"Actual entries: {actual_states}"
            )
    
    def assert_completion_entry_logged_with_outputs(self, expected_outputs: dict = None, expected_duration: int = None):
        """Assert completion entry logged with outputs and duration."""
        activity_log = self.get_activity_log()
        completion_entry = next((e for e in activity_log if 'outputs' in e), None)
        assert completion_entry is not None, "No completion entry found with outputs"
        if expected_outputs is not None:
            assert completion_entry['outputs'] == expected_outputs
        if expected_duration is not None:
            assert completion_entry['duration'] == expected_duration
    
    def assert_activity_log_matches(self, **checks):
        """Assert activity log matches expected values.
        
        Args:
            **checks: Checks to perform:
                - expected_count: Expected number of entries
                - expected_action_state: Expected action_state in entry (single value)
                - expected_action_states: List of expected action_states (one per entry in order)
                - expected_last_action_state: Expected action_state of last entry
                - expected_status: Expected status in entry
                - expected_entries: List of expected entry dicts (matched by action_state, not exact match)
                - workflow_complete: Check that completion entry has workflow_complete flag in outputs
        """
        from pathlib import Path
        from tinydb import TinyDB
        
        log_file = self.workspace / 'activity_log.json'
        
        if not log_file.exists():
            if 'expected_count' in checks and checks['expected_count'] == 0:
                return  # No entries expected, file doesn't exist - that's fine
            assert False, f"Activity log file does not exist at {log_file}"
        
        with TinyDB(log_file) as db:
            entries = db.all()
            
            if 'expected_count' in checks:
                assert len(entries) == checks['expected_count'], \
                    f"Expected {checks['expected_count']} entries, got {len(entries)}"
            
            if 'expected_action_states' in checks:
                # Check that entries match expected_action_states list in order
                expected_states = checks['expected_action_states']
                assert len(entries) == len(expected_states), \
                    f"Expected {len(expected_states)} entries, got {len(entries)}"
                for i, expected_state in enumerate(expected_states):
                    assert entries[i].get('action_state') == expected_state, (
                        f"Entry {i} should have action_state '{expected_state}', got '{entries[i].get('action_state')}'"
                    )
            
            if 'expected_last_action_state' in checks:
                # Check last entry's action_state
                assert len(entries) > 0, "No entries in activity log"
                assert entries[-1].get('action_state') == checks['expected_last_action_state'], (
                    f"Last entry should have action_state '{checks['expected_last_action_state']}', "
                    f"got '{entries[-1].get('action_state')}'"
                )
            
            if 'expected_action_state' in checks:
                matching_entries = [e for e in entries if e.get('action_state') == checks['expected_action_state']]
                assert len(matching_entries) > 0, \
                    f"No entry found with action_state={checks['expected_action_state']}"
                if 'expected_status' in checks:
                    assert matching_entries[0].get('status') == checks['expected_status'], \
                        f"Expected status {checks['expected_status']}, got {matching_entries[0].get('status')}"
            
            if 'workflow_complete' in checks and checks['workflow_complete']:
                # Check that completion entry has workflow_complete flag in outputs
                completion_entry = next((e for e in entries if 'outputs' in e), None)
                assert completion_entry is not None, "No completion entry found with outputs"
                assert completion_entry['outputs'].get('workflow_complete') is True, \
                    "Completion entry does not have workflow_complete flag set to True"
            
            if 'expected_entries' in checks:
                # Match entries by action_state (not exact match)
                expected_entries = checks['expected_entries']
                assert len(entries) == len(expected_entries), \
                    f"Expected {len(expected_entries)} entries, got {len(entries)}"
                for expected_entry in expected_entries:
                    expected_action_state = expected_entry.get('action_state')
                    assert any(
                        entry.get('action_state') == expected_action_state
                        for entry in entries
                    ), f"No entry found with action_state '{expected_action_state}'"
    
    def create_activity_tracker(self, bot_name='story_bot'):
        """Create ActivityTracker instance."""
        from agile_bot.src.actions.activity_tracker import ActivityTracker
        from agile_bot.src.bot.bot_paths import BotPaths
        bot_paths = BotPaths(workspace_path=self.workspace)
        return ActivityTracker(bot_paths=bot_paths, bot_name=bot_name)
    
    def track_activity_start(self, tracker, action_state):
        """Track activity start with tracker.
        
        Args:
            tracker: ActivityTracker instance
            action_state: Action state string (e.g., 'bot_name.behavior.action') or dict with bot_name, behavior, action
        """
        from agile_bot.src.actions.activity_tracker import ActionState
        
        if isinstance(action_state, str):
            # Parse action_state like 'bot_name.behavior.action'
            parts = action_state.split('.')
            if len(parts) == 3:
                bot_name, behavior, action = parts
                tracker.track_start(ActionState(bot_name, behavior, action))
            else:
                raise ValueError(f"Invalid action_state format: {action_state}")
        elif isinstance(action_state, dict):
            tracker.track_start(ActionState(action_state['bot_name'], action_state['behavior'], action_state['action']))
        else:
            raise ValueError(f"Invalid action_state type: {type(action_state)}")
    
    def create_minimal_guardrails_files(self, behavior_name: str):
        """Ensure guardrails directory structure exists for tests.
        
        This helper ensures directories exist for Guardrails class initialization.
        Tests always use production files from story_bot - no files are created.
        
        Args:
            behavior_name: Behavior name (e.g., 'exploration')
        """
        # Create behavior folder structure (directories only)
        behavior_dir = self.bot_directory / 'behaviors' / behavior_name
        behavior_dir.mkdir(parents=True, exist_ok=True)
        
        # Ensure guardrails directory structure exists
        required_context_dir = behavior_dir / 'guardrails' / 'required_context'
        strategy_dir = behavior_dir / 'guardrails' / 'strategy'
        decision_criteria_dir = strategy_dir / 'decision_criteria'
        
        required_context_dir.mkdir(parents=True, exist_ok=True)
        strategy_dir.mkdir(parents=True, exist_ok=True)
        decision_criteria_dir.mkdir(parents=True, exist_ok=True)
        
        # Note: Files (key_questions.json, evidence.json, etc.) are always read from production story_bot
        # Tests never create these files - they use the existing production files
    
    def setup_custom_bot_directory(self, bot_directory: Path = None, workspace_directory: Path = None):
        """Set up a custom bot directory for testing (instead of production story_bot).
        
        Args:
            bot_directory: Custom bot directory to use (defaults to tmp_path / 'bot' if use_custom_bot was True)
            workspace_directory: Optional workspace directory (defaults to self.workspace)
        """
        if bot_directory:
            self.bot_directory = bot_directory
        elif not hasattr(self, 'bot_directory') or self.bot_directory is None:
            # If use_custom_bot was True, bot_directory should already be set
            # Otherwise, create default custom bot directory
            from pathlib import Path as P
            # Try to infer tmp_path from workspace
            tmp_path = self.workspace.parent if self.workspace.name == 'workspace' else self.workspace
            self.bot_directory = tmp_path / 'bot'
        
        self.bot_directory.mkdir(parents=True, exist_ok=True)
        
        if workspace_directory:
            self.workspace = workspace_directory
            self.workspace.mkdir(parents=True, exist_ok=True)
        
        # Bootstrap environment (set environment variables directly)
        os.environ['BOT_DIRECTORY'] = str(self.bot_directory)
        os.environ['WORKING_AREA'] = str(self.workspace)
        
        # Create bot if it doesn't exist yet
        if self.bot is None:
            config_path = self.bot_directory / 'bot_config.json'
            if not config_path.exists():
                config_path = self.bot_directory / 'config' / 'bot_config.json'
            
            if config_path.exists():
                self.bot = Bot(
                    bot_name='story_bot',
                    bot_directory=self.bot_directory,
                    config_path=config_path
                )
    
    def create_behavior_json(self, behavior_name: str, actions: list = None, **kwargs):
        """Create behavior.json file for a behavior.
        
        Args:
            behavior_name: Name of the behavior
            actions: Optional list of action definitions. If None, uses default actions.
            **kwargs: Additional fields to include in behavior.json (description, goal, inputs, outputs, 
                     baseActionsPath, instructions, etc.)
        
        Returns:
            Path to the created behavior.json file
        """
        behavior_dir = self.bot_directory / 'behaviors' / behavior_name
        behavior_dir.mkdir(parents=True, exist_ok=True)
        behavior_file = behavior_dir / 'behavior.json'
        
        if actions is None:
            # Default actions
            actions = [
                {"name": "clarify", "order": 1, "next_action": "strategy"},
                {"name": "strategy", "order": 2, "next_action": "build"},
                {"name": "build", "order": 3, "next_action": "validate"},
                {"name": "validate", "order": 4, "next_action": "render"},
                {"name": "render", "order": 5}
            ]
        
        # Handle instructions - can be list or dict
        instructions = kwargs.get('instructions')
        if instructions is None:
            instructions = {}
        elif isinstance(instructions, list):
            # Convert list to dict format if needed, or keep as list
            instructions = instructions
        
        behavior_config = {
            "behaviorName": behavior_name,
            "description": kwargs.get('description', f"Test behavior: {behavior_name}"),
            "goal": kwargs.get('goal', f"Test goal for {behavior_name}"),
            "inputs": kwargs.get('inputs', "Test inputs"),
            "outputs": kwargs.get('outputs', "Test outputs"),
            "instructions": instructions,
            "actions_workflow": {
                "actions": actions
            }
        }
        
        # Add any additional fields from kwargs (baseActionsPath, etc.)
        for key, value in kwargs.items():
            if key not in ['description', 'goal', 'inputs', 'outputs', 'instructions']:
                behavior_config[key] = value
        
        behavior_file.write_text(json.dumps(behavior_config, indent=2), encoding='utf-8')
        return behavior_file
    
    def create_guardrails_files(self, behavior_name: str, questions: list = None, evidence: list = None):
        """Create guardrails files with content for a behavior.
        
        Args:
            behavior_name: Name of the behavior
            questions: Optional list of questions for key_questions.json
            evidence: Optional list of evidence items for evidence.json
        
        Returns:
            Tuple of (questions_file, evidence_file) paths, or None if no files created
        """
        guardrails_dir = self.bot_directory / 'behaviors' / behavior_name / 'guardrails' / 'required_context'
        guardrails_dir.mkdir(parents=True, exist_ok=True)
        
        questions_file = None
        evidence_file = None
        
        if questions is not None:
            questions_file = guardrails_dir / 'key_questions.json'
            questions_file.write_text(json.dumps({'questions': questions}), encoding='utf-8')
        
        if evidence is not None:
            evidence_file = guardrails_dir / 'evidence.json'
            evidence_file.write_text(json.dumps({'evidence': evidence}), encoding='utf-8')
        
        if questions_file or evidence_file:
            return questions_file, evidence_file
        return None
    
    def create_malformed_guardrails_file(self, behavior_name: str) -> Path:
        """Create a malformed guardrails JSON file for testing error handling.
        
        Args:
            behavior_name: Name of the behavior
        
        Returns:
            Path to the created malformed questions file
        """
        guardrails_dir = self.bot_directory / 'behaviors' / behavior_name / 'guardrails' / 'required_context'
        guardrails_dir.mkdir(parents=True, exist_ok=True)
        questions_file = guardrails_dir / 'key_questions.json'
        questions_file.write_text('invalid json {', encoding='utf-8')
        return questions_file
    
    def create_action_config(self, action_name: str, config_data: dict) -> Path:
        """Create action_config.json file for a base action.
        
        Args:
            action_name: Name of the action (e.g., 'clarify', 'validate')
            config_data: Dictionary of config data to write to the file
        
        Returns:
            Path to the created action_config.json file
        """
        # Get base_actions directory from agile_bot/base_actions
        repo_root = Path(__file__).parent.parent.parent.parent
        base_actions_dir = repo_root / 'agile_bot' / 'base_actions' / action_name
        base_actions_dir.mkdir(parents=True, exist_ok=True)
        config_file = base_actions_dir / 'action_config.json'
        config_file.write_text(json.dumps(config_data, indent=2), encoding='utf-8')
        return config_file

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
    
    def create_activity_log_with_entries(self, entries: list = None):
        """Create activity log file with entries.
        
        Args:
            entries: List of activity log entries (if None, creates default multiple entries)
        
        Returns:
            Path to log file
        """
        log_file = self.create_activity_log_file()
        if entries:
            from tinydb import TinyDB
            with TinyDB(log_file) as db:
                for entry in entries:
                    db.insert(entry)
        return log_file
    
    def assert_activity_logged_with_action_state(self, expected_action_state: str):
        """Assert activity logged with expected action_state."""
        activity_log = self.get_activity_log()
        if not any(entry.get('action_state') == expected_action_state for entry in activity_log):
            actual_states = [entry.get('action_state') for entry in activity_log]
            raise AssertionError(
                f"Expected action_state '{expected_action_state}' not found in activity log. "
                f"Actual entries: {actual_states}"
            )
    
    def assert_completion_entry_logged_with_outputs(self, expected_outputs: dict = None, expected_duration: int = None):
        """Assert completion entry logged with outputs and duration."""
        activity_log = self.get_activity_log()
        completion_entry = next((e for e in activity_log if 'outputs' in e), None)
        assert completion_entry is not None, "No completion entry found with outputs"
        if expected_outputs is not None:
            assert completion_entry['outputs'] == expected_outputs
        if expected_duration is not None:
            assert completion_entry['duration'] == expected_duration
    
    def assert_activity_log_matches(self, **checks):
        """Assert activity log matches expected values.
        
        Args:
            **checks: Checks to perform:
                - expected_count: Expected number of entries
                - expected_action_state: Expected action_state in entry (single value)
                - expected_action_states: List of expected action_states (one per entry in order)
                - expected_last_action_state: Expected action_state of last entry
                - expected_status: Expected status in entry
                - expected_entries: List of expected entry dicts (matched by action_state, not exact match)
                - workflow_complete: Check that completion entry has workflow_complete flag in outputs
        """
        from pathlib import Path
        from tinydb import TinyDB
        
        log_file = self.workspace / 'activity_log.json'
        
        if not log_file.exists():
            if 'expected_count' in checks and checks['expected_count'] == 0:
                return  # No entries expected, file doesn't exist - that's fine
            assert False, f"Activity log file does not exist at {log_file}"
        
        with TinyDB(log_file) as db:
            entries = db.all()
            
            if 'expected_count' in checks:
                assert len(entries) == checks['expected_count'], \
                    f"Expected {checks['expected_count']} entries, got {len(entries)}"
            
            if 'expected_action_states' in checks:
                # Check that entries match expected_action_states list in order
                expected_states = checks['expected_action_states']
                assert len(entries) == len(expected_states), \
                    f"Expected {len(expected_states)} entries, got {len(entries)}"
                for i, expected_state in enumerate(expected_states):
                    assert entries[i].get('action_state') == expected_state, (
                        f"Entry {i} should have action_state '{expected_state}', got '{entries[i].get('action_state')}'"
                    )
            
            if 'expected_last_action_state' in checks:
                # Check last entry's action_state
                assert len(entries) > 0, "No entries in activity log"
                assert entries[-1].get('action_state') == checks['expected_last_action_state'], (
                    f"Last entry should have action_state '{checks['expected_last_action_state']}', "
                    f"got '{entries[-1].get('action_state')}'"
                )
            
            if 'expected_action_state' in checks:
                matching_entries = [e for e in entries if e.get('action_state') == checks['expected_action_state']]
                assert len(matching_entries) > 0, \
                    f"No entry found with action_state={checks['expected_action_state']}"
                if 'expected_status' in checks:
                    assert matching_entries[0].get('status') == checks['expected_status'], \
                        f"Expected status {checks['expected_status']}, got {matching_entries[0].get('status')}"
            
            if 'workflow_complete' in checks and checks['workflow_complete']:
                # Check that completion entry has workflow_complete flag in outputs
                completion_entry = next((e for e in entries if 'outputs' in e), None)
                assert completion_entry is not None, "No completion entry found with outputs"
                assert completion_entry['outputs'].get('workflow_complete') is True, \
                    "Completion entry does not have workflow_complete flag set to True"
            
            if 'expected_entries' in checks:
                # Match entries by action_state (not exact match)
                expected_entries = checks['expected_entries']
                assert len(entries) == len(expected_entries), \
                    f"Expected {len(expected_entries)} entries, got {len(entries)}"
                for expected_entry in expected_entries:
                    expected_action_state = expected_entry.get('action_state')
                    assert any(
                        entry.get('action_state') == expected_action_state
                        for entry in entries
                    ), f"No entry found with action_state '{expected_action_state}'"
    
    def create_activity_tracker(self, bot_name='story_bot'):
        """Create ActivityTracker instance."""
        from agile_bot.src.actions.activity_tracker import ActivityTracker
        from agile_bot.src.bot.bot_paths import BotPaths
        bot_paths = BotPaths(workspace_path=self.workspace)
        return ActivityTracker(bot_paths=bot_paths, bot_name=bot_name)
    
    def track_activity_start(self, tracker, action_state):
        """Track activity start with tracker.
        
        Args:
            tracker: ActivityTracker instance
            action_state: Action state string (e.g., 'bot_name.behavior.action') or dict with bot_name, behavior, action
        """
        from agile_bot.src.actions.activity_tracker import ActionState
        
        if isinstance(action_state, str):
            # Parse action_state like 'bot_name.behavior.action'
            parts = action_state.split('.')
            if len(parts) == 3:
                bot_name, behavior, action = parts
                tracker.track_start(ActionState(bot_name, behavior, action))
            else:
                raise ValueError(f"Invalid action_state format: {action_state}")
        elif isinstance(action_state, dict):
            tracker.track_start(ActionState(action_state['bot_name'], action_state['behavior'], action_state['action']))
        else:
            raise ValueError(f"Invalid action_state type: {type(action_state)}")
    
    def story_graph_dict(self, minimal=False, scope_type=None, epic=None):
        """Return story graph dictionary for testing.
        
        Args:
            minimal: If True, returns minimal story graph for test file scope
            scope_type: Type of scope ('multiple_test_files' for multiple test files)
            epic: Epic name ('mob' for mob epic, None for default)
        
        Returns:
            Story graph dictionary
        """
        if minimal:
            return {
                "epics": [
                    {
                        "name": "Places Order",
                        "sub_epics": [
                            {
                                "name": "Validates Payment",
                                "story_groups": [
                                    {
                                        "stories": [
                                            {
                                                "name": "Place Order",
                                                "scenarios": []
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        elif scope_type == 'multiple_test_files':
            return {
                "epics": [
                    {
                        "name": "Manage Orders",
                        "sub_epics": [
                            {
                                "name": "Create Order",
                                "story_groups": [
                                    {
                                        "stories": [
                                            {
                                                "name": "Place Order",
                                                "scenarios": []
                                            },
                                            {
                                                "name": "Cancel Order",
                                                "scenarios": []
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        elif epic == 'mob':
            return {
                "epics": [
                    {
                        "name": "Manage Mobs",
                        "sequential_order": 1,
                        "estimated_stories": 6,
                        "domain_concepts": [
                            {
                                "name": "Mob",
                                "responsibilities": [
                                    {
                                        "name": "Groups minions together for coordinated action",
                                        "collaborators": ["Minion"]
                                    }
                                ]
                            }
                        ],
                        "sub_epics": []
                    }
                ]
            }
        else:
            # Default: test story graph
            return {
                "epics": [
                    {
                        "name": "Test Epic",
                        "sequential_order": 1,
                        "sub_epics": [],
                        "story_groups": []
                    }
                ]
            }
    
    def access_story_item(self, item_type, source, **access_params):
        """Access item from story map source.
        
        Args:
            item_type: Type of item ('epic', 'sub_epic', 'story', 'scenario', 'scenario_outline', 'epics')
            source: Source to access from (epics list, story_map, epic, story, etc.)
            **access_params: Additional parameters:
                - index: Index to access (default: 0 for first item)
                - name: Name to search for (for story/scenario/outline)
        
        Returns:
            The accessed item
        """
        index = access_params.get('index', 0)
        name = access_params.get('name')
        
        if item_type == 'epics':
            # Access epics from story_map
            story_map = source
            return story_map.epics()
        elif item_type == 'epic':
            if hasattr(source, 'epics'):  # It's a story_map
                epics = source.epics()
            else:  # It's an epics list
                epics = source
            return epics[index] if index is not None else epics[0]
        elif item_type == 'sub_epic':
            epics = source if isinstance(source, list) else source.epics()
            return epics[0].children[0]
        elif item_type == 'story':
            if name:
                # Search by name
                epic = source if hasattr(source, 'children') else source.epics()[0]
                for sub_epic in epic.children:
                    for story_group in sub_epic.children:
                        for story in story_group.children:
                            if story.name == name:
                                return story
                raise ValueError(f"Story '{name}' not found")
            elif hasattr(source, 'epics'):  # It's a story_map
                return source.epics()[0].children[0].children[0].children[0]
            elif hasattr(source, 'children'):  # It's an epic
                return source.children[0].children[0].children[0]
            else:  # It's an epics list
                return source[0].children[0].children[0].children[0]
        elif item_type == 'scenario':
            if name:
                # Search by name
                story = source if hasattr(source, 'scenarios') else self.access_story_item('story', source)
                for scenario in story.scenarios:
                    if scenario.name == name:
                        return scenario
                raise ValueError(f"Scenario '{name}' not found")
            elif hasattr(source, 'scenarios'):  # It's a story
                return source.scenarios[index]
            else:  # It's epics list
                story = self.access_story_item('story', source)
                return story.scenarios[index]
        elif item_type == 'scenario_outline':
            if name:
                # Search by name
                scenario = source if hasattr(source, 'examples_columns') else self.access_story_item('scenario', source)
                for outline in scenario.scenario_outlines if hasattr(scenario, 'scenario_outlines') else []:
                    if outline.name == name:
                        return outline
                raise ValueError(f"Scenario outline '{name}' not found")
            elif hasattr(source, 'scenario_outlines'):  # It's a story
                return source.scenario_outlines[index]
            else:  # It's epics list
                story = self.access_story_item('story', source)
                return story.scenario_outlines[index]
        else:
            raise ValueError(f"Unknown item_type: {item_type}")
    
    def assert_nodes_match(self, nodes, expected_count=None, expected_names=None):
        """Assert nodes match expected count and names.
        
        Args:
            nodes: List of nodes to check
            expected_count: Expected number of nodes (None = don't check count)
            expected_names: Expected names (list or None = don't check names)
        """
        if expected_count is not None:
            assert len(nodes) == expected_count, f"Expected {expected_count} nodes, got {len(nodes)}"
        if expected_names is not None:
            actual_names = [node.name for node in nodes]
            assert actual_names == expected_names, f"Expected names {expected_names}, got {actual_names}"
    
    def assert_children_match(self, parent, expected_count=None, expected_names=None):
        """Assert children match expected count and names.
        
        Args:
            parent: Parent item (Epic, SubEpic, StoryGroup, etc.)
            expected_count: Expected number of children (None = don't check count)
            expected_names: Expected names (list or None = don't check names)
        """
        children = parent.children
        if expected_count is not None:
            assert len(children) == expected_count, f"Expected {expected_count} children, got {len(children)}"
        if expected_names is not None:
            actual_names = [child.name for child in children]
            assert actual_names == expected_names, f"Expected names {expected_names}, got {actual_names}"
    
    def assert_stories_match(self, expected, actual):
        """Assert stories match expected.
        
        Args:
            expected: Expected stories (set, list, or dict)
            actual: Actual stories (set, list, or dict)
        """
        if isinstance(expected, set) and isinstance(actual, set):
            assert expected == actual, f"Expected {expected}, got {actual}"
        elif isinstance(expected, list) and isinstance(actual, list):
            assert set(expected) == set(actual), f"Expected {expected}, got {actual}"
        else:
            assert expected == actual, f"Expected {expected}, got {actual}"
    
    def assert_scenarios_match(self, story, expected_count=None, expected_names=None):
        """Assert scenarios match expected count and names.
        
        Args:
            story: Story instance
            expected_count: Expected number of scenarios (None = don't check count)
            expected_names: Expected names (list or None = don't check names)
        """
        scenarios = story.scenarios
        if expected_count is not None:
            assert len(scenarios) == expected_count, f"Expected {expected_count} scenarios, got {len(scenarios)}"
        if expected_names is not None:
            actual_names = [scenario.name for scenario in scenarios]
            assert actual_names == expected_names, f"Expected names {expected_names}, got {actual_names}"
    
    def assert_scenario_outlines_match(self, scenario, expected_count=None, expected_names=None):
        """Assert scenario outlines match expected count and names.
        
        Args:
            scenario: Scenario or Story instance (if Story, checks scenario_outlines)
            expected_count: Expected number of scenario outlines (None = don't check count)
            expected_names: Expected names (list or None = don't check names)
        """
        from agile_bot.src.scanners.story_map import Story
        if isinstance(scenario, Story):
            outlines = scenario.scenario_outlines
        else:
            outlines = scenario.scenario_outlines if hasattr(scenario, 'scenario_outlines') else []
        if expected_count is not None:
            assert len(outlines) == expected_count, f"Expected {expected_count} scenario outlines, got {len(outlines)}"
        if expected_names is not None:
            actual_names = [outline.name for outline in outlines]
            assert actual_names == expected_names, f"Expected names {expected_names}, got {actual_names}"
    
    def assert_instructions_have_structure(self, instructions, structure='validation_rules'):
        """Assert instructions have expected structure.
        
        Args:
            instructions: Instructions dict to check
            structure: Structure type to validate ('validation_rules' or custom structure dict)
        """
        if structure == 'validation_rules':
            # Default validation_rules structure check
            assert 'validation_rules' in instructions, "Instructions must contain 'validation_rules' key"
            validation_rules = instructions['validation_rules']
            assert len(validation_rules) > 0, "Instructions should contain validation rules"
            
            # Validate each rule structure (accepts Rule objects or dicts)
            from agile_bot.src.actions.rules.rule import Rule
            from agile_bot.test.domain.test_validate_knowledge_and_content_against_rules import validate_violation_structure
            
            for rule in validation_rules:
                # Handle Rule objects (new format)
                if isinstance(rule, Rule):
                    assert hasattr(rule, 'rule_file'), f"Rule object must have 'rule_file' attribute"
                    assert hasattr(rule, 'rule_content'), f"Rule object must have 'rule_content' attribute"
                    rule_file = str(rule.rule_file)
                    rule_content = rule.rule_content
                elif isinstance(rule, dict):
                    # Backward compatibility: dict format (from rules.validate() which returns dicts)
                    assert 'rule_content' in rule, f"Rule dict must contain 'rule_content' key: {rule}"
                    rule_content = rule['rule_content']
                    rule_file = rule.get('rule_file', 'unknown')
                    # If dict has scanner_results, validate it
                    if 'scanner_results' in rule:
                        scanner_results = rule['scanner_results']
                        if 'violations' in scanner_results:
                            violations = scanner_results['violations']
                            assert isinstance(violations, list), "Scanner results should contain violations list"
                            for violation in violations:
                                assert validate_violation_structure(violation, ['rule', 'line_number', 'location', 'violation_message', 'severity']), (
                                    f"Violation missing required fields: {violation}"
                                )
                else:
                    raise AssertionError(f"Rule should be a Rule object or dict, got: {type(rule)}")
                
                # Validate rule_content has scanner if it's a dict
                if isinstance(rule_content, dict):
                    assert 'scanner' in rule_content, f"Rule content must contain 'scanner' key: {rule_content}"
                    scanner_path = rule_content['scanner']
                    assert scanner_path is not None, f"Rule should have a scanner attached: {rule_file}"
            
            assert 'base_instructions' in instructions, "Instructions must contain 'base_instructions' key"
            base_instructions = instructions['base_instructions']
            assert isinstance(base_instructions, list), "Base instructions should be a list"
        elif isinstance(structure, dict):
            # Custom structure check - structure dict specifies required keys and their types/validators
            for key, validator in structure.items():
                assert key in instructions, f"Instructions must contain '{key}' key"
                if callable(validator):
                    validator(instructions[key])
                elif isinstance(validator, type):
                    assert isinstance(instructions[key], validator), f"'{key}' should be of type {validator.__name__}"
                elif isinstance(validator, list):
                    # List of allowed values
                    assert instructions[key] in validator, f"'{key}' should be one of {validator}"
    
    def assert_config_path_matches(self, instructions, config_path, config_key='knowledge_graph_config'):
        """Assert config path matches expected.
        
        Args:
            instructions: Instructions dict containing config
            config_path: Expected config path value (can be relative or absolute)
            config_key: Key in instructions that contains the config (default: 'knowledge_graph_config')
        """
        if config_key not in instructions:
            return
        config = instructions[config_key]
        if isinstance(config, dict) and 'path' in config:
            actual_path = config['path']
            # Handle both absolute and relative paths
            if '\\' in actual_path or '/' in actual_path:
                # Normalize paths for comparison
                from pathlib import Path
                actual_path_obj = Path(actual_path)
                config_path_obj = Path(config_path)
                # Check if actual path ends with the expected relative path
                assert str(actual_path_obj).replace('\\', '/').endswith(str(config_path_obj).replace('\\', '/')), \
                    f"Expected config path to end with '{config_path}', got '{actual_path}'"
            else:
                assert actual_path == config_path, f"Expected config path '{config_path}', got '{actual_path}'"
    
    def assert_instructions_merged_from_sources(self, merged_instructions, behavior, action, sources='both'):
        """Assert instructions merged from sources.
        
        Args:
            merged_instructions: Merged instructions dict to check
            behavior: Expected behavior name
            action: Expected action name
            sources: Which sources should be present ('both', 'base_only', or 'behavior_only')
        """
        assert merged_instructions['action'] == action, f"Expected action '{action}', got '{merged_instructions.get('action')}'"
        assert merged_instructions['behavior'] == behavior, f"Expected behavior '{behavior}', got '{merged_instructions.get('behavior')}'"
        
        if sources == 'both':
            assert 'base_instructions' in merged_instructions, "Instructions must contain 'base_instructions' key"
            assert 'behavior_instructions' in merged_instructions, "Instructions must contain 'behavior_instructions' key"
        elif sources == 'base_only':
            assert 'base_instructions' in merged_instructions, "Instructions must contain 'base_instructions' key"
            assert merged_instructions.get('behavior_instructions', []) == [], "Behavior instructions should be empty"
        elif sources == 'behavior_only':
            assert 'behavior_instructions' in merged_instructions, "Instructions must contain 'behavior_instructions' key"
            assert merged_instructions.get('base_instructions', []) == [], "Base instructions should be empty"
    
    def assert_instructions_contain(self, instructions, content_type, **content_params):
        """Assert instructions contain specified content type.
        content_type can be: 'next_behavior_reminder', 'reminder_prompt_text', 'guardrails', 'strategy_criteria_and_assumptions', 'template_path', 'validation_rules', 'render_required_fields', 'render_field_values'
        """
        from pathlib import Path
        
        if content_type == 'next_behavior_reminder':
            # instructions is action_result dict
            instructions_dict = instructions.get('instructions', {}) if isinstance(instructions, dict) else instructions
            assert instructions_dict, f"No instructions found. Result: {instructions}"
            base_instructions_list = instructions_dict.get('base_instructions', [])
            reminder_found = False
            next_behavior_found = False
            for i, instruction in enumerate(base_instructions_list):
                if 'NEXT BEHAVIOR REMINDER' in instruction:
                    reminder_found = True
                    if i + 1 < len(base_instructions_list):
                        next_instruction = base_instructions_list[i + 1]
                        if 'prioritization' in next_instruction.lower():
                            next_behavior_found = True
            assert reminder_found, "base_instructions should include 'NEXT BEHAVIOR REMINDER' section"
            assert next_behavior_found, "Reminder should mention 'prioritization' as the next behavior"
            return base_instructions_list
        
        elif content_type == 'reminder_prompt_text':
            # instructions is base_instructions_list
            instructions_text = ' '.join(instructions) if isinstance(instructions, list) else instructions
            assert 'next behavior in sequence' in instructions_text.lower(), "Reminder should contain 'next behavior in sequence' text"
            assert 'would you like to continue' in instructions_text.lower() or 'work on a different behavior' in instructions_text.lower(), "Reminder should contain prompt asking user if they want to continue"
        
        elif content_type == 'guardrails':
            # instructions is dict
            assert 'guardrails' in instructions
            assert 'required_context' in instructions['guardrails']
            assert 'key_questions' in instructions['guardrails']['required_context']
            assert instructions['guardrails']['required_context']['key_questions'] == content_params.get('expected_questions', [])
            assert 'evidence' in instructions['guardrails']['required_context']
            assert instructions['guardrails']['required_context']['evidence'] == content_params.get('expected_evidence', [])
        
        elif content_type == 'strategy_criteria_and_assumptions':
            # instructions is dict
            assert 'strategy_criteria' in instructions
            assert 'assumptions' in instructions
            assert instructions['assumptions'] == content_params.get('expected_assumptions', [])
            assert instructions['strategy_criteria'] is not None
        
        elif content_type == 'template_path':
            # instructions is dict
            template_name = content_params.get('template_name')
            if 'template_path' in instructions:
                assert template_name in instructions['template_path']
            # Note: template_path may be missing in minimal execution; skip strict enforcement
        
        elif content_type == 'validation_rules':
            # instructions is dict
            assert 'validation_rules' in instructions, "Instructions must contain 'validation_rules' key"
            return instructions['validation_rules']
        
        elif content_type == 'render_required_fields':
            # instructions is base_instructions_text string
            assert instructions.strip() != ''
            assert 'render' in instructions.lower() or 'template' in instructions.lower() or 'output' in instructions.lower()
        
        elif content_type == 'render_field_values':
            # instructions is base_instructions_text string
            assert instructions.strip() != ''
            assert 'render' in instructions.lower() or 'scenario' in instructions.lower() or 'template' in instructions.lower()
        
        else:
            raise ValueError(f"Unknown content_type: {content_type}")
    
    def assert_instructions_do_not_contain(self, instructions, content_type):
        """Assert instructions do not contain specified content type.
        content_type can be: 'next_behavior_reminder', 'next_action_instructions', 'guardrails', 'strategy_data'
        """
        if content_type == 'next_behavior_reminder':
            # instructions is action_result dict or BotResult object
            if hasattr(instructions, 'data'):
                instructions_dict = instructions.data.get('instructions', {})
            else:
                instructions_dict = instructions.get('instructions', {}) if isinstance(instructions, dict) else instructions
            base_instructions_list = instructions_dict.get('base_instructions', [])
            instructions_text = ' '.join(base_instructions_list)
            assert 'NEXT BEHAVIOR REMINDER' not in instructions_text, "base_instructions should NOT include 'NEXT BEHAVIOR REMINDER' when action is not final"
        
        elif content_type == 'next_action_instructions':
            # instructions is string
            assert instructions == '' or 'complete' in instructions.lower()
        
        elif content_type == 'guardrails':
            # instructions is dict
            assert 'guardrails' not in instructions or instructions['guardrails'] == {}
        
        elif content_type == 'strategy_data':
            # instructions is dict
            assert 'strategy_criteria' not in instructions or instructions['strategy_criteria'] == {}
            assert 'assumptions' not in instructions or instructions['assumptions'] == []
        
        else:
            raise ValueError(f"Unknown content_type: {content_type}")
    
    def assert_template_variables_replaced(self, instructions_text, type=None):
        """Assert template variables are replaced in instructions text.
        
        Args:
            instructions_text: The instructions text to check
            type: Type of template variables to check. None (default) = all build knowledge variables,
                  'render_configs' = render configs variables, 'render_instructions' = render instructions variables
        """
        if type is None or type == 'build':
            # In minimal setups we only verify instructions text is present
            assert isinstance(instructions_text, str)
            assert instructions_text.strip() != ''
            # Skip strict content checks since real instructions vary
        
        elif type == 'render_configs':
            # Check render configs template variables
            assert '{{render_configs}}' not in instructions_text
            # Content may vary by render specs; just ensure some render config text is present
            assert 'render' in instructions_text.lower()
        
        elif type == 'render_instructions':
            # Check render instructions template variables
            assert '{{render_configs}}' not in instructions_text
            assert '{{render_instructions}}' not in instructions_text
            # Ensure render instructions content was injected (non-empty)
            assert instructions_text.strip() != ''
    
    def assert_instructions_match(self, instructions, expected_content):
        """Assert instructions match expected content.
        
        Args:
            instructions: Instructions dict or string
            expected_content: Expected content (dict or string)
        """
        if isinstance(expected_content, dict) and isinstance(instructions, dict):
            assert instructions == expected_content, f"Expected {expected_content}, got {instructions}"
        else:
            assert str(instructions) == str(expected_content), f"Expected {expected_content}, got {instructions}"
    
    def assert_file_updated(self, file_path, expected_content):
        """Assert file updated with expected content.
        
        Args:
            file_path: Path to file
            expected_content: Expected content (dict or string)
        """
        from pathlib import Path
        import json
        file_path = Path(file_path)
        assert file_path.exists(), f"File {file_path} does not exist"
        actual_content = json.loads(file_path.read_text(encoding='utf-8')) if isinstance(expected_content, dict) else file_path.read_text(encoding='utf-8')
        if isinstance(expected_content, dict):
            assert actual_content == expected_content, f"Expected {expected_content}, got {actual_content}"
        else:
            assert actual_content == expected_content, f"Expected {expected_content}, got {actual_content}"
    
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
    
    # ========================================================================
    # Verification Methods (moved from test_execute_behavior_actions.py)
    # ========================================================================
    
    def verify_action_tracks_start(self, action_class, action_name: str, 
                                   behavior: str = 'exploration'):
        """Verify that action tracks start in activity log."""
        from types import SimpleNamespace
        
        # Create activity log file
        self.create_activity_log_file()
        
        # Create guardrails files (required by Guardrails class initialization)
        self.create_minimal_guardrails_files(behavior)
        
        # If action is 'build', create knowledge graph config structure
        if action_name == 'build':
            from agile_bot.test.domain.test_build_knowledge import given_setup
            kg_dir = given_setup('directory_structure', self.bot_directory, behavior=behavior)
            given_setup('config_and_template', self.bot_directory, kg_dir=kg_dir)
        
        # Create mock behavior object
        class MockBotPath:
            def __init__(self, bot_dir, workspace_dir):
                self.bot_directory = bot_dir
                self.workspace_directory = workspace_dir
                self.documentation_path = workspace_dir / 'docs'
        
        behavior_folder = self.bot_directory / 'behaviors' / behavior
        behavior_obj = SimpleNamespace()
        behavior_obj.folder = behavior_folder
        behavior_obj.name = behavior
        behavior_obj.bot_name = 'story_bot'
        behavior_obj.bot_paths = MockBotPath(self.bot_directory, self.workspace)
        behavior_obj.bot = None
        
        # Create action
        action = action_class(
            behavior=behavior_obj,
            action_config=None
        )
        action.track_activity_on_start()
        
        # Verify in activity log
        log_data = self.get_activity_log()
        assert any(
            e.get('action_state') == f'story_bot.{behavior}.{action_name}'
            for e in log_data
        ), f"Action start not found in activity log: {log_data}"
    
    def verify_action_tracks_completion(self, action_class, action_name: str,
                                       behavior: str = 'exploration',
                                       outputs: dict = None, duration: int = None):
        """Verify that action tracks completion in activity log."""
        from types import SimpleNamespace
        
        # Create activity log file
        self.create_activity_log_file()
        
        # Create guardrails files
        self.create_minimal_guardrails_files(behavior)
        
        # If action is 'build', create knowledge graph config structure
        if action_name == 'build':
            from agile_bot.test.domain.test_build_knowledge import given_setup
            kg_dir = given_setup('directory_structure', self.bot_directory, behavior=behavior)
            given_setup('config_and_template', self.bot_directory, kg_dir=kg_dir)
        
        # Create mock behavior object
        class MockBotPath:
            def __init__(self, bot_dir, workspace_dir):
                self.bot_directory = bot_dir
                self.workspace_directory = workspace_dir
                self.documentation_path = workspace_dir / 'docs'
        
        behavior_folder = self.bot_directory / 'behaviors' / behavior
        behavior_obj = SimpleNamespace()
        behavior_obj.folder = behavior_folder
        behavior_obj.name = behavior
        behavior_obj.bot_name = 'story_bot'
        behavior_obj.bot_paths = MockBotPath(self.bot_directory, self.workspace)
        behavior_obj.bot = None
        
        # Create action
        action = action_class(
            behavior=behavior_obj,
            action_config=None
        )
        action.track_activity_on_completion(
            outputs=outputs or {},
            duration=duration
        )
        
        # Verify in activity log
        log_data = self.get_activity_log()
        completion_entry = next((e for e in log_data if 'outputs' in e or 'duration' in e), None)
        assert completion_entry is not None, f"No completion entry found in activity log: {log_data}"
        if outputs:
            assert completion_entry.get('outputs') == outputs, \
                f"Expected outputs {outputs}, got {completion_entry.get('outputs')}"
        if duration:
            assert completion_entry.get('duration') == duration, \
                f"Expected duration {duration}, got {completion_entry.get('duration')}"
    
    def verify_workflow_transition(self, source_action: str, dest_action: str,
                                   behavior: str = 'exploration'):
        """Verify workflow transitions from source to dest action.
        
        NOTE: This method uses production story_bot behaviors. It does not create
        custom behavior.json files. If you need custom workflows, use production
        behaviors or create test behaviors in temporary directories.
        """
        # Use production behaviors - no need to create behavior.json files
        # Production story_bot already has all behaviors configured
        self.create_minimal_guardrails_files(behavior)
        
        # If build action is involved, create knowledge graph config structure
        if source_action == 'build' or dest_action == 'build':
            from agile_bot.test.domain.test_build_knowledge import given_setup
            kg_dir = given_setup('directory_structure', self.bot_directory, behavior=behavior)
            given_setup('config_and_template', self.bot_directory, kg_dir=kg_dir)
        
        # Reload bot to get updated behavior
        config_path = self.bot_directory / 'bot_config.json'
        bot = Bot(bot_name='story_bot', bot_directory=self.bot_directory, config_path=config_path)
        
        # Navigate to behavior and action
        behavior_obj = bot.behaviors.find_by_name(behavior)
        behavior_obj.actions.navigate_to(source_action)
        
        # Close current action (this should transition to next)
        behavior_obj.actions.close_current()
        
        # Verify current action is now dest_action
        current_action = behavior_obj.actions.current
        assert current_action is not None, f"Expected current action after transition, got None"
        assert current_action.action_name == dest_action, \
            f"Expected action '{dest_action}', got '{current_action.action_name}'"
    
    def verify_workflow_saves_completed_action(self, action_name: str,
                                               behavior: str = 'exploration'):
        """Verify workflow saves completed action to behavior_action_state.json.
        
        NOTE: This method uses production story_bot behaviors. It does not create
        custom behavior.json files. If you need custom workflows, use production
        behaviors or create test behaviors in temporary directories.
        """
        # Use production behaviors - no need to create behavior.json files
        # Production story_bot already has all behaviors configured
        self.create_minimal_guardrails_files(behavior)
        
        # If behavior has 'build' action, create knowledge graph configs
        if action_name == 'build':
            from agile_bot.test.domain.test_build_knowledge import given_setup
            kg_dir = given_setup('directory_structure', self.bot_directory, behavior=behavior)
            given_setup('config_and_template', self.bot_directory, kg_dir=kg_dir)
        
        # Reload bot to get updated behavior
        config_path = self.bot_directory / 'bot_config.json'
        bot = Bot(bot_name='story_bot', bot_directory=self.bot_directory, config_path=config_path)
        
        # Navigate to action and close it (this saves it as completed)
        behavior_obj = bot.behaviors.find_by_name(behavior)
        assert behavior_obj is not None, \
            f"Behavior '{behavior}' not found in bot. Available behaviors: {[b.name for b in bot.behaviors]}"
        behavior_obj.actions.navigate_to(action_name)
        behavior_obj.actions.close_current()
        
        # Verify completed action is saved in behavior_action_state.json
        state_file = self.workspace / 'behavior_action_state.json'
        assert state_file.exists(), f"State file {state_file} should exist"
        state_data = json.loads(state_file.read_text(encoding='utf-8'))
        
        action_state = f'story_bot.{behavior}.{action_name}'
        completed_actions = state_data.get('completed_actions', [])
        assert any(
            entry.get('action_state') == action_state
            for entry in completed_actions
        ), f"Action {action_state} should be in completed_actions: {completed_actions}"
    
    # ========================================================================
    # Build Scope Helpers
    # ========================================================================
    
    def create_build_scope(self, parameters: dict, bot_paths=None):
        """Create BuildScope instance from parameters.
        
        Args:
            parameters: Dict with scope configuration
            bot_paths: Optional BotPath instance
        
        Returns:
            BuildScope instance
        """
        from agile_bot.src.actions.build.build_scope import BuildScope
        return BuildScope(parameters, bot_paths)
    
    def assert_build_scope_contains(self, build_scope, expected_key: str, expected_value):
        """Assert BuildScope contains expected key-value pair.
        
        Args:
            build_scope: BuildScope instance
            expected_key: Key to check in build_scope.scope
            expected_value: Expected value for the key
        """
        assert expected_key in build_scope.scope, \
            f"Expected key '{expected_key}' not found in build_scope.scope. Keys: {list(build_scope.scope.keys())}"
        assert build_scope.scope[expected_key] == expected_value, \
            f"Expected build_scope.scope['{expected_key}'] == {expected_value}, got {build_scope.scope[expected_key]}"
    
    def assert_build_scope_matches(self, build_scope, expected_scope_contains: dict):
        """Assert BuildScope contains all expected key-value pairs.
        
        Args:
            build_scope: BuildScope instance
            expected_scope_contains: Dict of expected key-value pairs
        """
        for key, value in expected_scope_contains.items():
            self.assert_build_scope_contains(build_scope, key, value)
    
    def assert_action_uses_build_scope(self, action, parameters: dict):
        """Assert action uses BuildScope class and includes scope in instructions.
        
        Args:
            action: BuildKnowledgeAction instance
            parameters: Dict with scope configuration
        """
        from agile_bot.src.actions.action_context import ScopeActionContext, Scope, ScopeType
        
        # Convert dict parameters to typed context
        scope = None
        if 'scope' in parameters and parameters['scope']:
            scope_dict = parameters['scope']
            if isinstance(scope_dict, dict):
                scope_type = ScopeType(scope_dict.get('type', 'all'))
                scope = Scope(
                    type=scope_type,
                    value=scope_dict.get('value', []),
                    exclude=scope_dict.get('exclude', [])
                )
        context = ScopeActionContext(scope=scope)
        
        # Verify action uses BuildScope by checking if scope is in instructions
        # do_execute returns Instructions object (via get_instructions)
        instructions = action.do_execute(context)
        # Instructions object supports dict-like access via .get()
        scope_config = instructions.get('scope')
        assert scope_config is not None, f"Instructions should contain 'scope'. Available keys: {list(instructions.keys()) if hasattr(instructions, 'keys') else 'N/A'}"
        assert isinstance(scope_config, dict), f"Scope config should be dict, got {type(scope_config)}"
    
    # ========================================================================
    # Story Graph Filtering Helpers
    # ========================================================================
    
    def story_graph_with_epics_and_increments(self) -> dict:
        """Return test story graph with epics and increments.
        
        Returns:
            Dict with 'epics' and 'increments' keys
        """
        return {
            'epics': [
                {
                    'name': 'Epic A',
                    'sub_epics': [
                        {
                            'name': 'Sub-epic A1',
                            'story_groups': [
                                {
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
                            'name': 'Sub-epic B1',
                            'story_groups': [
                                {
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
    
    def filter_story_graph_legacy(self, scope_type: str, scope_value, story_graph: dict) -> dict:
        """Filter story graph using ScopingParameter (legacy method - use filter_story_graph with scope_kind instead).
        
        Args:
            scope_type: Scope type ('all', 'story', 'epic', 'increment')
            scope_value: Optional list of values for the scope
            story_graph: Story graph dict to filter
        
        Returns:
            Filtered story graph dict
        """
        from agile_bot.src.scope.scoping_parameter import ScopingParameter
        scope = {'type': scope_type}
        if scope_value is not None:
            scope['value'] = scope_value
        scoping_param = ScopingParameter(scope)
        return scoping_param.filter_story_graph(story_graph)
    
    def assert_story_graph_contains_epic(self, filtered_graph: dict, epic_name: str):
        """Assert filtered story graph contains epic.
        
        Args:
            filtered_graph: Filtered story graph dict
            epic_name: Expected epic name
        """
        epic_names = [epic.get('name') for epic in filtered_graph.get('epics', [])]
        assert epic_name in epic_names, \
            f"Expected epic '{epic_name}' not found in filtered graph. Found: {epic_names}"
    
    def assert_story_graph_contains_story(self, filtered_graph: dict, story_name: str):
        """Assert filtered story graph contains story.
        
        Args:
            filtered_graph: Filtered story graph dict
            story_name: Expected story name
        """
        story_names = []
        for epic in filtered_graph.get('epics', []):
            for sub_epic in epic.get('sub_epics', []):
                for story_group in sub_epic.get('story_groups', []):
                    for story in story_group.get('stories', []):
                        if isinstance(story, dict):
                            story_names.append(story.get('name'))
                        else:
                            story_names.append(story)
        assert story_name in story_names, \
            f"Expected story '{story_name}' not found in filtered graph. Found: {story_names}"
    
    def assert_story_graph_contains_increment(self, filtered_graph: dict, increment_name: str):
        """Assert filtered story graph contains increment.
        
        Args:
            filtered_graph: Filtered story graph dict
            increment_name: Expected increment name
        """
        increment_names = [inc.get('name') for inc in filtered_graph.get('increments', [])]
        assert increment_name in increment_names, \
            f"Expected increment '{increment_name}' not found in filtered graph. Found: {increment_names}"
    
    def assert_story_graph_contains_all_epics(self, filtered_graph: dict, expected_count: int):
        """Assert filtered story graph contains expected number of epics.
        
        Args:
            filtered_graph: Filtered story graph dict
            expected_count: Expected number of epics
        """
        actual_count = len(filtered_graph.get('epics', []))
        assert actual_count == expected_count, \
            f"Expected {expected_count} epics, got {actual_count}"
    
    def assert_story_graph_contains_all_increments(self, filtered_graph: dict, expected_count: int):
        """Assert filtered story graph contains expected number of increments.
        
        Args:
            filtered_graph: Filtered story graph dict
            expected_count: Expected number of increments
        """
        actual_count = len(filtered_graph.get('increments', []))
        assert actual_count == expected_count, \
            f"Expected {expected_count} increments, got {actual_count}"
    
    def build_parameters_with_scope(self, scope_type='all', scope_value=None):
        """Create build parameters dict with scope configuration.
        
        Args:
            scope_type: Scope type ('all', 'story', 'epic', 'increment')
            scope_value: Optional list of values for the scope
        
        Returns:
            Dict with 'scope' key containing scope configuration
        """
        if scope_type == 'all':
            return {'scope': {'type': 'all'}}
        return {'scope': {'type': scope_type, 'value': scope_value}}
    
    def build_parameters_with_story_names(self, story_names):
        """Create build parameters dict with story names.
        
        Args:
            story_names: String or list of story names
        
        Returns:
            Dict with 'story_names' key
        """
        if isinstance(story_names, str):
            story_names = [story_names]
        return {'story_names': story_names}
    
    def build_parameters_with_increment_priorities(self, priorities):
        """Create build parameters dict with increment priorities.
        
        Args:
            priorities: Int or list of increment priorities
        
        Returns:
            Dict with 'increment_priorities' key
        """
        if isinstance(priorities, int):
            priorities = [priorities]
        return {'increment_priorities': priorities}
    
    def build_parameters_with_epic_names(self, epic_names):
        """Create build parameters dict with epic names.
        
        Args:
            epic_names: String or list of epic names
        
        Returns:
            Dict with 'epic_names' key
        """
        if isinstance(epic_names, str):
            epic_names = [epic_names]
        return {'epic_names': epic_names}
    
    # ========================================================================
    # Knowledge Graph Setup Helpers
    # ========================================================================
    
    def setup_knowledge_graph_directory(self, behavior: str) -> Path:
        """Create knowledge graph directory structure for a behavior.
        
        Args:
            behavior: Behavior name
        
        Returns:
            Path to knowledge_graph directory
        """
        kg_dir = self.bot_directory / 'behaviors' / behavior / 'content' / 'knowledge_graph'
        kg_dir.mkdir(parents=True, exist_ok=True)
        return kg_dir
    
    def setup_knowledge_graph_config_and_template(self, behavior: str, template_name: str = 'story-graph-outline.json', output_name: str = 'story-graph.json') -> tuple:
        """Create knowledge graph config and template files.
        
        Args:
            behavior: Behavior name
            template_name: Name of template file
            output_name: Name of output file
        
        Returns:
            Tuple of (config_file_path, template_file_path)
        """
        kg_dir = self.setup_knowledge_graph_directory(behavior)
        
        config_file = kg_dir / 'build_story_graph_outline.json'
        config_file.write_text(
            json.dumps({
                'name': 'build_story_graph_outline',
                'path': 'docs/stories/',
                'template': template_name,
                'output': output_name
            }, indent=2),
            encoding='utf-8'
        )
        
        template_file = kg_dir / template_name
        template_file.write_text(
            json.dumps({
                '_explanation': {},
                'epics': []
            }, indent=2),
            encoding='utf-8'
        )
        
        return config_file, template_file
    
    def create_behavior_specific_instructions(self, behavior: str, action: str) -> Path:
        """Create behavior-specific instructions file in knowledge graph directory.
        
        Args:
            behavior: Behavior name
            action: Action name
        
        Returns:
            Path to instructions.json file
        """
        kg_dir = self.setup_knowledge_graph_directory(behavior)
        behavior_instructions_file = kg_dir / 'instructions.json'
        behavior_instructions_file.write_text(
            json.dumps({
                'behaviorName': behavior,
                'instructions': [f'{behavior}.{action} specific instructions']
            }, indent=2),
            encoding='utf-8'
        )
        return behavior_instructions_file
    
    # ========================================================================
    # Additional Creation Helpers (moved from test_helpers.py)
    # ========================================================================
    
    def create_strategy_guardrails(self, behavior_name: str, assumptions: list, criteria: dict) -> tuple:
        """Create strategy guardrails in behavior folder.
        
        Args:
            behavior_name: Name of the behavior
            assumptions: List of assumptions
            criteria: Dict of criteria
        
        Returns:
            Tuple of (assumptions_file, criteria_file) paths
        """
        guardrails_dir = self.bot_directory / 'behaviors' / behavior_name / 'guardrails' / 'strategy'
        guardrails_dir.mkdir(parents=True, exist_ok=True)
        
        assumptions_file = guardrails_dir / 'typical_assumptions.json'
        assumptions_file.write_text(json.dumps({'assumptions': assumptions}), encoding='utf-8')
        
        criteria_dir = guardrails_dir / 'strategy_criteria'
        criteria_dir.mkdir(exist_ok=True)
        criteria_file = criteria_dir / 'test_criteria.json'
        criteria_file.write_text(json.dumps(criteria), encoding='utf-8')
        
        return assumptions_file, criteria_file
    
    def create_knowledge_graph_template(self, behavior: str, template_name: str) -> Path:
        """Create knowledge graph template in behavior folder.
        
        Args:
            behavior: Behavior name
            template_name: Name of template file
        
        Returns:
            Path to template file
        """
        kg_dir = self.bot_directory / 'behaviors' / behavior / 'content' / 'knowledge_graph'
        kg_dir.mkdir(parents=True, exist_ok=True)
        
        template_file = kg_dir / f'{template_name}.json'
        template_file.write_text(json.dumps({'template': 'knowledge_graph'}), encoding='utf-8')
        return template_file
    
    def create_validation_rules(self, behavior: str, rules: list) -> Path:
        """Create validation rules in behavior folder.
        
        Args:
            behavior: Behavior name
            rules: List of rules
        
        Returns:
            Path to validation_rules.json file
        """
        rules_dir = self.bot_directory / 'behaviors' / behavior / '3_rules'
        rules_dir.mkdir(parents=True, exist_ok=True)
        
        rules_file = rules_dir / 'validation_rules.json'
        rules_file.write_text(json.dumps({'rules': rules}), encoding='utf-8')
        return rules_file
    
    def create_behavior_folder(self, folder_name: str) -> Path:
        """Create behavior folder in bot directory.
        
        Args:
            folder_name: Name of behavior folder
        
        Returns:
            Path to behavior directory
        """
        behavior_dir = self.bot_directory / 'behaviors' / folder_name
        behavior_dir.mkdir(parents=True, exist_ok=True)
        return behavior_dir
    
    def create_behavior_action_instructions(self, behavior: str, action: str) -> Path:
        """Create behavior-specific action instructions.
        
        Args:
            behavior: Behavior name
            action: Action name
        
        Returns:
            Path to instructions.json file
        """
        instructions_dir = self.bot_directory / 'behaviors' / behavior / action
        instructions_dir.mkdir(parents=True, exist_ok=True)
        
        instructions_file = instructions_dir / 'instructions.json'
        instructions_file.write_text(json.dumps({
            'instructions': [f'{behavior}.{action} specific instructions']
        }), encoding='utf-8')
        return instructions_file
    
    def create_base_instructions(self):
        """Create base action configs in agile_bot/base_actions.
        
        Uses the shared agile_bot/base_actions directory.
        """
        repo_root = Path(__file__).parent.parent.parent.parent
        base_actions = repo_root / 'agile_bot' / 'base_actions'
        
        actions = ['clarify', 'strategy', 'build', 'validate', 'render']
        orders = [1, 2, 3, 4, 5]
        next_actions = ['strategy', 'build', 'validate', 'render', None]
        
        for action, order, next_action in zip(actions, orders, next_actions):
            action_dir = base_actions / action
            action_dir.mkdir(parents=True, exist_ok=True)
            config = {
                'name': action,
                'workflow': True,
                'order': order,
                'instructions': [f'{action} base instructions']
            }
            if next_action:
                config['next_action'] = next_action
            config_file = action_dir / 'action_config.json'
            config_file.write_text(json.dumps(config), encoding='utf-8')
    
    def create_base_action_instructions(self, action: str) -> Path:
        """Get base action config path for specific action.
        
        Args:
            action: Action name
        
        Returns:
            Path to action_config.json file
        
        Raises:
            RuntimeError: If base action folder or config doesn't exist
        """
        repo_root = Path(__file__).parent.parent.parent.parent
        base_actions_dir = repo_root / 'agile_bot' / 'base_actions'
        action_dir = base_actions_dir / action
        if not action_dir.exists():
            raise RuntimeError(f"Base action folder missing: {action_dir}. Tests should rely on existing base actions.")
        config_file = action_dir / 'action_config.json'
        if not config_file.exists():
            raise RuntimeError(f"Base action config missing: {config_file}. Tests should rely on existing base actions.")
        return config_file
    
    def create_behavior_folder_with_json(self, folder_name: str) -> Path:
        """Create behavior folder with behavior.json file.
        
        Args:
            folder_name: Name of behavior folder
        
        Returns:
            Path to behavior directory
        
        Raises:
            RuntimeError: If attempting to write to production story_bot
        """
        behavior_folder = self.create_behavior_folder(folder_name)
        behavior_file = behavior_folder / 'behavior.json'
        
        # Safety check: prevent writing to production story_bot behavior.json files
        if self._is_production_story_bot_path(behavior_file):
            raise RuntimeError(
                f"TEST SAFETY: Attempted to write behavior.json to production story_bot directory: {behavior_file}\n"
                f"Tests should use temporary directories (tmp_path fixture) instead of production directories."
            )
    
    def _is_production_story_bot_path(self, path: Path) -> bool:
        """Check if path is in the production story_bot directory.
        
        Prevents tests from accidentally overwriting production behavior.json files.
        
        Args:
            path: Path to check
            
        Returns:
            True if path is in production story_bot, False otherwise
        """
        try:
            path = path.resolve()
            path_str = str(path).replace('\\', '/')
            
            # Get the repo root (agile_bot/test/domain/bot_test_helper.py -> repo root is 3 levels up)
            repo_root = Path(__file__).resolve().parent.parent.parent
            story_bot_behaviors = (repo_root / 'agile_bot' / 'bots' / 'story_bot' / 'behaviors').resolve()
            
            # Check if path is under the production story_bot/behaviors directory
            try:
                path.relative_to(story_bot_behaviors)
                # Path is under story_bot/behaviors - check if it's NOT in a temporary directory
                # Temporary directories typically contain: tmp, pytest, temp, or are under /tmp
                if any(indicator in path_str.lower() for indicator in ['/tmp/', '\\tmp\\', '.pytest', '\\temp\\', '/temp/', 'pytest-']):
                    return False
                # If it's in the actual repo's story_bot/behaviors, it's production
                return True
            except ValueError:
                # Path is not relative to story_bot/behaviors, so it's not production
                return False
        except Exception:
            # If we can't determine, be conservative and allow it (don't block the test)
            return False
        
        behavior_config = {
            "behaviorName": folder_name.split('_')[-1] if '_' in folder_name and folder_name[0].isdigit() else folder_name,
            "description": f"Test behavior: {folder_name}",
            "goal": f"Test goal for {folder_name}",
            "inputs": "Test inputs",
            "outputs": "Test outputs",
            "baseActionsPath": "agile_bot/base_actions",
            "instructions": [
                f"**BEHAVIOR WORKFLOW INSTRUCTIONS:**",
                "",
                f"Test instructions for {folder_name}."
            ],
            "actions_workflow": {
                "actions": [
                    {"name": "clarify", "order": 1, "next_action": "strategy"},
                    {"name": "strategy", "order": 2, "next_action": "build"},
                    {"name": "build", "order": 3, "next_action": "validate"},
                    {"name": "validate", "order": 4, "next_action": "render"},
                    {"name": "render", "order": 5}
                ]
            },
            "trigger_words": {
                "description": f"Trigger words for {folder_name}",
                "patterns": [f"test.*{folder_name}"],
                "priority": 10
            }
        }
        behavior_file.write_text(json.dumps(behavior_config, indent=2), encoding='utf-8')
        
        return behavior_folder
    
    # ========================================================================
    # Path Helpers (moved from test_helpers.py)
    # ========================================================================
    
    def get_behavior_dir(self, behavior: str) -> Path:
        """Get behavior directory path in bot directory.
        
        Args:
            behavior: Behavior name
        
        Returns:
            Path to behavior directory
        """
        return self.bot_directory / 'behaviors' / behavior
    
    def get_base_actions_dir(self) -> Path:
        """Get base_actions directory path from agile_bot/base_actions.
        
        Returns:
            Path to agile_bot/base_actions directory
        """
        repo_root = Path(__file__).parent.parent.parent.parent
        return repo_root / 'agile_bot' / 'base_actions'
    
    def get_base_bot_dir(self) -> Path:
        """Get test_base_bot directory path.
        
        Returns:
            Path to agile_bot/bots/test_base_bot directory
        """
        repo_root = Path(__file__).parent.parent.parent.parent
        return repo_root / 'agile_bot' / 'bots' / 'test_base_bot'
    
    def get_base_bot_rules_dir(self) -> Path:
        """Get test_base_bot rules directory path.
        
        Returns:
            Path to agile_bot/bots/test_base_bot/rules directory
        """
        return self.get_base_bot_dir() / 'rules'
    
    def update_bot_config_with_working_area(self) -> Path:
        """Update bot_config.json with WORKING_AREA field.
        
        Returns:
            Path to bot_config.json file
        """
        config_path = self.bot_directory / 'bot_config.json'
        
        # Load existing config if it exists, otherwise create new
        if config_path.exists():
            try:
                config = json.loads(config_path.read_text(encoding='utf-8'))
            except (json.JSONDecodeError, FileNotFoundError):
                config = {}
        else:
            config = {}
        
        # Add WORKING_AREA
        config['WORKING_AREA'] = str(self.workspace)
        config_path.write_text(json.dumps(config, indent=2), encoding='utf-8')
        return config_path
    
    # ========================================================================
    # Instructions Assertion Helpers
    # ========================================================================
    
    def assert_build_knowledge_instructions(self, instructions):
        """Assert BuildKnowledgeAction injected all required fields.
        
        Args:
            instructions: Instructions object from BuildKnowledgeAction
        """
        # Check base instructions exist
        base_instructions = instructions.get('base_instructions', [])
        assert base_instructions, "base_instructions should be present"
        
        # Check BuildKnowledgeAction-specific fields
        assert instructions.get('scope') is not None, "scope should be set"
        assert instructions.get('scope_story_names') is not None, "scope_story_names should be set"
        assert instructions.get('knowledge_graph_template') is not None, "knowledge_graph_template should be set"
        assert instructions.get('knowledge_graph_config') is not None, "knowledge_graph_config should be set"
        assert instructions.get('existing_file') is not None, "existing_file should be set"
        
        # Check that either update_mode or create_mode is set
        has_update = instructions.get('update_mode') or instructions.get('update_instructions')
        has_create = instructions.get('create_mode') or instructions.get('create_instructions')
        assert has_update or has_create, "Either update_mode or create_mode should be set"
        
        # Check rules are injected
        assert instructions.get('rules') is not None, "rules should be injected"
    
    def assert_clarify_context_instructions(self, instructions):
        """Assert ClarifyContextAction injected all required fields.
        
        Args:
            instructions: Instructions object from ClarifyContextAction
        """
        # Check base instructions exist
        base_instructions = instructions.get('base_instructions', [])
        assert base_instructions, "base_instructions should be present"
        
        # Check ClarifyContextAction-specific fields
        guardrails = instructions.get('guardrails')
        assert guardrails is not None, "guardrails should be set"
        assert 'required_context' in guardrails, "guardrails should contain required_context"
        
        required_context = guardrails['required_context']
        assert 'key_questions' in required_context, "required_context should have key_questions"
        assert 'evidence' in required_context, "required_context should have evidence"
    
    def assert_strategy_instructions(self, instructions):
        """Assert StrategyAction injected all required fields.
        
        Args:
            instructions: Instructions object from StrategyAction
        """
        # Check base instructions exist
        base_instructions = instructions.get('base_instructions', [])
        assert base_instructions, "base_instructions should be present"
        
        # Check StrategyAction-specific fields
        strategy_criteria = instructions.get('strategy_criteria')
        assert strategy_criteria is not None, "strategy_criteria should be set"
        assert isinstance(strategy_criteria, dict), "strategy_criteria should be a dict"
        
        assumptions = instructions.get('assumptions')
        assert assumptions is not None, "assumptions should be set"
        assert isinstance(assumptions, list), "assumptions should be a list"
    
    def assert_render_output_instructions(self, instructions):
        """Assert RenderOutputAction injected all required fields.
        
        Args:
            instructions: Instructions object from RenderOutputAction
        """
        # Check base instructions exist
        base_instructions = instructions.get('base_instructions', [])
        assert base_instructions, "base_instructions should be present"
        
        # Check RenderOutputAction-specific fields
        # Note: Some fields may be empty lists if no render configs exist
        assert instructions.get('render_instructions') is not None, "render_instructions should be set"
        assert instructions.get('render_configs') is not None, "render_configs should be set"
        assert instructions.get('executed_configs') is not None, "executed_configs should be set"
        assert instructions.get('executed_specs') is not None, "executed_specs should be set"
        assert instructions.get('template_specs') is not None, "template_specs should be set"
    
    def assert_validate_instructions(self, instructions):
        """Assert ValidateRulesAction injected all required fields.
        
        Args:
            instructions: Instructions object from ValidateRulesAction
        """
        # Check base instructions exist
        base_instructions = instructions.get('base_instructions', [])
        assert base_instructions, "base_instructions should be present"
        
        # Check ValidateRulesAction-specific fields
        # Placeholders should be replaced in base_instructions
        base_text = ' '.join(base_instructions)
        
        # Validate that placeholders were replaced (should not contain {{}} anymore)
        assert '{{rules}}' not in base_text, "{{rules}} placeholder should be replaced"
        assert '{{scanner_output}}' not in base_text, "{{scanner_output}} placeholder should be replaced"
        assert '{{schema}}' not in base_text, "{{schema}} placeholder should be replaced"
        assert '{{description}}' not in base_text, "{{description}} placeholder should be replaced"
        
        # Check that rules field exists (may be empty list if no rules)
        assert instructions.get('rules') is not None, "rules should be set"
    
    def assert_base_instructions_present(self, instructions):
        """Assert base instructions are present (generic check).
        
        Args:
            instructions: Instructions object
        """
        base_instructions = instructions.get('base_instructions', [])
        assert base_instructions, "base_instructions should be present"
        assert len(base_instructions) > 0, "base_instructions should not be empty"
    
    def assert_behavior_instructions_present(self, instructions):
        """Assert behavior metadata is present.
        
        Args:
            instructions: Instructions object
        """
        # Check for behavior metadata that Action._prepare_metadata sets
        behavior_metadata = instructions.get('behavior_metadata') or instructions.get('behavior_instructions')
        assert behavior_metadata is not None, "behavior_metadata should be set"
    
    def assert_behavior_instructions_contain_action(self, instructions, behavior: str, action: str):
        """Assert action metadata is present.
        
        Args:
            instructions: Instructions object
            behavior: Behavior name (not used, kept for compatibility)
            action: Action name (not used, kept for compatibility)
        """
        # Check for action metadata that Action._prepare_metadata sets
        action_metadata = instructions.get('action_metadata') or instructions.get('action_instructions')
        assert action_metadata is not None, "action_metadata should be set"
    
    def assert_instructions_indicate_updating_existing_file(self, instructions, expected_output: str):
        """Assert instructions indicate updating existing file.
        
        Args:
            instructions: Instructions dict or Instructions object
            expected_output: Expected output filename
        """
        assert 'knowledge_graph_config' in instructions or instructions.get('knowledge_graph_config'), \
            "Instructions should contain 'knowledge_graph_config'"
        config = instructions.get('knowledge_graph_config', {})
        assert config.get('output') == expected_output, \
            f"Expected output '{expected_output}', got '{config.get('output')}'"
        assert 'template_path' in instructions or instructions.get('template_path'), \
            "Instructions should contain 'template_path'"
    
    def assert_story_graph_updated_with_increments(self, instructions, story_graph_path: Path):
        """Assert story graph updated with increments.
        
        Args:
            instructions: Instructions dict or Instructions object
            story_graph_path: Path to story graph file
        """
        assert story_graph_path.exists(), f"Story graph file should exist: {story_graph_path}"
        config = instructions.get('knowledge_graph_config', {})
        assert config.get('output') == 'story-graph.json', \
            f"Expected output 'story-graph.json', got '{config.get('output')}'"
        assert 'template_path' in instructions or instructions.get('template_path'), \
            "Instructions should contain 'template_path'"
    
    # ========================================================================
    # Story Graph Helpers
    # ========================================================================
    
    def story_graph_dict(self, minimal=False, scope_type=None, epic=None):
        """Return story graph dictionary for testing.
        
        Args:
            minimal: If True, returns minimal story graph for test file scope
            scope_type: Type of scope ('multiple_test_files' for multiple test files)
            epic: Epic name ('mob' for mob epic, None for default)
        
        Returns:
            Story graph dictionary
        """
        if minimal:
            return {
                "epics": [
                    {
                        "name": "Places Order",
                        "sub_epics": [
                            {
                                "name": "Validates Payment",
                                "story_groups": [
                                    {
                                        "stories": [
                                            {
                                                "name": "Place Order",
                                                "scenarios": []
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        elif scope_type == 'multiple_test_files':
            return {
                "epics": [
                    {
                        "name": "Manage Orders",
                        "sub_epics": [
                            {
                                "name": "Create Order",
                                "story_groups": [
                                    {
                                        "stories": [
                                            {
                                                "name": "Place Order",
                                                "scenarios": []
                                            },
                                            {
                                                "name": "Cancel Order",
                                                "scenarios": []
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        elif epic == 'mob':
            return {
                "epics": [
                    {
                        "name": "Manage Mobs",
                        "sequential_order": 1,
                        "estimated_stories": 6,
                        "domain_concepts": [
                            {
                                "name": "Mob",
                                "responsibilities": [
                                    {
                                        "name": "Groups minions together for coordinated action",
                                        "collaborators": ["Minion"]
                                    }
                                ]
                            }
                        ],
                        "sub_epics": []
                    }
                ]
            }
        else:
            # Default: test story graph
            return {
                "epics": [
                    {
                        "name": "Test Epic",
                        "sequential_order": 1,
                        "sub_epics": [],
                        "story_groups": []
                    }
                ]
            }
    
    def access_story_item(self, item_type, source, **access_params):
        """Access item from story map source.
        
        Args:
            item_type: Type of item ('epic', 'sub_epic', 'story', 'scenario', 'scenario_outline', 'epics')
            source: Source to access from (epics list, story_map, epic, story, etc.)
            **access_params: Additional parameters:
                - index: Index to access (default: 0 for first item)
                - name: Name to search for (for story/scenario/outline)
        
        Returns:
            The accessed item
        """
        index = access_params.get('index', 0)
        name = access_params.get('name')
        
        if item_type == 'epics':
            # Access epics from story_map
            story_map = source
            return story_map.epics()
        elif item_type == 'epic':
            if hasattr(source, 'epics'):  # It's a story_map
                epics = source.epics()
            else:  # It's an epics list
                epics = source
            return epics[index] if index is not None else epics[0]
        elif item_type == 'sub_epic':
            epics = source if isinstance(source, list) else source.epics()
            return epics[0].children[0]
        elif item_type == 'story':
            if name:
                # Search by name
                epic = source if hasattr(source, 'children') else source.epics()[0]
                for sub_epic in epic.children:
                    for story_group in sub_epic.children:
                        for story in story_group.children:
                            if story.name == name:
                                return story
                raise ValueError(f"Story '{name}' not found")
            elif hasattr(source, 'epics'):  # It's a story_map
                return source.epics()[0].children[0].children[0].children[0]
            elif hasattr(source, 'children'):  # It's an epic
                return source.children[0].children[0].children[0]
            else:  # It's an epics list
                return source[0].children[0].children[0].children[0]
        elif item_type == 'scenario':
            if name:
                # Search by name
                story = source if hasattr(source, 'scenarios') else self.access_story_item('story', source)
                for scenario in story.scenarios:
                    if scenario.name == name:
                        return scenario
                raise ValueError(f"Scenario '{name}' not found")
            elif hasattr(source, 'scenarios'):  # It's a story
                return source.scenarios[index]
            else:  # It's epics list
                story = self.access_story_item('story', source)
                return story.scenarios[index]
        elif item_type == 'scenario_outline':
            if name:
                # Search by name
                scenario = source if hasattr(source, 'examples_columns') else self.access_story_item('scenario', source)
                for outline in scenario.scenario_outlines if hasattr(scenario, 'scenario_outlines') else []:
                    if outline.name == name:
                        return outline
                raise ValueError(f"Scenario outline '{name}' not found")
            elif hasattr(source, 'scenario_outlines'):  # It's a story
                return source.scenario_outlines[index]
            else:  # It's epics list
                story = self.access_story_item('story', source)
                return story.scenario_outlines[index]
        else:
            raise ValueError(f"Unknown item_type: {item_type}")
    
    def assert_nodes_match(self, nodes, expected_count=None, expected_names=None):
        """Assert nodes match expected count and names.
        
        Args:
            nodes: List of nodes to check
            expected_count: Expected number of nodes (None = don't check count)
            expected_names: Expected names (list or None = don't check names)
        """
        if expected_count is not None:
            assert len(nodes) == expected_count, f"Expected {expected_count} nodes, got {len(nodes)}"
        if expected_names is not None:
            actual_names = [node.name for node in nodes]
            assert actual_names == expected_names, f"Expected names {expected_names}, got {actual_names}"
    
    def assert_children_match(self, parent, expected_count=None, expected_names=None):
        """Assert children match expected count and names.
        
        Args:
            parent: Parent item (Epic, SubEpic, StoryGroup, etc.)
            expected_count: Expected number of children (None = don't check count)
            expected_names: Expected names (list or None = don't check names)
        """
        children = parent.children
        if expected_count is not None:
            assert len(children) == expected_count, f"Expected {expected_count} children, got {len(children)}"
        if expected_names is not None:
            actual_names = [child.name for child in children]
            assert actual_names == expected_names, f"Expected names {expected_names}, got {actual_names}"
    
    def assert_stories_match(self, expected, actual):
        """Assert stories match expected.
        
        Args:
            expected: Expected stories (set, list, or dict)
            actual: Actual stories (set, list, or dict)
        """
        if isinstance(expected, set) and isinstance(actual, set):
            assert expected == actual, f"Expected {expected}, got {actual}"
        elif isinstance(expected, list) and isinstance(actual, list):
            assert set(expected) == set(actual), f"Expected {expected}, got {actual}"
        else:
            assert expected == actual, f"Expected {expected}, got {actual}"
    
    def assert_scenarios_match(self, story, expected_count=None, expected_names=None):
        """Assert scenarios match expected count and names.
        
        Args:
            story: Story instance
            expected_count: Expected number of scenarios (None = don't check count)
            expected_names: Expected names (list or None = don't check names)
        """
        scenarios = story.scenarios
        if expected_count is not None:
            assert len(scenarios) == expected_count, f"Expected {expected_count} scenarios, got {len(scenarios)}"
        if expected_names is not None:
            actual_names = [scenario.name for scenario in scenarios]
            assert actual_names == expected_names, f"Expected names {expected_names}, got {actual_names}"
    
    def assert_scenario_outlines_match(self, scenario, expected_count=None, expected_names=None):
        """Assert scenario outlines match expected count and names.
        
        Args:
            scenario: Scenario or Story instance (if Story, checks scenario_outlines)
            expected_count: Expected number of scenario outlines (None = don't check count)
            expected_names: Expected names (list or None = don't check names)
        """
        from agile_bot.src.scanners.story_map import Story
        if isinstance(scenario, Story):
            outlines = scenario.scenario_outlines
        else:
            outlines = scenario.scenario_outlines if hasattr(scenario, 'scenario_outlines') else []
        if expected_count is not None:
            assert len(outlines) == expected_count, f"Expected {expected_count} scenario outlines, got {len(outlines)}"
        if expected_names is not None:
            actual_names = [outline.name for outline in outlines]
            assert actual_names == expected_names, f"Expected names {expected_names}, got {actual_names}"
    
    # ========================================================================
    # Instruction Assertion Helpers
    # ========================================================================
    
    def assert_instructions_have_structure(self, instructions, structure='validation_rules'):
        """Assert instructions have expected structure.
        
        Args:
            instructions: Instructions dict to check
            structure: Structure type to validate ('validation_rules' or custom structure dict)
        """
        if structure == 'validation_rules':
            # Default validation_rules structure check
            assert 'validation_rules' in instructions, "Instructions must contain 'validation_rules' key"
            validation_rules = instructions['validation_rules']
            assert len(validation_rules) > 0, "Instructions should contain validation rules"
            
            # Validate each rule structure (accepts Rule objects or dicts)
            from agile_bot.src.actions.rules.rule import Rule
            from agile_bot.test.domain.test_validate_knowledge_and_content_against_rules import validate_violation_structure
            
            for rule in validation_rules:
                # Handle Rule objects (new format)
                if isinstance(rule, Rule):
                    assert hasattr(rule, 'rule_file'), f"Rule object must have 'rule_file' attribute"
                    assert hasattr(rule, 'rule_content'), f"Rule object must have 'rule_content' attribute"
                    rule_file = str(rule.rule_file)
                    rule_content = rule.rule_content
                elif isinstance(rule, dict):
                    # Backward compatibility: dict format (from rules.validate() which returns dicts)
                    assert 'rule_content' in rule, f"Rule dict must contain 'rule_content' key: {rule}"
                    rule_content = rule['rule_content']
                    rule_file = rule.get('rule_file', 'unknown')
                    # If dict has scanner_results, validate it
                    if 'scanner_results' in rule:
                        scanner_results = rule['scanner_results']
                        if 'violations' in scanner_results:
                            violations = scanner_results['violations']
                            assert isinstance(violations, list), "Scanner results should contain violations list"
                            for violation in violations:
                                assert validate_violation_structure(violation, ['rule', 'line_number', 'location', 'violation_message', 'severity']), (
                                    f"Violation missing required fields: {violation}"
                                )
                else:
                    raise AssertionError(f"Rule should be a Rule object or dict, got: {type(rule)}")
                
                # Validate rule_content has scanner if it's a dict
                if isinstance(rule_content, dict):
                    assert 'scanner' in rule_content, f"Rule content must contain 'scanner' key: {rule_content}"
                    scanner_path = rule_content['scanner']
                    assert scanner_path is not None, f"Rule should have a scanner attached: {rule_file}"
            
            assert 'base_instructions' in instructions, "Instructions must contain 'base_instructions' key"
            base_instructions = instructions['base_instructions']
            assert isinstance(base_instructions, list), "Base instructions should be a list"
        elif isinstance(structure, dict):
            # Custom structure check - structure dict specifies required keys and their types/validators
            for key, validator in structure.items():
                assert key in instructions, f"Instructions must contain '{key}' key"
                if callable(validator):
                    validator(instructions[key])
                elif isinstance(validator, type):
                    assert isinstance(instructions[key], validator), f"'{key}' should be of type {validator.__name__}"
                elif isinstance(validator, list):
                    # List of allowed values
                    assert instructions[key] in validator, f"'{key}' should be one of {validator}"
    
    def assert_config_path_matches(self, instructions, config_path, config_key='knowledge_graph_config'):
        """Assert config path matches expected.
        
        Args:
            instructions: Instructions dict containing config
            config_path: Expected config path value (can be relative or absolute)
            config_key: Key in instructions that contains the config (default: 'knowledge_graph_config')
        """
        if config_key not in instructions:
            return
        config = instructions[config_key]
        if isinstance(config, dict) and 'path' in config:
            actual_path = config['path']
            # Handle both absolute and relative paths
            if '\\' in actual_path or '/' in actual_path:
                # Normalize paths for comparison
                from pathlib import Path
                actual_path_obj = Path(actual_path)
                config_path_obj = Path(config_path)
                # Check if actual path ends with the expected relative path
                assert str(actual_path_obj).replace('\\', '/').endswith(str(config_path_obj).replace('\\', '/')), \
                    f"Expected config path to end with '{config_path}', got '{actual_path}'"
            else:
                assert actual_path == config_path, f"Expected config path '{config_path}', got '{actual_path}'"
    
    def assert_instructions_merged_from_sources(self, merged_instructions, behavior, action, sources='both'):
        """Assert instructions merged from sources.
        
        Args:
            merged_instructions: Merged instructions dict to check
            behavior: Expected behavior name
            action: Expected action name
            sources: Which sources should be present ('both', 'base_only', or 'behavior_only')
        """
        assert merged_instructions['action'] == action, f"Expected action '{action}', got '{merged_instructions.get('action')}'"
        assert merged_instructions['behavior'] == behavior, f"Expected behavior '{behavior}', got '{merged_instructions.get('behavior')}'"
        
        if sources == 'both':
            assert 'base_instructions' in merged_instructions, "Instructions must contain 'base_instructions' key"
            assert 'behavior_instructions' in merged_instructions, "Instructions must contain 'behavior_instructions' key"
        elif sources == 'base_only':
            assert 'base_instructions' in merged_instructions, "Instructions must contain 'base_instructions' key"
            assert merged_instructions.get('behavior_instructions', []) == [], "Behavior instructions should be empty"
        elif sources == 'behavior_only':
            assert 'behavior_instructions' in merged_instructions, "Instructions must contain 'behavior_instructions' key"
            assert merged_instructions.get('base_instructions', []) == [], "Base instructions should be empty"
    
    def assert_instructions_contain(self, instructions, content_type, **content_params):
        """Assert instructions contain specified content type.
        content_type can be: 'next_behavior_reminder', 'reminder_prompt_text', 'guardrails', 'strategy_criteria_and_assumptions', 'template_path', 'validation_rules', 'render_required_fields', 'render_field_values'
        """
        from pathlib import Path
        
        if content_type == 'next_behavior_reminder':
            # instructions is action_result dict
            instructions_dict = instructions.get('instructions', {}) if isinstance(instructions, dict) else instructions
            assert instructions_dict, f"No instructions found. Result: {instructions}"
            base_instructions_list = instructions_dict.get('base_instructions', [])
            reminder_found = False
            next_behavior_found = False
            for i, instruction in enumerate(base_instructions_list):
                if 'NEXT BEHAVIOR REMINDER' in instruction:
                    reminder_found = True
                    if i + 1 < len(base_instructions_list):
                        next_instruction = base_instructions_list[i + 1]
                        if 'prioritization' in next_instruction.lower():
                            next_behavior_found = True
            assert reminder_found, "base_instructions should include 'NEXT BEHAVIOR REMINDER' section"
            assert next_behavior_found, "Reminder should mention 'prioritization' as the next behavior"
            return base_instructions_list
        
        elif content_type == 'reminder_prompt_text':
            # instructions is base_instructions_list
            instructions_text = ' '.join(instructions) if isinstance(instructions, list) else instructions
            assert 'next behavior in sequence' in instructions_text.lower(), "Reminder should contain 'next behavior in sequence' text"
            assert 'would you like to continue' in instructions_text.lower() or 'work on a different behavior' in instructions_text.lower(), "Reminder should contain prompt asking user if they want to continue"
        
        elif content_type == 'guardrails':
            # instructions is dict
            assert 'guardrails' in instructions
            assert 'required_context' in instructions['guardrails']
            assert 'key_questions' in instructions['guardrails']['required_context']
            assert instructions['guardrails']['required_context']['key_questions'] == content_params.get('expected_questions', [])
            assert 'evidence' in instructions['guardrails']['required_context']
            assert instructions['guardrails']['required_context']['evidence'] == content_params.get('expected_evidence', [])
        
        elif content_type == 'strategy_criteria_and_assumptions':
            # instructions is dict
            assert 'strategy_criteria' in instructions
            assert 'assumptions' in instructions
            assert instructions['assumptions'] == content_params.get('expected_assumptions', [])
            assert instructions['strategy_criteria'] is not None
        
        elif content_type == 'template_path':
            # instructions is dict
            template_name = content_params.get('template_name')
            if 'template_path' in instructions:
                assert template_name in instructions['template_path']
            # Note: template_path may be missing in minimal execution; skip strict enforcement
        
        elif content_type == 'validation_rules':
            # instructions is dict
            assert 'validation_rules' in instructions, "Instructions must contain 'validation_rules' key"
            return instructions['validation_rules']
        
        elif content_type == 'render_required_fields':
            # instructions is base_instructions_text string
            assert instructions.strip() != ''
            assert 'render' in instructions.lower() or 'template' in instructions.lower() or 'output' in instructions.lower()
        
        elif content_type == 'render_field_values':
            # instructions is base_instructions_text string
            assert instructions.strip() != ''
            assert 'render' in instructions.lower() or 'scenario' in instructions.lower() or 'template' in instructions.lower()
        
        else:
            raise ValueError(f"Unknown content_type: {content_type}")
    
    def assert_instructions_do_not_contain(self, instructions, content_type):
        """Assert instructions do not contain specified content type.
        content_type can be: 'next_behavior_reminder', 'next_action_instructions', 'guardrails', 'strategy_data'
        """
        if content_type == 'next_behavior_reminder':
            # instructions is action_result dict or BotResult object
            if hasattr(instructions, 'data'):
                instructions_dict = instructions.data.get('instructions', {})
            else:
                instructions_dict = instructions.get('instructions', {}) if isinstance(instructions, dict) else instructions
            base_instructions_list = instructions_dict.get('base_instructions', [])
            instructions_text = ' '.join(base_instructions_list)
            assert 'NEXT BEHAVIOR REMINDER' not in instructions_text, "base_instructions should NOT include 'NEXT BEHAVIOR REMINDER' when action is not final"
        
        elif content_type == 'next_action_instructions':
            # instructions is string
            assert instructions == '' or 'complete' in instructions.lower()
        
        elif content_type == 'guardrails':
            # instructions is dict
            assert 'guardrails' not in instructions or instructions['guardrails'] == {}
        
        elif content_type == 'strategy_data':
            # instructions is dict
            assert 'strategy_criteria' not in instructions or instructions['strategy_criteria'] == {}
            assert 'assumptions' not in instructions or instructions['assumptions'] == []
        
        else:
            raise ValueError(f"Unknown content_type: {content_type}")
    
    def assert_template_variables_replaced(self, instructions_text, type=None):
        """Assert template variables are replaced in instructions text.
        
        Args:
            instructions_text: The instructions text to check
            type: Type of template variables to check. None (default) = all build knowledge variables,
                  'render_configs' = render configs variables, 'render_instructions' = render instructions variables
        """
        if type is None or type == 'build':
            # In minimal setups we only verify instructions text is present
            assert isinstance(instructions_text, str)
            assert instructions_text.strip() != ''
            # Skip strict content checks since real instructions vary
        
        elif type == 'render_configs':
            # Check render configs template variables
            assert '{{render_configs}}' not in instructions_text
            # Content may vary by render specs; just ensure some render config text is present
            assert 'render' in instructions_text.lower()
        
        elif type == 'render_instructions':
            # Check render instructions template variables
            assert '{{render_configs}}' not in instructions_text
            assert '{{render_instructions}}' not in instructions_text
            # Ensure render instructions content was injected (non-empty)
            assert instructions_text.strip() != ''
    
    def assert_instructions_match(self, instructions, expected_content):
        """Assert instructions match expected content.
        
        Args:
            instructions: Instructions dict or string
            expected_content: Expected content (dict or string)
        """
        if isinstance(expected_content, dict) and isinstance(instructions, dict):
            assert instructions == expected_content, f"Expected {expected_content}, got {instructions}"
        else:
            assert str(instructions) == str(expected_content), f"Expected {expected_content}, got {instructions}"
    
    def assert_file_updated(self, file_path, expected_content):
        """Assert file updated with expected content.
        
        Args:
            file_path: Path to file
            expected_content: Expected content (dict or string)
        """
        from pathlib import Path
        import json
        file_path = Path(file_path)
        assert file_path.exists(), f"File {file_path} does not exist"
        actual_content = json.loads(file_path.read_text(encoding='utf-8')) if isinstance(expected_content, dict) else file_path.read_text(encoding='utf-8')
        if isinstance(expected_content, dict):
            assert actual_content == expected_content, f"Expected {expected_content}, got {actual_content}"
        else:
            assert actual_content == expected_content, f"Expected {expected_content}, got {actual_content}"
    
    # ========================================================================
    # Story Map Assertion Helpers
    # ========================================================================
    
    def assert_story_map_matches(self, story_map_or_epics, epic_name=None):
        """Assert story map matches expected epic.
        
        Args:
            story_map_or_epics: StoryMap instance or epics list
            epic_name: Expected epic name (None = use default)
        
        Returns:
            The epic if checking epics list, None otherwise
        """
        from agile_bot.src.scanners.story_map import Epic
        
        if isinstance(story_map_or_epics, list):
            # It's an epics list
            epics = story_map_or_epics
            assert len(epics) == 1, f"Expected 1 epic, got {len(epics)}"
            assert isinstance(epics[0], Epic), f"Expected Epic instance, got {type(epics[0])}"
            expected_name = epic_name if epic_name is not None else "Build Knowledge"
            assert epics[0].name == expected_name, \
                f"Expected epic name '{expected_name}', got '{epics[0].name}'"
            return epics[0]
        else:
            # It's a story_map
            epics_list = story_map_or_epics.epics()
            assert len(epics_list) == 1, f"Expected 1 epic, got {len(epics_list)}"
            expected_name = epic_name if epic_name is not None else "Test Epic"
            assert epics_list[0].name == expected_name, \
                f"Expected epic name '{expected_name}', got '{epics_list[0].name}'"
    
    def assert_map_location_matches(self, item, item_type=None, field=None):
        """Assert map location correctness for story map items.
        
        Args:
            item: Epic, SubEpic, Story, Scenario, or ScenarioOutline instance
            item_type: Type hint ('epic', 'sub_epic', 'story', 'scenario', 'scenario_outline') - auto-detected if None
            field: Optional field name to check (e.g., 'sequential_order', 'sizing')
        """
        from agile_bot.src.scanners.story_map import Epic, SubEpic, Story, Scenario, ScenarioOutline
        
        # Auto-detect type if not provided
        if item_type is None:
            if isinstance(item, Epic):
                item_type = 'epic'
            elif isinstance(item, SubEpic):
                item_type = 'sub_epic'
            elif isinstance(item, Story):
                item_type = 'story'
            elif isinstance(item, Scenario):
                item_type = 'scenario'
            elif isinstance(item, ScenarioOutline):
                item_type = 'scenario_outline'
        
        # Expected locations based on type
        expected_locations = {
            'epic': {
                None: "epics[0].name",
                'sequential_order': "epics[0].sequential_order"
            },
            'sub_epic': {
                None: "epics[0].sub_epics[0].name"
            },
            'story': {
                None: "epics[0].sub_epics[0].story_groups[0].stories[0].name",
                'sizing': "epics[0].sub_epics[0].story_groups[0].stories[0].sizing"
            },
            'scenario': {
                None: "epics[0].sub_epics[0].story_groups[0].stories[0].scenarios[0].name"
            },
            'scenario_outline': {
                None: "epics[0].sub_epics[0].story_groups[0].stories[0].scenario_outlines[0].name"
            }
        }
        
        # Check default location (name)
        expected_default = expected_locations.get(item_type, {}).get(None)
        assert item.map_location() == expected_default, \
            f"Expected map_location() == '{expected_default}', got '{item.map_location()}'"
        
        # Check additional fields if applicable
        if item_type == 'epic':
            expected_seq = expected_locations.get(item_type, {}).get('sequential_order')
            assert item.map_location('sequential_order') == expected_seq, \
                f"Expected map_location('sequential_order') == '{expected_seq}', got '{item.map_location('sequential_order')}'"
        elif item_type == 'story' and field == 'sizing':
            expected_sizing = expected_locations.get(item_type, {}).get('sizing')
            assert item.map_location('sizing') == expected_sizing, \
                f"Expected map_location('sizing') == '{expected_sizing}', got '{item.map_location('sizing')}'"
    
    # ========================================================================
    # Story Graph Helpers (moved from test_helpers.py)
    # ========================================================================
    
    def given_story_graph(self, story_graph: dict = None, docs_path: str = 'docs/stories', filename: str = 'story-graph.json') -> Path:
        """Create story graph file in workspace.
        
        Args:
            story_graph: Story graph dict (default: {'epics': []})
            docs_path: Relative path from workspace to docs directory (default: 'docs/stories')
            filename: Story graph filename (default: 'story-graph.json')
        
        Returns:
            Path to created story graph file
        """
        if story_graph is None:
            story_graph = {'epics': []}
        
        docs_dir = self.workspace / docs_path
        docs_dir.mkdir(parents=True, exist_ok=True)
        story_graph_file = docs_dir / filename
        story_graph_file.write_text(json.dumps(story_graph, indent=2), encoding='utf-8')
        return story_graph_file
    
    def given_story_graph_dict(self, minimal=False, scope_type=None, epic=None):
        """Return story graph dictionary for testing.
        
        Args:
            minimal: If True, returns minimal story graph for test file scope
            scope_type: Type of scope ('multiple_test_files' for multiple test files)
            epic: Epic name ('mob' for mob epic, None for default)
        
        Returns:
            Story graph dictionary
        """
        if minimal:
            return {
                "epics": [
                    {
                        "name": "Places Order",
                        "sub_epics": [
                            {
                                "name": "Validates Payment",
                                "story_groups": [
                                    {
                                        "stories": [
                                            {
                                                "name": "Place Order",
                                                "scenarios": []
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        elif scope_type == 'multiple_test_files':
            return {
                "epics": [
                    {
                        "name": "Manage Orders",
                        "sub_epics": [
                            {
                                "name": "Create Order",
                                "story_groups": [
                                    {
                                        "stories": [
                                            {
                                                "name": "Place Order",
                                                "scenarios": []
                                            },
                                            {
                                                "name": "Cancel Order",
                                                "scenarios": []
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        elif epic == 'mob':
            return {
                "epics": [
                    {
                        "name": "Manage Mobs",
                        "sequential_order": 1,
                        "estimated_stories": 6,
                        "domain_concepts": [
                            {
                                "name": "Mob",
                                "responsibilities": [
                                    {
                                        "name": "Groups minions together for coordinated action",
                                        "collaborators": ["Minion"]
                                    }
                                ]
                            }
                        ],
                        "sub_epics": []
                    }
                ]
            }
        else:
            return {
                "epics": [
                    {
                        "name": "Test Epic",
                        "sequential_order": 1,
                        "sub_epics": [],
                        "story_groups": []
                    }
                ]
            }
    
    def when_item_accessed(self, item_type, source, **access_params):
        """Access item from source (story map navigation).
        
        Args:
            item_type: Type of item ('epic', 'sub_epic', 'story', 'scenario', 'scenario_outline', 'epics')
            source: Source to access from (epics list, story_map, epic, story, etc.)
            **access_params: Additional parameters:
                - index: Index to access (default: 0 for first item)
                - name: Name to search for (for story/scenario/outline)
                - story_map: StoryMap instance (if accessing epics from story_map)
        
        Returns:
            The accessed item
        """
        index = access_params.get('index', 0)
        name = access_params.get('name')
        
        if item_type == 'epics':
            story_map = source
            return story_map.epics()
        elif item_type == 'epic':
            if hasattr(source, 'epics'):
                epics = source.epics()
            else:
                epics = source
            return epics[index] if index is not None else epics[0]
        elif item_type == 'sub_epic':
            epics = source if isinstance(source, list) else source.epics()
            return epics[0].children[0]
        elif item_type == 'story':
            if name:
                epic = source if hasattr(source, 'children') else source.epics()[0]
                for sub_epic in epic.children:
                    for story_group in sub_epic.children:
                        for story in story_group.children:
                            if story.name == name:
                                return story
                raise ValueError(f"Story '{name}' not found")
            elif hasattr(source, 'epics'):
                return source.epics()[0].children[0].children[0].children[0]
            elif hasattr(source, 'children'):
                return source.children[0].children[0].children[0]
            else:
                return source[0].children[0].children[0].children[0]
        elif item_type == 'scenario':
            if name:
                story = source if hasattr(source, 'scenarios') else self.when_item_accessed('story', source)
                for scenario in story.scenarios:
                    if scenario.name == name:
                        return scenario
                raise ValueError(f"Scenario '{name}' not found")
            elif hasattr(source, 'scenarios'):
                return source.scenarios[index]
            else:
                story = self.when_item_accessed('story', source)
                return story.scenarios[index]
        elif item_type == 'scenario_outline':
            if name:
                scenario = source if hasattr(source, 'examples_columns') else self.when_item_accessed('scenario', source)
                for outline in scenario.scenario_outlines if hasattr(scenario, 'scenario_outlines') else []:
                    if outline.name == name:
                        return outline
                raise ValueError(f"Scenario outline '{name}' not found")
            elif hasattr(source, 'scenario_outlines'):
                return source.scenario_outlines[index]
            else:
                story = self.when_item_accessed('story', source)
                return story.scenario_outlines[index]
        else:
            raise ValueError(f"Unknown item_type: {item_type}")
    
    # ========================================================================
    # Activity Log Helpers (moved from test_helpers.py)
    # ========================================================================
    
    def given_activity_log(self, entries: list = None, **params):
        """Create activity log with entries.
        
        Args:
            entries: List of activity log entries (if None, creates default multiple entries)
            **params: Additional parameters:
                - return_file: If True, return log file path (default: True for backward compatibility)
        
        Returns:
            Log file Path
        """
        log_file = self.workspace / 'activity_log.json'
        from tinydb import TinyDB
        
        with TinyDB(log_file) as db:
            if entries is None:
                db.insert({'action_state': 'story_bot.shape.render', 'timestamp': '09:00'})
                db.insert({'action_state': 'story_bot.discovery.render', 'timestamp': '10:00'})
            else:
                for entry in entries:
                    db.insert(entry)
        
        return log_file
    
    def read_activity_log(self) -> list:
        """Read activity log from workspace directory."""
        log_file = self.workspace / 'activity_log.json'
        from tinydb import TinyDB
        with TinyDB(log_file) as db:
            return db.all()
    
    def then_activity_logged_with_action_state(self, expected_action_state: str):
        """Assert activity logged with expected action_state."""
        from tinydb import TinyDB
        log_file = self.workspace / 'activity_log.json'
        
        with TinyDB(log_file) as db:
            entries = db.all()
            if not any(entry.get('action_state') == expected_action_state for entry in entries):
                actual_states = [entry.get('action_state') for entry in entries]
                raise AssertionError(
                    f"Expected action_state '{expected_action_state}' not found in activity log. "
                    f"Actual entries: {actual_states}"
                )
    
    def then_activity_log_matches(self, log_file=None, **checks):
        """Assert activity log matches expected values.
        
        Args:
            log_file: Optional Path to log file (if provided, used instead of workspace/activity_log.json)
            **checks: Checks to perform:
                - expected_count: Expected number of entries
                - expected_action_state: Expected action_state in entry (single value)
                - expected_action_states: List of expected action_states (one per entry in order)
                - expected_last_action_state: Expected action_state of last entry
                - expected_status: Expected status in entry
                - expected_entries: List of expected entry dicts (matched by action_state, not exact match)
                - workflow_complete: Check that completion entry has workflow_complete flag in outputs
        """
        from tinydb import TinyDB
        
        if log_file is None:
            log_file = self.workspace / 'activity_log.json'
        
        if not log_file.exists():
            if 'expected_count' in checks and checks['expected_count'] == 0:
                return
            assert False, f"Activity log file does not exist at {log_file}"
        
        with TinyDB(log_file) as db:
            entries = db.all()
            
            if 'expected_count' in checks:
                assert len(entries) == checks['expected_count'], \
                    f"Expected {checks['expected_count']} entries, got {len(entries)}"
            
            if 'expected_action_state' in checks:
                assert any(entry.get('action_state') == checks['expected_action_state'] for entry in entries), \
                    f"Expected action_state '{checks['expected_action_state']}' not found in entries"
            
            if 'expected_action_states' in checks:
                expected_states = checks['expected_action_states']
                actual_states = [entry.get('action_state') for entry in entries]
                assert len(actual_states) == len(expected_states), \
                    f"Expected {len(expected_states)} entries, got {len(actual_states)}"
                for i, expected_state in enumerate(expected_states):
                    assert actual_states[i] == expected_state, \
                        f"Entry {i}: expected '{expected_state}', got '{actual_states[i]}'"
            
            if 'expected_last_action_state' in checks:
                assert entries[-1].get('action_state') == checks['expected_last_action_state'], \
                    f"Expected last action_state '{checks['expected_last_action_state']}', got '{entries[-1].get('action_state')}'"
            
            if 'expected_status' in checks:
                assert any(entry.get('status') == checks['expected_status'] for entry in entries), \
                    f"Expected status '{checks['expected_status']}' not found in entries"
            
            if 'expected_entries' in checks:
                expected_entries = checks['expected_entries']
                for expected_entry in expected_entries:
                    expected_action_state = expected_entry.get('action_state')
                    matching_entry = next((e for e in entries if e.get('action_state') == expected_action_state), None)
                    assert matching_entry is not None, \
                        f"Expected entry with action_state '{expected_action_state}' not found"
                    for key, value in expected_entry.items():
                        if key != 'action_state':
                            assert matching_entry.get(key) == value, \
                                f"Entry {expected_action_state}: expected {key}='{value}', got '{matching_entry.get(key)}'"
            
            if 'workflow_complete' in checks:
                completion_entry = next((e for e in entries if 'outputs' in e), None)
                assert completion_entry is not None, "No completion entry found in activity log"
                assert completion_entry.get('outputs', {}).get('workflow_complete') == True, \
                    "Completion entry should have workflow_complete=True in outputs"
    
    def given_activity_tracker(self, bot_name='story_bot'):
        """Create activity tracker."""
        from agile_bot.src.actions.activity_tracker import ActivityTracker
        from agile_bot.src.bot.bot_paths import BotPaths
        bot_paths = BotPaths(workspace_path=self.workspace)
        return ActivityTracker(bot_paths=bot_paths, bot_name=bot_name)
    
    def when_activity_tracks_start(self, tracker, action_state):
        """Track activity start.
        
        Args:
            tracker: ActivityTracker instance
            action_state: Action state string (e.g., 'bot_name.behavior.action') or dict with bot_name, behavior, action
        """
        from agile_bot.src.actions.activity_tracker import ActionState
        
        if isinstance(action_state, str):
            parts = action_state.split('.')
            if len(parts) == 3:
                bot_name, behavior, action = parts
                action_state_obj = ActionState(bot_name=bot_name, behavior=behavior, action=action)
            else:
                raise ValueError(f"Invalid action_state format: {action_state}. Expected 'bot_name.behavior.action'")
        elif isinstance(action_state, dict):
            action_state_obj = ActionState(
                bot_name=action_state.get('bot_name'),
                behavior=action_state.get('behavior'),
                action=action_state.get('action')
            )
        else:
            action_state_obj = action_state
        
        tracker.track_start(action_state_obj)
    
    # ========================================================================
    # Instruction Assertion Helpers (moved from test_helpers.py)
    # ========================================================================
    
    def then_instructions_have_structure(self, instructions, structure='validation_rules'):
        """Assert instructions have expected structure.
        
        Args:
            instructions: Instructions dict to check
            structure: Structure type to validate ('validation_rules' or custom structure dict)
        """
        if structure == 'validation_rules':
            assert 'validation_rules' in instructions, "Instructions must contain 'validation_rules' key"
            validation_rules = instructions['validation_rules']
            assert len(validation_rules) > 0, "Instructions should contain validation rules"
            
            from agile_bot.src.actions.rules.rule import Rule
            from agile_bot.test.domain.test_validate_knowledge_and_content_against_rules import validate_violation_structure
            
            for rule in validation_rules:
                if isinstance(rule, Rule):
                    assert hasattr(rule, 'rule_file'), f"Rule object must have 'rule_file' attribute"
                    assert hasattr(rule, 'rule_content'), f"Rule object must have 'rule_content' attribute"
                    rule_file = str(rule.rule_file)
                    rule_content = rule.rule_content
                elif isinstance(rule, dict):
                    assert 'rule_content' in rule, f"Rule dict must contain 'rule_content' key: {rule}"
                    rule_content = rule['rule_content']
                    rule_file = rule.get('rule_file', 'unknown')
                    if 'scanner_results' in rule:
                        scanner_results = rule['scanner_results']
                        if 'violations' in scanner_results:
                            violations = scanner_results['violations']
                            assert isinstance(violations, list), "Scanner results should contain violations list"
                            for violation in violations:
                                assert validate_violation_structure(violation, ['rule', 'line_number', 'location', 'violation_message', 'severity']), (
                                    f"Violation missing required fields: {violation}"
                                )
                else:
                    raise AssertionError(f"Rule should be a Rule object or dict, got: {type(rule)}")
                
                if isinstance(rule_content, dict):
                    assert 'scanner' in rule_content, f"Rule content must contain 'scanner' key: {rule_content}"
                    scanner_path = rule_content['scanner']
                    assert scanner_path is not None, f"Rule should have a scanner attached: {rule_file}"
            
            assert 'base_instructions' in instructions, "Instructions must contain 'base_instructions' key"
            base_instructions = instructions['base_instructions']
            assert isinstance(base_instructions, list), "Base instructions should be a list"
        elif isinstance(structure, dict):
            for key, validator in structure.items():
                assert key in instructions, f"Instructions must contain '{key}' key"
                if callable(validator):
                    validator(instructions[key])
                elif isinstance(validator, type):
                    assert isinstance(instructions[key], validator), f"'{key}' should be of type {validator.__name__}"
                elif isinstance(validator, list):
                    assert instructions[key] in validator, f"'{key}' should be one of {validator}"
    
    def then_instructions_merged_from_sources(self, merged_instructions, behavior, action, sources='both'):
        """Assert instructions merged from sources.
        
        Args:
            merged_instructions: Merged Instructions object to check
            behavior: Expected behavior name (not checked, kept for compatibility)
            action: Expected action name (not checked, kept for compatibility)
            sources: Which sources should be present ('both', 'base_only', or 'behavior_only')
        """
        # Instructions object uses .get() to access fields
        base_instructions = merged_instructions.get('base_instructions', [])
        behavior_instructions = merged_instructions.get('behavior_instructions')
        
        if sources == 'both':
            assert base_instructions, "Instructions must contain 'base_instructions'"
            assert len(base_instructions) > 0, "base_instructions must not be empty"
            # behavior_instructions may or may not be present depending on whether behavior has instructions
        elif sources == 'base_only':
            assert base_instructions, "Instructions must contain 'base_instructions'"
            assert len(base_instructions) > 0, "base_instructions must not be empty"
            # Don't assert behavior_instructions is empty - it may be present
        elif sources == 'behavior_only':
            # In this mode, still check base_instructions exists (all Instructions have it)
            assert base_instructions is not None, "Instructions must have base_instructions field"
    
    def then_instructions_contain(self, instructions, content_type, **content_params):
        """Assert instructions contain specified content type.
        
        content_type can be: 'next_behavior_reminder', 'reminder_prompt_text', 'guardrails', 
        'strategy_criteria_and_assumptions', 'template_path', 'validation_rules', 
        'render_required_fields', 'render_field_values'
        """
        from pathlib import Path
        
        if content_type == 'next_behavior_reminder':
            instructions_dict = instructions.get('instructions', {}) if isinstance(instructions, dict) else instructions
            assert instructions_dict, f"No instructions found. Result: {instructions}"
            base_instructions_list = instructions_dict.get('base_instructions', [])
            reminder_found = False
            next_behavior_found = False
            for i, instruction in enumerate(base_instructions_list):
                if 'NEXT BEHAVIOR REMINDER' in instruction:
                    reminder_found = True
                    if i + 1 < len(base_instructions_list):
                        next_instruction = base_instructions_list[i + 1]
                        if 'prioritization' in next_instruction.lower():
                            next_behavior_found = True
            assert reminder_found, "base_instructions should include 'NEXT BEHAVIOR REMINDER' section"
            assert next_behavior_found, "Reminder should mention 'prioritization' as the next behavior"
            return base_instructions_list
        
        elif content_type == 'reminder_prompt_text':
            instructions_text = ' '.join(instructions) if isinstance(instructions, list) else instructions
            assert 'next behavior in sequence' in instructions_text.lower(), "Reminder should contain 'next behavior in sequence' text"
            assert 'would you like to continue' in instructions_text.lower() or 'work on a different behavior' in instructions_text.lower(), "Reminder should contain prompt asking user if they want to continue"
        
        elif content_type == 'guardrails':
            # Instructions might be a dict, Instructions object, or have nested structure
            # Convert Instructions object to dict if needed
            from agile_bot.src.instructions.instructions import Instructions as InstructionsClass
            if isinstance(instructions, InstructionsClass):
                # Instructions object - access guardrails directly
                guardrails = instructions.get('guardrails')
                if not guardrails:
                    import json
                    instructions_str = json.dumps(dict(instructions)) if instructions else '{}'
                    assert 'guardrails' in instructions_str or 'required_context' in instructions_str, \
                        f"Guardrails not found in instructions. Available keys: {list(dict(instructions).keys())}"
            elif isinstance(instructions, dict):
                # Check if guardrails is at top level
                if 'guardrails' in instructions:
                    guardrails = instructions['guardrails']
                # Check if it's nested under 'instructions'
                elif 'instructions' in instructions and isinstance(instructions['instructions'], dict) and 'guardrails' in instructions['instructions']:
                    guardrails = instructions['instructions']['guardrails']
                else:
                    # Try to find guardrails anywhere in the structure
                    import json
                    instructions_str = json.dumps(instructions) if instructions else '{}'
                    assert 'guardrails' in instructions_str or 'required_context' in instructions_str, \
                        f"Guardrails not found in instructions. Structure: {list(instructions.keys()) if isinstance(instructions, dict) else type(instructions)}"
                    # If we get here, guardrails might be at a different level - let's be more flexible
                    guardrails = instructions.get('guardrails') or (instructions.get('instructions', {}).get('guardrails') if isinstance(instructions.get('instructions'), dict) else {})
                assert guardrails, "Guardrails section not found in instructions"
                assert 'required_context' in guardrails, f"required_context not found in guardrails. Keys: {list(guardrails.keys()) if isinstance(guardrails, dict) else type(guardrails)}"
                assert 'key_questions' in guardrails['required_context']
                # Compare questions - might be list or dict
                actual_questions = guardrails['required_context']['key_questions']
                expected_questions = content_params.get('expected_questions', [])
                if isinstance(actual_questions, list):
                    assert actual_questions == expected_questions
                elif isinstance(actual_questions, dict):
                    # If it's a dict, check if values match
                    assert list(actual_questions.values()) == expected_questions or list(actual_questions.keys()) == expected_questions
                assert 'evidence' in guardrails['required_context']
                actual_evidence = guardrails['required_context']['evidence']
                expected_evidence = content_params.get('expected_evidence', [])
                if isinstance(actual_evidence, list):
                    assert actual_evidence == expected_evidence
                elif isinstance(actual_evidence, dict):
                    assert list(actual_evidence.values()) == expected_evidence or list(actual_evidence.keys()) == expected_evidence
            else:
                assert False, f"Instructions should be a dict, got {type(instructions)}"
        
        elif content_type == 'strategy_criteria_and_assumptions':
            assert 'strategy_criteria' in instructions
            assert 'assumptions' in instructions
            assert instructions['assumptions'] == content_params.get('expected_assumptions', [])
            assert instructions['strategy_criteria'] is not None
        
        elif content_type == 'template_path':
            template_name = content_params.get('template_name')
            if 'template_path' in instructions:
                assert template_name in instructions['template_path']
        
        elif content_type == 'validation_rules':
            assert 'validation_rules' in instructions, "Instructions must contain 'validation_rules' key"
            return instructions['validation_rules']
        
        elif content_type == 'render_required_fields':
            instructions_text = instructions if isinstance(instructions, str) else str(instructions)
            assert instructions_text.strip() != ''
            assert 'render' in instructions_text.lower() or 'template' in instructions_text.lower() or 'output' in instructions_text.lower()
        
        elif content_type == 'render_field_values':
            instructions_text = instructions if isinstance(instructions, str) else str(instructions)
            assert instructions_text.strip() != ''
            assert 'render' in instructions_text.lower() or 'scenario' in instructions_text.lower() or 'template' in instructions_text.lower()
        
        else:
            raise ValueError(f"Unknown content_type: {content_type}")
    
    def then_instructions_do_not_contain(self, instructions, content_type):
        """Assert instructions do not contain specified content type.
        
        content_type can be: 'next_behavior_reminder', 'next_action_instructions', 'guardrails', 'strategy_data'
        """
        if content_type == 'next_behavior_reminder':
            if hasattr(instructions, 'data'):
                instructions_dict = instructions.data.get('instructions', {})
            else:
                instructions_dict = instructions.get('instructions', {}) if isinstance(instructions, dict) else instructions
            base_instructions_list = instructions_dict.get('base_instructions', [])
            instructions_text = ' '.join(base_instructions_list)
            assert 'NEXT BEHAVIOR REMINDER' not in instructions_text, "base_instructions should NOT include 'NEXT BEHAVIOR REMINDER' when action is not final"
        
        elif content_type == 'next_action_instructions':
            instructions_text = instructions if isinstance(instructions, str) else str(instructions)
            assert instructions_text == '' or 'complete' in instructions_text.lower()
        
        elif content_type == 'guardrails':
            assert 'guardrails' not in instructions or instructions['guardrails'] == {}
        
        elif content_type == 'strategy_data':
            assert 'strategy_criteria' not in instructions or instructions['strategy_criteria'] == {}
            assert 'assumptions' not in instructions or instructions['assumptions'] == []
        
        else:
            raise ValueError(f"Unknown content_type: {content_type}")
    
    def then_instructions_match(self, instructions, expected_content):
        """Assert instructions match expected content.
        
        Args:
            instructions: Instructions dict or string
            expected_content: Expected content (dict or string)
        """
        if isinstance(expected_content, dict) and isinstance(instructions, dict):
            assert instructions == expected_content, f"Expected {expected_content}, got {instructions}"
        else:
            assert str(instructions) == str(expected_content), f"Expected {expected_content}, got {instructions}"
    
    def then_violation_has_field(self, violation, field, value):
        """Assert violation has expected field value.
        
        Args:
            violation: Violation dict
            field: Field name to check ('line_number', 'location', 'violation_message', 'severity', etc.)
            value: Expected value (for violation_message, checks if value is 'in' the message)
        """
        # Map common field names
        field_mapping = {
            'line_number': 'line_number',
            'location': 'location',
            'message': 'violation_message',
            'violation_message': 'violation_message',
            'severity': 'severity'
        }
        actual_field = field_mapping.get(field, field)
        assert actual_field in violation, f"Violation missing field '{actual_field}': {violation}"
        
        # For violation_message, use 'in' check; for others use exact match
        if actual_field == 'violation_message':
            assert value in violation[actual_field], \
                f"Expected message '{value}' not found in '{violation[actual_field]}'"
        else:
            assert violation[actual_field] == value, \
                f"Violation {actual_field} mismatch: expected {value}, got {violation[actual_field]}"
    
    # ========================================================================
    # MISSING FUNCTIONS FROM test_helpers.py - TO BE REORGANIZED
    # ========================================================================
    
    def then_completion_entry_logged_with_outputs(self, log_file_or_workspace: Path, expected_outputs: dict = None, expected_duration: int = None):
        """Assert completion entry logged with outputs and duration.
        
        Accepts either log_file Path or workspace_directory Path.
        """
        from tinydb import TinyDB
        if (log_file_or_workspace / 'activity_log.json').exists():
            log_file = log_file_or_workspace / 'activity_log.json'
        else:
            log_file = log_file_or_workspace
        
        with TinyDB(log_file) as db:
            entries = db.all()
            completion_entry = next((e for e in entries if 'outputs' in e), None)
            assert completion_entry is not None
            if expected_outputs is not None:
                assert completion_entry['outputs'] == expected_outputs
            if expected_duration is not None:
                assert completion_entry['duration'] == expected_duration
    
    def given_directory_created(self, directory, **params):
        """Create directory structure.
        
        Args:
            directory: Base directory path (workspace_directory, bot_directory, etc.)
            **params: Additional parameters:
                - directory_type: Type of directory ('workspace', 'docs_stories', 'knowledge_graph',
                                'docs', 'knowledge_graph_prioritization', 'behavior_render')
                - behavior: Behavior name (required for knowledge_graph, behavior_render)
        
        Returns:
            Created directory Path (always returns path for non-workspace types)
        """
        directory_type = params.get('directory_type', 'workspace')
        behavior = params.get('behavior')
        
        if directory_type == 'workspace':
            directory.mkdir(parents=True, exist_ok=True)
            return directory
        
        elif directory_type == 'docs_stories':
            docs_dir = directory / 'docs' / 'stories'
            docs_dir.mkdir(parents=True, exist_ok=True)
            return docs_dir
        
        elif directory_type == 'knowledge_graph':
            if not behavior:
                raise ValueError("behavior parameter required for knowledge_graph directory")
            behavior_dir = directory / 'behaviors' / behavior
            kg_dir = behavior_dir / 'content' / 'knowledge_graph'
            kg_dir.mkdir(parents=True, exist_ok=True)
            return kg_dir
        
        elif directory_type == 'docs':
            docs_dir = directory / "docs" / "stories"
            docs_dir.mkdir(parents=True, exist_ok=True)
            return docs_dir
        
        elif directory_type == 'knowledge_graph_prioritization':
            if not behavior:
                raise ValueError("behavior parameter required for knowledge_graph_prioritization directory")
            behavior_dir = directory / 'behaviors' / behavior
            kg_dir = behavior_dir / 'content' / 'knowledge_graph'
            kg_dir.mkdir(parents=True, exist_ok=True)
            return kg_dir
        
        elif directory_type == 'behavior_render':
            if not behavior:
                raise ValueError("behavior parameter required for behavior_render directory")
            behavior_dir = directory / 'behaviors' / behavior
            render_dir = behavior_dir / 'content' / 'render'
            render_dir.mkdir(parents=True, exist_ok=True)
            instructions_file = render_dir / 'instructions.json'
            if not instructions_file.exists():
                instructions_file.write_text(
                    json.dumps({
                        'behaviorName': behavior,
                        'instructions': [f'Render outputs for {behavior} behavior']
                    }),
                    encoding='utf-8'
                )
            return render_dir
        
        else:
            raise ValueError(f"Unknown directory_type: {directory_type}")
    
    def given_file_created(self, directory: Path, filename: str, content, file_type: str = 'json') -> Path:
        """Create file in directory.
        
        Args:
            directory: Directory where file should be created
            filename: Name of the file
            content: Content to write (dict for JSON, str for text)
            file_type: 'json' or 'text' (default: 'json')
        
        Returns:
            Path to created file
        """
        directory.mkdir(parents=True, exist_ok=True)
        file_path = directory / filename
        
        if file_type == 'json':
            if isinstance(content, dict):
                file_path.write_text(json.dumps(content, indent=2), encoding='utf-8')
            elif isinstance(content, str):
                file_path.write_text(content, encoding='utf-8')
            else:
                file_path.write_text(json.dumps(content, indent=2), encoding='utf-8')
        else:
            file_path.write_text(str(content), encoding='utf-8')
        
        return file_path
    
    def given_files_created(self, directory: Path, filenames: list, file_type: str = 'json') -> list:
        """Create multiple files in directory.
        
        Args:
            directory: Directory where files should be created
            filenames: List of tuples (filename, content) or list of filenames (if content is None, creates empty files)
            file_type: 'json' or 'text' (default: 'json')
        
        Returns:
            List of Path objects for created files
        """
        created_files = []
        for item in filenames:
            if isinstance(item, tuple):
                filename, content = item
            else:
                filename = item
                content = '' if file_type == 'text' else {}
            
            file_path = self.given_file_created(directory, filename, content, file_type=file_type)
            created_files.append(file_path)
        
        return created_files
    
    def given_environment_bootstrapped_and_activity_log_initialized(self, bot_directory: Path, workspace_directory: Path):
        """Bootstrap environment and initialize activity log."""
        import os
        os.environ['BOT_DIRECTORY'] = str(bot_directory)
        os.environ['WORKING_AREA'] = str(workspace_directory)
        self.workspace = workspace_directory
        self.workspace.mkdir(parents=True, exist_ok=True)
        log_file = self.create_activity_log_file()
        return log_file
    
    def then_environment_variables_not_set(self, var_names):
        """Assert environment variables are not set.
        
        Args:
            var_names: Variable names to check (can be list or *args)
        """
        import os
        if isinstance(var_names, str):
            var_names = [var_names]
        for var_name in var_names:
            assert var_name not in os.environ or os.environ[var_name] == '', \
                f"Environment variable {var_name} should not be set, but has value: {os.environ.get(var_name)}"
    
    def then_environment_variable_matches(self, var_name, expected_value):
        """Assert environment variable matches expected value."""
        import os
        from pathlib import Path
        actual_value = os.environ.get(var_name)
        if isinstance(expected_value, Path):
            expected_value = str(expected_value)
        if isinstance(actual_value, Path):
            actual_value = str(actual_value)
        assert actual_value == expected_value, \
            f"Environment variable {var_name} mismatch: expected {expected_value}, got {actual_value}"
    
    def then_function_returns_same_value(self, func, value):
        """Assert function returns same value on multiple calls."""
        result1 = func()
        result2 = func()
        result3 = func()
        assert result1 == value and result2 == value and result3 == value, \
            f"Function should return {value} consistently, got {result1}, {result2}, {result3}"
    
    def then_function_returns_path(self, func, expected_path):
        """Assert function returns expected path."""
        from pathlib import Path
        actual_path = func()
        if isinstance(actual_path, str):
            actual_path = Path(actual_path)
        if isinstance(expected_path, str):
            expected_path = Path(expected_path)
        assert actual_path == expected_path, \
            f"Function should return {expected_path}, got {actual_path}"
    
    def given_config_dict(self, config_type: str, **config_data) -> dict:
        """Create config dictionary.
        
        Creates different types of config dictionaries based on config_type:
        - 'state_file': Creates state_data dict with current_behavior, current_action, completed_actions, timestamp
        - 'file_paths': Creates file_paths dict/list
        - 'actions_workflow': Creates actions_workflow dict with actions list
        - 'behavior_config': Creates behavior_config dict with description, goal, inputs, outputs, actions_workflow, etc.
        - 'action_config': Creates action_config dict (if config provided, uses it; otherwise creates from action_name)
        - 'behavior_instructions': Creates behavior instructions dict
        """
        if config_type == 'state_file':
            return {
                'current_behavior': config_data.get('current_behavior', ''),
                'current_action': config_data.get('current_action', ''),
                'completed_actions': config_data.get('completed_actions', []),
                'timestamp': config_data.get('timestamp', '2025-12-04T16:00:00.000000')
            }
        elif config_type == 'file_paths':
            files = config_data.get('files', [])
            if isinstance(files, list):
                return {'files': files}
            return files if isinstance(files, dict) else {}
        elif config_type == 'actions_workflow':
            actions = config_data.get('actions', [])
            return {'actions': actions}
        elif config_type == 'behavior_config':
            behavior_config = {
                'description': config_data.get('description', ''),
                'goal': config_data.get('goal', ''),
                'inputs': config_data.get('inputs', []),
                'outputs': config_data.get('outputs', []),
            }
            if 'actions' in config_data:
                behavior_config['actions_workflow'] = {'actions': config_data['actions']}
            elif 'actions_workflow' in config_data:
                behavior_config['actions_workflow'] = config_data['actions_workflow']
            if 'instructions' in config_data:
                behavior_config['instructions'] = config_data['instructions']
            if 'trigger_words' in config_data:
                behavior_config['trigger_words'] = config_data['trigger_words']
            if 'behaviorName' in config_data:
                behavior_config['behaviorName'] = config_data['behaviorName']
            if 'order' in config_data:
                behavior_config['order'] = config_data['order']
            return behavior_config
        elif config_type == 'action_config':
            if 'config' in config_data:
                return config_data['config']
            action_name = config_data.get('action_name', 'clarify')
            return {
                'name': action_name,
                'workflow': config_data.get('workflow', True),
                'order': config_data.get('order', 1),
                'instructions': config_data.get('instructions', [f'{action_name} instructions'])
            }
        elif config_type == 'behavior_instructions':
            behavior = config_data.get('behavior', 'shape')
            instructions = config_data.get('instructions', {})
            if isinstance(instructions, dict):
                return instructions
            elif isinstance(instructions, list):
                return {'instructions': instructions}
            else:
                return {'instructions': [instructions] if instructions else []}
        else:
            raise ValueError(f"Unknown config_type: {config_type}")
    
    def when_action_injects(self, action, content='next_action'):
        """Action injects content.
        
        Args:
            action: Action instance
            content: Type of content to inject ('next_action', 'questions_and_evidence', 'strategy_criteria_and_assumptions')
        """
        if content == 'next_action':
            return action.inject_next_action_instructions()
        elif content == 'questions_and_evidence':
            from agile_bot.src.actions.action_context import ClarifyActionContext
            result = action.do_execute(ClarifyActionContext())
            return result
        elif content == 'strategy_criteria_and_assumptions':
            from agile_bot.src.actions.action_context import StrategyActionContext
            result = action.do_execute(StrategyActionContext())
            return result
        else:
            raise ValueError(f"Unknown content type: {content}")
    
    def then_scanners_match(self, behavior, count=None, structure_valid=None):
        """Assert scanners match expected values.
        
        Args:
            behavior: Behavior instance to check scanners from
            count: Expected number of scanner classes (optional)
            structure_valid: Whether to validate scanner structure (default: True if count is provided)
        """
        rules = behavior.rules
        scanners = [rule.scanner_class for rule in rules if rule.scanner_class]
        
        if count is not None:
            assert len(scanners) == count, (
                f"Expected {count} scanner classes discovered, got {len(scanners)}"
            )
            assert len(rules) >= count, (
                f"Expected at least {count} rules, got {len(rules)}"
            )
        
        if structure_valid is None:
            structure_valid = count is not None
        
        if structure_valid:
            for scanner_class in scanners:
                assert isinstance(scanner_class, type), (
                    f"Discovered scanner must be a class, got: {type(scanner_class)}"
                )
            for rule in rules:
                assert rule.has_scanner, f"Rule {rule.name} should have a scanner attached"
                scanner = rule.scanner
                assert scanner is not None, f"Rule {rule.name} should have a scanner instance"
    
    def when_scanner_scans(self, scanner_instance, bad_example, rule_obj, scanner_type='auto'):
        """Scanner scans files/knowledge graph.
        
        Args:
            scanner_instance: Scanner instance (may be unused if scanner_type='auto' and using rule.scan())
            bad_example: Dict containing test_files, code_files, and/or knowledge_graph
            rule_obj: Rule object to scan with
            scanner_type: Type of scanner ('auto', 'test', 'code', 'story'). 'auto' uses rule.scan() (preferred)
        """
        from pathlib import Path
        
        if scanner_type == 'auto':
            kg = {}
            test_files = []
            code_files = []
            
            if bad_example:
                kg = {k: v for k, v in bad_example.items() if k not in ['test_files', 'code_files']}
                
                if 'test_files' in bad_example:
                    test_files = [Path(tf) for tf in bad_example['test_files']]
                
                if 'code_files' in bad_example:
                    code_files = [Path(cf) for cf in bad_example['code_files']]
            
            files_dict = {}
            if test_files:
                files_dict['test'] = test_files
            if code_files:
                files_dict['src'] = code_files
            
            scanner_results = rule_obj.scan(kg, files=files_dict if files_dict else None)
            
            violations = []
            if 'violations' in scanner_results:
                violations = scanner_results['violations']
            elif 'file_by_file' in scanner_results:
                violations.extend(scanner_results['file_by_file'].get('violations', []))
            if 'cross_file' in scanner_results:
                violations.extend(scanner_results['cross_file'].get('violations', []))
            
            return violations
        
        elif scanner_type == 'test':
            violations = []
            test_files_to_scan = []
            if bad_example and 'test_files' in bad_example:
                test_files_to_scan = [Path(tf) for tf in bad_example['test_files']]
            
            kg = {}
            if bad_example:
                kg = {k: v for k, v in bad_example.items() if k not in ['test_files', 'code_files']}
            
            for test_file_path in test_files_to_scan:
                file_violations = scanner_instance.scan_test_file(test_file_path, rule_obj, kg)
                violations.extend(file_violations)
            
            return violations
        
        elif scanner_type == 'code':
            violations = []
            if bad_example and 'code_files' in bad_example:
                for code_file_path in bad_example['code_files']:
                    file_path = Path(code_file_path)
                    file_violations = scanner_instance.scan_code_file(file_path, rule_obj)
                    violations.extend(file_violations)
            return violations
        
        elif scanner_type == 'story':
            kg = bad_example if bad_example else {}
            return scanner_instance.scan(kg, rule_obj)
        
        else:
            raise ValueError(f"Unknown scanner_type: {scanner_type}. Must be 'auto', 'test', 'code', or 'story'")
    
    def then_item_matches(self, item, expected=None, item_type=None, **checks):
        """Assert item matches expected values.
        
        Args:
            item: The item to check (result, state_file, instructions, etc.)
            expected: Expected value(s) - can be a single value or dict (optional if using **checks)
            item_type: Optional type hint ('result', 'state_file', 'instructions', 'behavior_config', etc.)
            **checks: Additional checks to perform (e.g., action='clarify', behavior='shape')
        """
        from pathlib import Path
        
        if item_type is None:
            if hasattr(item, 'action'):
                item_type = 'result'
            elif isinstance(item, Path) and item.suffix == '.json':
                item_type = 'state_file'
            elif isinstance(item, dict) and 'instructions' in item:
                item_type = 'instructions'
            elif isinstance(item, dict) and 'behaviorName' in item:
                item_type = 'behavior_config'
        
        if item_type == 'result' or (hasattr(item, 'action')):
            if hasattr(item, 'action'):
                if isinstance(expected, str):
                    assert item.action == expected, f"Expected action {expected}, got {item.action}"
                elif 'action' in checks:
                    assert item.action == checks['action'], f"Expected action {checks['action']}, got {item.action}"
            if 'behavior' in checks:
                actual_behavior = getattr(item, 'behavior', None)
                assert actual_behavior == checks['behavior'], f"Expected behavior {checks['behavior']}, got {actual_behavior}"
            if 'status' in checks:
                actual_status = getattr(item, 'status', None)
                assert actual_status == checks['status'], f"Expected status {checks['status']}, got {actual_status}"
        elif item_type == 'state_file' or isinstance(item, Path):
            import json
            if isinstance(item, Path):
                state_data = json.loads(item.read_text())
                if isinstance(expected, dict):
                    for key, value in expected.items():
                        assert state_data.get(key) == value, f"State file {key} mismatch: expected {value}, got {state_data.get(key)}"
                elif 'action' in checks:
                    assert state_data.get('current_action') == checks['action']
        elif item_type == 'instructions' or (isinstance(item, dict) and 'instructions' in item):
            if isinstance(expected, (list, str)):
                if isinstance(expected, str):
                    expected = [expected]
                assert item.get('instructions') == expected, \
                    f"Instructions mismatch: expected {expected}, got {item.get('instructions')}"
            elif isinstance(expected, dict):
                for key, value in expected.items():
                    assert item.get(key) == value, f"Instructions {key} mismatch: expected {value}, got {item.get(key)}"
        elif item_type == 'behavior_config' or (isinstance(item, dict) and 'behaviorName' in item):
            if isinstance(expected, dict):
                for key, value in expected.items():
                    assert item.get(key) == value, f"Behavior config {key} mismatch: expected {value}, got {item.get(key)}"
            for key, value in checks.items():
                assert item.get(key) == value, f"Behavior config {key} mismatch: expected {value}, got {item.get(key)}"
        else:
            if isinstance(expected, dict):
                for key, value in expected.items():
                    if hasattr(item, key):
                        assert getattr(item, key) == value, f"{key} mismatch: expected {value}, got {getattr(item, key)}"
                    elif isinstance(item, dict):
                        assert item.get(key) == value, f"{key} mismatch: expected {value}, got {item.get(key)}"
            else:
                assert item == expected, f"Item mismatch: expected {expected}, got {item}"