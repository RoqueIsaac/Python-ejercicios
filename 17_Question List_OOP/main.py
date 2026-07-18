
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    #se crea una lista de objetos tipo Question, que tienen attributos text y answer
    #question es un elemento de la lista que a su vez es un diccionario
    question_bank.append(Question(question["question"], question['correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your score is: {quiz.score}/{quiz.question_number}")

