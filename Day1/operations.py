#Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
print("hello world")
#Airthmatic opertaions.
a = 5
b = 3

#addition
c = a + b
print(c)

#substraction
c = a - b
print(c)


# multiplication
c = a * b
print(c)

#division

c = a/b 
print(c)

#floor division
c = a//b

print(c)

#Modulus

c = a % 2
print(c)

# Exponent operator

c = a ** 2
print(c)

########Comparision Opearators######
#equals to
print(a==b)

#not equals to

print(a != b)

#greater than or equals

print( a >= b)

#less than or equals to 

print ( a<= b)

#Greater than 

print (a > b)

# less than 

print (a < b)

#####logical operators###
a = True
b = False
# and or and not are the logical operators in python

print(a and b)

print(not a)

print(a or b )

# identity operator (is & is not)

print(a is b)  # we can check id of the object bulit id function

# membership operator # (in & not in )

a = [1,2,3]
print(2 in a )
print(4 in a)

# Assignment operator

a = 5 
a = a + 1 # this gives a as 3 
print(a)
a += 1
print(a)

# precedence and associativity

print(3 * 5//5) # associativity is left to right
print(3**2**4) # associativity is right to left


