"""
Invoke CLI Tests

Tests for all stories in the 'Invoke CLI' sub-epic:
- Invoke Bot CLI
- Invoke Bot Behavior CLI  
- Invoke Bot Behavior Action CLI
- Get Help for Command Line Functions
- Detect Trigger Words Through Extension
- Save Through CLI
- CLI Parameter Parsing (infrastructure tests)

Tests use BaseBotCli pattern from cli_invocation_pattern.md.
CLI routes to bot, bot executes. Tests verify CLI routing and bot execution.
"""
import pytest
from pathlib import Path
import json
import argparse
import sys
from conftest import (
    create_bot_config_file,
    create_workflow_state_file,
    create_base_actions_structure
)
from agile_bot.bots.base_bot.test.test_helpers import (
    bootstrap_env, create_behavior_action_instructions,
    then_route_matches_expected, then_cli_result_matches_expected
)
from agile_bot.bots.base_bot.test.test_helpers import (
    create_base_action_instructions
)
from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
from agile_bot.bots.base_bot.src.cli.cli_parameter_parser import CliParameterParser

# ============================================================================
# HELPER CLASSES
# ============================================================================

class TriggerTestSetup:
    """Helper class to set up bot with trigger words for testing."""
    
    def __init__(self, bot_directory: Path, workspace_directory: Path, bot_name: str = 'story_bot'):
        self.bot_directory = bot_directory
        self.workspace_directory = workspace_directory
        self.bot_name = bot_name
        self.behaviors = ['shape', 'prioritization', 'arrange', 'discovery', 'exploration', 'scenarios', 'examples', 'tests']
        # Use actual action names that exist in the codebase and are configured in create_actions_workflow_json
        # Note: create_actions_workflow_json creates: clarify, strategy, validate, render (no 'build' yet)
        self.actions = ['clarify', 'strategy', 'validate', 'render']
        self.bot_config = None
    
    def setup_bot(self):
        """Set up bot with all behaviors and actions."""
        workspace_root = self.bot_directory.parent.parent.parent
        # Ensure bot_config is created in the same location as self.bot_directory
        # setup_bot_for_testing creates in workspace_root/agile_bot/bots/bot_name
        # which should match self.bot_directory (tmp_path/agile_bot/bots/story_bot)
        self.bot_config = setup_bot_for_testing(workspace_root, self.bot_name, self.behaviors)
        # Verify bot_config is in the expected location
        expected_bot_dir = workspace_root / 'agile_bot' / 'bots' / self.bot_name
        if self.bot_directory != expected_bot_dir:
            # If they don't match, create bot_config in self.bot_directory instead
            from agile_bot.bots.base_bot.test.conftest import create_bot_config_file, create_base_actions_structure
            from agile_bot.bots.base_bot.test.test_invoke_cli import _create_base_action_instructions
            self.bot_config = create_bot_config_file(self.bot_directory, self.bot_name, self.behaviors)
            create_base_actions_structure(self.bot_directory)
            _create_base_action_instructions(self.bot_directory)
        self._setup_behavior_folders_and_knowledge_graphs(workspace_root)
        self._create_story_graph_file()
        return self
    
    def _setup_behavior_folders_and_knowledge_graphs(self, workspace_root: Path):
        """Set up behavior folders with behavior.json files and knowledge graph configs."""
        from agile_bot.bots.base_bot.test.test_execute_behavior_actions import create_minimal_guardrails_files
        # Ensure behaviors are created in the same location as bot_directory
        # workspace_root / 'agile_bot' / 'bots' / bot_name should match self.bot_directory
        bot_dir = workspace_root / 'agile_bot' / 'bots' / self.bot_name
        behaviors_dir = bot_dir / 'behaviors'
        for behavior in self.behaviors:
            behavior_dir = behaviors_dir / behavior
            behavior_dir.mkdir(parents=True, exist_ok=True)
            create_actions_workflow_json(bot_dir, behavior)
            # Create minimal guardrails files (required by Guardrails class initialization)
            create_minimal_guardrails_files(bot_dir, behavior, self.bot_name)
            self._create_knowledge_graph_config(behavior_dir)
    
    def _create_knowledge_graph_config(self, behavior_dir: Path):
        """Create knowledge graph folder and config files for a behavior."""
        kg_dir = behavior_dir / 'content' / 'knowledge_graph'
        kg_dir.mkdir(parents=True, exist_ok=True)
        template_filename = 'test_template.json'
        kg_config = {'template': template_filename}
        (kg_dir / 'build_story_graph_outline.json').write_text(
            json.dumps(kg_config), encoding='utf-8'
        )
        template_content = {'instructions': ['Test knowledge graph template']}
        (kg_dir / template_filename).write_text(
            json.dumps(template_content), encoding='utf-8'
        )
    
    def _create_story_graph_file(self):
        """Create story graph file in workspace for validate action."""
        stories_dir = self.workspace_directory / 'docs' / 'stories'
        stories_dir.mkdir(parents=True, exist_ok=True)
        story_graph_file = stories_dir / 'story-graph.json'
        story_graph_file.write_text(json.dumps({
            'epics': [],
            'solution': {'name': 'Test Solution'}
        }), encoding='utf-8')
    
    def add_bot_triggers(self, patterns: list):
        """Add bot-level trigger words."""
        # workspace_root is bot_directory's parent.parent.parent (tmp_path)
        workspace_root = self.bot_directory.parent.parent.parent
        create_bot_trigger_words(workspace_root, self.bot_name, patterns)
        return self
    
    def add_behavior_triggers(self, behavior_patterns: dict):
        """Add behavior-level trigger words.
        
        
        """
        # workspace_root is bot_directory's parent.parent.parent (tmp_path)
        workspace_root = self.bot_directory.parent.parent.parent
        for behavior, patterns in behavior_patterns.items():
            create_behavior_trigger_words(workspace_root, self.bot_name, behavior, patterns)
        return self
    
    def add_action_triggers(self, behavior: str, action: str, patterns: list):
        """Add action-level trigger words."""
        # workspace_root is bot_directory's parent.parent.parent (tmp_path)
        workspace_root = self.bot_directory.parent.parent.parent
        create_action_trigger_words(workspace_root, self.bot_name, behavior, action, patterns)
        return self
    
    def add_all_action_triggers(self, template: str):
        """Add action triggers for all behavior/action combinations using template.
        
        
        """
        for behavior in self.behaviors:
            for action in self.actions:
                trigger = template.format(behavior=behavior, action=action)
                self.add_action_triggers(behavior, action, [trigger])
        return self
    
    def create_workflow_state(self, current_behavior: str, current_action: str):
        """Create workflow state file."""
        return create_workflow_state_file(
            self.workspace_directory,
            self.bot_name,
            current_behavior,
            current_action,
            completed_actions=[]
        )


