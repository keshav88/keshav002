# #question 1 find greatest of 4 number
# num1=int(input("Enter number 1: "))
# num2=int(input("Enter number 2: "))
# num3=int(input("Enter number 3: "))
# num4=int(input("Enter number 4: "))

# if(num1>num2):
#     if(num3>num4):
#         if(num1>num3):
#             print(num1,"is the greatest number of all")
#         elif(num1<num3):
#             print(num3,"is the greatest number of all")
#     elif(num3<num4):
#         if(num1>num4):
#             print(num1,"is the greatest number of all")
#         elif(num1<num4):
#             print(num4,"is the greatest number of all")
# else:
#     if(num3>num4):
#         if(num2>num3):
#             print(num2,"is the greatest number of all")
#         elif(num2<num3):
#             print(num3,"is the greatest number of all")
#     elif(num3<num4):
#         if(num2>num4):
#             print(num1,"is the greatest number of all")
#         elif(num2<num4):
#             print(num4,"is the greatest number of all")

# #question2 check if student is pass or fail
# sub1=int(input("Enter the vale of math: "))
# sub2=int(input("Enter the vale of english: "))
# sub3=int(input("Enter the vale of hindi: "))
# sum=(sub1+sub2+sub3)/3
# if(sub1<33 or sub2<33 or sub3<33):
#     print("Fail")
# elif(sum<40):
#     print("Fail")
# else:
#     print("Congetulations! You passed the exams")

# #question3 if the comment is a spam or not
# sent=input("Enter your sentence\n")
# if("make a lot of money" in sent):
#     spam = True
# elif("buy now" in sent):
#     spam = True
# elif("subscribe this" in sent):
#     spam=True
# elif("click this" in sent):
#     spam= True
# else:
#     spam=False

# if(spam):
#     print("Their is a spam comment ")
# else:
#     print("Their is no spam comment.")

# #question4 username is less than 10 characters or not
# un=input("Enter your Username\n")
# un1=len(un)
# if(un<10):
#     print("The username has less than 10 characters")
# else:
#     print("The username has more than 10 characters")

# #question5 given name is persent in list or not
# name1=input("Enter your name: ")
# l1=["Keshav","Madhav","Upanshu","krish","divya","garima","mahak"]
# if(name1 in l1):
#     print("Your name is present.")
# else:
#     print("Your name is not in the list.") 
