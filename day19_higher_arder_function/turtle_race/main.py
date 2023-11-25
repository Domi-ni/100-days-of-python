from turtle import Turtle, Screen
import random


def set_initial_location(turtle, y):
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(x=-250, y=y)


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [125, 75, 25, -25, -75, -125]
all_turtles = []
race_is_on = False

my_screen = Screen()
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose a color (red,  "
                               "orange, yellow, green, blue or purple)")
if user_bet:
    race_is_on = True
my_screen.setup(width=600, height=400)

for turtle_index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(x=-250, y=y_position[turtle_index])
    new_turtle = turtle
    all_turtles.append(new_turtle)

while race_is_on:
    for turtle in all_turtles:
        turtlex = turtle.xcor()
        if turtlex > 260:
            race_is_on = False
            print(turtle.pencolor())
            if user_bet == turtle.pencolor():
                print(f"You've win! {turtle.pencolor()} was the winner")
            else:
                print(f"You've lost! {turtle.pencolor()} was the winner")
        turtle.forward(random.randint(1, 10))

my_screen.exitonclick()
