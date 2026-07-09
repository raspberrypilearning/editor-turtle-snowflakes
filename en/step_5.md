## Create different shapes

Replace the code for your square with the following, and experiment to make different shapes.

```python filename="main.py" line_numbers="true" line_number_start="1" line_highlights="7-11"
import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(4)

# Make a shape
for i in range(2):
    my_turtle.forward(100)
    my_turtle.right(60)
    my_turtle.forward(100)
    my_turtle.right(120)
```

## Now run your code

Check that the turtle draws a parallelogram.

![black parallelogram outline with the turtle arrow at the upper-left corner](images/parallelogram.png)