class TriggerRouterTestHelper:
    
    """Helper class for testing trigger routing and CLI execution."""
    
    def __init__(self, bot_directory: Path, workspace_directory: Path, bot_name: str, bot_config: Path, python_workspace_root: Path = None):
        self.bot_directory = bot_directory
        self.workspace_directory = workspace_directory
        self.bot_name = bot_name
        self.bot_config = bot_config
        self.python_workspace_root = python_workspace_root
        self.router = None
        self.cli = None
    
    def _create_router_and_match(self, trigger_message: str, current_behavior: str = None, current_action: str = None):
        """Helper: Create router and match trigger."""
        # Patch get_python_workspace_root() to return the test's tmp_path where triggers are created
        # This allows BotPaths to always call get_python_workspace_root() (as it should),
        # but in tests, it returns the test root where we create trigger files
        import unittest.mock
        from agile_bot.bots.base_bot.src.bot import workspace as workspace_module
        python_workspace_root = self.bot_directory.parent.parent.parent  # tmp_path where triggers are created
        
        # Patch at both workspace module and bot_paths module level to ensure it works
        with unittest.mock.patch.object(workspace_module, 'get_python_workspace_root', return_value=python_workspace_root):
            # Also patch in bot_paths module in case it has a cached import
            from agile_bot.bots.base_bot.src.bot import bot_paths as bot_paths_module
            with unittest.mock.patch.object(bot_paths_module, 'get_python_workspace_root', return_value=python_workspace_root):
                from agile_bot.bots.base_bot.src.cli.trigger_router import TriggerRouter
                # Use bot_directory and workspace_directory to create router (router will use BotPaths internally)
                # BotPaths will always use get_python_workspace_root() which is patched in tests
                router = TriggerRouter(
                    bot_directory=self.bot_directory, 
                    bot_name=self.bot_name,
                    workspace_path=self.workspace_directory
                )
                return router.match_trigger(
                    message=trigger_message,
                    current_behavior=current_behavior,
                    current_action=current_action
                )
    
    def _create_cli_and_execute(self, route: dict, trigger_message: str):
        """Helper: Create CLI instance and execute route."""
        from agile_bot.bots.base_bot.src.cli.base_bot_cli import BaseBotCli
        from agile_bot.bots.base_bot.test.conftest import bootstrap_env
        
        bootstrap_env(self.bot_directory, self.workspace_directory)
        cli = BaseBotCli(
            bot_name=self.bot_name,
            bot_config_path=self.bot_config
        )
        
        if route.get('action_name') == 'close_current_action':
            result = cli.close_current_action()
        else:
            result = cli.run(
                behavior_name=route.get('behavior_name'),
                action_name=route.get('action_name'),
                context=trigger_message
            )
        
        return result
    
    def match_and_execute(self, trigger_message: str, current_behavior: str = None, current_action: str = None):
        """Match trigger and execute via CLI.
        
        Creates fresh router and CLI instances for each call to avoid state leakage.
        
        
        """
        route = self._create_router_and_match(trigger_message, current_behavior, current_action)
        if route is None:
            return None, None
        
        result = self._create_cli_and_execute(route, trigger_message)
        return route, result
    
    def assert_route(self, route, expected_bot: str, expected_behavior: str, expected_action: str, expected_type: str):
        """Assert route matches expected values."""
        then_route_matches_expected(route, expected_bot, expected_behavior, expected_action, expected_type)
    
    def assert_cli_result(self, result, expected_behavior: str, expected_action: str):
        """Assert CLI result matches expected values."""
        then_cli_result_matches_expected(result, expected_behavior, expected_action)


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

# Consolidated helper functions from test_invoke_bot_cli.py

def create_base_action_instructions_duplicate_removed(bot_directory: Path, action: str) -> Path:
    """Helper: Create base action instructions file in bot directory.
    
    Action folders no longer use numbered prefixes.
    """
    from agile_bot.bots.base_bot.test.test_helpers import get_test_base_actions_dir
    # Use test_base_bot if bot_directory is base_bot
    base_actions_dir = get_test_base_actions_dir(bot_directory)
    # Action folders no longer use numbered prefixes - use action name directly
    base_dir = base_actions_dir / action
    base_dir.mkdir(parents=True, exist_ok=True)
    instructions_file = base_dir / 'instructions.json'
    instructions_data = {
        'actionName': action,
        'instructions': [f'Base {action} instructions']
    }
    instructions_file.write_text(json.dumps(instructions_data), encoding='utf-8')
    return instructions_file

def create_bot_trigger_words(workspace: Path, bot_name: str, patterns: list) -> Path:
    """Helper: Create bot-level trigger words file."""
    trigger_dir = workspace / 'agile_bot' / 'bots' / bot_name
    trigger_dir.mkdir(parents=True, exist_ok=True)
    trigger_file = trigger_dir / 'trigger_words.json'
    trigger_data = {'patterns': patterns}
    trigger_file.write_text(json.dumps(trigger_data), encoding='utf-8')
    return trigger_file

