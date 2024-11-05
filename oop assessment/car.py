#class and object creation
#creating class and attributes

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

#creating a method
    def display_info(self):
        print(f"This is a {self.make} {self.model} {self.year} car.")

#creating instance of a class
car1 = Car("Audi", "BMW", "2021")

#calling the method
car1.display_info()