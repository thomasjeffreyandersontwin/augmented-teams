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
    
    def _get_scope_display(self) -> List[str]:
        if hasattr(self.state, '_get_scope_display_lines'):
            return self.state._get_scope_display_lines()
        return []
    
    @property
    def hierarchical_status(self) -> str:
        lines = []
        
        # Show scope if set
        scope_lines = self._get_scope_display()
        if scope_lines:
            lines.append("-" * 60)
            lines.extend(scope_lines)
            lines.append("-" * 60)
        else:
            lines.append("-" * 60)
        
        # Add Progress line after scope
        if self.state.has_current_action:
            lines.append(f"Progress: {self.state.progress_path}.{self.state.stage_name}")
        else:
            lines.append("Progress: No active workflow")
        
        if not self.bot or not self.bot.behaviors:
            lines.append("No behaviors available")
            lines.append("-" * 60)
            return "\n".join(lines)
        
        current_behavior_name = self.state.current_behavior_name
        current_action_name = self.state.current_action_name
        completed_behaviors = self.state.completed_behaviors or []
        completed_actions = self.state.completed_action_names or []
        stage = self.state.stage_name
        
        for behavior in self.bot.behaviors:
            b_name = behavior.name
            is_current_behavior = b_name == current_behavior_name
            is_completed_behavior = b_name in completed_behaviors
            
            # Get behavior description if available
            b_desc = getattr(behavior, 'description', '') or ''
            
            # Format behavior marker
            if is_completed_behavior:
                marker = "[x]"
            elif is_current_behavior:
                marker = "[*]"
            else:
                marker = "[ ]"
            
            # Show behavior line - only show description for current behavior
            if is_current_behavior and b_desc:
                lines.append(f"{marker} {b_name} - {b_desc}")
            else:
                lines.append(f"{marker} {b_name}")
            
            # Only show actions for current behavior
            if is_current_behavior and behavior.actions:
                for action in behavior.actions:
                    a_name = action.name
                    is_current_action = a_name == current_action_name
                    is_completed_action = a_name in completed_actions
                    
                    # Get action description if available
                    a_desc = getattr(action, 'description', '') or ''
                    
                    # Format action marker
                    if is_completed_action:
                        a_marker = "[x]"
                    elif is_current_action:
                        a_marker = "[*]"
                    else:
                        a_marker = "[ ]"
                    
                    # Show action line
                    if is_current_action and a_desc:
                        lines.append(f"  {a_marker} {a_name} - {a_desc}")
                    else:
                        lines.append(f"  {a_marker} {a_name}")
                    
                    if is_current_action:
                        instr_params = self._get_instructions_params(action)
                        submit_params = self._get_submit_params(action)
                        common_params = ' --path="..." --scope="..."'
                        
                        # Instructions
                        if stage == 'instructions' or stage == 'not_started':
                            lines.append(f"    [*] instructions{instr_params}{common_params}")
                        else:
                            lines.append(f"    [x] instructions{instr_params}{common_params}")
                        
                        # Submit
                        if stage == 'submitted':
                            lines.append(f"    [*] submit{submit_params}{common_params}")
                        elif stage in ('instructions', 'not_started', 'instructions_given'):
                            lines.append(f"    [ ] submit{submit_params}{common_params}")
                        else:
                            lines.append(f"    [x] submit{submit_params}{common_params}")
                        
                        # Confirm
                        lines.append(f"    [ ] confirm")
        
        lines.append("")
        lines.append("Run:")
        lines.append("echo 'instructions' | python repl_main.py to see instructions for this action.")
        lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
        lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
        lines.append("-" * 60)
        
        # Add quick commands menu
        lines.append("Commands: status | back | current | next | path [dir] | scope [filter] | help | exit")
        lines.append("run echo '[command]' | python repl_main.py to invoke commands")
        lines.append("=" * 90)
        
        return "\n".join(lines)
    
    def _get_instructions_params(self, action) -> str:
        # Check if action has context_class with fields
        if hasattr(action, 'context_class') and action.context_class:
            try:
                import dataclasses
                if dataclasses.is_dataclass(action.context_class):
                    fields = [f.name for f in dataclasses.fields(action.context_class)]
                    if 'context' in fields:
                        return ' --context="..."'
            except:
                pass
        return ''
    
    def _get_submit_params(self, action) -> str:
        params = []
        if hasattr(action, 'context_class') and action.context_class:
            try:
                import dataclasses
                if dataclasses.is_dataclass(action.context_class):
                    fields = [f.name for f in dataclasses.fields(action.context_class)]
                    if 'decisions' in fields:
                        params.append('--decisions="1:option,..."')
                    if 'assumptions_made' in fields or 'assumptions' in fields:
                        params.append('--assumptions="..."')
            except:
                pass
        if params:
            return ' ' + ' '.join(params)
        return ''
    
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
            "  path [dir]    - Show/set working directory",
            "  scope [filter]- Show/set/clear scope filter",
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
            name = action.name
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
            is_completed = action.name in completed
            is_current = action.name == self.state.current_action_name
            parts.append(self._format_item(action.name, is_current, is_completed))
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

