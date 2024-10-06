from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.point = 0

    def add_point(self, do_it=None):
        if do_it:
            self.point += 1
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.goto(0, 245)

        self.write(arg=f"{self.point}/50", align="center", font=("Courier", 30, "normal"))
