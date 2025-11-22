# WAP to ask the user to enter names of their 3 fav movies & store them in a list.

"""movie = []
movie.append(input("Enter 1st movie name : "))
movie.append(input("Enter 2nd movie name : "))
movie.append(input("Enter 3rd movie name : "))

print("Your list of Fav movies :",movie)"""

#_______________________________________________________________________________________________________________________________

# WAP to check if a list contains a palindrome of elements.

"""list1 = [1,2,3,2,1,6]
list2 = list1.copy()

list2.reverse()

if(list1 == list2):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.") """

#____________________________________________________________________________________________________________________________

# WAP to count the grade A in the following tuple -->

tup = ("C", "D", "A", "A", "B", "B" ,"A")

print(tup.count("A"))

# -->> Store the above values in a list & sort them from A to B.

list = []
list.append(tup[0])
list.append(tup[1])
list.append(tup[2])
list.append(tup[3])
list.append(tup[4])
list.append(tup[5])
list.append(tup[6])

list.sort()
print(list)