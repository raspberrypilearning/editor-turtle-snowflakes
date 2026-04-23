<h2 class="c-project-heading--task">Loops in loops</h2>

You can put loops inside of other loops to repeat and overlap shapes.

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

## Step 1

Add an outer loop in the line above `for i in range(2):`. 


<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 3
line_highlights: 7-13
---
my_turtle = turtle.Turtle()
my_turtle.speed(4)

# Make a shape
for i in range(10):
    for i in range(2):
        my_turtle.forward(100)
        my_turtle.right(60)
        my_turtle.forward(100)
        my_turtle.right(120)
    my_turtle.right(36)
--- /code --- 
</div>

## Step 2

**Run** your code to see what happens. You should see a drawing like this:  
  

<div class="c-project-output">

![ADD TEXT](images/snowflake1.png)
</div>

  
### Tip

<div class="c-project-callout c-project-callout--tip">

Make sure to indent the code below a loop.

</div>

## Now run your code

Confirm the observable result.
