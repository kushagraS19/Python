import random
import string

charVal = string.ascii_letters + string.digits + string.punctuation
pass_len = 5

"""password = ""

for i in range(pass_len):
    pass_val = random.choice(charVal)
    password += pass_val

print("Password :",password) """   

# By list comprehension

li = "".join([random.choice(charVal) for i in range(pass_len)])
print(li)