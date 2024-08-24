from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question = Question(item['question'], item['correct_answer']) #mini change and it worked
    # print(question.text) having the quotte problem
    # print(question.answer) ok
    question_bank.append(question)

print(question_bank)
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
  quiz.next_question()

if quiz.still_has_question() == False:
  print("You have reached the end of the game")