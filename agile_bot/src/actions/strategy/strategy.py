from pathlib import Path
from typing import Dict, Any, List
from .strategy_criterias import StrategyCriterias
from .assumptions import Assumptions
from ...utils import read_json_file

class Strategy:

    def __init__(self, behavior_folder: Path):
        strategy_dir = behavior_folder / 'guardrails' / 'strategy'
        self.strategy_criterias = StrategyCriterias(strategy_dir)
        self.assumptions = Assumptions(strategy_dir)
        self._strategy_dir = strategy_dir
        self._instructions: List[str] = []
        self._load_instructions()

    def _load_instructions(self):
        """Load instructions from instructions.json if it exists."""
        instructions_file = self._strategy_dir / 'instructions.json'
        if instructions_file.exists():
            instructions_data = read_json_file(instructions_file)
            self._instructions = instructions_data.get('instructions', [])

    @property
    def instructions(self) -> Dict[str, Any]:
        strategy_criteria_dict = {}
        for key, criteria in self.strategy_criterias.strategy_criterias.items():
            strategy_criteria_dict[key] = {'question': criteria.question, 'options': criteria.options, 'outcome': criteria.outcome}
        result = {'strategy_criteria': strategy_criteria_dict, 'assumptions': self.assumptions.assumptions}
        if self._instructions:
            result['instructions'] = self._instructions
        return result
