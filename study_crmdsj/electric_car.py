class Car():

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year)+" "+self.make+ " "+self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+ str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self,miles):
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("increment is a positive number!")
        
class Battery():
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size

    def describe_batery(self):
        print("This car has a " + str(self.battery_size) + " -kWh battery.")

class ElectricCar(Car):

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()
    
   

my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_batery()

