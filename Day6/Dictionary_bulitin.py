'''Builtin Functions in dictionary
1. all()
2. any()
3. len()
4. sorted()
5. str()
6. type()
'''
## all these functions in the dictionary takes the key as the references
s = {"name"  : "Jon", "email" : "Jon@gmail.com","address": "KTM"}
print(all(s))  # Gives True
print(any(s))  # Gives True
print(all([])) # Gives True

## 
a = {"" : 1}

print(all(a)) # this returns false because list a has a falsee key as an empty string

## any function also takes iterable (sequence) as a parameter. But it returns True
# if as leaset one of the elements is truthy

b = {0: "Hello", 1 : "World"}

print(any(b)) # This gives true 

# But if all the keys are falsy then it returns False

b = {"" : 1, 0:1}

print(any(b))

## Sorted functions sorts the dictionary using key name
s = {"name"  : "Jon", "email" : "Jon@gmail.com","address": "KTM"}
sorted(s)
print(sorted(s))
####
x = sorted(s)
print(x)
# If number and blank as a key name , then it returns the blank and number first

## str function Returns list
print(str(s))
## Type functions returns type of the data
print(type(s))
##len returns the length of the key or number of keys
print(len(s))









