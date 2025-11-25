# A class can store data and methods.
# A class is a collection of attributes and methods.
# Methods are the functions that belong to objects.

"""class Cars:
    def __init__(self):
        pass

    def hello(self,name): # Method initialization
        print("Moshi mosh... Orewa",name,"Kaizoku oni naru otokoda")

car1 = Cars()
car1.hello("Monkey D Luffy") # Method calling.

car2 = Cars()
car2.hello("Kaido")

car3 = Cars()
car3.hello("Lin Lin")

car4 = Cars()
car4.hello("Usopp") """

#___________________________________________________________________________________________________________________

# Static Method --->

# Methods that don't use the self parameter (Works at class level).
# It change the behaviour of normal method.

"""class Student :
    @staticmethod
    def hello():
        print("Hello")

s1 = Student()
s1.hello() """

#____________________________________________________________________________________________________________________

# Super Method -->

# super() method is used to access method of the parent class.

class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car started.")

    @staticmethod
    def stop():
        print("Car stopped")

class Tata(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
        super().start()

car1 = Tata("Benz", "Pani")        
print(car1.type)