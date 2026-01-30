

  <h2 class="c-project-heading--task">STEP TITLE</h2>
--- task ---

BRIEF SUMMARY OF STEP - one line

--- /task ---
Write the code to draw one branch of a snowflake, and store it inside a **function**. Then you can simply repeat it over and over to create a complete snowflake.

![branch](images/branch.PNG)

--- task ---

Define a function called `branch` by typing: 

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 12
line_highlights: 15
---
elsa.color("cyan")
turtle.Screen().bgcolor("grey")

def branch():
--- /code ---

--- /task ---

--- task ---

Remove the code for the parallelogram snowflake loops. Add the following code indented inside the `branch` function:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 15
line_highlights: 16-25
---
def branch():
    for i in range(3):
        for i in range(3):
            elsa.forward(30)
            elsa.backward(30)
            elsa.right(45)
        elsa.left(90)
        elsa.backward(30)
        elsa.left(45)
    elsa.right(90)
    elsa.forward(90)
--- /code ---

--- /task ---  

  
**Note**: Remember that indentation is important. Make sure to check that all your indentation is correct, otherwise your code won't work!

--- task ---
