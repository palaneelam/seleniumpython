str = "Hello"
print(str)

b,c,d = 5,6,"Great"

print(f"Value is {b}")
print(f"Value of c:", c)
print("Value of d:", d)

print(type(c))
print(type(d))

#******************** Python Numeric data types ****************************

#create a variable with integer value.
a=100
print("The type of variable having value", a, " is ", type(a))

#create a variable with float value.
b=10.2345
print("The type of variable having value", b, " is ", type(b))

#create a variable with complex value.
c=100+3j
print("The type of variable having value", c, " is ", type(c))

#********************** Python String data types *****************************

a = "string in a double quote"
b= 'string in a single quote'
print(a)
print(b)

# using ',' to concatenate the two or several strings
print(a,"concatenated with",b)

#using '+' to concate the two or several strings
print(a+" concated with "+b)

#**************************** List data types ***********************************

#list of having only integers
a= [1,2,3,4,5,6]
print(a)

#list of having only strings
b=["hello","john","reese"]
print(b)

#list of having both integers and strings
c= ["hey","you",1,2,3,"go"]
print(c)

#index are 0 based. this will print a single character
print(c[1]) #this will print "you" in list c

#************************* Tuple *****************************************************data
# The tuple is another data type which is a sequence of data similar to a list.
# But it is immutable. That means data in a tuple is write-protected.
# Data in a tuple is written using parenthesis and commas.

#tuple having only integer type of data.
a=(1,2,3,4)
print(a) #prints the whole tuple

#tuple having multiple type of data.
b=("hello", 1,2,3,"go")
print(b) #prints the whole tuple

#index of tuples are also 0 based.

print(b[4]) #this prints a single element in a tuple, in this case "go

# ************************* Dictionaries *****************************************************
# Python Dictionary is an unordered sequence of data of key-value pair form.
# It is similar to the hash table type. Dictionaries are written within curly braces in the form
# key:value. It is very useful to retrieve data in an optimized way among a large amount of data.
#a sample dictionary variable

a = {1:"first name",2:"last name", "age":33}

#print value having key=1
print(a[1])
#print value having key=2
print(a[2])
#print value having key="age"
print(a["age"])