import sys, os, re

# Path to the Jules folder
JULES_DIR = "C:/Users/Acer/jules_language"

def run_jules():
    if len(sys.argv) < 2:
        print("Usage: python jules_runner.py your_file.jules")
        return

    jules_file = os.path.abspath(sys.argv[1])
    print(f"Running: {jules_file}")

    # Process ask commands 
    with open(jules_file, 'r') as f:
        lines = f.readlines()

    modified = False
    for i, line in enumerate(lines):
        if line.strip().startswith('ask'):
            match = re.match(r'ask\s+"([^"]+)"\s+into\s+(\w+)', line.strip())
            if match:
                prompt = match.group(1)
                var_name = match.group(2)
                user_input = input(f"{prompt} ")
                lines[i] = f'{var_name} is "{user_input}"\n'
                modified = True

    if modified:
        temp_file = jules_file + ".tmp"
        with open(temp_file, 'w') as f:
            f.writelines(lines)
        jules_file = temp_file

    # Add Jules directory to Python path
    sys.path.insert(0, JULES_DIR)

    # Run Jules with the processed file
    os.system(f'python "{JULES_DIR}/jules.py" "{jules_file}"')

    # Clean up temp file if needed
    if modified:
        try:
            os.remove(jules_file)
        except:
            pass

if __name__ == "__main__":
    run_jules()
