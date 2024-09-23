from turtle import Turtle


class Paddles(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        move = self.ycor() + 20
        self.goto(self.xcor(), move)
    
    def go_down(self):
        move = self.ycor() - 20
        self.goto(self.xcor(), move)

    def paddle_position(self):
        print(self.position())
