"""
Build Knowledge Tests

Tests for all stories in the 'Build Knowledge' sub-epic:
- Load Story Graph Into Memory
- Inject Knowledge Graph Template for Build Knowledge
- Update Existing Knowledge Graph
- Create Build Scope
- Filter Knowledge Graph
"""
import pytest
from pathlib import Path
import json
from agile_bot.src.actions.build.build_action import BuildKnowledgeAction
from agile_bot.src.scanners.story_map import (
    StoryMap, Epic, SubEpic, StoryGroup, Story, Scenario, ScenarioOutline
)
from agile_bot.test.domain.bot_test_helper import BotTestHelper







class TestInjectKnowledgeGraphTemplateForBuildKnowledge:
    """Story: Inject Knowledge Graph Template for Build Knowledge - Tests template injection."""

    def test_action_injects_knowledge_graph_template(self, tmp_path):
        """
        SCENARIO: Action Injects Knowledge Graph Template
        """
        helper = BotTestHelper(tmp_path)
        behavior = 'exploration'
        template_name = 'story-graph-explored-outline.json'
        
        # Setup knowledge graph directory and files
        kg_dir = helper.bot_directory / 'behaviors' / behavior / 'content' / 'knowledge_graph'
        kg_dir.mkdir(parents=True, exist_ok=True)
        helper.given_file_created(kg_dir, 'build_story_graph_outline.json', {'template': template_name})
        helper.given_file_created(kg_dir, template_name, {'template': 'knowledge_graph', 'structure': {}})
        
        # Get behavior and action from BotTestHelper
        helper.bot.behaviors.navigate_to(behavior)
        behavior_obj = helper.bot.behaviors.current
        action_obj = BuildKnowledgeAction(behavior=behavior_obj, action_config=None)
        instructions = action_obj.instructions
        
        helper.then_instructions_contain(instructions, 'template_path', template_name=template_name)

    def test_action_loads_and_merges_instructions(self, tmp_path):
        """
        SCENARIO: Action Loads And Merges Instructions
        GIVEN: Base and behavior-specific instructions exist
        WHEN: Action method is invoked
        THEN: Instructions are loaded from both locations and merged
        """
        helper = BotTestHelper(tmp_path)
        behavior = 'shape'
        action = 'build'
        
        # Setup knowledge graph directory and files
        helper.setup_knowledge_graph_config_and_template(behavior)
        helper.create_behavior_specific_instructions(behavior, action)
        
        # Get behavior and action from BotTestHelper
        helper.bot.behaviors.navigate_to(behavior)
        behavior_obj = helper.bot.behaviors.current
        action_obj = BuildKnowledgeAction(behavior=behavior_obj, action_config=None)
        
        # Call get_instructions() to trigger _prepare_instructions() which injects BuildKnowledgeAction fields
        from agile_bot.src.actions.action_context import ScopeActionContext
        merged_instructions = action_obj.get_instructions(ScopeActionContext())
        
        helper.then_instructions_merged_from_sources(merged_instructions, behavior, action, sources='both')
        helper.assert_build_knowledge_instructions(merged_instructions)

    def test_all_template_variables_are_replaced_in_instructions(self, tmp_path):
        """
        SCENARIO: All Template Variables Are Replaced In Instructions
        GIVEN: Base instructions with {{rules}}, {{schema}}, {{description}}, {{instructions}} placeholders
        WHEN: Action loads and merges instructions with all injections
        THEN: All template variables are replaced with actual content
        """
        helper = BotTestHelper(tmp_path)
        behavior = 'shape'
        action = 'build'
        bot_name = 'story_bot'
        
        # Setup for template variables test
        # BotTestHelper already bootstraps environment and uses production bot with base actions
        kg_dir = helper.setup_knowledge_graph_directory(behavior)
        helper.create_behavior_specific_instructions(behavior, action)
        # Create behavior instructions.json
        behavior_dir = helper.bot_directory / 'behaviors' / behavior
        instructions_file = behavior_dir / 'instructions.json'
        instructions_file.write_text(
            json.dumps({
                'description': 'Shape the story map',
                'goal': 'Create initial story structure'
            }),
            encoding='utf-8'
        )
        # Create config and template files
        helper.setup_knowledge_graph_config_and_template(behavior)
        helper.given_file_created(kg_dir, 'story-graph-outline.json', {
            '_explanation': {
                'epics': 'Top-level epics',
                'sub_epics': 'Sub-epic breakdowns'
            },
            'epics': []
        })
        from agile_bot.test.domain.test_validate_knowledge_and_content_against_rules import given_rule_file_created
        given_rule_file_created(helper.bot_directory, None, 'verb-noun-format', None, rule_type='verb_noun_format')
        
        # Get behavior from BotTestHelper
        helper.bot.behaviors.navigate_to(behavior)
        behavior_obj = helper.bot.behaviors.current
        action_obj = BuildKnowledgeAction(behavior=behavior_obj, action_config=None)
        instructions = action_obj.instructions
        
        base_instructions_text = '\n'.join(instructions.get('base_instructions', []))
        from agile_bot.test.domain.test_helpers import then_template_variables_replaced
        then_template_variables_replaced(base_instructions_text)

