# Type coversion is done automatically on the py compiler.

a = 3
b = 3.5

sum = a + b
print(type(sum))

#_______________________________________________________________________________________________________________________________

# Type casting is done manually by the programmer.

c = "4"
d = 4

e = int(c) # This convert the str value in c into a integer value.

print(type(e))
print(d + e)
