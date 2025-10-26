#!/usr/bin/env python3
"""
Provision [FEATURE_NAME] service
Calls Provisioner from containerization
"""

import sys
from pathlib import Path

if __name__ == "__main__":
    feature_path = Path(__file__).parent.parent
    containerization_path = feature_path.parent.parent / "containerization"
    
    sys.path.insert(0, str(containerization_path))
    from provisioner import Provisioner
    
    # Default to SERVICE mode
    provisioner = Provisioner.create('SERVICE', feature_path, containerization_path)
    
    # Provision
    if not provisioner.provision(always=False):
        print("❌ Provisioning failed")
        sys.exit(1)
    
    print(f"✅ {feature_path.name} provisioned successfully!")
    sys.exit(0)
