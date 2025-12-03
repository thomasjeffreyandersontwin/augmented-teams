"""
Base Bot Tool Invocation Tests

Tests bot tool invocation behavior following orchestrator pattern:
- Test methods show Given-When-Then flow (under 20 lines)
- Helper functions provide reusable operations (under 20 lines)
- Tests verify observable behavior through public API
- Uses real implementations with temporary files
"""
import pytest
from pathlib import Path
import json
from unittest.mock import Mock, patch

# ============================================================================
# HELPER FUNCTIONS - Reusable test operations
# ============================================================================

def create_bot_config_file(workspace: Path, bot_name: str, behaviors: list) -> Path:
    """Helper: Create bot configuration file with behaviors."""
    config_dir = workspace / 'agile_bot' / 'bots' / bot_name / 'config'
    config_dir.mkdir(parents=True, exist_ok=True)
    config_file = config_dir / 'bot_config.json'
    config_data = {
        'name': bot_name,
        'behaviors': behaviors
    }
    config_file.write_text(json.dumps(config_data), encoding='utf-8')
    return config_file

def create_behavior_action_instructions(workspace: Path, bot_name: str, behavior: str, action: str) -> Path:
    """Helper: Create behavior action instructions file."""
    instructions_dir = workspace / 'agile_bot' / 'bots' / bot_name / 'behaviors' / behavior / action
    instructions_dir.mkdir(parents=True, exist_ok=True)
    instructions_file = instructions_dir / 'instructions.json'
    instructions_data = {
        'action': action,
        'behavior': behavior,
        'instructions': [f'{action} instructions for {behavior}']
    }
    instructions_file.write_text(json.dumps(instructions_data), encoding='utf-8')
    return instructions_file

def create_base_action_instructions(workspace: Path, action: str) -> Path:
    """Helper: Create base action instructions file with numbered prefix."""
    # Map action names to their numbered prefixes
    action_prefixes = {
        'gather_context': '2_gather_context',
        'decide_planning_criteria': '3_decide_planning_criteria',
        'build_knowledge': '4_build_knowledge',
        'render_output': '5_render_output',
        'correct_bot': 'correct_bot',
        'validate_rules': '7_validate_rules'
    }
    
    action_folder = action_prefixes.get(action, action)
    base_dir = workspace / 'agile_bot' / 'bots' / 'base_bot' / 'base_actions' / action_folder
    base_dir.mkdir(parents=True, exist_ok=True)
    instructions_file = base_dir / 'instructions.json'
    instructions_data = {
        'actionName': action,
        'instructions': [f'Base {action} instructions']
    }
    instructions_file.write_text(json.dumps(instructions_data), encoding='utf-8')
    return instructions_file

def verify_tool_routes_to_behavior(tool_name: str, expected_behavior: str, expected_action: str):
    """Helper: Verify tool routes to correct behavior action."""
    assert expected_behavior in tool_name.lower()
    assert expected_action in tool_name.lower()

# ============================================================================
# FIXTURES - Test setup
# ============================================================================

@pytest.fixture
def workspace_root(tmp_path):
    """Fixture: Temporary workspace directory."""
    workspace = tmp_path / 'workspace'
    workspace.mkdir()
    return workspace

@pytest.fixture
def test_bot_config(workspace_root):
    """Fixture: Test bot configuration."""
    return create_bot_config_file(
        workspace_root,
        'test_bot',
        ['shape', 'discovery', 'exploration', 'specification']
    )

# ============================================================================
# ORCHESTRATOR TESTS - Test flows with Given-When-Then
# ============================================================================

