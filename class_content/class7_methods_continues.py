# *********** Function Parameters  ****************************

# 1. Functions with Inputs
import math
# from art import logo

def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today")


greet()


# *** Function that allows for input
# def my_function(something):
#     Do this with something
#     Then do this
#     Finally do this

# something (parameter) = 123 (argument)

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"how do you do {name}")


greet_with_name("Neelam")


# Function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


greet_with("Neelam", "Pune")


# Positional Arguments
# def my_function(a,b,c):
#     # Do this with a
#     # Then do this with b
#     # finally do this with c

# keyword arguments
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


greet_with(location="Pune-MH", name="Neelam Pal")


# Function with outputs
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return (f"{formatted_f_name} {formatted_l_name}")


print(format_name("NeEELam", "pAl"))


# Multiple return values

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    f"Result: {formated_f_name} {formated_l_name}"


# Storing output in a variable
formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)
# or printing output directly
print(format_name(input("What is your first name? "), input("What is your last name? ")))

# Already used functions with outputs.
# length = len(formatted_name)


# Return as an early exit
def format_name(f_name, l_name):
    """Take a first and last name and format it
  to return the title case version of the name."""
    if f_name == "" or l_name == "":
        pass
        # return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

format_name("Neelam", "pal")
