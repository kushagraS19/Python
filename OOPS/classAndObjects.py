# Class is a blueprint for creating objects.
# Objects are the instances of class.

# Creating a class -->

naam = input("Enter your name : ")
x = int(input("Enter your age : "))

class Student:
    name = naam
    age = x

# Creating an object -->

s1 = Student()
print(s1.name)
print(s1.age)