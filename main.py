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

def drawTriangle():
    colormode(255)
    turtle.pencolor(randColor())
    for x in range(3): 
        turtle.forward(100)
        turtle.right(120)
def drawSquare():
    colormode(255)
    turtle.pencolor(randColor())
    for x in range(4):
        turtle.forward(100)
        turtle.right(90)
def drawPentagon():
    colormode(255)
    turtle.pencolor(randColor())
    for x in range(5):
        turtle.forward(100)
        turtle.right(72)
def drawHexagon():
    colormode(255)
    turtle.pencolor(randColor())
    for x in range(6):
        turtle.forward(100)
        turtle.right(60)
def drawHeptagon():
    colormode(255)
    turtle.pencolor(randColor())
    for x in range(7):
        turtle.forward(100)
        turtle.right(51.42)
def drawOctagon():
    colormode(255)
    turtle.pencolor(randColor())
    for x in range(8):
        turtle.forward(100)
        turtle.right(45)
def drawNonagon():
    colormode(255)
    turtle.pencolor(randColor())
    for x in range(9):
        turtle.forward(100)
        turtle.right(40)
def drawDecagon():
    colormode(255)
    turtle.pencolor(randColor())
    for x in range(10):
        turtle.forward(100)
        turtle.right(36)

drawTriangle()
drawSquare()
drawPentagon()
drawHexagon()
drawHeptagon()
drawOctagon()
drawNonagon()
drawDecagon()

screen.exitonclick()


