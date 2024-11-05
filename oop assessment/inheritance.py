# Base class Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

# Subclass Dog inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the base class constructor to initialize the name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

# Creating an instance of Dog
dog1 = Dog("Buddy", "Golden Retriever")

# Using methods from the base class Animal
dog1.eat()
dog1.sleep()

# Using method from the Dog class
dog1.bark()
