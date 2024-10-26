import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        current_question = html.unescape(self.current_question.text)
        self.question_number += 1
        return f'{self.question_number}: {current_question}'

    def answer(self):
        return self.current_question.answer

    def add_score(self):
        self.score += 1

    def tests(self):
        print(len(self.question_list))
        print(self.score)
