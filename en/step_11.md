## Draw a branch

Write the code to draw one branch of a snowflake.

First define a function called `branch`. Then add code indented inside the `branch` function. This is called at the end with `branch()`.

```python filename="main.py" line_numbers="true" line_number_start="10" line_highlights="16-28"
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
```

## Now run your code

Check that the code draws one snowflake branch.

![single black snowflake branch on a grey background](images/branch.PNG)

> [!DEBUG]
>
> Make sure to check that all your indentation is correct.
