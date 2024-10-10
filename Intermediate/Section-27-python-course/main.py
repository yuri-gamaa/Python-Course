from tkinter import *


def show_result():
    miles = str(round(float(into1.get()) * 1.609, 3))
    lb3.config(text=miles)


tkin = Tk()
tkin.minsize(300, 200)
tkin.title("Converter Miles to Km")

lb1 = Label(text="Miles:", font=("Arial", 15, "bold"))
lb1.place(x=70, y=40)
lb2 = Label(text="Km:", font=("Arial", 15, "bold"))
lb2.place(x=70, y=90)

into1 = Entry()
into1.place(x=140, y=45)
lb3 = Label(text="0", font=("Arial", 12, "bold"))
lb3.place(x=120, y=94)

but = Button(text="convert", command=show_result)
but.place(x=125, y=140)

tkin.mainloop()
