from turtle import Screen, Turtle

def up():
    tur.forward(10)

def down():
    tur.backward(10)
scn = Screen()

scn.setup(600, 600)

tu = Turtle()
tur = Turtle()

scn.listen()
scn.onkey(fun=tur.up, key='w')
scn.onkey(fun=tur.down, key='s')

tu.shape('square')
tu.shapesize(stretch_len=2)

left_body = tu.position()
right_body = (tu.xcor() - 20, tu.ycor() - 20)

print(left_body, right_body)

scn.exitonclick()