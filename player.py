from turtle import Turtle
NORTH = 90
STARTING_POINT = -280
PACE = 20

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(NORTH)
        self.goto(0,STARTING_POINT)

    
    def move_forward(self):
        new_y = self.ycor() + PACE
        self.goto(0,new_y)

    
    def reset_pos(self):
        self.goto(0,STARTING_POINT)