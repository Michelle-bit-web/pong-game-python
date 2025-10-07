from turtle import Screen
from modules.player_module import Player
from modules.ball_module import Ball
import time

#Screen setup
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0) #turn off auto animation
player_1 = Player((250, 0))
player_2 = Player((-250, 0))
ball = Ball()

#Event Listeners
screen.listen()
screen.onkeypress(key="Up", fun=player_1.move_up)
screen.onkeypress(key="Down", fun=player_1.move_down)
screen.onkeypress(key="w", fun=player_2.move_up)
screen.onkeypress(key="s", fun=player_2.move_down)

#Game logic
game_over = False

while not game_over:
    time.sleep(0.1)
    screen.update()  # manual update when tracer=0
    ball.move()

screen.exitonclick()