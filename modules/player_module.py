from turtle import Turtle

class Player(Turtle):
    def __init__(self, player_position):
        super().__init__()
        self.up()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(player_position)
        self.color("white")

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)