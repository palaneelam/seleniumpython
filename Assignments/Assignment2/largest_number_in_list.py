#Write a program that takes a list of numbers and returns the largest number in the list.
def get_largest_number(numbers):

    largest_number = numbers[0]
    for number in numbers:
        if number > largest_number:
            largest_number = number

    return largest_number

#numbers = input("List of numbers:")
#print(f"{numbers}")
numbers = [10, 20, 30, 40, 50]
largest_number = get_largest_number(numbers)
print(f"Largest number in the list is: {largest_number}")
