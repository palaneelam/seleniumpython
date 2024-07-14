import random

choices = ['rock', 'paper', 'scissor']


def computer_choice():
    return random.choice(choices)


def get_user_choice():
    user_choice = input("Enter your choice from - rock, paper & scissor")
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice from - rock, paper & scissor: ")
    return  user_choice

def game_rules(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie"
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "scissor" and computer_choice == "paper") or \
        (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer Win!"

def play_by_rules():
    user_choice = get_user_choice()
    get_computer_choice = computer_choice()
    print(f"Computer choose: {get_computer_choice}")
    result = game_rules(user_choice,get_computer_choice)
    print(result)

def play_game():
    print("Welcome to the game - ROCK, PAPER, SCISSOR!")
    while True:
        play_by_rules()
        play_again = input("Do you want to play again(yes/no):")
        if (play_again != "yes"):
            break
        print("Thanks for playing this game with me!")


play_game()