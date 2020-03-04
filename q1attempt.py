#Attempting question 1 of the DSA assignment

#Create two integer arrays A and B. The two arrays must contain at least 256 elements but
#must be of unequal size. Populate both arrays with randomly generated integers between
#0 and 1024. Sort array A using Shell Sort and array B using Quick Sort

#Python has arrays but they have to be imported

import array as arr #We import the array module and can designate it as arr as a shorthand
import random

A = arr.array('I', [0]) * 10
B = arr.array('I', [0]) * 300
x = 0

def pop_arrays():
    """
    y = type(A)
    print(y)

    A.append(4) #Adds the number 4 to the end of the array (increases array size)
    print(A)
    """
#https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/

    for x in range(len(A)):
        print("Value is currently %d" % (A[x]))
        A[x] += x
        print("Value is now %d" % (A[x]))
        """
        A[x] = random.randint(0, 1024)
        test = random.randint(0,1024)
        x += 1
        print(A[x])"""

pop_arrays()