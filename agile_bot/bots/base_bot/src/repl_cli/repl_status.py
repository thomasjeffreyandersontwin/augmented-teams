from typing import List


class REPLStatus:
    STAGE_MAP = {
        'not_started': 'instructions',
        'instructions_given': 'instructions',
        'submitted': 'submitted'
    }
    
    def __init__(self, bot, state_provider):
        self.bot = bot
        self.state = state_provider
    
    @property
    def behavior_names(self) -> List[str]:
        if not self.bot or not self.bot.behaviors:
            return []
        return [b.name for b in self.bot.behaviors]
    
    @property
    def full_status(self) -> List[str]:
        output_lines = [f"Progress: {self.state.progress_path}.{self.state.stage_name}"]
        
        if not self.bot or not self.bot.behaviors:
            return output_lines
        
        output_lines.append("Behaviors: " + " -> ".join(self._behavior_status_items))
        
        if not self.state.current_behavior:
            return output_lines
        
        output_lines.append("  Actions: " + " -> ".join(self._action_status_items))
        
        if self.state.current_action_name and self._operation_status_items:
            output_lines.append("    Operations: " + " -> ".join(self._operation_status_items))
        
        output_lines.append("")
        output_lines.append("[*] current  [OK] done  [ ] not started")
        return output_lines
    
    @property
    def compact_status(self) -> List[str]:
        output_lines = [""]
        
        if self.bot and self.bot.behaviors:
            output_lines.append("Behaviors: " + " | ".join(self.behavior_names))
        
        output_lines.extend([
            "Actions: clarify | strategy | build | validate | render",
            "",
            "  status        - Show workflow progress",
            "  back          - Return to previous action",
            "  current       - Re-execute current operation",
            "  next          - Advance to next action",
            "  help          - Show detailed help",
            "  exit          - Exit CLI"
        ])
        return output_lines
    
    @property
    def breadcrumbs(self) -> str:
        behavior = self.state.current_behavior
        if not behavior:
            return ""
        
        completed = self.state.completed_action_names
        parts = []
        for action in behavior.actions:
            name = action.action_name
            is_completed = name in completed
            is_current = name == self.state.current_action_name
            parts.append(self._format_item(name, is_current, is_completed, current_marker="*"))
        
        return " -> ".join(parts)
    
    @property
    def _behavior_status_items(self) -> List[str]:
        parts = []
        for behavior in self.bot.behaviors:
            is_completed = behavior.name in self.state.completed_behaviors
            is_current = behavior.name == self.state.current_behavior_name
            parts.append(self._format_item(behavior.name, is_current, is_completed))
        return parts
    
    @property
    def _action_status_items(self) -> List[str]:
        parts = []
        completed = self.state.completed_action_names
        for action in self.state.current_behavior.actions:
            is_completed = action.action_name in completed
            is_current = action.action_name == self.state.current_action_name
            parts.append(self._format_item(action.action_name, is_current, is_completed))
        return parts
    
    @property
    def _operation_status_items(self) -> List[str]:
        stage = self.state.stage_name
        if stage == 'instructions':
            return ["instructions [*]", "submit [ ]", "confirm [ ]"]
        elif stage == 'submitted':
            return ["instructions [OK]", "submit [*]", "confirm [ ]"]
        return []
    
    def _format_item(self, name: str, is_current: bool, is_completed: bool, current_marker: str = "[*]") -> str:
        if is_completed:
            return f"{name} [OK]"
        elif is_current:
            return f"{name} {current_marker}"
        return f"{name} [ ]"

