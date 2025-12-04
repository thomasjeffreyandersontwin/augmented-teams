"""
Perform Behavior Action Tests

Tests for all stories in the 'Perform Behavior Action' sub-epic:
- Inject Behavior Action Instructions
- Inject Guardrails as Part of Clarify Requirements
- Inject Planning Criteria Into Instructions
- Inject Knowledge Graph Template for Build Knowledge
- Inject Validation Rules for Validate Rules Action
- Inject Load Rendered Content Instructions
- Inject Load Structured Content Instructions
- Inject Load Template Instruction
- Inject Load Transformer Methods Instruction
- Inject Render Output Instructions
- Load Correct Bot Instructions
"""
import pytest
from pathlib import Path
import json

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def create_guardrails_files(workspace: Path, bot_name: str, behavior: str, questions: list, evidence: list) -> tuple:
    """Helper: Create guardrails files for behavior."""
    guardrails_dir = workspace / 'agile_bot' / 'bots' / bot_name / 'behaviors' / behavior / 'guardrails' / 'required_context'
    guardrails_dir.mkdir(parents=True, exist_ok=True)
    
    questions_file = guardrails_dir / 'key_questions.json'
    questions_file.write_text(json.dumps({'questions': questions}), encoding='utf-8')
    
    evidence_file = guardrails_dir / 'evidence.json'
    evidence_file.write_text(json.dumps({'evidence': evidence}), encoding='utf-8')
    
    return questions_file, evidence_file

def create_planning_guardrails(workspace: Path, bot_name: str, behavior: str, assumptions: list, criteria: dict) -> tuple:
    """Helper: Create planning guardrails files."""
    planning_dir = workspace / 'agile_bot' / 'bots' / bot_name / 'behaviors' / behavior / 'guardrails' / 'planning'
    planning_dir.mkdir(parents=True, exist_ok=True)
    
    assumptions_file = planning_dir / 'typical_assumptions.json'
    assumptions_file.write_text(json.dumps({'assumptions': assumptions}), encoding='utf-8')
    
    criteria_dir = planning_dir / 'decision_criteria'
    criteria_dir.mkdir(exist_ok=True)
    
    criteria_file = criteria_dir / 'test_criteria.json'
    criteria_file.write_text(json.dumps(criteria), encoding='utf-8')
    
    return assumptions_file, criteria_file

def create_knowledge_graph_template(workspace: Path, bot_name: str, behavior: str, template_name: str) -> Path:
    """Helper: Create knowledge graph template file."""
    kg_dir = workspace / 'agile_bot' / 'bots' / bot_name / 'behaviors' / behavior / 'content' / 'knowledge_graph'
    kg_dir.mkdir(parents=True, exist_ok=True)
    
    template_file = kg_dir / template_name
    template_file.write_text(json.dumps({'template': 'structure'}), encoding='utf-8')
    
    return template_file

def create_validation_rules(workspace: Path, bot_name: str, behavior: str, rules: list) -> Path:
    """Helper: Create validation rules file."""
    rules_dir = workspace / 'agile_bot' / 'bots' / bot_name / 'behaviors' / behavior / 'rules'
    rules_dir.mkdir(parents=True, exist_ok=True)
    
    rules_file = rules_dir / 'validation_rules.json'
    rules_file.write_text(json.dumps({'rules': rules}), encoding='utf-8')
    
    return rules_file

def create_common_rules(workspace: Path, rules: list) -> Path:
    """Helper: Create common bot rules."""
    rules_dir = workspace / 'agile_bot' / 'bots' / 'base_bot' / 'rules'
    rules_dir.mkdir(parents=True, exist_ok=True)
    
    rules_file = rules_dir / 'common_rules.json'
    rules_file.write_text(json.dumps({'rules': rules}), encoding='utf-8')
    
    return rules_file

# ============================================================================
# FIXTURES
# ============================================================================

@pytest.fixture
def workspace_root(tmp_path):
    """Fixture: Temporary workspace directory."""
    workspace = tmp_path / 'workspace'
    workspace.mkdir()
    return workspace

