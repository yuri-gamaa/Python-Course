from turtle import Turtle
from random import randint, choice


class Obstacles:

    def __init__(self):
        self.obstacles = []
        self.speed = 10
        self.number_of_obstacles = 1

    def qt_obstacles(self):
        if self.number_of_obstacles > 3:
            self.number_of_obstacles = 3
        if randint(1,6) <= self.number_of_obstacles:
            self.obstacles.append(self.create())

    def create(self):
        turtle = Turtle()
        list_of_colors = ['green', 'cyan', 'red', 'blue', 'black', 'yellow']
        turtle.penup()
        turtle.shape('square')
        turtle.shapesize(stretch_len=2)
        turtle.color(choice(list_of_colors))
        turtle.goto(300, randint(-240, 240))
        return turtle

    def move(self):
        for obst in self.obstacles:
            obst.backward(self.speed)

    def increase_speed(self):
        self.speed += 5

    def increase_obstacles(self):
        self.number_of_obstacles += 1

    def return_distance(self):
        obstacles_distances = []
        for item in self.obstacles:
            x = item.xcor()
            y = item.ycor()
            obstacles_distances.append((x, y))

        return obstacles_distances
