# print numbers from 1 to 100
# if nbr is divisible by 3 then print "fizz"
# if nbr is divisible by 5 then print "buzz"
# if nbr is divisible by 3 & 5 , then print "fizzbuzz"
# Output:
# 1,2,fizz,4,5,fizz,7,8,9,buzz,11,fizz,13,14,fizzbuzz,..... 100

num = 1
while num <= 100:
    div3 = num%3
    div5 = num%5
    if div3 == 0:
        print(f"fizz", end=' ')
        num = num +1
    elif div5 == 0:
        print(f"buzz", end=' ')
        num = num +1
    elif div3 == 0 and div5 == 0:
        print(f"fizzbuzz", end=' ')
        num =- num +1
    else:
        print(f"{num}", end=' ')
        num = num +1