# .endswith

str = "Going to college"
print(str.endswith("ege")) # Gives true if the string is ending with 'ege'.

# ___________________________________________________________________________________________________________________

# UpperCase & LowerCase -->

str1 = "kushagra Saini"
print(str1.capitalize()) # Capitalize First character in the string.

print(str1.upper()) # Capitalize every character in the string.

print(str1.lower()) # in lowerCase.

#____________________________________________________________________________________________________________________

# Replace --> 

print(str1.replace("a","z")) # replaces every a with z.
print(str1.replace("Saini","Sainiee"))

#____________________________________________________________________________________________________________________

# Find -->

print(str1.find("Saini")) # Return the 1st index of where it it found first.

# __________________________________________________________________________________________________________________

# Count-->

str2 = "I am kushagra Saini. I am 19 years old. I am learning python"

print(str2.count("a")) # Counts how many a are there.
print(str2.count("am"))