# ============================================================================
# STORY: Inject Guardrails as Part of Clarify Requirements
# ============================================================================

class TestInjectGuardrailsAsPartOfClarifyRequirements:
    """Story: Inject Guardrails as Part of Clarify Requirements - Tests guardrail injection."""

    def test_action_injects_questions_and_evidence(self, workspace_root):
        """
        SCENARIO: Action loads and injects guardrails for shape gather_context
        GIVEN: Guardrails configured with key questions and evidence
        WHEN: Action method is invoked
        THEN: Guardrails are injected into instructions
        """
        # Given: Guardrails files exist
        bot_name = 'test_bot'
        behavior = 'shape'
        action = 'gather_context'
        questions = ['What is the scope?', 'Who are the users?']
        evidence = ['Requirements doc', 'User interviews']
        
        questions_file, evidence_file = create_guardrails_files(workspace_root, bot_name, behavior, questions, evidence)
        
        # When: Call REAL GatherContextAction API to inject guardrails
        from agile_bot.bots.base_bot.src.actions.gather_context_action import GatherContextAction
        
        action_obj = GatherContextAction(
            bot_name=bot_name,
            behavior=behavior,
            workspace_root=workspace_root
        )
        instructions = action_obj.inject_questions_and_evidence()
        
        # Then: Guardrails injected into instructions
        assert 'key_questions' in instructions['guardrails']
        assert instructions['guardrails']['key_questions'] == questions
        assert 'evidence' in instructions['guardrails']
        assert instructions['guardrails']['evidence'] == evidence

    def test_action_uses_base_instructions_when_guardrails_missing(self, workspace_root):
        """
        SCENARIO: Action uses base instructions when guardrails do not exist
        GIVEN: Guardrails folder does not exist
        WHEN: Action method is invoked
        THEN: Uses base instructions only with info log
        """
        # Given: No guardrails files
        bot_name = 'test_bot'
        behavior = 'shape'
        action = 'gather_context'
        
        # When: Call REAL GatherContextAction API (guardrails missing)
        from agile_bot.bots.base_bot.src.actions.gather_context_action import GatherContextAction
        
        action_obj = GatherContextAction(
            bot_name=bot_name,
            behavior=behavior,
            workspace_root=workspace_root
        )
        instructions = action_obj.inject_questions_and_evidence()
        
        # Then: Returns instructions without guardrails gracefully
        assert 'guardrails' not in instructions or instructions['guardrails'] == {}

    def test_action_handles_malformed_guardrails_json(self, workspace_root):
        """
        SCENARIO: Action handles malformed guardrails JSON
        GIVEN: key_questions.json has invalid JSON
        WHEN: Action method is invoked
        THEN: Raises JSONDecodeError with clear message
        """
        # Given: Malformed guardrails file
        bot_name = 'test_bot'
        behavior = 'shape'
        guardrails_dir = workspace_root / 'agile_bot' / 'bots' / bot_name / 'behaviors' / behavior / 'guardrails' / 'required_context'
        guardrails_dir.mkdir(parents=True, exist_ok=True)
        
        questions_file = guardrails_dir / 'key_questions.json'
        questions_file.write_text('invalid json {')
        
        # When: Call REAL GatherContextAction API (invalid JSON)
        from agile_bot.bots.base_bot.src.actions.gather_context_action import GatherContextAction
        
        action_obj = GatherContextAction(
            bot_name=bot_name,
            behavior=behavior,
            workspace_root=workspace_root
        )
        
        # Then: Raises JSONDecodeError with helpful message
        with pytest.raises(json.JSONDecodeError) as exc_info:
            action_obj.inject_questions_and_evidence()
        
        assert 'key_questions.json' in str(exc_info.value) or 'Expecting' in str(exc_info.value)

    def test_action_loads_instructions_from_numbered_folder(self, workspace_root):
        """
        SCENARIO: Action loads base instructions from numbered folder (2_gather_context)
        GIVEN: Numbered base action folder exists (2_gather_context)
        WHEN: load_and_merge_instructions is called
        THEN: Instructions loaded from numbered folder with 'instructions' key
        """
        # Given: Create numbered base action folder with instructions
        base_actions_dir = workspace_root / 'agile_bot' / 'bots' / 'base_bot' / 'base_actions'
        numbered_folder = base_actions_dir / '2_gather_context'
        numbered_folder.mkdir(parents=True, exist_ok=True)
        
        instructions_file = numbered_folder / 'instructions.json'
        test_instructions = [
            "Review provided context",
            "Identify key questions",
            "Gather evidence"
        ]
        instructions_file.write_text(
            json.dumps({'instructions': test_instructions}),
            encoding='utf-8'
        )
        
        # When: Call load_and_merge_instructions
        from agile_bot.bots.base_bot.src.actions.gather_context_action import GatherContextAction
        
        action_obj = GatherContextAction(
            bot_name='test_bot',
            behavior='shape',
            workspace_root=workspace_root
        )
        result = action_obj.load_and_merge_instructions()
        
        # Then: Instructions loaded correctly from numbered folder
        assert 'base_instructions' in result
        assert result['base_instructions'] == test_instructions
        assert len(result['base_instructions']) == 3
        assert result['base_instructions'][0] == "Review provided context"

    def test_action_prefers_numbered_folder_over_unnumbered(self, workspace_root):
        """
        SCENARIO: Action prefers numbered folder when both exist
        GIVEN: Both 2_gather_context and gather_context folders exist
        WHEN: load_and_merge_instructions is called
        THEN: Instructions loaded from NUMBERED folder (2_gather_context)
        """
        # Given: Create BOTH numbered and unnumbered folders
        base_actions_dir = workspace_root / 'agile_bot' / 'bots' / 'base_bot' / 'base_actions'
        
        # Create numbered folder with correct instructions
        numbered_folder = base_actions_dir / '2_gather_context'
        numbered_folder.mkdir(parents=True, exist_ok=True)
        numbered_instructions = ["Correct numbered instructions"]
        (numbered_folder / 'instructions.json').write_text(
            json.dumps({'instructions': numbered_instructions}),
            encoding='utf-8'
        )
        
        # Create unnumbered folder with wrong instructions
        unnumbered_folder = base_actions_dir / 'gather_context'
        unnumbered_folder.mkdir(parents=True, exist_ok=True)
        unnumbered_instructions = ["Wrong unnumbered instructions"]
        (unnumbered_folder / 'instructions.json').write_text(
            json.dumps({'instructions': unnumbered_instructions}),
            encoding='utf-8'
        )
        
        # When: Call load_and_merge_instructions
        from agile_bot.bots.base_bot.src.actions.gather_context_action import GatherContextAction
        
        action_obj = GatherContextAction(
            bot_name='test_bot',
            behavior='shape',
            workspace_root=workspace_root
        )
        result = action_obj.load_and_merge_instructions()
        
        # Then: Instructions loaded from NUMBERED folder
        assert result['base_instructions'] == numbered_instructions
        assert result['base_instructions'][0] == "Correct numbered instructions"

    def test_action_uses_instructions_key_not_base_instructions_key(self, workspace_root):
        """
        SCENARIO: Action reads 'instructions' key from JSON (not 'base_instructions')
        GIVEN: instructions.json uses 'instructions' key
        WHEN: load_and_merge_instructions is called
        THEN: Instructions loaded successfully (not empty)
        """
        # Given: Create instruction file with 'instructions' key (standard format)
        base_actions_dir = workspace_root / 'agile_bot' / 'bots' / 'base_bot' / 'base_actions'
        action_folder = base_actions_dir / '2_gather_context'
        action_folder.mkdir(parents=True, exist_ok=True)
        
        # Use 'instructions' key (NOT 'base_instructions')
        instructions_content = {
            'actionName': 'gather_context',
            'instructions': [
                "Step 1",
                "Step 2",
                "Step 3"
            ]
        }
        (action_folder / 'instructions.json').write_text(
            json.dumps(instructions_content),
            encoding='utf-8'
        )
        
        # When: Call load_and_merge_instructions
        from agile_bot.bots.base_bot.src.actions.gather_context_action import GatherContextAction
        
        action_obj = GatherContextAction(
            bot_name='test_bot',
            behavior='shape',
            workspace_root=workspace_root
        )
        result = action_obj.load_and_merge_instructions()
        
        # Then: Instructions loaded (not empty array)
        assert 'base_instructions' in result
        assert len(result['base_instructions']) == 3
        assert result['base_instructions'] == ["Step 1", "Step 2", "Step 3"]


