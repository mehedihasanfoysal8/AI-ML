class Car:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name_print(self):
        print("This is my name :", self.name)

#Inheritance in python.....

# Inheritance here. super function car er sob attribute and method 
# er access niye niche. 
# super function ke call korar jonno first a supper key word ta likht hoi.
# then __init__(attribute ghuli pass korte hoi)

class ElectricCar(Car):
    def __init__(self, name, age, battery_size):
        super().__init__(name, age)
        self.battery_size = battery_size

new_car = Car("Mehedi", 12)

print(new_car.name, new_car.age)
new_car.name_print()