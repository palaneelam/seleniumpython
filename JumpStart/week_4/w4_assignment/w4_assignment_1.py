# Given two integer numbers, return their product only if the product is equal to or lower than 1000.
#   Otherwise, return their sum.

print("=======================_Assignment-1_==========================")

num1 = 100
num2 = 11

prod = num1 * num2
sum = num1 + num2

print("First Num: ", num1)
print("Second Num: ", num2)
if prod <= 1000:
    print("prod: ", prod)
else:
    print("sum: ", sum)