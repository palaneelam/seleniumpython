# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

print("=======================_Assignment-3_==========================")

def pal_num(orig):
    revrs = orig[::-1]
    orig_num = int(orig)
    revrs_num = int(revrs)
    # print("orig_num: ", orig_num)
    # print("revrs_num: ", revrs_num)
    if orig_num == revrs_num:
        print(f"Given Number {orig_num} is palindrome number")
    else:
        print(f"Given Number {orig_num} is NOT palindrome number")


user_num = input("Enter Num: ")
pal_num(user_num)



# -----------------------------------learning-----------------------------
# orig = input("Enter Num: ")
# revrs = orig[::-1]
#
# orig_num = int(orig)
# revrs_num = int(revrs)
#
# print("orig_num: ", orig_num)
# print("revrs_num: ", revrs_num)
#
# if orig_num == revrs_num:
#     print("Given Number is palindrome number")
# else:
#     print("Given Number is NOT a palindrome number")