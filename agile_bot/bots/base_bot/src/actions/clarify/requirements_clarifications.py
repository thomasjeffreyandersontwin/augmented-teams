from typing import Dict, Any, Optional, List, Union
from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
from agile_bot.bots.base_bot.src.actions.strategy.json_persistent import JsonPersistent
from agile_bot.bots.base_bot.src.actions.clarify.required_context import RequiredContext

class RequirementsClarifications(JsonPersistent):

    def __init__(self, behavior_name: str, bot_paths: BotPaths, required_context: RequiredContext, key_questions_answered: Dict[str, Any]=None, evidence_provided: Dict[str, Any]=None, context: Optional[Union[List[str], str]]=None):
        super().__init__(bot_paths, 'clarification.json')
        self.behavior_name = behavior_name
        self.required_context = required_context
        self.key_questions_answered = key_questions_answered or {}
        self.evidence_provided = evidence_provided or {}
        self.context = context

    def save(self):
        existing_data = self.load()
        # Get existing data for this behavior, or create new structure
        behavior_data = existing_data.get(self.behavior_name, {})
        existing_answers = behavior_data.get('key_questions', {}).get('answers', {})
        existing_evidence = behavior_data.get('evidence', {})
        existing_context = behavior_data.get('context')
        
        # Merge answers (new answers override existing)
        merged_answers = {**existing_answers, **self.key_questions_answered}
        # Merge evidence (new evidence overrides existing) - only provided evidence, flat dict structure
        merged_evidence = {**existing_evidence, **self.evidence_provided}
        # Merge context - append new items to existing list
        final_context = existing_context or []
        if self.context is not None:
            if isinstance(self.context, list):
                # Append new context items to existing list
                final_context = final_context if isinstance(final_context, list) else []
                final_context.extend(self.context)
            else:
                # Handle legacy string context - convert to list
                final_context = final_context if isinstance(final_context, list) else []
                final_context.append(self.context)
        
        # New structure: only save answers (questions are keys), only save provided evidence as flat dict, include context
        new_data = {
            'key_questions': {
                'answers': merged_answers
            },
            'evidence': merged_evidence,
            'context': final_context
        }
        merged_data = self.merge(existing_data, new_data, self.behavior_name)
        super().save(merged_data)

    @classmethod
    def load_all(cls, bot_paths: BotPaths) -> Dict[str, Any]:
        instance = cls.__new__(cls)
        instance.bot_paths = bot_paths
        instance.filename = 'clarification.json'
        return instance.load()