# Given two list of numbers, write a program to create a new list such that the new list
# should contain odd numbers from the first list and even numbers from the second list.

print("=======================_Assignment-4_==========================")

list_1 = [1, 2, 3, 4, 5]
list_2 = [1, 2, 3, 4, 5]
even_list = []
odd_list = []
final_list_odd_n_even = []

for l1 in list_1:
    if l1 % 2 == 0:
        print("Even Number: ",l1)
        # even_list = [l1]
        print(even_list[l1])


for l2 in list_2:
    if l2 % 2 == 1:
        print("Odd Number: ",l2)
        # odd_list = [l2]
        print(odd_list)


final_list_odd_n_even = even_list + odd_list
print(final_list_odd_n_even)

