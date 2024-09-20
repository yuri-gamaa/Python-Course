class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        user_answer = input(f'Q.{self.question_number} {current_question.question} (True/False): ')
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, question):
        if answer.lower() == question.lower():
            print("You're right.")
            self.score+=1
        else:
            print("You're wrong.")
        print(f'Score: {self.score}/{self.question_number}')
