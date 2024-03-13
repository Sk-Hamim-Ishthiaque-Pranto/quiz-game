class QuizBrain:
    correct_count = 0

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def still_has_a_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        user_ans = input(
            f"Q.{self.question_number + 1} {self.question_list[self.question_number].text} (True/False): ")
        self.check_ans(user_ans, self.question_list[self.question_number].answer)
        self.question_number += 1

    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.correct_count += 1
            print("You got the right answer")
        else:
            print('You are wrong ')
        print(f"The right answer is {correct_ans}")
        print(f"Your current score is {self.correct_count}/{self.question_number + 1}")
        print()
