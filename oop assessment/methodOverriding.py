# Base class Employee
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        print(f"{self.name}'s salary is: {self.base_salary} (Base Salary)")


# Subclass Manager that overrides calculate_salary
class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        total_salary = self.base_salary + self.bonus
        print(f"{self.name}'s total salary as a Manager is: {total_salary} (Base Salary + Bonus)")


# Creating instances
employee = Employee("Prisca", 50000)
manager = Manager("Muli", 70000, 15000)

# Calling calculate_salary on both instances
employee.calculate_salary()
manager.calculate_salary()
