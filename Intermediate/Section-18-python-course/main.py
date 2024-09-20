import colorgram
import turtle as t
import random as rd

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

tur = t.Turtle()

# Settings:
t.colormode(255)
tur.speed(0)
tur.hideturtle()
tur.width(10)
tur.penup()
tur.goto(-300, -100)

y = -100

for __ in range(20):
    for _ in range(20):
        tur.pendown()
        selected_color = rd.choice(rgb_colors)
        tur.color(selected_color)
        tur.forward(1)
        tur.penup()
        tur.forward(20)
    y += 20
    tur.goto(-300, y)

screen = t.Screen()
screen.exitonclick()
