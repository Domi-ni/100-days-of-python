import colorgram
import turtle as turtle_module
import random

turtle_module.colormode(255)


def set_to_initial_location(turtle):
    turtle.setheading(225)
    turtle.penup()
    turtle.forward(300)
    turtle.setheading(0)


def star_new_line(turtle):
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)
    turtle.forward(500)
    turtle.setheading(0)
    turtle.pendown()


colors = colorgram.extract('color.jpeg', 10)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

dot_color = random.choice(rgb_colors)
turtle = turtle_module.Turtle()
turtle.speed(10)
turtle.hideturtle()

set_to_initial_location(turtle)
for _ in range(10):
    for __ in range(10):
        dot_color = random.choice(rgb_colors)
        turtle.dot(20, dot_color)
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
    star_new_line(turtle)

my_screen = turtle_module.Screen()
my_screen.exitonclick()

print(turtle.pos())