class TestBotToolInvocation:
    """Bot tool invocation behavior tests."""

    def test_tool_invokes_behavior_action_when_called(self, workspace_root, test_bot_config):
        """
        SCENARIO: AI Chat invokes test_bot_shape_gather_context tool
        GIVEN: Bot has behavior 'shape' with action 'gather_context'
        WHEN: AI Chat invokes tool with parameters behavior='shape', action='gather_context'
        THEN: Tool routes to test_bot.Shape.GatherContext() method
        """
        # Given: Bot configuration and instructions exist
        create_behavior_action_instructions(workspace_root, 'test_bot', 'shape', 'gather_context')
        create_base_action_instructions(workspace_root, 'gather_context')
        
        # When: Call REAL Bot API (doesn't exist yet!)
        from agile_bot.bots.base_bot.src.bot import Bot
        bot = Bot(
            bot_name='test_bot',
            workspace_root=workspace_root,
            config_path=test_bot_config
        )
        result = bot.invoke_tool(
            tool_name='test_bot_shape_gather_context',
            parameters={'behavior': 'shape', 'action': 'gather_context'}
        )
        
        # Then: Tool executed and returned result
        assert result.status == 'completed'
        assert result.behavior == 'shape'
        assert result.action == 'gather_context'

    def test_server_preloads_bot_once_at_startup(self, workspace_root, test_bot_config):
        """
        SCENARIO: Server preloads bot once and reuses across invocations
        GIVEN: Bot has behaviors configured
        WHEN: MCP Server starts up
        THEN: Server instantiates Bot class once and reuses for all invocations
        """
        # Given: Bot config with multiple behaviors
        create_behavior_action_instructions(workspace_root, 'test_bot', 'shape', 'gather_context')
        create_behavior_action_instructions(workspace_root, 'test_bot', 'discovery', 'gather_context')
        create_base_action_instructions(workspace_root, 'gather_context')
        
        # When: Call REAL MCPServer API (doesn't exist yet!)
        from agile_bot.bots.base_bot.src.mcp_server import MCPServer
        server = MCPServer(
            bot_name='test_bot',
            workspace_root=workspace_root,
            config_path=test_bot_config
        )
        server.start()
        
        # Then: Bot loaded once and cached
        assert server.bot is not None
        assert server.bot.name == 'test_bot'
        assert len(server.bot.behaviors) == 4
        
        # Multiple invocations use same bot instance
        bot_id_1 = id(server.bot)
        server.invoke_tool('test_bot_shape_gather_context', {})
        bot_id_2 = id(server.bot)
        assert bot_id_1 == bot_id_2

    def test_tool_routes_to_correct_behavior_action_method(self, workspace_root, test_bot_config):
        """
        SCENARIO: Tool routes to correct behavior action method
        GIVEN: Bot has multiple behaviors with build_knowledge action
        WHEN: AI Chat invokes 'test_bot_exploration_build_knowledge'
        THEN: Tool routes to test_bot.Exploration.BuildKnowledge() not other behaviors
        """
        # Given: Multiple behaviors exist
        create_behavior_action_instructions(workspace_root, 'test_bot', 'shape', 'build_knowledge')
        create_behavior_action_instructions(workspace_root, 'test_bot', 'discovery', 'build_knowledge')
        create_behavior_action_instructions(workspace_root, 'test_bot', 'exploration', 'build_knowledge')
        create_base_action_instructions(workspace_root, 'build_knowledge')
        
        # When: Call REAL Bot API for specific behavior
        from agile_bot.bots.base_bot.src.bot import Bot
        bot = Bot(
            bot_name='test_bot',
            workspace_root=workspace_root,
            config_path=test_bot_config
        )
        result = bot.invoke_tool(
            tool_name='test_bot_exploration_build_knowledge',
            parameters={'behavior': 'exploration', 'action': 'build_knowledge'}
        )
        
        # Then: Routes to exploration behavior only (not shape or discovery)
        assert result.behavior == 'exploration'
        assert result.action == 'build_knowledge'
        assert result.executed_instructions_from == 'exploration/build_knowledge'

    def test_tool_raises_error_when_behavior_missing(self, workspace_root, test_bot_config):
        """
        SCENARIO: Tool handles missing behavior gracefully
        GIVEN: Bot does not have 'invalid_behavior' configured
        WHEN: AI Chat invokes tool for invalid behavior
        THEN: Tool raises AttributeError with clear message
        """
        # Given: Bot with valid behaviors only
        create_base_action_instructions(workspace_root, 'gather_context')
        
        # When: Call REAL Bot API with invalid behavior (doesn't exist!)
        from agile_bot.bots.base_bot.src.bot import Bot
        bot = Bot(
            bot_name='test_bot',
            workspace_root=workspace_root,
            config_path=test_bot_config
        )
        
        # Then: Raises AttributeError with clear message
        with pytest.raises(AttributeError) as exc_info:
            bot.invoke_tool(
                tool_name='test_bot_invalid_behavior_gather_context',
                parameters={'behavior': 'invalid_behavior', 'action': 'gather_context'}
            )
        
        assert 'Behavior invalid_behavior not found' in str(exc_info.value)
        assert 'test_bot' in str(exc_info.value)

    def test_tool_raises_error_when_action_missing(self, workspace_root, test_bot_config):
        """
        SCENARIO: Tool handles missing action gracefully
        GIVEN: Action 'invalid_action' does not exist in base actions
        WHEN: AI Chat invokes tool for invalid action
        THEN: Tool raises FileNotFoundError with clear message
        """
        # Given: Valid behavior but invalid action
        create_behavior_action_instructions(workspace_root, 'test_bot', 'shape', 'gather_context')
        
        # When: Call REAL Bot API with invalid action (doesn't exist!)
        from agile_bot.bots.base_bot.src.bot import Bot
        bot = Bot(
            bot_name='test_bot',
            workspace_root=workspace_root,
            config_path=test_bot_config
        )
        
        # Then: Raises FileNotFoundError for missing base action
        with pytest.raises(FileNotFoundError) as exc_info:
            bot.invoke_tool(
                tool_name='test_bot_shape_invalid_action',
                parameters={'behavior': 'shape', 'action': 'invalid_action'}
            )
        
        assert 'Action invalid_action not found in base actions' in str(exc_info.value)


