import math

# Method - 1
num = 5
result = num * (num-1) * (num-2) * (num-3) * (num-4)
print("Method - 1: ", result)


# -- Method - 2
result = 1
req_result = 1
for i in range(5, 0, -1):
    # print(i)
    req_result = req_result * i

# print(req_result)
print("Method - 2: ", req_result)


# -- Method - 3
print("Method - 3:", math.factorial(5))

# -- Method - 4

fact = 5
result = 1
while fact >= 1:
    # result = fact * (fact - 1) #
    # final_result = result*result
    # print(result)
    result *= fact
    fact -= 1

# print(result)
print("Method - 4:", result)

