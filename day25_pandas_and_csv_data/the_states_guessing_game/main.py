import turtle
import pandas

my_screen = turtle.Screen()
my_screen.title("U.S. States Game")
my_screen.bgpic("blank_states_img.gif")
my_screen.setup(width=725, height=491)

data = pandas.read_csv("50_states.csv")
data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = my_screen.textinput(title=f"{len(guessed_states)}/50 Guess a state name",
                                       prompt="What's another state's name").title()
    if answer_state == "Exit":
        missing_states = []
        states_list = data.state.to_list()
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("stats_to_learn.csv")

        break

    for state in data["state"]:
        if answer_state == state:
            guessed_states.append(state)
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(arg=state)






