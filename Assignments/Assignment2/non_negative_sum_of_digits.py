#Write a program that takes a non-negative integer as input and returns the sum of its digits.
digit_number = input ("Input any non-negative integer:")
print(f"Non-negative integer entered is {digit_number}")

sumOfDigits = 0 # Initialize variable

for digit in digit_number:
    sumOfDigits += int(digit)

print(f"Addition of the digits: {sumOfDigits}")