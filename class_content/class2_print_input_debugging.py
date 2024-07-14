# **********************  Interactive Coding Exercise - Printing  **********************
print("Day1 - Python print function")
print("The function is declared like this:")
print("print('what to print')")
print("Hello world!\nHello world!")

# **********************  Debugging Practice  ****************************************
# 1. Missing double quotes before the word Day.
# print(Day 1 - String Manipulation)
print("Day 1 - String Manipulation")

# 2. Outer double quotes changed to single quotes.
print('String Concatenation is done with the "+" sign.')

# 3. Extra indentation removed
print('e.g. print("Hello " + "world")')

# 4. Extra ( in print function removed.
# print(("New lines can be created with a backslash and n."))
print("New lines can be created with a backslash and n.")

# **********************  Input Function  ****************************************
# input("A prompt for the user)
input("What is your name?")
print("Hello " + input("What is your name?") + "!")

# Exercise - Provide any name in input box and print the length of name value
print(len(input("Enter your name please: ")))

# Doing the same thing using variables
name = input("What is your name?")
print(name)
nameLength = len(name)
print(nameLength)

# Numbers written like 345,123,456,678 are written as 345_456_678_987 in python programing language
print(123_456 + 345_345_45)

# ********************************************************************************************************************
# Type Error, Type Checking and Type Conversion
# ********************************************************************************************************************

num_char = len(input("What is your name"))
# print("Your name has "+num_char+" characters.")
# the above code will show error as u can't concatenate string and integer.
# To resolve this issue, convert/typecast int into string.

new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = float(123)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))

# ********************************************************************************************************************
# Mathematical Operations in python
# + add
# - subtract
# * multiply
# / division
# ** exponents
# Rules for priority is PEMDAS - Parenthesis, Exponents, Multiplication, Division, Addition, Subtraction

# **************************** Round function ***********************
bmi = 12.3456
print("BMI as round off: ",round(bmi,2))

# **************************** Floor Division ***********************
result = 8 // 3
print("Result from floor division:", result)

score = 0
score += 1 # or score = score+1
print("Score is: ", score)

# *********************************************************************
# Exercise - Create a program using maths and f-strings that tells us
# how many weeks we have left, if we live until 90 years old. It will
# take your current age as input and output message with our time left in this format:
# You have x weeks left
# where x is replaced with the actual calculated number of weeks the input age has left until age 90
# *********************************************************************
current_age = input("Enter your current age: ")
years = 90 - int(current_age)
weeks = years * 52
print(f"You have {weeks} left")