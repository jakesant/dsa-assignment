#Write a Boolean function that checks if a number is prime. Also implement the Sieve of Eratosthenes
#algorithm. Explain any optimizations made.

#PSEUDO-CODE:
#A number is prime if is only divisible by itself

#https://www.geeksforgeeks.org/bool-in-python/

numlist = list(range(2, 37)) #Creates a list with all values from 2 to 36 - last number is not inclusive

def prime(n):
    if (n % 2 != 0) and (n % 3 != 0) and (n % 5 != 0):
        return True
    elif n == 1: #Necessary as 1 is not a prime number
        return False        
    elif n == 2:
        return True
    elif n == 3:
        return True
    elif n == 5:
        return True        
    #The 3 conditions above are required as they act as base cases
    else:
        return False


def sieve(n):

    """Description:
    Create a list of consecutive numbers starting from 2 to n
    let prime variable = 2 (first prime number)
    Starting from p2, count up in increments of p and mark
    each of these numbers greater than or equal to p2 itself in the list.
    These numbers will be p(p+1), p(p+2), p(p+3), etc.
    Find the first number greater than p in the list that is not marked.
    If there was no such number, stop. Otherwise, let p now equal this number
    (which is the next prime), and repeat from step 3
    """

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

    print("The prime numbers smaller than",n,"are:")
    print(primelist)
#print(prime(1)) #Test case for checking prime number

sieve(36)