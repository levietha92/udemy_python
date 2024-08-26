# from question_model import Question


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_score = 0
        self.current_question = None

    def still_has_question(self):
        count_questions = len(self.question_list)
        return self.question_number < count_questions

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_asked = self.current_question.text
        return f"Q.{self.question_number}: {question_asked}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.user_score += 1
            return True
        else:
            return False

