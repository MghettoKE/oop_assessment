#static methods and attributes program
class Calculator:
    # Static attribute to keep track of how many times add() is called
    count = 0

    @staticmethod
    def add(a, b):
        # Increment the count each time add() is called
        Calculator.count += 1
        return a + b

# Using the static method without creating an instance of the class
result1 = Calculator.add(5, 3)
print(f"Result 1: {result1}, Add method called {Calculator.count} times")

result2 = Calculator.add(10, 20)
print(f"Result 2: {result2}, Add method called {Calculator.count} times")

result3 = Calculator.add(7, 8)
print(f"Result 3: {result3}, Add method called {Calculator.count} times")
