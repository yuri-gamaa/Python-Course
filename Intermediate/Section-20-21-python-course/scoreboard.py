from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.point = 0
        self.hideturtle()
        self.goto(0, 265)
        self.color("white")
        self.title()

    def title(self):
        self.write(arg=f"Score {self.point}", align="center",
                   font=("Courier", 20, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align="center",
                   font=("Courier", 20, "bold"))

    def add_points(self):
        self.clear()
        self.point += 1
        self.title()
