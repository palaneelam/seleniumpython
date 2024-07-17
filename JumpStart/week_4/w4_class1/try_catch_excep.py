
# ZeroDivisionError: division by zero
# ValueError: invalid literal for int() with base 10: 'a'

a = 10
try:
    num = int(input("Please enter number to divide a: "))
    result = a/num
except ZeroDivisionError as e:
    print("Error is: ", e)

except ValueError as ve:
    print("Error is: ", ve)

except Exception as excp:
    print("Error is: ", excp)

print("Result: ", result)


print("Devision completed")