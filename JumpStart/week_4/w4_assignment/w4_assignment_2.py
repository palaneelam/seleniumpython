# Write a program to iterate the first 10 numbers, and in each iteration,
# print the sum of the current and previous number.

print("=======================_Assignment-2_==========================")

sum = 0
for i in range (10):
    if i == 0:
        priev_num = 0
        curr_num = 0
    else:
        priev_num = i-1
        curr_num = i

    sum = priev_num + curr_num
    print(f"Sr.No._: {i+1}. current Number is {curr_num}, previous Number is {priev_num}, and sum: ", sum)
