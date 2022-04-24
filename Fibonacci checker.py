import math as m
 
# A function that returns true if the number is a perfect square, else
# returns false
def isPerfectSquare(num):
    s =int(m.sqrt(num))  # finding the square root of num
    return s*s == num
 
# A function that returns true if the number is fibonacci, otherwise
# returns false
def isFibonacciNumber(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
 
# The first 10 fibonacci numbers are:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# You can use the above numbers to countercheck the function

# Testing  isFibonacci()
n = int(input("Please enter the suspect number you want to check : "))
if(isFibonacciNumber(n) == True): 
    print(n , "is found guilty to being a fibonacci number")   
else: 
    print(n  ," is not a fibonacci number")
    
