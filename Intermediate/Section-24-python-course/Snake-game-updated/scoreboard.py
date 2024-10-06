from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.point = 0

#       *UPDATE*
        self.highest_score = int(self.read_file())

        self.hideturtle()
        self.goto(0, 265)
        self.color("white")
        self.title()

    def rewrite_file(self, new_point):
        with open("saved_score.txt", "w") as file:
            file.write(new_point)

    def read_file(self):
        with open("saved_score.txt", "r") as file:
            return file.read()

    def title(self):
        self.clear()
        self.write(arg=f"Score {self.point}   |   Highest Score: {self.highest_score}", align="center",
                   font=("Courtier", 20, "bold"))

#   *UPDATE*
    def reset_score(self):
        if self.point > self.highest_score:
            self.rewrite_file(str(self.point))
            self.highest_score = self.point
        self.point = 0
        self.title()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game Over", align="center",
    #                font=("Courier", 20, "bold"))

    def add_points(self):
        self.point += 1
        self.title()
