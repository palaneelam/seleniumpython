#***************************************  Randomisation and python lists ***********************************
import random

random_integer = random.randint(1,10)
print(random_integer)

#0.000000 - 0.99999999 (generates between 0 and t but doesnt inclde 1)
random_float = random.random()
print(random_float)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")
#***********************************************************************************************

#*********************** Understanding the offset and appending items to Lists *******************************************************
# Python list is a kind of data structure
# when multiple pieces of data that has some sort of connection between them. For ex..
# all states in US make sense to be in list or all fruit names in one single variable.
states_of_america = ['Delaware', 'Pennysylvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland',
                     'South Carolina', 'New Hampshire', 'Virginia', 'New York','North Carolina', 'Rohode Island',
                     'Vermont', 'Kentucky',"Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
                     'Illinois', 'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas',
                     'IOWA','Wisconsin', 'California', 'Minnesota', 'Oregon', 'Kansas', 'West Virginia', 'Nevada',
                     'Nebraska', 'Colorado', 'North Dakota', 'South Dakota', 'Montana', 'Washington', 'Idaho', 'Wyoming',
                     'Utah', 'Oklahoma', 'New Mexico', 'Arizona', 'Alaska','Hawaii']

print("First state value:",states_of_america[0])
print("Last state value:",states_of_america[-1])

# appends to the end of the list
states_of_america.append("NeelamLand")
states_of_america.extend(['NeelamLand', 'New MoonsLand'])
states_of_america.insert(0,'New Value')
states_of_america.remove('Pennysylvania')
print(states_of_america)

#******************************** IndexErrors and Working with Nested Lists  *****************************************
nbr = len(states_of_america)
print('Number of states in America: ', nbr)

# print(states_of_america[nbr])
print(states_of_america[nbr-1])

dirty_dozen = ['Strawberries', 'Spinach', 'Kale', 'Nectarines', 'Apples','Grapes', 'Peaches', 'Cherries',
               'Pears', 'Tomatoes', 'Celery', 'Potatoes']

fruits = ['Strawberries', 'Nectarines', 'Apples','Grapes', 'Peaches', 'Cherries','Pears']
vegetables = ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']

dirty_dozen = [fruits,vegetables]

print(dirty_dozen)
