<h2 class="c-project-heading--task">Use a loop</h2>
--- task ---

Instead of typing out many lines of code, it's easier to use a loop.

--- /task ---

--- task ---

Put it in a loop to create a square.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 3
line_highlights: 5-7
---
my_turtle = turtle.Turtle()

for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)
--- /code ---  
--- task ---
  
See what happens when you **run** your code.

--- /task ---
</div>

<div class="c-project-output">
![square drawn by the turtle in the visual output](images/turtle-loop.png)
</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

Make sure your code is indented like the example.

</div>
