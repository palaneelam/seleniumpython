# Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

def create_odd_even_list(list1, list2):
    """
    Create a new list containing odd numbers from the first list and even numbers from the second list.

    Parameters:
    list1 (list): The first list of numbers
    list2 (list): The second list of numbers

    Returns:
    list: A new list containing odd numbers from list1 and even numbers from list2
    """
    # Get odd numbers from the first list
    odd_numbers = [num for num in list1 if num % 2 != 0]
    print(f"Odd List: {odd_numbers}")

    # Get even numbers from the second list
    even_numbers = [num for num in list2 if num % 2 == 0]
    print(f"Even List: {even_numbers}")

    # Combine the odd and even numbers into a new list
    odd_even_list = odd_numbers + even_numbers
    # print(f"Combined List: {odd_even_list}")

    return odd_even_list

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [8, 9, 10, 11, 12, 13, 14]

result = create_odd_even_list(list1, list2)
print(f"New list: {result}")
