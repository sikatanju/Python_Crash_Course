### Function Basic III


# *** To be able accept as many key-value pairs as provided: we could use `**`:

# def greetings_with_cgpa(**students):
#     for student in students:
#         print("Student Name: ", student.title(), ", CGPA: ", students[student])


# greetings_with_cgpa(sika=3.8,zayed= 3.9,momin= 3.2)

### *** Storing functoin in a module: 
# * We could a bunch of functions in a module which is basically a separate file, then import that in main program

# * To import a module, use `import` keyword:
# import function_module

# * One way to call that imported function from imported module
# function_module.greet_user('sika')

# * Or we could just import all the function at once, then call like normal function
# from function_module import *

# greet_user('Tanjim')
# print(sum(1, 2))

# * We could import specific fuction(s):

# from function_module import greet_user, sum

# greet_user('sika')
# print(sum(1, 4))

# * Lastly we could use `as` to give our function or module an alias

# import function_module as fck
# fck.greet_user('sika')

# from function_module import greet_user as gu, poww as expo
# print(expo(2, 3))
