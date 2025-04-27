# Jules Language Quick Reference

## Basic Syntax

### Output to screen
```jules
show "Hello, World!"
```

### Variables
```jules
name is "Alice"
age is 25
```

### String concatenation
```jules
# Text + Text
show "Hello, " + name

# Text + Number (needs text() conversion)
show "Age: " + text(age)
```

### Numbers and calculations
```jules
x is 10
y is 5
sum is x + y
show "Sum: " + text(sum)  # Must convert numbers to text for display
```

### Conditions
```jules
when age less than 18 then
    show "You are under 18"
otherwise
    show "You are 18 or older"
done
```

### Loops
```jules
repeat 5 times
    show "Count: " + text(count)
done
```

## Working Script Examples

### Example 1: Basic variables and display
```jules
show "Jules in VS Code"

name is "Student"
show "Hello, " + name

age is "25"
show "Your age is: " + age
```

### Example 2: Number calculations
```jules
# Set age as text
age is "25"

# Convert to number for calculation
age_num is number(age)
future_age is age_num + 10
show "In 10 years you'll be: " + text(future_age)
```

## Common Issues

1. **String Concatenation with Numbers**
   
   When using `show` with numbers, you must convert them to text:
   ```jules
   # WRONG - Will not work
   show "Age: " + age
   
   # CORRECT - Convert number to text
   show "Age: " + text(age)
   ```

2. **The `ask` Command**
   
   The `ask` command may not work in some environments:
   ```jules
   # Instead of:
   ask "What is your name?" into name
   
   # Use direct assignment:
   name is "Alice"
   ```

3. **Comments**
   
   Comments must be on their own line, not at the end of code lines:
   ```jules
   # This is a comment
   name is "Alice"  # This will cause errors!
   ```

4. **Variable Types**
   
   Variables can store different types:
   ```jules
   # Store as text
   age_text is "25"
   
   # Store as number
   age_num is 25
   
   # Convert between types
   age_from_text is number(age_text)
   age_to_text is text(age_num)
   ```

## Debugging

If your Jules script isn't working as expected:

1. Run it with the debug_runner.py: `python debug_runner.py your_script.jules`
2. Make sure string concatenation uses text() for numbers
3. Keep comments on separate lines
4. Avoid complex expressions - break them into simpler steps
5. Check the Jules sample script for correct syntax examples 