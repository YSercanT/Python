import time
from turtle import Turtle,Screen
import turtle
import random
class Game():
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("white")
        self.screen.title("Crossing Game")
        self.screen.tracer(0)
        self.game_is_on=True
        self.player=Player()
        self.carsL=[]

    def Play(self):
        self.screen.listen()
        self.carsL.append(CarFactory().generateCar())
        self.screen.onkey(self.player.move_up, "w")
        self.screen.onkey(self.player.move_down, "s")
        self.screen.onkey(self.player.move_right, "d")
        self.screen.onkey(self.player.move_left, "a")

        while self.game_is_on:
            
            time.sleep(0.06)
            self.player.scoreBoard.write_()
            self.screen.update()
            tmp=CarFactory().generateCar()
            if tmp.controlCarCollision(self.carsL)==False:

                self.carsL.append(tmp)
            else:
                tmp.remove_turtle()
            for i in self.carsL:
                
                i.move(level=self.player.scoreBoard.level)
                
                if i.is_outside_bounds():
                    i.remove_turtle()
                    self.carsL.remove(i)
                    break
                if self.player.distance(i)<30  :
                    self.player.scoreBoard.game_over()
                    self.game_is_on=False
                    break



            if self.player.ycor() > 290:
                self.player.reset()
                self.player.scoreBoard.level_up()
                for i in self.carsL:
                    i.remove_turtle()
                    i.hideturtle()
                self.carsL.clear()

            if self.player.scoreBoard.level == 7 :
                self.game_is_on = False

        self.screen.exitonclick()

class CarFactory(Turtle):
    def __init__(self):
        super().__init__()
        turtle.colormode(255)
        self.starting_move_distance=10
        self.move_incriment=10
    def generateColor(self):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        if r>240 and g>240 and b>240:
            r=0
            b=0
            g=0
        return r,g,b
    def controlCarCollision(self,t):
        for i in t:
            
            if abs(self.ycor()-i.ycor())<20 or abs(self.xcor()-i.xcor())<30:
                return True
             
        return False
            
    def generate_Ycoord(self):
        return random.randint(-220,260)
    def move(self,level=1):
        self.forward(self.starting_move_distance+(self.move_incriment*(level-1)))
        
    def generateCar(self):
        self.shape("square")
        color = self.generateColor()
        self.color(color)
        self.penup()
        self.speed(0.2)
        self.shapesize(stretch_wid=2, stretch_len=4) 
        self.goto(300,self.generate_Ycoord())
        self.setheading(180)
        return self

    def is_outside_bounds(self):
        x_bound = -340
        x = self.xcor()
        
       
        return x < x_bound 
    def remove_turtle(self):
        self.penup()
        self.clear()
        self.reset()
        self.penup()
        self.hideturtle()
        
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.reset()
        self.scoreBoard=ScoreBoard()
    def reset(self):
        self.penup()
        self.speed(0)
        self.color("green")
        self.pensize(10)
        self.goto(0,-280)
        self.setheading(90)
    def move_up(self):
        self.forward(10)
    def move_down(self):
        if(abs(self.ycor()))<280:
            self.backward(10)
    def move_right(self):
        if(abs(self.xcor()))<280:

            self.goto(self.xcor()+10,self.ycor())
        
    def move_left(self):
        if(abs(self.xcor()))<280:

            self.goto(self.xcor()-10,self.ycor())
        
    def is_Finished(self):
        if self.ycor()>=280:
            self.scoreBoard.level_up()


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.goto(0,270)
        self.score=0
        self.level=1
        self.color("Black")
        self.write_()
    def write_(self):
        self.write(f"Level: {self.level} ",align="center",font=("Arial",18,"normal"))

    def calculate_Score(self):
        pass
    def level_up(self):
        self.level+=1
        self.clear()
        self.write(f"Level: {self.level} ",align="center",font=("Arial",18,"normal"))
    def game_over(self):
        self.goto(0,0)
        self.color("Black")
        self.write(f"Game Over",align="center",font=("Arial",24,"bold"))

game=Game()
game.Play()




