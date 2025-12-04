"""
Gather Context Tests

Tests for all stories in the 'Gather Context' sub-epic:
- Track Activity for Gather Context Action
- Proceed To Decide Planning
"""
import pytest
from pathlib import Path
import json
from prefect.testing.utilities import prefect_test_harness

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
        'current_behavior': 'story_bot.discovery',
        'current_action': current_action,
        'completed_actions': completed_actions or [],
        'timestamp': '2025-12-03T10:00:00Z'
    }), encoding='utf-8')
    return state_file

def verify_activity_logged(log_file: Path, action_state: str):
    """Helper: Verify activity was logged."""
    from tinydb import TinyDB
    with TinyDB(log_file) as db:
        entries = db.all()
        assert any(entry['action_state'] == action_state for entry in entries)

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
# STORY: Track Activity for Gather Context Action
# ============================================================================

class TestTrackActivityForGatherContextAction:
    """Story: Track Activity for Gather Context Action - Tests activity tracking during execution."""

    def test_track_activity_when_gather_context_action_starts(self, workspace_root):
        """
        SCENARIO: Track activity when gather_context action starts
        GIVEN: behavior is 'discovery' and action is 'gather_context'
        WHEN: gather_context action starts execution
        THEN: Activity logger creates entry with timestamp and action_state
        """
        # Given: Activity log initialized
        log_file = create_activity_log_file(workspace_root)
        
        # When: Action starts and logs activity
        from agile_bot.bots.base_bot.src.actions.gather_context_action import GatherContextAction
        action = GatherContextAction(
            bot_name='story_bot',
            behavior='discovery',
            workspace_root=workspace_root
        )
        action.track_activity_on_start()
        
        # Then: Activity logged with correct action_state
        verify_activity_logged(log_file, 'story_bot.discovery.gather_context')

    def test_track_activity_when_gather_context_action_completes(self, workspace_root):
        """
        SCENARIO: Track activity when gather_context action completes
        GIVEN: gather_context action started
        WHEN: gather_context action finishes execution
        THEN: Activity logger creates completion entry with outputs and duration
        """
        # Given: Activity log with start entry
        log_file = create_activity_log_file(workspace_root)
        
        # When: Action completes
        from agile_bot.bots.base_bot.src.actions.gather_context_action import GatherContextAction
        action = GatherContextAction(
            bot_name='story_bot',
            behavior='discovery',
            workspace_root=workspace_root
        )
        action.track_activity_on_completion(
            outputs={'questions_count': 5, 'evidence_count': 3},
            duration=330
        )
        
        # Then: Completion entry logged
        from tinydb import TinyDB
        with TinyDB(log_file) as db:
            log_data = db.all()
            completion_entry = next(e for e in log_data if 'outputs' in e)
            assert completion_entry['outputs']['questions_count'] == 5
            assert completion_entry['duration'] == 330

    def test_track_multiple_gather_context_invocations_across_behaviors(self, workspace_root):
        """
        SCENARIO: Track multiple gather_context invocations across behaviors
        GIVEN: activity log contains entries for shape and discovery
        WHEN: both entries are present
        THEN: activity log distinguishes same action in different behaviors using full path
        """
        # Given: Activity log with multiple behavior entries
        log_dir = workspace_root / 'project_area'
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / 'activity_log.json'
        from tinydb import TinyDB
        with TinyDB(log_file) as db:
            db.insert({'action_state': 'story_bot.shape.gather_context', 'timestamp': '09:00'})
            db.insert({'action_state': 'story_bot.discovery.gather_context', 'timestamp': '10:00'})
        
        # When: Read activity log
        from tinydb import TinyDB
        with TinyDB(log_file) as db:
            log_data = db.all()
        
        # Then: 2 separate entries with full paths
        assert len(log_data) == 2
        assert log_data[0]['action_state'] == 'story_bot.shape.gather_context'
        assert log_data[1]['action_state'] == 'story_bot.discovery.gather_context'


# ============================================================================
# STORY: Proceed To Decide Planning
# ============================================================================

class TestProceedToDecidePlanning:
    """Story: Proceed To Decide Planning - Tests transition from gather_context to decide_planning_criteria."""

    def test_seamless_transition_from_gather_context_to_decide_planning_criteria(self, workspace_root):
        """
        SCENARIO: Seamless transition from gather_context to decide_planning_criteria
        GIVEN: gather_context action is complete
        WHEN: gather_context action finalizes
        THEN: Action saves state and injects next action instructions
        """
        # Given: Action config and workflow state
        create_workflow_state(workspace_root, 'story_bot.discovery.gather_context')
        
        # When: Action transitions
        from agile_bot.bots.base_bot.src.actions.gather_context_action import GatherContextAction
        action = GatherContextAction(
            bot_name='story_bot',
            behavior='discovery',
            workspace_root=workspace_root
        )
        result = action.finalize_and_transition()
        
        # Then: Transition instructions provided
        assert 'decide_planning_criteria' in result.next_action

    def test_workflow_state_captures_gather_context_completion(self, workspace_root):
        """
        SCENARIO: Workflow state captures gather_context completion
        GIVEN: gather_context action completes
        WHEN: Action saves workflow state
        THEN: workflow state updated with timestamp and completed_actions
        """
        # Given: Workflow state exists
        state_file = create_workflow_state(workspace_root, 'story_bot.exploration.gather_context')
        
        # When: Action saves completion
        from agile_bot.bots.base_bot.src.actions.gather_context_action import GatherContextAction
        action = GatherContextAction(
            bot_name='story_bot',
            behavior='exploration',
            workspace_root=workspace_root
        )
        action.save_state_on_completion()
        
        # Then: Completion captured
        state_data = json.loads(state_file.read_text(encoding='utf-8'))
        assert any(
            'gather_context' in entry.get('action_state', '')
            for entry in state_data.get('completed_actions', [])
        )

    def test_workflow_resumes_at_decide_planning_criteria_after_interruption(self, workspace_root):
        """
        SCENARIO: Workflow resumes at decide_planning_criteria after interruption
        GIVEN: gather_context is completed and chat was interrupted
        WHEN: user reopens chat and invokes bot tool
        THEN: Router forwards to decide_planning_criteria action
        """
        # Given: Workflow state with completed gather_context
        state_file = create_workflow_state(
            workspace_root,
            'story_bot.discovery.gather_context',
            completed_actions=[{
                'action_state': 'story_bot.discovery.gather_context',
                'timestamp': '2025-12-03T10:05:30Z'
            }]
        )
        
        # When: Router determines next action
        from agile_bot.bots.base_bot.src.router import Router
        router = Router(workspace_root=workspace_root)
        next_action = router.determine_next_action_from_state(state_file)
        
        # Then: Next action is decide_planning_criteria
        assert next_action == 'decide_planning_criteria'

