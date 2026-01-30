

<h2 class="c-project-heading--task">STEP TITLE</h2>
--- task ---

BRIEF SUMMARY OF STEP - one line

--- /task ---




--- task ---



At the end of the loop, below `elsa.right(36)`, choose a random colour

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 10
line_highlights: 17
---
for i in range(10):
    for i in range(2):
        elsa.forward(100)
        elsa.right(60)
        elsa.forward(100)
        elsa.right(120)
    elsa.right(36)
    elsa.color(random.choice(colours))
--- /code ---

**Note**: make sure this line is also indented, so that your program knows it's within the loop.

--- /task ---

--- task ---

Save and run your code for a multi-coloured snowflake!

![](images/colour-list.png)

--- /task ---


--- collapse ---
---
title: More colours
---

There are a lot more colours you can choose from! Have a look at [this website](https://wiki.tcl.tk/37701) for a complete list.

--- /collapse ---
