from turtle import Turtle,Screen
import turtle
import random

class turtleRace():
    def __init__(self):
        turtle.colormode(255)
        
        self.totalRacers=6
        self.height=400
        self.width=500
        self.racers={}
        self.screen=Screen()
        self.screen.setup(width=self.width,height=self.height)
            
    def setRacers(self,numberOfRacers):
        self.totalRacers=numberOfRacers
    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
        return color
    def setStartPoint(self):
        startHeight=((self.height-50)/2)*-1
        distance=(self.height-50)/self.totalRacers
        return (startHeight,distance)

  

    def createTheRacers(self):
        startHeight,distance= self.setStartPoint()
        for i in range(6):
            self.racers[i]=turtle.Turtle("turtle")
            self.racers[i].color(self.random_color())
            self.racers[i].penup()
            self.racers[i].goto(-220,startHeight+distance/2)
            self.racers[i].pendown()
            self.racers[i].speed(0)
            startHeight+=distance
    def move(self):
        while self.is_race_on:
            for i,k  in enumerate(self.racers):
                rand_distance=random.randint(1,10)
                self.racers[i].forward(rand_distance)
                if(self.racers[i].xcor()>=240):
                    self.is_race_on=False
                    self.winner_name=i+1
                    break
        
    
    def add_names(self):
        for i,k  in enumerate(self.racers):
            self.racers[i].penup()
            self.racers[i].sety(self.racers[i].ycor() + 10)
            self.racers[i].write(i+1,move=None,align="center",font=("Arial",10,"normal"))
            self.racers[i].sety(self.racers[i].ycor() - 10)
            

    def delete_names(self):
        for i,k  in enumerate(self.racers):
            self.racers[i].clear()
    def start_theRace(self):
        self.is_race_on=False
        self.createTheRacers()
        self.add_names()
        self.user_bet=self.screen.textinput(title="Make your bet",prompt="Which turtle will win the race enter a number:")
        self.delete_names()
        if self.user_bet:
            self.is_race_on=True
        self.move()
        if self.winner_name==self.user_bet:
            turtle.write("You've won! The turtle{} is the winner".format(self.winner_name),move=None,align="center",font=("Arial",12,"bold"))
        elif self.winner_name!=self.user_bet: 
            turtle.write("You've lost! The turtle{}  is the winner,\nbut I'm sure you'll win next time".format(self.winner_name),move=None,align="center",font=("Arial",12,"bold"))
            
    def __main__(self):
        self.start_theRace()
        self.screen.exitonclick()
        #turtle.done()
play=turtleRace()
play.__main__()