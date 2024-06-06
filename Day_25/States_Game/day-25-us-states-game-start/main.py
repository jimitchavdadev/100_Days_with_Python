import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
score = 0
guessed_states = []

while score <= 50:
    txt = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state's name?")
    if txt.lower() == "quit":
        break

    answer_state = txt.title()
    if answer_state in all_states:
        guessed_states.append(answer_state)
        score += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

states_to_learn=all_states

for i in guessed_states:
    states_to_learn.remove(i)

states_to_learn_csv = pandas.DataFrame(states_to_learn)
states_to_learn_csv.to_csv("States_to_learn.csv")
