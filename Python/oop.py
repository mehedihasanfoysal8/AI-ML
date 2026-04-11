class Car:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name_print(self):
        print("This is my name :", self.name)


new_car = Car("Mehedi", 12)

print(new_car.name, new_car.age)
new_car.name_print()