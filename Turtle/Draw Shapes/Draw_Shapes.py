from turtle import Turtle,Screen
import random
class shapeMaker():
    def __init__(self):
        
        self.colors = ["red", "green", "blue", "yellow", "purple", "brown", "pink", "orange",  "black"]
        self.pen_colors = ["black", "red", "green", "blue", "yellow", "purple", "brown", "pink", "orange"]
        self.pen_sizes = [1, 2, 3]
        self.pen_shapes = ["square", "circle", "triangle", "classic"]
    
    def make_shape(self):
        self.MAX_SHAPE = int(input("Enter shape: "))
        
    def calculate_the_angle(self, shape):
        theta= (shape-2)*180
        return theta
    
    def draw_the_shape(self, theta,shape=3,pen_size=4,pen_shape="classic"):
        col=random.choice(self.colors)
        pen_col=random.choice(self.pen_colors)

        self.x.color(col)
        self.x.pencolor(pen_col)
        self.x.width(pen_size)
        self.x.shape(pen_shape)
        #print("Shape : " , shape)
        #print("Angle is  : ",(theta/shape))
        for _ in range(shape):
            
            self.x.forward(100)
            

            self.x.right(180-(theta/shape))
        
    def __main__(self):
        self.x=Turtle()
        self.Screen= Screen()
        self.Screen.setup(width=self.Screen.window_width(), height=self.Screen.window_height())
        self.x.penup()  
        self.x.goto(-50, (self.Screen.window_width()/2)-30) 
        self.x.pendown()  
        pen_size=random.choice(self.pen_sizes)
        pen_shape=random.choice(self.pen_shapes)
        self.make_shape()
        for i in range(3,self.MAX_SHAPE+1):
            theta=self.calculate_the_angle(i)
            self.draw_the_shape(theta,i,pen_size,pen_shape)
shaper = shapeMaker()
shaper.__main__()
            

