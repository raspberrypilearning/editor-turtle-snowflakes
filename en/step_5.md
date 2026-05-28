<h2 class="c-project-heading--task">Create different shapes</h2>

Replace the code for your square with the following, and experiment to make different shapes.

## Step 1

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 7-11
---
import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(4)

# Make a shape
for i in range(2):
    my_turtle.forward(100)
    my_turtle.right(60)
    my_turtle.forward(100)
    my_turtle.right(120)
--- /code --- 
</div>

## Step 2

Run the code and it will draw a shape called a parallelogram.
  

<div class="c-project-output">
 ![ADD TEXT](images/parallelogram.png)
</div>

## Now run your code

Run your code and check that the turtle draws a parallelogram.
