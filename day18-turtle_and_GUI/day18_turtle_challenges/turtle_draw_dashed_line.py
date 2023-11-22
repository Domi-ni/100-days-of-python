import turtle
jhon_the_turtle = turtle.Turtle()

for _ in range (50):
    jhon_the_turtle.forward(10)
    jhon_the_turtle.penup()
    jhon_the_turtle.forward(10)
    jhon_the_turtle.pendown()

my_screen = turtle.Screen()
my_screen.exitonclick()