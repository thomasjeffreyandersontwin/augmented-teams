"""
Build Knowledge Tests

Tests for all stories in the 'Build Knowledge' sub-epic:
- Track Activity for Build Knowledge Action
- Proceed To Render Output
"""
import pytest
from pathlib import Path
import json

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
# STORY: Track Activity for Build Knowledge Action
# ============================================================================

class TestTrackActivityForBuildKnowledgeAction:
    """Story: Track Activity for Build Knowledge Action - Tests activity tracking for build_knowledge."""

    def test_track_activity_when_build_knowledge_action_starts(self, workspace_root):
        """
        SCENARIO: Track activity when build_knowledge action starts
        GIVEN: action is 'build_knowledge'
        WHEN: action starts execution
        THEN: Activity logger creates entry with action_state
        """
        # Given: Activity log initialized
        log_file = create_activity_log_file(workspace_root)
        
        # When: Action starts
        from agile_bot.bots.base_bot.src.actions.build_knowledge_action import BuildKnowledgeAction
        action = BuildKnowledgeAction(
            bot_name='story_bot',
            behavior='exploration',
            workspace_root=workspace_root
        )
        action.track_activity_on_start()
        
        # Then: Activity logged
        from tinydb import TinyDB
        with TinyDB(log_file) as db:
            log_data = db.all()
            assert any(
                e['action_state'] == 'story_bot.exploration.build_knowledge'
                for e in log_data
            )

    def test_track_activity_when_build_knowledge_action_completes(self, workspace_root):
        """
        SCENARIO: Track activity when build_knowledge action completes
        GIVEN: build_knowledge action started
        WHEN: action finishes execution
        THEN: Activity logger creates completion entry with outputs and duration
        """
        # Given: Activity log
        log_file = create_activity_log_file(workspace_root)
        
        # When: Action completes
        from agile_bot.bots.base_bot.src.actions.build_knowledge_action import BuildKnowledgeAction
        action = BuildKnowledgeAction(
            bot_name='story_bot',
            behavior='exploration',
            workspace_root=workspace_root
        )
        action.track_activity_on_completion(
            outputs={'knowledge_items_count': 12, 'file_path': 'knowledge.json'},
            duration=420
        )
        
        # Then: Completion logged with metrics
        from tinydb import TinyDB
        with TinyDB(log_file) as db:
            log_data = db.all()
            completion_entry = next((e for e in log_data if 'outputs' in e), None)
            assert completion_entry is not None
            assert completion_entry['duration'] == 420


# ============================================================================
# STORY: Proceed To Render Output
# ============================================================================

class TestProceedToRenderOutput:
    """Story: Proceed To Render Output - Tests transition to render_output action."""

    def test_seamless_transition_from_build_knowledge_to_render_output(self, workspace_root):
        """
        SCENARIO: Seamless transition from build_knowledge to render_output
        GIVEN: build_knowledge action is complete
        WHEN: action finalizes
        THEN: Workflow proceeds to render_output
        """
        # Given: Workflow state
        create_workflow_state(workspace_root, 'story_bot.discovery.build_knowledge')
        
        # When: Action transitions
        from agile_bot.bots.base_bot.src.actions.build_knowledge_action import BuildKnowledgeAction
        action = BuildKnowledgeAction(
            bot_name='story_bot',
            behavior='discovery',
            workspace_root=workspace_root
        )
        result = action.finalize_and_transition()
        
        # Then: Next action is render_output
        assert result.next_action == 'render_output'

    def test_workflow_state_captures_build_knowledge_completion(self, workspace_root):
        """
        SCENARIO: Workflow state captures build_knowledge completion
        GIVEN: build_knowledge action completes
        WHEN: Action saves workflow state
        THEN: completed_actions includes build_knowledge entry
        """
        # Given: Workflow state
        state_file = create_workflow_state(workspace_root, 'story_bot.exploration.build_knowledge')
        
        # When: Save completion
        from agile_bot.bots.base_bot.src.actions.build_knowledge_action import BuildKnowledgeAction
        action = BuildKnowledgeAction(
            bot_name='story_bot',
            behavior='exploration',
            workspace_root=workspace_root
        )
        action.save_state_on_completion()
        
        # Then: Completion captured
        state_data = json.loads(state_file.read_text(encoding='utf-8'))
        assert any(
            'build_knowledge' in entry.get('action_state', '')
            for entry in state_data.get('completed_actions', [])
        )

