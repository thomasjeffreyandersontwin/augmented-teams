#!/usr/bin/env python3
"""
Base class for service-test.py files
Provides common functionality for loading URLs from config and running tests
"""

import sys
import yaml
from pathlib import Path

def get_base_url(feature_path, mode='SERVICE'):
    """Get base URL from config based on mode"""
    config_file = feature_path / "config" / "feature-config.yaml"
    
    if not config_file.exists():
        return 'http://localhost:8000'  # fallback
    
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    
    if mode == 'SERVICE':
        return config.get('environment', {}).get('development', {}).get('url', 'http://localhost:8000')
    else:  # CONTAINER
        return config.get('environment', {}).get('production', {}).get('url', 'http://localhost:8000')

# Global mode variable for get_base_url
_mode = 'SERVICE'

def run_service_tests(test_functions):
    """Common runner for service tests"""
    global _mode
    
    # Get feature_path from the caller's file
    import inspect
    caller_frame = inspect.currentframe().f_back
    caller_file = Path(caller_frame.f_globals['__file__'])
    feature_path = caller_file.parent
    
    containerization_path = feature_path.parent.parent / "containerization"
    sys.path.insert(0, str(containerization_path))
    
    import argparse
    from provisioner import Provisioner
    
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['SERVICE', 'CONTAINER'])
    parser.add_argument('--always-provision', action='store_true')
    args = parser.parse_args()
    
    # Store mode globally
    _mode = args.mode
    
    # Provision and start
    provisioner = Provisioner.create(args.mode, feature_path, containerization_path)
    if not provisioner.provision(args.always_provision):
        sys.exit(1)
    if not provisioner.start(args.always_provision):
        sys.exit(1)
    
    # Run all test functions
    for test_func in test_functions:
        test_func()
    
    print("✅ All service tests passed")
