from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(1200,600)
# turtle_winner = (screen.textinput(title="Which turtle wins?",
#                                  prompt="Which turtle you bet that is gonna be the winner?"
#                                         "Red, Green, Black or Cyan?").lower())
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()

list_turtles = [t1, t2, t3, t4]
colors_turtles = ['red', 'green', 'black', 'blue']
turtles_range = range(len(list_turtles))
x = 420
y = 120
ys = []

finish_line = Turtle()

finish_line.hideturtle()
finish_line.penup()
finish_line.goto(x-50, 190)
finish_line.pendown()
finish_line.setheading(270)
finish_line.forward(340)

for t in turtles_range:

    list_turtles[t].speed(10)
    list_turtles[t].penup()
    list_turtles[t].shape('turtle')
    list_turtles[t].color(colors_turtles[t])
    list_turtles[t].goto(-400, y)
    ys.append(y)
    y -= 70

true = True
while true:

    rd = randint(0, 3)
    turtle_time = rd

    for run in range(1):

        list_turtles[run].speed(6)
        list_turtles[turtle_time].forward(randint(10, 25))

        if list_turtles[turtle_time].distance(x, ys[turtle_time]) <= 50:
            print(f"Winner: {colors_turtles[turtle_time]}")
            # if turtle_winner == colors_turtles[turtle_time]:
            #     print(f"You were write, {turtle_winner} won.")
            # else:
            #     print("What a shame, you were wrong.")
            true = False

screen.exitonclick()
