<h2 class="c-project-heading--task">Make a snowflake</h2>
--- task ---

Make a new shape that looks like a snowflake.

--- /task ---


--- task ---

To start drawing at the side of the screen add `penup()` and `pendown()` to your code.

--- /task ---

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 10-13
---
import turtle
import random

my_turtle = turtle.Turtle()
my_turtle.speed(20)
my_turtle.color('blue')
turtle.Screen().bgcolor('grey')

colours = ["cyan", "purple", "white", "blue"]

my_turtle.penup()
my_turtle.forward(90)
my_turtle.left(45)
my_turtle.pendown()
--- /code ---
--- task ---

**Run** your code and check the pen moves.

--- /task --- 
  