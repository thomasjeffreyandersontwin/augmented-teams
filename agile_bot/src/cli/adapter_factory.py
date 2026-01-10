"""
Factory for creating domain-specific adapters based on domain type and channel.

Uses registry pattern to avoid cyclomatic complexity.
"""

from typing import Any


class AdapterFactory:
    """
    Factory for creating channel adapters for domain objects.
    Uses registry pattern to avoid cyclomatic complexity.
    """
    
    # Registry maps: (domain_type_name, channel) -> (module_path, class_name)
    _registry = {
        # Instructions domain
        ('Instructions', 'json'): ('agile_bot.src.instructions.json_instructions', 'JSONInstructions'),
        ('Instructions', 'tty'): ('agile_bot.src.instructions.tty_instructions', 'TTYInstructions'),
        ('Instructions', 'markdown'): ('agile_bot.src.instructions.markdown_instructions', 'MarkdownInstructions'),
        
        # Guardrails domain objects
        ('Guardrails', 'tty'): ('agile_bot.src.actions.guardrails.tty_guardrails', 'TTYGuardrails'),
        ('RequiredContext', 'tty'): ('agile_bot.src.actions.guardrails.tty_required_context', 'TTYRequiredContext'),
        ('Strategy', 'tty'): ('agile_bot.src.actions.guardrails.tty_strategy', 'TTYStrategy'),
        
        # Scope domain
        ('Scope', 'json'): ('agile_bot.src.scope.json_scope', 'JSONScope'),
        ('Scope', 'tty'): ('agile_bot.src.scope.tty_scope', 'TTYScope'),
        ('Scope', 'markdown'): ('agile_bot.src.scope.markdown_scope', 'MarkdownScope'),
        
        # Navigation domain
        ('NavigationResult', 'json'): ('agile_bot.src.navigation.json_navigation', 'JSONNavigation'),
        ('NavigationResult', 'tty'): ('agile_bot.src.navigation.tty_navigation', 'TTYNavigation'),
        ('NavigationResult', 'markdown'): ('agile_bot.src.navigation.markdown_navigation', 'MarkdownNavigation'),
        
        # BotPath domain (both old BotPaths and new BotPath)
        ('BotPath', 'json'): ('agile_bot.src.bot_path.json_bot_path', 'JSONBotPath'),
        ('BotPath', 'tty'): ('agile_bot.src.bot_path.tty_bot_path', 'TTYBotPath'),
        ('BotPath', 'markdown'): ('agile_bot.src.bot_path.markdown_bot_path', 'MarkdownBotPath'),
        ('BotPaths', 'json'): ('agile_bot.src.bot_path.json_bot_path', 'JSONBotPath'),
        ('BotPaths', 'tty'): ('agile_bot.src.bot_path.tty_bot_path', 'TTYBotPath'),
        ('BotPaths', 'markdown'): ('agile_bot.src.bot_path.markdown_bot_path', 'MarkdownBotPath'),
        
        # Help domain
        ('Help', 'json'): ('agile_bot.src.help.json_help', 'JSONHelp'),
        ('Help', 'tty'): ('agile_bot.src.help.tty_help', 'TTYHelp'),
        ('Help', 'markdown'): ('agile_bot.src.help.markdown_help', 'MarkdownHelp'),
        
        # ExitResult domain
        ('ExitResult', 'json'): ('agile_bot.src.exit_result.json_exit_result', 'JSONExitResult'),
        ('ExitResult', 'tty'): ('agile_bot.src.exit_result.tty_exit_result', 'TTYExitResult'),
        ('ExitResult', 'markdown'): ('agile_bot.src.exit_result.markdown_exit_result', 'MarkdownExitResult'),
        
        # Bot domain
        ('Bot', 'json'): ('agile_bot.src.bot.json_bot', 'JSONBot'),
        ('Bot', 'tty'): ('agile_bot.src.bot.tty_bot', 'TTYBot'),
        ('Bot', 'markdown'): ('agile_bot.src.bot.markdown_bot', 'MarkdownBot'),
        
        # Behavior domain (single)
        ('Behavior', 'json'): ('agile_bot.src.behaviors.json_behavior', 'JSONBehavior'),
        ('Behavior', 'tty'): ('agile_bot.src.behaviors.tty_behavior', 'TTYBehavior'),
        ('Behavior', 'markdown'): ('agile_bot.src.behaviors.markdown_behavior', 'MarkdownBehavior'),
        
        # Behaviors domain (collection)
        ('Behaviors', 'json'): ('agile_bot.src.behaviors.json_behavior', 'JSONBehaviors'),
        ('Behaviors', 'tty'): ('agile_bot.src.behaviors.tty_behavior', 'TTYBehaviors'),
        ('Behaviors', 'markdown'): ('agile_bot.src.behaviors.markdown_behavior', 'MarkdownBehaviors'),
        
        # Actions domain (collection)
        ('Actions', 'json'): ('agile_bot.src.actions.json_actions', 'JSONActions'),
        ('Actions', 'tty'): ('agile_bot.src.actions.tty_actions', 'TTYActions'),
        ('Actions', 'markdown'): ('agile_bot.src.actions.markdown_actions', 'MarkdownActions'),
        
        # ValidateRulesAction
        ('ValidateRulesAction', 'json'): ('agile_bot.src.actions.validate.json_validate_action', 'JSONValidateAction'),
        ('ValidateRulesAction', 'tty'): ('agile_bot.src.actions.validate.tty_validate_action', 'TTYValidateAction'),
        ('ValidateRulesAction', 'markdown'): ('agile_bot.src.actions.validate.markdown_validate_action', 'MarkdownValidateAction'),
        
        # BuildKnowledgeAction (specific)
        ('BuildKnowledgeAction', 'json'): ('agile_bot.src.actions.build.json_build_action', 'JSONBuildAction'),
        ('BuildKnowledgeAction', 'tty'): ('agile_bot.src.actions.build.tty_build_action', 'TTYBuildAction'),
        ('BuildKnowledgeAction', 'markdown'): ('agile_bot.src.actions.build.markdown_build_action', 'MarkdownBuildAction'),
        
        # ClarifyContextAction (specific)
        ('ClarifyContextAction', 'json'): ('agile_bot.src.actions.clarify.json_clarify_action', 'JSONClarifyAction'),
        ('ClarifyContextAction', 'tty'): ('agile_bot.src.actions.clarify.tty_clarify_action', 'TTYClarifyAction'),
        ('ClarifyContextAction', 'markdown'): ('agile_bot.src.actions.clarify.markdown_clarify_action', 'MarkdownClarifyAction'),
        
        # StrategyAction (specific)
        ('StrategyAction', 'json'): ('agile_bot.src.actions.strategy.json_strategy_action', 'JSONStrategyAction'),
        ('StrategyAction', 'tty'): ('agile_bot.src.actions.strategy.tty_strategy_action', 'TTYStrategyAction'),
        ('StrategyAction', 'markdown'): ('agile_bot.src.actions.strategy.markdown_strategy_action', 'MarkdownStrategyAction'),
        
        # RenderOutputAction (specific)
        ('RenderOutputAction', 'json'): ('agile_bot.src.actions.render.json_render_action', 'JSONRenderAction'),
        ('RenderOutputAction', 'tty'): ('agile_bot.src.actions.render.tty_render_action', 'TTYRenderAction'),
        ('RenderOutputAction', 'markdown'): ('agile_bot.src.actions.render.markdown_render_action', 'MarkdownRenderAction'),
        
        # StoryGraph domain
        ('StoryGraph', 'json'): ('agile_bot.src.story_graph.json_story_graph', 'JSONStoryGraph'),
        ('StoryGraph', 'tty'): ('agile_bot.src.story_graph.tty_story_graph', 'TTYStoryGraph'),
        ('StoryGraph', 'markdown'): ('agile_bot.src.story_graph.markdown_story_graph', 'MarkdownStoryGraph'),
    }
    
    @classmethod
    def create(cls, domain_object: Any, channel: str, **kwargs):
        """
        Create appropriate adapter for domain object and channel.
        
        Args:
            domain_object: Domain object to adapt (Status, Scope, etc.)
            channel: Output channel ('json', 'tty', 'markdown')
            **kwargs: Additional arguments to pass to adapter constructor (e.g., is_current)
        
        Returns:
            Adapter instance wrapping domain_object
        
        Raises:
            ValueError: If no adapter registered for domain type and channel
        """
        domain_type = type(domain_object).__name__
        
        # Fallback for dict/list - use generic JSON adapter
        if domain_type in ('dict', 'list'):
            from agile_bot.src.cli.adapters import GenericAdapter
            return GenericAdapter(domain_object, channel)
        
        key = (domain_type, channel)
        
        if key not in cls._registry:
            raise ValueError(f"No {channel} adapter registered for {domain_type}")
        
        module_path, class_name = cls._registry[key]
        
        # Dynamic import
        import importlib
        module = importlib.import_module(module_path)
        adapter_class = getattr(module, class_name)
        
        return adapter_class(domain_object, **kwargs)
    
    @classmethod
    def register(cls, domain_type: str, channel: str, module_path: str, class_name: str):
        """
        Register new adapter mapping.
        Allows extending factory without modifying core code.
        """
        cls._registry[(domain_type, channel)] = (module_path, class_name)
