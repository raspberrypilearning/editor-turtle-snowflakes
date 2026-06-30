<h2 class="c-project-heading--task">Repeat to make the snowflake</h2>

Put `branch()` in a loop so that it draws it eight times.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 24
line_highlights: 28-30
---
    my_turtle.right(90)
    my_turtle.forward(90)

for i in range(8):
    branch()
    my_turtle.left(45)
--- /code ---
</div>

## Now run your code

Check that eight branches join together to make a full snowflake.

<div class="c-project-output">
 
![cyan eight-branch snowflake on a grey background](images/snowflake2.png)

</div>



