import turtle
import pandas



screen = turtle.Screen()
screen.title("India States Game")
image = "Map-of-India-Worksheet.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("India_states.csv")
all_states = data["ststes"].to_list()
guessed_states = []

while len(guessed_states) < 28:
    state_name = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                  prompt="What's the another state?").title()


# If states name is one of the states of the India_states.csv
    if state_name == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states ]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if state_name in all_states:
        guessed_states.append(state_name)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.ststes == state_name]
        t.goto(float(state_data.x), float(state_data.y))
        t.write(state_data.ststes.item())






turtle.mainloop()
