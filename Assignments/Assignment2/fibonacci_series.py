#Write a function that generates the first n Fibonacci numbers. The function should take n as an argument and return a list of the first n Fibonacci numbers.
def generate_fibonacci(n):
    """
    Generate the first n Fibonacci numbers.

    Parameters:
    n (int): The number of Fibonacci numbers to generate

    Returns:
    list: A list containing the first n Fibonacci numbers
    """

    fibonacci_numbers = [] # Initializes an empty list

    i, j = 0, 1 # Initialize the variables
    for _ in range(n):
        fibonacci_numbers.append(i) # appends the fibonacci numbers to the list
        i, j = j, i + j

    return fibonacci_numbers # returns the value

n = int(input ("Input the number to generate fibonacci series:")) # Takes the input
fibonacci_series = generate_fibonacci(n) # calls the function to generate fibonacci series
print(f"The first {n} Fibonacci numbers are: {fibonacci_series}")
