# #Q1 Table of a given number using for loop 
# a=int(input("Enter a number for table: "))
# for i in range(1,11):
#     print(a*i)


# #Q2 Greet all the people in the list
# l1=["Harry","Saham","Sachin","Rahul",]

# for name in l1:
#     if name.startswith("S"):
#         print("Thank you for coming here " + name)


# #Q3 Attemt Q1 with while loop
# a=int(input("Enter a number for table: "))
# i=1
# while i<=10:
#     print(i*a)
#     i=i+1


# #Q4 Given number is prime or not
# num=int(input("Enter your number: "))
# for i in range (2,num):
#     if num%i==0:
#         print("The given number is not a prime number")
#         break
# else:
#     print("The given number is prime")
# if num==1:
#     print("The given number is prime")



# #Q5 The sum of first n natural numbers 
# n = int(input("Enter the nth number: "))
# a=0
# for i in range (1,n+1):
#     a=a+i
# print(a)


# #Q6 Find the factorial of any number
# l=int(input("Enter a number: "))
# fac=1
# for i in range(1,l+1):
#     if l==1:
#         fac = 1
#         break
#     fac=fac*i
# print(fac)




#07 star pattern

# for r in range(1,4):
#     print("*"*r)


# n=3
# for r in range (3):
#     print(" "*(n-r-1),end="")
#     print("*"*(1+(2*r)),end="")
#     print(" "*(n-r-1))


# for r in range (1,4):
#     for j in range (1,4):
#         if r==2 and j==2:
#             print(" ",end="")
#             pass
#         else :
#             print("*",end="")
#     print("\n",end="")    