"""
@bref -> practicar input y sentencia if - elif - else
Programa que calcula el precio de una pizza, de acuerdo al tamaño, peperoni y extra queso

"""

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S" or size == "s":
    bill += 15
elif size == "M" or size == "m":
    bill += 20
elif size == "L" or size == "l":
    bill += 25
else:
    print("Sorry, please enter S, M, or L.")

if pepperoni == "Y" or pepperoni == "y" :
    if size == "S" or size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y" or extra_cheese == "y":
    bill += 1

print(f"Your final bill is: ${bill}.")