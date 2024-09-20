from turtle import Turtle, Screen

trl = Turtle()
screen = Screen()


def move_forward():
    trl.forward(10)


def move_backward():
    trl.back(10)


def turn_to_right():
    # trl.right(10)
    new_heading = trl.heading() - 10
    trl.setheading(new_heading)


def turn_to_left():
    # trl.left(10)
    new_heading = trl.heading() + 10
    trl.setheading(new_heading)


def clear_screen():
    trl.clear()
    trl.penup()
    trl.home()
    trl.pendown()


trl.speed(0)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_to_left)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_to_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
