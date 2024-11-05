employees = []

def add_employee(employees, name,salary):
    return employees + [{"name" : name, "salary" : salary}]

def calculate_total_payroll(employees):
    return sum(employee["salary"] for employee in employees if employee["salary"] > 0)

# usage
employees = add_employee(employees,"Prisca", 1000)
employees = add_employee(employees,"Muli",2000)
total_payroll = calculate_total_payroll(employees)
print(f"Total Payroll: {total_payroll}")
print(f"Employees: {employees}")


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


emp3 = Employee("Bob", "40000")
print(f"{emp3.name} {emp3.salary}")


class Payroll:
    def __init__(self, employees):
        self.employees = employees

    def calculate_total_payroll(self):
        return sum(employee["salary"] for employee in self.employees if employee["salary"] > 0)

    def __repr__(self):
        return f"Payroll with {len(self.employees)} employees"


# Create a Payroll object and calculate the total payroll
payroll = Payroll(employees)
print(f"Total Payroll from Payroll Class: {payroll.calculate_total_payroll()}")
