# Create a Python set such that it shows the element from both lists in a pair

def create_number_square_set(list1, list2):
    """
    Create a set containing pairs of elements from two lists.

    Parameters:
    list1 (list): The first list of numbers
    list2 (list): The second list of numbers

    Returns:
    set: A set of tuples where each tuple contains an element from list1 and a corresponding element from list2
    """
    # Ensure both lists have the same length
    if len(list1) != len(list2):
        raise ValueError("Length of the lists should be same")

    # Create a set of tuples, each containing an element from list1 and a corresponding element from list2
    number_square_set = {(list1[i], list2[i]) for i in range(len(list1))}

    return number_square_set

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

result = create_number_square_set(first_list, second_list)
print(f"Pairs set: {result}")