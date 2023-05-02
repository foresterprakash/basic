# disctionary creates the information in column 
student = {"Name":"Prakash","age": 23, "department":"forest"}
#print(type(student))

# now multiple disctionary

students = [{"Name":"Prakash","age": 23, "department":"forest"},{"Name":"shekhar","age":24,"department":"soil"}] # this is the list of dictionary
print(type(students))

# using dict() function is also possible for creating dictionary

ab = dict(name = "prakash", age = "24")
print(ab)

# Accessing dictionary values # 
# dictionary values can be accessed using big bracket or using get method
name = student.get("Prakash")
print(student.get("Name"))

print(students[1].get("Name"))


