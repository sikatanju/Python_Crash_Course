age: int = 20

# print(age)
# print(type(age))

age: str = 'Python'

# print(age)
# print(type(age))

## Mutable & Immutable

## All the primitive types are immutable, which means they're value can't change

x = 1
# print(id(x)) # Id gets the address.

x = 2
# print(id(x))

x += 1
# print(id(x))

# let's say, when it's mutable type

x = [1, 2, 3]
print(id(x))

x.append(4);
x.append(4);
print(id(x))
