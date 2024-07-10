### While loops in Python

# a = 10

# while a >= 0:
#     print(a)
#     a -= 1;


# a = 1
# while a != -1:
#     print("Enter a number to echo or \nEnter -1 to exit the program: ", end='')
#     a = int(input())
#     print(f'You inputted : {a}')
    

# * Using a flag to stop the while loop : 

# active = True

# while active: 
#     active = input("Enter your name: , or Enter quit to exit the program: ")
#     if active.lower() == 'quit':
#         active = False


# * Or using break, and continue in python ...

# * Using while loops in list, dictionaries: 

# users = ['sika', 'jack', 'mikaila']

# confirmed_users = []

# # while len(users) > 0:
# while users:
#     temp = users.pop()
#     print(f'Verifying users: {temp}')
#     confirmed_users.append(temp)

# print("All the verified users : ")
# for user in confirmed_users:
#     print(user)

# * Removing all instances of a specific item in a list: 

# pets = ['dog', 'cat', 'cow', 'goat','cat', 'shephard', 'brown hound', 'cat', 'cat']

# while 'cat' in pets:
#     pets.remove('cat')

# while pets:
#     print(pets.pop())
     
# * Doing simple surveys using dictionary

# wish = {}
# poll_active = True

# while poll_active:
#     print("Please sate your name : ", end='')
#     name = input()
#     print("Which city would you like to visit in your lifetime : ", end='')
#     wishes = input()
#     wish[name] = wishes
#     name = input("Would you like to get more responses (yes/no): ")
#     if name.lower() == 'no':
#         break;


# for response in wish:
#     print(f'{response.title()} wants to visit : {wish[response].title()}')
    