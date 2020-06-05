#Write a function that returns the sum of the first n numbers of the
#Fibonacci sequence. The first 2 numbers in the sequence
#are 1,1, …

def sum_fib(nterms):
    x = nterms
    sum = 0

    while nterms != 0:
        sum += fib(nterms)
        nterms -= 1

    print("The sum of the first", x, "values is", sum)

def fib(n): #Recursive Fibonacci program
    if(n<0):
        print("The number entered cannot be negtive")
    elif(n==1):
        return 1
    elif(n==2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

sum_fib(5)