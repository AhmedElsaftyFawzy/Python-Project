class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        if len(self.question_list) > self.question_number:
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number+1}: {current_question.text} (True/False)? ")
        self.question_number += 1
        self.check(answer, current_question.answer)

    def check(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print('You got it right')
            self.score += 1
        else:
            print('that is wrong')

        print(f'the correct answer: {correct_answer}')
        print(f"This your score : {self.score}/{self.question_number}")
