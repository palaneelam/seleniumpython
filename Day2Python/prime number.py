num=11
if (num>1):
    for i in range(2,num):
     if(num%i==0):
        print ("The number is not prime",num)
        break
    else:
        print("The number is prime",num)
else:
   print("Not Prime")
