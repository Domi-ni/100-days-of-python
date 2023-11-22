import turtle as t
import random


def change_color(turtle):
    r = random.random()
    g = random.random()
    b = random.random()

    turtle.color(r, g, b)


def turn(turtle):
    key = random.randint(1, 2)
    if key == 1:
        tu ][}
nova_the_turtle = t.Turtle()

for _ in range(random.randint(50,1000)):
    nova_the_turtle.forward(random.randint(10, 100))
    turn(nova_the_turtle)
    change_color(nova_the_turtle)

my_screen = t.Screen()
my_screen.exitonclick()