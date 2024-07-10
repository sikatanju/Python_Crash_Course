### Functions: 

# * Definign a simple function : 

# def hello():
#     print("Hello World!")

# hello()

# def hello_to_me(name):
#     print(f"Hello, {name.title()}")

# hello_to_me('sika')


# ** Passing Arguments:
# * There are several ways to do this: 

# * #1: Positional Arguments: in this case in which order we pass arguments matters to the parameter

# def printName(name, age):
#     print(f'Hello my name is {name}, & I\'m {age} years old')

# printName() # Throws error
# printName('Sika', 23)
# printName(23, 'Sika')

# * #2: Keyword Arguments: Order doesn't matter at all

# def printSkills(name, skills, age):
#     print(f'My name is {name.title()}, {age} years old & and I know these : {skills}')

# printSkills(skills=['Java', 'Docker', 'Spring Boot', 'Python', 'Django'], name='sika', age=23)

# * #3: Default Values: If no value is passed down from arguments, we use a default value instead

# def say_my_name(name='Heisenberg', speciality='Crystal'):
#     print(f'My name is {name.title()}, & I can cook the best {speciality} in town')

# say_my_name(name='Sika', speciality='Paratha')
# say_my_name(name='Sika', 'Paratha') # Throws exception
# say_my_name('Sika', 'Paratha') 
# say_my_name(speciality='Paratha')


# * A function doesn't necessarily need to print value, it could also return values:

# def get_full_name(first_name, last_name):
#     return first_name.title() + ' ' + last_name.title()

# print(get_full_name('sika', 't'))

# def sum(num1, num2):
#     return num1+num2

# print(sum(1, 2))

# * Returning a dictionary:

# def full_name(first_name, last_name, age=None):
#     fullName = { 'first_name': first_name,
#             'last_name' : last_name}
#     if age != None:
#         fullName['age'] = age

#     return fullName


# print(full_name('Sika', 'Tanjim', 23))

