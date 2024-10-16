import turtle
from  turtle import *


class Scoreboard(turtle.Turtle):


    Current_Score = 0

    def __init__(self, x, y):
        super().__init__()
        self.Current_Score = self.Current_Score
        self.shape("circle")
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write_Score()






    def write_Score(self):
        self.clear()
        self.write(f"{self.Current_Score}/50", move=False, align="center", font=("Arial", 20, "bold"))


    def congrats_message(self):
        self.write("CONGRATULATIONS", move=False, align="center", font=("Arial", 20, "bold"))

    def increment_score(self):
        self.Current_Score += 1










