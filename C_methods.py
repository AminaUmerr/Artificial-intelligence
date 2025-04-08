# Class with a method

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name)

p1 = Employee("Amna", 20)
p1.myfunc()

# Extra Example: Another method to display age
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_age(self):
        print("My age is", self.age)

p1 = Employee("Amna", 20)
p1.display_age()
