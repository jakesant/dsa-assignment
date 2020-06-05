#Write a Boolean function that checks if a number is prime. Also implement the Sieve of Eratosthenes
#algorithm. Explain any optimizations made.

def prime(n):
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
        
    if(pol is True):
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")

def sieve(n):
    sievelist = [True for i in range(n+1)] #Creates a list with the values of True going from 0 to n+1
    primelist = [] #Initiates list which will store values of prime numbers
    p = 2

    while((p * p) <= n):
        for i in range(p*p, n+1, p):
            sievelist[i] = False
        p=p+1

    for p in range(2, n):
        if sievelist[p]:
            primelist.append(p) #Adds the prime number we have found to the list

    print("The prime numbers smaller than",n,"are:")
    print(primelist)

prime(36)
prime(97)
sieve(36)