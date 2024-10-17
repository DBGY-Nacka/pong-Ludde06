from random import randint
from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.move_speed = 0.07
        self.move_x = 10
        self.move_y = randint(-10, 10)

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.move_y *= -1
        self.move_speed *= 0.95 #Increases speed by 5%

    def x_bounce(self):
        self.move_x *= -1
        self.move_speed *= 0.95

    def reset_position(self):
        self.goto(0, 0)
        self.x_bounce()
        self.move_speed = 0.05 #Reset the speed