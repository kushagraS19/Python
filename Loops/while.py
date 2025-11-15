# Loops are used to repeat instructions.

"""n = 1
while n <= 50:
    print("hello", n)
    n += 1"""

# Print numbers from 1 to 10

"""i = 1
while i <= 10:
    print(i)
    i += 1"""

# print table of 2 

"""i = 1
while i <= 10:
    print("2 *",i,"=",i*2)
    i += 1"""

# Print numbers from 1 to 100 --> 

"""i = 1
while i <= 100:
    print(i)
    i += 1"""

# Print numbers from 100 to 1 --> 

"""i = 100
while i >= 1:
    print(i)
    i -= 1"""

# Print the elements of the following list using a loop --> 

"""n = [1,4,9,16,25,36,49,64,81,100]
i = 0

while i < len(n):
    print(n[i])
    i += 1"""

# Search for a number x in this tuple using loop --> 

n = (1,4,9,16,25,36,49,64,81,100)
i = 0
x = int(input("Choose a number to search in the tuple : "))

while i < len(n):
    if(n[i] == x):
        print("Number found at index :",i)
        break
    else :
        print("Finding ..")
    i += 1