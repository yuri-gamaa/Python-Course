from turtle import Turtle


class Crosser(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.go_back()
        self.shape('turtle')

    def walk(self):
        self.setheading(90)
        self.forward(10)

    def walk_back(self):
        self.setheading(270)
        self.forward(10)

    def go_back(self):
        self.goto(0, -280)
