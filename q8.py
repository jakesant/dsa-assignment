#Write a program that finds an approximation to the square root of a given number n using
#an iterative numerical method such as the Newton-Raphson Method.

#Newton-Raphson Method works by
#Formula --- x sub(n+1) = x sub n - f(x sub n)/f'(x sub n) -- sub means subscript

def guess_root(n):
    result = 0

    if n == 0:
        result = 0
    elif n < 0:
        print("Error. The number entered is negative")
        pass
    else:
        guess = n/2
        
        for i in range(20):
            result = (guess + n/guess)/2
            guess = result
            
    return result

print("%0.12f" %(guess_root(300)))