class TestUpdateExistingKnowledgeGraph:
    """Story: Update Existing Knowledge Graph - Tests that build updates existing story-graph.json instead of creating a new file."""

    def test_behavior_updates_existing_story_graph_json(self, tmp_path):
        """
        Test that prioritization behavior updates existing story-graph.json by adding increments array,
        rather than creating a separate story-graph-increments.json file.
        """
        helper = BotTestHelper(tmp_path)
        behavior = 'prioritization'
        
        existing_story_graph = helper.given_story_graph_dict(epic='mob')
        stories_dir = helper.workspace / 'docs' / 'stories'
        story_graph_path = helper.given_file_created(stories_dir, 'story-graph.json', existing_story_graph)
        
        # Setup knowledge graph directory
        kg_dir = helper.bot_directory / 'behaviors' / behavior / 'content' / 'knowledge_graph'
        kg_dir.mkdir(parents=True, exist_ok=True)
        helper.given_file_created(kg_dir, 'build_story_graph_increments.json', {
            "name": "build_story_graph_outline",
            "path": "docs/stories",
            "template": "story_graph_increments.json",
            "output": "story-graph.json"
        })
        helper.given_file_created(kg_dir, 'story_graph_increments.json', {
            "_explanation": {},
            "epics": [],
            "increments": []
        })
        
        # Get behavior and action from BotTestHelper
        helper.bot.behaviors.navigate_to(behavior)
        behavior_obj = helper.bot.behaviors.current
        action_obj = BuildKnowledgeAction(behavior=behavior_obj, action_config=None)
        instructions = action_obj.instructions
        
        helper.assert_instructions_indicate_updating_existing_file(instructions, 'story-graph.json')
        helper.assert_story_graph_updated_with_increments(instructions, story_graph_path)
        helper.assert_config_path_matches(instructions, 'docs/stories')

