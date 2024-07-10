# class Student:

#     def __init__(self, name, age, cgpa):
#         # * """ Initialize name, age & cgpa of a student
#         self.name = name
#         self.age = age
#         self.cgpa = cgpa

#     def get_cgpa(self):
#         return self.cgpa
    
#     def get_name(self):
#         return self.name
    
#     def evaluate(self):
#         if self.cgpa >= 3.8:
#             return 'Darn Good'
                
#         if self.cgpa > 3.5:
#             return 'Good'

    


# my_student = Student('Sika', 23, 3.8)

# print(my_student.get_name())
# print(my_student.evaluate())


class Car:
    # * Setting a default value for an attribute
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odo_meter = 0

    def set_odo_meter_reading(self, new_reading):
        self.odo_meter = new_reading

    def get_odo_meter_reading(self):
        return self.odo_meter
    

urus = Car('Lamborghini', 'Urus', 2023)

print(urus.get_odo_meter_reading())

# urus.odo_meter= 11
urus.set_odo_meter_reading(113)
print(urus.get_odo_meter_reading())
