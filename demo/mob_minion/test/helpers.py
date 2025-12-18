"""
Helper functions for mob_minion tests.

These helpers extract common Given/When/Then patterns to reduce duplication
and improve test readability. All helpers follow BDD naming conventions.
"""
from domain.mob import Mob
from domain.minion import Minion
from domain.strategy import Strategy
from domain.mob_template import MobTemplate
from domain.target import Target
from managers.strategy_manager import StrategyManager
from managers.template_manager import TemplateManager
from managers.mob_manager import MobManager
from combat.combat_tracker import CombatTracker


# ============================================================================
# GIVEN HELPERS - Setup test state
# ============================================================================

def given_mob_exists():
    """Given: Mob exists - creates and returns a new Mob instance."""
    return Mob()


def given_mob_with_minions(actor_ids):
    """Given: Mob exists with minions - creates Mob and adds minions."""
    mob = Mob()
    for actor_id in actor_ids:
        minion = Minion(actor_id=actor_id)
        mob.add_minion(minion)
    return mob


def given_mob_with_strategy(strategy_name):
    """Given: Mob exists with assigned strategy - creates Mob and assigns strategy."""
    mob = Mob()
    strategy = Strategy(name=strategy_name)
    mob.assign_strategy(strategy)
    return mob


def given_mob_with_minions_and_strategy(actor_ids, strategy_name):
    """Given: Mob exists with minions and strategy - creates fully configured Mob."""
    mob = given_mob_with_minions(actor_ids)
    strategy = Strategy(name=strategy_name)
    mob.assign_strategy(strategy)
    return mob


def given_strategy_manager():
    """Given: Strategy Manager exists - creates and returns StrategyManager."""
    return StrategyManager()


def given_strategy(name):
    """Given: Strategy exists - creates and returns Strategy with given name."""
    return Strategy(name=name)


def given_available_strategies(mob):
    """Given: Available strategies - returns available and compatible strategies."""
    strategy_manager = StrategyManager()
    available_strategies = strategy_manager.get_available_strategies()
    compatible_strategies = strategy_manager.get_compatible_strategies(mob)
    return available_strategies, compatible_strategies


def given_template_manager():
    """Given: Template Manager exists - creates and returns TemplateManager."""
    return TemplateManager()


def given_template(name):
    """Given: Template exists - creates and returns MobTemplate with given name."""
    return MobTemplate(name=name)


def given_saved_template(template_manager, template):
    """Given: Template is saved - saves template and returns it."""
    template_manager.save_template(template)
    return template


def given_mob_manager():
    """Given: Mob Manager exists - creates and returns MobManager."""
    return MobManager()


def given_mob_in_manager(mob_manager, mob):
    """Given: Mob is in manager - adds mob to manager and returns mob."""
    mob_manager.add_mob(mob)
    return mob


def given_combat_tracker():
    """Given: Combat Tracker exists - creates and returns CombatTracker."""
    return CombatTracker()


def given_target(actor_id):
    """Given: Target exists - creates and returns Target with given actor_id."""
    return Target(actor_id=actor_id)


def given_targets_in_combat(combat_tracker, actor_ids):
    """Given: Targets are in combat - adds targets to tracker and returns list."""
    targets = []
    for actor_id in actor_ids:
        target = Target(actor_id=actor_id)
        combat_tracker.add_target(target)
        targets.append(target)
    return targets


# ============================================================================
# WHEN HELPERS - Perform actions
# ============================================================================

def when_game_master_views_available_strategies(mob):
    """When: Game Master views available strategies - returns available and compatible strategies."""
    strategy_manager = StrategyManager()
    available_strategies = strategy_manager.get_available_strategies()
    compatible_strategies = strategy_manager.get_compatible_strategies(mob)
    return available_strategies, compatible_strategies


def when_game_master_assigns_strategy_to_mob(mob, strategy):
    """When: Game Master assigns strategy to mob - assigns strategy and returns assigned strategy."""
    mob.assign_strategy(strategy)
    return mob.get_strategy()


def when_game_master_adds_minions_to_mob(mob, actor_ids):
    """When: Game Master adds minions to mob - adds minions and returns mob."""
    for actor_id in actor_ids:
        minion = Minion(actor_id=actor_id)
        mob.add_minion(minion)
    return mob


def when_game_master_views_mob(mob):
    """When: Game Master views mob - returns minions, status, and strategy."""
    minions = mob.get_minions()
    status = mob.get_status()
    assigned_strategy = mob.get_strategy()
    return minions, status, assigned_strategy


# ============================================================================
# THEN HELPERS - Verify outcomes
# ============================================================================

def then_mob_has_minions(mob, expected_count):
    """Then: Mob has expected number of minions - verifies minion count."""
    assert len(mob.get_minions()) == expected_count


def then_mob_has_strategy(mob, expected_strategy_name):
    """Then: Mob has expected strategy - verifies strategy assignment."""
    assigned_strategy = mob.get_strategy()
    assert assigned_strategy is not None
    assert assigned_strategy.name == expected_strategy_name


def then_mob_has_no_strategy(mob):
    """Then: Mob has no strategy - verifies no strategy is assigned."""
    assert mob.get_strategy() is None


def then_strategies_have_descriptions(available_strategies):
    """Then: Strategies have descriptions - verifies all strategies have descriptions."""
    for strategy in available_strategies:
        assert strategy.description is not None













