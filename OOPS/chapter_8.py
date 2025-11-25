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

class Account :

    def __init__(self):
        self.bal = 0
        self.acc = 123456778

    def Credit(self,money):
        self.bal += money
        print(money,"credited to your account.")

    def Debit(self, mon):
        self.bal -= mon
        print(mon,"debited to your account.")

    def printBal(self):
        print("Account no. :",self.acc,"\nCurrent balance : ",self.bal)       

acc1 = Account()
acc1.Credit(7000)
acc1.Debit(5000)
acc1.printBal()