# __Exercise-1: ****************************************************************************
# Exercise-1 - Write a program that adds the digits in a 2 digit number.
# For eg.: if the input was 35, then the output should be 3+5 = 8
# ---------------------------------------------------------------------------

# req_num = input("Please Enter 2 digit number: ")
# sum_digits = 0
# for dig in req_num:
#     sum_digits = sum_digits + int(dig)
#
# print(sum_digits)


# __Exercise-2: ****************************************************************************
# Exercise-2: Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# You should convert the bmi to a whole number and print out a whole number in order to pass all the tests.
# For ex: weight = 80, height = 1.75 m - then BMI = weight / height*height = 26.122 or 26
# ---------------------------------------------------------------------------

# user_weight = float(input("Please Enter Weight of user(in KG): "))
# user_Height = float(input("Please Enter Height of user(in meter): "))
# BMI = ((user_weight)/(user_Height*user_Height))
# print("User BMI is: ", BMI)
# print("User BMI is: ", BMI.__floor__())


# __Exercise-3: ****************************************************************************
# Exercise-3: Write a program that works out whether if a given number is an odd or even number.
# Even numbers can be divided by 2 with no remainder - num%2 == 0
# ---------------------------------------------------------------------------

# user_num = int(input("please enter Number to test even/ Odd: "))
# remainder = (user_num)%2
# if remainder == 0:
#     print("Given Number is Even")
# else:
#     print("Given Number is Odd")


# __Exercise-4: ****************************************************************************
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height
# It should tell them the interpretation of their BMI based on the BMI value.
#        Under 18.5 they are underweight
#        Over 18.5 but below 25 they have a normal weight
#        Over 25 but below 30 they are slightly overweight
#        Over 30 but below 35 they are obese
#        Above 35 they are clinically obese
# ---------------------------------------------------------------------------

# user_weight = float(input("Please Enter Weight of user(in KG): "))
# user_Height = float(input("Please Enter Height of user(in meter): "))
# BMI = ((user_weight)/(user_Height*user_Height))
# print("User BMI is: ", BMI)
# # print("User BMI is: ", BMI.__floor__())
#
# if BMI <= 18.5:
#     print("User is Under Weight")
# elif 18.5 < BMI <=25:
#     print("User is Normal Weight")
# elif 25 < BMI <= 30:
#     print("User is Slighly Over Weight")
# elif 30 < BMI <= 35:
#     print("User is obese")
# else:
#     print("User is clinically obese")

# __Exercise-5: ****************** LOVE CALCULATORS ****************************************
# __Exercise-5: Write a program that tests the compatiability between two people
# To work out the love score between two people:
#   1. Take both people's name and check for the number of times the letters in the word TRUE occurs.
#   2. Then check for the number of times the letters in the word LOVE occurs.
#   3. Then combine these numbers to make a 2 digit number.

# For Love scores less than 10 or greater than 90, the message should be:
# "Your score less than 10 or greater than 90, then message should be:
# "Your score is 'x' you go together like coke and mentos

# For love scores between 40 and 50, the message should be:
# "Your score is 'x' you are alright together.

# otherwise, the message will just be their score. e.g: "Your score is z"
# ---------------------------------------------------------------------------

# first_Person = input("Enter First Person name: ")
# second_Person = input("Enter Second Person name: ")
# love_text = "LOVE"
# print("first_Person: ", first_Person)
# print("second_Person: ", second_Person)
# print("love_text: ", love_text)

# name = "MANORANJAN"
# count_num = 0
# for let in name:
#     if let == "A":
#         count_num = count_num + 1
#     print(let)
#
# print("count_num: ", count_num)

# __Exercise-6: ****************************************************************************
# print numbers from 1 to 100
# if nbr is divisible by 3 then print "fizz"
# if nbr is divisible by 5 then print "buzz"
# if nbr is divisible by 3 & 5 , then print "fizzbuzz"
# Output:
# 1,2,fizz,4,5,fizz,7,8,9,buzz,11,fizz,13,14,fizzbuzz,..... 100
# ---------------------------------------------------------------------------

# user_number = int(input("Please enter Number: "))

#
for user_number in range (1, 101):
    rem_div_3 = user_number%3
    rem_div_5 = user_number%5
    rem_div_3_and_5 = user_number%15

    # if ((rem_div_3 != 0) & (rem_div_5 != 0) & (rem_div_3_and_5 != 0)):
    #     print(user_number)

    if ((rem_div_3 == 0) and (rem_div_5 == 0)):
        print("Fizz_Buzz")
    elif rem_div_3 == 0:
        print("FIZZ")
    elif rem_div_5 == 0:
        print("Buzz")
    else:
        print(user_number)

#
