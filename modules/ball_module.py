from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.color("MediumOrchid1")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)