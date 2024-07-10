# *** Storing single or multiple classes in a module.

### *** We could store single or multiple classes in a module to keep our code clean and short.

# * Then use those classes by importing as modules like shown below
# from car import Car
# my_car = Car('Lambo', 'Urus', 2024)
# # print(my_car.brand_name)

# * Import multiple classes from a module

# from car import Car, Electric_Car

# my_ev = Electric_Car('Tesla', 'Plaid', 2024)
# my_car = Car('Lambo', 'Urus', 2024)

# print(my_ev.get_range())
# print(my_car.get_full_name())

# *** Importing an entire module:

# import car

# my_ev = car.Electric_Car('Tesla', 'Plaid', 2024)
# my_car = car.Car('Lambo', 'Urus', 2024)

# print(my_ev.get_range())
# print(my_car.get_full_name())

# ** Importing all classes from a module (not recommended):

# from car import *

# my_ev = Electric_Car('Tesla', 'Plaid', 2024)
# my_car = Car('Lambo', 'Urus', 2024)

# print(my_ev.get_range())
# print(my_car.get_full_name())



# *** Importing a module into a module: (shown in `cars.py` & `electric_cars.py` file)

# from electric_cars import  Electric_Car

# my_ev = Electric_Car('Lambo', 'Urus EV', 2028)

# print(my_ev.get_range())


# *** Lastly we could give aliases to imported classes : 

# from electric_cars import  Electric_Car as EC

# my_ev = EC('Lambo', 'Urus EV', 2028)

# print(my_ev.get_range())


### *** Last but not least, we could use any Python's built-in module by simply importing that module like `random`

# from random import randint

# * Generates a random int inclusive to given parameters
# print(randint(1, 2))