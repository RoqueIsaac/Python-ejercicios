"""
@bref -> Practicar  sentencias  If - elif - else,
el programa hace que el usuario encuentra un tesoro, selecionando 1 de las
opciones o caminos para llegar al tesoro
"""

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

side = input("You are at a cross road. Where yo do want to go ? type 'left' or 'right' ").lower()
if side == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    swim = input("type 'wait' to wait for a boat or 'swim' to swim across ").lower()
    if swim == "wait":
        print("You are in the boat and found 3 doors")
        door  = input("Select red, blue or yellow: ").lower()
        if door == "red":
            print("Burned by fire. Game Over")
        elif door == "blue":
            print("Eaten by beasts. Game Over")
        elif door == "yellow":
            print("You found the treasure !!")
        else:
            print("Game Over")
    else:
        print("Attacked by trout. Game over")
else:
    print("Fall into a hole. Game Over")



