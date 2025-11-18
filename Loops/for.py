# For loops are used for sequential traversal. For traversing list, string, tuples etc.

"""nums = [1,3,5]

for val in nums:
    print(val)"""


"""tup = (1,7,3,9,66,55)

for val in tup:
    print(val) """

#__________________________________________________________________________________________________________

# For with else --> 

"""name = "Kushagra"

for char in name:
    if(char == 'y'):
        print("g found")
        break
    else :
        print("Finding..")
else :
    print("Loop END")"""

#__________________________________________________________________________________________________________

# Print the elements of the following list using a for loop --> 

"""nums = [1,4,9,16,25,36,49,64,81,100]

for val in nums:
    print(val)"""

#__________________________________________________________________________________________________________

# Search a number in a tuple using loop --->

"""x = int(input("Enter a number to search in the tuple : "))
nums = (1,4,9,16,25,36,49,64,81,100)
idx = 0

for val in nums:
    if(val == x):
        print("Found at index",idx)
        break
    else:
        print("Finding..")    
    idx += 1    
else:
    print("The number is not here.")"""

#_____________________________________________________________________________________________________________

###########  Range --> 

# Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
# range(start, stop, step) step means kitna increase karna.

"""for el in range(8):
    print(el)
print()

for i in range(1,5):
    print(i)
print()

for j in range(1,9,2):
    print(j)"""

#_______________________________________________________________________________________________________________________

# PASS --> 

# This skips the loop.
# If we do not want to write a statement in the loop and want to leave it blank.
# It is used as placeholder for the future code.

for i in range(65):
    pass # Skips the loop.

print("Some useful work")