import turtle as t
import random


def change_color(turtle):
    r = random.random()
    g = random.random()
    b = random.random()

    turtle.color(r, g, b)


def draw_spirograph(size_of_gap, turtle):
    for _ in range(int(360 / size_of_gap)):
        current_heading = turtle.heading()
        turtle.circle(100)
        change_color(turtle)
        dotty_the_turtle.setheading(current_heading + size_of_gap)


dotty_the_turtle = t.Turtle()
dotty_the_turtle.speed(0)

draw_spirograph(5, dotty_the_turtle)

my_screen = t.Screen()
my_screen.exitonclick()
