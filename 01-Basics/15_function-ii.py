#### * Function Basic II:

# * Any changes made to a list in a function is permanent: 

# def print_design(unprinted, printed):
#     while len(unprinted) > 0:
#         temp = unprinted.pop()
#         print(f'Printing : {temp}')
#         printed.append(temp)

# def show_printed(printed):
#     print("\n\nAll the printed list : ")
#     for temp in printed:
#         print(temp)


# unprinted_list = ['Oppenheimer', 'Kong vs Godzilla', 'Hunter X Hunter']
# printed = []


# print_design(unprinted=unprinted_list, printed=printed)
# show_printed(printed)
# print(unprinted_list)
# print(printed)


# *** To prevent a function from modifying the original list, we could pass a copy of our list:
# * That way, only the copy will be modified, which we don't care about:


# def print_design(unprinted, printed):
#     while len(unprinted) > 0:
#         temp = unprinted.pop()
#         print(f'Printing : {temp}')
#         printed.append(temp)

# def show_printed(printed):
#     print("\n\nAll the printed list : ")
#     for temp in printed:
#         print(temp)

# unprinted_list = ['Oppenheimer', 'Kong vs Godzilla', 'Hunter X Hunter']
# printed = []

# # * To pass a copy of a list, we could use slice notation `[:]`: 
# print_design(unprinted_list[:], printed)
# show_printed(printed)
# print(f'Unprinted List : {unprinted_list}')
# print(f'Printed List : {printed}')



# *** Passing an arbitrary number of arguments: 
# * In case you're not sure, how many arguments you might need to pass:

# * Under the hood, it creates a tuple called toppings & store all the arguments we provide.
# def make_pizza(*toppings):
#     # print(toppings)
#     print("All these topping will be in your pizza : ")
#     for topping in toppings:
#         print(topping)


# # make_pizza('Chicken')
# make_pizza('Chicken', 'Beef', 'Watermelon', 'Banana')


## ** Check out these three examples : 

# * #1:
# def make_pizza( not_toppings, *toppings):
#     print('Ignore it ' , not_toppings)
#     print("All these topping will be in your pizza : ")
#     for topping in toppings:
#         print(topping)

# make_pizza(1, 'Chicken', 'Beef', 'Watermelon', 'Banana')

# * #2:
# def make_pizza(*toppings, not_toppings):
#     # print(toppings)
#     print("All these topping will be in your pizza : ")
#     for topping in toppings:
#         print(topping)

# make_pizza('Chicken', 'Beef', 'Watermelon', 'Banana', not_toppings=1)

# * #3:
# def make_pizza(not_toppings , *toppings, not_toppings_2):
#     print(not_toppings)
#     print("All these topping will be in your pizza : ")
#     for topping in toppings:
#         print(topping)

# make_pizza(1, 'Chicken', 'Beef', 'Watermelon', 'Banana',2) # Throws exception
# make_pizza(1, 'Chicken', 'Beef', 'Watermelon', 'Banana', not_toppings_2='Not Toppings 2') # Works just fine





