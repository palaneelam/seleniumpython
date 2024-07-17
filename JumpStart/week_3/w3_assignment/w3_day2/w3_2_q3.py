# Write a program that takes a list of numbers and returns the largest number in the list.

# num_list = [2, 3, 5]
# num_list_len = num_list.__len__()
# print("num_list_len: ", num_list_len)
#
# max_num_list_indx = num_list_len-1
# print("max_num_list_indx: ", max_num_list_indx)
# print("==============================================")
# largest_Num = 0
#
# for i in range(1, num_list_len):
#     if largest_Num < num_list[i-1]:
#         largest_Num = num_list[i-1]
#     else:
#         largest_Num = num_list[i]
#
# print("largest_Num: ", largest_Num )


# num_list = [4, 2, 6]
# num_list_len = num_list.__len__()
# print("num_list_len: ", num_list_len)
# largest_Num = 0
# next_Num = []
#
# for usr_num in num_list:
#     fnum = num_list[0]
#
#     for take_next_num in range(1, num_list_len+1):
#         if fnum > num_list[take_next_num]:
#             larNum = fnum
#         # print("Greatest Num is: ", largest_Num)
#     else:
#         larNum = num_list[take_next_num]
#         # print("Greatest Num is: ", largest_Num)
#
# print("Greatest Num is: ", largest_Num)
    # print(un)

# ==============================================================
given_num_list = [2, 3, 91, 5]
# given_num_list_sort = given_num_list.sort() - why this is NOT working?
given_num_list.sort()
print("Largest element is:", given_num_list[-1])

# ---------------------------------------------------------
# list of numbers
list1 = [10, 20, 4]

# sorting the list
list1.sort()
# list1 = list1.sort()
# list_sorted = copy(list1.sort())

# printing the last element
print("Largest element is:", list1[-1])

