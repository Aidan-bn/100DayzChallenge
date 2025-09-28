#The way to pass inherince
#class Super:
    #super attributes

#class Sub(Super):
    #sub attributes

class SuperClass:
    def function_1(self):
        print('Super function is here')

class SubClass(SuperClass):
    def __init__(self):
        self.name = ""
    def function_2(self):
        print('Subclass function', self.name)
        
one = SubClass()
print(one.function_1())

two = SuperClass()
print(two.function_1())

# Given the Employee class, create a Developer class that inherits from Employee. The Developer class
# has one method, update_codebase(), which prints "Employee has updated the codebase". Then,
# use the Developer instance, python_dev, to call print_company() and update_codebase().

class Employee:
    #something here
    def print_company(self):
        print('Yoof Galore')

class Developer(Employee):
    def __init__(self):
        self.python_dev = ''
        
    def update_codebase(self):
        print('Employee has updated the codebase')

dev = Developer()

print(dev.print_company(), ' ', dev.update_codebase())
