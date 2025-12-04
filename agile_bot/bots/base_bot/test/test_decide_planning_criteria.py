"""
Decide Planning Criteria Tests

Tests for all stories in the 'Decide Planning Criteria' sub-epic:
- Track Activity for Planning Action
- Proceed To Build Knowledge
"""
import pytest
from pathlib import Path
import json
from agile_bot.bots.base_bot.test.test_helpers import read_activity_log

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def create_activity_log_file(workspace: Path) -> Path:
    """Helper: Create activity log file."""
    log_dir = workspace / 'project_area'
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / 'activity_log.json'
    log_file.write_text(json.dumps({'_default': {}}), encoding='utf-8')
    return log_file

def create_workflow_state(workspace: Path, current_action: str, completed_actions: list = None) -> Path:
    """Helper: Create workflow state file."""
    state_dir = workspace / 'project_area'
    state_dir.mkdir(parents=True, exist_ok=True)
    state_file = state_dir / 'workflow_state.json'
    state_file.write_text(json.dumps({
        'current_behavior': 'story_bot.exploration',
        'current_action': current_action,
        'completed_actions': completed_actions or [],
        'timestamp': '2025-12-03T10:00:00Z'
    }), encoding='utf-8')
    return state_file

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
# STORY: Track Activity for Planning Action
# ============================================================================

class TestTrackActivityForPlanningAction:
    """Story: Track Activity for Planning Action - Tests activity tracking for decide_planning_criteria."""

    def test_track_activity_when_planning_action_starts(self, workspace_root):
        """
        SCENARIO: Track activity when planning action starts
        GIVEN: action is 'decide_planning_criteria'
        WHEN: action starts execution
        THEN: Activity logger creates entry with action_state
        """
        # Given: Activity log initialized
        log_file = create_activity_log_file(workspace_root)
        
        # When: Action starts
        from agile_bot.bots.base_bot.src.actions.planning_action import PlanningAction
        action = PlanningAction(
            bot_name='story_bot',
            behavior='exploration',
            workspace_root=workspace_root
        )
        action.track_activity_on_start()
        
        # Then: Activity logged
        log_data = read_activity_log(log_file)
        assert any(
            e['action_state'] == 'story_bot.exploration.decide_planning_criteria'
            for e in log_data
        )

    def test_track_activity_when_planning_action_completes(self, workspace_root):
        """
        SCENARIO: Track activity when planning action completes
        GIVEN: planning action started
        WHEN: action finishes execution
        THEN: Activity logger creates completion entry with outputs
        """
        # Given: Activity log
        log_file = create_activity_log_file(workspace_root)
        
        # When: Action completes
        from agile_bot.bots.base_bot.src.actions.planning_action import PlanningAction
        action = PlanningAction(
            bot_name='story_bot',
            behavior='exploration',
            workspace_root=workspace_root
        )
        action.track_activity_on_completion(
            outputs={'criteria_count': 3, 'assumptions_count': 2},
            duration=240
        )
        
        # Then: Completion logged
        log_data = read_activity_log(log_file)
        completion_entry = next((e for e in log_data if 'outputs' in e), None)
        assert completion_entry is not None
        assert completion_entry['outputs']['criteria_count'] == 3


# ============================================================================
# STORY: Proceed To Build Knowledge
# ============================================================================

class TestProceedToBuildKnowledge:
    """Story: Proceed To Build Knowledge - Tests transition to build_knowledge action."""

    def test_seamless_transition_from_planning_to_build_knowledge(self, workspace_root):
        """
        SCENARIO: Seamless transition from planning to build_knowledge
        GIVEN: decide_planning_criteria action is complete
        WHEN: action finalizes
        THEN: Workflow proceeds to build_knowledge
        """
        # Given: Workflow state
        create_workflow_state(workspace_root, 'story_bot.exploration.decide_planning_criteria')
        
        # When: Action transitions
        from agile_bot.bots.base_bot.src.actions.planning_action import PlanningAction
        action = PlanningAction(
            bot_name='story_bot',
            behavior='exploration',
            workspace_root=workspace_root
        )
        result = action.finalize_and_transition()
        
        # Then: Next action is build_knowledge
        assert result.next_action == 'build_knowledge'

    def test_workflow_state_captures_planning_completion(self, workspace_root):
        """
        SCENARIO: Workflow state captures planning completion
        GIVEN: planning action completes
        WHEN: Action saves workflow state
        THEN: completed_actions includes planning entry
        """
        # Given: Workflow state
        state_file = create_workflow_state(workspace_root, 'story_bot.discovery.decide_planning_criteria')
        
        # When: Save completion
        from agile_bot.bots.base_bot.src.actions.planning_action import PlanningAction
        action = PlanningAction(
            bot_name='story_bot',
            behavior='discovery',
            workspace_root=workspace_root
        )
        action.save_state_on_completion()
        
        # Then: Completion captured
        state_data = json.loads(state_file.read_text(encoding='utf-8'))
        assert any(
            'decide_planning_criteria' in entry.get('action_state', '')
            for entry in state_data.get('completed_actions', [])
        )

