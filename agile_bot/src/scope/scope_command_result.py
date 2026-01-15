"""
ScopeCommandResult - wraps scope command responses for proper serialization.
"""

from typing import Optional


class ScopeCommandResult:
    """Result of a scope command - includes status, message, and the Scope object."""
    
    def __init__(self, status: str, message: str, scope: 'Scope'):
        """Initialize scope command result.
        
        Args:
            status: Status string (success, error, etc.)
            message: Human-readable message
            scope: The Scope domain object
        """
        self.status = status
        self.message = message
        self.scope = scope
