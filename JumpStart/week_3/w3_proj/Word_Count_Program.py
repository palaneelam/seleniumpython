# Project Description:
# Write a program that takes a text input from the user and counts the
# number of words, characters, and lines in the input.

user_input = input("Please enter word/ sentence: ")

user_input_word = user_input.split(" ")
# print(user_input_word)
print("Total words are: ", user_input_word.__len__())

user_input_char = user_input.replace(" ", "")
# print(user_input_char)
print("Total Letters are: ", user_input_char.__len__())