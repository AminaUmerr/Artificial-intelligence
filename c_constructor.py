# Class with constructor

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

e1 = Employee("Saira", 21)
print(e1.name)
print(e1.age)

# Example: Creating multiple instances
e2 = Employee("Amna", 20)
print(e2.name, e2.age)
