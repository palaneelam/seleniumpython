#Create a game where the computer randomly selects a number between 1 and 100, and the player has to guess the number. The computer provides feedback on whether the guess is too high or too low until the player guesses correctly.

import random

def computer_guesses_number():
    """
    A game where the computer randomly selects a number between 1 and 100,
    and the player has to guess the number.
    """
    # Computer selects a random number between 1 and 100
    guess_number = random.randint(1, 100)
    correct_guess = False
    attempts = 0

    print("Hello, Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    # Loop until the player guesses the number correctly
    while not correct_guess:
        try:
            # Player inputs their guess
            player_guess = int(input("Guess the number I have selected: "))
            attempts += 1
            print(f"{attempts}")

            if attempts > 5:
                play_again = input("Do you want to play again(yes/no):")
                attempts = 0
                if (play_again != "yes"):
                    break
                print("Thanks for playing this game with me!")
            else:
                # Provide feedback on the guess
                if player_guess < guess_number:
                    print("Too low! Try again.")
                elif player_guess > guess_number:
                    print("Too high! Try again.")
                else:
                    correct_guess = True
                    print(f"Congratulations! You guessed the correct number {guess_number}")
        except ValueError:
            print(f"Invalid input. Please enter an integer between 1 and 100. Current input is {player_guess}")

computer_guesses_number()