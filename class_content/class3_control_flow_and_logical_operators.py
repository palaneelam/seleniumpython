# ******************************* Control Flow and Logical Operators ****************************************************
# if condition:
#   do this
# else:
#   do this
# *********************************************************************************************************************

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

# *********************************************************************************************************************
# Comparison Operators:
#     >     Greater than
#     <     Less than
#     >=    Greater than or equal to
#     <=    Less than or equal to
#     ==    Equal to
#     !=    Not equal to

# ******************************* Nested If-Else Statement ***********************************
# Nested If statements:
# if condition:
#   if another condition:
#         do this
#     else:
#         do this
# else:
#   do this
# if/elif/else
# if condition1:
#   do A
#   elif condition2:
#     do B
#   else:
#     do this
# *********************************************************************************************************************
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# ******************************** Multiple if Statements ***********************************************************

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age!"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3

    print("Your final bill is:",bill)

# ******************************* Logical Operators *****************************************************************
# A And B
# C or D
# not E
# *********************************************************************************************************************
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age!"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3

    print("Your final bill is:",bill)
