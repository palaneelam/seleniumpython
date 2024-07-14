# print("hello, here we are doing addition of two numbers")
# a = input(f"Enter first number:")
# b = input(f"Enter second number:")
# c = float(a)+float(b)
# print(f"Addition of {a} and {b} is:",c)
#
#_______________________________________________
# # Exercise - Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# # You should convert the bmi to a whole number and print out a whole number in order to pass all the tests.
# # For ex: weight = 80, height = 1.75 m - then BMI = weight / height*height = 26.122 or 26
# #        Under 18.5 they are underweight
# #        Over 18.5 but below 25 they have a normal weight
# #        Over 25 but below 30 they are slightly overweight
# #        Over 30 but below 35 they are obese
# #        Above 35 they are clinically obese
#
#____________________________
print("Lets calculate the Body Mass Index(BMI)")
weight= input("Enter your weight in k.g:")
height= input("Enter you Height in meter:")
c = int(weight) / (float(height) * float(height))
print("Your BMI is ", c)
if c < 18.5:
    print("The individual is  underweight")
elif ((c>18.5) and (c<25)):
    print("The individual has normal weight")
elif ((c>25) and (c<30)):
    print("The individual is slightly overweight")
elif ((c>30) and (c<35)):
    print("The individual is obese")
else:
    print("The individual is clinically obese")
#___________________________
# print("Let's check if the number is even or odd")
# num1=input("Enter a number:")
# if int(num1) % 2 == 0:
#     print(f"The number {num1}  is even")
# else:
#     print(f"The number {num1} is odd")
# ----------------------------
# print("We are printing 1 to 100 numbers here")
# for i in range (1,101,1):
#     if ((i%3==0) and (i%5==0)):
#         print("fizzbuzz")
#     elif i%3==0:
#         print("fizz")
#     elif i%5==0:
#         print("buzz")
#     else:
#         print(int(i))
# _____________________
# print("This is a lover calculator")
# name1=input("Enter first name:")
# name2=input("Enter second name:")
# combination=name1+name2
# print(combination)
# count1=0
# count2=0
# for i in range (combination):
#     if str.count(t):
#         count1=count1+1
#     elif str.count(r):
#         count1=count1+1
#     elif str.count(u):
#         count1=count1+1
#     elif str.count(e):
#         count1 = count1+1
#     else:
#         print("calculation for true is done")

#----------------------------------------
# def love_calculator():
#     name1 = str(input("please enter your name:"))
#     name2 = str(input("please enter your name:"))
#     word1, word2 = list('true'), list('love')
#     count1=0
#     count2 = 0
#     for i in name1+name2:
#         if i in word1:
#             count1 += 1
#     for i in name1+name2:
#         if i in word2:
#             count2 += 1
#     score = int(str(count1) + str(count2))
#     if score<10 or score>90:
#         print("Your score is", score, "you go together like coke and mentos.")
#     elif score>40 and score<50:
#         print("Your score is", score, "you are alright together.")
#     else:
#         print("your score is ", score)
#
# love_calculator()