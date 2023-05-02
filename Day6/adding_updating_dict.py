##Adding and updating the dictionary values
student = {"name":"John", "age":23,"department":"CS"}
# if the key is not present in the dictionary then it adds the key as assign the value 4

student["id"] = 4
print(student)

#If the key if is already present in the dictionary then it updates the value in the id,
#In this case 5
student["id"] = 5 #id 4 is updated to 5
student["name"] = "Jane" # name in the dictionary Jon is updated to Jane

#we can also use update() method to update the existing dictionary
further_info = {"email":"jane@gmail.com","address":"kalanki"}

# This gives {"name":"John", "age":23,"department":"CS","email":"jane@gmail.com","address":"kalanki"}
student.update(further_info)
print(student)

## delete the items from dictionary

# use pop function in student dictionary
a = student.pop("address") # pop method takes key as a parameter , ehich removes the provided key value pair form the dictionary
#and returns the vaue

print(student)
print(a)

# If we try to pop out the key not present in the dictionary then it raises keyError
# student.pop("height")  # This raises error  because "height" key is not present in the dictionary

#But we can assign a default value

height = student.pop("height", 5.9)  # This gives 5.9 in the height variable
print(height)

## use popitem function in student dictionary
# this pops out the last item in the dictionary and returns 
# a (key, value) as tuple
data = student.popitem()
print(data)

## "Clear" removes the values inside the dictionary but "del" function removes the dictionary itself

''''restrictions in dictionary keys
1. Dictionary keys must be immutable
2. Tuples can be used as the dictionary key until it has no any mutable values
3. If the key is repeated, the last assigned key is considered
'''
a = {(1,2): 1} # Tgis is valid
#b = {[1,2]: 1} # This is invalid

b = {"id" : 5, "id" : 6} # the id gives the value 6 

print(b.get("id"))








