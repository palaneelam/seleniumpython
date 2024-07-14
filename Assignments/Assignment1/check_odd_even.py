# Write a program that works out whether if a given number is an odd or even number.
num = input ("Enter Number:")
num = int(num)
print(f"Number entered is {num}")
rem = num%2
if rem == 0:
    print(f"Number entered is even")
else:
    print(f"Number entered is odd")