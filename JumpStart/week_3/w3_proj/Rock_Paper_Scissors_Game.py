import random

# comp_choice = ["rock", "paper", "Scissor"]
# # random.comp_choice
# print(comp_choice[0])
# print(comp_choice)

# option = ["rock", "paper", "Scissor"]
# comp_choice = random.choice(option)
#
# user_choice = input("Please enter choice rock, paper or Scissor: ")
#
# print("user_choice: ", user_choice)
# print("comp_choice: ", comp_choice)
#
# if (user_choice == "paper" and comp_choice == "rock") or \
#         (user_choice == "rock" and comp_choice == "scissor") or \
#         (user_choice == "scissor" and comp_choice == "paper"):
#     print("You won!")
#
# else:
#     print("You lost and Comp won!")

# if user_choice == "paper" and comp_choice == "rock":
#     print("You won!")
# elif user_choice == "rock" and comp_choice == "scissor":
#     print("You won!")
# elif user_choice == "scissor" and comp_choice == "paper":
#     print("You won!")
# else:
#     print("You lost and Comp won!")

# -------------------------------------------------------------

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


game_images = [rock, paper, scissors]

options = ["ROCK", "PAPER", "SCISSOR"]
comp_choice = random.randint(0, 2)
print("comp_choice: ", comp_choice)
print(game_images[comp_choice])

user_choice = int(input("What do you choose? Type 0 for ROCK, 1 for PAPER or 2 for SCISSOR.\nEnter your choice: "))
print("user_choice: ", user_choice)
print(game_images[user_choice])
print("----------------------------------")
if user_choice < 0 or user_choice > 2:
    print("Please enter valid option")
    print("user_choice: ", user_choice, options[user_choice])
    print("comp_choice: ", comp_choice, options[comp_choice])

elif user_choice == comp_choice:
    print("This is Draw")
    print("user_choice: ", user_choice, options[user_choice])
    print("comp_choice: ", comp_choice, options[comp_choice])

elif user_choice == 0 & comp_choice == 1:
    print("You lost and COMP Won!")
    print("user_choice: ", user_choice, options[user_choice])
    print("comp_choice: ", comp_choice, options[comp_choice])

elif user_choice == 1 & comp_choice == 2:
    print("You lost and COMP Won!")
    print("user_choice: ", user_choice, options[user_choice])
    print("comp_choice: ", comp_choice, options[comp_choice])

elif user_choice == 2 & comp_choice == 0:
    print("You lost and COMP Won!")
    print("user_choice: ", user_choice, options[user_choice])
    print("comp_choice: ", comp_choice, options[comp_choice])

else:
    print("You Won!")
    print("user_choice: ", user_choice, options[user_choice])
    print("comp_choice: ", comp_choice, options[comp_choice])


print("Thank you")
