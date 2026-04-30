<h2 class="c-project-heading--task">Use a loop</h2>

Instead of typing out many lines of code, it's easier to use a loop.

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

## Step 1

**Delete the code** you added to make a square. Put the first two lines in a loop.


<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 3
line_highlights: 7-9
---
my_turtle = turtle.Turtle()
my_turtle.speed(4)

# Make a shape
for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)
--- /code ---  
</div>

## Step 2

See what happens when you **run** your code.


<div class="c-project-output">
![square drawn by the turtle in the visual output](images/turtle-loop.png)
</div>

### Debugging

<div class="c-project-callout c-project-callout--debug">

Make sure your code is indented like the example.

</div>

## Now run your code

Run your code and check that the loop draws a square.
