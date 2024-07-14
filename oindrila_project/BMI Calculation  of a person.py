# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height
# It should tell them the interpretation of their BMI based on the BMI value.
#        Under 18.5 they are underweight
#        Over 18.5 but below 25 they have a normal weight

the_height = float(input("Enter the height in cm: "))
the_weight = float(input("Enter the weight in kg: "))
the_BMI = the_weight / (the_height/100)**2
if the_BMI <= 18.5:
    print("Oops! You are underweight eat healthy.",the_BMI)
elif the_BMI <= 25:
    print("Awesome! You are healthy keep it up.","your BMI is ",the_BMI)
elif the_BMI <= 35:
    print("Eee! You are overweight contact dietetian.",the_BMI)
else:
    print("Seesh! You are obese sorry.",the_BMI)

#Exercise - Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# You should convert the bmi to a whole number and print out a whole number in order to pass all the tests.
# For ex: weight = 80, height = 1.75 m - then BMI = weight / height*height = 26.122 or 26

height_of_user=float(input("Enter height"))
weight_of_user=float(input("Enter weight"))
BMI_of_user=int(weight_of_user/(height_of_user/100)**2)
print("your expected BMI Is"," ",BMI_of_user)