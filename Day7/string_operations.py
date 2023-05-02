a = "Hello "
b = "World"

print(a+b)  # it concatenates two strings

print(a*3)  # * is used as a broadcast operator "Hello","Hello","Hello"

# membership operator
print("H" in a)
print("W" not in b)

# string elements can be accessed with indexing and slicing as in list and tuples 
# but item assignment in any particular index is not possible because string is an immutable data type