class TestBehaviorActionInstructions:
    """Behavior action instruction loading and merging tests."""

    def test_action_loads_and_merges_instructions(self, workspace_root):
        """
        SCENARIO: Action loads and merges instructions for shape gather_context
        GIVEN: Base and behavior-specific instructions exist
        WHEN: Action method is invoked
        THEN: Instructions are loaded from both locations and merged
        """
        # Given: Both instruction files exist
        bot_name = 'test_bot'
        behavior = 'shape'
        action = 'gather_context'
        
        config_file = create_bot_config_file(workspace_root, bot_name, ['shape'])
        behavior_instructions = create_behavior_action_instructions(workspace_root, bot_name, behavior, action)
        base_instructions = create_base_action_instructions(workspace_root, action)
        
        # When: Call REAL GatherContextAction API to load and merge instructions
        from agile_bot.bots.base_bot.src.actions.gather_context_action import GatherContextAction
        action_obj = GatherContextAction(
            bot_name=bot_name,
            behavior=behavior,
            workspace_root=workspace_root
        )
        merged_instructions = action_obj.load_and_merge_instructions()
        
        # Then: Instructions merged from both sources
        assert 'base_instructions' in merged_instructions
        assert 'behavior_instructions' in merged_instructions
        assert merged_instructions['action'] == action
        assert merged_instructions['behavior'] == behavior

    def test_action_uses_base_only_when_behavior_instructions_missing(self, workspace_root):
        """
        SCENARIO: Action uses base instructions when behavior-specific missing
        GIVEN: Base instructions exist but behavior-specific do not
        WHEN: Action method is invoked
        THEN: Returns base instructions only with info log
        """
        # Given: Only base instructions exist (no behavior-specific)
        bot_name = 'test_bot'
        behavior = 'shape'
        action = 'gather_context'
        
        config_file = create_bot_config_file(workspace_root, bot_name, ['shape'])
        base_instructions = create_base_action_instructions(workspace_root, action)
        
        # When: Call REAL GatherContextAction API (behavior instructions missing)
        from agile_bot.bots.base_bot.src.actions.gather_context_action import GatherContextAction
        action_obj = GatherContextAction(
            bot_name=bot_name,
            behavior=behavior,
            workspace_root=workspace_root
        )
        merged_instructions = action_obj.load_and_merge_instructions()
        
        # Then: Uses base instructions only
        assert 'base_instructions' in merged_instructions
        assert 'behavior_instructions' not in merged_instructions or merged_instructions['behavior_instructions'] is None
        assert merged_instructions['action'] == action

    def test_action_raises_error_when_base_instructions_missing(self, workspace_root):
        """
        SCENARIO: Action handles missing base instructions
        GIVEN: Base action instructions do not exist
        WHEN: Action method is invoked
        THEN: Raises FileNotFoundError with clear message
        """
        # Given: No base instructions (behavior instructions exist but base missing)
        bot_name = 'test_bot'
        behavior = 'shape'
        action = 'gather_context'
        
        config_file = create_bot_config_file(workspace_root, bot_name, ['shape'])
        create_behavior_action_instructions(workspace_root, bot_name, behavior, action)
        
        # When: Call REAL GatherContextAction API (base instructions missing)
        from agile_bot.bots.base_bot.src.actions.gather_context_action import GatherContextAction
        action_obj = GatherContextAction(
            bot_name=bot_name,
            behavior=behavior,
            workspace_root=workspace_root
        )
        
        # Then: Raises FileNotFoundError for missing base instructions
        with pytest.raises(FileNotFoundError) as exc_info:
            action_obj.load_and_merge_instructions()
        
        assert f'Base instructions not found for action {action}' in str(exc_info.value)

