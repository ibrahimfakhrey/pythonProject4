import turtle
import pandas
screen =turtle.Screen()
screen.title("state Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_state=[]
while len(guessed_state)<50:
    answer_state=screen.textinput(title=f"{len(guessed_state)}/50 state correct ",prompt="what is the state name ?").title()
    if answer_state=="Exit":
        missing_state=[]
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
        new_data =pandas.DataFrame(missing_state)
        new_data.to_csv("states to_learn.csv")
        break


    if answer_state in all_states:
        guessed_state.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_date=data[data.state== answer_state]
        t.goto(int(state_date.x),int(state_date.y))
        t.write(answer_state)










screen.exitonclick()