import logging
from pathlib import Path
from typing import Dict, Any, List, Callable, TYPE_CHECKING
from agile_bot.bots.base_bot.src.actions.clarify.requirements_clarifications import RequirementsClarifications
from agile_bot.bots.base_bot.src.actions.strategy.strategy_decision import StrategyDecision
if TYPE_CHECKING:
    from agile_bot.bots.base_bot.src.bot.behavior import Behavior
logger = logging.getLogger(__name__)

class ContextDataInjector:

    def __init__(self, behavior: 'Behavior'):
        self.behavior = behavior

    def _inject_data(self, instructions: Dict[str, Any], loader: Callable, key: str, messages: List[str]) -> list:
        bot_paths = self.behavior.bot_paths
        data = loader(bot_paths)
        if not data:
            return []
        instructions[key] = data
        return messages

    def inject_clarification_data(self, instructions: Dict[str, Any]) -> list:
        return self._inject_data(
            instructions,
            RequirementsClarifications.load_all,
            'clarification',
            ['', '**CLARIFICATION DATA AVAILABLE:**', "The 'clarification' data in your instructions contains answers to key questions and evidence gathered from previous clarification sessions across all behaviors.", 'This data represents the context and requirements that have been established. Use this information to inform your decisions and ensure consistency with previously gathered requirements.', "The clarification data is organized by behavior name, with each behavior containing 'key_questions' (questions and answers) and 'evidence' (required and provided evidence)."]
        )

    def inject_strategy_data(self, instructions: Dict[str, Any]) -> list:
        return self._inject_data(
            instructions,
            StrategyDecision.load_all,
            'strategy',
            ['', '**STRATEGY DATA AVAILABLE:**', "The 'strategy' data in your instructions contains planning decisions and assumptions made during previous strategy sessions across all behaviors.", 'This data represents the strategic choices and assumptions that guide how work should be approached. Reference this data to ensure your actions align with established strategic decisions.', "The strategy data is organized by behavior name, with each behavior containing 'strategy_criteria' (decision criteria and decisions made), 'assumptions' (typical assumptions and assumptions made), and 'recommended_activities'."]
        )

    def inject_context_files(self, instructions: Dict[str, Any]) -> list:
        bot_paths = self.behavior.bot_paths
        workspace_directory = bot_paths.workspace_directory
        docs_path = bot_paths.documentation_path
        context_dir = workspace_directory / docs_path / 'context'
        
        # Create context directory if it doesn't exist
        if not context_dir.exists():  # scanner ignore
            context_dir.mkdir(parents=True, exist_ok=True)
            logger.info(f"Created context directory: {context_dir}")
        
        context_files = []
        for file_path in context_dir.iterdir():
            if file_path.is_file():
                context_files.append(file_path.name)
        instructions['context_files'] = context_files
        return ['', '**ORIGINAL CONTEXT FILES AVAILABLE:**', f"The following original context files are available in the docs/context/ folder: {', '.join(context_files)}", 'These files contain the original input files, prompts, and source material provided at the start of the project.', 'You can read these files directly from the docs/context/ folder when you need additional context or to reference the original requirements.', "Common files include 'input.txt' (original input), 'initial-context.md' (initial context), and other source materials."]