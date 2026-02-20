import turtle
import random

my_turtle = turtle.Turtle()
turtle.Screen().bgcolor("grey")
turtle.speed(1)
colours = ["cyan", "purple", "white", "blue"]


my_turtle.penup()
my_turtle.forward(90)
my_turtle.left(45)
my_turtle.pendown()

def branch():
    my_turtle.color(random.choice(colours))
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

for i in range(8):
    branch()
    my_turtle.left(45)