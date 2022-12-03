'''
#Inheritance - Single Level and Single Parent
class ParentClass():

    #Class Variables
    var1 = None
    var2 = None
    Parentvar1 = "parentVariable Value"

    #Constructors
    def __init__(self,var1,var2):
        self.var1=var1
        self.var2=var2
        print("parentclass constructors")

    #Methods
    def parentFunction(self):
        print("This is a message from ParentClass.parentFunction")
        total = self.var1 * self.var2
        print(total)

# inheritance---------
class ChildClass(ParentClass):
    
    #Class Variables
    ChildVar1 = None
    ChildVar2 = None

    #Constructors
    def __init__(self,a,b,c,d):
        super().__init__(c,d)
        self.ChildVar1 = a
        self.ChildVar2 = b
        print("child class variable")

    #Methods    
    def childFunction(self):
        print("This is a message from ChildClass.childFunction")
        total = self.ChildVar1 + self.ChildVar2
        print(total)


# Create an object of the Child Class
cObj = ChildClass(1, 2, 3, 4)

# CALL CHILDCLASS and PARENTCLASS methods from the child object
cObj.childFunction()
cObj.parentFunction()
'''
'''
#Inheritance - Single Level and Multiple Parents

class Parent_1():
    #Class variables
    P1Var1 = None
    
    # class Constructor
    def __init__(self,V1):
        print("This is another parent-level class parent1")       
        self.P1Var1 = V1

    # class methods    
    def Parent1Function(self):
        print("This is a message from the Parent_1.Parent1Function")
        print(self.P1Var1)


class Parent_2():
    #Class variables
    P2Var1 = None
    
    # class Constructor
    def __init__(self,V1):
        print("This is another parent-level class parent2")       
        self.P2Var1 = V1

    # class methods      
    def Parent2Function(self):
        print("This is a message from the Parent_2.Parent2Function")
        print(self.P2Var1)

# Class that inherits from 2 parents
class ChildMI(Parent_1, Parent_2):
     #Class variables
    CVar1 = None
    
    # class Constructor
    def __init__(self,V1):
        super().__init__(V1)
        super().__init__(V1)
        print("This is the ChildMI, this inherits Parent_1 and Parent_2")       
        self.CVar1 = V1

    # class methods      
    def ChildMIFunction(self):
        print("This is a message from the ChildMI.ChildMIFunction")
        print(self.CVar1)


# Create ChildMI Object
gcObj = ChildMI(34)

gcObj.ChildMIFunction()
gcObj.Parent1Function()
gcObj.Parent2Function()
'''
#""""""""""""""""""""""
#Inheritance - Multi Level

class GrandParent():
    #Class variables
    P1Var1 = None
    
    # class Constructor
    def __init__(self,V1):
        print("This is the GrandParent class")       
        self.P1Var1 = V1

    # class methods    
    def GrandParentFunction(self):
        print("This is a message from the GrandParent.GrandParentFunction")
        print(self.P1Var1)

# This inherits the GrandParent class
class Parent(GrandParent):
    #Class variables
    P2Var1 = None
    
    # class Constructor
    def __init__(self,V1):
        super().__init__(30)
        print("This is the Parent class")       
        self.P2Var1 = V1

    # class methods    
    def ParentFunction(self):
        print("This is a message from the Parent.ParentFunction")
        print(self.P2Var1)
        
# Class that inherits Parent Class
class Child(Parent):
     #Class variables
    CVar1 = None
    
    # class Constructor
    def __init__(self,V1):
        super().__init__(21)
        print("This is the ChildMI, this inherits Parent_1 and Parent_2")       
        self.CVar1 = V1

    # class methods    
    def ChildFunction(self):
        print("This is a message from the Child.ChildFunction")
        print(self.CVar1)

# Create ChildMI Object
gcObj = Child(20)

gcObj.GrandParentFunction()
gcObj.ParentFunction()
gcObj.ChildFunction()
