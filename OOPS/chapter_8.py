# Create a student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class Student:
    def __init__(self, Name, marks):
        self.Name = Name
        self.marks = marks

    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi",self.Name,", your average score is",sum/3)

s1 = Student("Kushagra", [98,89,90])                
s1.avg()

s1.Name = "Hehe"
s1.marks = [3,3,3]
s1.avg()