# #Q1 find the greatest of all three
# def greatest_3(a,b,c):
#     if (a>b and a>c):
#         return a
#     elif (b>a and b>c):
#         return b
#     elif (c>a and c>b):
#         return c
    

# g=greatest_3(55,63,70)
# print(g)



# #Q2 Convert celsius to fahrenheit
# #F=C*(9/5)+32
# #C=(F-32)(5/9)

# def celsius_fahrenheit(c):
#     f=c*(9/5)+32
#     return f 

# f= celsius_fahrenheit(30)
# print(f)


# #Q3 prevent print() to print a new line
# print("How",end=" ")
# print("are" , end= " ")
# print("you", end="")


# #Q4 the sum of first n natural numbers
# def sum_nth(n):
#     if n==0 :
#         return 0
#     return n+ sum_nth(n-1)

# s = sum_nth(5)
# print(s)


# # Q5 print 
# # ***
# # **
# # *
# for i in range (1,4):
#     print("*"*(4-i))


# #Q7 remove some given words from list and strip it at the same time 
# def str_removeandsplit(string , word):
#     newstr= string.replace(word,"")
#     return newstr.split()

# this = "harry is a good boy"
# n = str_removeandsplit(this,"harry")
# print(n)
    

  