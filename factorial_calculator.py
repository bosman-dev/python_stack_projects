"""factorial of a number calculator
# uisng While loop
#number = eval(input("enter a non-negative integer to take the factorial of: "))
#product = 1
#i = 0
#while i < number:
    #product = product * ( i + 1)
    #i = i + 1
#print("the factorial of ",number," is ", product)"""


# using the For loop

number = input("enter a non-negative integer to take the factorial of: ")
product = 1
for i in range(int(number)):
    product = product * ( i + 1)
print("the factorial of ",number," is ", product)

# factorial function 
"""def factorial(n):
    f = 1
    while (n > 0):
        f = f * n
        n = n - 1
    return f
#print(factorial(6))

def factorial(n):
     if n == 0:
         return 1
     else:
         return n * factorial(n-1)
#print(factorial(6))"""