def create_behavior_trigger_words(workspace: Path, bot_name: str, behavior: str, patterns: list) -> Path:
    """Helper: Create behavior-level trigger words in behavior.json (new format)."""
    bot_dir = workspace / 'agile_bot' / 'bots' / bot_name
    # Create or update behavior.json file with trigger words (REQUIRED after refactor)
    behavior_dir = bot_dir / 'behaviors' / behavior
    behavior_dir.mkdir(parents=True, exist_ok=True)
    behavior_file = behavior_dir / 'behavior.json'
    
    create_actions_workflow_json(bot_dir, behavior)
    behavior_data = json.loads(behavior_file.read_text())
    
    # Update trigger_words in behavior.json (router reads from behavior.json now)
    behavior_data['trigger_words'] = {
        'description': f'Trigger words for {behavior}',
        'patterns': patterns,
        'priority': 10
    }
    behavior_file.write_text(json.dumps(behavior_data, indent=2), encoding='utf-8')
    return behavior_file

def create_action_trigger_words(workspace: Path, bot_name: str, behavior: str, action: str, patterns: list) -> Path:
    """Helper: Create action-level trigger words file."""
    action_dir = workspace / 'agile_bot' / 'bots' / bot_name / 'behaviors' / behavior / action
    action_dir.mkdir(parents=True, exist_ok=True)
    trigger_file = action_dir / 'trigger_words.json'
    trigger_data = {'patterns': patterns}
    trigger_file.write_text(json.dumps(trigger_data), encoding='utf-8')
    return trigger_file


def then_verify_route_and_result_for_bot_only(setup, helper, behavior, action, route, result, trigger_message):
    """Then: Verify route and result for bot-only trigger."""
    helper.assert_route(route, setup.bot_name, behavior, action, 'bot_only')
    # Action name should match what was routed to
    helper.assert_cli_result(result, behavior, action)

def then_verify_route_and_result_for_bot_and_behavior(setup, helper, behavior, action, route, result, trigger_message):
    """Then: Verify route and result for bot and behavior trigger."""
    helper.assert_route(route, setup.bot_name, behavior, action, 'bot_and_behavior')
    # Action name should match what was routed to
    helper.assert_cli_result(result, behavior, action)

def then_verify_route_and_result_for_explicit_action(setup, helper, behavior, action, route, result):
    """Then: Verify route and result for explicit action trigger."""
    helper.assert_route(route, setup.bot_name, behavior, action, 'bot_behavior_action')
    # Action name should match what was routed to
    helper.assert_cli_result(result, behavior, action)

def then_verify_close_trigger_route_and_result(setup, route, result):
    """Then: Verify close trigger route and result."""
    assert route is not None, f"Failed for {setup.bot_name}"
    assert route['bot_name'] == setup.bot_name
    assert route['action_name'] == 'close_current_action'
    assert route['match_type'] == 'close'
    assert result['status'] == 'success'

def when_setup_action_triggers_for_all_behaviors(setup, action_trigger_templates: dict):
    """When: Setup action triggers for all behaviors."""
    for behavior in setup.behaviors:
        for action, template in action_trigger_templates.items():
            trigger = template.format(behavior=behavior)
            setup.add_action_triggers(behavior, action, [trigger])

def given_trigger_router_helper_and_message(setup, trigger_message: str):
    """Given step: Create trigger router helper and set trigger message."""
    # Bootstrap environment before creating helper (required for BotPaths)
    from agile_bot.bots.base_bot.test.conftest import bootstrap_env
    bootstrap_env(setup.bot_directory, setup.workspace_directory)
    
    # Patch get_python_workspace_root() to return the test's tmp_path where triggers are created
    # This allows BotPaths to always call get_python_workspace_root() (as it should),
    # but in tests, it returns the test root where we create trigger files
    import unittest.mock
    from agile_bot.bots.base_bot.src.bot import workspace as workspace_module
    python_workspace_root = setup.bot_directory.parent.parent.parent  # tmp_path where triggers are created
    with unittest.mock.patch.object(workspace_module, 'get_python_workspace_root', return_value=python_workspace_root):
        helper = TriggerRouterTestHelper(
            setup.bot_directory, 
            setup.workspace_directory, 
            setup.bot_name, 
            setup.bot_config
        )
        return helper, trigger_message

def when_all_combinations_tested(cli, behaviors, actions, **params):
    """
    Consolidated function for testing all behavior/action combinations.
    Replaces: when_test_all_behavior_action_combinations
    
    Args:
        cli: CLI instance or setup object
        behaviors: List of behaviors to test
        actions: List of actions to test
        **params: Additional parameters:
            - setup: Setup object (if cli is not a setup object)
            - helper: Trigger router helper
            - trigger_message: Trigger message to test
            - verify_func: Verification function
            - current_behavior: Current behavior (if None, tests all)
            - current_action: Current action (if None, tests all)
    """
    setup = params.get('setup', cli)
    helper = params.get('helper')
    trigger_message = params.get('trigger_message', '')
    verify_func = params.get('verify_func')
    current_behavior = params.get('current_behavior')
    current_action = params.get('current_action')
    
    if helper is None or verify_func is None:
        raise ValueError("helper and verify_func parameters required")
    
    for behavior in (behaviors if current_behavior is None else [current_behavior]):
        for action in (actions if current_action is None else [current_action]):
            setup.create_workflow_state(behavior, action)
            route, result = helper.match_and_execute(
                trigger_message,
                current_behavior=behavior,
                current_action=action
            )
            verify_func(setup, helper, behavior, action, route, result, trigger_message)

def given_behavior_triggers_dict(behavior=None, triggers=None):
    """
    Consolidated function for creating behavior triggers dictionary.
    Replaces: given_standard_behavior_triggers_dict
    
    Args:
        behavior: Behavior name (if None, returns all standard behaviors)
        triggers: Custom triggers dict (if None, uses standard triggers)
    
    Returns:
        Dictionary mapping behavior names to trigger strings
    """
    if triggers is not None:
        return triggers
    
    standard_triggers = {
        'shape': 'kick off shaping for a new feature',
        'prioritization': 'rank the backlog for launch',
        'arrange': 'arrange the feature map layout',
        'discovery': 'start discovery for the new product',
        'exploration': 'begin the exploration phase',
        'scenarios': 'draft behavior scenarios',
        'examples': 'prepare usage examples',
        'tests': 'design test coverage'
    }
    
    if behavior is None:
        return standard_triggers
    elif behavior in standard_triggers:
        return {behavior: standard_triggers[behavior]}
    else:
        return {}

