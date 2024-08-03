number=22

total_sum=0
while number>0:
    sum=number%10
    total_sum+=sum
    number //= 10

print(total_sum)

