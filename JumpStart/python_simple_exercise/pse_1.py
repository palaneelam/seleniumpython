# Write a Python program to find the sum of two numbers.

# Method-1
num1, num2 = 4, 5
sum = num1 + num2
print("Result by Method-1 --> Sum of num1 and num2 is: ", sum)

# Method-2
num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num1: "))
print("Result by Method-2 --> Sum of num1 and num2 is: ", num1 + num2)


# Method-3

def sum_of_2_num(num1, num2):
    sum = num1 + num2
    print("Result by Method-3 --> Sum is: ", sum)
    return sum


sum_of_2_num(3, 4)


# Method-4
def sum_of_2_nums(num1, num2):
    sum = num1 + num2
    # print("Result by Method-3 --> Sum is: ", sum)
    return sum


print("Result by Method-4 --> Sum of 2 num is: ", sum_of_2_nums(3, 5))
