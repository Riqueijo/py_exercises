#!/usr/bin/env python
"""
some exercises to develop my logic
"""
__author__ = "Henrique Daguerre"

from random import randint

options = ["Rock", "Paper", "Scissor"]
user_choice = int(input("Choice: "))
bot_choice = int(randint(0, 2))


if user_choice <= 2:
    print(options[user_choice] + " vs " + options[bot_choice] )

    if user_choice - bot_choice == 0:
        print("Draw!")

    elif bot_choice == 0:
        if user_choice == 1:
            print("you win!")
        elif user_choice == 2:
            print("bot win!")

    elif bot_choice == 1:
        if user_choice == 2:
            print("you win!")
        elif user_choice == 0:
            print("bot win!")

    elif bot_choice == 2:
        if user_choice == 1:
            print("you win!")
        elif user_choice == 0:
            print("bot win!")
else:
    quit()