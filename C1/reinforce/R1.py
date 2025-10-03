# Write a short python function, is multiple(n, m), that takes two integer values and returns True if n is a multiple of m, that is, n = mi, for some integer i, and false otherwise

""" First of all, we need to create two inputs, one called n, and onde called m, that will receive our 2 values necessaries. 

n = int(input()), this means that all the content the user types, will be converted to a integer value, and that this value will be armazened in the N variable

def is_multiple(n, m) -  This is a function, that will receive two inputs, exactly like a mathematical function from  R^2 to R^1.

if((n%m==0) - This if statement are declaring the following: if i divide n by m and the rest will be zero, then we have an even number, thus return True, else, return False.

By the end, we call the function with is_multiple(n, m)
"""

n = int(input())
m = int(input())

def is_multiple(n, m):
    if ((n%m==0)):
        return print("True")
    else:
        return print("False")
   

is_multiple(n, m)