# ============================================================================
# STORY: Inject Planning Criteria Into Instructions
# ============================================================================

class TestInjectPlanningCriteriaIntoInstructions:
    """Story: Inject Planning Criteria Into Instructions - Tests planning criteria injection."""

    def test_action_injects_decision_criteria_and_assumptions(self, workspace_root):
        """
        SCENARIO: Action loads and injects planning criteria for exploration
        GIVEN: Planning guardrails configured with assumptions and criteria
        WHEN: Action method is invoked
        THEN: Planning criteria injected into instructions
        """
        # Given: Planning guardrails exist
        bot_name = 'test_bot'
        behavior = 'exploration'
        action = 'decide_planning_criteria'
        assumptions = ['Stories follow user story format', 'Acceptance criteria are testable']
        criteria = {'scope': ['Component', 'System', 'Solution']}
        
        assumptions_file, criteria_file = create_planning_guardrails(workspace_root, bot_name, behavior, assumptions, criteria)
        
        # When: Call REAL PlanningAction API to inject planning criteria
        from agile_bot.bots.base_bot.src.actions.planning_action import PlanningAction
        
        action_obj = PlanningAction(
            bot_name=bot_name,
            behavior=behavior,
            workspace_root=workspace_root
        )
        instructions = action_obj.inject_decision_criteria_and_assumptions()
        
        # Then: Decision criteria and assumptions injected into instructions
        assert 'decision_criteria' in instructions
        assert 'assumptions' in instructions
        assert instructions['assumptions'] == assumptions
        assert instructions['decision_criteria']['scope'] == criteria['scope']

    def test_action_uses_base_planning_when_guardrails_missing(self, workspace_root):
        """
        SCENARIO: Action uses base planning instructions when guardrails missing
        GIVEN: Planning guardrails do not exist
        WHEN: Action method is invoked
        THEN: Returns None or empty dict gracefully
        """
        # Given: No planning guardrails files
        bot_name = 'test_bot'
        behavior = 'exploration'
        
        # When: Call REAL PlanningAction API (planning guardrails missing)
        from agile_bot.bots.base_bot.src.actions.planning_action import PlanningAction
        
        action_obj = PlanningAction(
            bot_name=bot_name,
            behavior=behavior,
            workspace_root=workspace_root
        )
        instructions = action_obj.inject_decision_criteria_and_assumptions()
        
        # Then: Returns instructions without planning criteria gracefully
        assert 'decision_criteria' not in instructions or instructions['decision_criteria'] == {}
        assert 'assumptions' not in instructions or instructions['assumptions'] == []


