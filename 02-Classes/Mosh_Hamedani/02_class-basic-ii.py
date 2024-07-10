# *** Class ...

# ** Class methods and Instance methods

# class Car:
#     def __init__(self, name, year):
#         self.name = name
#         self.year= year

#     def drive(self, miles):
#         print(f"Driving {miles} miles :)")

#     # ** Static method refers to as factory method in python
#     # ** This works, but not sure it's okay
#     # @staticmethod
#     # def favourite_car():
#     #     return Car("Lambo Urus", 2024)
    
#     # * This is by Mosh Hamedani
#     @classmethod
#     def favourite_car(cls):
#         return cls('Lambo Urus', 2024)
    
#     # * Magic Methods: 
    
#     # * This str() method is kind of like toString method in Java:
#     def __str__(self) -> str:
#         return f'Name: {self.name}, Year: {self.year}'

# car = Car('Audi A8', 2024)
# print(car.name)

# car = Car.favourite_car()
# print(car.name)

# cr = Car.favourite_car()
# print(str(cr)) print(cr)


# ** Comparing objects:

# To compare two objects:

class Uni:

    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

    def __eq__(self, other_obj):
        return self.name == other_obj.name and self.rank == other_obj.rank
    
    def __gt__(self, other_obj):
        return self.rank < other_obj.rank

nubt = Uni('NUBTK', 1000)
nubtk = Uni('NUBTK', 1001)

# In order to use == on object, we need to define __eq__ method in the class to correctly compare two objects
# print(nubtk == nubt)

# print(nubt > nubtk)
# print(nubt < nubtk) # ** Note that we didn't define `__lt__()` method, Python figures it out automatically.

# ** We can also define `__add__()` method for adding two objects (perhaps useful for objects with numerical value)