# #- Numbers
# # String
# # Boolen
# # List
# # Tuple
# # Set
# # Dictionary
# # lets start with examples
# a = 1
# print(type(a))

# # to check the type of the data we use type() built in function
# # for example
# a = 2e3
# print(a)
# print(type(a))
# b = int(a)
# print(b)
# ## 
# print(3e3654789) # this gives infinity value (inf)
# ## 
# print(1e-2)
# ## Complex data type
# b = 3 +4j
# print(b)
# print(type(b))

# ## List data types
# ## mutable - can be changed or modified
# ## Immutable - cannot be changed or modified
# a = [1,2,3] # mutable - List, set and dictionary
# print(a)
# a.append(4)
# print(a)
## Perform task check mutable and immutable
# a = [1,2,3,4]
# a[1] =4
# print(a[-1])
# print(a)
# b = (1,2,3,4)
# b[1] = 4
## List ## list of the data 
## may not be the same data type
## is mutable object
## indexing forward (0,1,2...) and back ward (negative indexing== (-1,-2,-3))
## slicing
a = [1,2,3,4,5,6,7,8]
b = a[2:5]
print(b)
c = [a[0:2],a[5:7]]
print(c)