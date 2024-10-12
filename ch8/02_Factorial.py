#n! = 1*2*3*4*......(n-1)*n
#n! = {1*2*3*4*.....(n-1)}*n
#n! = n*(n-1)!

# def factorial_iter(n):
#     product = 1
#     for i in range (n):
#         product=product*(i+1)
#     return product




#Recursion
def factorial_recursion(n):
    if n==1 or n==0 :
        return 1
    return n*factorial_recursion(n-1)

f=factorial_recursion(0)
print(f)
