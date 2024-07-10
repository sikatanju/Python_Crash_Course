### Trying to get input.

# a, b = input(), input()

# print(a, b)

# * By default all the input is string

# a = input()

# print(type(a)) # Return str

# * To take an input as an int: 

# a = input()
# a = int(a)

# * Simple just do it in one line: 

# a = int(input())
# print(type(a))

# * Or any other type in that matter: 

# a = float(input())
# print(a, type(a))

# * In case of bool, Python evaluate any non-empty string as True, even if you type 'False'
# a = input()
# print(bool(a))

# * Instead take string input, and compare that with 'True' or 'False'
a = input()

if a.lower() == 'true':
    print("Input is True");
elif a.lower() == 'false':
    print("Input is false");

