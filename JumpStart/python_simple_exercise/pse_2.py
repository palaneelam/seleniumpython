# Write a Python program to check if a number is even or odd.

# *************************************************************************
# Method-1
# given_num = 4.3
#
# if given_num % 2 == 0:
#     print("Result by Method-1 --> Given Num is EVEN")
# elif given_num % 2 == 1:
#     print("Result by Method-1 --> Given Num is ODD")
# else:
#     print("Result by Method-1 --> Given Num is NOT an Integer")

# *************************************************************************
# Method-2
# user_num = int(input("Enter Number to check ODD or EVEN: "))
# if user_num % 2 == 0:
#     print("Result by Method-2 --> Given Num is EVEN")
# elif given_num % 2 == 1:
#     print("Result by Method-2 --> Given Num is ODD")
# else:
#     print("Result by Method-2 --> Given Num is NOT an Integer")

# *************************************************************************
# Method-3

# def check_num(checkNum):
#     checkNum_result = ""
#     if checkNum % 2 == 0:
#         checkNum_result = "EVEN"
#         print(f"Result by Method-3 --> Given Num {checkNum} is {checkNum_result}")
#     elif given_num % 2 == 1:
#         checkNum_result = "ODD"
#         print(f"Result by Method-3 --> Given Num {checkNum} is {checkNum_result}")
#     else:
#         print("Result by Method-3 --> Given Num is NOT an Integer")
#
#
# check_num(9)

# *************************************************************************
# Method-4

def check_give_num(check_Given_Num):
    checkNum_result = ""
    if check_Given_Num % 2 == 0:
        given_Num_result = "EVEN"
        # print("Result by Method-3 --> Given Num is EVEN")
        print(f"Result by Method-4 --> Given Num {check_Given_Num} is {given_Num_result}")
    elif check_Given_Num % 2 == 1:
        given_Num_result = "ODD"
        # print("Result by Method-3 --> Given Num is ODD")
        print(f"Result by Method-4 --> Given Num {check_Given_Num} is {given_Num_result}")
    else:
        given_Num_result = "NOT an Integer"
        # print("Result by Method-3 --> Given Num is NOT an Integer")
        print(f"Result by Method-4 --> Given Num {check_Given_Num} is {given_Num_result}")

    return given_Num_result


print(f"Result by Method-4 -->", check_give_num(11.4))
