#Write a Python program to find the largest number among three numbers.
a=90
b=80
c=989
if(a>b and a>c):
    print("Largest number is ",a)
else:
    if(b>c and b>a):
        print ("The largest number is ",b)
    else:
        print("The largest number is ",c)

