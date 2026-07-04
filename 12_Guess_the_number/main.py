import random
import art


def new_game():
    game = input("\nDo you want to play again? Type 'y' or 'n': ").lower()
    if game == "y":
        print("\n" * 20)
        return True
    else:
        print("\nThanks for playing! Goodbye!")
        return False
#-----------------------------------

def guess_num():
    num = random.randint(1, 100)
    return num
#-----------------------------------


def guess_nm():
    attempts = 0
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if level == "easy":
        attempts = 10
    else:
        attempts = 5

    guess_number = guess_num()

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_number = int(input("Make a guess: "))
        if user_number > guess_number:
            print("Too high !")
        elif user_number < guess_number:
            print("Too low !")
        elif user_number == guess_number:
            print(f"You got it !!, The answer was {guess_number}.")
            break
        attempts -= 1
        if attempts == 0:
            print("\nYou've run out of guesses. ")
            print(f"the right answer was {guess_number}.")
        else:
            print("Guess Again!")


var = True
while  var:
    guess_nm()
    var = new_game()