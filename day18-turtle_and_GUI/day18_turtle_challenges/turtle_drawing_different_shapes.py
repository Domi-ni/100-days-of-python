from turtle import Turtle, Screen
import random


def change_color(turtle):
    r = random.random()
    g = random.random()
    b = random.random()

    turtle.color(r, g, b)


tommy_the_turtle = Turtle()

for sides in range(3, 11):
    change_color(tommy_the_turtle)
    for _ in range(sides):
        tommy_the_turtle.forward(100)
        tommy_the_turtle.right(360/sides)

my_screen = Screen()
my_screen.exitonclick()
