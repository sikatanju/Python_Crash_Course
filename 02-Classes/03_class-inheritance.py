##
# *** Inheritance in Python:

class Car:
    def __init__ (self, brand_name, model, year):
        self.brand_name = brand_name
        self.model = model
        self.year = year
        self.meter = 0

    def get_full_name (self):
        return f'Name: {self.brand_name} {self.model} {self.year}'.title()
    
    def read_meter(self):
        return self.meter
    
    def set_meter(self, mileage):
        if mileage >= self.meter:
            self.meter = mileage
        else:
            print('You can\'t roll back an odometer')

    def fill_fuel_tank(self):
        print('Gas Tank is full')

class Tesla(Car):
    def __init__(self, brand_name, model, year):
        super().__init__(brand_name, model, year)

        # * Defining attributes and methods for the child class (Tesla)
        self.battery_size = '99kwh'

    def get_battery_capacity(self):
        return self.battery_size
    
    # * Overriding a method
    def fill_fuel_tank(self):
        print("Electric car doesn't any fuel tank")
    
tesla = Tesla('Tesla', 'S', 2024)

# print(tesla.brand_name)
# print(tesla.get_full_name())
# print(tesla.get_battery_capacity())
tesla.fill_fuel_tank()