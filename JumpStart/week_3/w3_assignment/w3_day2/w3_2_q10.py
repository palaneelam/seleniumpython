# Write a function to merge two sorted lists into a single sorted list.
# The function should take two lists as input and return a merged, sorted list.

# list_1 = [2, 4, 8, 6]
# list_2 = [9, 7, 11]
# list_1.sort()
# list_2.sort()
# print(list_1)
# print(list_2)
# merged_list = list_1 + list_2
# merged_list.sort()
# print(merged_list)

# list_1 = [2, 4, 8, 6]
# list_2 = [9, 7, 11]
# list_1.sort()
# list_2.sort()
# print(list_1)
# print(list_2)
# merged_list = list_1 + list_2
# merged_list.sort()
# print(merged_list)

# def sorted_list(list_1, list_2):
#     merged_list = list_1 + list_2
#     merged_list.sort()
#
#     return merged_list
#     # print(merged_list)
#
#
# list_1 = [2, 4, 8, 6, 1, 99]
# list_2 = [9, 7, 11, 49]
#
# # returned_merged_sorted_list = sorted_list(list_1, list_2)
# # print("returned_merged_sorted_list: ", returned_merged_sorted_list)
#
# print("returned_merged_sorted_list: ", sorted_list(list_1, list_2))

# **************************************************************************
def sorted_list(list_1, list_2):
    merged_list = list_1 + list_2
    merged_list.sort()

    return merged_list


list_1 = [2, 4, 8, 6, 1, 99]
list_2 = [9, 7, 11, 49]

print("returned_merged_sorted_list: ", sorted_list(list_1, list_2))