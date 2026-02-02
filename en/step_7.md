<h2 class="c-project-heading--task">Loops in loops</h2>
--- task ---

You can put loops inside of other loops to repeat and overlap shapes.

--- /task ---

--- task ---

Add another loop in the line above `for i in range(2):`. 

--- /task ---

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 3
line_highlights: 5-11
---
my_turtle = turtle.Turtle()

for i in range(10):
    for i in range(2):
        my_turtle.forward(100)
        my_turtle.right(60)
        my_turtle.forward(100)
        my_turtle.right(120)
    my_turtle.right(36)
--- /code --- 

--- task ---

**Run** your code to see what happens. You should see a drawing like this:  
  
--- /task ---
</div>

<div class="c-project-output">

![ADD TEXT](images/snowflake1.png)
</div>

  
<div class="c-project-callout c-project-callout--tip">

### Tip

Make sure to indent the code below a loop.

</div>