def given_setup(setup_type, bot_directory, **setup_params):
    """
    Consolidated function for INVOKE CLI setup.
    Replaces: given_bot_setup_with_triggers, given_bot_setup_with_behavior_triggers
    
    Args:
        setup_type: Type of setup ('bot_with_triggers')
        bot_directory: Bot directory path
        **setup_params: Additional parameters:
            - workspace_directory: Workspace directory path (required)
            - behaviors: List of behavior names (optional, defaults to standard behaviors)
            - triggers: Dict of triggers (for 'bot_with_triggers' setup_type)
            - behavior_triggers: Dict mapping behavior names to trigger patterns
    
    Returns:
        TriggerTestSetup object
    """
    workspace_directory = setup_params.get('workspace_directory')
    if workspace_directory is None:
        raise ValueError("workspace_directory is required")
    
    if setup_type == 'bot_with_triggers':
        triggers = setup_params.get('triggers')
        behavior_triggers = setup_params.get('behavior_triggers')
        
        setup = TriggerTestSetup(bot_directory, workspace_directory).setup_bot()
        
        if behavior_triggers:
            # Convert behavior_triggers dict to format expected by add_behavior_triggers
            behavior_patterns = {behavior: [trigger] for behavior, trigger in behavior_triggers.items()}
            setup.add_behavior_triggers(behavior_patterns)
        elif triggers:
            # If triggers is provided as a list, add as bot triggers
            setup.add_bot_triggers(triggers)
        
        return setup
    else:
        raise ValueError(f"Unknown setup_type: {setup_type}")

def given_action_trigger_templates_dict():
    """Given: Action trigger templates dictionary."""
    return {
        'clarify': 'gather context for {behavior}',
        'strategy': 'decide planning criteria for {behavior}',
        'render': 'render outputs for {behavior}',
        'validate': 'validate outputs for {behavior}'
    }

def given_bot_setup_with_action_triggers(bot_directory: Path, workspace_directory: Path, action_trigger_templates: dict):
    """Given: Bot setup with action triggers."""
    return TriggerTestSetup(bot_directory, workspace_directory).setup_bot()

def when_cli_created_with_mock_bot(mock_bot):
    """When: CLI created with mock bot."""
    from agile_bot.bots.base_bot.src.cli.base_bot_cli import BaseBotCli
    return BaseBotCli(bot=mock_bot)

def given_behavior_triggers_dictionary():
    """Given step: Create behavior triggers dictionary."""
    return {
        'shape': 'kick off shaping for a new feature',
        'prioritization': 'rank the backlog for launch',
        'arrange': 'organize the stories',
        'discovery': 'discover the user flows',
        'exploration': 'explore the domain',
        'scenarios': 'write the scenarios',
        'examples': 'create examples',
        'tests': 'write the tests'
    }

def when_test_all_behaviors_with_triggers(setup, helper, behavior_triggers: dict, verify_func):
    """When step: Test all behaviors with their triggers."""
    for behavior, trigger_message in behavior_triggers.items():
        for current_action in setup.actions:
            setup.create_workflow_state(behavior, current_action)
            route, result = helper.match_and_execute(
                trigger_message,
                current_behavior=behavior,
                current_action=current_action
            )
            verify_func(setup, helper, behavior, current_action, route, result, trigger_message)

def given_action_trigger_templates_dictionary():
    """Given step: Create action trigger templates dictionary."""
    return {
        'clarify': 'gather context for {behavior}',
        'strategy': 'decide planning criteria for {behavior}',
        'build': 'build knowledge for {behavior}',
        'validate': 'validate rules for {behavior}',
        'render': 'render output for {behavior}'
    }

def when_test_all_behaviors_with_action_templates(setup, helper, action_trigger_templates: dict, verify_func):
    """When step: Test all behaviors with action trigger templates."""
    for behavior in setup.behaviors:
        for action, template in action_trigger_templates.items():
            trigger_message = template.format(behavior=behavior)
            route, result = helper.match_and_execute(
                trigger_message,
                current_behavior=None,  # Not needed for explicit triggers
                current_action=None
            )
            verify_func(setup, helper, behavior, action, route, result)

def _create_base_action_instructions(bot_directory: Path):
    """Helper: Create base action instructions in bot directory."""
    actions = ['initialize_workspace', 'gather_context', 'decide_planning_criteria', 
               'build_knowledge', 'validate', 'render']
    for action in actions:
        create_base_action_instructions(bot_directory, action)

def setup_bot_for_testing(workspace_root: Path, bot_name: str, behaviors: list):
    """Helper: Set up complete bot structure for testing.
    
    
    """
    bot_dir = workspace_root / 'agile_bot' / 'bots' / bot_name
    bot_config = create_bot_config_file(bot_dir, bot_name, behaviors)
    create_base_actions_structure(bot_dir)
    _create_base_action_instructions(bot_dir)
    return bot_config


# ============================================================================
# FIXTURES
# ============================================================================

@pytest.fixture
def workspace_root(tmp_path):
    """Fixture: Temporary workspace directory."""
    workspace = tmp_path
    return workspace

# ============================================================================
# TEST CLASSES - Detect Trigger Words Through Extension
# ============================================================================

