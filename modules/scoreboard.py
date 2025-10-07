from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.draw_scores()

    def draw_scores(self):
        self.goto(-120, 200)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(120, 200)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

    def update_score(self, side):
        if side == "left":
            self.l_score += 1
            self.clear()
            self.draw_scores()
        elif side == "right":
            self.r_score += 1
            self.clear()
            self.draw_scores()