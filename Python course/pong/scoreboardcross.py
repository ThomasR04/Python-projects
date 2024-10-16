from turtle import Turtle
FONT = ("Courier", 25, "normal")

class Scoreboardcross(Turtle):


    def __init__(self):
        super().__init__()
        self.level = 1



    def update(self):
        self.clear()
        self.penup()
        self.goto(-280, 250)
        self.write(f"LEVEL: {self.level}",align="left", font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center", font=("courier", 40, "normal"))


