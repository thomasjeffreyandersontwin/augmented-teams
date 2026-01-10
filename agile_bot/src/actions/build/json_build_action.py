"""
JSON adapter for BuildKnowledgeAction.
"""

import json
from agile_bot.src.cli.adapters import JSONAdapter
from agile_bot.src.actions.build.build_action import BuildKnowledgeAction


class JSONBuildAction(JSONAdapter):
    """Serializes BuildKnowledgeAction to JSON - exposes all BuildKnowledgeAction properties."""
    
    def __init__(self, action: BuildKnowledgeAction, is_current: bool = False, is_completed: bool = False):
        self.action = action
        self.is_current = is_current
        self.is_completed = is_completed
    
    # Expose ALL domain properties
    @property
    def action_name(self):
        return self.action.action_name
    
    @property
    def description(self):
        return self.action.description
    
    @property
    def order(self):
        return self.action.order
    
    @property
    def next_action(self):
        return self.action.next_action
    
    @property
    def workflow(self):
        return self.action.workflow
    
    @property
    def auto_confirm(self):
        return self.action.auto_confirm
    
    @property
    def skip_confirm(self):
        return self.action.skip_confirm
    
    @property
    def behavior(self):
        return self.action.behavior
    
    @property
    def knowledge(self):
        """Build-specific property."""
        return self.action.knowledge
    
    @property
    def knowledge_graph_spec(self):
        """Build-specific property."""
        return self.action.knowledge_graph_spec
    
    @property
    def knowledge_graph_template(self):
        """Build-specific property."""
        return self.action.knowledge_graph_template
    
    def to_dict(self) -> dict:
        """Convert BuildKnowledgeAction to dict."""
        result = {
            'action_name': self.action.action_name,
            'description': self.action.description,
            'order': self.action.order,
            'next_action': self.action.next_action,
            'workflow': self.action.workflow,
            'auto_confirm': self.action.auto_confirm,
            'skip_confirm': self.action.skip_confirm,
            'behavior': self.action.behavior.name if self.action.behavior else None,
        }
        
        # Add build-specific properties
        if self.action.knowledge:
            result['knowledge'] = {
                'has_spec': self.action.knowledge_graph_spec is not None,
                'has_template': self.action.knowledge_graph_template is not None
            }
            
            if self.action.knowledge_graph_spec:
                result['knowledge_graph_spec'] = {
                    'path': str(self.action.knowledge_graph_spec.config_path),
                    'output': self.action.knowledge_graph_spec.config_data.get('output', 'story-graph.json')
                }
            
            if self.action.knowledge_graph_template:
                result['knowledge_graph_template'] = {
                    'path': str(self.action.knowledge_graph_template.template_path)
                }
        
        return result
    
    def deserialize(self, data: str) -> dict:
        """Parse JSON string to dict."""
        return json.loads(data)
