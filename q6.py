#Write a Boolean function that checks if a number is prime. Also implement the Sieve of Eratosthenes
#algorithm. Explain any optimizations made.

#PSEUDO-CODE:
#A number is prime if is only divisible by itself

#https://www.geeksforgeeks.org/bool-in-python/

def prime(n):
    if (n % 2 != 0) and (n % 3 != 0) and (n % 5 != 0):
        return True
    elif n == 1:
        return False        
    elif n == 2:
        return True
    elif n == 3:
        return True
    elif n == 5:
        return True        
    else:
        return False

print(prime(1))