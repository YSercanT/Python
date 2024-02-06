from turtle import Turtle,Screen
import time
import random
import sys
class Snake:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)
        self.starting_positions=[(0,0),(-20,0),(-40,0)]
        self.segments=[]
        self.game_is_on=True
        self.food=Food()
        self.scoreBoard=ScoreBoard()

        
    def init_body(self):
        for position in self.starting_positions:
            self.add_segment(position)
        self.head=self.segments[0]
    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)
    def turnRight(self):
        if self.head.heading()!=180:
            self.head.setheading(0)
    def turnLeft(self):
        if self.head.heading()!=0:
            self.head.setheading(180)
    def exit_game(self):
        sys.exit(0)
    def listener(self):
        self.screen.listen()
        self.screen.onkey(key="w",fun=self.up)
        self.screen.onkey(key="s",fun=self.down)
        self.screen.onkey(key="d",fun=self.turnRight)
        self.screen.onkey(key="a",fun=self.turnLeft)
        self.screen.onkey(key="q", fun=self.exit_game)
    def add_segment(self,position):
        newSegment=Turtle("square")
        newSegment.penup()
        newSegment.color("white")
        newSegment.goto(position)
        self.segments.append(newSegment)
    def collision(self):
        for segment in self.segments[1:]:
            
            if self.head.distance(segment)<10:
                
                return True
        return False

        
    def extend(self):
        self.add_segment(self.segments[-1].position())
        pass
    def reset(self):
        for i in self.segments:
            i.reset()
        self.segments.clear()
        self.init_body()
        
    def move(self):
        
        while self.game_is_on:
            
            if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
                    #self.game_is_on=False
                    #self.scoreBoard.game_over()
                    self.scoreBoard.reset()
                    self.reset()
                    
            self.screen.update()
            for seg_num in range(len(self.segments)-1,0,-1):
                new_x=self.segments[seg_num-1].xcor()
                new_y=self.segments[seg_num-1].ycor()
                self.segments[seg_num].goto(new_x,new_y)
                self.listener()
                if self.head.distance(self.food)< 15:
                    #print("nom nom nom")
                    self.food.refresh()
                    self.scoreBoard.increase_score()
                    self.extend()
            self.head.forward(20)
            if self.collision():
                #self.game_is_on=False
                #self.scoreBoard.game_over()
                self.scoreBoard.reset()
                self.reset()
                break
            time.sleep(0.09)
            

                
                
    def __main__(self):
        self.init_body()
        self.move()
        self.screen.exitonclick()
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        random_x=random.randint(-280,280)
        random_y=random.randint(-280,280)

        self.goto(random_x,random_y)
    
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = self.read_high_score()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.goto(0,270)
        self.score=0
        self.color("white")
        self.update_ScoreBoard()
    def read_high_score(self):
        try:
            with open("data.txt", "r") as data_file:
                return int(data_file.read())
        except FileNotFoundError:
            with open("data.txt", "w") as new_data_file:
                new_data_file.write("0")
            return 0

    def update_ScoreBoard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",align="center",font=("Arial",18,"normal"))

    def increase_score(self):
        self.score+=1
        self.update_ScoreBoard()
    def reset(self):
        if self.score>self.high_score: 
            self.high_score=self.score
            with open("data.txt","w") as data:
                data.write(str(self.high_score))
        self.score=0
        self.update_ScoreBoard()
    """def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write(f"Game Over",align="center",font=("Arial",24,"bold"))
"""

snake=Snake()

snake.__main__()
