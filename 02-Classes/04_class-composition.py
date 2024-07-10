###
# *** Compisition refers to the process of breaking large classes into smaller classes that work together

##
# *** Inheritance in Python:

# * Parent Class:
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

# * Child class with instances
class Tesla(Car):
    def __init__(self, brand_name, model, year):
        super().__init__(brand_name, model, year)

        # self.battery_size = '99kwh'
        # * Here `Battery` instance is used as attribute in the Tesla class
        self.battery = Battery('75kwh')

    def get_battery_capacity(self):
        return self.battery.get_battery_capacity()
    
    def upgrade_battery(self, new_battery_cap):
        self.battery.upgrade_battery(new_battery_capacity=new_battery_cap)

    # * Overriding a method
    def fill_fuel_tank(self):
        print("Electric car doesn't any fuel tank")

    def get_range(self):
        btr = self.battery.get_battery_capacity()
        cap = btr[0]
        cap += btr[1]
        cap = int(cap)
        return cap * 1.5

class Battery:
    def __init__(self, battery_capacity='50khw'):
        self.battery_capacity = battery_capacity

    def get_battery_capacity(self):
        return self.battery_capacity
    
    def upgrade_battery(self, new_battery_capacity):
        self.battery_capacity = new_battery_capacity
        print('New battery Capacity is set to : ', new_battery_capacity)
        # if new_battery_capacity < self.battery_capacity:    
        # else:
        #     print("New battery capacity can't be more than initial capacity set at the time of creation of the car")

    
tesla = Tesla('Tesla', 'S', 2024)

# print(tesla.brand_name)
# print(tesla.get_full_name())
# print(tesla.get_battery_capacity())
# tesla.fill_fuel_tank()
# print(tesla.get_battery_capacity())
# tesla.set_battery_cap('80khw')
# print(tesla.get_battery_capacity())
# print(tesla.get_range())
# tesla.upgrade_battery('99khw')
# print(tesla.get_range())
