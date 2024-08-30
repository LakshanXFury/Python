import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

#Load image to the turtle game
img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

# # To know the X & Y value on the turtle screen
# def get_mouse_click_cor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",
                                    prompt="What's another state's name..?").title()
    print(answer_state)

    if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_states.append(state)
        missing_states = [state for state in all_states if state not in guessed_state]  # using list comprehension
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        # t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
