

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.marks = 0
        self.question_list = question_list

    def next_question(self):
        self.question_number += 1
        print(f"Q. {self.question_number}: {self.question_list[self.question_number].text} True/ False")

    def score(self, ans):
        if self.question_list[self.question_number].answer == ans:
            print("Yep! Correct answer")
            self.marks += 1
        else:
            print("sorry! Wrong answer")

    def start_quiz(self):
        while self.question_number < len(self.question_list)-1:
            self.next_question()
            self.score(input())
            print(f"score: {self.marks}/{self.question_number}")