class TestDetectTriggerWordsThroughExtension:
    """Story: Detect Trigger Words Through Extension (Sub-epic: Invoke CLI)"""

    def test_trigger_bot_only_no_behavior_or_action_specified(self, bot_directory, workspace_directory):
        """
        SCENARIO: Trigger bot only (no behavior or action specified)
        GIVEN: user types message containing trigger words
        AND: bot is at specific behavior and action from workflow state
        WHEN: Extension intercepts user message
        THEN: Extension identifies target bot from trigger patterns
        AND: Extension routes to bot using current behavior and action from state
        AND: CLI executes current behavior and action
        """
        # Arrange: Set up bot with bot-level triggers
        setup = TriggerTestSetup(bot_directory, workspace_directory).setup_bot().add_bot_triggers([
            'lets work on stories',
            'time to kick off stories',
            'ready to work on stories'
        ])
        
        # Given: Trigger router helper and message
        helper, trigger_message = given_trigger_router_helper_and_message(setup, 'lets work on stories')
        
        # When: Test all behavior/action combinations
        when_all_combinations_tested(setup, setup.behaviors, setup.actions, 
                                     helper=helper, trigger_message=trigger_message, 
                                     verify_func=then_verify_route_and_result_for_bot_only)

    def test_trigger_bot_and_behavior_no_action_specified(self, bot_directory, workspace_directory):
        """
        SCENARIO: Trigger bot and behavior (no action specified)
        GIVEN: user types message containing behavior-specific trigger words
        AND: behavior is at specific action from workflow state
        WHEN: Extension intercepts user message
        THEN: Extension identifies bot and behavior from trigger patterns
        AND: Extension routes to behavior using current action from state
        AND: CLI executes behavior with current action
        """
        # Arrange: Set up bot with behavior-level triggers
        behavior_triggers = given_behavior_triggers_dict()
        setup = given_setup('bot_with_triggers', bot_directory, workspace_directory=workspace_directory, behavior_triggers=behavior_triggers)
        
        # Given: Trigger router helper
        helper, _ = given_trigger_router_helper_and_message(setup, '')
        
        # When: Test all behaviors with triggers
        when_test_all_behaviors_with_triggers(setup, helper, behavior_triggers, then_verify_route_and_result_for_bot_and_behavior)

    def test_trigger_bot_behavior_and_action_explicitly(self, bot_directory, workspace_directory):
        """
        SCENARIO: Trigger bot, behavior, and action explicitly
        GIVEN: user types message containing action-specific trigger words
        WHEN: Extension intercepts user message
        THEN: Extension identifies bot, behavior, and action from trigger patterns
        AND: Extension routes directly to specified action
        AND: CLI executes specified action
        """
        # Arrange: Set up bot with action-level triggers for all combinations
        action_trigger_templates = given_action_trigger_templates_dict()
        setup = given_bot_setup_with_action_triggers(bot_directory, workspace_directory, action_trigger_templates)
        
        when_setup_action_triggers_for_all_behaviors(setup, action_trigger_templates)
        
        # Given: Trigger router helper
        helper, _ = given_trigger_router_helper_and_message(setup, '')
        
        # When: Test all behaviors with action templates
        when_test_all_behaviors_with_action_templates(setup, helper, action_trigger_templates, then_verify_route_and_result_for_explicit_action)
    
    def test_trigger_close_current_action(self, bot_directory, workspace_directory):
        """
        SCENARIO: Trigger close current action
        GIVEN: user types message containing close trigger words
        AND: bot is at specific behavior and action from workflow state
        WHEN: Extension intercepts user message
        THEN: Extension identifies close action from trigger patterns
        AND: Extension routes to close_current_action
        AND: CLI closes current action and advances workflow
        """
        # Arrange: Set up bot with close trigger words
        setup = TriggerTestSetup(bot_directory, workspace_directory).setup_bot().add_bot_triggers([
            'close current action',
            'done with this step',
            'continue to next action'
        ])
        
        # Given: Trigger router helper and message
        helper, trigger_message = given_trigger_router_helper_and_message(setup, 'done with this step')
        
        # When: Test all behavior/action combinations for close trigger
        def verify_close(setup, helper, behavior, action, route, result, trigger_message):
            then_verify_close_trigger_route_and_result(setup, route, result)
        when_all_combinations_tested(setup, setup.behaviors, setup.actions, 
                                     helper=helper, trigger_message=trigger_message, 
                                     verify_func=verify_close)


# ============================================================================
# EXCEPTION HANDLING TESTS
# ============================================================================

def given_mock_bot_created(tmp_path: Path, bot_name: str = 'test_bot'):
    """Given: Mock bot created."""
    from unittest.mock import Mock
    mock_bot = Mock()
    mock_bot.name = bot_name
    mock_bot.bot_directory = tmp_path / bot_name
    return mock_bot


def when_cli_infers_parameter_description_for_unknown_command(cli):
    """When: CLI infers parameter description for unknown command."""
    from agile_bot.bots.base_bot.src.cli.base_bot_cli import BaseBotCli
    return cli._infer_parameter_description(
        cmd_name='unknown_command_xyz',
        param_num='1',
        cmd_content=''
    )


class TestCLIExceptions:
    """Tests for CLI exception handling - no fallbacks."""

    def test_cli_returns_generic_description_for_unknown_command(self, tmp_path):
        """
        SCENARIO: CLI returns generic description when parameter description cannot be inferred
        GIVEN: Mock bot is created
        WHEN: CLI is created with mock bot
        AND: Inferring parameter description for unknown command
        THEN: Generic description is returned (graceful fallback)
        """
        # Given: Mock bot is created
        mock_bot = given_mock_bot_created(tmp_path)
        
        # When: CLI is created with mock bot
        cli = when_cli_created_with_mock_bot(mock_bot)
        
        # When: Inferring parameter description for unknown command
        # Then: Returns a generic description (graceful fallback instead of error)
        description = when_cli_infers_parameter_description_for_unknown_command(cli)
        # The implementation returns 'Optional action name' for param 1, or 'Parameter N' for unknown params
        assert description is not None
        assert len(description) > 0


# ============================================================================
# HELPER FUNCTIONS - Domain Classes (Stories 1-2: TriggerWords)
# ============================================================================

from unittest.mock import Mock
from agile_bot.bots.base_bot.src.bot.trigger_words import TriggerWords
from agile_bot.bots.base_bot.src.bot.behavior import Behavior  # BehaviorConfig merged into Behavior


def given_behavior_config_with_trigger_patterns(patterns: list, priority: int = 0):
    """Given: Behavior with trigger patterns (BehaviorConfig merged into Behavior)."""
    behavior_config = Mock(spec=Behavior)
    behavior_config.trigger_words = {
        'patterns': patterns,
        'priority': priority
    }
    return behavior_config


def given_behavior_config_with_list_triggers(patterns: list):
    """Given: Behavior with list trigger words (BehaviorConfig merged into Behavior)."""
    behavior_config = Mock(spec=Behavior)
    behavior_config.trigger_words = patterns
    return behavior_config


