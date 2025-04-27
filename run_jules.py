#!/usr/bin/env python3
"""
Run the Jules programming language interpreter (Fixed version for external folders)
"""

import sys, os
import traceback

# Add Jules directory to Python path
JULES_DIR = "C:/Users/Acer/jules_language"
sys.path.insert(0, JULES_DIR)

# Now we can import Jules modules
from jules.core.interpreter import run_file, run_interactive

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            print(f"Running file: {sys.argv[1]}")
            run_file(sys.argv[1])
        else:
            run_interactive()
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc() 