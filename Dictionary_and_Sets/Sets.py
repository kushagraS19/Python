# Sets in python is something similar like sets in maths.
# Set is the collection of unorderd items.
# Each element in the set must be unique and immutable (We cannot store lists, dictionary or any other mutable values in a set.)
# The set itself is mutable but the values in it must be immutable.

"""nums = {1,2,3,4, 6, "Kush", "Kush"} # Item is stored only once in a set, so it resolves in {"kush",1,2,3,4}.

print(nums)
print(type(nums))"""

# To create a null set -->

"""kush = set()"""

#________________________________________________________________________________________________________________________

# Methods of Sets -->

# .add --> adds an element

sets = set()
print(sets)
print()

sets.add(45)
sets.add(67)
sets.add("kush")
sets.add("saini")

print(sets)

# .remove --> removes the element

print("After removing")
sets.remove("kush")
print(sets)

# .clear --> clear all values in the set.
 
"""print("After clearing")
sets.clear()
print(sets)"""

# .pop --> Removes a random value.

sets.pop()
print(sets)

#________________________________________________________________________________________________________________________

# Union and intersection of sets --> 

# Union --> Combines both set values and gives a new set.

set1 = {1,6,8,"Kush"}
set2 = {4,8,1,"Saini"}

newSet = set1.union(set2)
print("Union --> ")
print(newSet)

# Intersection --> Combines only the common values in both sets and gives a new set of common values.

set3 = {1,4,7,9}
set4 = {4,7,8,3}

nayaSet = set3.intersection(set4)
print("Intersection --> ")
print(nayaSet)