<h2 class="c-project-heading--task">Add a random colour</h2>

Add the code so that every time you run your code, you will get a slightly different snowflake.

## Step 1

First import the `random` library. 

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 2
---
import turtle
import random

my_turtle = turtle.Turtle()
--- /code ---
</div>

## Step 2

Then create a list called `colours` to store colours to select from.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 7
line_highlights: 8
---
turtle.Screen().bgcolor('grey')
colours = ['cyan', 'purple', 'white', 'blue']

# Make a shape
for i in range(10):
--- /code ---
</div>

## Step 3

At the end of the loop, choose a random colour from the list.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 10
line_highlights: 18
---
# Make a shape
for i in range(10):
    for i in range(2):
        my_turtle.forward(100)
        my_turtle.right(60)
        my_turtle.forward(100)
        my_turtle.right(120)
    my_turtle.right(36)
    my_turtle.color(random.choice(colours))
--- /code ---
</div>

## Now run your code

Check that different parts of the snowflake use colours from your list.

<div class="c-project-output">

![snowflake outline in cyan, purple, and blue on a grey background](images/colour-list.png)
</div>