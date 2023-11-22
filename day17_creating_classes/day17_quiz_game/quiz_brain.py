class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        correct_answer = current_question.answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False) ").lower()
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"Correct answer")
        else:
            print(f"Wrong answer")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your correct score is: {self.score}/{self.question_number}\n")