class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary
class Manager(Employee):
    def calculate_salary(self):
        return self.base_salary + 20000  # bonus

class Developer(Employee):
    def calculate_salary(self):
        return self.base_salary + 10000  # bonus

class Intern(Employee):
    def calculate_salary(self):
        return self.base_salary  # no bonus

employees = [
    Manager("Rahul", 50000),
    Developer("Anjali", 40000),
    Intern("Arun", 20000)
]

for emp in employees:
    print(f"{emp.name}'s Salary: ₹{emp.calculate_salary()}")
