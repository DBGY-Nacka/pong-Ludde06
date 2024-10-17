from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)#Decrease the y coordinate by 20
    
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)#Increase the y coordinate by 20