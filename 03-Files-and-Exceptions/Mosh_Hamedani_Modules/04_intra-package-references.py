# ** There are two ways to reference another package's module in one module

# ** One way to do is absolute path

# from ecommerce.products import get_product_name

# get_product_name()

# ** Another way is to use relative path:

# from .ecommerce.sales import generate_order_id

# generate_order_id()