<h2 class="c-project-heading--task">Changing colours</h2>

So far the turtle has been drawing black lines on a white background.

## Step 1

Set the colour of the turtle in the code. 

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 5
---
import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(4)
my_turtle.color('cyan')

# Make a shape
for i in range(10):
--- /code ---
</div>

## Step 2

Experiment with other colours. 

<div class="c-project-callout c-project-callout--tip">

### Tip

`cyan` is used in the example above, but you can use other colours, including any from this list:

- 'orange'
- 'yellow'
- 'purple'
- 'blue'

Have a look at [this website](https://wiki.tcl.tk/37701) for a complete list.

</div>

## Now run your code

Check that the snowflake is drawn in the colour you chose.

<div class="c-project-output">

![blue snowflake outline on a dotted white canvas](images/step7.png)

</div>



