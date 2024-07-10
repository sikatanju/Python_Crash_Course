# *** Exceptions from Mosh Hamedani

# try:
#     age = int(input('Enter you age: '))
# except ValueError as ex:
#     print("You didn't enter a valid age :(", ex)
#     # print("Type of exception ", type(ex))
# else:
#     print(f'Your age is {age}')

# try:
#     age = int(input('Enter you age: '))
#     age / 0
# except (ValueError, ZeroDivisionError) as ex:
#         print("You didn't enter a valid age :( or Can't divide the number by zero")

# else:
#     print(f'Your age is {age}')


# ** Raising exceptions:

def divide_two_number(num1, num2):
    if num1 == 0:
        return 0
    elif num2 == 0:
        raise ZeroDivisionError("You can't divide a number by zero")
    else:
        return num1/num2
    
try:
    print(divide_two_number(1,0))
except ZeroDivisionError as error:
    print(error)