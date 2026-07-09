## Set the background

Change the colour of the background by adding the code below. You can experiment with other colours.

```python filename="main.py" line_numbers="true" line_number_start="1" line_highlights="6"
import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(4)
my_turtle.color('cyan')
turtle.Screen().bgcolor('grey')

# Make a shape
for i in range(10):
```

## Now run your code

Check that the snowflake is drawn on a new background colour.

Here is an example of the snowflake on a grey background.

![cyan snowflake outline on a grey background](images/step8.png)
