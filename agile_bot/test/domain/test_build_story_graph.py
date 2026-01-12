"""
Build Knowledge Tests

Tests for all stories in the 'Build Knowledge' sub-epic:
- Inject Knowledge Graph Template for Build Knowledge
- Update Existing Knowledge Graph
"""
import pytest
from pathlib import Path
import json
from agile_bot.src.actions.build.build_action import BuildKnowledgeAction
from agile_bot.test.domain.bot_test_helper import BotTestHelper




class TestBuildStoryGraph:

    def test_action_injects_knowledge_graph_template(self, tmp_path):
        """
        SCENARIO: Action Injects Knowledge Graph Template
        GIVEN: Production story_bot with shape behavior (has knowledge graph templates)
        WHEN: Action injects knowledge graph template
        THEN: Instructions contain template_path from existing templates
        """
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        action_obj = BuildKnowledgeAction(behavior=helper.bot.behaviors.current, action_config=None)
        
        instructions = action_obj.get_instructions()
        
        assert 'template_path' in instructions
        assert instructions['template_path'] is not None

    def test_action_loads_and_merges_instructions(self, tmp_path):
        """
        SCENARIO: Action Loads And Merges Instructions
        GIVEN: Production story_bot with shape behavior (has knowledge graph templates)
        WHEN: Action injects knowledge graph and instructions
        THEN: Instructions contain all BuildKnowledgeAction-specific fields
        """
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        action_obj = helper.bot.behaviors.current.actions.find_by_name('build')
        
        instructions = action_obj.do_execute()
        
        helper.build.assert_build_knowledge_instructions(instructions)

    def test_all_template_variables_are_replaced_in_instructions(self, tmp_path):
        """
        SCENARIO: All Template Variables Are Replaced In Instructions
        GIVEN: Production story_bot with shape behavior (has knowledge graph templates)
        WHEN: Action injects all template variables
        THEN: Instructions contain all required BuildKnowledgeAction fields
        """
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        action_obj = helper.bot.behaviors.current.actions.find_by_name('build')
        
        instructions = action_obj.do_execute()
        
        helper.build.assert_build_knowledge_instructions(instructions)

    def test_behavior_updates_existing_story_graph_json(self, tmp_path):
        """
        SCENARIO: Prioritization behavior updates existing story-graph.json
        GIVEN: Production prioritization behavior with increments templates
        AND: Existing story-graph.json in workspace
        WHEN: Action injects knowledge graph template for increments
        THEN: Instructions use production template (story_graph_increments.json) that updates existing file
        """
        helper = BotTestHelper(tmp_path)
        
        existing_story_graph = helper.story.given_story_graph_dict(epic='mob')
        stories_dir = helper.workspace / 'docs' / 'stories'
        story_graph_path = helper.files.given_file_created(stories_dir, 'story-graph.json', existing_story_graph)
        
        helper.bot.behaviors.navigate_to('prioritization')
        action_obj = BuildKnowledgeAction(behavior=helper.bot.behaviors.current, action_config=None)
        
        instructions = action_obj.do_execute()
        
        # Then: Instructions indicate updating existing file
        assert instructions.get('knowledge_graph_config'), "Instructions should contain 'knowledge_graph_config'"
        config = instructions.get('knowledge_graph_config', {})
        assert config.get('output') == 'story-graph.json', f"Expected output 'story-graph.json', got '{config.get('output')}'"
        assert instructions.get('template_path'), "Instructions should contain 'template_path'"
        assert story_graph_path.exists(), f"Story graph file should exist: {story_graph_path}"
        path_str = str(config.get('path')).replace('\\', '/')
        assert 'docs/stories' in path_str, f"Expected path to contain 'docs/stories', got '{config.get('path')}'"
