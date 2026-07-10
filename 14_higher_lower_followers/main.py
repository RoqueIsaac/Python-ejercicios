import random
import os

import art
from game_data import data

print(art.logo)
score = 0
game = True

data1 = random.choice(data)

while game:
    print(f"Compare A: {data1['name']}, a {data1['description']}, from: {data1['country']}  ")

    print(art.vs)
    data2 = random.choice(data)
    if data1 == data2:
        data2 = random.choice(data)

    print(f"Against B: {data2['name']}, a {data2['description']}, from: {data2['country']} ")

    user_choose=input("Who has more followers ? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(art.logo)

    if user_choose == 'a' and (data1['follower_count'] > data2['follower_count']):
        score += 1
        print(f"You're right! Current score: {score}")
    elif user_choose == 'b' and (data1['follower_count'] < data2['follower_count']):
        score += 1
        print(f"You're right! Current score: {score}")
        data1 = data2
    else:

        print(f"Sorry, that's wrong. Final score: {score}")
        game = False
        break




