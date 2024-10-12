# Use to read all elements of the file without open it
# f=open("sample.txt","r")
f=open("sample.txt") #---> aagr kuch aage kuch bhi nahi likhnge toh woh aapne aap read kar lega 
# a=f.read()  #----> this read all the things in the file
# a= f.read(5) #----> this read oly read the given number of character
a= f.readline() #-----> this only read the first line of the file
print(a)
a= f.readline() #---> if we use it again this read the second line of file and if use it again the this read third line and so on
print(a)
f.close



