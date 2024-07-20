# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

def palindrome_num(number):
    """
    Check if the given number is a palindrome without using slicing.

    Parameters:
    number (int): The number to check

    Returns:
    bool: True if the number is a palindrome, False otherwise
    """
    actual_number = number
    reversed_number = 0

    while number > 0:
        pal_num_generator = number % 10  # Get the last digit
        reversed_number = reversed_number * 10 + pal_num_generator  # Build the reversed number
        number = number // 10  # Remove the last digit from the original number

    return actual_number == reversed_number

number = int(input("Enter a number: "))
if palindrome_num(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
