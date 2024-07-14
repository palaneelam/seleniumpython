#****************************************************************************************************
# What is a Namespace?
# A namespace in Python is essentially a system to ensure that all the names in a program are unique
# and can be used without any conflict. It maps every name to a corresponding object, allowing you
# to refer to the object by its name.

# Types of Namespace:
# Global Namespace: This namespace includes names at the top level of the Python script or module.
# It's accessible throughout the entire module.

# Local Namespace: This namespace includes names inside a function. It's accessible only within the
# function where it's defined.

# Built-in Namespace: This namespace includes built-in functions and built-in exception names.
# It's automatically loaded when Python starts.

# How Namespaces Work:
# When you define a variable, function, class, or any other object in Python, it gets stored in a
# namespace.
# Python uses namespaces to determine the scope of a name, whether it's a local variable, a global
# variable, or a built-in function.
# Namespaces help in avoiding naming conflicts and make the code more organized and modular.

# Example:
# Global namespace
global_var = 10

def example_function():
    # Local namespace
    local_var = 20
    print(global_var)  # Accessing global variable within function
    print(local_var)

example_function()

# Built-in namespace
print(len("hello"))  # len is a built-in function

# In this example:

# global_var belongs to the global namespace and is accessible throughout the script.
# local_var belongs to the local namespace of the example_function and is accessible only within that
# function.
# len is a built-in function provided by Python and belongs to the built-in namespace.

# Usage:
# Namespaces help in organizing code by keeping variables, functions, and classes in separate containers.
# They enable code reusability by allowing you to define objects with the same name in different
# namespaces without conflicts.
# Understanding namespaces is crucial for debugging, as it helps in identifying scope-related issues
# and resolving them effectively.
# By leveraging namespaces effectively, you can write cleaner, more modular, and maintainable Python
# code.

#*************************************************************************************************
# Using global varibale
num = 1

def printNumber():
    global num
    num = num+1
    print(num)

# global variables are used for declaring global constants like pi, URL etc.
# These varibales as a naming convention must be written in capital letter

PI = 3.14159
URL = "google.com"