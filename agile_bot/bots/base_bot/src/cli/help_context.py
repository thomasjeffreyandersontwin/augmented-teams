from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class BehaviorHelpContext:
    bot_name: str
    behavior_name: str
    behavior_description: str
    actions: List[str]
    additional_options: Optional[Dict[str, str]] = None

@dataclass
class ActionHelpContext:
    bot_name: str
    action_name: str
    action_description: str
    parameters: List[str]
    parameter_descriptions: Dict[str, str]








