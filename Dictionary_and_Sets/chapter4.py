# Store the folowing word meanings in a py dictonary.

"""wordMeanings = {
    "table" : ("a piece of furniture","list of fact and figures"),
    "cat" : "a small animal",
}

print(wordMeanings)"""

#___________________________________________________________________________________________________________________________

# You are given a list of subjects for students. Assume one classroom is needed for 1 subject. How many classrooms are needed by all students.

"""subjects = {"python","java","C++","python","javaScript","java","python","java","C++","C"}

classes = len(subjects)
print("The number of classrooms needed are :",classes)"""

#___________________________________________________________________________________________________________________________

# WAP to enter marks of 3 subject from user and store them in a dictionary.

"""mar1 = float(input("Marks of subject 1 : "))
mar2 = float(input("Marks of subject 2 : "))
mar3 = float(input("Marks of subject 3 : "))

marks = {}
marks.update({"subject 1" : mar1})
marks.update({"subject 2" : mar2})
marks.update({"subject 3" : mar3})

print("Marks of student : ")
print(marks)"""

#__________________________________________________________________________________________________________________________

# Find a way to store 9 , 9.0 in a set --> 

set1 = set()

a = "9"
b = "9.0"

set1.add(a)
set1.add(b)
print(set1)

# Another way --> 

set2 = {
    ("float" , 9.0),
    ("int" , 9)
}

print(set2)