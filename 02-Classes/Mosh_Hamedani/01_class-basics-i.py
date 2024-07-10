# ** Class in Python

# ** Use Pascal notation for ClassName

# class Point:
#     def draw(self):
#         print("draw")


# obj = Point()
# obj.draw()
# print(type(obj))
# print(isinstance(obj, Point)) # * Returns true or false

# *** Class Attributes vs Instance Attributes


# class Car:
#     wheels = 4

#     def __init__(self, brand):
#         self.brand_name= brand

#     def print_car_name(self):
#         print(self.brand_name)

# bmw = Car('bmw')
# audi = Car(4)

# # bmw.print_car_name()
# # audi.print_car_name()

# # audi.wheels = 2
# # print(audi.wheels)
# # bmw.wheels = 3
# # print(bmw.wheels)

# Car.wheels = 5
# audi.wheels = 2
# print(audi.wheels)
# bmw.wheels = 3
# print(bmw.wheels)
# print(Car.wheels)