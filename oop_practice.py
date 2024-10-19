## The self means that this class is the a base/parent class
class Employee():
    new_id = 1
    def __init__(self): # "__init__" is used to initialize objects of a class. It is also called a constructor.
        # "self" refers to the first parameter of an instance of the class that the method is being called on.
        self.id = Employee.new_id
        Employee.new_id += 1
    def say_id(self):
        print("My id is {}.".format(self.id))

## Admin class inherits from the Employee class.
# Write your code below
class Admin(Employee):
    def say_id(self):
        super().say_id() ## Adding super() will overide to provide access to the parent class. 
        #print("I am an Admin.") ## This line overides output "My id is 3"

## Manager class added for multiple inheritance.
class Manager(Admin):
    def say_id(self):
        print("I am in charge!")
        #super().say_id()

## The variable e1 is having an instance of Employee.
e1 = Employee()
e1.say_id()
e2 = Employee()
e2.say_id()
e3 = Admin()
e3.say_id()
e4 = Manager()
e4.say_id()

## OUTPUT
# My id is 1.
# My id is 2.
# My id is 3.