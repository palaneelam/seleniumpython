#16.	Write a Python program to find the common elements between two lists.-

a=[11,12,40]
b=[23,11,40]
if(a[0]==b[0] or a[0]==b[1] or a[0]==b[2]):
    print ("The common is ",a[0])
if (a[1]==b[0] or a[1]==b[2] or a[1]==b[1]):
     print ("The common is",a[1])
if(a[2]==b[0] or a[2]==b[1] or a[2]==b[2]):
    print("The common is",a[2])

