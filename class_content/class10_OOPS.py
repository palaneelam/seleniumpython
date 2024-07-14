# https://docs.python.org/3/library/turtle.html#turtle.shape
# import turtle
from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()

#**********************************************************
#How to add python packages and use PyPi - Practice Modifying Object attributes and calling methods

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Employee Name", ["Neelam", "Deepti"])
table.add_column("City", ["Pune", "Delhi"])
table.add_column("Country", ["India", "India"])
print(table.align)
table.align = "l"
print(table)

#********************************************************************
# Working with Attributes, Class Constructors and the __init__() function

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# user_1 = User()
# user_1.id = "001"
# user_1.username = "Neelam"
#
# print(user_1.username)
#
# user_2 = User()
# user_2.id = "002"
# user_2.name = "Pal"

user_1 = User("001", "Neelam")
user_2 = User("002", "jack")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)