# ============================================================================
# STORY: Inject Knowledge Graph Template for Build Knowledge
# ============================================================================

class TestInjectKnowledgeGraphTemplateForBuildKnowledge:
    """Story: Inject Knowledge Graph Template for Build Knowledge - Tests template injection."""

    def test_action_injects_knowledge_graph_template(self, workspace_root):
        """
        SCENARIO: Action loads and injects knowledge graph template for exploration
        GIVEN: Knowledge graph template exists
        WHEN: Action method is invoked
        THEN: Template path injected into instructions
        """
        # Given: Knowledge graph template exists
        bot_name = 'test_bot'
        behavior = 'exploration'
        action = 'build_knowledge'
        template_name = 'story-graph-explored-outline.json'
        
        template_file = create_knowledge_graph_template(workspace_root, bot_name, behavior, template_name)
        
        # When: Call REAL BuildKnowledgeAction API to inject template
        from agile_bot.bots.base_bot.src.actions.build_knowledge_action import BuildKnowledgeAction
        
        action_obj = BuildKnowledgeAction(
            bot_name=bot_name,
            behavior=behavior,
            workspace_root=workspace_root
        )
        instructions = action_obj.inject_knowledge_graph_template()
        
        # Then: Template path injected into instructions
        assert 'knowledge_graph_template' in instructions
        assert template_name in instructions['knowledge_graph_template']
        assert Path(instructions['knowledge_graph_template']).exists()

    def test_action_raises_error_when_template_missing(self, workspace_root):
        """
        SCENARIO: Action handles missing knowledge graph template
        GIVEN: Template does not exist
        WHEN: Action method is invoked for action requiring template
        THEN: Raises FileNotFoundError
        """
        # Given: No knowledge graph template
        bot_name = 'test_bot'
        behavior = 'exploration'
        action = 'build_knowledge'
        
        # When: Call REAL BuildKnowledgeAction API (template missing)
        from agile_bot.bots.base_bot.src.actions.build_knowledge_action import BuildKnowledgeAction
        
        action_obj = BuildKnowledgeAction(
            bot_name=bot_name,
            behavior=behavior,
            workspace_root=workspace_root
        )
        
        # Then: Raises FileNotFoundError for missing template
        with pytest.raises(FileNotFoundError) as exc_info:
            action_obj.inject_knowledge_graph_template()
        
        assert 'Knowledge graph template not found' in str(exc_info.value) or 'template' in str(exc_info.value).lower()


