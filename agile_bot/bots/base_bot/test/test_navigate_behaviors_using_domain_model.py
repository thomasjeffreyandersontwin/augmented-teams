"""
Sub-epic: Navigate Bot Behaviors and Actions With CLI

Domain-focused navigation tests (Behaviors/Actions) replacing legacy CLI
command parsing checks.
"""
import json
from pathlib import Path

from conftest import bootstrap_env, create_bot_config_file
from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json, create_base_actions_structure
from agile_bot.bots.base_bot.test.test_execute_behavior_actions import create_minimal_guardrails_files
from agile_bot.bots.base_bot.src.bot.bot import Bot


def _setup_bot(tmp_path, behaviors):
    bot_dir = tmp_path / "agile_bot" / "bots" / "story_bot"
    workspace_dir = tmp_path / "workspace"
    bot_dir.mkdir(parents=True, exist_ok=True)
    workspace_dir.mkdir(parents=True, exist_ok=True)

    create_base_actions_structure(bot_dir)
    create_bot_config_file(bot_dir, "story_bot", behaviors)

    for idx, behavior_name in enumerate(behaviors, start=1):
        create_actions_workflow_json(bot_dir, behavior_name, order=idx)
        create_minimal_guardrails_files(bot_dir, behavior_name, "story_bot")

    bootstrap_env(bot_dir, workspace_dir)
    bot = Bot(bot_name="story_bot", bot_directory=bot_dir, config_path=bot_dir / "bot_config.json")
    return bot, workspace_dir


def _read_state(workspace_dir: Path) -> dict:
    state_file = workspace_dir / "behavior_action_state.json"
    assert state_file.exists(), "State file should exist after navigation"
    return json.loads(state_file.read_text(encoding="utf-8"))


def test_navigate_sets_current_behavior_and_first_action(tmp_path):
    bot, workspace_dir = _setup_bot(tmp_path, ["shape", "discovery"])

    bot.behaviors.navigate_to("shape")

    assert bot.behaviors.current.name == "shape"
    assert bot.behaviors.current.actions.current_action_name == "clarify"

    state = _read_state(workspace_dir)
    assert state["current_behavior"] == "story_bot.shape"
    if state.get("current_action"):
        assert state["current_action"].startswith("story_bot.shape.clarify")


def test_close_current_advances_and_persists_state(tmp_path):
    bot, workspace_dir = _setup_bot(tmp_path, ["shape"])
    bot.behaviors.navigate_to("shape")

    actions = bot.behaviors.current.actions
    actions.close_current()  # complete clarify -> advance to strategy

    assert actions.current_action_name == "strategy"
    state = _read_state(workspace_dir)
    completed = [a.get("action_state") for a in state.get("completed_actions", [])]
    assert "story_bot.shape.clarify" in completed
    assert state.get("current_action") == "story_bot.shape.strategy"


def test_remaining_actions_respects_completion(tmp_path):
    bot, workspace_dir = _setup_bot(tmp_path, ["shape"])
    bot.behaviors.navigate_to("shape")

    actions = bot.behaviors.current.actions
    assert "strategy" in actions.remaining_actions

    actions.close_current()  # completes clarify, moves to strategy
    remaining = actions.remaining_actions
    assert "clarify" not in remaining
    assert remaining == ["validate", "render"]

