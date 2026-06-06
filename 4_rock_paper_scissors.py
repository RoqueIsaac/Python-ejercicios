"""
@bref Juego de piedra, papel y tijeras

"""
import random as ran

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
optionS = ["Rock", "Paper", "Scissors"]
opt = ["0", "1", "2"]
pc = ran.randint(0, 2)

print("\n    Rock - Paper - Scisors -> Game\n")
user = input("What do you choose? 0 for Rock, 1 Paper, 2 Scissors -> ")

i=0
while i == 0:
    if user not in opt:
        print("\nInvalid option. Try again.")
        user = input("0 for Rock, 1 Paper, 2 Scissors -> ")
    else:
        i=1
        user =int(user)

print(f"\nYou chose: {optionS[user]}")
print(options[user])
print(f"Computer chose: {optionS[pc]}")
print(options[pc])

if user == pc:
    print("It's a draw!")
elif (user == 0 and pc == 2) or (user == 1 and pc == 0) or (user == 2 and pc == 1):
    print("User win")
else:
    print("Computer win")






