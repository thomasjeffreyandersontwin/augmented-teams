"""
Build Knowledge Tests

Tests for all stories in the 'Build Knowledge' sub-epic:
- Track Activity for Build Knowledge Action
- Proceed To Render Output
"""
import pytest
from pathlib import Path
import json
from agile_bot.bots.base_bot.src.bot.build_knowledge_action import BuildKnowledgeAction
from agile_bot.bots.base_bot.test.test_helpers import (
    bootstrap_env,
    verify_action_tracks_start,
    verify_action_tracks_completion,
    verify_workflow_transition,
    verify_workflow_saves_completed_action,
    create_knowledge_graph_template,
    get_bot_dir
)

# Use fixtures from conftest.py (bot_directory, workspace_directory)

# ============================================================================
# STORY: Track Activity for Build Knowledge Action
# ============================================================================

class TestTrackActivityForBuildKnowledgeAction:
    """Story: Track Activity for Build Knowledge Action - Tests activity tracking for build_knowledge."""

    def test_track_activity_when_build_knowledge_action_starts(self, bot_directory, workspace_directory):
        verify_action_tracks_start(bot_directory, workspace_directory, BuildKnowledgeAction, 'build_knowledge')

    def test_track_activity_when_build_knowledge_action_completes(self, bot_directory, workspace_directory):
        verify_action_tracks_completion(
            bot_directory,
            workspace_directory,
            BuildKnowledgeAction,
            'build_knowledge',
            outputs={'knowledge_items_count': 12, 'file_path': 'knowledge.json'},
            duration=420
        )


# ============================================================================
# STORY: Proceed To Render Output
# ============================================================================

class TestProceedToRenderOutput:
    """Story: Proceed To Render Output - Tests transition to render_output action."""

    def test_seamless_transition_from_build_knowledge_to_render_output(self, bot_directory, workspace_directory):
        verify_workflow_transition(bot_directory, workspace_directory, 'build_knowledge', 'render_output')

    def test_workflow_state_captures_build_knowledge_completion(self, bot_directory, workspace_directory):
        verify_workflow_saves_completed_action(bot_directory, workspace_directory, 'build_knowledge')


# ============================================================================
# STORY: Inject Knowledge Graph Template for Build Knowledge
# ============================================================================

class TestInjectKnowledgeGraphTemplateForBuildKnowledge:
    """Story: Inject Knowledge Graph Template for Build Knowledge - Tests template injection."""

    def test_action_injects_knowledge_graph_template(self, bot_directory, workspace_directory):
        bot_name = 'story_bot'  # Match fixture
        behavior = 'exploration'
        template_name = 'story-graph-explored-outline.json'
        
        # Bootstrap environment
        bootstrap_env(bot_directory, workspace_directory)
        
        # Create knowledge graph directory structure
        behavior_dir = bot_directory / 'behaviors' / behavior
        kg_dir = behavior_dir / 'content' / 'knowledge_graph'
        kg_dir.mkdir(parents=True, exist_ok=True)
        
        # Create config file that references the template
        config_file = kg_dir / 'build_story_graph_outline.json'
        config_file.write_text(json.dumps({'template': template_name}), encoding='utf-8')
        
        # Create the actual template file
        template_file = kg_dir / template_name
        template_file.write_text(json.dumps({'template': 'knowledge_graph', 'structure': {}}), encoding='utf-8')
        
        action_obj = BuildKnowledgeAction(bot_name=bot_name, behavior=behavior, bot_directory=bot_directory)
        instructions = action_obj.inject_knowledge_graph_template()
        
        assert 'knowledge_graph_template' in instructions
        assert 'template_path' in instructions
        assert template_name in instructions['template_path']
        assert Path(instructions['template_path']).exists()

    def test_action_raises_error_when_template_missing(self, bot_directory, workspace_directory):
        bot_name = 'story_bot'  # Match fixture
        behavior = 'exploration'
        
        # Bootstrap environment
        bootstrap_env(bot_directory, workspace_directory)
        
        behavior_dir = bot_directory / 'behaviors' / behavior
        behavior_dir.mkdir(parents=True, exist_ok=True)
        
        action_obj = BuildKnowledgeAction(bot_name=bot_name, behavior=behavior, bot_directory=bot_directory)
        
        with pytest.raises(FileNotFoundError) as exc_info:
            action_obj.inject_knowledge_graph_template()
        
        error_msg = str(exc_info.value).lower()
        assert 'knowledge graph' in error_msg
