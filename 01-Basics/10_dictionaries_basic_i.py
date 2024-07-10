# * We'll learn how to work with dictionaries in Python
# *** Dictionaries in Python is simply key-value pairs

# * Creating & accessing a dictionary
student = {
    'name': 'Sika',
    'age' : 23,
    'cgpa' : 3.9
}


# print({student.get('name')) # If given key doesn't exists, it returns a default value : 'none'
# print(student['name']) # If given key doesn't exists, it throws an exception.
# for key in student:
#     print(f'{key.title()} : {student.get(key)}')

# * Adding a new value pair
student['address'] = 'Khulna (temp)'
# print(student.get('address'))

# ** Removing an existing key-value pair: 

# * 1: Using del
# del student['name']
# print(student['name'])

# * 2: Using pop method, it removes the key-value pair & returns the value:
# name = student.pop('name') 
# print(student.get('name')) # Throws an exception


# * Starting with an empty dictionaries:
# me = {}
# me['name'] = 'Tanjim'
# me['age'] = 23
# me['occupation'] = 'broke'
# print(me)


# * Modifying an existing value
# me['age'] = 23.5;
# print(me)

# student.update({'name':'Tanjiro'})
# print(student['name'])


# * Looping through a dictionary:
# * 1:
# for key in student:          # it's same as `for key in student.keys():`
#     print(f'{key}: {student.get(key)}')

# * 2:
# for key, value in student.items():
#     print(f'{key}: {value}')

# * 3: 
# for value in student.values():
#     print(value)

# * 4: To see the values without repetition, we could use a set:
# for value in set(student.values()):
    # print(value)

# *** To build a set in python: 
# set = {1, 2, 1, 3, 4, 5} # Here, second 1 will omit by itself
# print(set)