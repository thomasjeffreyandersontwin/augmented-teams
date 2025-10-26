#!/usr/bin/env python3
"""
Shared Test Runner - unified testing for code, service, and container modes
"""

import sys
import subprocess
import requests
import argparse
from pathlib import Path
import time
from provisioner import Provisioner

class TestRunner:
    """Test runner that uses provisioners"""
    
    def __init__(self, feature_path):
        self.feature_path = feature_path
        self.containerization_path = feature_path.parent.parent / "containerization"
        self.provisioner = None
    
    def run_tests(self, mode, always_provision=False):
        """Run tests for the given mode"""
        # Create provisioner using static factory method from provisioner module
        from provisioner import Provisioner
        self.provisioner = Provisioner.create(mode, self.feature_path, self.containerization_path)
        
        # Provision
        if not self.provisioner.provision(always_provision):
            print("❌ Provisioning failed")
            return 1
        
        # Start (if needed)
        if not self.provisioner.start(always_provision):
            print("❌ Failed to start")
            return 1
        
        # Get test URL
        test_url = self.provisioner.get_test_url()
        
        # Run appropriate test
        if mode == 'CODE':
            return self._test_code()
        elif test_url:
            return self._test_service(test_url)
        
        return 1
    
    def _test_code(self):
        """Run code tests"""
        print(f"🔍 Running code tests for {self.feature_path.name}...")
        sys.path.insert(0, str(self.feature_path))
        
        try:
            from main import app
            print("✅ Code imports successfully")
            return 0
        except Exception as e:
            print(f"❌ Code test failed: {e}")
            return 1
    
    def _test_service(self, url):
        """Test service endpoints"""
        print(f"🔍 Testing service at {url}...")
        
        # Import the app to discover routes
        sys.path.insert(0, str(self.feature_path))
        from main import app
        
        # Test all routes
        success_count = 0
        total_count = 0
        
        # Discover routes from the app
        skipped_routes = []
        for route in app.routes:
            if hasattr(route, 'path') and hasattr(route, 'methods'):
                methods = route.methods
                path = route.path
                
                # Skip routes with path parameters (they require specific values)
                if '{' in path and '}' in path:
                    for method in methods:
                        if method in ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']:
                            skipped_routes.append(f"{method} {path}")
                    continue
                
                for method in methods:
                    if method in ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']:
                        total_count += 1
                        test_url = f"{url}{path}"
                        
                        try:
                            if method == 'GET':
                                response = requests.get(test_url, timeout=5)
                            elif method == 'POST':
                                # For POST, send empty JSON body
                                response = requests.post(test_url, json={}, timeout=5)
                            elif method == 'PUT':
                                response = requests.put(test_url, json={}, timeout=5)
                            elif method == 'DELETE':
                                response = requests.delete(test_url, timeout=5)
                            elif method == 'PATCH':
                                response = requests.patch(test_url, json={}, timeout=5)
                            
                            if response.status_code < 400:
                                print(f"✅ {method} {path} - {response.status_code}")
                                success_count += 1
                            elif response.status_code in [401, 403]:
                                # Auth required - acceptable
                                print(f"🔐 {method} {path} - {response.status_code} (auth required)")
                                success_count += 1
                            elif response.status_code == 422:
                                # Validation error - acceptable for POST without data
                                print(f"✓ {method} {path} - {response.status_code} (validates params)")
                                success_count += 1
                            else:
                                print(f"⚠️ {method} {path} - {response.status_code}")
                        except Exception as e:
                            print(f"❌ {method} {path} - {e}")
        
        if total_count == 0:
            # Fallback to simple health check
            return self._simple_health_check(url)
        
        print(f"\n📊 Results: {success_count}/{total_count} tests passed")
        return 0 if success_count == total_count else 1
    
    def _simple_health_check(self, url):
        """Simple health check fallback"""
        try:
            response = requests.get(f"{url}/", timeout=5)
            if response.status_code == 200:
                print(f"✅ Service health check passed: {response.json()}")
                return 0
            else:
                print(f"❌ Service returned {response.status_code}")
                return 1
        except Exception as e:
            print(f"❌ Service test failed: {e}")
            return 1

def main():
    parser = argparse.ArgumentParser(description='Shared test runner')
    parser.add_argument('feature_path', nargs='?', help='Feature path')
    parser.add_argument('mode', choices=['CODE', 'SERVICE', 'CONTAINER'])
    parser.add_argument('--url', help='Override test URL')
    parser.add_argument('--always-provision', action='store_true', help='Always provision and start')
    
    args = parser.parse_args()
    
    # Get feature path
    if args.feature_path:
        feature_path = Path(args.feature_path)
    else:
        feature_path = Path(__file__).parent.parent
    
    # Create runner and run tests
    runner = TestRunner(feature_path)
    
    # Set test URL if provided
    test_url = args.url
    
    result = runner.run_tests(args.mode, args.always_provision)
    sys.exit(result)

if __name__ == "__main__":
    main()
