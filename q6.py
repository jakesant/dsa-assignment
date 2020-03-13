#Write a Boolean function that checks if a number is prime. Also implement the Sieve of Eratosthenes
#algorithm. Explain any optimizations made.

#PSEUDO-CODE:
#A number is prime if is only divisible by itself

#https://www.geeksforgeeks.org/bool-in-python/

def prime(n):
    if (n % 2 != 0) and (n % 3 != 0) and (n % 5 != 0):
        print("Das is true")
        return True
    elif n == 1:
        print("Das is false")
        return False        
    elif n == 2:
        print("Das is true")
        return True
    elif n == 3:
        print("Das is true")
        return True
    elif n == 5:
        print("Das is true")
        return True        
    else:
        print("Das is false")
        return False

prime(1)