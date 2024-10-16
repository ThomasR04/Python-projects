import colorgram
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
screen = turtle_module.Screen()
screen.setup(1000,600)


color_list = [  (200, 10, 35), (247, 236, 37), (240, 244, 251), (239, 231, 3), (36, 216, 77), (223, 159, 61), (39, 79, 185), (28, 39, 159), (210, 73, 16), (17, 151, 18), (239, 39, 152), (65, 9, 27), (188, 14, 9), (216, 25, 127), (218, 140, 198), (223, 161, 7), (59, 12, 7), (67, 202, 227), (10, 96, 60), (84, 80, 212), (17, 19, 52), (237, 157, 218), (106, 232, 195), (99, 205, 136), (212, 84, 58), (8, 222, 235), (236, 171, 161)]
def produce_dots():
 for i in range(10):
  tim.pendown()
  tim.dot(20, random.choice(color_list) )
  tim.penup()
  tim.forward(50)

def start_nextRow_left():
 tim.left(90)
 tim.forward(40)
 tim.left(90)
 tim.forward(50)




def start_nextRow_right():
 tim.right(90)
 tim.forward(40)
 tim.right(90)
 tim.forward(50)


for i in range(5):
  produce_dots()
  start_nextRow_left()
  produce_dots()
  start_nextRow_right()


screen.exitonclick()