#!/usr/bin/env python3
"""
Maintenance and automated update script for profile terminal assets.
Rebuilds SVGs and refreshes repository metrics.
"""

import subprocess
import sys
import os

def update_assets():
    print("Regenerating dark and light SVGs...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ascii_script = os.path.join(script_dir, "ascii_to_svg.py")
    result = subprocess.run([sys.executable, ascii_script], capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout.strip())
        print("Profile assets refreshed successfully.")
    else:
        print("Error regenerating SVGs:", result.stderr)

if __name__ == "__main__":
    update_assets()
