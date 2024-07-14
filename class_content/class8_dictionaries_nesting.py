# ******** Dictionaries, Nesting & the secret auction *******************************************
# 1. The Python Dictionary
#       Key         Value
#       Bug         An error in a program that prevents the program from running as expected
#       Function    A piece of code that you can easily call over and over again
#       Loop        The action of doing something over and over again
#  Syntax: {key: Value}
#          {"Bug": "An error in a program that prevents the program from running as expected",
#           "Function": "A piece of code that you can easily call over and over again",
#           "Loop": "The action of doing something over and over again"}

programing_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Function": "A piece of code that you can easily call over and over again",
    "Loop": "The action of doing something over and over again"
}

# Retrieving items from dictionary
print(programing_dictionary["Bug"])

# Adding new items to dictionary
programing_dictionary["LoopNew"] = "The action of doing something over and over again"
print(programing_dictionary)

# Create an empty dictionary
empty_dictionary = {}

# Wiping an exisiting dictionary
programing_dictionary = {}
print(programing_dictionary)

# Edit an item in a dictionary
programing_dictionary["Bug"] = "A moth in your computer"
print(programing_dictionary)

# Loop through a dictionary
for key in programing_dictionary:
    print(key)
    print(programing_dictionary[key])

# ****************** Nesting Lists and Dictionaries ************************************
# We can use list and dictionary both as key values. For eg.:
# {
#   Key: [List],
#   Key2: {Dict},
# }

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a dictionary
travel_log = {
    "France": {"Cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"Cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 10},
}

# Putting everything a nested list format
travel_log = {
    {"country": "France", "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    {"country": "Germany", "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 10},
}

# Putting everything in more readable format -  A list which contains 2 items
# and each item is a dictionary
# and each dictionary has 3 key value pairs
# and they all contain different types of data. First one has value as string,
# second one has a list, third one has number

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 10
    },
]
