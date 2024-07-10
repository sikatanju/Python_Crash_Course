# Exceptions in Python:

# *** In Python, we handle Exceptions using `try-except`:

# try:
#     print(5/0)
# except:
#     print(f'Can\'t divide a num by zero')

# * Trying to implement exceptions on a simple calculator that only performs division

# print('This calculator only performs division')

# while True:    
#     first_number = input('Input first number (press "q" to exit) : ')
#     if first_number == 'q':
#         break

#     second_number = input('Input 2nd number (press "q" to exit) : ')
#     if second_number == 'q':
#         break
    
#     first_number = int(first_number)
#     second_number = int(second_number)
    
    # ** The only code that should go in the try block is the code that might cause an exception.
#     try:
#         division = first_number / second_number
#     except ZeroDivisionError:
#         print('Can\'t divide by zero')
#     else:
#         print(division)


# ** FileNotFoundError: Handling file not found error exception:

# from pathlib import Path

# path = Path('not-found.txt')

# try:
#     txt = path.read_text(encoding='utf-8')    
# except FileNotFoundError:
#     print("File Not found in the given path: ", path)
# else:
#     print(txt)


# ** Failing Silently: Even after catching an error, sometimes we might want to ignore that error

# * to do that, Python has `pass` statement

# from pathlib import Path

# path = Path('not-found.txt')

# try:
#     txt = path.read_text(encoding='utf-8')    
# except FileNotFoundError:
#     pass
# else:
#     print(txt)

# ** Trying an exercise: 

# while True:    
#     first_numbe, second_numbe = 0, 0
    
#     while True:
#         try:
#             first_number = input('Input first number (press "q" to exit) : ')
#             if first_number == 'q':
#                 break

#             first_numbe = int(first_number)

#         except ValueError:
#             print("Please enter a number")
#         else:
#             break
    
#     while True:
#         try:
#             second_number = input('Input 2nd number (press "q" to exit) : ')
#             if second_number == 'q':
#                 break
            
#             second_numbe = int(second_number)

#         except ValueError:
#             print("Please enter a number")
#         else:
#             break

#     try:
#         division = first_numbe / second_numbe
#     except ZeroDivisionError:
#         print('Can\'t divide by zero')
#     else:
#         print(f'\nDivision : {division}\n')