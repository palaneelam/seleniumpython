# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number

def print_current_previous_num(cnum,pnum):
    # cnum = 0
    # pnum = 0

    print(f"Printing current and previous number sum in the range (10)")
    for i in range(10):
        sum = cnum + pnum
        print(f"Current Number {cnum} Previous Number {pnum} Sum: {sum}")
        pnum = cnum
        cnum += 1

def call_print_method():
    cnum = 0
    pnum = 0
    print_current_previous_num(cnum, pnum)
    print(f"Printing is completed")

call_print_method()


