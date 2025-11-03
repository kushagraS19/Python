# color = input("What is the color of the signal light ? : ")

# if(color == "red"):
#     print("STOP")
# elif(color == "yellow"):
#     print("WAIT")
# elif(color == "green"):
#     print("You can Go now")
# else:
#     print("Your light is broken")        

#______________________________________________________________________________________________________________________-

# if-elif-else with logical operators.

print("Fill your marks below -->")
print("")

m1 = int(input("Discrete : "))
m2 = int(input("OOPM : "))
m3 = int(input("EEES : "))
m4 = int(input("Data structure : "))
m5 = int(input("DCS : "))

result = (m1 + m2 + m3 + m4 + m5) / 5

print("")
print("Percentage = ",result)
if(result >= 90):
    print("Grade A")
elif(result >= 80 and result < 90):
    print("Grade B")
elif(result >= 70 and result < 80):
    print("Grade C")
else:
    print("Grade D")