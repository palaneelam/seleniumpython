#print numbers from 1 to 100
# if nbr is divisible by 3 then print "fizz"
# if nbr is divisible by 5 then print "buzz"
# if nbr is divisible by 3 & 5 , then print "fizzbuzz"
# Output:
# 1,2,fizz,4,5,fizz,7,8,9,buzz,11,fizz,13,14,fizzbuzz,..... 100
# Iterate through numbers from 0 to 50 using the range function
for fizzbuzz in range(100):
    # Check if the current number is divisible by both 3 and 5 (i.e., divisible by 15)
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        # If divisible by both 3 and 5, print "fizzbuzz" and continue to the next iteration
        print("fizzbuzz")
        continue
    # Check if the current number is divisible only by 3
    elif fizzbuzz % 3 == 0:
        # If divisible only by 3, print "fizz" and continue to the next iteration
        print("fizz")
        continue
    # Check if the current number is divisible only by 5
    elif fizzbuzz % 5 == 0:
        # If divisible only by 5, print "buzz" and continue to the next iteration
        print("buzz")
        continue
    # If the number is neither divisible by 3 nor 5, print the number itself
    print(fizzbuzz)


