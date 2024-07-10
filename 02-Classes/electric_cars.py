from cars import Car

class Electric_Car(Car):
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