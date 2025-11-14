# Dictionaries are used to store data values in key:value pairs.
# They are unordered, mutable and don't allow duplicate keys.
# We can also store lists and tuples in dictionary.

"""info = {
  "name" : "Hehe",
  "age" : 19,
  "phoneNumber" : 9202216169,
  "is_adult" : True,
  "subjects" : ["C++" , "Java" , "Pyhton"],
  "Marks" : 87.6,
  12 : 45,
  34.66 : 67,
  () : 56
}

info["surname"] = "Saini" # We can add keys and values in a dictionary.
info["name"] = "Kushagra" # We can also overwrite exixting values.

print("My name is :",info["name"],info["surname"])
print("I got",info["Marks"],"marks in",info["subjects"])"""

#_____________________________________________________________________________________________________

# Nested Dictionaries -->

"""student = {
  "name" : "Kushagra",
  "marks" : {
    "maths" : 60,
    "Physics" : 64,
    "Chemistry" : 74, 
  }
}

print(student["marks"]["maths"])"""

#__________________________________________________________________________________________________

# Methods on Dictionaries -->

student = {
  "name" : "Hehe",
  "age" : 19,
  "phoneNumber" : 9202216169,
  "is_adult" : True,
  "subjects" : ["C++" , "Java" , "Pyhton"],
  "Marks" : 87.6,
}

# .keys -->

"""
print(student.keys()) # Returns all the keys in a dictionary. Only the outer keys will return not the nested ones. We can also typecast it into form of lists and tuples.

print(list(student.keys()))
print(tuple(student.keys()))
print()
print(len(student)) # To get the number of key value pairs."""

# .value -->
# Returns all the values stored in a dictionary. All operations are same as the .keys function.

"""print(student.values())"""

# .values--> 
# Returns all the key:value pairs as a tuple.

"""print(student.items())"""

"""print(student["name"])
print(student.get("name")) # Both method gives same answers but in first method if the name does not exist in the dict it gives error and in .get method it give none value."""

# .update -->
# inserts a specified items to the dictionary (a new dictionary or new key : value pairs)

student.update({"City" : "Indore"})
print(student)
print()

new_dict = {
    "State" : "M.P",
    "Country" : "India",
    "name" : "Kushagra" # If we try to add a key that already exist in the old dict it simply overwrite the old value.
}
student.update(new_dict)
print(student)