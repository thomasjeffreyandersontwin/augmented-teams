from typing import List
from agile_bot.bots.base_bot.src.repl_cli.formatters.output_formatter import OutputFormatter


class REPLStatus:
    def __init__(self, bot, state_provider, formatter: OutputFormatter):
        self.bot = bot
        self.state = state_provider
        self.formatter = formatter
    
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
        # Legend line using formatter markers
        current_marker = self.formatter.status_marker(is_current=True, is_completed=False)
        completed_marker = self.formatter.status_marker(is_current=False, is_completed=True)
        pending_marker = self.formatter.status_marker(is_current=False, is_completed=False)
        output_lines.append(f"{current_marker} current  {completed_marker} done  {pending_marker} not started")
        return output_lines
    
    def _get_scope_display(self) -> List[str]:
        if hasattr(self.state, '_get_scope_display_lines'):
            return self.state._get_scope_display_lines()
        return []
    
    @property
    def hierarchical_status(self) -> str:
        lines = []
        
        if not self.bot or not self.bot.behaviors:
            lines.append("No behaviors available")
            lines.append(self.formatter.subsection_separator())
            return "\n".join(lines)
        
        current_behavior_name = self.state.current_behavior_name
        current_action_name = self.state.current_action_name
        
        stage = self.state.stage_name
        
        # Get domain behaviors (not CLI wrappers)
        domain_bot = self.bot.domain_bot if hasattr(self.bot, 'domain_bot') else self.bot
        for behavior in domain_bot.behaviors:
            b_name = behavior.name
            is_current_behavior = b_name == current_behavior_name
            # Use domain logic - each behavior knows if it's completed
            is_completed_behavior = behavior.is_completed
            
            # Get behavior description if available
            b_desc = getattr(behavior, 'description', '') or ''
            
            # Format behavior marker using formatter
            marker = self.formatter.status_marker(
                is_current=is_current_behavior,
                is_completed=is_completed_behavior
            )
            
            # Show behavior line - only show description for current behavior
            if is_current_behavior and b_desc:
                lines.append(f"{marker} {b_name} - {b_desc}")
            else:
                lines.append(f"{marker} {b_name}")
            
            # Only show actions for current behavior
            if is_current_behavior and behavior.actions:
                for action in behavior.actions:
                    a_name = action.action_name
                    is_current_action = a_name == current_action_name
                    # Use domain logic to determine completion
                    is_completed_action = behavior.actions.is_action_completed(a_name)
                    
                    # Get action description if available
                    a_desc = getattr(action, 'description', '') or ''
                    
                    # Format action marker using formatter
                    a_marker = self.formatter.status_marker(
                        is_current=is_current_action,
                        is_completed=is_completed_action
                    )
                    
                    # Show action line with proper indentation
                    if is_current_action and a_desc:
                        lines.append(f"  {a_marker} {a_name} - {a_desc}")
                    else:
                        lines.append(f"  {a_marker} {a_name}")
                    
                    if is_current_action:
                        instr_params = self._get_instructions_params(action)
                        submit_params = self._get_submit_params(action)
                        common_params = ' --path="..." --scope="..."'
                        
                        # Instructions - use formatter
                        if stage == 'instructions' or stage == 'not_started':
                            instr_marker = self.formatter.status_marker(is_current=True, is_completed=False)
                        else:
                            instr_marker = self.formatter.status_marker(is_current=False, is_completed=True)
                        lines.append(f"    {instr_marker} instructions{instr_params}{common_params} -> Returns instructions for the AI Chat (you) to follow for this action.")
                        
                        # Submit - use formatter
                        if stage == 'submitting':
                            submit_marker = self.formatter.status_marker(is_current=True, is_completed=False)
                        elif stage in ('instructions', 'not_started'):
                            submit_marker = self.formatter.status_marker(is_current=False, is_completed=False)
                        else:
                            submit_marker = self.formatter.status_marker(is_current=False, is_completed=True)
                        lines.append(f"    {submit_marker} submit{submit_params}{common_params} -> Submit data the AI Chat (you) have created as a result of following instructions for this action")
                        
                        # Confirm - use formatter
                        if stage == 'confirming':
                            confirm_marker = self.formatter.status_marker(is_current=True, is_completed=False)
                        elif stage in ('instructions', 'not_started', 'submitting'):
                            confirm_marker = self.formatter.status_marker(is_current=False, is_completed=False)
                        else:
                            confirm_marker = self.formatter.status_marker(is_current=False, is_completed=True)
                        lines.append(f"    {confirm_marker} confirm -> Confirm all operations have been completed for this action. Move on to next action.")
        
        lines.append("")
        lines.append("Run:")
        lines.append("```")
        lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
        lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
        lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
        lines.append("```")
        lines.append(self.formatter.subsection_separator())
        
        # Add quick commands menu
        lines.append("## 💻 **Commands:**")
        lines.append("**status | back | current | next | path [dir] | scope [filter] | help | exit**")
        lines.append("")
        lines.append("```")
        lines.append("// Run")
        lines.append("echo '[command]' | python repl_main.py")
        lines.append("// to invoke commands")
        lines.append("```")
        lines.append("")
        lines.append(self.formatter.section_separator())
        
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
            "  scope [filter]- Show/set/clear scope filter (use COMPLETE paths)",
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
        current_marker = self.formatter.status_marker(is_current=True, is_completed=False)
        pending_marker = self.formatter.status_marker(is_current=False, is_completed=False)
        completed_marker = self.formatter.status_marker(is_current=False, is_completed=True)
        
        if stage == 'instructions':
            return [f"instructions {current_marker}", f"submit {pending_marker}", f"confirm {pending_marker}"]
        elif stage == 'submitted':
            return [f"instructions {completed_marker}", f"submit {current_marker}", f"confirm {pending_marker}"]
        return []
    
    def _format_item(self, name: str, is_current: bool, is_completed: bool, current_marker: str = None) -> str:
        if current_marker is None:
            # Use formatter to generate marker
            marker = self.formatter.status_marker(is_current=is_current, is_completed=is_completed)
        else:
            # Use provided marker (for backward compatibility)
            if is_completed:
                marker = self.formatter.status_marker(is_current=False, is_completed=True)
            elif is_current:
                marker = current_marker
            else:
                marker = self.formatter.status_marker(is_current=False, is_completed=False)
        return f"{name} {marker}"

