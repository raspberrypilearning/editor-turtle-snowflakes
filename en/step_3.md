<h2 class="c-project-heading--task">Turn your turtle</h2>
--- task ---

To draw shapes add code that **turns** `my_turtle`.
 
--- /task ---


<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 8
---
import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(4)

# Make a shape
my_turtle.forward(100)
my_turtle.right(90)

--- /code ---

--- task ---

Click on **Run** to run the Turtle program. Experiment with `right` and `left` to change the direction. Change the number to turn more or less.

--- /task ---
</div>


<div class="c-project-callout c-project-callout--tip">

### Tip

The value `90` inside the brackets is in degrees. So this line is telling your turtle to turn right by 90 degrees.

</div>
