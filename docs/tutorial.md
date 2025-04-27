# Jules Language Tutorial

Welcome to Jules, a friendly programming language designed to be easy to read and understand. This tutorial will walk you through the basics of programming with Jules.

## Getting Started

To run a Jules program, use the interpreter:

```bash
python jules.py your_program.jules
```

Or start an interactive session:

```bash
python jules.py
```

## Hello World

Let's start with a simple program:

```jules
show "Hello, World!"
```

The `show` command displays text on the screen.

## Variables

Jules uses the `is` keyword to create and set variables:

```jules
name is "Jules"
age is 7
is_cool is yes
```

## Data Types

Jules has several data types:

### Numbers

```jules
whole_number is 42
decimal_number is 3.14
```

### Text (Strings)

```jules
greeting is "Hello there!"
```

### Boolean (Yes/No)

```jules
is_raining is yes
is_sunny is no
```

### Lists

```jules
fruits is ["apple", "banana", "cherry"]
numbers is [1, 2, 3, 4, 5]
```

### Things (Dictionaries)

```jules
person is {name: "Jules", age: 7, likes_coding: yes}
```

## Input and Output

### Output with `show`

```jules
show "Hello!"
show "The answer is " + 42
show person
```

### Input with `ask`

```jules
ask "What is your name?" into name
show "Hello, " + name
```

## Operators

### Arithmetic

```jules
sum is 5 + 3          # Addition
difference is 10 - 2   # Subtraction
product is 4 times 3   # Multiplication
quotient is 10 divided by 2  # Division
```

### Comparison

```jules
5 is 5              # Equal to
5 is not 10         # Not equal to
7 greater than 3    # Greater than
2 less than 9       # Less than
```

### Logical

```jules
yes and yes     # Logical AND
no or yes       # Logical OR
not yes         # Logical NOT
```

## Control Structures

### Conditionals

```jules
when age greater than 18 then
    show "You are an adult"
otherwise
    show "You are a child"
done
```

Multiple conditions:

```jules
when grade is "A" then
    show "Excellent!"
otherwise when grade is "B" then
    show "Good job!"
otherwise when grade is "C" then
    show "Fair"
otherwise
    show "Keep trying"
done
```

### Loops

#### Repeat a fixed number of times:

```jules
repeat 5 times
    show "Count: " + count
done
```

The `count` variable is automatically provided in `repeat times` loops.

#### Repeat for each item in a collection:

```jules
fruits is ["apple", "banana", "cherry"]
repeat each fruit in fruits
    show "I like " + fruit
done
```

#### While loops:

```jules
number is 1
while number less than 5
    show number
    number is number + 1
done
```

## Functions and Procedures

### Functions (return a value)

```jules
make square(x)
    return x times x
done

result is square(5)
show result  # Shows 25
```

### Procedures (don't return a value)

```jules
do greet(name)
    show "Hello, " + name + "!"
done

greet("Jules")  # Shows "Hello, Jules!"
```

## Error Handling

```jules
try
    # Code that might cause an error
    result is 10 divided by 0
catch
    show "An error occurred!"
    show error  # Shows the error message
done
```

## Advanced Examples

### Calculate Factorial

```jules
make factorial(n)
    when n is 0 then
        return 1
    otherwise
        return n times factorial(n - 1)
    done
done

show factorial(5)  # Shows 120
```

### Todo List Application

```jules
todos is []

do add_todo(item)
    todos is todos + [item]
    show "Added: " + item
done

do list_todos()
    when todos is [] then
        show "No todos yet!"
    otherwise
        show "Todo List:"
        repeat each todo in todos
            show "- " + todo
        done
    done
done

do main()
    running is yes
    while running
        show "1. Add todo"
        show "2. List todos"
        show "3. Exit"
        
        ask "Choose an option: " into choice
        
        when choice is "1" then
            ask "Enter a todo item: " into item
            add_todo(item)
        otherwise when choice is "2" then
            list_todos()
        otherwise when choice is "3" then
            running is no
            show "Goodbye!"
        otherwise
            show "Invalid choice. Try again."
        done
    done
done

main()  # Start the program
```

## Next Steps

Now that you know the basics of Jules, try:

1. Modifying the examples
2. Creating your own programs
3. Exploring the provided examples in the `examples` folder

Remember, programming in Jules should be fun and easy to understand, just like having a conversation with your computer! 