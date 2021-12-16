import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#  ta opcja zbiera koordynaty z klikniecia mysza
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()   # data["state"] #wszystkie stany prawie jak for
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What is another state's name?").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states: # in dziala z lista
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] # wyjmuje aktualny wiersz row
        t.goto(int(state_data.x), int(state_data.y))
        #  t.write(state_data.state)
        # t.write(state_data.state.item())
        t.write(answer_state)

    #turtle.mainloop() zapetla po kliknieciu nie wychodzi z okna turtle


