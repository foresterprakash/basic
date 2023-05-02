##Accessing the dictionary values
student = {"name":"John", "age":23,"department":"CS"}

print(student.get("name"))  # This gives John
print(student.get("age"))   # This gives 23
print(student.get("id"))    # This raises keyError

#We can also use get() method in dictionary to access the value
print(student.get("name"))  # This also gives John

#But if the key is not present in then dictionary then it gives None
# print(student.get("id"))    #This gives None as id Key is not present in the dictionary

#we can give the default value to the get() method

# but if we give default value to the key already present in the dictionary,
#It ignores the default value
print(student.get("name","Jon"))



