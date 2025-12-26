import json
import re
from pathlib import Path
from typing import Dict, Any, Optional
from agile_bot.bots.base_bot.src.repl_cli.repl_results import REPLCommandResponse
from agile_bot.bots.base_bot.src.repl_cli.repl_commands.repl_command import InstructionDisplayCommand
from agile_bot.bots.base_bot.src.actions.action_context import ClarifyActionContext, StrategyActionContext, ScopeActionContext


class WorkflowCommand(InstructionDisplayCommand):
    """Base for workflow commands - provides action phase/state properties and workflow operations."""
    
    @property
    def action_phase(self) -> str:
        return self.session.action_phase
    
    @property
    def is_submitted(self) -> bool:
        return self.action_phase == 'submitted'
    
    @property
    def is_instructions_given(self) -> bool:
        return self.action_phase == 'instructions_given'
    
    @property
    def is_not_started(self) -> bool:
        return self.action_phase == 'not_started'
    
    @property
    def can_submit(self) -> bool:
        return self.action_phase in ('not_started', 'instructions_given')
    
    def _parse_clarification_args(self, args: str) -> Dict[str, Any]:
        """Parse clarification arguments from simplified formats: 
        Dot notation (preferred):
        - answers.q1="answer1"
        - evidence.item1="value1"
        - context="item1, item2"
        
        Compact format:
        - answers="q1=answer1, q2=answer2"
        - evidence="item1=value1, item2=value2"
        
        Legacy: key_questions (instead of answers) still supported
        
        Returns dict with 'answers', 'evidence_provided', and 'context' (list) keys.
        """
        answers = {}
        evidence_provided = {}
        context = None
        
        if not args or not args.strip():
            return {'answers': answers, 'evidence_provided': evidence_provided, 'context': context}
        
        # First try compact format: answers="q1=answer1, q2=answer2" or key_questions="q1=answer1, q2=answer2"
        compact_kq_pattern = r'(?:clarify\.)?(answers|key_questions)="([^"]+)"'
        compact_ev_pattern = r'(?:clarify\.)?evidence="([^"]+)"'
        
        kq_match = re.search(compact_kq_pattern, args)
        if kq_match:
            # Parse key=value pairs from compact format
            pairs_str = kq_match.group(2)
            pairs = [p.strip() for p in pairs_str.split(',') if '=' in p]
            for pair in pairs:
                key, value = pair.split('=', 1)
                answers[key.strip()] = value.strip()
        
        ev_match = re.search(compact_ev_pattern, args)
        if ev_match:
            # Parse key=value pairs from compact format
            pairs_str = ev_match.group(1)
            pairs = [p.strip() for p in pairs_str.split(',') if '=' in p]
            for pair in pairs:
                key, value = pair.split('=', 1)
                evidence_provided[key.strip()] = value.strip()
        
        # If no compact format matches, try dot notation
        if not kq_match and not ev_match:
            # Accept both "answers" and "key_questions" for backwards compatibility
            quoted_pattern = r'(?:clarify\.)?(answers|key_questions|evidence)\.([^=]+)="([^"]*)"'
            unquoted_pattern = r'(?:clarify\.)?(answers|key_questions|evidence)\.([^=]+)=([^\s]+)'
            
            matches = list(re.finditer(quoted_pattern, args))
            if not matches:
                matches = list(re.finditer(unquoted_pattern, args))
            
            for match in matches:
                category = match.group(1)
                key = match.group(2).strip()
                value = match.group(3).strip()
                
                if category in ('answers', 'key_questions'):
                    answers[key] = value
                elif category == 'evidence':
                    evidence_provided[key] = value
        
        # Parse context separately
        context_quoted_pattern = r'(?:clarify\.)?context="(.+?)"\s*$|(?:clarify\.)?context="(.+)'
        context_match = re.search(context_quoted_pattern, args)
        if context_match:
            context_str = context_match.group(1) if context_match.group(1) else context_match.group(2)
            context_str = context_str.rstrip('"').strip()
            context = [item.strip() for item in context_str.split(',') if item.strip()]
        
        return {'answers': answers, 'evidence_provided': evidence_provided, 'context': context}
    
    def _parse_strategy_args(self, args: str) -> Dict[str, Any]:
        """Parse strategy arguments from simplified format:
        - decision1="option1" decision2="option2"
        - assumptions="assumption1, assumption2"
        
        Returns dict with 'choices' (dict) and 'assumptions' (list) keys.
        """
        choices = {}
        assumptions = None
        
        if not args or not args.strip():
            return {'choices': choices, 'assumptions': assumptions}
        
        # Parse assumptions first (known keyword)
        assumptions_pattern = r'(?:strategy\.)?assumptions="(.+?)"\s*$|(?:strategy\.)?assumptions="(.+)'
        assumptions_match = re.search(assumptions_pattern, args)
        if assumptions_match:
            assumptions_str = assumptions_match.group(1) if assumptions_match.group(1) else assumptions_match.group(2)
            assumptions_str = assumptions_str.rstrip('"').strip()
            assumptions = [item.strip() for item in assumptions_str.split(',') if item.strip()]
        
        # Parse all remaining key="value" pairs as decisions
        # Match any word followed by ="value"
        decision_pattern = r'(\w+)="([^"]*)"'
        decision_matches = list(re.finditer(decision_pattern, args))
        for match in decision_matches:
            key = match.group(1).strip()
            value = match.group(2).strip()
            # Skip 'assumptions' keyword (already parsed)
            if key.lower() not in ('assumptions', 'strategy'):
                choices[key] = value
        
        return {'choices': choices, 'assumptions': assumptions}
    
    def _parse_scope_args(self, args: str, action_name: str) -> Dict[str, Any]:
        """Parse scope arguments from simplified format:
        - scope="story1, story2" (searches entire graph)
        - scope="file:path1, path2"
        
        Also supports legacy format with action prefix (build.scope="...")
        Returns dict with 'scope' (Scope object) key or empty dict if no scope found.
        """
        from agile_bot.bots.base_bot.src.actions.action_context import Scope, ScopeType
        
        if not args or not args.strip():
            return {}
        
        # Pattern for scope: scope="value" (action prefix optional)
        scope_pattern = rf'(?:{action_name}\.)?scope="([^"]+)"'
        
        # Parse scope
        scope_match = re.search(scope_pattern, args)
        if scope_match:
            scope_value_full = scope_match.group(1).strip()
            
            # Check if it's files scope (only special type)
            if ':' in scope_value_full and scope_value_full.split(':', 1)[0].strip().lower() == 'files':
                parts = scope_value_full.split(':', 1)
                scope_value_str = parts[1].strip()
                scope_values_raw = [v.strip() for v in scope_value_str.split(',') if v.strip()]
                scope_type = ScopeType.FILES
                scope_value = scope_values_raw
            else:
                # No prefix or not files - search entire graph with these terms
                scope_type = ScopeType.STORY
                scope_values_raw = [v.strip() for v in scope_value_full.split(',') if v.strip()]
                scope_value = scope_values_raw
            
            return {'scope': Scope(type=scope_type, value=scope_value)}
        
        return {}
    
    def execute_submit(self, args: str = "") -> REPLCommandResponse:
        """Execute the current action's submit() method. SINGLE SOURCE OF TRUTH."""
        action = self.current_action
        if not action:
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
        
        try:
            # Parse arguments if provided and action uses ClarifyActionContext, StrategyActionContext, or ScopeActionContext
            context = action.context_class()
            if args and isinstance(context, ClarifyActionContext):
                parsed = self._parse_clarification_args(args)
                # Set the parsed values if we found any
                if parsed['answers']:
                    context.answers = parsed['answers']
                if parsed['evidence_provided']:
                    context.evidence_provided = parsed['evidence_provided']
                if parsed['context']:
                    context.context = parsed['context']
            elif args and isinstance(context, StrategyActionContext):
                parsed = self._parse_strategy_args(args)
                # Set decisions as direct attributes on context
                if parsed['choices']:
                    for key, value in parsed['choices'].items():
                        setattr(context, key, value)
                if parsed['assumptions']:
                    context.assumptions = parsed['assumptions']
            elif args and isinstance(context, ScopeActionContext):
                parsed = self._parse_scope_args(args, action.action_name)
                # Set the parsed scope if we found one
                if 'scope' in parsed:
                    context.scope = parsed['scope']
            
            # Call the real action.submit() method
            result = action.submit(context)
            
            # Format output
            status = result.get('status', 'unknown')
            message = result.get('message', 'Work submitted')
            saved_path = result.get('saved_path')
            questions_count = result.get('questions_answered', 0)
            evidence_count = result.get('evidence_count', 0)
            
            output_lines = [
                f"Executing: {self.current_behavior_name}.{self.current_action_name}.submit",
                "",
                f"[{status.upper()}]",
                f"- {message}",
            ]
            
            # Add detailed information if available
            if questions_count > 0:
                output_lines.append("")
                output_lines.append(f"**Questions & Answers saved:** {questions_count}")
                answers = result.get('answers', {})
                if answers:
                    for q_key, answer in list(answers.items())[:5]:  # Show first 5
                        output_lines.append(f"  - {q_key}: {answer[:60]}{'...' if len(str(answer)) > 60 else ''}")
                    if len(answers) > 5:
                        output_lines.append(f"  ... and {len(answers) - 5} more")
            
            if evidence_count > 0:
                output_lines.append("")
                output_lines.append(f"**Evidence saved:** {evidence_count}")
                evidence = result.get('evidence_provided', {})
                if evidence:
                    for e_key, e_value in list(evidence.items())[:5]:  # Show first 5
                        output_lines.append(f"  - {e_key}: {str(e_value)[:60]}{'...' if len(str(e_value)) > 60 else ''}")
                    if len(evidence) > 5:
                        output_lines.append(f"  ... and {len(evidence) - 5} more")
            
            # Display context if provided (as list)
            saved_context = result.get('context')
            if saved_context:
                output_lines.append("")
                if isinstance(saved_context, list):
                    output_lines.append(f"**Context saved:** {len(saved_context)} item(s)")
                    for idx, item in enumerate(saved_context[:5], 1):  # Show first 5
                        item_preview = item[:60] + ('...' if len(item) > 60 else '')
                        output_lines.append(f"  {idx}. {item_preview}")
                    if len(saved_context) > 5:
                        output_lines.append(f"  ... and {len(saved_context) - 5} more")
                else:
                    # Fallback for string context
                    output_lines.append("**Context saved:**")
                    context_preview = saved_context[:100] + ('...' if len(saved_context) > 100 else '')
                    output_lines.append(f"  {context_preview}")
            
            # Display strategy decisions if provided
            choices = result.get('choices', {})
            if choices:
                output_lines.append("")
                output_lines.append(f"**Strategy Decisions saved:** {len(choices)}")
                for decision_key, decision_value in list(choices.items())[:5]:  # Show first 5
                    output_lines.append(f"  - {decision_key}: {decision_value}")
                if len(choices) > 5:
                    output_lines.append(f"  ... and {len(choices) - 5} more")
            
            # Display assumptions if provided (as list)
            assumptions = result.get('assumptions')
            if assumptions and isinstance(assumptions, list):
                output_lines.append("")
                output_lines.append(f"**Assumptions saved:** {len(assumptions)} item(s)")
                for idx, assumption in enumerate(assumptions[:5], 1):  # Show first 5
                    assumption_preview = assumption[:60] + ('...' if len(assumption) > 60 else '')
                    output_lines.append(f"  {idx}. {assumption_preview}")
                if len(assumptions) > 5:
                    output_lines.append(f"  ... and {len(assumptions) - 5} more")
            
            output_lines.extend([
                "",
                "Run: echo 'confirm' | python repl_main.py to confirm context saved and advance to next."
            ])
            
            output = "\n".join(output_lines)
            
            return REPLCommandResponse(
                output=output,
                response=output,
                status="success",
                action=self.current_action_name
            )
        except Exception as e:
            error_msg = f"ERROR executing {self.current_action_name}.submit(): {str(e)}"
            return REPLCommandResponse(
                output=error_msg,
                response=error_msg,
                status="error",
                action=self.current_action_name
            )
    
    def execute_confirm(self) -> REPLCommandResponse:
        """Execute the current action's confirm() method and advance. SINGLE SOURCE OF TRUTH."""
        action = self.current_action
        behavior = self.current_behavior
        if not behavior or not action:
            return self.error_no_current_behavior()
        
        current_behavior_name = behavior.name
        current_action_name = action.action_name
        
        try:
            # Call the real action.confirm() method
            context = action.context_class()
            result = action.confirm(context)
            
            # Check if at last action BEFORE closing
            is_last_action = behavior.actions.next() is None
            
            # Mark current action as complete and advance
            behavior.actions.close_current()
            
            # If not at last action, advance to next action and show navigation
            if not is_last_action:
                return self.display_navigation()
            
            # At last action - behavior is complete
            # Mark behavior as complete in state file
            self._mark_behavior_complete(current_behavior_name)
            
            # Check for next behavior BEFORE close_current since it advances the index
            next_behavior = self.bot.behaviors.next()
            
            if next_behavior:
                # Advance to next behavior
                self.bot.behaviors.close_current()
                # Navigate to next behavior's first action
                if next_behavior.actions.names:
                    self.navigate_to_behavior_action(next_behavior.name, next_behavior.actions.names[0])
                    return self.display_navigation()
            
            # No more behaviors - all complete
            return REPLCommandResponse(
                output=f"COMPLETE: {current_behavior_name} behavior finished\n\nALL BEHAVIORS COMPLETE!",
                response="COMPLETE: All behaviors finished",
                status="success"
            )
        except Exception as e:
            error_msg = f"ERROR executing {current_action_name}.confirm(): {str(e)}"
            return REPLCommandResponse(
                output=error_msg,
                response=error_msg,
                status="error",
                action=current_action_name
            )
    
    def _mark_behavior_complete(self, behavior_name: str) -> None:
        """Add behavior to completed_behaviors in state file."""
        state_file = self.session.workspace_directory / 'behavior_action_state.json'
        if not state_file.exists():
            return
        try:
            state_data = json.loads(state_file.read_text())
            completed = state_data.get('completed_behaviors', [])
            if behavior_name not in completed:
                completed.append(behavior_name)
            state_data['completed_behaviors'] = completed
            state_file.write_text(json.dumps(state_data, indent=2))
        except (json.JSONDecodeError, IOError):
            pass


class InstructionsCommand(WorkflowCommand):
    @property
    def name(self) -> str:
        return "instructions"
    
    @property
    def takes_args(self) -> bool:
        return True
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        if not self.has_current_action:
            return self.error_no_current_action("get instructions for")
        
        action = self.current_action
        context = None
        
        # Parse arguments if provided and action uses ScopeActionContext
        if args:
            action_context = action.context_class()
            if isinstance(action_context, ScopeActionContext):
                parsed = self._parse_scope_args(args, action.action_name)
                # Set the parsed scope if we found one
                if 'scope' in parsed:
                    action_context.scope = parsed['scope']
                    context = action_context
        
        # Display instructions with optional context
        return self.display_instructions(action=action, context=context)


class SubmitCommand(WorkflowCommand):
    @property
    def name(self) -> str:
        return "submit"
    
    @property
    def takes_args(self) -> bool:
        return True
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        if not self.has_current_action:
            return self.error_no_current_action("submit for")
        return self.execute_submit(args)


class ConfirmCommand(WorkflowCommand):
    @property
    def name(self) -> str:
        return "confirm"
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        if not self.has_current_action:
            return self.error_no_current_action("confirm")
        return self.execute_confirm()

