# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum

def get_product_sum(num1, num2):
    """
        Return the product of two numbers if it is less than or equal to 1000.
        Otherwise, return their sum.

        Parameters:
        num1 (int): The first integer number
        num2 (int): The second integer number

        Returns:
        int: The product or the sum of the two numbers
        """
    product = num1 * num2
    addition = num1 + num2
    if product <= 1000:
        return product
    else:
        return addition

def product_or_sum():
    num1 = int(input("Enter 1st Integer:\n"))
    print(f"1st Integer is: {num1}")
    num2 = int(input("Enter 2nd Integer:\n"))
    print(f"2nd Integer is: {num2}")
    result = get_product_sum(num1,num2)
    print(f"Result of 2 integers is: {result}")

product_or_sum()



