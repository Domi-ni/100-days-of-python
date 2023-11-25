from turtle import Turtle, Screen


def go_forward():
    tobby.forward(2)

                             
def go_backward():
    tobby.forward(-2)


def turn_left():
    tobby.left(5)


def turn_right():
    tobby.right(5)


def clear_screen():
    tobby.clear()
    tobby.penup()
    tobby.home()
    tobby.pendown()


tobby = Turtle()
tobby.pensize(2)

my_screen = Screen()
my_screen.listen()

my_screen.onkeypress(key="w", fun=go_forward)
my_screen.onkeypress(key="s", fun=go_backward)
my_screen.onkeypress(key="a", fun=turn_left)
my_screen.onkeypress(key="d", fun=turn_right)
my_screen.onkeypress(key="c", fun=clear_screen)

my_screen.exitonclick()
