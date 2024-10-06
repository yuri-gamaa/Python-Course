from turtle import Turtle


class Details(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.print()

    def add_level(self):
        self.level += 1

    def print(self):
        self.clear()
        self.goto(-290, 260)
        string = "Level " + str(self.level)
        self.write(arg=string, font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align='center', font=("Courier", 30, "bold"))

    def return_level(self):
        return self.level