# ============================================================================
# STORY: Inject Validation Rules for Validate Rules Action
# ============================================================================

class TestInjectValidationRulesForValidateRulesAction:
    """Story: Inject Validation Rules for Validate Rules Action - Tests validation rules injection."""

    def test_action_injects_behavior_specific_and_bot_rules(self, workspace_root):
        """
        SCENARIO: Action loads and injects action instructions plus validation rules
        GIVEN: Action instructions, common rules, and behavior-specific rules exist
        WHEN: Action method is invoked
        THEN: Action instructions AND merged rules injected into instructions
        """
        # Given: Action instructions exist in base_actions
        base_actions_dir = workspace_root / 'agile_bot' / 'bots' / 'base_bot' / 'base_actions'
        validate_action_dir = base_actions_dir / '7_validate_rules'
        validate_action_dir.mkdir(parents=True, exist_ok=True)
        
        action_instructions = [
            "Load and review clarification.json and planning.json",
            "Evaluate Content Data against all rules",
            "Generate validation report"
        ]
        (validate_action_dir / 'instructions.json').write_text(
            json.dumps({'actionName': 'validate_rules', 'instructions': action_instructions}),
            encoding='utf-8'
        )
        
        # Given: Both rule files exist
        bot_name = 'test_bot'
        behavior = 'exploration'
        action = 'validate_rules'
        common_rules = ['Rule 1: Stories must have title', 'Rule 2: AC must be testable']
        behavior_rules = ['Rule 3: AC must use Given-When-Then']
        
        common_file = create_common_rules(workspace_root, common_rules)
        behavior_file = create_validation_rules(workspace_root, bot_name, behavior, behavior_rules)
        
        # When: Call REAL ValidateRulesAction API to inject rules
        from agile_bot.bots.base_bot.src.actions.validate_rules_action import ValidateRulesAction
        
        action_obj = ValidateRulesAction(
            bot_name=bot_name,
            behavior=behavior,
            workspace_root=workspace_root
        )
        instructions = action_obj.inject_behavior_specific_and_bot_rules()
        
        # Then: Action instructions AND validation rules injected
        assert 'action_instructions' in instructions, "Missing action_instructions key"
        assert 'validation_rules' in instructions, "Missing validation_rules key"
        
        # Verify action instructions loaded
        assert instructions['action_instructions'] == action_instructions
        assert 'Load and review clarification.json' in instructions['action_instructions'][0]
        
        # Verify rules loaded
        rules = instructions['validation_rules']
        assert any('Stories must have title' in str(rule) for rule in rules)
        assert any('Given-When-Then' in str(rule) for rule in rules)

    def test_action_injects_common_rules_when_behavior_rules_missing(self, workspace_root):
        """
        SCENARIO: Action uses common rules when behavior-specific missing
        GIVEN: Common rules exist but behavior-specific do not
        WHEN: Action method is invoked
        THEN: Uses common rules only
        """
        # Given: Only common rules exist
        bot_name = 'test_bot'
        behavior = 'exploration'
        common_rules = ['Common rule 1', 'Common rule 2']
        create_common_rules(workspace_root, common_rules)
        
        # When: Call REAL ValidateRulesAction API (behavior rules missing)
        from agile_bot.bots.base_bot.src.actions.validate_rules_action import ValidateRulesAction
        
        action_obj = ValidateRulesAction(
            bot_name=bot_name,
            behavior=behavior,
            workspace_root=workspace_root
        )
        instructions = action_obj.inject_common_bot_rules()
        
        # Then: Returns common bot rules only
        assert 'validation_rules' in instructions
        rules = instructions['validation_rules']
        assert len(rules) >= 2
        assert any('Common rule' in str(rule) for rule in rules)

    def test_action_raises_error_when_common_rules_missing(self, workspace_root):
        """
        SCENARIO: Action handles missing common rules
        GIVEN: Common rules do not exist
        WHEN: Action method is invoked
        THEN: Raises FileNotFoundError
        """
        # Given: No common rules files
        bot_name = 'test_bot'
        behavior = 'exploration'
        
        # When: Call REAL ValidateRulesAction API (common rules missing)
        from agile_bot.bots.base_bot.src.actions.validate_rules_action import ValidateRulesAction
        
        action_obj = ValidateRulesAction(
            bot_name=bot_name,
            behavior=behavior,
            workspace_root=workspace_root
        )
        
        # Then: Raises FileNotFoundError for missing common rules
        with pytest.raises(FileNotFoundError) as exc_info:
            action_obj.inject_common_bot_rules()
        
        assert 'Common bot rules not found' in str(exc_info.value) or 'rules' in str(exc_info.value).lower()

    def test_action_loads_individual_rule_files_from_directory(self, workspace_root):
        """
        SCENARIO: Action loads all individual rule JSON files from rules directory
        GIVEN: Rules directory contains multiple individual rule files
        WHEN: Action method is invoked
        THEN: All rule files are loaded and included in validation rules
        """
        # Given: Multiple individual rule files exist (like story_bot's 8_tests behavior)
        bot_name = 'test_bot'
        behavior = 'spec_tests'
        
        rules_dir = workspace_root / 'agile_bot' / 'bots' / bot_name / 'behaviors' / behavior / 'rules'
        rules_dir.mkdir(parents=True, exist_ok=True)
        
        # Create individual rule files (like story_bot pattern)
        rule1_file = rules_dir / 'test_file_naming.json'
        rule1_file.write_text(json.dumps({
            'description': 'Test files must be named after sub-epics',
            'key_principles': ['test_sub_epic_name.py']
        }), encoding='utf-8')
        
        rule2_file = rules_dir / 'ubiquitous_language.json'
        rule2_file.write_text(json.dumps({
            'description': 'Use domain language in tests',
            'key_principles': ['Story nouns become classes']
        }), encoding='utf-8')
        
        rule3_file = rules_dir / 'use_arrange_act_assert.json'
        rule3_file.write_text(json.dumps({
            'description': 'Tests follow AAA pattern',
            'key_principles': ['Arrange, Act, Assert']
        }), encoding='utf-8')
        
        # Also create common rules
        create_common_rules(workspace_root, ['Common rule'])
        
        # When: Call ValidateRulesAction to load rules
        from agile_bot.bots.base_bot.src.actions.validate_rules_action import ValidateRulesAction
        
        action_obj = ValidateRulesAction(
            bot_name=bot_name,
            behavior=behavior,
            workspace_root=workspace_root
        )
        instructions = action_obj.inject_behavior_specific_and_bot_rules()
        
        # Then: All individual rule files loaded
        assert 'validation_rules' in instructions
        rules = instructions['validation_rules']
        
        # Should have common rule + 3 individual behavior rule files
        assert len(rules) >= 4  # 1 common + 3 behavior rules
        
        # Verify individual rule files are included
        rule_files = [rule.get('rule_file') for rule in rules if isinstance(rule, dict) and 'rule_file' in rule]
        assert 'test_file_naming.json' in rule_files
        assert 'ubiquitous_language.json' in rule_files
        assert 'use_arrange_act_assert.json' in rule_files
        
        # Verify rule content is loaded
        rule_contents = [rule.get('rule_content') for rule in rules if isinstance(rule, dict) and 'rule_content' in rule]
        assert any('Test files must be named' in str(content) for content in rule_contents)
        assert any('domain language' in str(content) for content in rule_contents)
        assert any('AAA pattern' in str(content) for content in rule_contents)

    def test_action_prefers_single_validation_rules_file_over_individual_files(self, workspace_root):
        """
        SCENARIO: Action prefers single validation_rules.json if it exists
        GIVEN: Both validation_rules.json and individual rule files exist
        WHEN: Action method is invoked
        THEN: Only validation_rules.json is loaded (not individual files)
        """
        # Given: Both single file and individual files exist
        bot_name = 'test_bot'
        behavior = 'exploration'
        
        rules_dir = workspace_root / 'agile_bot' / 'bots' / bot_name / 'behaviors' / behavior / 'rules'
        rules_dir.mkdir(parents=True, exist_ok=True)
        
        # Create single validation_rules.json
        validation_file = rules_dir / 'validation_rules.json'
        validation_file.write_text(json.dumps({
            'rules': ['Rule from validation_rules.json']
        }), encoding='utf-8')
        
        # Also create individual rule files
        other_file = rules_dir / 'other_rule.json'
        other_file.write_text(json.dumps({
            'description': 'This should be ignored'
        }), encoding='utf-8')
        
        create_common_rules(workspace_root, ['Common rule'])
        
        # When: Call ValidateRulesAction
        from agile_bot.bots.base_bot.src.actions.validate_rules_action import ValidateRulesAction
        
        action_obj = ValidateRulesAction(
            bot_name=bot_name,
            behavior=behavior,
            workspace_root=workspace_root
        )
        instructions = action_obj.inject_behavior_specific_and_bot_rules()
        
        # Then: Only validation_rules.json loaded (not individual files)
        rules = instructions['validation_rules']
        assert any('validation_rules.json' in str(rule) for rule in rules)
        assert not any('other_rule.json' in str(rule) for rule in rules)
        assert not any('This should be ignored' in str(rule) for rule in rules)

    def test_action_loads_rules_from_numbered_rules_folder(self, workspace_root):
        """
        SCENARIO: Action loads rules from numbered rules folder (e.g., 3_rules)
        GIVEN: Behavior has 3_rules folder (not just rules)
        WHEN: Action method is invoked
        THEN: Rules are loaded from 3_rules folder
        """
        # Given: Rules in 3_rules folder (like story_bot scenarios behavior)
        bot_name = 'story_bot'
        behavior = '6_scenarios'
        
        rules_dir = workspace_root / 'agile_bot' / 'bots' / bot_name / 'behaviors' / behavior / '3_rules'
        rules_dir.mkdir(parents=True, exist_ok=True)
        
        # Create individual rule files in 3_rules folder
        rule1_file = rules_dir / 'given_describes_state_not_actions.json'
        rule1_file.write_text(json.dumps({
            'description': 'Given statements describe STATE not actions',
            'examples': []
        }), encoding='utf-8')
        
        rule2_file = rules_dir / 'write_plain_english_scenarios.json'
        rule2_file.write_text(json.dumps({
            'description': 'Write scenarios in plain English',
            'examples': []
        }), encoding='utf-8')
        
        create_common_rules(workspace_root, ['Common rule'])
        
        # When: Call ValidateRulesAction
        from agile_bot.bots.base_bot.src.actions.validate_rules_action import ValidateRulesAction
        
        action_obj = ValidateRulesAction(
            bot_name=bot_name,
            behavior=behavior,
            workspace_root=workspace_root
        )
        instructions = action_obj.inject_behavior_specific_and_bot_rules()
        
        # Then: Rules loaded from 3_rules folder
        assert 'validation_rules' in instructions
        rules = instructions['validation_rules']
        
        # Should have common rule + 2 behavior rules from 3_rules folder
        assert len(rules) >= 3
        
        # Verify rule files from 3_rules are included
        rule_files = [rule.get('rule_file') for rule in rules if isinstance(rule, dict) and 'rule_file' in rule]
        assert 'given_describes_state_not_actions.json' in rule_files
        assert 'write_plain_english_scenarios.json' in rule_files


