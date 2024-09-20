from turtle import Turtle, Screen

t1 = Turtle()



t1.penup()
t1.shape('turtle')
t1.goto(-350, 10)
print(t1.distance(150, 10))
t1.forward(600)
print(t1.distance(150, 10))
screen = Screen()
screen.exitonclick()
