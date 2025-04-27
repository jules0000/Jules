"""
Jules Programming Language

A friendly programming language designed for beginners.
"""

import sys
from jules.core.interpreter import JulesInterpreter, run_file, run_interactive

def main():
    """Entry point for the Jules language"""
    if len(sys.argv) > 1:
        run_file(sys.argv[1])
    else:
        run_interactive()

if __name__ == "__main__":
    main() 