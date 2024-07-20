# 1.
import math
from collections import deque
from functools import reduce

import numpy

total = 0
for i in range(1,11):
    total += i
print(total)

# 2.
total = sum(range(1,11))
print(total)

# 3
total = 0
i = 1
while i<=10:
    total += i
    i += 1
print(total)

# 4 - list comprehension
total = sum([i for i in range(1,11)])
print(total)

# 5
total = reduce(lambda x,y:x+y, range(1,11))
print(total)

# 6 recursion
def sum_total(n):
    if n == 1:
        return 1
    else:
        return n+sum_total(n-1) # 10+sum(9) --- 10+45 = 55
                                # 9+sum(8) -- 9+36
                                # 8+sum(7) --- 8+28
                                # 7+sum(6) --- 7+ 21
                                # 6+sum(5) --- 6+ 15
                                # 5+sum(4) --- 5+10
                                # 4+sum(3) -- 4+ 6
                                # 3+sum(2) -- 3+3
                                # 2+sum(1) --3
                                # 2+1 = 3
                                # 3+1

total = sum_total(10)
print(total)


# 7 -airthematic progressin
n = 10
total = n * (n+1) // 2
print(total)

# 8
total = math.fsum(range(1,11))
print(total)

# 9
total = numpy.sum(numpy.arange(1,11))
print(total)

# 10
total = sum(i for i in range(1,11))
print(total)

# 11
numbers = deque(range(1,11))
total = sum(numbers)
print(total)

# 5 = 5*4*3*2*1




















