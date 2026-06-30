<h2 class="c-project-heading--task">Make the turtle move</h2>

Start by adding this code to draw the first line.

<div class="c-project-code">

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 6-7
---
import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(4)

# Make a shape
my_turtle.forward(100)
--- /code ---
</div>

## Now run your code

Check that the line the turtle draws. Change the **forward** number to make it longer or shorter. 

<div class="c-project-output">

![black turtle line pointing right on a dotted white canvas](images/import-turtle.png)
</div>


<div class="c-project-callout c-project-callout--tip">

### Tip

Edit the **speed** number in the starter code to make the turtle draw faster or slower. 

</div>

