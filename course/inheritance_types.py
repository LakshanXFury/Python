""" Types of Inheritance """


# Single Inheritance
class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):  # Employee inherits from Person
    def __init__(self, name, salary):
        super().__init__(name)  # Calls the constructor of the parent class (Person.__init__) to initialize name.
        self.salary = salary


# Multiple Inheritance
class Job:
    def __init__(self, salary):
        self.salary = salary


class EmployeePersonJob(Employee, Job):
    def __init__(self, name, salary):
        Employee.__init__(self, name, salary)  # Initialize Employee
        Job.__init__(self, salary)  # Initialize Job


# Multilevel Inheritance
class Manager(EmployeePersonJob):
    def __init__(self, name, salary, department):
        EmployeePersonJob.__init__(self, name, salary)  # Explicitly initialize EmployeePersonJob
        self.department = department


# Hierarchical Inheritance
class AssistantManager(EmployeePersonJob):
    def __init__(self, name, salary, team_size):
        EmployeePersonJob.__init__(self, name, salary)  # Explicitly initialize EmployeePersonJob
        self.team_size = team_size


# Hybrid Inheritance  (Multiple + Multilevel)
class SeniorManager(Manager, AssistantManager):
    def __init__(self, name, salary, department, team_size):
        Manager.__init__(self, name, salary, department)
        AssistantManager.__init__(self, name, salary, team_size)


# Creating objects to show inheritance

# Single Inheritance
emp = Employee("Lakshan", "30k")
print(emp.name, emp.salary)

# Multiple Inheritance
emp2 = EmployeePersonJob("Night", "50k")
print(emp2.name, emp2.salary)

# Multilevel Inheritance
emp3 = Manager("Fury", "20k", "IT")
print(emp3.name, emp3.salary, emp3.department)

# Hierarichal Inheritance
emp4 = AssistantManager("John", "70k", 2)
print(emp4.name, emp4.salary, emp4.team_size)

# Hybrid Inheritance
emp5 = SeniorManager("Wick", "100k", "IT", 6000)
print(emp5.name, emp5.salary, emp5.department, emp5.team_size)