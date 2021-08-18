from turtle import Turtle
import random
EAST = 0

class East_Obstacles(Turtle):
    def __init__(self):
        super().__init__()
        self.x_starting_point = -400
        self.east_y_starting_points = [-180, -120, -70 ,-30 , -10, 20, 70 ,130, 250 ]
        self.random_speed = [5,10,15,20,25]
        self.color_list = ['red','blue','green', 'yellow', 'orange', 'pink', 'brown', 'grey']
        self.shape('square')
        self.shapesize(stretch_len=2, outline=3)
        self.penup()
        self.color(random.choice(self.color_list))
        self.goto(self.x_starting_point,random.choice(self.east_y_starting_points))
        self.setheading(EAST)

    def move_east(self):
        self.fd(random.choice(self.random_speed))

    def reset_east_obstacle(self):

        self.goto(self.x_starting_point,random.choice(self.east_y_starting_points))
    