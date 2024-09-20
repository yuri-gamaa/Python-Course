from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT = 20


class Snake:
    
    def __init__(self):
        self.part = []
        self.create_sneak()
        self.head = self.part[0]

    def create_sneak(self):
        for pos in START_POSITIONS:
            self.add_part(pos)

    def add_part(self, position):
        t = Turtle('square')
        t.penup()
        t.color('white')
        t.goto(position)
        self.part.append(t)

    def extend(self):
        self.add_part(self.part[-1].position())

    def move(self):
        for i in range(len(self.part) - 1, 0, -1):
            x = self.part[i - 1].xcor()
            y = self.part[i - 1].ycor()
            self.part[i].goto(x, y)
        self.head.forward(MOVEMENT)

    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

