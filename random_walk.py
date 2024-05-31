from turtle import *
from random import *
#from main import randColor


turtl = Turtle()
screen = Screen()
random = Random()


def random_movement():
    num = random.randint(0, 40)
    num2 = random.randint(0, 100)
    num3 = random.randint(0, 100)
    turtl.speed(0)
    turtl.width(10)
    colormode(255)
    turtl.pencolor(num3, num2, num3)

    if num <= 10:
        turtl.left(90)
        turtl.forward(num2)
    elif num > 10 and num <= 20:
        turtl.right(90)
        turtl.forward(num2)
    elif num > 20 and num <= 30:
        turtl.back(num2)
    else:
        turtl.forward(num2)

while True:
    random_movement()

screen.exitonclick()

