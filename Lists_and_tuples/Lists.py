# List is a built-in data type that stores a set of values.
# It is almost like an array.
# It can store elements of different types together. (ex- float, int, string etc.)
# Lists are mutable.
# Lists have no limit on indices.

"""marks = [94.4, 67.7, 89.7, 23.9, 90.8]

print(marks)
print(type(marks))
print(marks[2])
print(len(marks)) """

"""student = ["kushagra", 90 , "Indore"]
student[0] = "Kush"
print(student)"""

#_______________________________________________________________________________________________________________________________

#  List Slicing

# Same rules and methods as Strings.

"""marks = [1,2,3,4,5,6,7,8,9]

print(marks[2:6]) # Does not include the value on 6th index.
print(marks[0:]) # Means 0th index to the last index or 0th index to len(marks).
print(marks[:5]) # Means from 0th index to 4th index."""

#____________________________________________________________________________________________________________________________

# List Methods

list = [4,8,9,2,6]

list.append(5) # Adds a value at last of the list.
print("After append :",list)

list.sort() # Sorts in ascending order.
print("After sorting :",list)

list.sort(reverse=True) # Sorts in descending order.
print("Descending order :",list)

list.reverse() # Reverse the list.
print("After reversing :",list)

list.insert(3, 89) # Adds a value at a specific index.
print("After inserting :",list)

list.append(5)
list.remove(5) # Removes only first occurence of element.
print("After remove :",list)

list.pop(4) # Remove an element of a specific index.
print("After pop :",list)