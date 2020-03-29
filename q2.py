#Take the two sorted arrays A and B from the question above and merge
#into a new array C. You must do this in linear time. Note that the size of C
#must be size of A plus size of B.

#Python has arrays but they have to be imported

import array as arr #We import the array module and can designate it as arr as a shorthand
import random
import time #Used to examine time taken for function to fully execute

A = arr.array('I', [0]) * 256
B = arr.array('I', [0]) * 300
C = arr.array('I')

def pop_arrays():

#https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/

    for x in range(len(A)):
        A[x] = random.randint(0, 1024)

    for x in range(len(B)):
        B[x] = random.randint(0, 1024) 

    print("Both arrays have now been populated")

def merge_arrays(array1, array2, result):
    start_time = time.time()
    #https://stackoverflow.com/questions/7237875/linear-merging-for-lists-in-python

    while len(array1) and len(array2):
        if array1[0] < array2[0]:
            result.append(array1.pop(0)) #Append doesn't work here because it would add the element add the end of C and the size was already defined
        else:
            result.append(array2.pop(0))

    result.extend(array1)
    result.extend(array2)

    end_time = time.time()
    
    final_time = end_time-start_time
    print("Time taken is %0.7f seconds" % float(final_time))

    print(result)


def shellshort(array):

    n = len(array)
    gap = len(array)//2

    while gap > 0: 
  
        for i in range(gap, n): 
  
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i 
            temp = array[i] 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while  j >= gap and array[j-gap] >temp: 
                array[j] = array[j-gap] 
                j -= gap 
  
            # put temp (the original a[i]) in its correct location 
            array[j] = temp 
        gap //= 2

    print(array)

pop_arrays()
shellshort(A)
shellshort(B)
merge_arrays(A, B, C)