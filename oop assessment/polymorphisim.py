# Base class Animal
class Animal:
    def make_sound(self):
        pass

# Subclass Cat
class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Subclass Dog
class Dog(Animal):
    def make_sound(self):
        print("Woof!")

# Function that accepts an object and calls make_sound
def animal_sound(animal):
    animal.make_sound()

# Creating instances of Cat and Dog
cat = Cat()
dog = Dog()

# Demonstrating polymorphism by passing instances to the same function
animal_sound(cat)
animal_sound(dog)
