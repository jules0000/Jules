#!/usr/bin/env python3
"""
Jules Language Interpreter

A simple and friendly programming language designed for beginners.
"""

import re
import sys
import os
import importlib.util

# Enable this for debugging
DEBUG = True

def debug_print(message):
    """Print debug messages if DEBUG is True"""
    if DEBUG:
        print(f"DEBUG: {message}")

class JulesInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.procedures = {}
        self.libraries = {}
        
    def tokenize(self, code):
        """Convert code string into tokens"""
        # Remove comments (anything after #)
        code = re.sub(r'#.*$', '', code, flags=re.MULTILINE)
        
        # Add spaces around special characters for easier tokenization
        code = re.sub(r'([+\-*/=<>"])', r' \1 ', code)
        
        # Split by whitespace and filter out empty tokens
        tokens = [token for token in code.split() if token]
        return tokens
    
    def parse_and_execute(self, code):
        """Parse and execute Jules code"""
        lines = code.split('\n')
        i = 0
        result = None
        
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines and comments
            if not line or line.startswith('#'):
                i += 1
                continue
                
            debug_print(f"Executing line: {line}")
                
            # Parse show command
            if line.startswith('show'):
                value = self._parse_expression(line[4:].strip())
                debug_print(f"Showing value: {value} (type: {type(value)})")
                print(str(value))
                i += 1
                
            # Parse variable assignment
            elif ' is ' in line and not line.startswith('when'):
                parts = line.split(' is ', 1)
                var_name = parts[0].strip()
                value = self._parse_expression(parts[1].strip())
                debug_print(f"Setting variable {var_name} = {value} (type: {type(value)})")
                self.variables[var_name] = value
                i += 1
                
            # Parse when/then/otherwise/done blocks
            elif line.startswith('when'):
                condition_text = line[4:].split('then')[0].strip()
                condition_result = self._evaluate_condition(condition_text)
                debug_print(f"Condition '{condition_text}' evaluated to {condition_result}")
                
                # Find the matching done
                done_idx = self._find_matching_done(lines, i)
                
                # Find otherwise if it exists
                otherwise_idx = self._find_otherwise(lines, i, done_idx)
                
                if condition_result:
                    # Execute the then block
                    debug_print("Executing 'then' block")
                    self.parse_and_execute('\n'.join(lines[i+1:otherwise_idx if otherwise_idx else done_idx]))
                elif otherwise_idx:
                    # Execute the otherwise block
                    debug_print("Executing 'otherwise' block")
                    self.parse_and_execute('\n'.join(lines[otherwise_idx+1:done_idx]))
                
                i = done_idx + 1  # Move past the 'done'
                
            # Parse repeat loops
            elif line.startswith('repeat'):
                if 'times' in line:
                    # repeat n times
                    count_expr = line.split('repeat')[1].split('times')[0].strip()
                    count = int(self._parse_expression(count_expr))
                    debug_print(f"Repeating {count} times")
                    done_idx = self._find_matching_done(lines, i)
                    loop_body = '\n'.join(lines[i+1:done_idx])
                    
                    for count_value in range(1, count + 1):  # Start from 1 for more natural counting
                        # Add count variable to access the current iteration
                        debug_print(f"Loop iteration {count_value}")
                        old_count = self.variables.get('count', None)
                        self.variables['count'] = count_value
                        self.parse_and_execute(loop_body)
                        if old_count is not None:
                            self.variables['count'] = old_count
                        else:
                            if 'count' in self.variables:
                                del self.variables['count']
                    
                    i = done_idx + 1  # Move past the 'done'
                elif 'each' in line:
                    # repeat each item in list
                    match = re.match(r'repeat each (\w+) in (.+)', line)
                    if match:
                        item_name = match.group(1)
                        list_expr = match.group(2)
                        items = self._parse_expression(list_expr)
                        debug_print(f"Iterating over list: {items}")
                        
                        done_idx = self._find_matching_done(lines, i)
                        loop_body = '\n'.join(lines[i+1:done_idx])
                        
                        # Save the original value of the loop variable if it exists
                        old_value = self.variables.get(item_name, None)
                        
                        for item in items:
                            debug_print(f"Processing item: {item}")
                            self.variables[item_name] = item
                            self.parse_and_execute(loop_body)
                        
                        # Restore the original value or remove the variable
                        if old_value is not None:
                            self.variables[item_name] = old_value
                        else:
                            if item_name in self.variables:
                                del self.variables[item_name]
                        
                        i = done_idx + 1  # Move past the 'done'
            
            # Parse while loops
            elif line.startswith('while'):
                condition_text = line[5:].strip()
                done_idx = self._find_matching_done(lines, i)
                loop_body = '\n'.join(lines[i+1:done_idx])
                
                iteration = 1
                while self._evaluate_condition(condition_text):
                    debug_print(f"While loop iteration {iteration} (condition: {condition_text})")
                    self.parse_and_execute(loop_body)
                    iteration += 1
                    
                    # Safety valve to prevent infinite loops during development
                    if iteration > 1000:
                        debug_print("Possible infinite loop detected, breaking")
                        break
                
                i = done_idx + 1  # Move past the 'done'
            
            # Parse ask command
            elif line.startswith('ask'):
                match = re.match(r'ask\s+"([^"]+)"\s+into\s+(\w+)', line)
                if match:
                    prompt = match.group(1)
                    var_name = match.group(2)
                    debug_print(f"Asking input with prompt: {prompt}")
                    user_input = input(prompt + " ")
                    self.variables[var_name] = user_input
                    debug_print(f"Got input: {user_input}")
                i += 1
            
            # Parse function definitions
            elif line.startswith('make'):
                match = re.match(r'make\s+(\w+)\((.*?)\)', line)
                if match:
                    func_name = match.group(1)
                    params = [p.strip() for p in match.group(2).split(',') if p.strip()]
                    
                    done_idx = self._find_matching_done(lines, i)
                    func_body = lines[i+1:done_idx]
                    
                    debug_print(f"Defining function {func_name} with parameters {params}")
                    self.functions[func_name] = {
                        'params': params,
                        'body': func_body
                    }
                    
                    i = done_idx + 1  # Move past the 'done'
            
            # Parse procedure definitions
            elif line.startswith('do '):
                match = re.match(r'do\s+(\w+)\((.*?)\)', line)
                if match:
                    proc_name = match.group(1)
                    params = [p.strip() for p in match.group(2).split(',') if p.strip()]
                    
                    done_idx = self._find_matching_done(lines, i)
                    proc_body = lines[i+1:done_idx]
                    
                    debug_print(f"Defining procedure {proc_name} with parameters {params}")
                    self.procedures[proc_name] = {
                        'params': params,
                        'body': proc_body
                    }
                    
                    i = done_idx + 1  # Move past the 'done'
            
            # Parse library imports
            elif line.startswith('get'):
                lib_name = line[3:].strip()
                debug_print(f"Importing library: {lib_name}")
                self._import_library(lib_name)
                i += 1
            
            # Parse function/procedure calls
            elif '(' in line and ')' in line:
                call_match = re.match(r'(\w+)\((.*?)\)', line)
                if call_match:
                    func_name = call_match.group(1)
                    arg_str = call_match.group(2)
                    args = [self._parse_expression(arg.strip()) for arg in arg_str.split(',') if arg.strip()]
                    
                    debug_print(f"Function/procedure call: {func_name}{args}")
                    
                    # Check if it's a function call
                    if func_name in self.functions:
                        result = self._call_function(func_name, args)
                    # Check if it's a procedure call
                    elif func_name in self.procedures:
                        self._call_procedure(func_name, args)
                    # Check if it's a library function
                    elif any(func_name in lib for lib in self.libraries.values()):
                        for lib in self.libraries.values():
                            if func_name in lib:
                                result = lib[func_name](*args)
                                break
                    # Built-in function
                    elif func_name == 'number':
                        try:
                            result = float(args[0]) if '.' in str(args[0]) else int(args[0])
                        except ValueError:
                            print(f"Cannot convert {args[0]} to a number")
                            result = 0
                    elif func_name == 'text':
                        result = str(args[0])
                    else:
                        print(f"Unknown function or procedure: {func_name}")
            
            # Parse special syntax for library function call with 'into'
            elif ' into ' in line and not line.startswith('ask'):
                match = re.match(r'(\w+)\((.*?)\)\s+into\s+(\w+)', line)
                if match:
                    func_name = match.group(1)
                    arg_str = match.group(2)
                    var_name = match.group(3)
                    
                    args = [self._parse_expression(arg.strip()) for arg in arg_str.split(',') if arg.strip()]
                    debug_print(f"Library function call with 'into': {func_name}{args} -> {var_name}")
                    
                    # Look for the function in libraries
                    if any(func_name in lib for lib in self.libraries.values()):
                        for lib in self.libraries.values():
                            if func_name in lib:
                                result = lib[func_name](*args)
                                self.variables[var_name] = result
                                break
                    else:
                        print(f"Unknown function: {func_name}")
                
            # Parse return statement
            elif line.startswith('return'):
                result = self._parse_expression(line[6:].strip())
                debug_print(f"Returning value: {result}")
                return result
            
            # Parse try/catch blocks
            elif line.startswith('try'):
                try_idx = i
                done_idx = self._find_matching_done(lines, i)
                catch_idx = None
                
                # Find catch if it exists
                for j in range(try_idx + 1, done_idx):
                    if lines[j].strip() == 'catch':
                        catch_idx = j
                        break
                
                if catch_idx:
                    try:
                        # Execute the try block
                        debug_print("Executing 'try' block")
                        self.parse_and_execute('\n'.join(lines[try_idx+1:catch_idx]))
                    except Exception as e:
                        # Execute the catch block
                        debug_print(f"Exception caught: {e}")
                        self.variables['error'] = str(e)
                        self.parse_and_execute('\n'.join(lines[catch_idx+1:done_idx]))
                
                i = done_idx
            
            i += 1
        
        return result

    def _parse_expression(self, expr):
        """Parse and evaluate a Jules expression"""
        expr = expr.strip()
        debug_print(f"Parsing expression: {expr}")
        
        # String literal
        if expr.startswith('"') and expr.endswith('"'):
            return expr[1:-1]
        
        # Function call
        if '(' in expr and ')' in expr:
            call_match = re.match(r'(\w+)\((.*?)\)', expr)
            if call_match:
                func_name = call_match.group(1)
                arg_str = call_match.group(2)
                args = [self._parse_expression(arg.strip()) for arg in arg_str.split(',') if arg.strip()]
                
                # Check if it's a function call
                if func_name in self.functions:
                    return self._call_function(func_name, args)
                # Check if it's a library function
                elif any(func_name in lib for lib in self.libraries.values()):
                    for lib in self.libraries.values():
                        if func_name in lib:
                            return lib[func_name](*args)
                # Built-in function
                elif func_name == 'number':
                    try:
                        return float(args[0]) if '.' in str(args[0]) else int(args[0])
                    except ValueError:
                        print(f"Cannot convert {args[0]} to a number")
                        return 0
                elif func_name == 'text':
                    return str(args[0])
        
        # Number
        try:
            return int(expr)
        except ValueError:
            try:
                return float(expr)
            except ValueError:
                pass
        
        # Boolean literals
        if expr == 'yes':
            return True
        elif expr == 'no':
            return False
        
        # Variable
        if expr in self.variables:
            return self.variables[expr]
            
        # Access dictionary/thing fields with dot notation
        if '.' in expr and not expr.startswith('.') and not expr.endswith('.'):
            parts = expr.split('.', 1)
            container_name = parts[0].strip()
            field_name = parts[1].strip()
            
            if container_name in self.variables:
                container = self.variables[container_name]
                if isinstance(container, dict) and field_name in container:
                    return container[field_name]
                    
        # Access list items with brackets
        if '[' in expr and ']' in expr:
            match = re.match(r'(\w+)\[(.+?)\]', expr)
            if match:
                list_name = match.group(1)
                index_expr = match.group(2)
                
                if list_name in self.variables:
                    container = self.variables[list_name]
                    index = self._parse_expression(index_expr)
                    if isinstance(container, list) and 0 <= index < len(container):
                        return container[index]
        
        # List literal
        if expr.startswith('[') and expr.endswith(']'):
            if expr == '[]':  # Empty list
                return []
            items = expr[1:-1].split(',')
            return [self._parse_expression(item.strip()) for item in items]
        
        # Dictionary/thing literal
        if expr.startswith('{') and expr.endswith('}'):
            if expr == '{}':  # Empty dictionary
                return {}
            
            # Parse key-value pairs
            items = expr[1:-1].split(',')
            thing = {}
            for item in items:
                if ':' in item:
                    key, value = item.split(':', 1)
                    thing[key.strip()] = self._parse_expression(value.strip())
            return thing
        
        # Addition 
        if '+' in expr:
            parts = expr.split('+', 1)
            left = self._parse_expression(parts[0].strip())
            right = self._parse_expression(parts[1].strip())
            
            # Convert to string if either operand is a string
            if isinstance(left, str) or isinstance(right, str):
                return str(left) + str(right)
            else:
                return left + right
        
        # Handle parentheses grouping
        if expr.startswith('(') and expr.endswith(')'):
            return self._parse_expression(expr[1:-1].strip())
        
        # Subtraction
        if '-' in expr and not expr.startswith('-'):  # Avoid negatives
            parts = expr.split('-', 1)
            left = self._parse_expression(parts[0].strip())
            right = self._parse_expression(parts[1].strip())
            return left - right
        
        # Unary minus (negative numbers)
        if expr.startswith('-'):
            return -self._parse_expression(expr[1:].strip())
        
        # Multiplication
        if 'times' in expr:
            parts = expr.split('times', 1)
            left = self._parse_expression(parts[0].strip())
            right = self._parse_expression(parts[1].strip())
            return left * right
        
        # Division
        if 'divided by' in expr:
            parts = expr.split('divided by', 1)
            left = self._parse_expression(parts[0].strip())
            right = self._parse_expression(parts[1].strip())
            if right == 0:
                print("Warning: Division by zero!")
                return 0
            return left / right
        
        return expr  # Return as is for now
    
    def _evaluate_condition(self, condition):
        """Evaluate a condition expression"""
        condition = condition.strip()
        debug_print(f"Evaluating condition: {condition}")
        
        # Logical AND
        if ' and ' in condition:
            parts = condition.split(' and ', 1)
            left = self._evaluate_condition(parts[0].strip())
            right = self._evaluate_condition(parts[1].strip())
            return left and right
        
        # Logical OR
        if ' or ' in condition:
            parts = condition.split(' or ', 1)
            left = self._evaluate_condition(parts[0].strip())
            right = self._evaluate_condition(parts[1].strip())
            return left or right
        
        # Logical NOT
        if condition.startswith('not '):
            return not self._evaluate_condition(condition[4:].strip())
        
        # String contains
        if ' contains ' in condition:
            parts = condition.split(' contains ', 1)
            left = str(self._parse_expression(parts[0].strip()))
            right = str(self._parse_expression(parts[1].strip()))
            return right in left
        
        # Equal comparison
        if ' is ' in condition and not ' is not ' in condition:
            parts = condition.split(' is ', 1)
            left = self._parse_expression(parts[0].strip())
            right = self._parse_expression(parts[1].strip())
            return left == right
        
        # Not equal comparison
        if ' is not ' in condition:
            parts = condition.split(' is not ', 1)
            left = self._parse_expression(parts[0].strip())
            right = self._parse_expression(parts[1].strip())
            return left != right
        
        # Greater than
        if ' greater than ' in condition:
            parts = condition.split(' greater than ', 1)
            left = self._parse_expression(parts[0].strip())
            right = self._parse_expression(parts[1].strip())
            return left > right
        
        # Less than
        if ' less than ' in condition:
            parts = condition.split(' less than ', 1)
            left = self._parse_expression(parts[0].strip())
            right = self._parse_expression(parts[1].strip())
            return left < right
        
        # Greater than or equal to
        if ' greater than or equal to ' in condition:
            parts = condition.split(' greater than or equal to ', 1)
            left = self._parse_expression(parts[0].strip())
            right = self._parse_expression(parts[1].strip())
            return left >= right
        
        # Less than or equal to
        if ' less than or equal to ' in condition:
            parts = condition.split(' less than or equal to ', 1)
            left = self._parse_expression(parts[0].strip())
            right = self._parse_expression(parts[1].strip())
            return left <= right
        
        # Boolean value
        return bool(self._parse_expression(condition))
    
    def _find_matching_done(self, lines, start_idx):
        """Find the matching 'done' for a block statement"""
        depth = 1
        for i in range(start_idx + 1, len(lines)):
            line = lines[i].strip()
            if not line or line.startswith('#'):
                continue
            if line.startswith(('when', 'repeat', 'make', 'do', 'try', 'while')):
                depth += 1
            elif line == 'done':
                depth -= 1
                if depth == 0:
                    return i
        return len(lines) - 1  # Fallback to end of file
    
    def _find_otherwise(self, lines, start_idx, end_idx):
        """Find the 'otherwise' statement in a when/then block"""
        depth = 1
        for i in range(start_idx + 1, end_idx):
            line = lines[i].strip()
            if not line or line.startswith('#'):
                continue
            if line.startswith('when'):
                depth += 1
            elif line == 'done':
                depth -= 1
            elif (line == 'otherwise' or line.startswith('otherwise when')) and depth == 1:
                return i
        return None
    
    def _call_function(self, func_name, args):
        """Call a Jules function"""
        if func_name not in self.functions:
            raise Exception(f"Function '{func_name}' is not defined")
        
        func = self.functions[func_name]
        if len(args) != len(func['params']):
            raise Exception(f"Function '{func_name}' expects {len(func['params'])} arguments, but got {len(args)}")
        
        debug_print(f"Calling function: {func_name}{args}")
        
        # Save current variables
        old_vars = self.variables.copy()
        
        # Set up function parameters
        for i, param_name in enumerate(func['params']):
            self.variables[param_name] = args[i]
        
        # Execute function body
        result = self.parse_and_execute('\n'.join(func['body']))
        
        # Restore variables
        self.variables = old_vars
        
        return result
    
    def _call_procedure(self, proc_name, args):
        """Call a Jules procedure"""
        if proc_name not in self.procedures:
            raise Exception(f"Procedure '{proc_name}' is not defined")
        
        proc = self.procedures[proc_name]
        if len(args) != len(proc['params']):
            raise Exception(f"Procedure '{proc_name}' expects {len(proc['params'])} arguments, but got {len(args)}")
        
        debug_print(f"Calling procedure: {proc_name}{args}")
        
        # Save current variables
        old_vars = self.variables.copy()
        
        # Set up procedure parameters
        for i, param_name in enumerate(proc['params']):
            self.variables[param_name] = args[i]
        
        # Execute procedure body
        self.parse_and_execute('\n'.join(proc['body']))
        
        # Restore variables
        self.variables = old_vars
    
    def _import_library(self, lib_name):
        """Import a Jules library"""
        if lib_name in self.libraries:
            return  # Already imported
        
        # Check built-in libraries first
        if lib_name == 'drawing':
            try:
                # Try to import the drawing module
                from jules.libs import drawing
                self.libraries['drawing'] = drawing.drawing_functions
                return
            except ImportError:
                try:
                    # For development, try relative path
                    spec = importlib.util.spec_from_file_location("drawing", os.path.join("jules", "libs", "drawing.py"))
                    drawing_module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(drawing_module)
                    self.libraries['drawing'] = drawing_module.drawing_functions
                    return
                except Exception as e:
                    print(f"Could not import drawing library: {e}")
                    return
        
        # Custom libraries would be handled here
        print(f"Library '{lib_name}' not found")


