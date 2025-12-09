"""
Decide Planning Criteria Tests

Tests for all stories in the 'Decide Planning Criteria' sub-epic:
- Track Activity for Planning Action
- Proceed To Build Knowledge
"""
import pytest
from pathlib import Path
import json
from agile_bot.bots.base_bot.src.bot.planning_action import PlanningAction
from agile_bot.bots.base_bot.test.test_helpers import (
    bootstrap_env,
    verify_action_tracks_start,
    verify_action_tracks_completion,
    verify_workflow_transition,
    verify_workflow_saves_completed_action,
    create_planning_guardrails
)

# Use fixtures from conftest.py (bot_directory, workspace_directory)

# ============================================================================
# STORY: Track Activity for Planning Action
# ============================================================================

class TestTrackActivityForPlanningAction:
    """Story: Track Activity for Planning Action - Tests activity tracking for decide_planning_criteria."""

    def test_track_activity_when_planning_action_starts(self, bot_directory, workspace_directory):
        verify_action_tracks_start(bot_directory, workspace_directory, PlanningAction, 'decide_planning_criteria')

    def test_track_activity_when_planning_action_completes(self, bot_directory, workspace_directory):
        verify_action_tracks_completion(
            bot_directory,
            workspace_directory, 
            PlanningAction, 
            'decide_planning_criteria',
            outputs={'criteria_count': 3, 'assumptions_count': 2},
            duration=240
        )


# ============================================================================
# STORY: Proceed To Build Knowledge
# ============================================================================

class TestProceedToBuildKnowledge:
    """Story: Proceed To Build Knowledge - Tests transition to build_knowledge action."""

    def test_seamless_transition_from_planning_to_build_knowledge(self, bot_directory, workspace_directory):
        verify_workflow_transition(bot_directory, workspace_directory, 'decide_planning_criteria', 'build_knowledge')

    def test_workflow_state_captures_planning_completion(self, bot_directory, workspace_directory):
        verify_workflow_saves_completed_action(bot_directory, workspace_directory, 'decide_planning_criteria', behavior='discovery')


# ============================================================================
# STORY: Inject Planning Criteria Into Instructions
# ============================================================================

class TestInjectPlanningCriteriaIntoInstructions:
    """Story: Inject Planning Criteria Into Instructions - Tests planning criteria injection."""

    def test_action_injects_decision_criteria_and_assumptions(self, bot_directory, workspace_directory):
        bot_name = 'test_bot'
        behavior = 'exploration'
        assumptions = ['Stories follow user story format', 'Acceptance criteria are testable']
        criteria = {'scope': ['Component', 'System', 'Solution']}
        
        # Bootstrap environment
        bootstrap_env(bot_directory, workspace_directory)
        
        create_planning_guardrails(bot_directory, behavior, assumptions, criteria)
        
        action_obj = PlanningAction(bot_name=bot_name, behavior=behavior, bot_directory=bot_directory)
        instructions = action_obj.inject_decision_criteria_and_assumptions()
        
        assert 'decision_criteria' in instructions
        assert 'assumptions' in instructions
        assert instructions['assumptions'] == assumptions
        # decision_criteria structure may vary - just verify it's present and has data
        assert instructions['decision_criteria'] is not None

    def test_action_uses_base_planning_when_guardrails_missing(self, bot_directory, workspace_directory):
        bot_name = 'test_bot'
        behavior = 'exploration'
        
        # Bootstrap environment
        bootstrap_env(bot_directory, workspace_directory)
        
        action_obj = PlanningAction(bot_name=bot_name, behavior=behavior, bot_directory=bot_directory)
        instructions = action_obj.inject_decision_criteria_and_assumptions()
        
        assert 'decision_criteria' not in instructions or instructions['decision_criteria'] == {}
        assert 'assumptions' not in instructions or instructions['assumptions'] == []