def given_behavior_config_with_no_triggers():
    """Given: Behavior with no trigger words (BehaviorConfig merged into Behavior)."""
    behavior_config = Mock(spec=Behavior)
    behavior_config.trigger_words = None
    return behavior_config


def when_trigger_words_instantiated(behavior_config, behavior=None):
    """When: TriggerWords instantiated."""
    # TriggerWords only takes behavior_config, not behavior parameter
    return TriggerWords(behavior_config)


def when_matches_called(trigger_words: TriggerWords, text: str):
    """When: matches() called."""
    return trigger_words.matches(text)


def when_priority_accessed(trigger_words: TriggerWords):
    """When: priority property accessed."""
    return trigger_words.priority


def then_priority_is(result: int, expected: int):
    """Then: Priority is expected value."""
    assert result == expected


def then_matches_returns(result: bool, expected: bool):
    """Then: Matches returns expected value."""
    assert result == expected


# ============================================================================
# TEST CLASSES - Domain Classes (Stories 1-2: TriggerWords)
# ============================================================================

class TestGetTriggerPriority:
    """Story: Get Trigger Priority (Sub-epic: Invoke CLI)"""
    
def given_behavior_config_from_trigger_config(trigger_config):
    """Given: BehaviorConfig from trigger configuration."""
    if isinstance(trigger_config, dict):
        return given_behavior_config_with_trigger_patterns(
            trigger_config.get('patterns', []),
            trigger_config.get('priority', 0)
        )
    else:
        return given_behavior_config_with_list_triggers(trigger_config)


class TestGetTriggerPriority:
    """Story: Get Trigger Priority (Sub-epic: Invoke CLI)"""
    
    @pytest.mark.parametrize("trigger_config,expected_priority", [
        # Example 1: Priority configured
        ({'patterns': ['test'], 'priority': 5}, 5),
        # Example 2: No priority field
        ({'patterns': ['test']}, 0),
        # Example 3: List trigger format
        (['test', 'pattern'], 0),
    ])
    def test_priority_property_returns_configured_priority_or_zero(self, trigger_config, expected_priority):
        """
        SCENARIO: Priority property returns configured priority or zero
        GIVEN: BehaviorConfig with different trigger configurations
        WHEN: priority property accessed
        THEN: Returns configured priority when available, otherwise returns 0
        """
        # Given: BehaviorConfig with trigger configuration
        behavior_config = given_behavior_config_from_trigger_config(trigger_config)
        
        # When: TriggerWords instantiated and priority accessed
        trigger_words = when_trigger_words_instantiated(behavior_config)
        result = when_priority_accessed(trigger_words)
        
        # Then: Priority is expected value
        then_priority_is(result, expected_priority)


class TestMatchTextAgainstTriggers:
    """Story: Match Text Against Triggers (Sub-epic: Invoke CLI)"""
    
    def test_matches_returns_true_when_text_matches_any_pattern(self):
        """
        SCENARIO: Matches returns true when text matches any pattern
        GIVEN: BehaviorConfig with multiple patterns ['test', 'pattern', 'xyz']
        WHEN: matches() called with text 'This is a test'
        THEN: Returns True
        """
        # Given: BehaviorConfig with multiple patterns
        behavior_config = given_behavior_config_with_trigger_patterns(['test', 'pattern', 'xyz'])
        
        # When: TriggerWords instantiated and matches() called
        trigger_words = when_trigger_words_instantiated(behavior_config)
        result = when_matches_called(trigger_words, 'This is a test')
        
        # Then: Returns True
        then_matches_returns(result, True)
    
    def test_matches_returns_false_when_no_patterns_match(self):
        """
        SCENARIO: Matches returns false when no patterns match
        GIVEN: BehaviorConfig with patterns ['xyz', 'abc']
        WHEN: matches() called with text 'This is a test'
        THEN: Returns False
        """
        # Given: BehaviorConfig with patterns
        behavior_config = given_behavior_config_with_trigger_patterns(['xyz', 'abc'])
        
        # When: TriggerWords instantiated and matches() called
        trigger_words = when_trigger_words_instantiated(behavior_config)
        result = when_matches_called(trigger_words, 'This is a test')
        
        # Then: Returns False
        then_matches_returns(result, False)
    
    def test_matches_returns_false_when_no_triggers_configured(self):
        """
        SCENARIO: Matches returns false when no triggers configured
        GIVEN: BehaviorConfig with no triggers
        WHEN: matches() called with text 'This is a test'
        THEN: Returns False
        """
        # Given: BehaviorConfig with no triggers
        behavior_config = given_behavior_config_with_no_triggers()
        
        # When: TriggerWords instantiated and matches() called
        trigger_words = when_trigger_words_instantiated(behavior_config)
        result = when_matches_called(trigger_words, 'This is a test')
        
        # Then: Returns False
        then_matches_returns(result, False)
    
    def test_matches_works_with_list_trigger_format(self):
        """
        SCENARIO: Matches works with list trigger format
        GIVEN: BehaviorConfig with list triggers ['test', 'pattern']
        WHEN: matches() called with text 'This is a test'
        THEN: Returns True
        """
        # Given: BehaviorConfig with list triggers
        behavior_config = given_behavior_config_with_list_triggers(['test', 'pattern'])
        
        # When: TriggerWords instantiated and matches() called
        trigger_words = when_trigger_words_instantiated(behavior_config)
        result = when_matches_called(trigger_words, 'This is a test')
        
        # Then: Returns True
        then_matches_returns(result, True)
    
    def test_matches_checks_all_patterns_until_match_found(self):
        """
        SCENARIO: Matches checks all patterns until match found
        GIVEN: BehaviorConfig with patterns ['xyz', 'abc', 'test']
        WHEN: matches() called with text 'This is a test'
        THEN: Returns True (third pattern matches)
        """
        # Given: BehaviorConfig with patterns
        behavior_config = given_behavior_config_with_trigger_patterns(['xyz', 'abc', 'test'])
        
        # When: TriggerWords instantiated and matches() called
        trigger_words = when_trigger_words_instantiated(behavior_config)
        result = when_matches_called(trigger_words, 'This is a test')
        
        # Then: Returns True
        then_matches_returns(result, True)
    
    def test_matches_handles_regex_patterns(self):
        """
        SCENARIO: Matches handles regex patterns
        GIVEN: BehaviorConfig with regex pattern 'test.*pattern'
        WHEN: matches() called with text 'test this pattern'
        THEN: Returns True
        """
        # Given: BehaviorConfig with regex pattern
        behavior_config = given_behavior_config_with_trigger_patterns(['test.*pattern'])
        
        # When: TriggerWords instantiated and matches() called
        trigger_words = when_trigger_words_instantiated(behavior_config)
        result = when_matches_called(trigger_words, 'test this pattern')
        
        # Then: Returns True
        then_matches_returns(result, True)
    
    def test_matches_is_case_insensitive(self):
        """
        SCENARIO: Matches is case insensitive
        GIVEN: BehaviorConfig with pattern 'TEST'
        WHEN: matches() called with text 'this is a test'
        THEN: Returns True (case insensitive)
        """
        # Given: BehaviorConfig with pattern
        behavior_config = given_behavior_config_with_trigger_patterns(['TEST'])
        
        # When: TriggerWords instantiated and matches() called
        trigger_words = when_trigger_words_instantiated(behavior_config)
        result = when_matches_called(trigger_words, 'this is a test')
        
        # Then: Returns True
        then_matches_returns(result, True)
    
    def test_matches_handles_invalid_regex_patterns_by_falling_back_to_literal(self):
        """
        SCENARIO: Matches handles invalid regex patterns by falling back to literal
        GIVEN: BehaviorConfig with invalid regex pattern '['
        WHEN: matches() called with text 'This contains [ bracket'
        THEN: Returns True (fallback to literal matching)
        """
        # Given: BehaviorConfig with invalid regex pattern
        behavior_config = given_behavior_config_with_trigger_patterns(['['])
        
        # When: TriggerWords instantiated and matches() called
        trigger_words = when_trigger_words_instantiated(behavior_config)
        result = when_matches_called(trigger_words, 'This contains [ bracket')
        
        # Then: Returns True
        then_matches_returns(result, True)