class TestLoadStoryGraphIntoMemory:
    """Story: Load Story Graph Into Memory - Tests loading story graph and creating StoryMap object model."""
    
    @staticmethod
    def _create_mock_bot(bot_directory: Path):
        """Helper: Create MockBot instance for testing StoryMap.from_bot().
        
        Used by: test_from_bot_loads_story_graph, test_from_bot_raises_when_file_not_found
        """
        class MockBot:
            def __init__(self, bot_directory):
                self.bot_directory = bot_directory
        
        return MockBot(bot_directory)
    
    def test_story_map_loads_epics(self, tmp_path):
        """
        SCENARIO: Story Map Loads Epics
        """
        # Given: Story map is loaded
        helper = BotTestHelper(tmp_path)
        story_map = helper.create_story_map()
        # When: Epics are retrieved from story map
        epics = helper.when_item_accessed('epics', story_map)
        # Then: Epics contain single build knowledge epic
        helper.assert_story_map_matches(epics)
    
    def test_epic_has_sub_epics(self, tmp_path):
        """
        SCENARIO: Epic Has Sub Epics
        """
        # Given: Story map is loaded
        helper = BotTestHelper(tmp_path)
        story_map = helper.create_story_map()
        epics = helper.when_item_accessed('epics', story_map)
        epic = helper.assert_story_map_matches(epics)
        # When: Epic children are retrieved
        children = epic.children
        # Then: Children contain single sub epic
        assert len(children) == 1
        assert isinstance(children[0], SubEpic)
        assert children[0].name == "Load Story Graph"
    
    def test_sub_epic_has_story_groups(self, tmp_path):
        """
        SCENARIO: Sub Epic Has Story Groups
        """
        # Given: Story map is loaded
        helper = BotTestHelper(tmp_path)
        story_map = helper.create_story_map()
        epics = helper.when_item_accessed('epics', story_map)
        epic = helper.assert_story_map_matches(epics)
        sub_epic = epic.children[0]
        # When: Sub epic children are retrieved
        children = sub_epic.children
        # Then: Children contain single story group
        assert len(children) == 1
        assert isinstance(children[0], StoryGroup)
    
    def test_story_group_has_stories(self, tmp_path):
        """
        SCENARIO: Story Group Has Stories
        """
        # Given: Story map is loaded
        helper = BotTestHelper(tmp_path)
        story_map = helper.create_story_map()
        epics = helper.when_item_accessed('epics', story_map)
        epic = helper.assert_story_map_matches(epics)
        sub_epic = epic.children[0]
        story_group = sub_epic.children[0]
        # When: Story group stories are retrieved
        stories = story_group.children
        # Then: Stories contain single story
        assert len(stories) == 1
        assert isinstance(stories[0], Story)
        assert stories[0].name == "Load Story Graph Into Memory"
    
    def test_story_has_properties(self, tmp_path):
        """
        SCENARIO: Story Has Properties
        """
        # Given: Story map is loaded
        helper = BotTestHelper(tmp_path)
        story_map = helper.create_story_map()
        # When: Story is retrieved from path
        story = helper.when_item_accessed('story', story_map)
        # Then: Story has expected properties
        assert story.name == "Load Story Graph Into Memory"
        assert story.users == ["Story Bot"]
        assert story.story_type == "user"
        assert story.sizing == "5 days"
        assert story.sequential_order == 1
        assert story.connector is None
    
    def test_story_has_scenarios(self, tmp_path):
        """
        SCENARIO: Story Has Scenarios
        """
        # Given: Story map is loaded
        helper = BotTestHelper(tmp_path)
        story_map = helper.create_story_map()
        story = helper.when_item_accessed('story', story_map)
        # When: Story scenarios are retrieved
        scenarios = story.scenarios
        # Then: Scenarios contain expected scenarios
        assert len(scenarios) == 2
        assert isinstance(scenarios[0], Scenario)
        assert scenarios[0].name == "Story graph file exists"
        assert scenarios[0].type == "happy_path"
        assert scenarios[1].name == "Story graph file missing"
        assert scenarios[1].type == "error_case"
    
    def test_scenario_has_properties(self, tmp_path):
        """
        SCENARIO: Scenario Has Properties
        """
        # Given: Story map is loaded
        helper = BotTestHelper(tmp_path)
        story_map = helper.create_story_map()
        story = helper.when_item_accessed('story', story_map)
        # When: Scenario is retrieved from story
        scenario = helper.when_item_accessed('scenario', story)
        # Then: Scenario has expected properties
        assert scenario.name == "Story graph file exists"
        assert scenario.type == "happy_path"
        assert len(scenario.background) == 1
        assert scenario.background[0] == "Given story graph file exists"
        assert len(scenario.steps) == 2
        assert scenario.steps[0] == "When story graph is loaded"
        assert scenario.steps[1] == "Then story map is created with epics"
    
    def test_scenario_default_test_method(self, tmp_path):
        """
        SCENARIO: Scenario Default Test Method
        """
        # Given: Story map is loaded
        helper = BotTestHelper(tmp_path)
        story_map = helper.create_story_map()
        story = helper.when_item_accessed('story', story_map)
        # When: Scenario is retrieved from story
        scenario = helper.when_item_accessed('scenario', story)
        # Then: Scenario has default test method
        assert scenario.default_test_method == "test_story_graph_file_exists"
    
    def test_story_has_scenario_outlines(self, tmp_path):
        """
        SCENARIO: Story Has Scenario Outlines
        """
        # Given: Story map is loaded
        helper = BotTestHelper(tmp_path)
        story_map = helper.create_story_map()
        story = helper.when_item_accessed('story', story_map)
        # When: Story scenario outlines are retrieved
        scenario_outlines = story.scenario_outlines
        # Then: Scenario outlines contain expected outline
        assert len(scenario_outlines) == 1
        assert isinstance(scenario_outlines[0], ScenarioOutline)
        assert scenario_outlines[0].name == "Load story graph with different formats"
    
    def test_scenario_outline_has_examples(self, tmp_path):
        """
        SCENARIO: Scenario Outline Has Examples
        """
        # Given: Story map is loaded
        helper = BotTestHelper(tmp_path)
        story_map = helper.create_story_map()
        story = helper.when_item_accessed('story', story_map)
        # When: Scenario outline is retrieved from story
        scenario_outline = helper.when_item_accessed('scenario_outline', story)
        # Then: Scenario outline has expected examples
        assert len(scenario_outline.examples_columns) == 2
        assert scenario_outline.examples_columns == ["file_path", "expected_epics"]
        assert len(scenario_outline.examples_rows) == 2
        assert scenario_outline.examples_rows[0] == ["story-graph.json", "2"]
        assert scenario_outline.examples_rows[1] == ["story-graph-v2.json", "3"]
    
    def test_story_default_test_class(self, tmp_path):
        """
        SCENARIO: Story Default Test Class
        """
        # Given: Story map is loaded
        helper = BotTestHelper(tmp_path)
        story_map = helper.create_story_map()
        # When: Story is retrieved from path
        story = helper.when_item_accessed('story', story_map)
        # Then: Story has default test class
        assert story.default_test_class == "TestLoadStoryGraphIntoMemory"
    
    def test_story_map_walk_traverses_all_nodes(self, tmp_path):
        """
        SCENARIO: Story Map Walk Traverses All Nodes
        """
        # Given: Story map is loaded
        helper = BotTestHelper(tmp_path)
        story_map = helper.create_story_map()
        epics = helper.when_item_accessed('epics', story_map)
        epic = helper.when_item_accessed('epic', epics)
        # When: Story map is walked
        nodes = list(story_map.walk(epic))
        # Then: Nodes match expected structure
        assert len(nodes) == 4
        assert isinstance(nodes[0], Epic)
        assert nodes[0].name == "Build Knowledge"
        assert isinstance(nodes[1], SubEpic)
        assert nodes[1].name == "Load Story Graph"
        assert isinstance(nodes[2], StoryGroup)
        assert isinstance(nodes[3], Story)
        assert nodes[3].name == "Load Story Graph Into Memory"
    
    def test_map_location_for_epic(self, tmp_path):
        """
        SCENARIO: Map Location For Epic
        """
        # Given: Story map is loaded
        helper = BotTestHelper(tmp_path)
        story_map = helper.create_story_map()
        epics = helper.when_item_accessed('epics', story_map)
        # When: First epic is retrieved
        epic = helper.when_item_accessed('epic', epics)
        # Then: Epic map location is correct
        helper.assert_map_location_matches(epic)
    
    def test_map_location_for_sub_epic(self, tmp_path):
        """
        SCENARIO: Map Location For Sub Epic
        """
        # Given: Story map is loaded
        helper = BotTestHelper(tmp_path)
        story_map = helper.create_story_map()
        epics = helper.when_item_accessed('epics', story_map)
        # When: Sub epic is retrieved from epics
        sub_epic = helper.when_item_accessed('sub_epic', epics)
        # Then: Sub epic map location is correct
        helper.assert_map_location_matches(sub_epic)
    
    def test_map_location_for_story(self, tmp_path):
        """
        SCENARIO: Map Location For Story
        """
        # Given: Story map is loaded
        helper = BotTestHelper(tmp_path)
        story_map = helper.create_story_map()
        epics = helper.when_item_accessed('epics', story_map)
        # When: Story is retrieved from epics
        story = helper.when_item_accessed('story', epics)
        # Then: Story map location is correct
        helper.assert_map_location_matches(story)
    
    def test_scenario_map_location(self, tmp_path):
        """
        SCENARIO: Scenario Map Location
        """
        # Given: Story map is loaded
        helper = BotTestHelper(tmp_path)
        story_map = helper.create_story_map()
        epics = helper.when_item_accessed('epics', story_map)
        # When: Scenario is retrieved from epics
        scenario = helper.when_item_accessed('scenario', epics)
        # Then: Scenario map location is correct
        helper.assert_map_location_matches(scenario)
    
    def test_scenario_outline_map_location(self, tmp_path):
        """
        SCENARIO: Scenario Outline Map Location
        """
        # Given: Story map is loaded
        helper = BotTestHelper(tmp_path)
        story_map = helper.create_story_map()
        epics = helper.when_item_accessed('epics', story_map)
        # When: Scenario outline is retrieved from epics
        scenario_outline = helper.when_item_accessed('scenario_outline', epics)
        # Then: Scenario outline map location is correct
        helper.assert_map_location_matches(scenario_outline)
    
    def test_from_bot_loads_story_graph(self, tmp_path):
        """
        SCENARIO: From Bot Loads Story Graph
        """
        helper = BotTestHelper(tmp_path)
        docs_dir = helper.bot_directory / 'docs'
        docs_dir.mkdir(parents=True, exist_ok=True)
        story_graph = helper.given_story_graph_dict()
        story_graph_path = helper.given_file_created(docs_dir, 'story-graph.json', story_graph)
        story_map = StoryMap.from_bot(helper.bot_directory)
        helper.assert_story_map_matches(story_map)
    
    def test_from_bot_with_path(self, tmp_path):
        """
        SCENARIO: From Bot With Path
        """
        # Given: Bot directory, docs directory, and story graph file are created
        helper = BotTestHelper(tmp_path)
        docs_dir = helper.bot_directory / 'docs'
        docs_dir.mkdir(parents=True, exist_ok=True)
        story_graph = helper.given_story_graph_dict()
        story_graph_path = helper.given_file_created(docs_dir, 'story-graph.json', story_graph)
        # When: Story map is created from bot
        story_map = StoryMap.from_bot(helper.bot_directory)
        # Then: Story map contains test epic
        helper.assert_story_map_matches(story_map)
    
    def test_scenario_map_location_duplicate(self, tmp_path):
        """
        SCENARIO: Scenario Map Location
        """
        # Given: Story map is loaded
        helper = BotTestHelper(tmp_path)
        story_map = helper.create_story_map()
        epics = helper.when_item_accessed('epics', story_map)
        # When: Scenario is retrieved from epics
        scenario = helper.when_item_accessed('scenario', epics)
        # Then: Scenario map location is correct
        helper.assert_map_location_matches(scenario)
    
    def test_scenario_outline_map_location_duplicate(self, tmp_path):
        """
        SCENARIO: Scenario Outline Map Location
        """
        # Given: Story map is loaded
        helper = BotTestHelper(tmp_path)
        story_map = helper.create_story_map()
        epics = helper.when_item_accessed('epics', story_map)
        # When: Scenario outline is retrieved from epics
        scenario_outline = helper.when_item_accessed('scenario_outline', epics)
        # Then: Scenario outline map location is correct
        helper.assert_map_location_matches(scenario_outline)

