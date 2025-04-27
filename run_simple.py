#!/usr/bin/env python3
"""
Simple Jules interpreter for demonstration
"""

import sys

def run_simple_jules(filename):
    """Run a simplified version of Jules language"""
    try:
        with open(filename, 'r') as file:
            lines = file.read().splitlines()
        
        variables = {}
        
        for line in lines:
            line = line.strip()
            
            # Skip empty lines and comments
            if not line or line.startswith('#'):
                continue
            
            # Simple show command
            if line.startswith('show '):
                value = line[5:].strip()
                result = evaluate_expression(value, variables)
                print(result)
            
            # Simple variable assignment
            elif ' is ' in line:
                parts = line.split(' is ', 1)
                var_name = parts[0].strip()
                value = parts[1].strip()
                
                # Evaluate the expression on the right side
                variables[var_name] = evaluate_expression(value, variables)
    
    except FileNotFoundError:
        print(f"Could not find file: {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

def evaluate_expression(expr, variables):
    """Evaluate a Jules expression"""
    # Handle parenthesized expressions first
    if expr.startswith('(') and expr.endswith(')'):
        expr = expr[1:-1].strip()
    
    # Handle string literals
    if expr.startswith('"') and expr.endswith('"'):
        return expr[1:-1]  # Remove quotes
    
    # Handle boolean literals
    if expr == 'yes':
        return True
    if expr == 'no':
        return False
    
    # Handle variable references
    if expr in variables:
        return variables[expr]
    
    # Handle numeric literals
    if expr.isdigit():
        return int(expr)
    
    # Handle string concatenation and arithmetic operations
    if ' + ' in expr:
        parts = expr.split(' + ', 1)
        left = evaluate_expression(parts[0].strip(), variables)
        right = evaluate_expression(parts[1].strip(), variables)
        
        # String concatenation if either is a string
        if isinstance(left, str) or isinstance(right, str):
            return str(left) + str(right)
        else:
            return left + right
    
    # Handle subtraction
    if ' - ' in expr:
        parts = expr.split(' - ', 1)
        left = evaluate_expression(parts[0].strip(), variables)
        right = evaluate_expression(parts[1].strip(), variables)
        return left - right
    
    # Handle multiplication
    if ' * ' in expr:
        parts = expr.split(' * ', 1)
        left = evaluate_expression(parts[0].strip(), variables)
        right = evaluate_expression(parts[1].strip(), variables)
        return left * right
    
    # Handle division
    if ' / ' in expr:
        parts = expr.split(' / ', 1)
        left = evaluate_expression(parts[0].strip(), variables)
        right = evaluate_expression(parts[1].strip(), variables)
        if right == 0:
            print("Warning: Division by zero!")
            return 0
        return left / right
    
    # Handle comparison operations
    if ' > ' in expr:
        parts = expr.split(' > ', 1)
        left = evaluate_expression(parts[0].strip(), variables)
        right = evaluate_expression(parts[1].strip(), variables)
        return left > right
    
    if ' < ' in expr:
        parts = expr.split(' < ', 1)
        left = evaluate_expression(parts[0].strip(), variables)
        right = evaluate_expression(parts[1].strip(), variables)
        return left < right
    
    if ' == ' in expr:
        parts = expr.split(' == ', 1)
        left = evaluate_expression(parts[0].strip(), variables)
        right = evaluate_expression(parts[1].strip(), variables)
        return left == right
    
    # If we get here and can't parse, return the expression as is
    return expr

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(f"Running simple Jules: {sys.argv[1]}")
        run_simple_jules(sys.argv[1])
    else:
        print("Please provide a Jules file to run.")
        print("Example: python run_simple.py examples/hello.jules") 