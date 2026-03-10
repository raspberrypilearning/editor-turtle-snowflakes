<h2 class="c-project-heading--task">Make a snowflake</h2>
--- task ---

Make a new shape that looks like a snowflake.

--- /task ---


--- task ---

**Delete the code** from the previous shape you made.

--- /task ---

--- task ---

Start a **new shape** by drawing at the side of the screen add `penup()` and `pendown()` to your code.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 11-14
---
import turtle
import random

my_turtle = turtle.Turtle()
my_turtle.speed(4)
my_turtle.color('blue')
turtle.Screen().bgcolor('grey')
colours = ["cyan", "purple", "white", "blue"]

# Make a shape
my_turtle.penup()
my_turtle.forward(90)
my_turtle.left(45)
my_turtle.pendown()
--- /code ---
</div>
--- task ---

**Run** your code and check the pen moves.

--- /task --- 
  
