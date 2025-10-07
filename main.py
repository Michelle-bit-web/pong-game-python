from turtle import Screen
from modules.player_module import Player

#Screen setup
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0) #turn off auto animation
player = Player()

#Event Listeners
screen.listen()
screen.onkeypress(key="Up", fun=player.move_up)
screen.onkeypress(key="Down", fun=player.move_down)

#Game logic
game_over = False

while not game_over:
    screen.update()  # manual update when tracer=0

screen.exitonclick()