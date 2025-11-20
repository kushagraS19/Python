# WAP to calculate avg of 3 numbers.

"""def avg (a ,b,c):
    av = (a+b+c)/3
    print("The average of 3 numbers is :",av)

a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))
c = int(input("Enter number 3 : "))

avg(a,b,c)"""

#_____________________________________________________________________________________________________________________

# WAF to print the length of a list.

"""
list1 = [3,6,8,3,2,5,7]

def count (list):
    give = len(list)
    return give

print(count(list1))"""

#_________________________________________________________________________________________________________________________

# WAF to print the elements of a list in a single line.

"""nums = [1,2,3,4,5,6,7,8,9,10]

def listItems (nums):
    for i in nums:
        print(i, end=" ")

listItems(nums)  """      

#______________________________________________________________________________________________________________________

# WAF to find the factorial of n.

"""n = int(input("Enter a number : "))

def factorial (n):
    fact = 1
    for i in range(1,n+1):
        fact *= i

    return fact    
        
print("Factorial of",n,"is :",factorial(n))"""

#_________________________________________________________________________________________________________________________

# WAF to convert USD into INR --> 

"""usd = float(input("Enter amount in USD : "))

def convert (usd):
    con = usd * 88.527
    return con

print("The amount is INR :",convert(usd))"""

#_______________________________________________________________________________________________________________________

# WAF to find a number is even or odd --> 

"""x = int(input("Enter a number : "))

def check (x):
    if(x%2 == 0):
        return "Even"
    else:
        return "Odd"
    
print(check(x))   """ 

#___________________________________________________________________________________________________________________

# Recursion -->>>>

# Write a recursive function to calculate the sum of first n natural numbers --> 

"""def sum (n):
    if (n == 0):
        return 0
    return sum(n-1) + n

summ = int(input("Enter a number : "))
print(sum(summ))"""

#_____________________________________________________________________________________________________________

# Write a recursive function to print all elements in a list -->

def printL(list,idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    printL(list, idx+1)

hehe = ["hehe","haha","hihi","huahau","buahahaha"]    
printL(hehe)