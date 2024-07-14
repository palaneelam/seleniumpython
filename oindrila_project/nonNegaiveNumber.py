Num=int(input("Enter the Number"))
result=0
Digit=Num

while Num>0:
    rem=Num%10
    result=result+rem
    Num=int(Num/10)


print(result)


