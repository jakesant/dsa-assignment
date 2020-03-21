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


def sieve(arr):
    for x in arr:
        if (arr[x] == 2) or (arr[x] == 3) or (arr[x] == 5):
            arr[x] = 0

print(prime(1))