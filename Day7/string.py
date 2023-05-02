# empty strings can be created using str function
s = str()  # empty string
print(s)
# empty string can also be created with empty quotes (single or double)
s = ""
print(s)

## Non empty string

s = "I'm broadway" # This is a valid string
#s = 'I'm broadway' # This is invalid

# Escape sequence is used to supress the actual meaning of the character
# Some escape sequence are '\'\n'\\'\b'\n'\t',\r

a = 'I\'m broadway' # this is valid because of escape sequence
print(a)
##
a = "Hello\nWorld" # \n breaks the line in the console
print(a)

a = "Hello broadway\rWorld" # CARRIAGE RETURN
print(a)

a = "Helloooooooo\rBroadway"
print(a)

#\r takes the cursor  in the very beginning. Here the result will be "World broadway"

#triple quoted string are also possible in python
a = '''I'm getting late'''
print(a)

### Accessing string in a string

