import turtle
from Scoreboard import Scoreboard
import pandas

screen = turtle.Screen()
screen.title("U.S States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("States.csv")
all_states = data.state.to_list()
guessed_states = []


score = Scoreboard(225,200)


while len(guessed_states) < 50:
 answer_state = screen.textinput(title = "Guess the State", prompt= "Guess Another state").title()

 if answer_state == "Exit":
     missing_states = []
     for states in all_states:
         if states not in guessed_states:
             missing_states.append(states)
     new_data =  pandas.DataFrame(missing_states)
     new_data.to_csv("Learn_states.csv")
     break

 if answer_state in all_states:
     states = turtle.Turtle()
     states.hideturtle()
     states.penup()
     state_p = data[data.state == answer_state]
     states.goto(state_p.x.item(), state_p.y.item())
     states.write(answer_state)
     guessed_states.append(answer_state)
     score.increment_score()
     score.write_Score()

#congrats = Scoreboard(0,0)
#congrats.congrats_message()








def get_mouse_click(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click)

turtle.mainloop()