def run_file(filename):
    """Run a Jules program from file"""
    try:
        with open(filename, 'r') as file:
            code = file.read()
        
        # Process the file line by line instead of using the interpreter directly
        lines = code.split('\n')
        interpreter = JulesInterpreter()
        i = 0
        
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines and comments
            if not line or line.startswith('#'):
                i += 1
                continue
            
            # Function definition
            if line.startswith('make'):
                match = re.match(r'make\s+(\w+)\((.*?)\)', line)
                if match:
                    func_name = match.group(1)
                    params = [p.strip() for p in match.group(2).split(',') if p.strip()]
                    
                    # Find the matching done
                    depth = 1
                    done_idx = i
                    for j in range(i + 1, len(lines)):
                        curr_line = lines[j].strip()
                        if not curr_line or curr_line.startswith('#'):
                            continue
                        if curr_line.startswith(('when', 'repeat', 'make', 'do', 'try', 'while')):
                            depth += 1
                        elif curr_line == 'done':
                            depth -= 1
                            if depth == 0:
                                done_idx = j
                                break
                    
                    func_body = lines[i+1:done_idx]
                    
                    if DEBUG:
                        print(f"DEBUG: Defining function {func_name} with parameters {params}")
                    
                    interpreter.functions[func_name] = {
                        'params': params,
                        'body': func_body
                    }
                    
                    i = done_idx + 1  # Skip to after the 'done'
                else:
                    i += 1
                continue
            
            # Execute a single line at a time
            interpreter.parse_and_execute(line)
            i += 1
                
    except FileNotFoundError:
        print(f"Could not find file: {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")
        if DEBUG:
            import traceback
            traceback.print_exc()


def run_interactive():
    """Run Jules in interactive mode"""
    print("Jules Language Interactive Mode")
    print("Type 'exit' to quit")
    
    interpreter = JulesInterpreter()
    buffer = []
    
    while True:
        try:
            if not buffer:
                line = input("jules> ")
            else:
                line = input("... ")
                
            if line.lower() == 'exit':
                break
                
            buffer.append(line)
            
            # Execute when we have a complete block or a simple statement
            if line == 'done' or (not any(line.startswith(kw) for kw in ['when', 'repeat', 'make', 'do', 'try', 'while']) and not buffer[-2:-1] == ['then']):
                code = '\n'.join(buffer)
                try:
                    result = interpreter.parse_and_execute(code)
                    if result is not None and not buffer[-1].startswith('show'):
                        print(result)
                except Exception as e:
                    print(f"Oops! Something went wrong: {e}")
                buffer = []
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_file(sys.argv[1])
    else:
        run_interactive() 