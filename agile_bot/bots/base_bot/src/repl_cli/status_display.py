from __future__ import annotations
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from agile_bot.bots.base_bot.src.repl_cli.cli_bot.cli_bot import CLIBot
    from agile_bot.bots.base_bot.src.repl_cli.cli_bot.cli_behavior import CLIBehavior
    from agile_bot.bots.base_bot.src.repl_cli.cli_bot.cli_actions.cli_action import CLIAction


class StatusDisplay:
    
    def __init__(self, cli_bot: CLIBot):
        self.cli_bot = cli_bot
        self.header = HeaderDisplay()
        self.hierarchy = HierarchyTreeDisplay()
        self.footer = FooterDisplay()
    
    def render(self) -> str:
        header_text = self.header.render(self.cli_bot)
        hierarchy_text = self.hierarchy.render(self.cli_bot)
        footer_text = self.footer.render()
        
        return f"{header_text}\n\n{hierarchy_text}\n\n{footer_text}"


class HeaderDisplay:
    
    def render(self, cli_bot: CLIBot) -> str:
        bot_name = cli_bot.name.upper().replace('_', ' ')
        workspace_path = cli_bot.path
        
        header = f"{bot_name} CLI"
        header += f"\nBot Path: {cli_bot.bot_directory}"
        header += f"\nWorking Area: {workspace_path}"
        
        return header


class HierarchyTreeDisplay:
    
    def render(self, cli_bot: CLIBot) -> str:
        lines = []
        
        current_behavior = cli_bot.behaviors.current
        behaviors = cli_bot.behaviors.all
        
        for behavior_name in behaviors:
            behavior = cli_bot.behaviors.get_behavior(behavior_name)
            if behavior is None:
                continue
            
            is_current = current_behavior and behavior.name == current_behavior.name
            status_icon = "[*]" if is_current else "[ ]"
            
            lines.append(f"{status_icon} {behavior.name}")
            
            if is_current and behavior.actions:
                current_action = behavior.actions.current
                actions = behavior.actions.all
                
                for action_name in actions:
                    action = behavior.actions.get_action(action_name)
                    if action is None:
                        continue
                    
                    is_current_action = current_action and action.name == current_action.name
                    action_icon = "    [*]" if is_current_action else "    [ ]"
                    lines.append(f"{action_icon} {action.name}")
        
        return "\n".join(lines) if lines else "No behaviors loaded"


class FooterDisplay:
    
    def render(self) -> str:
        commands = [
            "status",
            "back",
            "next",
            "help",
            "exit"
        ]
        return f"Commands: {' | '.join(commands)}"


class BreadcrumbVisitor:
    
    def __init__(self):
        self.breadcrumbs = []
    
    def visit_behavior(self, behavior: CLIBehavior) -> None:
        self.breadcrumbs.append(behavior.name)
    
    def visit_action(self, action: CLIAction) -> None:
        self.breadcrumbs.append(action.name)
    
    def get_output(self) -> str:
        return " > ".join(self.breadcrumbs)
    
    def reset(self) -> None:
        self.breadcrumbs = []

