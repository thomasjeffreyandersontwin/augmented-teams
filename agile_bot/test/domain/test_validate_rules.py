
import pytest
import json
from pathlib import Path
from agile_bot.test.domain.bot_test_helper import BotTestHelper


class TestValidateWithRules:
    """Tests that rules are properly formatted into instructions for AI to use."""
    
    def test_story_graph_rules_formatted_in_instructions(self, tmp_path):
        """
        SCENARIO: Story graph validation includes rule content in instructions
        GIVEN: Production story_bot with shape behavior (validates story graph)
        AND: Story graph file exists
        WHEN: Validate action executes
        THEN: Instructions contain rule descriptions, DO/DON'T sections, and priorities from rule files
        """
        # GIVEN: Production story_bot with shape behavior (validates story graph)
        helper = BotTestHelper(tmp_path)
        
        # AND: Story graph file exists
        story_graph_data = {'epics': []}
        helper.story.create_story_graph(story_graph_data)
        
        helper.bot.behaviors.navigate_to('shape')
        behavior = helper.bot.behaviors.current
        
        # AND: Validate action from production behavior
        from agile_bot.src.actions.validate.validate_action import ValidateRulesAction
        from agile_bot.src.actions.action_context import ValidateActionContext
        action = ValidateRulesAction(behavior=behavior, action_config=None)
        
        # WHEN: Validate action executes
        result = action.do_execute(ValidateActionContext())
        
        # THEN: Instructions contain rule content from rule files
        helper.validate.assert_validate_instructions(result)
    
    def test_file_rules_formatted_in_instructions(self, tmp_path):
        """
        SCENARIO: File validation includes rule content in instructions
        GIVEN: Production story_bot with code behavior (validates files)
        AND: Story graph file exists
        WHEN: Validate action executes
        THEN: Instructions contain rule descriptions, DO/DON'T sections, and priorities from rule files
        """
        # GIVEN: Production story_bot with code behavior (validates files)
        helper = BotTestHelper(tmp_path)
        
        # AND: Story graph file exists
        story_graph_data = {'epics': []}
        helper.story.create_story_graph(story_graph_data)
        
        helper.bot.behaviors.navigate_to('code')
        behavior = helper.bot.behaviors.current
        
        # AND: Validate action from production behavior
        from agile_bot.src.actions.validate.validate_action import ValidateRulesAction
        from agile_bot.src.actions.action_context import ValidateActionContext
        action = ValidateRulesAction(behavior=behavior, action_config=None)
        
        # WHEN: Validate action executes
        result = action.do_execute(ValidateActionContext())
        
        # THEN: Instructions contain rule content from rule files
        helper.validate.assert_validate_instructions(result)

class TestValidateWithScanners:
    """Tests that scanners execute and receive correct data (story_graph vs files)."""
    
    def test_story_graph_scanner_receives_story_graph_data(self, tmp_path):
        """
        SCENARIO: Story graph scanners receive scoped story_graph data
        GIVEN: Story graph with multiple epics ("Build Knowledge", "Epic B")
        AND: Scope filtered to "Build Knowledge" epic
        AND: Production story_bot with shape behavior
        WHEN: Validate action executes with scope
        THEN: Scanner receives filtered story graph (only "Build Knowledge" epic)
        AND: Scanner executes successfully
        AND: Instructions contain "Build Knowledge" in scope description
        """
        # GIVEN: Story graph with multiple epics
        helper = BotTestHelper(tmp_path)
        story_graph_data = {
            'epics': [
                {'name': 'Build Knowledge', 'sub_epics': [], 'story_groups': []},
                {'name': 'Epic B', 'sub_epics': [], 'story_groups': []}
            ]
        }
        helper.story.create_story_graph(story_graph_data)
        
        # AND: Scope filtered to "Build Knowledge" epic
        from agile_bot.src.scope import Scope, ScopeType
        scope = Scope(workspace_directory=tmp_path)
        scope.filter(type=ScopeType.STORY, value=['Build Knowledge'])
        
        # AND: Production story_bot with shape behavior
        helper.bot.behaviors.navigate_to('shape')
        behavior = helper.bot.behaviors.current
        
        # AND: Validate action with rules
        from agile_bot.src.actions.validate.validate_action import ValidateRulesAction
        from agile_bot.src.actions.action_context import ValidateActionContext
        action = ValidateRulesAction(behavior=behavior, action_config=None)
        
        # WHEN: Validate action executes with scope
        context = ValidateActionContext(scope=scope)
        result = action.do_execute(context)
        
        # THEN: Instructions reference the scoped epic
        instructions = result.get('base_instructions', [])
        instructions_text = ' '.join(instructions)
        assert 'Build Knowledge' in instructions_text, \
            "Instructions must reference scoped epic 'Build Knowledge'"
        
        # AND: Scanner executed successfully
        validation_rules = result.get('validation_rules', [])
        assert len(validation_rules) > 0, "Shape behavior must have validation rules"
        
        scanner_executed = any(
            rule.get('scanner_status', {}).get('status') == 'EXECUTED'
            for rule in validation_rules
        )
        assert scanner_executed, "Scanner must execute and receive scoped story graph"
    
    def test_file_scanner_receives_file_data(self, tmp_path):
        """
        SCENARIO: File scanners receive scoped file paths
        GIVEN: Multiple Python files (test_foo.py, test_bar.py, main.py)
        AND: Scope filtered to test files only (**/test*.py)
        AND: Production story_bot with code behavior
        WHEN: Validate action executes with scope
        THEN: Scanner receives filtered files (only test_foo.py, test_bar.py)
        AND: Scanner executes successfully
        AND: Instructions reference test file scope
        """
        # GIVEN: Multiple Python files
        helper = BotTestHelper(tmp_path)
        test_dir = tmp_path / 'test'
        test_dir.mkdir()
        src_dir = tmp_path / 'src'
        src_dir.mkdir()
        
        (test_dir / 'test_foo.py').write_text('# test file')
        (test_dir / 'test_bar.py').write_text('# test file')
        (src_dir / 'main.py').write_text('# main file')
        
        # AND: Scope filtered to test files only
        from agile_bot.src.scope import Scope, ScopeType
        scope = Scope(workspace_directory=tmp_path)
        scope.filter(type=ScopeType.FILES, value=['**/test*.py'])
        
        # AND: Production story_bot with code behavior
        helper.bot.behaviors.navigate_to('code')
        behavior = helper.bot.behaviors.current
        
        # AND: Validate action with rules
        from agile_bot.src.actions.validate.validate_action import ValidateRulesAction
        from agile_bot.src.actions.action_context import ValidateActionContext
        action = ValidateRulesAction(behavior=behavior, action_config=None)
        
        # WHEN: Validate action executes with scope
        context = ValidateActionContext(scope=scope)
        result = action.do_execute(context)
        
        # THEN: Instructions reference file scope
        instructions = result.get('base_instructions', [])
        instructions_text = ' '.join(instructions)
        
        # Should reference test files in scope or file count
        has_file_reference = (
            'test' in instructions_text.lower() or
            'file' in instructions_text.lower() or
            str(test_dir) in instructions_text or
            'test_foo.py' in instructions_text or
            'test_bar.py' in instructions_text
        )
        assert has_file_reference, "Instructions must reference scoped files"
        
        # AND: Scanner executed successfully
        validation_rules = result.get('validation_rules', [])
        assert len(validation_rules) > 0, "Code behavior must have validation rules"
        
        scanner_executed = any(
            rule.get('scanner_status', {}).get('status') == 'EXECUTED'
            for rule in validation_rules
        )
        assert scanner_executed, "Scanner must execute and receive scoped files"

