from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.currentLevel = 1
        self.hideturtle()
        self.penup()
        self.color('black')
        self.update()

    def update(self):
        self.clear()
        self.goto(-360,250)
        self.write(f"Level {self.currentLevel}", align="left", font=("Arial",15, "bold"))
        
    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=("Arial",30, "bold"))