# ============================================================================
# STORY: Inject Load Rendered Content Instructions
# ============================================================================

class TestInjectLoadRenderedContentInstructions:
    """Story: Inject Load Rendered Content Instructions - Tests rendered content instruction injection."""

    def test_action_injects_instructions_to_load_rendered_acceptance_criteria(self, workspace_root):
        """
        SCENARIO: Action injects instructions to load rendered acceptance criteria
        GIVEN: Rendered content exists
        WHEN: Action needs to load content
        THEN: Load instructions injected with file path
        """
        # Given: Rendered content file exists
        bot_name = 'test_bot'
        behavior = 'discovery'
        action = 'gather_context'
        
        rendered_path = workspace_root / 'agile_bot' / 'bots' / bot_name / 'docs' / 'stories' / 'acceptance-criteria.md'
        rendered_path.parent.mkdir(parents=True, exist_ok=True)
        rendered_path.write_text('# Acceptance Criteria\n\n- AC1: System loads config\n- AC2: System validates data')
        
        # When: Call REAL GatherContextAction API to inject content paths
        from agile_bot.bots.base_bot.src.actions.gather_context_action import GatherContextAction
        
        action_obj = GatherContextAction(
            bot_name=bot_name,
            behavior=behavior,
            workspace_root=workspace_root
        )
        instructions = action_obj.inject_gather_context_instructions()
        
        # Then: Content path injected into instructions
        assert 'rendered_content_paths' in instructions
        assert 'acceptance-criteria.md' in str(instructions['rendered_content_paths'])
        assert any(Path(p).exists() for p in instructions['rendered_content_paths'])

    def test_action_handles_missing_rendered_content_file(self, workspace_root):
        """
        SCENARIO: Action handles missing rendered content file
        GIVEN: Rendered content does not exist
        WHEN: Action injects instructions
        THEN: Returns empty list or includes fallback guidance
        """
        # Given: No rendered content files
        bot_name = 'test_bot'
        behavior = 'discovery'
        action = 'gather_context'
        
        # When: Call REAL GatherContextAction API (rendered content missing)
        from agile_bot.bots.base_bot.src.actions.gather_context_action import GatherContextAction
        
        action_obj = GatherContextAction(
            bot_name=bot_name,
            behavior=behavior,
            workspace_root=workspace_root
        )
        instructions = action_obj.inject_gather_context_instructions()
        
        # Then: Returns empty list or includes fallback message
        assert 'rendered_content_paths' in instructions
        assert (
            instructions['rendered_content_paths'] == [] or
            'not rendered yet' in str(instructions).lower() or
            'run render action' in str(instructions).lower()
        )