class TestCreateBuildScope:
    """Story: Create Build Scope (Sub-epic: Build Knowledge)"""
    
    @pytest.mark.parametrize("parameters,expected_scope_contains", [
        # Example 1: Scope 'all'
        ({'scope': {'type': 'all'}}, {'all': True}),
        # Example 2: Story names
        ({'scope': {'type': 'story', 'value': ['Story1']}}, {'story_names': ['Story1']}),
        # Example 3: Multiple story names
        ({'scope': {'type': 'story', 'value': ['Story1', 'Story2']}}, {'story_names': ['Story1', 'Story2']}),
        # Example 4: Increment priorities
        ({'scope': {'type': 'increment', 'value': [1]}}, {'increment_priorities': [1]}),
        # Example 5: Multiple increment priorities
        ({'scope': {'type': 'increment', 'value': [1, 2]}}, {'increment_priorities': [1, 2]}),
        # Example 6: Epic names
        ({'scope': {'type': 'epic', 'value': ['Epic A']}}, {'epic_names': ['Epic A']}),
        # Example 7: Multiple epic names
        ({'scope': {'type': 'epic', 'value': ['Epic A', 'Epic B']}}, {'epic_names': ['Epic A', 'Epic B']}),
        # Example 8: Increment names
        ({'scope': {'type': 'increment', 'value': ['Increment 1']}}, {'increment_names': ['Increment 1']}),
        # Example 9: No parameters (defaults to 'all')
        ({}, {'all': True}),
    ])
    def test_build_scope_created_with_different_parameter_combinations(self, tmp_path, parameters, expected_scope_contains):
        """
        SCENARIO: Build scope created with different parameter combinations
        GIVEN: Parameters dict with scope configuration
        WHEN: BuildScope instantiated with parameters
        THEN: BuildScope scope property returns expected configuration
        """
        # Given: Parameters dict
        helper = BotTestHelper(tmp_path)
        # When: BuildScope instantiated
        build_scope = helper.create_build_scope(parameters)
        
        # Then: BuildScope scope property returns expected configuration
        helper.assert_build_scope_matches(build_scope, expected_scope_contains)
    
    def test_build_scope_defaults_to_all_when_no_parameters(self, tmp_path):
        """
        SCENARIO: Build scope defaults to 'all' when no parameters provided
        GIVEN: Empty parameters dict
        WHEN: BuildScope instantiated
        THEN: Scope defaults to 'all'
        """
        # Given: Empty parameters
        helper = BotTestHelper(tmp_path)
        parameters = {}
        
        # When: BuildScope instantiated
        build_scope = helper.create_build_scope(parameters)
        
        # Then: Scope defaults to 'all'
        helper.assert_build_scope_contains(build_scope, 'all', True)
    
    def test_action_uses_build_scope_to_define_build_scope(self, tmp_path):
        """
        SCENARIO: Action uses BuildScope to define build scope
        GIVEN: BuildKnowledgeAction with parameters
        WHEN: Action executes with scope parameters
        THEN: Uses BuildScope class and includes scope in instructions
        """
        # Given: BotTestHelper provides production story_bot and workspace
        helper = BotTestHelper(tmp_path)
        behavior_name = 'exploration'
        
        # Create knowledge graph directory and config
        kg_dir = helper.bot_directory / 'behaviors' / behavior_name / 'content' / 'knowledge_graph'
        kg_dir.mkdir(parents=True, exist_ok=True)
        helper.setup_knowledge_graph_config_and_template(behavior_name)
        
        # Get behavior from BotTestHelper
        helper.bot.behaviors.navigate_to(behavior_name)
        behavior = helper.bot.behaviors.current
        action = BuildKnowledgeAction(behavior=behavior, action_config=None)
        parameters = helper.build_parameters_with_scope('all')
        
        # When: Action executes with scope parameters
        # Then: Uses BuildScope class
        helper.assert_action_uses_build_scope(action, parameters)





