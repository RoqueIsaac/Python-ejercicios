
class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.questions_list = q_list

    def next_question(self):
        question = self.questions_list[self.question_number]
        #incrementa el valor para mostrarlo en el Q., sin embargo la pregunta es el elemento de
        #la lista antes del incremento
        self.question_number += 1

        user_answer = input(f"Q.{self.question_number}: {question.text} (True / False): )?: ")
        self.check_answer(user_answer, question.answer)

    def still_has_question(self):
        return self.question_number < len(self.questions_list)


    def check_answer(self, answer,correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")





