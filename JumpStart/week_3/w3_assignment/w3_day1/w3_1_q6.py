# __Exercise-6: ****************************************************************************
# print numbers from 1 to 100
# if nbr is divisible by 3 then print "fizz"
# if nbr is divisible by 5 then print "buzz"
# if nbr is divisible by 3 & 5 , then print "fizzbuzz"
# Output:
# 1,2,fizz,4,5,fizz,7,8,9,buzz,11,fizz,13,14,fizzbuzz,..... 100
# ---------------------------------------------------------------------------

# user_number = int(input("Please enter Number: "))

#
for user_number in range (1, 101):
    rem_div_3 = user_number%3
    rem_div_5 = user_number%5
    rem_div_3_and_5 = user_number%15

    # if ((rem_div_3 != 0) & (rem_div_5 != 0) & (rem_div_3_and_5 != 0)):
    #     print(user_number)

    if ((rem_div_3 == 0) and (rem_div_5 == 0)):
        print("Fizz_Buzz")
    elif rem_div_3 == 0:
        print("FIZZ")
    elif rem_div_5 == 0:
        print("Buzz")
    else:
        print(user_number)
