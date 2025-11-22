import os

# Open, read & close File --> 

# We have to open the file before reading or writing.

"""
data = f.read()
print(data)
print(type(data))
f.close()"""

#___________________________________________________________________________________________________________

# Reading a file --->>>

# We use .read() operation


# --> data = f.read(5) # We can argument i.e., we can choose how many characters we need to access.

"""line1 = f.readline()
print(line1) # Read a single line at a time.

line2 = f.readline()
print(line2) """

#________________________________________________________________________________________________________

# Writing to a file -- > 

# We have two modes "w" and "a".
# "w" mode overwrites the old data in the file with the new one.
# "a" mode appends the data at the last of the file.

"""f = open("D:\Kushagra\Python\File_I_O\demo.txt","w")
f.write("I am writing new data to the file.")

f1 = open("D:\Kushagra\Python\File_I_O\demo.txt", "a")
f1.write(" New data added.")
f1.write("\nI am learning fast")"""

# If we use "w" and "a" mode to open a file that does not exist, then py automattically creates a new file.

"""f2 =  open("D:\Kushagra\Python\File_I_O\sample.txt","a")
f2.close"""

#_____________________________________________________________________________________________________________

# Deleting a file --->>>

# To delete a file we need to import "os" module. Which is done at the top of this file.

os.remove("D:\Kushagra\Python\File_I_O\demo.txt")