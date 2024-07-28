# Write a Python program to find the index of an element in a list.
# *************************************************************************
# Method-1
my_list = [2, 4, 6, 8, 10]
print(my_list)
size = my_list.__len__()
# print(my_list.__len__())

element = 12
index = 0
result = ""

for i in range(0, size):
    if element == my_list[i]:
        result = "Existed"
        index = i
    else:
        result = "NOT Existed"
        index = "OUT OF INDEX"

print(f"Method-1 >> Subject element is '{result}' and INDEX is '{index}'")

# *************************************************************************
# Method-2

# *************************************************************************
# Method-3


# *************************************************************************
# Method-4

# *************************************************************************
# Method-5



# =====================================================================================
