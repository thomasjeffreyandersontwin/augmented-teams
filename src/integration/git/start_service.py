#!/usr/bin/env python3
"""
Start the Git Commit REST Service
"""

import subprocess
import sys
from pathlib import Path

def main():
    # Change to the git integration directory
    git_dir = Path(__file__).parent
    print(f"Starting Git Commit Service from: {git_dir}")
    
    # Install requirements if needed
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      cwd=git_dir, check=True)
        print("✅ Dependencies installed")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return 1
    
    # Start the service
    try:
        subprocess.run([sys.executable, "git_commit.py"], cwd=git_dir, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Service failed to start: {e}")
        return 1
    except KeyboardInterrupt:
        print("\n🛑 Service stopped by user")
        return 0

if __name__ == "__main__":
    sys.exit(main())
