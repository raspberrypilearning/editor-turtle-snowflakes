<h2 class="c-project-heading--task">STEP TITLE</h2>
--- task ---

Use a loop to create a square.

--- /task ---


<h2 class="c-project-heading--explainer">Using loops to create shapes</h2>

To create a square, you have repeated some lines of code. Instead of typing out many lines of code, it's easier to use a loop.


--- task ---

Edit your code, put it in a loop to create a square.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 5-7
---
import turtle

my_turtle = turtle.Turtle()

for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)
--- /code ---  
--- task ---
  
Try and see what happens when you run your code.

--- /task ---
</div>

![square drawn by the turtle in the visual output](images/turtle-loop.png)
</div>

