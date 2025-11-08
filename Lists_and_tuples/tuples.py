# Tuples are a built-in data types that let us create IMMUTABLE sequences of values.
# Unlike lists tuples are immutable.

tup = (2,5,7,9,0)
print(tup[2])

#______________________________________________________________________________________

# Slicing --> It is same as slicing in list or string.

print(tup[1:4])

#__________________________________________________________________________________

# Methods in Tuple
# Two important methods of tuple -->

tup1 = (2,1,4,7,1,2)

print(tup1.index(1)) # Returns index of first occurence.

print(tup1.count(1)) # Counts total occurence.
