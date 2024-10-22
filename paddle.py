from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=6, stretch_len=0.5)
        self.goto(position)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 25)#Decrease the y coordinate by 20
    
    def down(self):
        self.goto(self.xcor(), self.ycor() - 25)#Increase the y coordinate by 20