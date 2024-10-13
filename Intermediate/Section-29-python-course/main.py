from tkinter import *
from gerar_pass import new_pass


def clear_entry():
    text_origin.delete(0, END)
    user_input.delete(0, END)
    user_password.delete(0, END)


def save_pass():
    the_origin = text_origin.get()
    email = user_input.get()
    passwd = user_password.get()

    with open("passes.txt", 'a') as file:
        file.write(the_origin + '\t\t|\t\t' + email + "\t\t|\t\t" + passwd + "\n")

    clear_entry()


def generate_pass():
    user_password.delete(0, END)
    user_password.insert(0, new_pass())


tk = Tk()
tk.title("Password Manager")
tk.minsize(400, 550)
tk.config(pady=20, padx=40, bg="#000000")
can = Canvas(width=210, height=320, bg="#000000", highlightthickness=0)
img = PhotoImage(file="cadeado-full-size.png")
can.create_image(100, 160, image=img)
can.grid(column=1, row=0)

origin = Label(width=20, text="Origin:", font=("Courier", 13, "bold"), fg="#ffffff", bg="#000000")
origin.grid(column=0, row=2)

text_origin = Entry(width=40, fg="#ffffff", bg="#000000", highlightthickness=1, font=("Courier", 11, "bold"))
text_origin.grid(column=1, row=2, columnspan=2)

user = Label(width=20, text="Username/Email:", font=("Courier", 13, "bold"), fg="#ffffff", bg="#000000")
user.grid(column=0, row=3)

user_input = Entry(width=40, fg="#ffffff", bg="#000000", highlightthickness=1, font=("Courier", 11, "bold"))
user_input.grid(column=1, row=3, columnspan=2)

password = Label(width=20, text="Password:", font=("Courier", 13, "bold"), fg="#ffffff", bg="#000000")
password.grid(column=0, row=4)

user_password = Entry(width=22, fg="#ffffff", bg="#000000", highlightthickness=1, font=("Courier", 11, "bold"))
user_password.grid(column=1, row=4)

generate_passwd_button = Button(width=21, height=0, text="Generate Password", fg="#ffffff",
                                bg="#000000", highlightthickness=1,
                                font=("Courier", 9, "bold"), command=generate_pass)
generate_passwd_button.grid(column=2, row=4)

send = Button(width=63, height=1, text="Send", fg="#ffffff",
              bg="#000000", font=("Courier", 11, "bold"),
              command=save_pass)
send.grid(column=0, row=5, columnspan=3)

tk.mainloop()
