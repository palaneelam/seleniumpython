# Given two integer numbers, return their product only if the product is equal to or lower than 1000.
#   Otherwise, return their sum.

print("=======================_Assignment-1_==========================")

def prodSum(num1, num2):
    prod = num1 * num2
    sum = num1 + num2
    result = 0
    if prod <= 1000:
        result = prod
    else:
        result = sum

    # print("Result is: ", result)
    return result


num1 = int(input("Please Enter First Number: "))
num2 = int(input("Please Enter Second Number: "))

print("Final Result is: ", prodSum(num1, num2))


# ----------------------Learning--------------------------------------
# num1 = 100
# num2 = 11
#
# prod = num1 * num2
# sum = num1 + num2
#
# print("First Num: ", num1)
# print("Second Num: ", num2)
# if prod <= 1000:
#     print("prod: ", prod)
# else:
#     print("sum: ", sum)


# num1 = int(input("Please Enter First Number: "))
# num2 = int(input("Please Enter Second Number: "))
#
# prod = num1 * num2
# sum = num1 + num2
#
# print("First Num: ", num1)
# print("Second Num: ", num2)
# if prod <= 1000:
#     print("prod: ", prod)
# else:
#     print("sum: ", sum)
