import turtle
import time
turtle.bgcolor("white")
turtle.pensize(2)

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)
def line():
    for i in range(112):
        turtle.forward(1)
turtle.speed(0)
turtle.color("red", "red")

turtle.begin_fill()

turtle.left(140)
line()
curve()

turtle.left(120)
curve()
line()

turtle.end_fill()

turtle.penup()
turtle.goto(0, 85)
turtle.pendown()
turtle.color("lightgreen")
turtle.write("Seni Seviyorum", align="center", font=("Verdana", 14, "bold"))

turtle.hideturtle()
turtle.done()
