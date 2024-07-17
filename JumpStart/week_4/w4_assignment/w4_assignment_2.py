# Write a program to iterate the first 10 numbers, and in each iteration,
# print the sum of the current and previous number.

print("=======================_Assignment-2_==========================")

sum = 0
for i in range (1, 10+1):
    # print(i)
    priev_num = i-1
    curr_num = i
    sum = priev_num + curr_num
    sum = priev_num + curr_num
    print(f"Sr.No._: {i}. current Number is {curr_num}, previous Number is {priev_num}, and sum: ", sum)