from abc import ABC, abstractmethod
from agile_bot.bots.base_bot.src.repl_cli.repl_results import REPLCommandResponse


class REPLCommand(ABC):
    """Base class for all REPL commands."""
    
    def __init__(self, session):
        self.session = session
        self.bot = session.bot
    
    @property
    @abstractmethod
    def name(self) -> str:
        pass
    
    @property
    def takes_args(self) -> bool:
        return False
    
    @abstractmethod
    def execute(self, args: str = "") -> REPLCommandResponse:
        pass
    
    @property
    def current_behavior(self):
        return self.session.current_behavior
    
    @property
    def current_action(self):
        return self.session.current_action
    
    @property
    def has_current_behavior(self) -> bool:
        return self.session.has_current_behavior
    
    @property
    def has_current_action(self) -> bool:
        return self.session.has_current_action
    
    @property
    def current_behavior_name(self):
        return self.session.current_behavior_name
    
    @property
    def current_action_name(self):
        return self.session.current_action_name
    
    def error_no_current_action(self, context: str = "") -> REPLCommandResponse:
        msg = f"ERROR: No current action{' to ' + context if context else ''}"
        return REPLCommandResponse(output=msg, response="ERROR: No current action", status="error")
    
    def error_no_current_behavior(self) -> REPLCommandResponse:
        return REPLCommandResponse(
            output="ERROR: No current behavior set. Please select a behavior first.",
            response="ERROR: No current behavior set",
            status="error"
        )
    
    def error_behavior_not_found(self, behavior_name: str) -> REPLCommandResponse:
        available = ", ".join(self.bot.behaviors.names)
        output = f"ERROR: behavior '{behavior_name}' not found\nAvailable behaviors: {available}"
        return REPLCommandResponse(output=output, response=f"ERROR: behavior '{behavior_name}' not found", status="error")
    
    def error_action_not_found(self, action_name: str) -> REPLCommandResponse:
        behavior = self.current_behavior
        available = ", ".join(behavior.actions.names) if behavior else ""
        output = f"ERROR: action '{action_name}' not found\nAvailable actions: {available}"
        return REPLCommandResponse(output=output, response=f"ERROR: action '{action_name}' not found", status="error")


class InstructionDisplayCommand(REPLCommand):
    """Base class for all commands that display action instructions.
    
    This is the SINGLE SOURCE OF TRUTH for formatting instruction output.
    ALL commands that display instructions MUST inherit from this class.
    
    Template method pattern: _wrap_with_context_header enforces header at bottom.
    """
    
    def _wrap_with_context_header(self, content: str, response_msg: str) -> REPLCommandResponse:
        """
        Template method: Wraps content with context header at the bottom.
        
        This enforces consistent structure - header is ALWAYS at the bottom.
        """
        header = self.session.get_context_header_for_ai()
        
        output = "\n".join([
            content,
            "",
            header
        ])
        
        return REPLCommandResponse(
            output=output,
            response=response_msg,
            status="success"
        )
    
    def _get_submit_message(self, action) -> str:
        """Generate dynamic submit message based on action's context parameters."""
        # Get the action's context class
        context_class = action.context_class
        
        # Get field names from the context class (excluding common base fields)
        if hasattr(context_class, '__dataclass_fields__'):
            fields = context_class.__dataclass_fields__
            # Filter out common base fields (scope is from ScopeActionContext, message is from RulesActionContext)
            common_fields = {'scope', 'message', 'background', 'skip_cross_file', 'all_files', 'force_full'}
            param_fields = [name for name in fields.keys() if name not in common_fields]
            
            if param_fields:
                # Build action-specific parameter examples
                param_examples = []
                for field in param_fields:
                    # Get field type annotation for better examples
                    field_obj = fields[field]
                    
                    # Provide generic examples based on field type
                    if field == 'answers':
                        action_name = self.current_action_name if self.has_current_action else 'action'
                        param_examples.append(f'{action_name}.key_questions.q1="answer 1" {action_name}.key_questions.q2="answer 2"')
                    elif field == 'evidence_provided':
                        action_name = self.current_action_name if self.has_current_action else 'action'
                        param_examples.append(f'{action_name}.evidence.e1="description or file path" {action_name}.evidence.e2="description"')
                    elif field == 'context':
                        action_name = self.current_action_name if self.has_current_action else 'action'
                        param_examples.append(f'{action_name}.context="original chat, file references, etc."')
                    elif field == 'assumptions':
                        param_examples.append('decision1="option1" decision2="option2" assumptions="assumption1, assumption2"')
                    elif 'Dict' in str(field_obj.type):
                        # Generic dict fields
                        param_examples.append(f'--{field}=\'{{"key_1": "value 1", "key_2": "value 2"}}\'')
                    elif 'List' in str(field_obj.type):
                        # Generic list fields
                        param_examples.append(f'--{field}=\'["item 1", "item 2"]\'')
                    else:
                        # Other fields - generic placeholder
                        param_examples.append(f'--{field}="value"')
                
                params_str = ' '.join(param_examples)
                return f"Run: echo 'submit {params_str}' | python repl_main.py when ready to submit your work."
        
        return "Run: echo 'submit' | python repl_main.py when ready to submit your work."
    
    def navigate_to_behavior_action(self, behavior_name: str, action_name: str) -> None:
        """
        Navigate to a specific behavior and action. SINGLE SOURCE OF TRUTH.
        
        This consolidates the repeated pattern of navigating to behavior then action.
        """
        self.bot.behaviors.navigate_to(behavior_name)
        behavior = self.bot.behaviors.current
        if behavior:
            behavior.actions.navigate_to(action_name)
    
    def display_navigation(self) -> REPLCommandResponse:
        """
        Display navigation result (moving to a behavior/action).
        
        Shows: location + prompt to run echo 'instructions' | python repl_main.py to see instructions, then header at bottom (via template method)
        """
        if not self.has_current_action:
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
        
        location = f"{self.current_behavior_name}.{self.current_action_name}"
        
        content = "\n".join([
            f"Now at: {location}",
            "",
            "Run: echo 'instructions' | python repl_main.py to see instructions for this action."
        ])
        
        return self._wrap_with_context_header(content, f"Moved to {location}")
    
    def display_instructions(self, action=None, context=None, operation="instructions") -> REPLCommandResponse:
        """
        THE ONLY METHOD that formats and displays action instructions.
        
        All instruction display paths (next, back, current, action, behavior, dot notation, etc.)
        MUST call this method to ensure consistency.
        """
        # Use current action if none specified
        if action is None:
            action = self.current_action
        
        if not action:
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
        
        try:
            # Call the action's get_instructions() - it formats everything
            if context is None:
                context = action.context_class()
            
            result = action.get_instructions(context)
            formatted_output = result.get('formatted_output', '')
            
            # Format execution line
            if operation == "instructions":
                exec_line = f"EXECUTING {self.current_behavior_name}.{action.action_name}.instructions"
            else:
                exec_line = f"EXECUTING {self.current_behavior_name}.{action.action_name}"
            
            # Build content (just instructions, no submit message yet)
            content = "\n".join([
                "=================================",
                exec_line,
                "",
                formatted_output
            ])
            
            # Wrap with context header
            response = self._wrap_with_context_header(content, content)
            
            response.action = action.action_name
            response.context_passed_to_action = context
            return response
        except Exception as e:
            error_msg = f"ERROR executing {action.action_name}.get_instructions(): {str(e)}"
            return REPLCommandResponse(
                output=error_msg,
                response=error_msg,
                status="error",
                action=action.action_name
            )

