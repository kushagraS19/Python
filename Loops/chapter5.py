# Print numbers from 1 to 100 using for and range-->

"""for i in range(1,101):
    print(i)"""

# Print nums from 100 to 1 -->

"""for i in range(100,0,-1):
    print(i)"""

# Print table of n --> 

"""n = int(input("Enter a number : "))

for i in range(1,11):
    print(i*n)"""

#__________________________________________________________________________________________________________________________

# WAP to find the sum of first n numbers (using while).

"""x = int(input("Enter a number : "))
sum = 0

while x > 0:
    sum += x
    x -= 1

print(sum)"""

#__________________________________________________________________________________________________________________________

# WAP to find the factorial of n.

x = int(input("Enter a number : "))
fact = 1

for i in range(1,x+1):
    fact *= i

print(fact)    