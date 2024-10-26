from tkinter import *


# window = Tk()
# window.minsize(width=350, height=500)
# window.config(bg="#202056", padx=40, pady=60)
# window.title("Quiz")
#
# canvas = Canvas(width=270, height=230, bg="#000000", highlightthickness=0)
# canvas.grid(column=0, row=0, columnspan=2)
#
# confirm = PhotoImage(file="images/true.png")
# cancel = PhotoImage(file="images/false.png")
#
# x = 20
# y = 30
#
# conf_button = Button(padx=x, pady=y,bd="", image=confirm)
# conf_button.grid(column=1, row=1)
#
# cancel_button = Button(padx=x, pady=y, image=cancel)
# cancel_button.grid(column=0, row=1)
#
# window.mainloop()

# test = {
#     'data': 1,
#     'data': 2,
#     'data': 3,
# }
#
# print(test[0]['data'])

from quiz_brain import QuizBrain
from data import questions, answers
from question_model import Question

#
# question_bank = [Question(questions[i], answers[i]) for i in range(0, len(questions))]
# quiz = QuizBrain(question_bank)
#
# print(quiz.next_question())

teste = "True"

if not teste:
    print('hm')
else:
    print(type(teste))
