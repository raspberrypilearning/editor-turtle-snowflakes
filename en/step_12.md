<h2 class="c-project-heading--task">Draw a branch</h2>
--- task ---

Write the code to draw one branch of a snowflake.

--- /task ---

--- task ---

First define a function called `branch`.

--- /task ---

--- task ---

Add code indented inside the `branch` function. This is called at the end with `branch()`.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 10
line_highlights: 16-28
---
# Make a shape
my_turtle.penup()
my_turtle.forward(90)
my_turtle.left(45)
my_turtle.pendown()

def branch():
    for i in range(3):
        for i in range(3):
            my_turtle.forward(30)
            my_turtle.backward(30)
            my_turtle.right(45)
        my_turtle.left(90)
        my_turtle.backward(30)
        my_turtle.left(45)
    my_turtle.right(90)
    my_turtle.forward(90)

branch()
--- /code ---
</div>

--- task ---

**Test:** click run and try it out.

--- /task ---  

![branch](images/branch.PNG)
  
<div class="c-project-callout c-project-callout--debug">

### Debugging

Make sure to check that all your indentation is correct.

</div>

