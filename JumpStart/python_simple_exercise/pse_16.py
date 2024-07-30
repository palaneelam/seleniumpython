# Write a Python program to find the common elements between two lists.
# *************************************************************************
# Method-1
print("Test")

list_1 = [2, 4, 6, 8]
list_2 = [3, 5, 2, 4, 9, 11, 2, 8]
duplicate_element = []

for i in range(0, list_1.__len__()):
    # print("Element from List_1: ", i)
    for j in range(0, list_2.__len__()):
        print("Element from List_1: ", list_1[i])
        print("Element from List_2: ", list_2[j])
        if list_1[i] == list_2[j]:
            common_element = list_1[i]
            duplicate_element.append(list_1[i])
            print("Duplicate common_element: ", common_element)
    print("++++++++++++++++++++++++++++++++++")

print("duplicate_element: ", duplicate_element)
# duplicate_element
# *************************************************************************
# Method-2


# *************************************************************************
# Method-3


# *************************************************************************
# Method-4

# *************************************************************************
# Method-5



# =====================================================================================
