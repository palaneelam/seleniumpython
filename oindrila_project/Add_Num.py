 #Exercise - Write a program that adds the digits in a 2 digit number.
# For eg.: if the input was 35, then the output should be 3+5 = 8
num = int(input("Enter a Number: "))
result=0
hold=num
while num>0:
    rem=num%10
    result=result+rem
    num=int(num/10)
print("The sum of two digit is",result)