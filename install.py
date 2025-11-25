#!/usr/bin/env python3
"""
Installation script for LoRA Downloader plugin
This script is used by ComfyUI Manager to install the plugin
"""

import subprocess
import sys
import os

def install_dependencies():
    """Install required Python packages"""
    try:
        # Install requests if not already installed
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", 
                             os.path.join(os.path.dirname(__file__), "requirements.txt")])
        print("Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        return False

if __name__ == "__main__":
    success = install_dependencies()
    sys.exit(0 if success else 1)
