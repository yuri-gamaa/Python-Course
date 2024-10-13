from tkinter import *
from tkinter import messagebox
from gerar_pass import new_pass
from pyperclip import copy
import json

# ------------------------------------------------- Functions ------------------------------------------------------- #


def clear_entry():
    text_origin.delete(0, END)
    user_input.delete(0, END)
    user_password.delete(0, END)


def save_pass():
    the_origin = text_origin.get()[0].upper() + text_origin.get()[1:].lower()
    email = user_input.get()
    passwd = user_password.get()

    if not the_origin or not email or not passwd:
        pass
    else:
        info = {the_origin: {"username/email": email, "password": passwd}}

        with open("passes.json", 'r', encoding="utf-8") as file:
            content = json.load(file)
            content.update(info)
        with open("passes.json", 'w', encoding="utf-8") as file:
            json.dump(content, file, indent=4)

        clear_entry()


def generate_pass():
    user_password.delete(0, END)
    new_password = new_pass()
    user_password.insert(0, new_password)
    copy(new_password)


def search_data():
    try:
        place = text_origin.get()[0].upper() + text_origin.get()[1:].lower()
    except IndexError:
        messagebox.showinfo(title="Error", message="You left the entry in blank.")
    else:
        with open("passes.json", 'r', encoding="utf-8") as file:
            content = json.load(file)

        if place in content:
            user = content[place]["username/email"]
            passwd = content[place]["password"]
            messagebox.showinfo(title=place, message=f"{user}\n{passwd}")
            copy(passwd)
        else:
            messagebox.showinfo(title="Error", message="Data not found.")


# -------------------------------------------- Check if file exists ------------------------------------------------ #

try:
    file = open('passes.json')
except FileNotFoundError:
    bd = {}
    with open('passes.json', 'w') as file:
        json.dump(bd, file)

# -------------------------------------------------- Window -------------------------------------------------------- #

tk = Tk()
tk.title("Password Manager")
tk.minsize(400, 550)
tk.config(pady=20, padx=40, bg="#000000")

# -------------------------------------------------- Canva --------------------------------------------------------- #

can = Canvas(width=210, height=320, bg="#000000", highlightthickness=0)
img = PhotoImage(file="cadeado-full-size.png")
can.create_image(100, 160, image=img)
can.grid(column=1, row=0)

# -------------------------------------------------- Labels -------------------------------------------------------- #

origin = Label(width=20, text="Origin:", font=("Courier", 13, "normal"), fg="#ffffff", bg="#000000")
origin.grid(column=0, row=2)

user = Label(width=20, text="Username/Email:", font=("Courier", 13, "normal"), fg="#ffffff", bg="#000000")
user.grid(column=0, row=3)

password = Label(width=20, text="Password:", font=("Courier", 13, "normal"), fg="#ffffff", bg="#000000")
password.grid(column=0, row=4)

# -------------------------------------------------- Entries -------------------------------------------------------- #

text_origin = Entry(width=22, fg="#ffffff", bg="#000000", highlightthickness=1, font=("Courier", 11, "normal"))
text_origin.grid(column=1, row=2)

user_input = Entry(width=40, fg="#ffffff", bg="#000000", highlightthickness=1, font=("Courier", 11, "normal"))
user_input.grid(column=1, row=3, columnspan=2)

user_password = Entry(width=22, fg="#ffffff", bg="#000000", highlightthickness=1, font=("Courier", 11, "normal"))
user_password.grid(column=1, row=4)

# -------------------------------------------------- Buttons -------------------------------------------------------- #

search = Button(width=21, height=0, text="Search", fg="#ffffff",
                bg="#000000", highlightthickness=1,
                font=("Courier", 9, "normal"), command=search_data)
search.grid(column=2, row=2)

generate_passwd_button = Button(width=21, height=0, text="Generate Password", fg="#ffffff",
                                bg="#000000", highlightthickness=1,
                                font=("Courier", 9, "normal"), command=generate_pass)
generate_passwd_button.grid(column=2, row=4)

send = Button(width=63, height=1, text="Send", fg="#ffffff",
              bg="#000000", font=("Courier", 11, "normal"),
              command=save_pass)
send.grid(column=0, row=5, columnspan=3)

tk.mainloop()
