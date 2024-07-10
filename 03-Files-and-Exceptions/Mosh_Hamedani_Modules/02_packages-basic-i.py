# ** Packages in Python

# ** Packages is a container for one or more modules in Python (sub-directory)

# ** package is mapped to a sub-directory and modules are mapped to a file.

# ** In Python, we use `__init__.py` file in a directory to mark it as a package.

# * Here we defined a package with the name `ecommerce`:

# * To import that package's module

import ecommerce.sales as ecs

ecs.calc_shipping()

# * Or this way: 

from ecommerce.sales import calc_shipping

calc_shipping()


# * Or another way would be:

from ecommerce import sales

sales.generate_order_id()