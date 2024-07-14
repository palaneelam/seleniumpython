#Write a program that counts the number of vowels in a given string.

entered_string = input("Enter the input string:")

get_vowel_count = sum(entered_string.upper().count(letter) for letter in "AEIOU")
print(f"Number of vowels in entered string is: {get_vowel_count}")
