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


class Electric_Car(Car):
    def __init__(self, brand_name, model, year):
        super().__init__(brand_name, model, year)
        self.battery_cap = 65
        # self.range = self.battery_cap*1.75


    def get_range(self):
        return self.battery_cap*1.75
    
    def upgrade_battery(self):
        self.battery_cap = 99