class TestFilterKnowledgeGraph:
    """Story: Filter Knowledge Graph (Sub-epic: Build Knowledge)"""
    
    def test_filter_returns_all_when_scope_is_all(self, tmp_path):
        """
        SCENARIO: Filter returns all when scope is all
        GIVEN: Story graph with multiple epics and increments
        WHEN: ScopingParameter filters with scope type 'all'
        THEN: Story graph contains all epics and increments
        """
        # Given: Story graph with epics and increments
        helper = BotTestHelper(tmp_path)
        story_graph = helper.story_graph_with_epics_and_increments()
        
        # When: Filter with scope 'all'
        filtered_graph = helper.filter_story_graph('build', 'all', None, story_graph=story_graph)
        
        # Then: All epics and increments present
        helper.assert_story_graph_contains_all_epics(filtered_graph, 2)
        helper.assert_story_graph_contains_all_increments(filtered_graph, 2)
    
    def test_filter_by_story_names_returns_matching_stories(self, tmp_path):
        """
        SCENARIO: Filter by story names returns matching stories
        GIVEN: Story graph with multiple stories
        WHEN: ScopingParameter filters with story names
        THEN: Story graph contains only matching stories and their parent epics
        """
        # Given: Story graph with stories
        helper = BotTestHelper(tmp_path)
        story_graph = helper.story_graph_with_epics_and_increments()
        
        # When: Filter by story names
        filtered_graph = helper.filter_story_graph('build', 'story', ['Story A1'], story_graph=story_graph)
        
        # Then: Only matching story and its parent epic present
        helper.assert_story_graph_contains_epic(filtered_graph, 'Epic A')
        helper.assert_story_graph_contains_story(filtered_graph, 'Story A1')
        assert 'Epic B' not in [epic.get('name') for epic in filtered_graph.get('epics', [])]
    
    def test_filter_by_epic_names_returns_matching_epics(self, tmp_path):
        """
        SCENARIO: Filter by epic names returns matching epics
        GIVEN: Story graph with multiple epics
        WHEN: ScopingParameter filters with epic names
        THEN: Story graph contains only matching epics and their increments
        """
        # Given: Story graph with epics
        helper = BotTestHelper(tmp_path)
        story_graph = helper.story_graph_with_epics_and_increments()
        
        # When: Filter by epic names
        filtered_graph = helper.filter_story_graph('build', 'epic', ['Epic A'], story_graph=story_graph)
        
        # Then: Only matching epic present
        helper.assert_story_graph_contains_epic(filtered_graph, 'Epic A')
        assert 'Epic B' not in [epic.get('name') for epic in filtered_graph.get('epics', [])]
        helper.assert_story_graph_contains_increment(filtered_graph, 'Increment 1')
    
    def test_filter_by_increment_priorities_returns_matching_increments(self, tmp_path):
        """
        SCENARIO: Filter by increment priorities returns matching increments
        GIVEN: Story graph with increments having different priorities
        WHEN: ScopingParameter filters with increment priorities
        THEN: Story graph contains only matching increments and their stories
        """
        # Given: Story graph with increments
        helper = BotTestHelper(tmp_path)
        story_graph = helper.story_graph_with_epics_and_increments()
        
        # When: Filter by increment priorities
        filtered_graph = helper.filter_story_graph('build', 'increment', [1], story_graph=story_graph)
        
        # Then: Only matching increment present
        helper.assert_story_graph_contains_increment(filtered_graph, 'Increment 1')
        assert 'Increment 2' not in [inc.get('name') for inc in filtered_graph.get('increments', [])]
        helper.assert_story_graph_contains_epic(filtered_graph, 'Epic A')
    
    def test_filter_by_increment_names_returns_matching_increments(self, tmp_path):
        """
        SCENARIO: Filter by increment names returns matching increments
        GIVEN: Story graph with increments having different names
        WHEN: ScopingParameter filters with increment names
        THEN: Story graph contains only matching increments and their stories
        """
        # Given: Story graph with increments
        helper = BotTestHelper(tmp_path)
        story_graph = helper.story_graph_with_epics_and_increments()
        
        # When: Filter by increment names
        filtered_graph = helper.filter_story_graph('build', 'increment', ['Increment 1'], story_graph=story_graph)
        
        # Then: Only matching increment present
        helper.assert_story_graph_contains_increment(filtered_graph, 'Increment 1')
        assert 'Increment 2' not in [inc.get('name') for inc in filtered_graph.get('increments', [])]
        helper.assert_story_graph_contains_epic(filtered_graph, 'Epic A')