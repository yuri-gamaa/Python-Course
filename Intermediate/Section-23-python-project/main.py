from turtle import Screen
from crosser import Crosser
from obstacles import Obstacles
from details import Details
from time import sleep

scn = Screen()

scn.setup(600, 600)
scn.tracer(0)

turtle = Crosser()
obst = Obstacles()
dts = Details()

scn.listen()
scn.onkey(fun=turtle.walk, key='w')
scn.onkey(fun=turtle.walk_back, key='s')

objects_list = []

play_game = True
while play_game:
    scn.update()
    sleep(0.1)
    obst.qt_obstacles()
    obst.move()
    dts.print()

    if turtle.ycor() >= 300:
        dts.add_level()
        turtle.go_back()
        obst.increase_speed()
        if (dts.return_level() % 3) == 0:
            obst.increase_obstacles()

    for item in obst.return_distance():
        left_body = (item[0] - 5, item[1] - 5)
        right_body = (item[0] + 20, item[1] - 5)
        if turtle.distance(left_body) < 20 or turtle.distance(right_body) < 20:
            dts.game_over()
            play_game = False

scn.exitonclick()
