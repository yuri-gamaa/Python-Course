from tkinter import *
from math import floor


STICK = "I"
reps = 0
clock = None


def get_ready(n):
    minute = floor(n / 60)
    second = floor(n % 60)

    if minute < 10:
        minute = f'0{minute}'
    if second < 10:
        second = f'0{second}'

    timer.config(text=f'{minute}:{second}')
    if n > 0:
        global clock
        clock = tk.after(1000, get_ready, n - 1)
    else:
        run_timer()


def run_timer():
    global reps
    reps += 1

    if reps % 2 == 0:
        title.config(text="    Break", font=("Onyx", 22, "bold"), fg="#ff0000")
        add_sticks()
        get_ready(10*60)
    else:
        title.config(text="    Work", font=("Onyx", 22, "bold"), fg="#50dd50")
        get_ready((60*60) - 0.01)


def reset_functions():
    tk.after_cancel(clock)
    title.config(text="    Timer", fg="#000000")
    timer.config(text="00:00")
    stick.config(text="")
    global reps
    reps = 0


def add_sticks():
    if reps // 2 < 7:
        show_sticks = STICK*(reps // 2)
    else:
        leftover = (reps // 2) - 6
        show_sticks = STICK*6 + '\n' + STICK*leftover

    stick.config(text=show_sticks)


tk = Tk()
tk.minsize(350, 380)
tk.title("Pomodoro Project")
tk.config(padx=25, pady=10, bg="#ffffff")

title = Label(text="    Timer", font=("Onyx", 22, "bold"), bg="#ffffff")
title.grid(column=3, row=1)

can = Canvas(width=200, height=230, bg="#ffffff", highlightthickness=0)
img = PhotoImage(file="relogio.png")
can.create_image(115, 120, image=img)
can.grid(column=3, row=2)

timer = Label(width=5, text="00:00", font=("Onyx", 29, "bold"), bg="#ffffff")
can.create_window(115, 130, window=timer)

start = Button(text="Start", bg="#ffffff", font=("Onyx", 10, "bold"), command=run_timer)
start.grid(column=1, row=4)

reset = Button(text="Reset", bg="#ffffff", font=("Onyx", 10, "bold"), command=reset_functions)
reset.grid(column=4, row=4)

stick = Label(width=5, bg="#ffffff", font=("Onyx", 20, "bold"))
stick.grid(column=3, row=4)

tk.mainloop()
