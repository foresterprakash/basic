a = [[1,2,3],[4,5]]
b = a 
print (b is a)
print(a == b)

from copy import deepcopy
b = deepcopy(a)
b[0][1] = 5
print(b)
print(a)

## note copy does the duplication of list but changes in copy will alter the original list too.
## But in the deepcopy, the mutable objects inside the list does remain same in original list. 

