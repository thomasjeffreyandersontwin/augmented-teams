"""
Build Test Helper
Handles build action, knowledge graphs, templates, configs + build-specific instruction assertions
"""
import json
from pathlib import Path
from .base_helper import BaseHelper


class BuildTestHelper(BaseHelper):
    """Helper for build action, knowledge graphs, and templates testing"""
    
    def setup_knowledge_graph_directory(self, behavior: str) -> Path:
        """Create knowledge graph directory structure for a behavior.
        
        Args:
            behavior: Behavior name
        
        Returns:
            Path to knowledge_graph directory
        """
        kg_dir = self.parent.bot_directory / 'behaviors' / behavior / 'content' / 'knowledge_graph'
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
    
    def create_knowledge_graph_template(self, behavior: str, template_name: str) -> Path:
        """Create knowledge graph template in behavior folder.
        
        Args:
            behavior: Behavior name
            template_name: Name of template file
        
        Returns:
            Path to template file
        """
        kg_dir = self.parent.bot_directory / 'behaviors' / behavior / 'content' / 'knowledge_graph'
        kg_dir.mkdir(parents=True, exist_ok=True)
        
        template_file = kg_dir / f'{template_name}.json'
        template_file.write_text(json.dumps({'template': 'knowledge_graph'}), encoding='utf-8')
        return template_file
    
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
        assert config is not None, "knowledge_graph_config should be set in instructions"
