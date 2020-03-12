#Write a function that returns the sum of the first n numbers of the
#Fibonacci sequence (Wikipedia). The first 2 numbers in the sequence
#are 1,1, …


#https://www.geeksforgeeks.org/sum-fibonacci-numbers/

def sumFib(nterms):

    x = nterms
    sum = 0

    while nterms != 0:
        sum += fib(nterms)
        nterms -= 1

    print("The sum of the first", x, "values is", sum)

def fib(n): #General recursive Fibonacci program
    if(n<0):
        print("The number entered cannot be negative")
    elif(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

sumFib(5)