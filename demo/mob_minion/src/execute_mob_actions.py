"""
Execute Mob Actions Module

Implements the Execute Mob Actions sub-epic functionality for commanding mobs
and executing coordinated actions for all minions in a mob.
"""
from typing import List, Dict, Optional
from .create_mob import Mob


class MobCommandHandler:
    """Handles identification of mob from clicked token.
    
    Story: Click Mob Token To Command
    """
    
    def __init__(self, foundry_token_api, foundry_actor_system):
        """Initialize MobCommandHandler with dependencies.
        
        Args:
            foundry_token_api: Foundry VTT Token API dependency
            foundry_actor_system: Foundry VTT Actor System dependency
        """
        self.foundry_token_api = foundry_token_api
        self.foundry_actor_system = foundry_actor_system
    
    def identify_mob_from_token(self, token_id: str) -> Optional[Mob]:
        """Identify mob associated with clicked token.
        
        Scenario: Game Master clicks mob token to command mob
        
        Args:
            token_id: ID of clicked token
            
        Returns:
            Optional[Mob]: Mob entity if token belongs to mob, None otherwise
        """
        token = self.foundry_token_api.get_token_by_id(token_id)
        
        if not token:
            return None
        
        mob_id = token.get_flag('mob-minion', 'mobId')
        
        if not mob_id:
            return None  # Token doesn't belong to any mob
        
        return self._get_mob_entity(mob_id)
    
    def prepare_action(self, mob: Mob) -> Dict:
        """Prepare to execute action for all minions in mob.
        
        Args:
            mob: Mob entity to prepare
            
        Returns:
            Dict: Action preparation result with mob and minion tokens
        """
        minion_tokens = [
            self.foundry_token_api.get_token_by_id(token_id)
            for token_id in mob.token_ids
        ]
        minion_tokens = [token for token in minion_tokens if token is not None]
        
        return {
            'mob': mob,
            'minion_tokens': minion_tokens,
            'minion_count': len(minion_tokens)
        }
    
    def _get_mob_entity(self, mob_id: str) -> Optional[Mob]:
        """Get mob entity from Foundry actor system.
        
        Args:
            mob_id: Mob entity ID
            
        Returns:
            Optional[Mob]: Mob entity or None if not found
        """
        mob_data = self.foundry_actor_system.get_mob(mob_id)
        
        if not mob_data:
            return None
        
        return Mob(
            mob_id=mob_data.id,
            token_ids=mob_data.token_ids,
            actor_ids=mob_data.actor_ids
        )


class TargetSelector:
    """Determines target based on mob's strategy.
    
    Story: Determine Target From Strategy
    """
    
    def __init__(self, foundry_combat_system):
        """Initialize TargetSelector with dependency.
        
        Args:
            foundry_combat_system: Foundry VTT Combat System dependency
        """
        self.foundry_combat_system = foundry_combat_system
    
    def determine_target_from_strategy(self, mob: Mob) -> Optional[Dict]:
        """Determine target using mob's assigned strategy.
        
        Scenario: System determines target using assigned strategy
        
        Args:
            mob: Mob entity with assigned strategy
            
        Returns:
            Optional[Dict]: Selected target enemy or None if none available
        """
        strategy = mob.strategy or 'Default'
        available_enemies = self.foundry_combat_system.get_available_enemies()
        
        if len(available_enemies) == 0:
            return None
        
        if strategy == 'AttackMostPowerful':
            return self._select_most_powerful_target(available_enemies)
        elif strategy == 'AttackWeakest':
            return self._select_weakest_target(available_enemies)
        elif strategy == 'AttackMostDamaged':
            return self._select_most_damaged_target(available_enemies)
        elif strategy == 'DefendLeader':
            return self._select_leader_target(available_enemies)
        else:
            return self._select_default_target(available_enemies)
    
    def _select_most_powerful_target(self, enemies: List[Dict]) -> Dict:
        """Select most powerful target (highest power level).
        
        Args:
            enemies: Available enemy entities
            
        Returns:
            Dict: Most powerful enemy
        """
        return max(enemies, key=lambda e: self._get_enemy_power(e))
    
    def _select_weakest_target(self, enemies: List[Dict]) -> Dict:
        """Select weakest target (lowest power level).
        
        Args:
            enemies: Available enemy entities
            
        Returns:
            Dict: Weakest enemy
        """
        return min(enemies, key=lambda e: self._get_enemy_power(e))
    
    def _select_most_damaged_target(self, enemies: List[Dict]) -> Dict:
        """Select most damaged target (highest damage taken).
        
        Args:
            enemies: Available enemy entities
            
        Returns:
            Dict: Most damaged enemy
        """
        return max(enemies, key=lambda e: self._get_damage_taken(e))
    
    def _select_leader_target(self, enemies: List[Dict]) -> Dict:
        """Select leader target (for defend leader strategy).
        
        Args:
            enemies: Available enemy entities
            
        Returns:
            Dict: Leader enemy (first available)
        """
        return enemies[0]
    
    def _select_default_target(self, enemies: List[Dict]) -> Dict:
        """Select default target (nearest enemy or first available).
        
        Scenario: System uses default strategy when no strategy assigned
        
        Args:
            enemies: Available enemy entities
            
        Returns:
            Dict: Default target enemy
        """
        return enemies[0]
    
    def _get_enemy_power(self, enemy: Dict) -> int:
        """Get enemy power level.
        
        Args:
            enemy: Enemy entity
            
        Returns:
            int: Power level
        """
        return enemy.get('powerLevel', enemy.get('level', 1))
    
    def _get_damage_taken(self, enemy: Dict) -> int:
        """Get damage taken by enemy.
        
        Args:
            enemy: Enemy entity
            
        Returns:
            int: Damage taken
        """
        max_health = enemy.get('maxHealth', 1)
        current_health = enemy.get('currentHealth', max_health)
        return max_health - current_health


class AttackExecutor:
    """Executes attack actions for all minions in mob.
    
    Story: Execute Attack Action
    """
    
    def __init__(self, foundry_combat_system):
        """Initialize AttackExecutor with dependency.
        
        Args:
            foundry_combat_system: Foundry VTT Combat System dependency
        """
        self.foundry_combat_system = foundry_combat_system
    
    def execute_attack_action(self, action_preparation: Dict, target: Dict) -> List[Dict]:
        """Execute attack for all minions in mob via Foundry combat system.
        
        Scenario: System executes attack for all minions in mob
        
        Args:
            action_preparation: Action preparation result from MobCommandHandler
            target: Target enemy entity
            
        Returns:
            List[Dict]: Array of attack results for each minion
        """
        mob = action_preparation['mob']
        minion_tokens = action_preparation['minion_tokens']
        attack_results = []
        
        for minion_token in minion_tokens:
            attack_result = self._execute_minion_attack(minion_token, target)
            attack_results.append(attack_result)
        
        return attack_results
    
    def _execute_minion_attack(self, minion_token: Dict, target: Dict) -> Dict:
        """Execute attack for a single minion.
        
        Args:
            minion_token: Minion token entity
            target: Target enemy entity
            
        Returns:
            Dict: Attack result with hit/miss and damage
        """
        attack_roll = self.foundry_combat_system.roll_attack(minion_token, target)
        damage_roll = None
        
        if attack_roll.get('hit', False):
            damage_roll = self.foundry_combat_system.roll_damage(minion_token, target)
        
        return {
            'minion_id': minion_token.get('id'),
            'target_id': target.get('id'),
            'hit': attack_roll.get('hit', False),
            'damage': damage_roll.get('total', 0) if damage_roll else 0
        }
