"""
Test that workflow correctly determines next action based on current_action.

Workflow loads state from current_action (source of truth), with fallback to completed_actions if current_action is missing or invalid.
"""
import pytest
import json
import os
from pathlib import Path
from agile_bot.bots.base_bot.src.state.workflow import Workflow
from conftest import bootstrap_env, create_workflow_state_file


# ============================================================================
# INLINE HELPERS - Used only by tests in this file
# ============================================================================

def create_test_workflow(
    bot_dir: Path,
    workspace_dir: Path,
    bot_name: str,
    behavior: str,
    current_action: str,
    completed_actions: list = None
) -> Workflow:
    """Helper: Create workflow with specified state for testing."""
    # Bootstrap environment
    bootstrap_env(bot_dir, workspace_dir)
    
    # Create workflow state file
    create_workflow_state_file(
        workspace_dir, bot_name, behavior, current_action, completed_actions
    )
    
    states = ['gather_context', 'decide_planning_criteria', 
              'build_knowledge', 'render_output', 'validate_rules']
    transitions = [
        {'trigger': 'proceed', 'source': 'gather_context', 'dest': 'decide_planning_criteria'},
        {'trigger': 'proceed', 'source': 'decide_planning_criteria', 'dest': 'build_knowledge'},
        {'trigger': 'proceed', 'source': 'build_knowledge', 'dest': 'render_output'},
        {'trigger': 'proceed', 'source': 'render_output', 'dest': 'validate_rules'},
    ]
    
    return Workflow(
        bot_name=bot_name,
        behavior=behavior,
        bot_directory=bot_dir,
        states=states,
        transitions=transitions
    )


def test_workflow_determines_next_action_from_current_action(bot_directory, workspace_directory):
    """Scenario: Workflow determines next action from current_action (source of truth)"""
    
    # Given workflow_state.json shows:
    #   - current_action: build_knowledge
    #   - completed_actions: [gather_context] (may be behind)
    bot_name = 'story_bot'
    behavior = 'shape'
    completed = [{'action_state': f'{bot_name}.{behavior}.gather_context', 'timestamp': '2025-12-04T15:44:22.812230'}]
    
    # When workflow loads state (current_action is the source of truth)
    workflow = create_test_workflow(bot_directory, workspace_directory, bot_name, behavior, 'build_knowledge', completed)
    
    # Then current_state should be build_knowledge (uses current_action from file)
    assert workflow.current_state == 'build_knowledge'


def test_workflow_starts_at_first_action_when_no_completed_actions(bot_directory, workspace_directory):
    """Scenario: No completed actions yet"""
    
    # Given workflow loads state with no completed_actions
    bot_name = 'story_bot'
    behavior = 'shape'
    
    workflow = create_test_workflow(bot_directory, workspace_directory, bot_name, behavior, 'gather_context', [])
    
    # Then current_state should be the first action (gather_context)
    assert workflow.current_state == 'gather_context'


def test_workflow_uses_current_action_when_provided(bot_directory, workspace_directory):
    """Scenario: Workflow uses current_action when provided"""
    
    # Given current_action: decide_planning_criteria
    # And completed_actions: [gather_context]
    bot_name = 'story_bot'
    behavior = 'shape'
    completed = [
        {'action_state': f'{bot_name}.{behavior}.gather_context', 'timestamp': '2025-12-04T15:45:00.000000'}
    ]
    
    workflow = create_test_workflow(bot_directory, workspace_directory, bot_name, behavior, 'decide_planning_criteria', completed)
    
    # Then current_state should be decide_planning_criteria (uses current_action from file)
    assert workflow.current_state == 'decide_planning_criteria'


def test_workflow_falls_back_to_completed_actions_when_current_action_missing(bot_directory, workspace_directory):
    """Scenario: Workflow falls back to completed_actions when current_action is missing"""
    
    # Given workflow_state.json shows:
    #   - current_action: "" (missing or empty)
    #   - completed_actions: [gather_context]
    bot_name = 'story_bot'
    behavior = 'shape'
    completed = [
        {'action_state': f'{bot_name}.{behavior}.gather_context', 'timestamp': '2025-12-04T15:45:00.000000'}
    ]
    
    # Bootstrap environment
    bootstrap_env(bot_directory, workspace_directory)
    
    # Create workflow state with empty current_action
    workflow_file = workspace_directory / 'workflow_state.json'
    workflow_file.write_text(json.dumps({
        'current_behavior': f'{bot_name}.{behavior}',
        'current_action': '',  # Empty - should trigger fallback
        'completed_actions': completed,
        'timestamp': '2025-12-04T15:45:00.000000'
    }), encoding='utf-8')
    
    states = ['gather_context', 'decide_planning_criteria', 
              'build_knowledge', 'render_output', 'validate_rules']
    transitions = [
        {'trigger': 'proceed', 'source': 'gather_context', 'dest': 'decide_planning_criteria'},
        {'trigger': 'proceed', 'source': 'decide_planning_criteria', 'dest': 'build_knowledge'},
        {'trigger': 'proceed', 'source': 'build_knowledge', 'dest': 'render_output'},
        {'trigger': 'proceed', 'source': 'render_output', 'dest': 'validate_rules'},
    ]
    
    workflow = Workflow(
        bot_name=bot_name,
        behavior=behavior,
        bot_directory=bot_directory,
        states=states,
        transitions=transitions
    )
    
    # Then current_state should be decide_planning_criteria (next after last completed)
    assert workflow.current_state == 'decide_planning_criteria'


def test_workflow_starts_at_first_action_when_no_workflow_state_file_exists(bot_directory, workspace_directory):
    """Scenario: No workflow_state.json file exists (fresh start)"""
    # Given workspace directory exists but workflow_state.json does NOT exist
    bot_name = 'story_bot'
    behavior = 'shape'
    
    # Bootstrap environment
    bootstrap_env(bot_directory, workspace_directory)
    
    workflow_file = workspace_directory / 'workflow_state.json'
    assert not workflow_file.exists()
    
    # When workflow is created
    states = ['gather_context', 'decide_planning_criteria', 
              'build_knowledge', 'render_output', 'validate_rules']
    transitions = [
        {'trigger': 'proceed', 'source': 'gather_context', 'dest': 'decide_planning_criteria'},
        {'trigger': 'proceed', 'source': 'decide_planning_criteria', 'dest': 'build_knowledge'},
        {'trigger': 'proceed', 'source': 'build_knowledge', 'dest': 'render_output'},
        {'trigger': 'proceed', 'source': 'render_output', 'dest': 'validate_rules'},
    ]
    
    workflow = Workflow(bot_name=bot_name, behavior=behavior, bot_directory=bot_directory, states=states, transitions=transitions)
    
    # Then current_state should be the FIRST action (gather_context)
    assert workflow.current_state == 'gather_context'
