#Write a function that computes cosine or sine by taking the first n terms of the appropriate series expansion

#To evaluate the value of sin and cos, we can make use of MacLaurin's Theorem
#f(x) = f(0) + f'(0)x+ f''(0)/2! x^2 + f'''0/3! x^3 ...

def cos(n):
    result = 0.0

    for i in range(31): #Performs series for up to 31 terms to give a more accurate result
        dividend = ((-1)**i) * (n**(2*i))
        divisor = fact(2*i)
        result += dividend/divisor

    return result

def sin(n):
    result = 0.0

    for i in range(31): #Performs series for up to 31 terms to give a more accurate result
        dividend = ((-1)**i) * (n**((2*i)+1))
        divisor = fact((2*i)+1)
        result += dividend/divisor

    return result

def fact(n):
    if (n == 0):
        return 1.0
    else:
        return n * fact(n-1)

print("%0.12f" %sin(2.68))
print("%0.12f" %sin(20))
print("%0.12f" %sin(90))
print("%0.12f" %cos(2.68))
print("%0.12f" %cos(20))
print("%0.12f" %cos(90))
