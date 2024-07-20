# Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list

def arrange_list_by_dict_values(main_list, dictionary_list):
    """
    Iterate through a list and remove elements that do not exist as values in the dictionary.

    Parameters:
    lst (list): The list of elements to check
    dct (dict): The dictionary whose values to check against

    Returns:
    list: A filtered list containing only elements that exist as values in the dictionary
    """
    # Create a set of dictionary values for faster lookup
    dict_values = set(dictionary_list.values())

    # Iterate over the list and remove elements that are not in the dictionary values
    i = 0
    while i < len(main_list):
        if main_list[i] not in dict_values:
            main_list.pop(i)
        else:
            i += 1

    return main_list


input_list = [10, 20, 30, 40, 50]
input_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

result = arrange_list_by_dict_values(input_list, input_dict)
print(f"Arranged List: {result}")


