# Write a Python program to remove duplicates from a list.
# *************************************************************************
# Method-1

# my_list = [1, 2, 7, 3, 4]
# list_size = my_list.__len__()
# print(my_list)
# print(list_size)
# unique_list = []
# count = 0
#
# for scom in range(0, list_size):
#     for comp in range(0, list_size-1):
#         print("my_list - set Num for compare: ", my_list[scom])
#         print("my_list - Next Num to COMPARE: ", my_list[comp+1])
#         if my_list[scom] != my_list[comp]:
#             print(f"Found Duplicate as: {my_list[scom]}")
#         else:
#             count += 1
#
#
# print("count: ", count)



# # *************************************************************************
# # Method-2
# my_list = [1, 2, 7, 3, 4, 1]
# print(my_list)
# unique_list = set(my_list)
# print(unique_list)

# *************************************************************************
# Method-3
orig_list = [2, 4, 6, 8, 10]
size = orig_list.__len__()
print("Size of List is: ",size)
uniq_list = []
print(orig_list)
print("-============================================-")
# for list_elmnt in range(size-1):
#     print("Element in List: ", orig_list[list_elmnt])
#     print("Next Element in list: ", orig_list[list_elmnt+1])
#     print("------------------------------")
    # if list_elmnt == list_elmnt+1:
    #     print("Duplicate")
    # else:
    #     print("No Duplicate")

for fe in range(size-1):
    print("Element in List: ", orig_list[fe])
    print("Next Element in list: ", orig_list[fe+1])
    for ne in range(size-1):
        if orig_list[fe] == orig_list[ne]:
            continue
        if orig_list[fe] == orig_list[ne+1]:
            print("Duplicate Found")
        else:
            print("NO Duplicate Found")


    print("------------------------------")


# *************************************************************************
# Method-4

# *************************************************************************
# Method-5



# =====================================================================================
