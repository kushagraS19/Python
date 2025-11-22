# Create a new file "practice.txt" using pyhton. Add data in it : 

""" f.write("Hi everyone.\nWe are learning File I/O. \nUsing java. \nI like programming.")"""

#________________________________________________________________________________________________________-

#

"""with open("D:\Kushagra\Python\Practice_sets\practice.txt","r") as f:
    data = f.read()

new_data = data.replace("java", "Python")
print(new_data)    

with open("D:\Kushagra\Python\Practice_sets\practice.txt","w") as f:
    f.write(new_data)"""

#_________________________________________________________________________________________________________

# WAF to chech if the word learning is existing in the or not -->

"""word = "learning"
with open("D:\Kushagra\Python\Practice_sets\practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else :
        print("Not found")"""

#_______________________________________________________________________________________________________________-->

# WAF to find in which line of the file does the word "learning" occur first. Print -1 if the word does not exist.

"""def check_for_word():
    word = "learning"
    with open("D:\Kushagra\Python\Practice_sets\practice.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else :
            print("Not found")

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("D:\Kushagra\Python\Practice_sets\practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(word,"found at line",line_no)
            line_no += 1    

with open("D:\Kushagra\Python\Practice_sets\practice.txt","a") as f:
    f.write("\nlearning goes on..")

check_for_line()"""

#_________________________________________________________________________________________________________________

# From a file containing numbers separated by a comma, print the count of even numbers.

with open("D:\Kushagra\Python\Practice_sets\even_numbers.txt","r") as f:
    data = f.read()
    print(data)

"""num = ""
for i in range(len(data)):
    if(data[i] == ','):
        print(int(num))
        num = ""
    else:
        num += data[i]"""

count = 0

nums = data.split(",")
for val in nums:
    if(int(val) % 2 == 0):
        count += 1

print(count)        