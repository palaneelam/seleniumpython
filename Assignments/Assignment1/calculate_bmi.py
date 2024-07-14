# Exercise - Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

weight = input ("Enter Weight:") # Weight in KGs
weight = float(weight)
print(f"Weight entered is {weight}")
height = input ("Enter Height:") # Height in metres
height = float(height)
print(f"Height entered is {height}")

bmi1 = weight / (height*height)
bmi = int(bmi1)

print(f"Calculated BMI: {bmi}")