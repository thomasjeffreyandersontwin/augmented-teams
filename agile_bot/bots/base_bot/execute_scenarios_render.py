#!/usr/bin/env python3
"""Execute scenarios.render.instructions operation directly."""
import sys
from pathlib import Path

# Add workspace to path
workspace_root = Path(__file__).parent
if str(workspace_root) not in sys.path:
    sys.path.insert(0, str(workspace_root))

from src.repl_cli.headless.headless_session import HeadlessSession
from src.repl_cli.headless.headless_config import HeadlessConfig
from src.repl_cli.headless.non_recoverable_error import NonRecoverableError

def main():
    import json
    
    # Use current directory as workspace (already in WSL path format)
    workspace_directory = Path(__file__).parent.resolve()
    
    config = HeadlessConfig.load()
    if not config.is_configured:
        print(json.dumps({
            'status': 'error',
            'error': 'Headless mode not configured - API key required'
        }, indent=2))
        sys.exit(1)
    
    # Keep executing until done or blocked
    iteration = 0
    max_iterations = 100  # Safety limit
    
    while iteration < max_iterations:
        iteration += 1
        print(f"Iteration {iteration}: Executing scenarios.render.instructions...", file=sys.stderr)
        
        session = HeadlessSession(workspace_directory=workspace_directory, config=config, timeout=600)
        
        # Execute the operation
        result = session.invokes_operation(
            behavior='scenarios',
            action='render',
            operation='instructions',
            context_file=None
        )
        
        # Output result as JSON
        output = {
            'iteration': iteration,
            'status': result.status,
            'session_id': result.session_id,
            'log_path': str(result.log_path) if result.log_path else None,
            'loop_count': result.loop_count,
            'context_loaded': result.context_loaded,
            'behavior': result.behavior,
            'action': result.action,
            'operation': result.operation,
            'operations_executed': result.operations_executed,
        }
        
        if result.status == 'blocked':
            output['block_reason'] = result.block_reason
            print(json.dumps(output, indent=2))
            print(f"Blocked: {result.block_reason}", file=sys.stderr)
            sys.exit(0)
        
        if result.status == 'completed':
            print(json.dumps(output, indent=2))
            print(f"Completed after {iteration} iteration(s)", file=sys.stderr)
            sys.exit(0)
        
        if result.status == 'error':
            print(json.dumps(output, indent=2))
            print(f"Error occurred", file=sys.stderr)
            sys.exit(1)
        
        # If we get here, status is something unexpected - continue anyway
        print(json.dumps(output, indent=2))
        print(f"Unexpected status '{result.status}', continuing...", file=sys.stderr)
    
    # If we exit the loop, we've hit max iterations
    print(json.dumps({
        'status': 'error',
        'error': f'Max iterations ({max_iterations}) reached without completion'
    }, indent=2))
    sys.exit(1)

if __name__ == '__main__':
    main()