# ============================================================================
# CLI PARAMETER PARSING TESTS (Infrastructure)
# ============================================================================

# HELPER FUNCTIONS - Reusable test operations

def create_params_with_scope(scope_string):
    return {'scope': scope_string}

def create_params_with_multiple_keys(**kwargs):
    return kwargs

def create_cli_args_namespace(**kwargs):
    defaults = {
        'behavior': 'code',
        'action': 'validate',
        'scope': None,
        'skip_cross_file': False,
        'user_message': None,
        'skiprule': None,
        'exclude': None
    }
    defaults.update(kwargs)
    return argparse.Namespace(**defaults)

def verify_scope_contains_files(scope_dict, expected_files):
    assert isinstance(scope_dict, dict)
    assert scope_dict['type'] == 'files'
    assert scope_dict['value'] == expected_files

def verify_scope_has_file_count(scope_dict, expected_count):
    assert isinstance(scope_dict, dict)
    assert len(scope_dict['value']) == expected_count

def simulate_cli_invocation(cli_args_list):
    original_argv = sys.argv
    sys.argv = ['test'] + cli_args_list
    try:
        args, params = CliParameterParser.parse_arguments()
        return args, params
    finally:
        sys.argv = original_argv

def create_validation_cli_args(scope_value):
    return [
        '--behavior', 'code',
        '--action', 'validate',
        '--scope', scope_value
    ]

def verify_json_array_not_corrupted(normalized_string, expected_values):
    parsed_scope = json.loads(normalized_string)
    assert isinstance(parsed_scope['value'], list)
    assert len(parsed_scope['value']) == len(expected_values)
    for i, expected_value in enumerate(expected_values):
        assert parsed_scope['value'][i] == expected_value
    assert '["' not in normalized_string or normalized_string.count('["') == 1
    assert '"]' not in normalized_string or normalized_string.count('"]') == 1


# FIXTURES - Test setup

@pytest.fixture
def python_dict_with_single_file():
    return "{'type': 'files', 'value': ['file1.py']}"

@pytest.fixture
def python_dict_with_multiple_files():
    return "{'type': 'files', 'value': ['file1.py', 'file2.py', 'file3.py']}"

@pytest.fixture
def json_string_with_double_quotes():
    return '{"type": "files", "value": ["file1.py"]}'


# ORCHESTRATOR TESTS - Test flows with Given-When-Then

