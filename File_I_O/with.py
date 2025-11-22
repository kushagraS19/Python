with open("D:\Kushagra\Python\File_I_O\sample.txt","r") as f:
    data = f.read()
    print(data)

with open("D:\Kushagra\Python\File_I_O\sample.txt","w") as f:
    f.write("New Data")