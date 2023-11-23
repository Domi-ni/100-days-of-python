import turtle as t
import random

t.colormode(255)


def change_color(turtle):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    turtle.color(r, g, b)


def random_walk(turtle):
    directions = [0, 90, 180, 270]
    for _ in range(random.randint(100, 200)):
        turtle.forward(30)
        turtle.setheading(random.choice(directions))
        change_color(turtle)


nova_the_turtle = t.Turtle()
nova_the_turtle.pensize(5)
nova_the_turtle.speed(10)

random_walk(nova_the_turtle)

my_screen = t.Screen()
my_screen.exitonclick()
