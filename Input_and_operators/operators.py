# ARITHMETIC OPERATORS

"""num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)
print(num1 ** num2)""" # Means num1^num2 (num1 ki power num2)

#_________________________________________________________________________________________________________________________

# RELATIONAL / COMPARISON OPERATORS.
# == , != , > , < , >= , <= .
# Relational operators always gives only true and False. 

"""a = 50
b = 45

print(a == b) # False
print(a != b) # True
print(a > b) # True
print(a < b) # False
print(a <= b) # False
print(a >= b)""" # True

#__________________________________________________________________________________________________________________________

# ASSIGNMENT OPERATORS. 
# = , += , -= , *= , /= , %= , **= .

# b = 23

# b += 34 # b = b + 34 (Value of b becomes 57)
# b -= 5 # b = b - 5
# b *= 2 # b = b * 5
# b /= 2 # b = b/2
# b **= 2 # b = b ^ 2
# b %= 2 

# print(b)

#___________________________________________________________________________________________________________________________

# LOGICAL OPERATORS
# and , or , not
# not operator changes the output value to true to false and false to true.
# and operator gives false if one of the given conditions is false.
# or operator gives true if one of the given conditions is true.

a = 50
b = 30

print(not a==b) # a == b is false but because of not it gives true.
if(a == 50 and b == 30):
    print("hehe")

if(a == 50 or b == 5):
    print("hihi")