# factorial
import math

#1
n = math.factorial(5)
print(n)

#2
n = 5
total = n*(n-1)*(n-2)*(n-3)*(n-4)
print(total)

#3
def factorial(n):
    m = 0
    j = 1
    for i in range(n,m,-1):
        j = j*i
    return j

result = factorial(5)
print(result)

#4
def factorial_forward(n):
     j = 1
     for i in range(1,n+1):
         j *= i
     return j

result = factorial_forward(5)
print(result)

 #5
def factorial_whileloop(n):
    j = 1
    while n > 0:
        j = j*n
        n = n-1
    return j
result = factorial_whileloop(5)
print(result)
