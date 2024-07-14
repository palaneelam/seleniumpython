# Exercise - Write a program that adds the digits in a 2 digit number.
two_digit_number = input ("Input any two digit number:")
print(f"Two digit number entered is {two_digit_number}")
d1 = two_digit_number[0]
print(f"First Digit:{d1}")
d2 = two_digit_number[1]
print(f"Second Digit:{d2}")

sumOfDigits = int(d1) + int(d2)
print(f"Addition of the digits: {sumOfDigits}")