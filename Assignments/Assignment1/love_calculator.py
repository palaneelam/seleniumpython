# Write a program that tests the compatiability between two people
# To work out the love score between two people:
#   1. Take both people's name and check for the number of times th letters in the word TRUE occurs.
#   2. Then check for the number of times the letters in the work LOVE occurs.
#   3. Then combine these numbers to make a 2 digit number.
# For Love scores less than 10 or greater than 90, the message should be:
# "Your score less than 10 or greater than 90, then message should be:
# "Your score is 'x' you go together like coke and mentos
# For love scores between 40 and 50, the message should be:
# "Your score is 'x' you are alright together.
# otherwise, the message will just be their score. e.g: "Your score is z"

person1 = input ("Enter First Person Name:")
print(f"Name entered is {person1}")
person2 = input ("Enter Second Person Name:")
print(f"Name entered is {person2}")

joinedname = person1 + person2
print(f"Joined name is: {joinedname}")

get_true_count = sum(joinedname.upper().count(letter) for letter in "TRUE")
print(f"{get_true_count}")
get_love_count = sum(joinedname.upper().count(letter) for letter in "LOVE")
print(f"{get_love_count}")
true_love_count = get_true_count + get_love_count

print(f"Love Compatibility Score is: {true_love_count}")

if true_love_count < 10 or true_love_count > 90:
    print(f"Your score is less than 10 or greater than 90")
elif 40 < true_love_count < 50:
    print(f"Your score is {true_love_count} you are alright together")
else:
    print(f"Your score is {true_love_count}")
