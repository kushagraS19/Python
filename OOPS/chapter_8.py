# Create a student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

"""class Student:
    def __init__(self, Name, marks):
        self.Name = Name
        self.marks = marks

    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi",self.Name,", your average score is",sum/3)

s1 = Student("Kushagra", [97,98,99])
s1.avg()

s1.Name = "Hehe"
s1.marks = [3,3,3]
s1.avg()"""

#____________________________________________________________________________________________________

"""class Account :

    def __init__(self,acc_no):
        self.bal = 0
        self.acc = acc_no

    def Credit(self,money):
        self.bal += money
        print(money,"credited to your account.")

    def Debit(self, mon):
        self.bal -= mon
        print(mon,"debited to your account.")

    def printBal(self):
        print("Account no. :",self.acc,"\nCurrent balance : ",self.bal)       

acc1 = Account(12345)
acc1.Credit(7000)
acc1.Debit(5000)
acc1.printBal() """

#___________________________________________________________________________________________________________

# Define a circle class. Calculate area and perimeter.

"""class Circle:
    def __init__(self , r):
        self.r = r

    def area(self):
        self.area = 3.14 * self.r * self.r
        print("The area of circle :",self.area)    

    def perimeter(self):
        self.peri = 2 * 3.14 * self.r
        print("The perimeter of the circle :",self.peri)

c1 = Circle(5)
c1.area()
c1.perimeter()"""

#_____________________________________________________________________________________________________________________

# Define an employee class with attribute role,department & salary.

"""class Employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("The department of Employee :",self.department)    
        print("The role of Employee :",self.role)
        print("The salary of Employee :",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age =age
        super().__init__("Engineer","IT","78,000")

    def showEng(self):
        print("Name :",self.name)
        print("Age :",self.age)    

e2 = Engineer("Kushagra",19)
e2.showEng()
e2.showDetails()"""

#_____________________________________________________________________________________________________________________

# Create a class called Order which stores item and its price. Use dunder function __gt__.

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price    
    

odr1 = Order("Chips",20)
odr2 = Order("Samosa",40)

print(odr1 > odr2)