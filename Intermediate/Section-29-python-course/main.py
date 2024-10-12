from tkinter import *


def clear_entry():
    text_origin.delete(0, END)
    user_input.delete(0, END)
    user_password.delete(0, END)


def save_pass():
    the_origin = text_origin.get()
    email = user_input.get()
    passwd = user_password.get()

    with open("passes.txt", 'a') as file:
        new_string = the_origin + '\t\t|\t\t' + email + '\t\t|\t\t' + passwd + '\n'
        file.write(new_string)

    clear_entry()


try:
    with open("passes.txt") as file:
        if file:
            pass
except FileNotFoundError:
    with open("passes.txt", 'w') as file:
        file.write('Passes:\n')

tk = Tk()
tk.title("Password Manager")
tk.minsize(500, 550)
tk.config(pady=20, padx=40, bg="#000000")
can = Canvas(width=310, height=320, bg="#000000", highlightthickness=0)
img = PhotoImage(file="cadeado-full-size.png")
can.create_image(100, 160, image=img)
can.grid(column=1, row=0)

origin = Label(text="Origin:", font=("Onyx", 14, "bold"), fg="#ffffff", bg="#000000")
origin.grid(column=0, row=2)

text_origin = Entry(width=48, fg="#ffffff", bg="#000000", highlightthickness=1)
text_origin.grid(column=1, row=2, columnspan=2)

user = Label(text="Username/Email:", font=("Onyx", 14, "bold"), fg="#ffffff", bg="#000000")
user.grid(column=0, row=3)

user_input = Entry(width=48, fg="#ffffff", bg="#000000", highlightthickness=1)
user_input.grid(column=1, row=3, columnspan=2)

password = Label(text="Password:", font=("Onyx", 13, "bold"), fg="#ffffff", bg="#000000")
password.grid(column=0, row=4)

user_password = Entry(width=48, fg="#ffffff", bg="#000000", highlightthickness=1)
user_password.grid(column=1, row=4, columnspan=2)

send = Button(width=64, height=1, text="Send", fg="#ffffff",
              bg="#000000", highlightthickness=1,
              font=("Onyx", 9, "bold"), command=save_pass)
send.grid(column=0, row=5, columnspan=3)

tk.mainloop()
