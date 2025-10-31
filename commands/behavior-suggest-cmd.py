def behavior_suggest(feature=None):
    """
    When doing repetitive tasks, suggest creating new behaviors to capture patterns.
    
    Analyzes patterns in current session and suggests new behaviors that could:
    - Be added to an existing behavior-feature
    - Create a new behavior-feature
    - Be added to the feature currently being worked on
    
    This is primarily an AI-driven function that analyzes conversation and code patterns.
    """
    from pathlib import Path
    import io
    import sys
    
    print("💡 Behavior Suggestion")
    print("="*60)
    print("\nThis command helps identify repetitive patterns and suggests creating new behaviors.")
    print("\nThe AI assistant should:")
    print("1. Analyze the current conversation for repetitive patterns")
    print("2. Identify common tasks, code structures, or operations")
    print("3. Suggest creating a new behavior with context")
    print("4. Ask for user confirmation and placement decision")
    print("5. Use \\behavior-structure create to scaffold after confirmation")
    print("\n💡 Tip: The AI should proactively suggest behaviors when detecting repetition,")
    print("   using natural language like: 'Hi, we're doing this a lot. Let's make a new behavior.'")
    print("\nSuggested behavior placement options:")
    print("  • Existing behavior-feature (e.g., add to cursor-behavior)")
    print("  • New behavior-feature (create entirely new feature)")
    print("  • Current feature (add to feature being worked on)")
    
    return {
        "status": "info",
        "message": "Behavior suggestion is primarily AI-driven. Use during conversation to detect patterns."
    }


if __name__ == "__main__":
    import sys
    
    # Fix Windows console encoding for emoji support
    if sys.platform == "win32":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    
    feature = sys.argv[1] if len(sys.argv) > 1 else None
    behavior_suggest(feature)
