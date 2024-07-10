course = "Python Programming"

# print(len(course))

# print(course[0])

# In python, we have a negative index

# print(course[-18]) # It just rotates back
# print(course[0:6])
# print(course[:6])
# print(course[0:])
# print(course[:])
# print(course[-18:-1])

# # Different address, since String is immutable
# print(id(course))
# print(id(course[0])) 


### Escape Sequence

msg = 'Pythong "Programming'
# print(msg)

msg = "Pythong \"Programming"
# print(msg)


#1: # -- comment
#2: \" -- escape for "
#3: \' -- escape for '
#4: \\ -- escape for \
#5: \n -- new line

firstName = 'sika'
lastName = 'tanjim'
# fullName = firstName + ' ' + lastName

fullName = f"{firstName} {lastName}"
print(fullName)
print(f"Hello, my name is {fullName.title()}")
# print(fullName.istitle())

### Strip method:

# msg = '    adding a lot of whitespaces before & after the string '
# print(msg)
# print(msg.rstrip()) # It removes the whitespaces from the end of the string
# print(msg.lstrip()) # from the beginning
# print(msg.strip()) # from both sides

### Removing prefix & suffix:

name = 'sika Tanjim'
print(name.removeprefix('sika'))
print(name.removesuffix('Tanjim'))
