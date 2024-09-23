from turtle import Screen, Turtle
from paddles import Paddles
from ball import Ball
from score import Score
from time import sleep

sc = Screen()

h = 600
sc.setup(800, h)
sc.bgcolor('black')
sc.title('Pong Game')
sc.tracer(0)

line = Turtle()
line.goto(0, -300)
line.shape('square')
line.color('white')
line.pensize(5)
line.setheading(90)

for part in range(-300, 300, 10):
    line.penup()
    line.forward(20)
    line.pendown()
    line.forward(20)

p1 = Paddles((-350, 0))
p2 = Paddles((350, 0))
ball = Ball()
score = Score()

sc.listen()
sc.onkey(p1.go_up, 'w')
sc.onkey(p1.go_down, 's')
sc.onkey(p2.go_up, 'i')
sc.onkey(p2.go_down, 'k')

set_time = 0.034
while True:
    sc.update()
    sleep(set_time)
    ball.move()
    score.update_score()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 380:
        score.add_player1()
        ball.go_back()
        set_time -= 0.003
        print(score.player1)
    elif ball.xcor() < -380:
        score.add_player2()
        ball.go_back()
        set_time -= 0.003
        print(score.player2)

    if score.player1 == 5 or score.player2 == 5:
        if score.player1 > score.player2:
            print("Player 1 wins")
        else:
            print("Player 2 wins")
        break

    if ball.distance(p2) < 50 and ball.xcor() > 320 or ball.distance(p1) < 50 and ball.xcor() < -320:
        ball.bounce_x()

sc.exitonclick()
