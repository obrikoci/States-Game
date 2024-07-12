import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
correct_guesses = 0

while correct_guesses < 50:
    answer_state = (screen.textinput(title=f"{correct_guesses}/50 States correct", prompt="Name a U.S. state")).title()

    if answer_state == "Exit":
        new_data = pandas.DataFrame(all_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        correct_guesses += 1
        all_states.remove(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)




