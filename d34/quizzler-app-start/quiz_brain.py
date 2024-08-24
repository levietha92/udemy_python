# from question_model import Question


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_score = 0  #earlier the user_score +=1 didn't work because i missed self.user_score in the function and also this line.

    def still_has_question(self):
        count_questions = len(self.question_list)
        return self.question_number < count_questions

    def next_question(self):
        question_number = self.question_number
        question_asked = self.question_list[question_number].text
        user_answer = input(
            f"Q{question_number + 1}. {question_asked} True/False? ")
        correct_answer = self.question_list[question_number].answer
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Yoohoo, you are smart")
            self.user_score += 1
        else:
            print("BOOOOOOO")

        print(f"Your score is {self.user_score} / {len(self.question_list)}")
        print("\n")
        self.question_number += 1
