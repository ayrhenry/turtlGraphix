from turtle import *
from random import *

def randColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rand_color = (r, g, b)
    return rand_color

random = Random()
turtle2 = Turtle()
screen = Screen()
turtle2.speed(0)


for x in range(0, 300, 2):
    colormode(255)
    turtle2.color(randColor())
    turtle2.circle(100)
    turtle2.left(x)



screen.exitonclick()