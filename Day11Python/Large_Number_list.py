num1=[100,300,20]

if(num1[0]>num1[1] and num1[0]>num1[2]):
    print("The largest number is :",num1[0])
else:
    if(num1[1]>num1[0] and num1[1]>num1[2]):
        print("The Largest number is :",num1[1])
    else:
        print("The largest number is :", num1[2])