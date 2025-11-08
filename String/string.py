# Str is a data type that stores a sequence of characters.

# To give a new line or use tab we use escaping sequence characters.

"""str1 = "This is a string. \nWe are creating it in python."
print(str1)
print("")

str2 = "This is a string. \tWe are creating it in python."
print(str2)"""

#_______________________________________________________________________________________________________________

# concatenation is adding two strings

str1 = "Hello, I am "
str2 = "Kushagra Saini"

print(str1 + str2)  

#_______________________________________________________________________________________________________________

# To get the length of a string -->

str3 = "Kushagra"
print(len(str3)) # It shows the number of characters in the string. It also include the space as characters given between words.

str4 = "Kushgara Saini" # Number of character are 13 but beacuse of one space it gives 14.
print(len(str4))

#________________________________________________________________________________________________________________

# We can get a character by searching at the index of the string.

str5 = "Kushagra"

print(str5[4]) # On 4th index the character is a. Because the index starts from zero.
