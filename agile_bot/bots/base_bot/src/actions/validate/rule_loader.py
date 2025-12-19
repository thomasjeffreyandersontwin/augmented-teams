import logging
from pathlib import Path
from typing import List
from agile_bot.bots.base_bot.src.actions.validate.rule import Rule

class RuleLoader:

    def __init__(self, bot_name: str, behavior_name: str, bot_paths, behavior=None):
        self.bot_name = bot_name
        self.behavior_name = behavior_name
        self.bot_paths = bot_paths
        self.behavior = behavior

    def load_bot_rules(self) -> List[Rule]:
        bot_rules_dir = self.bot_paths.bot_directory / 'rules'
        bot_rules = self._load_rules_from_glob(bot_rules_dir, '*.json', 'common')
        bot_rules.extend(self._load_specialization_rules(bot_rules_dir))
        return bot_rules

    def _load_rules_from_glob(self, rules_dir: Path, pattern: str, behavior: str=None) -> List[Rule]:
        if behavior is None:
            if self.behavior and hasattr(self.behavior, 'name'):
                behavior = self.behavior.name
            else:
                behavior = self.behavior_name if self.behavior_name else 'common'
        rules = []
        for rule_file in rules_dir.glob(pattern):
            if not self._is_in_disabled_folder(rule_file):
                rules.append(Rule(rule_file_path=rule_file, behavior_name=behavior, bot_name=self.bot_name))
        return rules

    def _load_specialization_rules(self, bot_rules_dir: Path) -> List[Rule]:
        specializations_dir = bot_rules_dir / 'specializations'
        if not (specializations_dir.exists() and specializations_dir.is_dir()):
            return []
        rules = []
        for rule_file in specializations_dir.rglob('*.json'):
            if not self._is_in_disabled_folder(rule_file):
                rules.append(Rule(rule_file_path=rule_file, behavior_name='common', bot_name=self.bot_name))
        return rules

    def load_behavior_rules(self) -> List[Rule]:
        behavior_folder = self.bot_paths.bot_directory / 'behaviors' / self.behavior_name
        behavior_rules_dir = behavior_folder / 'rules'
        behavior_rules = []
        for rule_file in behavior_rules_dir.glob('*.json'):
            if not self._is_in_disabled_folder(rule_file):
                behavior_rules.append(self._create_rule(rule_file))
        for subdir_name in ['3_rules', 'rules']:
            subdir = behavior_folder / subdir_name
            if subdir != behavior_rules_dir:
                behavior_rules.extend(self._load_rules_from_subdir(subdir, behavior_rules_dir))
        return behavior_rules

    def _create_rule(self, rule_file: Path) -> Rule:
        return Rule(rule_file_path=rule_file, behavior_name=self.behavior_name, bot_name=self.bot_name)

    def _load_rules_from_subdir(self, subdir: Path, behavior_rules_dir: Path) -> List[Rule]:
        rules = []
        for rule_file in subdir.rglob('*.json'):
            if self._is_in_disabled_folder(rule_file):
                continue
            if behavior_rules_dir.exists() and rule_file.is_relative_to(behavior_rules_dir):
                continue
            try:
                rules.append(self._create_rule(rule_file))
            except Exception:
                continue
        return rules

    def _is_in_disabled_folder(self, file_path: Path) -> bool:
        parts = file_path.parts
        return 'disabled' in parts