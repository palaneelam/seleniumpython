# Write a Python program to check if a number is prime.

# *************************************************************************
# Method-1
# Result - 2, 3, 5, 7, 11, 13, 17

# num = 12
# for i in range(2, num-1):
#     if (num % 1 == 0) and (num % num == 0) : # and (num % i != 0)
#         result = "PRIME"
#         print(i)
#     else:
#         result = "NOT a PRIME"
#
# print(f"Given number {num} is {result} number")


num = 8
count = 0

for i in range(1, num+1):
    if num % i == 0:
        count += 1

if count == 2:

    print("Num is PRIME")
else:
    print("Num is NOT PRIME")

# while num != 0:
#     if num



#     if (num % 1 == 0) and (num % num == 0) : # and (num % i != 0)
#         result = "PRIME"
#         print(i)
#     else:
#         result = "NOT a PRIME"
#
# print(f"Given number {num} is {result} number")

# *************************************************************************
# Method-2


# *************************************************************************
# Method-3


# *************************************************************************
# Method-4

# *************************************************************************
# Method-5



# =====================================================================================
