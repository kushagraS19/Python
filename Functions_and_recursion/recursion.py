# Recursion happens when a function call itself repeatedly.
# These are similar to loop.
# All the things done by loops can also be done by recursion.
# Loops and recursion are interconnected.

"""def show(n): # Recursive function 
    if (n==0):
        return 
    print(n)
    show(n-1)
    print("END")

show(5)"""

#________________________________________________________________________________________

# Factorial of n by recursion -- > 

def fact(n):
    if(n == 0 or n == 1):
        return 1 
    else :
        return n * fact(n-1)
    
x = int(input("Enter a number : "))
print(fact(x))    