from turtle import Turtle, Screen
import pandas

my_screen = Screen()
my_screen.bgpic("blank_states_img.gif")
my_screen.exitonclick()

data = pandas.read_csv("./50_states.csv")

guess = input("Guess a state")
for state in data[state]:
    if guess == state:
        point += 1
        guess.goto(data(data[state] == x, data(data[state] == x))

