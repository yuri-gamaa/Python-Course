from tkinter import Tk, PhotoImage, Label, Button
from random import randint, choice
import pandas


data = pandas.read_csv("flashcard-app-db.csv")
words = {}
en_word = ''


def chose_word():
    row = randint(2, 494)
    global words
    words = {
        "w": {
            "ptBR": data.iloc[row, 1],
            "en1": data.iloc[row, 0],
            "en2": data.iloc[randint(2, 494), 0]
        }
    }

    while True:
        if words["w"]["en2"] == words["w"]["en1"]:
            words["w"]["en2"] = data.iloc[randint(2, 494), 0]
        else:
            break

    global en_word
    en_word = choice([words["w"]["en1"], words["w"]["en2"]])


def insert_values():
    header.config(text=data.columns[0])
    word.config(text=en_word)


def confirm():
    pt_br_id = data[data['Português'] == words['w']['ptBR']].index
    en_id = data[data['Inglês'] == en_word].index

    if en_id[0] == pt_br_id[0]:
        print("Deu bom!")
    else:
        print("Deu ruim!")

    chose_word()
    insert_values()


def cancel():
    pt_br_id = data[data['Português'] == words['w']['ptBR']].index
    en_id = data[data['Inglês'] == en_word].index

    if en_id[0] != pt_br_id[0]:
        print("Deu bom!")
    else:
        print("Deu ruim!")

    chose_word()
    insert_values()


def change_cards():
    pt_br = words["w"]["ptBR"]
    en = en_word

    if header.cget("text") == data.columns[0] and word.cget("text") == en:
        header.config(text=data.columns[1])
        word.config(text=pt_br)
    else:
        header.config(text=data.columns[0])
        word.config(text=en)


chose_word()

# ---------------------------------------------------- Window --------------------------------------------------------#

window = Tk()
window.maxsize(800, 500)
window.minsize(650, 500)
window.config(padx=100, pady=10, bg="#ffffff")

# --------------------------------------------------- Buttons --------------------------------------------------------#

flashcard = Button(padx=60, pady=50, width=60, height=14, bd=3, bg="#ffffff", command=change_cards)
flashcard.grid(column=0, row=0, columnspan=2, rowspan=2)

image_conf = PhotoImage(file="1.png")
image_cancel = PhotoImage(file="2.png")

width_image = 80
height_image = 80

conf = Button(width=width_image, height=height_image, bd=0, bg="#ffffff", image=image_conf, command=confirm)
conf.grid(column=0, row=2)

cancel = Button(width=width_image, height=height_image, bd=0, bg="#ffffff", image=image_cancel, command=cancel)
cancel.grid(pady=50, column=1, row=2)

# --------------------------------------------------- Labels --------------------------------------------------------#

header = Label(text=data.columns[0], font=("Onyx", 18, "bold"), bg="#ffffff")
header.grid(column=0, row=0, columnspan=2)

word = Label(text=en_word, font=("Onyx", 18, "bold"), bg="#ffffff")
word.grid(column=0, row=1, columnspan=2)

window.mainloop()
