# Jules Language Specification

Jules is a programming language designed to be beginner-friendly, with syntax that closely resembles natural English.

## 1. Syntax Overview

Jules uses minimal punctuation and avoids symbols that might confuse beginners:
- No semicolons (`;`) to end statements
- No parentheses (`()`) unless absolutely necessary (e.g., for function calls)
- No curly braces (`{}`) for blocks
- Blocks are marked with keywords (`then`/`done`) rather than indentation alone

## 2. Data Types

### Primitive Types
- `number`: Integers and floating-point numbers (7, 3.14)
- `text`: Text strings ("Hello world")
- `yes`/`no`: Boolean values (true/false)

### Complex Types
- `list`: Ordered collections of items ([1, 2, 3])
- `thing`: Key-value pairs, similar to dictionaries ({name: "Jules", age: 7})

## 3. Variables

Variables are declared and assigned with the `is` keyword:

```jules
name is "Jules"
age is 7
```

## 4. Operators

### Arithmetic Operators
- Addition: `+`
- Subtraction: `-`
- Multiplication: `times`
- Division: `divided by`

### Comparison Operators
- Equal: `is`
- Not equal: `is not`
- Greater than: `greater than`
- Less than: `less than`
- Greater than or equal: `greater than or equal to`
- Less than or equal: `less than or equal to`

### Logical Operators
- And: `and`
- Or: `or`
- Not: `not`

## 5. Control Structures

### Conditionals

```jules
when condition then
    # code to execute when condition is true
otherwise
    # code to execute when condition is false
done
```

Multiple conditions:

```jules
when condition1 then
    # code for condition1
otherwise when condition2 then
    # code for condition2
otherwise
    # default code
done
```

### Loops

Repeat a fixed number of times:

```jules
repeat 5 times
    # code to repeat
done
```

Iterate over a collection:

```jules
repeat each item in collection
    # code to execute for each item
done
```

While loop:

```jules
while condition
    # code to repeat while condition is true
done
```

### Loop Control
- `stop`: Exit the current loop (like break)
- `skip`: Skip to the next iteration (like continue)

## 6. Functions and Procedures

Functions (return values):

```jules
make function_name(param1, param2)
    # function body
    return value
done
```

Procedures (no return values):

```jules
do procedure_name(param1, param2)
    # procedure body
done
```

## 7. Input and Output

### Output
Display text to the user:

```jules
show "Hello, World!"
```

### Input
Get input from the user:

```jules
ask "What is your name?" into name
```

## 8. Error Handling

```jules
try
    # code that might cause an error
catch
    # code to execute if an error occurs
done
```

## 9. Comments

Comments start with `#` and continue to the end of the line:

```jules
# This is a comment
name is "Jules"  # This is also a comment
```

## 10. Standard Library

- `text`: String manipulation functions
- `numbers`: Mathematical functions
- `lists`: List operations
- `time`: Date and time functions
- `files`: File input/output operations
- `drawing`: Simple graphics

## 11. Importing Libraries

```jules
get library_name
```

## 12. File Extensions

Jules files use the `.jules` extension. 