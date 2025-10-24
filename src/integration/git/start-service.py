#!/usr/bin/env python3
"""
Start the Git Integration Service
"""

import sys
from provision_service import install_dependencies, start_service_foreground

def main():
    print("🚀 Starting Git Integration Service")
    print("=" * 40)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Dependency installation failed")
        return 1
    
    # Start the service in foreground
    return start_service_foreground()

if __name__ == "__main__":
    sys.exit(main())
