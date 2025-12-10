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


# ============================================================================
# STORY: Update Existing Knowledge Graph Instead of Creating New File
# ============================================================================

class TestUpdateExistingKnowledgeGraph:
    """Story: Update Existing Knowledge Graph - Tests that build_knowledge updates existing story-graph.json instead of creating a new file."""

    def test_prioritization_updates_existing_story_graph_json(self, bot_directory, workspace_directory):
        """
        Test that prioritization behavior updates existing story-graph.json by adding increments array,
        rather than creating a separate story-graph-increments.json file.
        """
        bot_name = 'story_bot'
        behavior = 'prioritization'
        
        # Bootstrap environment
        bootstrap_env(bot_directory, workspace_directory)
        
        # Create existing story-graph.json with epics (from shape behavior)
        stories_dir = workspace_directory / 'docs' / 'stories'
        stories_dir.mkdir(parents=True, exist_ok=True)
        
        existing_story_graph = {
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
        
        story_graph_path = stories_dir / 'story-graph.json'
        story_graph_path.write_text(json.dumps(existing_story_graph, indent=2), encoding='utf-8')
        
        # Create knowledge graph config for prioritization
        behavior_dir = bot_directory / 'behaviors' / behavior
        kg_dir = behavior_dir / 'content' / '1_knowledge_graph'
        kg_dir.mkdir(parents=True, exist_ok=True)
        
        config_file = kg_dir / 'build_story_graph_increments.json'
        config_data = {
            "name": "build_story_graph_outline",
            "path": "docs/stories",
            "template": "story_graph_increments.json",
            "output": "story-graph.json"
        }
        config_file.write_text(json.dumps(config_data), encoding='utf-8')
        
        # Create template file
        template_file = kg_dir / 'story_graph_increments.json'
        template_content = {
            "_explanation": {},
            "epics": [],
            "increments": []
        }
        template_file.write_text(json.dumps(template_content), encoding='utf-8')
        
        # Create action and get instructions
        action_obj = BuildKnowledgeAction(bot_name=bot_name, behavior=behavior, bot_directory=bot_directory)
        instructions = action_obj.inject_knowledge_graph_template()
        
        # Verify instructions include update guidance
        assert 'knowledge_graph_config' in instructions
        assert instructions['knowledge_graph_config']['output'] == 'story-graph.json'
        
        # Verify that instructions should indicate updating existing file
        # The instructions should guide the LLM to load existing story-graph.json and add increments
        assert 'template_path' in instructions
        
        # Verify existing file still exists and wasn't replaced
        assert story_graph_path.exists()
        
        # Verify that the config specifies the same output file (not a new file)
        config = instructions['knowledge_graph_config']
        assert config['output'] == 'story-graph.json'
        assert config['path'] == 'docs/stories'
        
        # The actual update logic should be in the instructions passed to LLM
        # This test verifies the action provides the correct guidance
