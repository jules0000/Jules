"""
Jules Drawing Library

A simple wrapper for Python's turtle module that can be used in Jules programs.
"""

import turtle
from functools import wraps

# Store all created turtles
turtles = {}
turtle_count = 0

def jules_function(func):
    """Decorator for Jules library functions to handle errors gracefully"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Oops! {e}")
            return None
    return wrapper

@jules_function
def create_turtle():
    """Create a new turtle and return its ID"""
    global turtle_count
    turtle_count += 1
    turtle_id = f"turtle_{turtle_count}"
    turtles[turtle_id] = turtle.Turtle()
    return turtle_id

@jules_function
def move_forward(turtle_id, distance):
    """Move the turtle forward by the specified distance"""
    if turtle_id in turtles:
        turtles[turtle_id].forward(distance)
    else:
        print(f"Turtle {turtle_id} not found")

@jules_function
def move_backward(turtle_id, distance):
    """Move the turtle backward by the specified distance"""
    if turtle_id in turtles:
        turtles[turtle_id].backward(distance)
    else:
        print(f"Turtle {turtle_id} not found")

@jules_function
def turn_right(turtle_id, angle):
    """Turn the turtle right by the specified angle"""
    if turtle_id in turtles:
        turtles[turtle_id].right(angle)
    else:
        print(f"Turtle {turtle_id} not found")

@jules_function
def turn_left(turtle_id, angle):
    """Turn the turtle left by the specified angle"""
    if turtle_id in turtles:
        turtles[turtle_id].left(angle)
    else:
        print(f"Turtle {turtle_id} not found")

@jules_function
def pen_up(turtle_id):
    """Lift the pen so the turtle doesn't draw"""
    if turtle_id in turtles:
        turtles[turtle_id].penup()
    else:
        print(f"Turtle {turtle_id} not found")

@jules_function
def pen_down(turtle_id):
    """Lower the pen so the turtle draws when it moves"""
    if turtle_id in turtles:
        turtles[turtle_id].pendown()
    else:
        print(f"Turtle {turtle_id} not found")

@jules_function
def set_pen_color(turtle_id, color):
    """Set the pen color"""
    if turtle_id in turtles:
        turtles[turtle_id].pencolor(color)
    else:
        print(f"Turtle {turtle_id} not found")

@jules_function
def set_fill_color(turtle_id, color):
    """Set the fill color"""
    if turtle_id in turtles:
        turtles[turtle_id].fillcolor(color)
    else:
        print(f"Turtle {turtle_id} not found")

@jules_function
def set_speed(turtle_id, speed):
    """Set the turtle's speed (1-10 or 'slowest', 'slow', 'normal', 'fast', 'fastest')"""
    speeds = {
        "slowest": 1,
        "slow": 3,
        "normal": 6,
        "fast": 8,
        "fastest": 0
    }
    
    speed_value = speeds.get(speed, speed)
    
    if turtle_id in turtles:
        turtles[turtle_id].speed(speed_value)
    else:
        print(f"Turtle {turtle_id} not found")

@jules_function
def begin_fill(turtle_id):
    """Begin filling a shape"""
    if turtle_id in turtles:
        turtles[turtle_id].begin_fill()
    else:
        print(f"Turtle {turtle_id} not found")

@jules_function
def end_fill(turtle_id):
    """End filling a shape"""
    if turtle_id in turtles:
        turtles[turtle_id].end_fill()
    else:
        print(f"Turtle {turtle_id} not found")

@jules_function
def clear_screen():
    """Clear the screen"""
    turtle.clear()

@jules_function
def hide_turtle(turtle_id):
    """Hide the turtle"""
    if turtle_id in turtles:
        turtles[turtle_id].hideturtle()
    else:
        print(f"Turtle {turtle_id} not found")

@jules_function
def show_turtle(turtle_id):
    """Show the turtle"""
    if turtle_id in turtles:
        turtles[turtle_id].showturtle()
    else:
        print(f"Turtle {turtle_id} not found")

@jules_function
def goto(turtle_id, x, y):
    """Move turtle to the specified position"""
    if turtle_id in turtles:
        turtles[turtle_id].goto(x, y)
    else:
        print(f"Turtle {turtle_id} not found")

@jules_function
def set_pen_size(turtle_id, width):
    """Set the pen's width"""
    if turtle_id in turtles:
        turtles[turtle_id].pensize(width)
    else:
        print(f"Turtle {turtle_id} not found")

@jules_function
def draw_circle(turtle_id, radius):
    """Draw a circle with the specified radius"""
    if turtle_id in turtles:
        turtles[turtle_id].circle(radius)
    else:
        print(f"Turtle {turtle_id} not found")

@jules_function
def write_text(turtle_id, text, font_size=12):
    """Write text at the current position"""
    if turtle_id in turtles:
        turtles[turtle_id].write(text, font=("Arial", font_size, "normal"))
    else:
        print(f"Turtle {turtle_id} not found")

@jules_function
def setup(width=800, height=600):
    """Set up the drawing window size"""
    turtle.setup(width, height)

@jules_function
def title(title_text):
    """Set the window title"""
    turtle.title(title_text)

@jules_function
def done():
    """Finish drawing and keep the window open"""
    turtle.done()

# Register functions in a dictionary for easy import to Jules
drawing_functions = {
    "create_turtle": create_turtle,
    "move_forward": move_forward,
    "move_backward": move_backward,
    "turn_right": turn_right,
    "turn_left": turn_left,
    "pen_up": pen_up,
    "pen_down": pen_down,
    "set_pen_color": set_pen_color,
    "set_fill_color": set_fill_color,
    "set_speed": set_speed,
    "begin_fill": begin_fill,
    "end_fill": end_fill,
    "clear_screen": clear_screen,
    "hide_turtle": hide_turtle,
    "show_turtle": show_turtle,
    "goto": goto,
    "set_pen_size": set_pen_size,
    "draw_circle": draw_circle,
    "write_text": write_text,
    "setup": setup,
    "title": title,
    "done": done
} 