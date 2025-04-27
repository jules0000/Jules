@echo off
echo Jules Quick Setup - Works in Any Folder
echo =====================================

echo Creating necessary files...

REM Create VS Code folder
mkdir .vscode 2>nul

REM Create the runner script that makes ask command work
echo import sys, os, re> jules_runner.py
echo.>> jules_runner.py
echo # Path to the Jules folder>> jules_runner.py
echo JULES_DIR = "C:/Users/Acer/jules_language">> jules_runner.py
echo.>> jules_runner.py
echo def run_jules():>> jules_runner.py
echo     if len(sys.argv) ^< 2:>> jules_runner.py
echo         print("Usage: python jules_runner.py your_file.jules")>> jules_runner.py
echo         return>> jules_runner.py
echo.>> jules_runner.py 
echo     jules_file = os.path.abspath(sys.argv[1])>> jules_runner.py
echo     print(f"Running: {jules_file}")>> jules_runner.py
echo.>> jules_runner.py
echo     # Process ask commands >> jules_runner.py
echo     with open(jules_file, 'r') as f:>> jules_runner.py
echo         lines = f.readlines()>> jules_runner.py
echo.>> jules_runner.py
echo     modified = False>> jules_runner.py
echo     for i, line in enumerate(lines):>> jules_runner.py
echo         if line.strip().startswith('ask'):>> jules_runner.py
echo             match = re.match(r'ask\s+"([^"]+)"\s+into\s+(\w+)', line.strip())>> jules_runner.py
echo             if match:>> jules_runner.py
echo                 prompt = match.group(1)>> jules_runner.py
echo                 var_name = match.group(2)>> jules_runner.py
echo                 user_input = input(f"{prompt} ")>> jules_runner.py
echo                 lines[i] = f'{var_name} is "{user_input}"\n'>> jules_runner.py
echo                 modified = True>> jules_runner.py
echo.>> jules_runner.py
echo     if modified:>> jules_runner.py
echo         temp_file = jules_file + ".tmp">> jules_runner.py
echo         with open(temp_file, 'w') as f:>> jules_runner.py
echo             f.writelines(lines)>> jules_runner.py
echo         jules_file = temp_file>> jules_runner.py
echo.>> jules_runner.py 
echo     # Add Jules directory to Python path>> jules_runner.py
echo     sys.path.insert(0, JULES_DIR)>> jules_runner.py
echo.>> jules_runner.py
echo     # Run Jules with the processed file>> jules_runner.py
echo     os.system(f'python "{JULES_DIR}/jules.py" "{jules_file}"')>> jules_runner.py
echo.>> jules_runner.py
echo     # Clean up temp file if needed>> jules_runner.py
echo     if modified:>> jules_runner.py
echo         try:>> jules_runner.py
echo             os.remove(jules_file)>> jules_runner.py
echo         except:>> jules_runner.py
echo             pass>> jules_runner.py
echo.>> jules_runner.py
echo if __name__ == "__main__":>> jules_runner.py
echo     run_jules()>> jules_runner.py

REM Create a fixed run_jules.py script
echo #!/usr/bin/env python3> run_jules.py
echo """>> run_jules.py
echo Run the Jules programming language interpreter (Fixed version for external folders)>> run_jules.py
echo """>> run_jules.py
echo.>> run_jules.py
echo import sys, os>> run_jules.py
echo import traceback>> run_jules.py
echo.>> run_jules.py
echo # Add Jules directory to Python path>> run_jules.py
echo JULES_DIR = "C:/Users/Acer/jules_language">> run_jules.py
echo sys.path.insert(0, JULES_DIR)>> run_jules.py
echo.>> run_jules.py
echo # Now we can import Jules modules>> run_jules.py
echo from jules.core.interpreter import run_file, run_interactive>> run_jules.py
echo.>> run_jules.py
echo if __name__ == "__main__":>> run_jules.py
echo     try:>> run_jules.py
echo         if len(sys.argv) ^> 1:>> run_jules.py
echo             print(f"Running file: {sys.argv[1]}")>> run_jules.py
echo             run_file(sys.argv[1])>> run_jules.py
echo         else:>> run_jules.py
echo             run_interactive()>> run_jules.py
echo     except Exception as e:>> run_jules.py
echo         print(f"An error occurred: {e}")>> run_jules.py
echo         traceback.print_exc()>> run_jules.py

REM Create tasks.json for VS Code
echo {> .vscode\tasks.json
echo     "version": "2.0.0",>> .vscode\tasks.json
echo     "tasks": [>> .vscode\tasks.json
echo         {>> .vscode\tasks.json
echo             "label": "Run Jules File",>> .vscode\tasks.json
echo             "type": "process",>> .vscode\tasks.json
echo             "command": "python",>> .vscode\tasks.json
echo             "args": [>> .vscode\tasks.json
echo                 "${workspaceFolder}/jules_runner.py",>> .vscode\tasks.json
echo                 "${file}">> .vscode\tasks.json
echo             ],>> .vscode\tasks.json
echo             "group": {>> .vscode\tasks.json
echo                 "kind": "build",>> .vscode\tasks.json
echo                 "isDefault": true>> .vscode\tasks.json
echo             },>> .vscode\tasks.json
echo             "presentation": {>> .vscode\tasks.json
echo                 "reveal": "always",>> .vscode\tasks.json
echo                 "panel": "new">> .vscode\tasks.json
echo             }>> .vscode\tasks.json
echo         }>> .vscode\tasks.json
echo     ]>> .vscode\tasks.json
echo }>> .vscode\tasks.json

REM Create a simple example for users
echo # Jules Example with Ask Command> example.jules
echo.>> example.jules
echo # Ask for user input>> example.jules
echo ask "What is your name?" into name>> example.jules
echo.>> example.jules
echo # Display the name>> example.jules
echo show "Hello">> example.jules
echo show name>> example.jules
echo.>> example.jules
echo # Ask for more input>> example.jules
echo ask "What is your age?" into age>> example.jules
echo.>> example.jules
echo # Display age information>> example.jules
echo show "You are">> example.jules
echo show age>> example.jules
echo show "years old.">> example.jules

echo.
echo Setup completed successfully!
echo.
echo Files created:
echo - jules_runner.py (runs Jules files with working ask command)
echo - run_jules.py (fixed version that works in external folders)
echo - .vscode/tasks.json (VS Code configuration)
echo - example.jules (sample file showing how to use ask command)
echo.
echo To run a Jules file:
echo 1. Open VS Code in this folder
echo 2. Open a .jules file
echo 3. Press Ctrl+Shift+B or F5 to run it
echo.
echo Command line options:
echo - python jules_runner.py your_file.jules (supports ask command)
echo - python run_jules.py your_file.jules (simpler version)
echo.
pause 