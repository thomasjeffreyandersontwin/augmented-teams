"""
Minimal formatters for display helpers (icons, separators).

NOTE: These are NOT for serialization (adapters handle that).
These are ONLY for display utilities like icons and separators in TTY output.
"""

from .output_formatter import OutputFormatter

__all__ = ['OutputFormatter']
