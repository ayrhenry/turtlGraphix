from turtle import *
from random import *


turtle = Turtle()
screen = Screen()
random = Random()

def randColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b

def draw_shape(num_sides):
    colormode(255)
    turtle.pencolor(randColor())
    for x in range(num_of_sides): 
        turtle.forward(100)
        turtle.right(360 / num_of_sides)

for num_of_sides in range(3, 11):
    draw_shape(num_of_sides)

screen.exitonclick()


