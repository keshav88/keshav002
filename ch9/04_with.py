# using "with" we dont have to clase the file
with open("another.txt","r") as f:
    a=f.read()
with open("another.txt","w") as f:
    a=f.write("Me")