class TestCliAcceptsScopeWithPythonDictSyntax:
    
    def test_cli_accepts_scope_with_single_file_when_python_dict_syntax_used(self, python_dict_with_single_file):
        # Given: Parameters with scope as Python dict string
        params = create_params_with_scope(python_dict_with_single_file)
        
        # When: Parameters are processed
        processed_params = CliParameterParser._parse_json_parameters(params)
        
        # Then: Scope becomes dict object with file
        verify_scope_contains_files(processed_params['scope'], ['file1.py'])
    
    def test_cli_accepts_scope_with_multiple_files_when_python_dict_syntax_used(self, python_dict_with_multiple_files):
        # Given: Parameters with scope containing multiple files
        params = create_params_with_scope(python_dict_with_multiple_files)
        
        # When: Parameters are processed
        processed_params = CliParameterParser._parse_json_parameters(params)
        
        # Then: All files are preserved
        verify_scope_has_file_count(processed_params['scope'], 3)
        verify_scope_contains_files(processed_params['scope'], ['file1.py', 'file2.py', 'file3.py'])
    
    def test_cli_accepts_scope_with_json_syntax_when_double_quotes_used(self, json_string_with_double_quotes):
        # Given: Parameters with scope as valid JSON
        params = create_params_with_scope(json_string_with_double_quotes)
        
        # When: Parameters are processed
        processed_params = CliParameterParser._parse_json_parameters(params)
        
        # Then: Scope becomes dict object
        verify_scope_contains_files(processed_params['scope'], ['file1.py'])
    
    def test_cli_preserves_nested_paths_when_scope_has_subdirectories(self):
        # Given: Parameters with nested file paths
        params = create_params_with_scope("{'type': 'files', 'value': ['dir/file1.py', 'dir/subdir/file2.py']}")
        
        # When: Parameters are processed
        processed_params = CliParameterParser._parse_json_parameters(params)
        
        # Then: Nested paths are preserved
        scope_files = processed_params['scope']['value']
        assert scope_files[0] == 'dir/file1.py'
        assert scope_files[1] == 'dir/subdir/file2.py'
    
    def test_cli_preserves_exclude_patterns_when_scope_has_exclusions(self):
        # Given: Parameters with scope containing exclude patterns
        params = create_params_with_scope("{'type': 'files', 'value': ['file1.py'], 'exclude': ['*test*']}")
        
        # When: Parameters are processed
        processed_params = CliParameterParser._parse_json_parameters(params)
        
        # Then: Exclude patterns are preserved
        assert processed_params['scope']['exclude'] == ['*test*']
    
    def test_cli_keeps_regular_strings_unchanged_when_not_json(self):
        # Given: Parameters with regular string values
        params = create_params_with_multiple_keys(
            user_message='Hello world',
            behavior='code'
        )
        
        # When: Parameters are processed
        processed_params = CliParameterParser._parse_json_parameters(params)
        
        # Then: Strings remain unchanged
        assert processed_params['user_message'] == 'Hello world'
        assert processed_params['behavior'] == 'code'
    
    def test_cli_handles_malformed_scope_gracefully_when_syntax_invalid(self):
        # Given: Parameters with malformed scope string
        params = create_params_with_scope("{'type': 'files', 'value': [unclosed")
        
        # When: Parameters are processed
        processed_params = CliParameterParser._parse_json_parameters(params)
        
        # Then: Scope remains as string
        assert isinstance(processed_params['scope'], str)


class TestCliNormalizesPythonDictToJson:
    
    def test_cli_replaces_single_quotes_with_double_quotes_when_normalizing(self):
        # Given: Python dict string with single quotes
        python_dict_string = "{'key': 'value'}"
        
        # When: String is normalized
        normalized_string = CliParameterParser._try_fix_json(python_dict_string)
        
        # Then: Single quotes become double quotes
        assert normalized_string == '{"key": "value"}'
    
    def test_cli_normalizes_array_syntax_when_python_list_used(self):
        # Given: Python dict with list using single quotes
        python_dict_string = "{'files': ['file1.py', 'file2.py']}"
        
        # When: String is normalized
        normalized_string = CliParameterParser._try_fix_json(python_dict_string)
        
        # Then: Array becomes valid JSON array
        assert normalized_string == '{"files": ["file1.py", "file2.py"]}'
    
    def test_cli_preserves_json_when_already_valid(self):
        # Given: Already valid JSON string
        json_string = '{"type": "files", "value": ["file.py"]}'
        
        # When: String is normalized
        normalized_string = CliParameterParser._try_fix_json(json_string)
        
        # Then: JSON remains unchanged
        assert normalized_string == json_string


class TestCliBuildsParametersFromArguments:
    
    def test_cli_recognizes_scope_as_dict_when_building_parameters(self):
        # Given: Arguments with scope as Python dict string
        args = create_cli_args_namespace(
            scope="{'type': 'files', 'value': ['file1.py']}"
        )
        
        # When: Parameters are built from arguments
        params = CliParameterParser._build_params_from_args(args, [])
        
        # Then: Scope is dict object
        verify_scope_contains_files(params['scope'], ['file1.py'])
    
    def test_cli_preserves_boolean_flags_when_building_parameters(self):
        # Given: Arguments with skip_cross_file flag set
        args = create_cli_args_namespace(skip_cross_file=True)
        
        # When: Parameters are built from arguments
        params = CliParameterParser._build_params_from_args(args, [])
        
        # Then: Flag is preserved
        assert params['skip_cross_file'] is True


class TestCliHandlesScopeInRealUsage:
    
    def test_cli_accepts_single_file_scope_when_validating_one_file(self):
        # Given: CLI invoked with scope for single file
        cli_args = create_validation_cli_args("{'type': 'files', 'value': ['agile_bot/bots/base_bot/src/actions/instructions.py']}")
        cli_args.append('--skip-cross-file')
        
        # When: CLI processes arguments
        args, params = simulate_cli_invocation(cli_args)
        
        # Then: Scope contains exactly one file
        assert params['scope']['value'][0] == 'agile_bot/bots/base_bot/src/actions/instructions.py'
        assert params.get('skip_cross_file') is True
    
    def test_cli_accepts_multiple_files_scope_when_validating_many_files(self):
        # Given: CLI invoked with scope for multiple files
        cli_args = create_validation_cli_args("{'type': 'files', 'value': ['file1.py', 'file2.py', 'file3.py']}")
        
        # When: CLI processes arguments
        args, params = simulate_cli_invocation(cli_args)
        
        # Then: Scope contains all files
        verify_scope_has_file_count(params['scope'], 3)
        assert 'file1.py' in params['scope']['value']
        assert 'file2.py' in params['scope']['value']
        assert 'file3.py' in params['scope']['value']
    
    def test_cli_handles_windows_paths_when_scope_uses_backslashes(self):
        # Given: CLI invoked with Windows-style paths
        cli_args = create_validation_cli_args("{'type': 'files', 'value': ['agile_bot\\\\bots\\\\base_bot\\\\src\\\\file.py']}")
        
        # When: CLI processes arguments
        args, params = simulate_cli_invocation(cli_args)
        
        # Then: Windows paths are preserved
        assert 'agile_bot\\bots\\base_bot\\src\\file.py' in params['scope']['value'][0]


class TestCliPreservesArrayValuesInScope:
    
    def test_cli_does_not_corrupt_array_values_when_normalizing_syntax(self):
        # Given: Python dict with array values
        python_dict_string = "{'type': 'files', 'value': ['file1.py', 'file2.py']}"
        
        # When: String is normalized
        normalized_string = CliParameterParser._try_fix_json(python_dict_string)
        
        # Then: Array values are NOT mangled
        verify_json_array_not_corrupted(normalized_string, ['file1.py', 'file2.py'])
