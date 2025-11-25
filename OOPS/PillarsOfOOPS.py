# Abstraction -->

# Hiding the implementation details of a class and only showing the essential features to the user.
# It is hiding the unnecessary details and showing only the essential ones to the user.

"""class Car:
    def __init__(self):
        self.acc = False
        self.brake = False
        self.clutch = False

    def Start(self):
        self.clutch = True # These two are unnecessary details that did not show on the output to the user.
        self.acc = True
        print("Car started") # This one is essential to it get to the user.

car1 = Car()
car1.Start()  """      

#_____________________________________________________________________________________________________________________

# Encapsulation -->

# Wrapping data and functions into a single unit (object).

#_____________________________________________________________________________________________________________________

# Inheritance --> 

# When one class derives the properties & methods of another class.
# The class derived is called derived or child class & the other one is called parent or base class.

"""class Car:
    @staticmethod
    def start():
        print("Car started.")

    @staticmethod
    def stop():
        print("Car stopped")

class Tata(Car):
    def __init__(self,name):
        self.name = name

car1 = Tata("Mercedes")
car2 = Tata("Nano")        

print(car1.name)
print(car1.start())"""

# Types of Inheritance --> 

# Single inheritance --> Single class is derived from a single base class.

# Multi-level inheritance --> A class is derived from a single base class and become the base class for another derived class. Ex - B class is derived from A and class C is derived from Class B.

"""class Car:
    @staticmethod
    def start():
        print("Car started.")

    @staticmethod
    def stop():
        print("Car stopped")

class Tata(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(Tata):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("Petrol")        
print(car1.start())"""

# Multiple inheritance --> One derived class, Many parent or base classes.

class A:
    var1 = "Welcome to class A"

class B:
    var2 = "Welcome to class B"

class C(A,B):
    var4 = "Welcome to class D"

d1 = C()
print(d1.var1)            
print(d1.var2)          
print(d1.var4)            