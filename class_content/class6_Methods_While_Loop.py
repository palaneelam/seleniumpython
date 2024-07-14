#******************* Defining & Calling Functions ********************************
# Built-n Function - https://docs.python.org/3/library/functions.html- len,print, int(), input()
# user-defined functions - starts with def
# Defining Functions - def my_function():
#                           #Do this

print("Hello")
num_char = len("Hello")
print(num_char)

def my_function():
    print("Hello")
    print("Bye")

my_function()

#*********************** Indentation ***************************************************
# Reading material - https://peps.python.org/pep-0008/
def my_function():
    print("Hello")

#*************************  While Loop ********************************************
#A while loop in Python repeatedly executes a block of code as long as a specified condition is true.
# It has the following syntax:
# while condition:
    # Code block
# The condition is checked before each iteration of the loop. If the condition evaluates to True,
# the code block is executed. After the code block is executed, the condition is checked again.
# If the condition is still True, the code block is executed again. This process continues until
# the condition becomes False, at which poopooint the loop terminates and control passes to the next
# statement after the loop.
# Here's an example of a simple while loop that prints numbers from 1 to 5:
num = 1
while num <= 5:
    print(num)
    num += 1

# Difference between while and for loops:
# The main difference between while and for loops is in their syntax and use cases:
#
# Syntax:
#
# A while loop has a condition that is checked before each iteration.
# A for loop iterates over a sequence (such as a list or range) and executes the code block for each
# element in the sequence.
# Use Cases:
#
# while loops are typically used when you don't know in advance how many times you need to execute
# the loop, or when the loop termination depends on a condition other than iterating over a sequence.
# for loops are used when you want to iterate over a known sequence of elements, such as elements
# in a list, characters in a string, or numbers in a range.
# Practical Examples:
# Use of while loop:
# Calculating factorial of a number until a certain condition is met.
# Implementing a guessing game where the user has multiple attempts to guess a number.
# Calculating factorial using while loop
num = 5
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print("Factorial:", factorial)

# Use of for loop:
# Iterating over elements in a list or range.
# Processing characters in a string.
# Iterating over a list using for loop
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)
#
# # Processing characters in a string using for loop
text = "Python"
for char in text:
    print(char)
# In summary, while loops are used when the number of iterations is not known in advance or
# when the loop termination depends on a condition other than iterating over a sequence, while for
# loops are used for iterating over a known sequence of elements. Both types of loops have their own
# use cases and can be used effectively depending on the specific requirements of the problem.
