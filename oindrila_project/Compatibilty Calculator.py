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
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combine_name = (name1 + name2).lower()
#TRUE
nrT = combine_name.count("t")
nrR = combine_name.count("r")
nrU = combine_name.count("u")
nrE = combine_name.count("e")
nrTrue = nrT + nrR + nrU + nrE

#LOVE
nrL = combine_name.count("l")
nrO = combine_name.count("o")
nrV = combine_name.count("v")
nrLove = nrL + nrO + nrV + nrE

str_totalNr = str(nrTrue) + str(nrLove)
int_totalNr = int(str_totalNr)

#Find the compatibility
if int_totalNr > 40 and int_totalNr < 50:
    print(f"Your score is {str_totalNr}, you are alright together.")
elif int_totalNr <= 10 or int_totalNr >= 90:
    print(f"Your score is {str_totalNr}, you go together like coke and mentos.")
else:
    print(f"Your score is {str_totalNr}")