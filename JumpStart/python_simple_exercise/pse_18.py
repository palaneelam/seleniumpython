# Write a Python program to find the index of an element in a list.
# *************************************************************************
# Method-1
my_list = [2, 4, 6, 8, 4, 10]
print(my_list)
size = len(my_list)
# print(size)

element = 4
# index =
result = ""

for i in range(0, size):
    # print("element: ", element)
    # print("For Loop Num: ", i)
    # print("my_list[i]: ", my_list[i])
    if element == my_list[i]:
        result = "Existed"
        index = i
        # print("index: ", index)
        print(f"Method-1 >> Subject element is '{result}' and INDEX is '{index}'")
    else:
        result = "NOT Existed"
        index = "OUT OF INDEX"
        # print(f"Method-1 >> Subject element is '{result}' and INDEX is '{index}'")

    # print(f"Method-1 >> Subject element is '{result}' and INDEX is '{index}'")

# *************************************************************************
# Method-2

# *************************************************************************
# Method-3


# *************************************************************************
# Method-4

# *************************************************************************
# Method-5



# =====================================================================================
