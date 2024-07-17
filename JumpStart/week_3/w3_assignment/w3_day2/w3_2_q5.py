# - Write a program that takes a non-negative integer as input and returns the sum of its digits.

give_num = input("Please enter number: ")
sum_of_digit = 0
validate_give_num = int(give_num)
if validate_give_num <= 0:
    print("This is NOT a NON-Negative Number")
else:
    print("You entered NON-Negative Number as: ", validate_give_num)
    for i in give_num:
        sum_of_digit = sum_of_digit + int(i)
    print("sum_of_digit: ", sum_of_digit)

# print("sum_of_digit: ", sum_of_digit)



# - ------------------------------
# - Write a program that takes a non-negative integer as input and returns the sum of its digits.

# give_num = input("Please enter number: ")
#
# validate_give_num = int(give_num)
# if validate_give_num <= 0:
#     print("This is NOT a NON-Negative Number")
# else:
#     print("You entered NON-Negative Number as: ", validate_give_num)
#
# sum_of_digit = 0
#
# for i in give_num:
#     sum_of_digit = sum_of_digit + int(i)
#
# print("sum_of_digit: ", sum_of_digit)