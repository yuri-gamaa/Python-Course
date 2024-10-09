import turtle
import states
import scoreboard

scr = turtle.Screen()
ttl = turtle.Turtle()
st = states.States()
sco = scoreboard.Scoreboard()

image = "blank_states_img.gif"

scr.setup(725, 590)
scr.addshape(image)
ttl.shape(image)
sco.scoreboard()
scr.tracer(0)

game = True
while game:
    scr.update()
    guess = scr.textinput("States", "Guess a state from USA:").title().lower()
    if guess == "exit":
        st.create_lack()
        game = False
    else:
        if st.check_guess(guess):
            sco.add_point(do_it=True)
        else:
            sco.add_point()

    if len(st.completed) == 50:
        st.you_won()
        game = True


scr.exitonclick()
