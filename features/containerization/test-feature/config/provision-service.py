#!/usr/bin/env python3
"""Provision this feature by calling provisioner class"""

import sys
from pathlib import Path

if __name__ == "__main__":
    feature_path = Path(__file__).parent.parent
    containerization_path = feature_path.parent.parent / "containerization"
    
    # Import and use provisioner
    sys.path.insert(0, str(containerization_path))
    from provisioner import Provisioner
    
    # Create appropriate provisioner based on mode (default to SERVICE)
    mode = sys.argv[1] if len(sys.argv) > 1 else 'SERVICE'
    always = '--always' in sys.argv
    
    provisioner = Provisioner.create(mode, feature_path, containerization_path)
    
    # Provision and start
    if provisioner.provision(always) and provisioner.start(always):
        sys.exit(0)
    else:
        sys.exit(1)
