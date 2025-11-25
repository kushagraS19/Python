# Used to delete object properties or object itself.

class Person:
    def __init__(self, name):
        self.name = name
        print(name)

s1 = Person("Kushagra")
del s1        
print(s1)