# create a dictionary
a = dict()
a.fromkeys([1,2,3],1)

# Dictionary method
student = {"name":"Jane","age":45, "dept":"cs"}
#student.clear() - This clears the dictionary

s = student.copy() # This is shallow copy 
print(s.fromkeys([1,2,3], "Hello world")) # this returns a dictionary {1:"Hello word", 2: "Hello world", 3: "Hello world"}

# if second parameter i.e. value not provided then None is considered
# {1:None, 2:None, 3:None}

##Items and Keys method in dictionary

print(student.items())  # it returns list-like object of tuples containing (key,value) pair
print(student.keys())   # it returns list-like object of tuples containing (keys: id or name)
print(student.values()) # it returns list like object of tuples containing (values : "Jane",45 etc) 

## default value set 
student.setdefault("name","Jon") # name key is already present in the dictionary so default value will not be considered
student.setdefault("id",1) # id key is not present in the dictionary. SO it is added in the dictionary.
##
print(student)

##Tasks





