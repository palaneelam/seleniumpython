#Write a function to merge two sorted lists into a single sorted list. The function should take two lists as input and return a merged, sorted list.


def merge_sorted_lists(list1,list2):

    merged_list = [] #Initialize empty merged list
    i, j = 0, 0        # Initialize variables

    while i < len(list1): #Itereate till the length of the list
        merged_list.append(list1[i]) #Append list1 to merged_list
        i += 1

    while j < len(list2): #Itereate till the length of the list
        merged_list.append(list2[j]) #Append list2 to merged_list
        j+=1

    return merged_list

list1 = [1, 2, 3, 4, 5] #Initialize list1
list2 = [10, 20, 30, 40, 50] #Initialize list2

sorted_lists = merge_sorted_lists(list1, list2)
print(f"Merged sorted list is: {sorted_lists}")