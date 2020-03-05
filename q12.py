#Write a function that returns the sum of the first n numbers of the
#Fibonacci sequence (Wikipedia). The first 2 numbers in the sequence
#are 1,1, …

def fib(n): #General recursive Fibonacci program
    if(n<0):
        print("The number entered cannot be negative")
    elif(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(3))