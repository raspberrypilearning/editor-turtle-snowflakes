<h2 class="c-project-heading--task">Use a loop</h2>

Instead of typing out many lines of code, it's easier to use a loop.

## Step 1

**Delete the code** you added to make a square. 

## Step 2

Put the first two lines in a loop with `range(4)`.

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
for i in :
    my_turtle.forward(100)
    my_turtle.right(90)
--- /code ---  
</div>

## Now run your code

Check that the loop draws a square.

<div class="c-project-output">

![black square outline with the turtle arrow at the top-left corner](images/turtle-loop.png)

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

Make sure your code is indented like the example.

</div>


