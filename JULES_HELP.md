# Jules Language Guide

Jules is a beginner-friendly programming language designed to be readable, simple, and close to natural English. This guide will help you understand how to use Jules and address common issues.

## Table of Contents
- [Basic Syntax](#basic-syntax)
- [Working with Variables](#working-with-variables)
- [String Operations](#string-operations)
- [Numbers and Math](#numbers-and-math)
- [Control Structures](#control-structures)
- [Using the Ask Command](#using-the-ask-command)
- [Common Issues and Solutions](#common-issues-and-solutions)
- [Examples](#examples)

## Basic Syntax

### Output text to the screen
```jules
show "Hello World!"
```

### Comments
```jules
# This is a comment
# Comments must be on their own line
```

## Working with Variables

### Assigning variables
```jules
name is "Alice"
age is 25
is_student is yes  # Boolean true
```

### Using variables
```jules
show name
show age
```

## String Operations

### String concatenation
```jules
first_name is "John"
last_name is "Doe"

# Concatenate strings
full_name is first_name + " " + last_name
show full_name  # Shows "John Doe"
```

### Important: When concatenating with numbers
```jules
age is 25

# WRONG - Will not work correctly
show "Age: " + age

# CORRECT - Convert number to text first
show "Age: " + text(age)
```

## Numbers and Math

### Numeric variables
```jules
x is 10
y is 5

# Basic operations
sum is x + y        # 15
difference is x - y # 5
product is x * y    # 50
quotient is x / y   # 2
```

### Converting between types
```jules
# String to number
age_text is "25"
age_number is number(age_text)  # Converts to 25

# Number to string
count is 10
count_text is text(count)  # Converts to "10"
```

## Control Structures

### Conditionals
```jules
age is 16

when age less than 18 then
    show "You are under 18"
otherwise
    show "You are 18 or older"
done
```

### Loops
```jules
# Repeat a fixed number of times
repeat 5 times
    show "Count: " + text(count)
done

# Iterate over items
names is ["Alice", "Bob", "Charlie"]
repeat each person in names
    show "Hello, " + person
done

# While loop
number is 1
while number less than 5
    show text(number)
    number is number + 1
done
```

## Using the Ask Command

The `ask` command lets you get input from the user:

```jules
# Ask for input and store in variable
ask "What is your name?" into name
show "Hello, " + name

ask "How old are you?" into age
age_number is number(age)
show "Next year you will be " + text(age_number + 1)
```

**Note**: If you get an error with the `ask` command, use the special `jules_runner.py` script to run your program:
```
python jules_runner.py your_script.jules
```

## Common Issues and Solutions

### 1. String concatenation with numbers
If you see errors or unexpected output with string concatenation, make sure to convert numbers to text:
```jules
age is 25
# CORRECT:
show "Age: " + text(age)
```

### 2. Comments at end of lines
Jules does not support comments at the end of code lines:
```jules
# WRONG:
name is "Alice"  # This is a user name

# CORRECT:
# This is a user name
name is "Alice"
```

### 3. Import errors in external folders
If you see "Import jules.core.interpreter could not be resolved" in an external folder, use:
```
python jules_runner.py your_file.jules
```

## Examples

### Simple greeting program
```jules
# Ask for user's name
ask "What is your name?" into name

# Say hello
show "Hello, " + name
show "Welcome to Jules!"

# Ask for age
ask "How old are you?" into age
age_number is number(age)

# Show different messages based on age
when age_number less than 18 then
    show "You are quite young!"
otherwise
    show "You are an adult!"
done

show "Thank you for using Jules!"
```

### Number guessing game
```jules
# Simple number guessing game
secret is 42
guesses is 0
guessed is no

show "I'm thinking of a number between 1 and 100"

while guessed is no
    ask "What's your guess?" into guess
    guess_number is number(guess)
    guesses is guesses + 1
    
    when guess_number is secret then
        show "Correct! You got it in " + text(guesses) + " tries!"
        guessed is yes
    otherwise when guess_number less than secret then
        show "Too low, try again"
    otherwise
        show "Too high, try again"
    done
done
```

---

For more examples, check the `examples/` folder in the Jules language directory. 
