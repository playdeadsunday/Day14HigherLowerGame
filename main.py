from higher_lower_art import logo, vs
from higher_lower_data import data
import random

import os
def clear(): return os.system('cls')


def fetch():
    return random.choice(data)


def compare(one,two):
    highest = 0
    if one['follower_count'] > two['follower_count']:
        return one
    else:
        return two


def game():
    clear()
    contenders = []
    message = ""
    score = 0
    should_continue = True
    while should_continue:
        print(logo)

        if len(contenders) != 0:
            print(message)

        while len(contenders) < 2:
            acc = fetch()
            contenders.append(acc)

        if contenders[0] == contenders[1]:
            contenders.pop()
            contenders.append(fetch())

        a = contenders[0]
        b = contenders[1]

        print(f"Compare A: {a['name']}, a {a['description']} from {a['country']}")

        print(vs)

        print(f"Against B: {b['name']}, a {b['description']} from {b['country']}")

        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_input == "a":
            guess = a
        elif user_input == "b":
            guess = b

        max = compare(a, b)
        if max == guess:
            score += 1
            message = f"You're right! Current score: {score}."
            contenders[0] = contenders[1]
            contenders.pop()
            clear()
        else:
            clear()
            print(logo)
            message = f"Sorry that's wrong. Final score: {score}"
            print(message)
            should_continue = False


game()
