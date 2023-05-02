# # tuple packing and Unpacking
# a = 1,2,3 # Note there is noo small bracket bu t still creates a tuple and called tupe packing

# #The element in the RHS are assigned to each variables in the LHS, This is called tuple
# a, b,c = 1,2, "Hello word"


# #a,b,c = 1,2 # this gives error because in tuple packing, identity and variables should be same in number

# #swapping value by using tuple packing unpackig

# a = 1
# b = 2

# a,b = b,a
# print(a)
# print(b)

# tuple slicing
a = 1,2,3,4,5,6,7,8
print(a[:]) # this gives all value
print (a[::2]) # this traverse throgh all the elements in the tuple but returns on the jump of one

print(a[1:5:2]) # this gives the value form 1 to 5 index , jumping one 

### Now Next example

a = 1,2,3,4,5,6,7,8,9,10
print(a[-2:-10:-2])