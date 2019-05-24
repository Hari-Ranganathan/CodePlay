print("Text editor")
filename = input("please input the filename: ")
file_contents = ""
try:
    with open(filename,'r') as f:
        file_contents = f.read()
except Exception as e:
    print(e)
print(file_contents)
append = input()
with open(filename,'w') as f:
    f.write(file_contents +"\n"+append)
print(filename + " written successfully")