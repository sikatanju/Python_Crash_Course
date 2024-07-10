# import sys


# ** Modules

# *** Modules are consists of highly related code you could say, it could be a bunch of functions or classes.

# * To import a single function from a module :

from module_i import calc_shipping

calc_shipping()

# * To import all the functions from a module:

from module_i import *


# ** There is another way to import a module

import module_i as moo # * Here `as` is used to give module_i an allias

# * Now this allias `moo` acts as an obj through which we can access the functions of that module

moo.calc_shipping()




# paths = ['']

# * These are the paths python searches automatically for importing a module
paths = sys.path

# for pat in paths:
#     print(pat)
