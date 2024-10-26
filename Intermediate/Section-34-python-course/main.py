from question_model import Question
from data import questions, answers
from quiz_brain import QuizBrain
import ui


question_bank = [Question(questions[i], answers[i]) for i in range(0, len(questions))]
quiz = QuizBrain(question_bank)
gui = ui.Ui(quiz)
