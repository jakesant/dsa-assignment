#Write a Boolean function that checks if a number is prime. Also implement the Sieve of Eratosthenes
#algorithm. Explain any optimizations made.

import time

def prime(n):
    test_start = time.perf_counter()
    pol = False

    if (n % 2 != 0) and (n % 3 != 0) and (n % 5 != 0):
        pol = True
    elif n == 1: #Necessary as 1 is not a prime number
        pol = False        
    elif n == 2:
        pol = True
    elif n == 3:
        pol = True
    elif n == 5:
        pol = True        
    #The 3 conditions above are required as they act as base cases
    else:
        pol = False
    test_end = time.perf_counter()
    if(pol is True):
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")

    print("The time taken for the algorithm to run was %.8f seconds" % (test_end - test_start))

def sieve(n):
    test_start = time.perf_counter() #Gets current time; used for testing speed of algorithm
    sievelist = [True for i in range(n+1)] #Creates a list with the values of True going from 0 to n+1
    primelist = [] #Initiates list which will store values of prime numbers
    p = 2

    while((p * p) <= n):
        if(sievelist[p] == True): #If number we have set as P is prime
            for i in range(p*p, n+1, p):
                sievelist[i] = False
        p=p+1

    for p in range(2, n):
        if sievelist[p]:
            primelist.append(p) #Adds the prime number we have found to the list

    test_end = time.perf_counter()
    print("The prime numbers smaller than",n,"are:")
    print(primelist)
    print("The time taken for the algorithm to run was %.8f seconds" % (test_end - test_start)) #Gives time taken for Sieve algorithm to run to 5 significant digits after decimal


prime(36)
sieve(36)