# The __init__ function or constructor --> 
# This invokes or called when an object is created.
# All classes have a function called _init_(), which is always executed when the object is being initiated.

class Student:
    # Default constructors
    def __init__():
        pass

    # Parameterized constructors
    def __init__(self, fullName):
        self.name = fullName
        print("Adding new student")
        

s1 = Student("Kushagra Saini")
print(s1.name)

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class. It is mandatory to give at least one parameter to the init function.

s2 = Student("hehe")
print(s2.name)