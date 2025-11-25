# Private (like) Attributes & Methods.
# Private methods and attributes are meant to be used only within the class and are not accessible from outside the class.

class Account:
    def __init__(self,acc,accPass):
        self.acc = acc
        self.__accPass = accPass # use double underScore before a variable or method to make it private.

    def ResetPass(self):
        print(self.__accPass)    

acc1 = Account("12345" , "abcde")        
print(acc1.acc)

acc1.ResetPass()

class person:
    __name = "anonymous"

    def __hello(self):
        print("Hello")

    def Welcome (self):
        self.__hello()

p1 = person()
p1.Welcome()