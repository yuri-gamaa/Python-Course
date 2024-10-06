from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT = 20


class Snake:
    
    def __init__(self):
        self.parts = []
        self.create_sneak()
        self.head = self.parts[0]

    def create_sneak(self):
        for pos in START_POSITIONS:
            self.add_part(pos)

    def add_part(self, position):
        t = Turtle('square')
        t.penup()
        t.color('white')
        t.goto(position)
        self.parts.append(t)

    def extend(self):
        self.add_part(self.parts[-1].position())

    def restart_snake(self):
        for part in self.parts:
            part.goto(1000, 1000)
        self.parts.clear()
        self.create_sneak()
        self.head = self.parts[0]

    def move(self):
        for i in range(len(self.parts) - 1, 0, -1):
            x = self.parts[i - 1].xcor()
            y = self.parts[i - 1].ycor()
            self.parts[i].goto(x, y)
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

