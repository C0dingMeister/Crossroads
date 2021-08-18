import random
from turtle import Screen, distance
from player import Player
from west_obstacle import Obstacles
from east_obstacle import East_Obstacles
from scoreboard import Score
import time

#Setting up the screen

screen = Screen()
screen.setup(width=800, height=600)
screen.title("CrossRoads")
screen.tracer(0)


# setting up the player

player = Player()


screen.onkey(player.move_forward, "Up")
screen.listen()

#Setting up the obstacle

west_obstacle = []
east_obstacle = []


for i in range(25):
    i = Obstacles()
    west_obstacle.append(i)

for j in range(10):
    j = East_Obstacles()
    east_obstacle.append(j)

#Setting up scoreboard

score = Score()







game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)
    for obstacle in west_obstacle:
        obstacle.move_obstacle()
        if obstacle.xcor() < -410:
            obstacle.reset_west_obstacle()
            screen.update()
        if player.distance(obstacle) < 25 :
            screen.update()
            score.game_over()
            game_is_on = False

    for obstacle in east_obstacle:
        obstacle.move_east()
        if obstacle.xcor() > 410:
            obstacle.reset_east_obstacle()
            screen.update()
            
        if player.distance(obstacle) < 25 :
            screen.update()
            score.game_over()
            game_is_on = False

        
   

    if player.ycor() > 290:
        player.reset_pos()
        screen.update()
        score.currentLevel += 1
        score.update()
    

   



screen.exitonclick()
