# List Basic II
# *** Using Loop in List:

names = ['john', 'pam', 'michael']

# for name in names:
    # print(name)

# for i in range(len(names)):
#     print(names[i])

# for temp in names:
#     print(F'{temp.title()}', end='')
#     print(', that\'s a great name.')


# print("You all have great names")

# *** Using ternary operator
# for i in range(1, 5):
#     print(f"{i} - ", end='') if i != 4 else print(i)

# # *** Creating list with range
# numbers = list(range(1, 5))
# for num in numbers:
#     print(f'{num} ,', end='')

# # * Creating only with even value, from 2 to 50
# evenNumber = list(range(2, 51, 2))
# for evennum in evenNumber:
#     print (f'{evennum}, ', end='') if evennum != 50 else print(f'{evennum}')

# # * Appending value in list:
# num = []
# for i in range(10, 21, 1):
#     num.append(i ** 2)
#     # print(num[len(num)-1])
#     print(num[-1])

# * Simple functions:
# num = [1, 2, 3, 4, 5]
# print(min(num))
# print(max(num))
# print(sum(num))