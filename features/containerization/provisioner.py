#!/usr/bin/env python3
"""
Provisioner Classes

Contains all provisioner implementations for CODE, SERVICE, and CONTAINER modes
"""

import sys
import subprocess
import requests
import time
from pathlib import Path
from abc import ABC, abstractmethod

class Provisioner(ABC):
    """Abstract base class for provisioners"""
    
    def __init__(self, feature_path, containerization_path):
        self.feature_path = feature_path
        self.containerization_path = containerization_path
    
    @staticmethod
    def create(mode, feature_path, containerization_path):
        """Factory method to create appropriate provisioner"""
        if mode == 'CODE':
            return CodeProvisioner(feature_path, containerization_path)
        elif mode == 'SERVICE':
            return ServiceProvisioner(feature_path, containerization_path)
        elif mode == 'CONTAINER':
            return ContainerProvisioner(feature_path, containerization_path)
        else:
            raise ValueError(f"Unknown mode: {mode}")
    
    def is_provisioning_needed(self):
        """Check if provisioning is needed (check if up to date)"""
        # TODO: Implement checking logic (e.g., compare timestamps, check if deps installed, etc.)
        return True
    
    def is_service_running(self):
        """Check if service is already running"""
        test_url = self.get_test_url()
        if not test_url:
            return False
        try:
            response = requests.get(test_url, timeout=2)
            return response.status_code == 200
        except:
            return False
    
    @abstractmethod
    def provision(self, always=False):
        """Provision the service"""
        pass
    
    @abstractmethod
    def start(self, always=False):
        """Start the service"""
        pass
    
    @abstractmethod
    def get_test_url(self):
        """Get the URL for testing"""
        pass

class CodeProvisioner(Provisioner):
    """Provisioner for code-only tests (no service needed)"""
    
    def provision(self, always=False):
        """No provisioning needed for code tests"""
        return True
    
    def start(self, always=False):
        """No start needed for code tests"""
        return True
    
    def get_test_url(self):
        """No URL for code tests"""
        return None

class ServiceProvisioner(Provisioner):
    """Provisioner for in-memory service tests"""
    
    def _get_config(self):
        """Load config from feature-config.yaml"""
        import yaml
        config_file = self.feature_path / "config" / "feature-config.yaml"
        if config_file.exists():
            with open(config_file, 'r') as f:
                return yaml.safe_load(f)
        return {}
    
    def provision(self, always=False):
        """Provision the service"""
        # Check if provisioning is needed
        if not always and not self.is_provisioning_needed():
            print("✅ Service already provisioned and up to date")
            return True
        
        print(f"🚀 Provisioning {self.feature_path.name}...")
        print("=" * 60)
        
        # Install dependencies from build.requirements in config
        print("📦 Installing dependencies...")
        config = self._get_config()
        requirements = config.get('build', {}).get('requirements', [])
        
        if requirements:
            # Install each requirement
            for req in requirements:
                result = subprocess.run([sys.executable, "-m", "pip", "install", req])
                if result.returncode != 0:
                    print(f"❌ Failed to install {req}")
                    return False
            print("✅ Dependencies installed")
        else:
            print("⚠️ No build.requirements in config")
        
        return True
    
    def start(self, always=False):
        """Start service in-memory"""
        # Check if already running
        if not always and self.is_service_running():
            print("✅ Service already running")
            return True
        
        # Start service by importing and running with uvicorn
        print("🚀 Starting service in-memory...")
        sys.path.insert(0, str(self.feature_path))
        import uvicorn
        import threading
        
        # Run in background thread
        # Try service.py first, fall back to main.py
        try:
            from service import app
            module = "service"
        except ImportError:
            from main import app
            module = "main"
        
        def run_server():
            uvicorn.run(f"{module}:app", host='0.0.0.0', port=8000, log_level='info', reload=False)
        
        server_thread = threading.Thread(target=run_server, daemon=True)
        server_thread.start()
        
        # Wait for service to be ready
        time.sleep(2)
        return True
    
    def get_test_url(self):
        """Get service test URL from config (dev)"""
        config = self._get_config()
        return config.get('environment', {}).get('development', {}).get('url', "http://localhost:8000")

