#************************************ Python Loops ****************************************************
from random import random

fruits = ['Apple', 'Peach', 'Pear']
for fruit in fruits:
    print("Fruit name:",fruit)
    print(fruit + 'Pie')
    print(fruits)
print(fruits)

#************************** For loops and the range() function *****************************
# for number in range(1,11,3)
#   print(number)

total=0
for number in range(1,101):
    total += number
print(total)
