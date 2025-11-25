# The data or any variable are stored in a class are known as the attributes of that class.
# Types of Attributes --> 
# Class attributes --> Same for every objects or methods.
# Instance or object attributes --> Different for all the objects.

class Student:
    college = "Acropolis"
    name = "Anonymous" # Class attribute

    def __init__(self, name):
        self.name = name # obj attribute

s1 = Student("Kushagra Saini")
print(s1.name)   # If the class and obj attribute is same, the priority is given to the obj attribute.