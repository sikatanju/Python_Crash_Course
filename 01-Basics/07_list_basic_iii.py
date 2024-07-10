# List Basic III

# * List Comprehesions

# * The work we were doing before, could be done in one line:
# squares = [value ** 2 for value in range(1, 11, 1)]
# print(squares)

# ** Slicing a list: (Of course, in all this examples, we could used negative indexing)
# players = ['lm10', 'cr7', 'm6', 'tk8', 'ic1']
# print(players[0:3]) # ['lm10', 'cr7', 'm6']
# print(players[:2]) # ['lm10', 'cr7']
# print(players[2:4]) # ['m6', 'tk8']
# print(players[2:]) # ['m6', 'tk8', 'ic1']

# # * Looping through a slice:
# num = list(range(11, 21))
# for nn in num[0:4]:
#     print(nn)

# ** Copying a list:
myfood = ['biriyani', 'porata', 'ice-cream', 'burgers']
notmyfood = myfood[:] 

# * if we were trying to copy without using slice, we would have exactly the same list with two references
# myfood.append('pizza')
# notmyfood.append('ghee')
# print(f'My food {myfood} & id {id(myfood)}')
# print(f'Not My food {notmyfood} & id {id(notmyfood)}')

# * check this : 
# notmyfood = myfood
# myfood.append('pizza')
# notmyfood.append('ghee')
# print(f'My food {myfood} & id {id(myfood)}')
# print(f'Not My food {notmyfood} & id {id(notmyfood)}')

# *** Tuples: Tuples are immutable list, meaning we can't change the list after it has been defined (although we could reassing them)
# * To create a tuple, use () instead of []
# * Use tuple when you want to store a set of values that should not changd through-out the life of a program.
# names = ('john', 'wick')
# print(names)

# name[0] = 'sika' # Throws an error
# names = ('sika', 'tanjim') # It's valid
# for name in names:
#     print(name)
