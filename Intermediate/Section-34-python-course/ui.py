from tkinter import *
from quiz_brain import QuizBrain


class Ui:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.minsize(width=320, height=500)
        self.window.config(bg="#202056", padx=30, pady=30)
        self.window.title("Quiz")

        self.score_lab = Label(text="00", anchor='e', font=("Arial", 15, "bold"), fg="#ffffff", bg="#202056")
        self.score_lab.grid(ipadx=60, column=1, row=0)

        self.canvas = Canvas(width=270, height=230, bg="#ffffff", highlightthickness=0)
        self.text_canvas = self.canvas.create_text(135, 115, width=258, fill="black",
                                                   font=("Arial", 16, "bold", "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        confirm = PhotoImage(file="images/true.png")
        cancel = PhotoImage(file="images/false.png")

        self.conf_button = Button(borderwidth=-1, highlightthickness=0, image=confirm, command=self.select_true)
        self.conf_button.grid(column=1, row=2, rowspan=2)

        self.cancel_button = Button(borderwidth=-1, highlightthickness=0, image=cancel, command=self.select_false)
        self.cancel_button.grid(column=0, row=2, rowspan=2, padx=26)

        self.change_text()

        self.window.mainloop()

    def select_true(self):
        if 'T' in self.quiz.answer():
            self.change_score()
        self.change_text()

    def select_false(self):
        if 'F' in self.quiz.answer():
            self.change_score()
        self.change_text()

    def change_text(self):
        question = self.quiz.next_question()
        self.canvas.itemconfig(self.text_canvas, text=question)

        if not self.quiz.still_has_questions():
            self.end_of_game()

    def change_score(self):
        self.quiz.add_score()

        if self.quiz.score < 10:
            new_score = '0' + str(self.quiz.score)
        else:
            new_score = str(self.quiz.score)

        self.score_lab.config(text=new_score)

    def do_nothing(self):
        pass

    def end_of_game(self):
        self.conf_button.config(command=self.do_nothing)
        self.cancel_button.config(command=self.do_nothing)
        self.canvas.itemconfig(self.text_canvas, text=f"Score: {self.quiz.score}")
        self.score_lab.config(text="")