class ContainerProvisioner(Provisioner):
    """Provisioner for container tests"""
    
    def _get_config(self):
        """Load config from feature-config.yaml"""
        import yaml
        config_file = self.feature_path / "config" / "feature-config.yaml"
        if config_file.exists():
            with open(config_file, 'r') as f:
                return yaml.safe_load(f)
        return {}
    
    def provision(self, always=False):
        """Provision the container"""
        # Check if provisioning is needed
        if not always and not self.is_provisioning_needed():
            print("✅ Service already provisioned and up to date")
            return True
        
        print(f"🚀 Provisioning {self.feature_path.name}...")
        print("=" * 60)
        
        # Install dependencies from build.requirements in config
        print("📦 Installing dependencies...")
        config = self._get_config()
        requirements = config.get('build', {}).get('requirements', [])
        
        if requirements:
            # Install each requirement
            for req in requirements:
                result = subprocess.run([sys.executable, "-m", "pip", "install", req])
                if result.returncode != 0:
                    print(f"❌ Failed to install {req}")
                    return False
            print("✅ Dependencies installed")
        else:
            print("⚠️ No build.requirements in config")
        
        return True
    
    def start(self, always=False):
        """Start container by spawning service.py as background subprocess"""
        # Check if already running
        if not always and self.is_service_running():
            print("✅ Container already running")
            return True
        
        # Start service by spawning service.py in background
        print("🚀 Starting container...")
        sys.path.insert(0, str(self.feature_path))
        import uvicorn
        import threading
        
        # Try service.py first, fall back to main.py
        try:
            from service import app
            module = "service"
        except ImportError:
            from main import app
            module = "main"
        
        def run_server():
            uvicorn.run(f"{module}:app", host='0.0.0.0', port=8000, log_level='info', reload=False)
        
        server_thread = threading.Thread(target=run_server, daemon=True)
        server_thread.start()
        
        # Wait for service to be ready
        time.sleep(2)
        return True
    
    def get_test_url(self):
        """Get container test URL from config (production)"""
        config = self._get_config()
        return config.get('environment', {}).get('production', {}).get('url', "http://localhost:8000")

def main():
    """
    Main provisioning CLI
    
    Examples:
        # Provision a feature in SERVICE mode
        python provisioner.py SERVICE features/git-integration
        
        # Provision in CONTAINER mode
        python provisioner.py CONTAINER features/git-integration
        
        # Provision with --always flag (skip checks)
        python provisioner.py SERVICE features/git-integration --always
        
        # Code mode (no service needed)
        python provisioner.py CODE features/git-integration
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='Provision service')
    parser.add_argument('mode', choices=['CODE', 'SERVICE', 'CONTAINER'], help='Mode: CODE, SERVICE, or CONTAINER')
    parser.add_argument('feature_path', nargs='?', help='Feature path (default: parent)')
    parser.add_argument('--always', action='store_true', help='Always provision/start (skip checks)')
    
    args = parser.parse_args()
    
    # Get feature path
    if args.feature_path:
        feature_path = Path(args.feature_path)
    else:
        # Default to parent of containerization folder
        feature_path = Path(__file__).parent.parent
    
    # Get containerization path
    containerization_path = Path(__file__).parent
    
    # Create provisioner
    provisioner = Provisioner.create(args.mode, feature_path, containerization_path)
    
    # Run provisioning
    if not provisioner.provision(args.always):
        print("❌ Provisioning failed")
        sys.exit(1)
    
    # Start service (if not CODE mode)
    if args.mode != 'CODE':
        if not provisioner.start(args.always):
            print("❌ Failed to start service")
            sys.exit(1)
    
    print(f"✅ {feature_path.name} provisioned and started successfully!")
    sys.exit(0)

if __name__ == "__main__":
    main()

