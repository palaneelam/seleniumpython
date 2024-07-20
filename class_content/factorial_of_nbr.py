import math

#1
print(math.factorial(5))

#2
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)

#3
n = 5
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(factorial)

4
def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

print(factorial_recursive(5))

#5 - creating function
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_iterative(5))

#6
fact = 5
result = 1
while fact >= 1:
    result = result * fact
    fact -= 1
print(result)



