# Single line If / Ternary Operator

# In variable form

"""food = input("Food : ")
eat = "Yes" if food == "cake" else "No"
print(eat)"""

#___________________________________________________________________________________________________________

# In statement form

"""food = input("Food : ")

print("Sweet") if food == "cake" or food == "jalebi" else print("Not sweet")"""

#____________________________________________________________________________________________________________

# CLEVER IF

# if the condition is true then the statement or value at the right side of the ( ) is executed or stored.

salary = float(input("Salary : "))
tax = salary * (0.1,0.2) [salary >= 50000]
print(tax)