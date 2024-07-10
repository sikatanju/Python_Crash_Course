# *** Here we're going to learn to read and write to files with `with-statement`

""" Python Docs : 

f = open('workfile', 'w', encoding="utf-8")

The first argument is a string containing the filename. The second argument is another string containing a few characters 
describing the way in which the file will be used. mode can be 'r' when the file will only be read, 'w' for only writing 
(an existing file with the same name will be erased), and 'a' opens the file for appending; any data written to the file 
is automatically added to the end. 'r+' opens the file for both reading and writing. The mode argument is optional; 
'r' will be assumed if it’s omitted.

"""

# * Before that we could also do this: (classic way)

# temp_file = open('contents/temp.txt', 'w', encoding='utf-8')
# temp_file.write('Temp file :(')
# temp_file.close()


# *** Now using `with-statement`:

# with open ('contents/any.txt', 'r', encoding='utf-8') as any_file:
    # print(f'Contents of any_file : {any_file.read()}')
    
# with open ('contents/temp.txt', 'w', encoding='utf-8') as temp_file:
    # print("Temp File")

# with open ('contents/any.txt', 'r', encoding='utf-8') as any_file, open('contents/temp.txt', 'w') as temp_file:
#     # print(f'Contents of any_file : {any_file.read()}')
#     # str = any_file.read()
#     temp_file.write(any_file.read())