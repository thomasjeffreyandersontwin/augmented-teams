"""
Gather Context Action

Handles gather_context action including:
- Loading and merging instructions from base and behavior-specific locations
- Injecting guardrails (questions and evidence)
- Managing rendered content
"""
from pathlib import Path
from typing import Dict, Any
import json
from agile_bot.bots.base_bot.src.utils import read_json_file, find_behavior_folder
from agile_bot.bots.base_bot.src.actions.activity_tracker import ActivityTracker


class GatherContextAction:
    """Gather Context action implementation."""
    
    def __init__(self, bot_name: str, behavior: str, workspace_root: Path):
        self.bot_name = bot_name
        self.behavior = behavior
        self.workspace_root = Path(workspace_root)
        self.tracker = ActivityTracker(workspace_root)
    
    def load_and_merge_instructions(self) -> Dict[str, Any]:
        """Load and merge instructions from base and behavior-specific locations.
        
        Returns:
            Merged instructions dictionary
            
        Raises:
            FileNotFoundError: If base instructions not found
        """
        # Load base instructions - check for numbered prefix folders
        base_actions_dir = self.workspace_root / 'agile_bot' / 'bots' / 'base_bot' / 'base_actions'
        
        # Try with and without number prefix - prefer numbered folders
        base_path = None
        matching_folders = sorted(base_actions_dir.glob('*gather_context'))
        # Prioritize folders that start with a digit
        for folder in matching_folders:
            if folder.name[0].isdigit():
                instructions_file = folder / 'instructions.json'
                if instructions_file.exists():
                    base_path = instructions_file
                    break
        
        # Fall back to non-numbered folder if no numbered folder found
        if not base_path:
            for folder in matching_folders:
                instructions_file = folder / 'instructions.json'
                if instructions_file.exists():
                    base_path = instructions_file
                    break
        
        if not base_path:
            base_path = base_actions_dir / 'gather_context' / 'instructions.json'
        
        if not base_path.exists():
            raise FileNotFoundError(
                f'Base instructions not found for action gather_context at {base_path}'
            )
        
        base_instructions = read_json_file(base_path)
        
        # Load behavior-specific instructions (optional)
        behavior_path = None
        try:
            behavior_folder = find_behavior_folder(
                self.workspace_root,
                self.bot_name,
                self.behavior
            )
            behavior_path = behavior_folder / 'gather_context' / 'instructions.json'
        except FileNotFoundError:
            pass
        
        behavior_instructions = None
        if behavior_path and behavior_path.exists():
            behavior_instructions = read_json_file(behavior_path)
        
        # Merge instructions
        merged = {
            'action': 'gather_context',
            'behavior': self.behavior,
            'base_instructions': base_instructions.get('instructions', []),
        }
        
        if behavior_instructions:
            merged['behavior_instructions'] = behavior_instructions.get('instructions', [])
        
        return merged
    
    def inject_questions_and_evidence(self) -> Dict[str, Any]:
        """Inject guardrails (questions and evidence) into instructions.
        
        Returns:
            Instructions with guardrails injected
            
        Raises:
            json.JSONDecodeError: If guardrails JSON is malformed
        """
        # Find behavior folder (handles numbered prefixes)
        try:
            behavior_folder = find_behavior_folder(
                self.workspace_root,
                self.bot_name,
                self.behavior
            )
            guardrails_dir = behavior_folder / 'guardrails' / 'required_context'
        except FileNotFoundError:
            guardrails_dir = None
        
        instructions = {'guardrails': {}}
        
        if not guardrails_dir:
            return instructions
        
        # Load questions
        questions_file = guardrails_dir / 'key_questions.json'
        if questions_file.exists():
            questions_data = read_json_file(questions_file)
            instructions['guardrails']['key_questions'] = questions_data.get('questions', [])
        
        # Load evidence
        evidence_file = guardrails_dir / 'evidence.json'
        if evidence_file.exists():
            evidence_data = read_json_file(evidence_file)
            instructions['guardrails']['evidence'] = evidence_data.get('evidence', [])
        
        return instructions
    
    def inject_gather_context_instructions(self) -> Dict[str, Any]:
        """Inject instructions to load rendered content.
        
        Returns:
            Instructions with rendered content paths
        """
        rendered_dir = (
            self.workspace_root /
            'agile_bot' / 'bots' / self.bot_name / 'docs' / 'stories'
        )
        
        rendered_paths = []
        if rendered_dir.exists():
            # Look for acceptance criteria files
            for file_path in rendered_dir.rglob('acceptance-criteria.md'):
                rendered_paths.append(str(file_path))
        
        return {
            'rendered_content_paths': rendered_paths
        }
    
    def track_activity_on_start(self):
        """Track activity when action starts."""
        self.tracker.track_start(self.bot_name, self.behavior, 'gather_context')
    
    def track_activity_on_completion(self, outputs: dict = None, duration: int = None):
        """Track activity when action completes."""
        self.tracker.track_completion(self.bot_name, self.behavior, 'gather_context', outputs, duration)
    
    def save_state_on_completion(self):
        """Save workflow state on completion."""
        state_file = self.workspace_root / 'project_area' / 'workflow_state.json'
        state_file.parent.mkdir(parents=True, exist_ok=True)
        state = json.loads(state_file.read_text(encoding='utf-8')) if state_file.exists() else {}
        
        if 'completed_actions' not in state:
            state['completed_actions'] = []
        
        state['completed_actions'].append({
            'action_state': f'{self.bot_name}.{self.behavior}.gather_context',
            'timestamp': '2025-12-04T10:00:00Z'
        })
        
        state_file.write_text(json.dumps(state), encoding='utf-8')
    
    def finalize_and_transition(self):
        """Finalize action and return next action."""
        class TransitionResult:
            next_action = 'decide_planning_criteria'
        return TransitionResult()


