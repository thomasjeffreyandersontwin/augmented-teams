"""
Common guard function for all command runners.

Ensures runners are only called from their Cursor commands with --from-command flag.
"""

import sys


def require_command_invocation(command_name):
    """
    Guard to ensure runner is called from its Cursor command, not directly.
    
    Args:
        command_name: The slash command name (e.g., "bdd-validate", "code-agent-sync")
    
    Provides helpful message if --from-command flag is not present.
    Removes the flag from sys.argv if present.
    """
    if '--from-command' not in sys.argv:
        import io
        
        # Fix encoding for Windows console
        if sys.platform == "win32":
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
            sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
        
        print()
        print("=" * 70)
        print("This runner needs to be called via its associated Cursor command.")
        print("=" * 70)
        print()
        print("Please run the following command instead:")
        print()
        print(f"    /{command_name}")
        print()
        print("Why?")
        print("  - The slash command triggers the full AI-assisted workflow")
        print("  - It ensures proper orchestration and validation")
        print("  - Running the Python file directly bypasses these safeguards")
        print()
        print("=" * 70)
        print()
        sys.exit(1)
    
    # Remove the --from-command flag before processing other args
    sys.argv.remove('--from-command')

