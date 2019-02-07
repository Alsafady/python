
# Declare a variable and initialize it

myint = 7
print(myint)

# re-declaring the variable works
myint = 10
print(myint)

myfloat = 7.0
print(myfloat)

myfloat = float(7)
print(myfloat)

mystring = 'hello'
print(mystring)

mystring = "hello"
print(mystring)

mystring = "Don't worry about apostrophes"
print(mystring)

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

a, b = 3, 4
print(a,b)


# Mixing operators between numbers and strings is not supported:
# This will not work!
one = 1
two = 2
hello = "hello"

print(one + two + hello)


# ERROR: variables of different types cannot be combined
#print ("string type " + 123)
print ("string type " + str(123))
