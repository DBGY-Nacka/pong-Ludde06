from random import randint
from turtle import Turtle
import time

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.movement_speed = 0.07
        self.move_x = 10
        self.move_y = randint(-10, 10) #Random direction in y direction

    def y_bounce(self):
        self.move_y *= -1
        self.movement_speed *= 0.95 #Increases speed by 5%

    def x_bounce(self):
        self.move_x *= -1
        self.movement_speed *= 0.95

    def move(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def reset_position(self):
        self.goto(0, 0)
        self.x_bounce()#Changes direction on restart
        self.movement_speed = 0.05 #Reset the speed