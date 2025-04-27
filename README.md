# Jules Language

Jules is a beginner-friendly programming language designed to be readable, simple, and close to natural English.

## Features

- Minimal syntax with English-like commands
- Readable control structures
- Simple data types
- Friendly error messages
- Designed for beginners and educational purposes

## Running Jules

There are two simple ways to run Jules:

### Option 1: Using the batch file (Windows)

1. Double-click `run_jules.bat` to open the interactive mode
2. Or drag and drop a `.jules` file onto `run_jules.bat`

### Option 2: Using Python directly

```bash
# Run a Jules script
python jules.py your_script.jules

# Or use interactive mode
python jules.py
```

## Using Jules in Any Folder

If you want to use Jules in a different folder:

1. Copy the `jules_setup.bat` file to your target folder
2. Run it by double-clicking
3. It will create all necessary files to run Jules
4. You can then run Jules files with VS Code (Ctrl+Shift+B) or the command line

## Example

```jules
show "Hello World"

ask "What is your name?" into name
show "Nice to meet you, " + name

when name is "Jules" then
    show "That's my name too!"
otherwise
    show "My name is Jules"
done
```

## Documentation

See the `docs` folder for more information about the language syntax and features.
For help with the `ask` command and more examples, see `JULES_HELP.md`. 