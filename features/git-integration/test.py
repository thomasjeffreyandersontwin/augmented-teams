#!/usr/bin/env python3
"""
Test runner for git-integration
Calls TestRunner from containerization
"""

import sys
from pathlib import Path

# Add containerization to path
feature_path = Path(__file__).parent
containerization_path = feature_path.parent / "containerization"

sys.path.insert(0, str(containerization_path))
from test import TestRunner

def main():
    """Run tests"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Test git-integration')
    parser.add_argument('mode', choices=['CODE', 'SERVICE', 'CONTAINER'])
    parser.add_argument('--always-provision', action='store_true')
    
    args = parser.parse_args()
    
    runner = TestRunner(feature_path)
    result = runner.run_tests(args.mode, args.always_provision)
    sys.exit(result)

if __name__ == "__main__":
    main()

