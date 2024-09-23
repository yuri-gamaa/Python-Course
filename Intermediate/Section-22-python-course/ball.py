from turtle import Turtle
from random import choice


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.x_movement = 10
        self.y_movement = 10

    def move(self):
        x = self.xcor() + self.x_movement
        y = self.ycor() + self.y_movement
        self.goto(x, y)

    def random_side(self):
        options = [1, -1]
        side = choice(options)
        self.x_movement *= side
        self.y_movement *= side

    def bounce_y(self):
        self.y_movement *= -1

    def bounce_x(self):
        self.x_movement *= -1

    def go_back(self):
        self.goto(0, 0)
        self.x_movement *= -1
