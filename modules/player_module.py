from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(250, 0)
        self.color("white")

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)