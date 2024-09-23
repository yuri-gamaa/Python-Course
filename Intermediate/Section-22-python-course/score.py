from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.player1 = 0
        self.player2 = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player1, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.player2, align="center", font=("Courier", 80, "normal"))

    def add_player1(self):
        self.player1 += 1
        self.update_score()

    def add_player2(self):
        self.player2 += 1
        self.update_score()
