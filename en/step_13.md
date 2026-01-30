<h2 class="c-project-heading--task">STEP TITLE</h2>
--- task ---

BRIEF SUMMARY OF STEP - one line

--- /task ---
## Using a function to draw a snowflake

Your parallelogram snowflake is cool, but it does not look as snowflake-like as it could. Let's fix that!

For this drawing, we need to move the turtle from the centre of the window. The `penup()` and `pendown()` instructions let us do this without drawing a line, just like picking up a real pen from the paper and moving it somewhere else to start writing.

--- task ---

Add the following instructions below the `colours` list:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 5
line_highlights: 7-10
---
colours = ["cyan", "purple", "white", "blue"]

elsa.penup()
elsa.forward(90)
elsa.left(45)
elsa.pendown()

elsa.color("cyan")
--- /code ---

--- /task --- 
  