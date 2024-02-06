from turtle import Turtle,Screen
t=Turtle()
screen=Screen()
def move_forwards():
    t.forward(10)
def move_backwards():
    t.backward(10)
def turnLeft():
    t.left(90)
def turnRight():
    t.right(90)
def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
screen.listen()
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="d",fun=turnRight)
screen.onkey(key="a",fun=turnLeft)
screen.onkey(key="c",fun=clear)

screen.exitonclick()