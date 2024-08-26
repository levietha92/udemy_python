from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizUI

question_bank = []

for item in question_data:
    question = Question(item['question'], item['correct_answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizUI(quiz)
