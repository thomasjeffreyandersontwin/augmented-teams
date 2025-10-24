#!/usr/bin/env python3
"""
Git Integration Service Complete Provisioning Script

Performs full system setup:
- Environment validation
- Dependencies installation  
- Service configuration
- Repository setup
- Full testing
- Production readiness validation
"""

import subprocess
import sys
import time
import requests
from pathlib import Path

def run_command(cmd, cwd=None, check=True):
    """Run a command and return the result"""
    print(f"Running: {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    try:
        result = subprocess.run(cmd, cwd=cwd, check=check, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return result
    except subprocess.CalledProcessError as e:
        print("Command failed: {e}")
        if e.stderr:
            print(f"Error: {e.stderr}")
        return e

def validate_environment():
    """Validate system environment and prerequisites"""
    print("Validating system environment...")
    
    git_dir = Path(__file__).parent
    
    # Check Python version
    python_version = sys.version_info
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print(f"Python 3.8+ required, found {python_version.major}.{python_version.minor}")
        return False
    print(f"Python {python_version.major}.{python_version.minor}.{python_version.micro} - OK")
    
    # Check if git is available
    try:
        result = run_command(["git", "--version"], cwd=git_dir)
        print(f"Git available - OK")
    except Exception as e:
        print(f"Git not available: {e}")
        return False
    
    # Check for .env file
    env_file = git_dir / ".env"
    env_template = git_dir / "env-template.txt"
    if not env_file.exists():
        if env_template.exists():
            print("WARNING: .env file not found, but env-template.txt exists")
            print("Please copy env-template.txt to .env and configure your GitHub token")
        else:
            print("WARNING: No .env file found - GitHub authentication may not work")
    else:
        print(".env file found - OK")
    
    # Check required files exist
    required_files = [
        "build-requirements.txt",
        "service.py", 
        "integration.py",
        "test-service.py"
    ]
    
    for file_name in required_files:
        file_path = git_dir / file_name
        if not file_path.exists():
            print(f"Required file missing: {file_name}")
            return False
        print(f"{file_name} - OK")
    
    print("Environment validation completed successfully")
    return True

def setup_service_configuration():
    """Setup service configuration and validate modules"""
    print("Setting up service configuration...")
    
    git_dir = Path(__file__).parent
    
    # Check if service.py can be imported
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("service", git_dir / "service.py")
        service_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(service_module)
        print("Service module import - OK")
    except Exception as e:
        print(f"Service module import failed: {e}")
        return False
    
    # Check if integration.py can be imported
    try:
        spec = importlib.util.spec_from_file_location("integration", git_dir / "integration.py")
        integration_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(integration_module)
        print("Integration module import - OK")
    except Exception as e:
        print(f"Integration module import failed: {e}")
        return False
    
    print("Service configuration setup completed successfully")
    return True

def production_readiness_check():
    """Perform production readiness validation"""
    print("Performing production readiness check...")
    
    git_dir = Path(__file__).parent
    
    # Check if service can start and respond
    process = start_service()
    if not process:
        print("Service startup failed - NOT READY")
        return False
    
    try:
        # Test all critical endpoints
        endpoints_to_test = [
            "/",
            "/auth/github",
            "/status", 
            "/tree",
            "/search/files?pattern=*.py"
        ]
        
        for endpoint in endpoints_to_test:
            try:
                response = requests.get(f"http://localhost:8001{endpoint}", timeout=5)
                if response.status_code == 200:
                    print(f"Endpoint {endpoint} - OK")
                    
                    # Check GitHub auth status for auth endpoint
                    if endpoint == "/auth/github":
                        data = response.json()
                        if data.get("authenticated"):
                            print(f"GitHub authentication - OK ({data.get('message', '')})")
                        else:
                            print(f"GitHub authentication - WARNING ({data.get('message', '')})")
                else:
                    print(f"Endpoint {endpoint} - FAILED (status {response.status_code})")
                    return False
            except Exception as e:
                print(f"Endpoint {endpoint} - FAILED ({e})")
                return False
        
        print("All critical endpoints responding - OK")
        return True
        
    finally:
        # Always cleanup
        if process:
            process.terminate()
            process.wait()
            print("Test service stopped")

def install_dependencies():
    """Install dependencies from build-requirements.txt"""
    print("Checking dependencies...")
    
    git_dir = Path(__file__).parent
    
    # Check if build-requirements.txt exists
    requirements_file = git_dir / "build-requirements.txt"
    if not requirements_file.exists():
        print("build-requirements.txt not found")
        return False
    
    # Install dependencies
    print("Installing dependencies...")
    result = run_command([sys.executable, "-m", "pip", "install", "-r", "build-requirements.txt"], 
                        cwd=git_dir)
    
    if result.returncode == 0:
        print("Dependencies installed successfully")
        return True
    else:
        print("Failed to install dependencies")
        return False

def start_service_foreground():
    """Start the service in foreground (blocks until stopped)"""
    git_dir = Path(__file__).parent
    service_file = git_dir / "service.py"
    
    if not service_file.exists():
        print("service.py not found")
        return 1
    
    print("Starting Git Integration Service...")
    try:
        subprocess.run([sys.executable, "service.py"], cwd=git_dir, check=True)
        return 0
    except subprocess.CalledProcessError as e:
        print(f"Service failed to start: {e}")
        return 1
    except KeyboardInterrupt:
        print("Service stopped by user")
        return 0

def start_service():
    """Start the Git Integration Service in background"""
    print("Starting Git Integration Service...")
    
    git_dir = Path(__file__).parent
    service_file = git_dir / "service.py"
    
    if not service_file.exists():
        print("service.py not found")
        return None
    
    # Start the service in the background
    try:
        process = subprocess.Popen([sys.executable, "service.py"], 
                                 cwd=git_dir, 
                                 stdout=subprocess.PIPE, 
                                 stderr=subprocess.PIPE)
        
        # Wait a moment for the service to start
        print("Waiting for service to start...")
        time.sleep(3)
        
        # Check if service is running
        try:
            response = requests.get("http://localhost:8001/", timeout=5)
            if response.status_code == 200:
                print("Service started successfully on port 8001")
                return process
            else:
                print(f"Service responded with status {response.status_code}")
                return None
        except requests.exceptions.RequestException:
            print("Service failed to start or is not responding")
            return None
            
    except Exception as e:
        print(f"Failed to start service: {e}")
        return None

def run_tests():
    """Run the test suite"""
    print("Running test suite...")
    
    git_dir = Path(__file__).parent
    test_file = git_dir / "test-service.py"
    
    if not test_file.exists():
        print("test-service.py not found")
        return False
    
    result = run_command([sys.executable, "test-service.py"], cwd=git_dir)
    
    if result.returncode == 0:
        print("All tests passed!")
        return True
    else:
        print("Some tests failed")
        return False

def cleanup(process):
    """Clean up the service process"""
    if process:
        print("Stopping service...")
        process.terminate()
        process.wait()
        print("Service stopped")

def main():
    """Complete provisioning function"""
    print("Git Integration Service Complete Provisioning")
    print("=" * 60)
    
    # Step 1: Validate environment
    if not validate_environment():
        print("Environment validation failed")
        return 1
    
    # Step 2: Install dependencies
    if not install_dependencies():
        print("Dependency installation failed")
        return 1
    
    # Step 3: Setup service configuration
    if not setup_service_configuration():
        print("Service configuration setup failed")
        return 1
    
    # Step 4: Production readiness check
    if not production_readiness_check():
        print("Production readiness check failed")
        return 1
    
    # Step 5: Run comprehensive tests
    process = start_service()
    if not process:
        print("Service startup failed")
        return 1
    
    try:
        test_success = run_tests()
        
        if test_success:
            print("\n" + "=" * 60)
            print("COMPLETE PROVISIONING SUCCESSFUL!")
            print("=" * 60)
            print("Environment validated - OK")
            print("Dependencies installed - OK")
            print("Service configured - OK")
            print("Production ready - OK")
            print("All tests passed - OK")
            print("\nService is ready for production use!")
            return 0
        else:
            print("\n" + "=" * 60)
            print("PROVISIONING COMPLETED WITH TEST FAILURES")
            print("=" * 60)
            print("Environment validated - OK")
            print("Dependencies installed - OK")
            print("Service configured - OK")
            print("Production ready - OK")
            print("Some tests failed - CHECK REQUIRED")
            return 1
            
    finally:
        # Always cleanup
        cleanup(process)

if __name__ == "__main__":
    sys.exit(main())
