# Slicing is an operation that slice the string / cut the string or accessible part of a string.
# str[starting_index : ending_index] --> Ending index is not included. Suppose if end index is 4 the characters return will be limited to index.

str1 = "Kushagra"

print(str1[1:4])

# To get the last index of string -->  

str2 = "Saini"

print(str2[0 : len(str2)])

# Other methods --> 

print(str1[:4]) # This means 0:4
print(str1[0 :]) # This means 0 : last index

#_________________________________________________________________________________________________________________________________

# Negative index in slicing --> 
# When we go from right to left, the indices are -ve.
# When we go from left to right, the indices are +ve.
# "Kushagra" --> Form K to U .. +ve indices, from U to K .. -ve indices.
 
srt = "Kushagra"

print(srt[-5 : -1])