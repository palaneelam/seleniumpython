# alt+enter - show context menu/action
# ctrl+w - select the line of code(s)
# ctrl + shift + w - deselect the lines of code
# ctrl + / - comment / uncomment block of code
# ctrl + d = duplicate line(s)
# ctrl + y = delete the line(s)
# ctrl + minus = collapse
# ctrl + equals = expand
# ctrl + shift + minus = collapse all similar regions in the code
# ctrl + shift + equals = expand all similar regions in the code
# ctrl + alt + t = surround the code with template code
# ctrl + shift + delete = unwrap your code from the template code
# alt + j = select the similar keyword from the code
# alt + shift + j = deselect the selected similar keyword from the code
# shift + F6 = renaming same varibale in the entire file
# ctrl + alt + v = replace the entire expression or statement with some variable across the file
# to restore code from local history -> right click on editor white space and select open history -> show local history

import random


def add_nbrs(a, b):
    if a and b:
        return 1
    return 2
    print("Hello World!")
    print("Hello Everyone!")

    print("Hello Today!")

    print("Hello Noone!")


def add_nbrs1(a, b):
    if a and b:
        return 1
    return 2
    print("Hello World!")
    print("Hello Everyone!")
    print("Hello Today!")
    print("Hello Noone!")


def random_method(y):
    print(y + random)

print("Hello there!")


def bubble_sort(arr):
    n = len(arr)
    for j in range(n):
        for i in range(0, n - j - 1):
            i_ = arr[i] > arr[i + 1]
            if i_:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

































