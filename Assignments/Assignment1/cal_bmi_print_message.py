# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height
# It should tell them the interpretation of their BMI based on the BMI value.

weight = input ("Enter Weight:") # Weight in KGs
weight = float(weight)
print(f"Weight entered is {weight}")
height = input ("Enter Height:") # Height in metres
height = float(height)
print(f"Height entered is {height}")

bmi1 = weight / (height*height)
bmi = int(bmi1)

print(f"Calculated BMI: {bmi}")

if bmi < 18.5:
    print(f"Your are underweight")
elif 18.5 <= bmi <= 25:
    print(f"Your weight is normal")
elif 25 <= bmi <= 30:
    print(f"Your are slightly overweight")
elif 30 <= bmi <= 35:
    print(f"Your are obese")
elif bmi > 35:
    print(f"Your are clinically obese")