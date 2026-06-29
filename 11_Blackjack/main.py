"""
@bref Juego de Blackjack, el jugador con cartas mas cercanas a la suma de 21, gana.
El Blackjack (21) se consigue solo con 2 cartas, 10 y 11, si la computadora las obtiene,
esta gana sin importar las cartas del usuario. Si el usuario obtiene mas de 21, pierde
inmediatamente. El 11 es comodin, puede ser 1 o 11; es 1 cuando la suma de sus
cartas > 21.
@bref
"""

import random
import art

def deck():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

#-----------------------------

def compare(user_cards, computer_cards):
    if sum(computer_cards) == 21 and len(computer_cards) == 2:
        print("Blackjack !!... PC wins")
    elif (sum(user_cards)) > 21:
        print("You went over. You Loose 😭 ")
    elif (len(user_cards) == 2) and (sum(user_cards) == 21):
        print("Win with a Blackjack !!!")
    elif (sum(computer_cards)) == (sum(user_cards)):
        print("It's a Draw 🙃")
    elif sum(computer_cards) > 21:
        print("PC went over. You Win 😁!!")
    elif sum(user_cards) > sum(computer_cards):
        print("You Win  😃!!")
    else:  #sum(computer_cards) > sum(user_cards):
        print("PC wins !!!")
#-----------------------------

def add_cart(list_cards):
    card = deck()
    if card == 11 and (sum(list_cards) + card) > 21:
        card = 1
    elif (11 in list_cards) and (sum(list_cards) + card > 21):
        # cambia 11 a 1 cuando sobrepase 21 con la nueva carta
        list_cards = [1 if x == 11 else x for x in list_cards]

    list_cards.append(card)

    return list_cards

#--------------------------------

def new_game():
    user_cards = []
    computer_cards = []

    print("\n"*20)
    user_other_card = True
    pc_other_card   = True
    print(art.logo)

    for j in range(2):

        user_cards     = add_cart(user_cards)
        computer_cards = add_cart(computer_cards)

        if sum(computer_cards) == 21:
            pc_other_card = False

    while user_other_card:

        #solo se muestra la primera computer_card al usuario
        print(f"    Your Cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"    Computer's first card: {computer_cards[0]} ")

        user_new_card = input("Type 'y' to get another card or type 'n' to pass: ").lower()
        if user_new_card == 'y':
            user_cards = add_cart(user_cards)
        else:
            user_other_card = False

        if sum(user_cards) > 21:
            pc_other_card   = False
            user_other_card = False


    while pc_other_card:

        pc_sum = sum(computer_cards)
        if pc_sum < 17:
            computer_cards = add_cart(computer_cards)
        else:
            pc_other_card = False

    print(f" Your final hand is: {user_cards}, final score: {sum(user_cards)}")
    print(f" Computer's final hand: {computer_cards}, final score: {sum(computer_cards)} \n")

    compare(user_cards, computer_cards)

    print("\n")
#-----------------------------

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    new_game()
else:
    print("\n\nOk..... bye")

