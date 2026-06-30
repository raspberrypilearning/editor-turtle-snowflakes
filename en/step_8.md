<h2 class="c-project-heading--task">Set the background</h2>

Change the colour of the background by adding the code below. You can experiment with other colours. 

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 6
---
import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(4)
my_turtle.color('cyan')
turtle.Screen().bgcolor('grey')

# Make a shape
for i in range(10):
--- /code ---
</div>

## Now run your code

Check that the snowflake is drawn on a new background colour.


<div class="c-project-output">
Here is an example of the snowflake on a grey background

![cyan snowflake outline on a grey background](images/step8.png)

</div>
