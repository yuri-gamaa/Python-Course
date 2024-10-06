from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

s = Screen()
s.bgcolor('black')
s.setup(1000, 600)
s.tracer(0)
s.title("Jogo da cobrinha")

snk = Snake()
food = Food()
score = ScoreBoard()

s.listen()
s.onkey(snk.turn_up, "w")
s.onkey(snk.turn_down, "s")
s.onkey(snk.turn_left, "a")
s.onkey(snk.turn_right, "d")

game = True
while game:

    s.update()
    time.sleep(0.05)

    snk.move()

    if snk.head.distance(food) < 15:
        food.refresh()
        score.add_points()
        snk.extend()

    if (snk.head.xcor() <= -520 or snk.head.xcor() >= 500 or
        snk.head.ycor() <= -300 or snk.head.ycor() >= 320):
        # UPDATED
        score.reset_score()
        snk.restart_snake()

    for square in snk.parts[1:]:
        if snk.head.distance(square) < 10:
            # UPDATED
            score.reset_score()
            snk.restart_snake()

s.exitonclick()
