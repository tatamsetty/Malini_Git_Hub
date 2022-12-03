"""
class xParent():  # Create a Parent Class
    "This is a Parent Class"
    var1 = "Parent-Test"
    def func1(self):
        print("This is parent class")


# Child class that inherits the xParent
# and uses the names same as the ones from the parent class
class xChild(xParent):
    "This is the Child class"
    var1 = "Child-Test"
    def func1(self):
        print("This is child class")


objA = xChild()
objA.func1()    # This should print message from the child class
"""

class Parent1():
    "A parent class to demonstrate the SUPER"
    
    # Parent1 Class Variable
    X = 100
    
    # Parent1 Consructor
    def __init__(self):
        print("This is a message from ",Parent1.__name__)
    
    # Parent1 Method
    def func1(self):
        print("This is a message from Parent1.func1")


# ##########################
# Child Class with a method
# ##########################
class Child1(Parent1):
    "A child class to demonstrate the SUPER"
    
    # Child1 Class Variable
    X = 999
    
    # Child1 Consructor
    def __init__(self):
    
        # Call the parent Classes Constructor using the super()
        super().__init__()
        
        # Refer the variable X from Parent1 Class using super()
        print(super().X)

        # Refer the variable X from Child1 Class
        print(self.X)
        
    
    def func1(self):
        print("This is a message from Child1.func1")

        
    # This is a func2, calling the Parent1 classes method.
    def func2(self):
        super().func1()


# Create an objec to demonstrate SUPER()
print(1240)
supObject = Child1()
supObject.func1()
supObject.func2()