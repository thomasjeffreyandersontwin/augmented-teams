from pathlib import Path
from typing import Dict, Any, Type
from agile_bot.bots.base_bot.src.actions.action import Action
from agile_bot.bots.base_bot.src.actions.action_context import ActionContext, ClarifyActionContext
from agile_bot.bots.base_bot.src.actions.clarify.required_context import RequiredContext
from agile_bot.bots.base_bot.src.actions.clarify.requirements_clarifications import RequirementsClarifications

class ClarifyContextAction(Action):
    context_class: Type[ActionContext] = ClarifyActionContext

    def __init__(self, behavior=None, action_config=None):
        super().__init__(behavior=behavior, action_config=action_config)
        self._required_context = RequiredContext(self.behavior.folder)

    @property
    def action_name(self) -> str:
        return 'clarify'

    @action_name.setter
    def action_name(self, value: str):
        raise AttributeError('action_name is read-only for ClarifyContextAction')

    @property
    def required_context(self) -> RequiredContext:
        return self._required_context

    @property
    def key_questions(self):
        return self.required_context.key_questions

    @property
    def evidence(self):
        return self.required_context.evidence

    def do_execute(self, context: ClarifyActionContext) -> Dict[str, Any]:
        instructions = self.instructions.copy()
        instructions.set('guardrails', {'required_context': self.required_context.instructions})
        if context.key_questions_answered or context.evidence_provided:
            self.save_clarification(context)
        return {'instructions': instructions.to_dict()}

    def save_clarification(self, context: ClarifyActionContext):
        clarifications = RequirementsClarifications(
            behavior_name=self.behavior.name,
            bot_paths=self.behavior.bot_paths,
            required_context=self.required_context,
            key_questions_answered=context.key_questions_answered or {},
            evidence_provided=context.evidence_provided or {}
        )
        clarifications.save()