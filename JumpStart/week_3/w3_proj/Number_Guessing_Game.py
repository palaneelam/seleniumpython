# Project Description:
# Create a game where the computer randomly selects a number between 1 and 100, and # the player has to guess the number.
# The computer provides feedback on whether the guess is too high or too low until the player guesses correctly.
# Function to check user's guess against actual answer
# Choosing a random number between 1 and 100.
# Make function to set difficulty
# Let the user guess a number
# Function to check user's guess against actual answer
# Track the number of turns and reduce by 1 if they get it wrong.
# Repeat the guessing functionality if they get it wrong.
# ***********************************************************************************************

import random

comp_selected_num = random.randint(1, 100)
print(comp_selected_num)

user_guess_num = int(input("Please enter your guess: "))
while user_guess_num != comp_selected_num:
    # print("Your guess is correct")
    # user_guess_num = int(input("Please enter your guess: "))
    # comp_selected_num == user_guess_num

    if user_guess_num > comp_selected_num:
        print("Your guess is high")
        # user_guess_num = int(input("Please enter your guess: "))

    elif user_guess_num < comp_selected_num:
        print("Your guess is Low")
        # user_guess_num = int(input("Please enter your guess: "))

    # elif user_guess_num == comp_selected_num:
    #     print("Your guess is correct")

    user_guess_num = int(input("Please enter your guess: "))

print("Your guess is correct")
