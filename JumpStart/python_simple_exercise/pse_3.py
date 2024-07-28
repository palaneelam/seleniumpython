# Write a Python program to find the largest number among three numbers.

# *************************************************************************
# Method-1
num1, num2, num3 = 8, 11, 7

if num1 > num2 and num1> num3:
    print(f"Result by Method-1 --> {num1} is greatest in {num1}, {num2}, {num3}")
elif num2 > num1 and num2 > num3:
    print(f"Result by Method-1 --> {num2} is greatest in {num1}, {num2}, {num3}")
else:
    print(f"Result by Method-1 --> {num3} is greatest in {num1}, {num2}, {num3}")