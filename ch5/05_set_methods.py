#creating an empty set
b = set()
print(type(b))

#adding values to empty set
b.add(3)
b.add(2)
b.add(2) #adding a value repeatedly does not change a set 

# #b.add([1,3,2,4,5,6]) #we cannot add list in set because list value can be change 
# #b.add{
#     1:2,
#     "keshav":"pagal hai"
#     } ##we cannot add dictionry in set because list value can be change 
b.add((1,3,2,4,5,7,9,7,8,5,3)) #but we can add truple because we cannot change truple values

# print(b)

# #length of set
# print(len(b)) #tells the length of set

# #removal of an item
# b.remove(2) #remove 2 from set b \
# # b.remove(15) #throws a error while trying to remove 15 (which is not present in set)
# print(b)

# print(b.pop()) #remove any random value from set 
# print(b)

# b.clear() #it remove all element from the set

# b= b.union({2,4,7,5,9,0,1})
# print(b)

b= b.intersection({2,5,1,8})
print(b)