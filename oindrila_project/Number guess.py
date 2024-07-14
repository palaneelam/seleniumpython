import random
import math

comp_selected_num = random.randint(1, 100)
print(comp_selected_num)

user_guess_num = int(input("Please enter your guess: "))
while user_guess_num != comp_selected_num:
    # print("Your guess is correct")
    # user_guess_num = int(input("Please enter your guess: "))
    # comp_selected_num == user_guess_num

    if user_guess_num > comp_selected_num:
        print("Your guess is high")
        user_guess_num = int(input("Please enter your guess: "))

    elif user_guess_num < comp_selected_num:
        print("Your guess is Low")
        user_guess_num = int(input("Please enter your guess: "))

    elif user_guess_num == comp_selected_num:
        print("Your guess is correct")