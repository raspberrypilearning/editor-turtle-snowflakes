## Use a loop

Instead of typing out many lines of code, it's easier to use a loop.

## Step 1

**Delete the code** you added to make a square.

## Step 2

Put the first two lines in a loop with `range(4)`.

```python filename="main.py" line_numbers="true" line_number_start="3" line_highlights="7-9"
my_turtle = turtle.Turtle()
my_turtle.speed(4)

# Make a shape
for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)
```

## Now run your code

Check that the loop draws a square.

![black square outline with the turtle arrow at the top-left corner](images/turtle-loop.png)

> [!DEBUG]
>
> Make sure your code is indented like the example.
