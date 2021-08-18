from player import STARTING_POINT
from turtle import Turtle
import random

WEST = 180
EAST = 0

class Obstacles(Turtle):
    def __init__(self):
        super().__init__()
        self.x_starting_point  = 400
        self.west_y_starting_points = [-200, -150, -100 ,0 ,50 , 100, 200, 280 ]
        self.color_list = ['red','blue','green', 'yellow', 'orange', 'pink', 'brown', 'grey']
        self.random_speed = [5,10,15,20,25]
        
        self.shape('square')
        self.shapesize(stretch_len=2, outline=2)
        self.penup()
        self.color(random.choice(self.color_list))
        self.goto(self.x_starting_point,random.choice(self.west_y_starting_points))
        self.setheading(WEST)
    
    def east_obstacles(self):
        self.x_starting_point *= -1
        self.east_y_starting_points = [-180, -120, -70 ,-30, 70 ,130, 250 ]
        self.shape('arrow')
        self.shapesize(stretch_len=2)
        self.penup()
        self.color("red")
        self.goto(self.x_starting_point,random.choice(self.east_y_starting_points))
        self.setheading(EAST)


    def move_obstacle(self):
        self.fd(self.random_speed[random.randint(0,4)])

    def reset_west_obstacle(self):

        self.goto(self.x_starting_point,random.choice(self.west_y_starting_points))

    def reset_east_obstacle(self):

        self.goto(self.x_starting_point,random.choice(self.east_y_starting_points))
    
