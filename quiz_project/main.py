from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_list = []
for ques in question_data:
    question_list.append(Question(ques["text"], ques["answer"]))

quiz_1 = QuizBrain(question_list)
quiz_1.start_quiz()