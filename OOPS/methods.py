# A class can store data and methods.
# A class is a collection of attributes and methods.
# Methods are the functions that belong to objects.

class Cars:
    def __init__(self):
        pass

    def hello(self,name): # Method initialization
        print("Hello I am",name)

car1 = Cars()
car1.hello("Mercedes Benz") # Method calling