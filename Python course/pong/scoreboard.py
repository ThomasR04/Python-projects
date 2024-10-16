from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
       super().__init__()
       self.coord = 0
       self.color("white")
       self.penup()
       self.hideturtle()
       self.l_score = 0
       self.r_score = 0
       self.update()


    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("courier", 80, "normal"))
        self.goto(0, 290)
        self.setheading(270)
        while self.coord < 250:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
            self.coord += 15
        self.coord = 0




    def update_scoreboard_l(self):
        self.l_score += 1



    def update_scoreboard_r(self):
        self.r_score += 1




