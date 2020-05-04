#Take the two sorted arrays A and B from the question above and merge
#into a new array C. You must do this in linear time. Note that the size of C
#must be size of A plus size of B.

#Python has arrays but they have to be imported

import array as arr #We import the array module and can designate it as arr as a shorthand
import random
import time #Used to examine time taken for function to fully execute

A = arr.array('I', [0]) * 256
B = arr.array('I', [0]) * 300
C = arr.array('I', [0])

def pop_arrays():

#https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/

    for x in range(len(A)):
        A[x] = random.randint(0, 1024)

    for x in range(len(B)):
        B[x] = random.randint(0, 1024) 

    print("Both arrays have now been populated")

def quicksort(array, first, last):
    """Sorts array using quicksort
    Arguments:
        array {int array} -- int array of size >= 256
        first {index} -- first element
        last {index} -- last element
    """

    if first < last:
        pivot = partition(array, first, last)
        quicksort(array, first, pivot - 1)
        quicksort(array, pivot + 1, last)
    #https://www.geeksforgeeks.org/python-program-for-quicksort/
    #https://github.com/gbrunofranco/PythonAlgorithms/blob/master/sort/quick_sort.py

    return array

def partition(array, first, last):
    pivot = array[last]
    i = first - 1
    for j in range(first, last):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[last] = array[last], array[i + 1]
    return i + 1

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

def merge_arrays(array1, array2, result):
    #https://youtu.be/xF3TU-QlhJQ
    start_time = time.perf_counter()
    #https://stackoverflow.com/questions/7237875/linear-merging-for-lists-in-python

    while len(array1) and len(array2):
        if array1[0] < array2[0]:
            result.append(array1.pop(0)) #Append doesn't work here because it would add the element add the end of C and the size was already defined
        else:
            result.append(array2.pop(0))

    result.extend(array1)
    result.extend(array2)

    end_time = time.perf_counter()
    print("Time taken is %0.7f seconds" % (end_time-start_time))

def merge2(array1, array2, result):
    start_time = time.perf_counter()
    i = 0
    j = 0
    k = 0

    while(i < len(array1) and j < len(array2)):
        if(array1[i] < array2[j]):
            result[k] = array1[i] #Array index out of range occurs because of C
            i += 1
            k += i
        else:
            result[k] = array2[j] #array happens here because I need to use append as well
            j += 1
            k += i

    if(i < len(array1)):
        #append remaining elements from array1 to the result
        result.append(array1[i:])
    elif(j < len(array2)):
        result.append(array2[j:])

    end_time = time.perf_counter()
    print("Time taken is %0.7f seconds" % (end_time-start_time))

pop_arrays()
shellshort(A)
quicksort(B,0,len(B)-1)
#merge_arrays(A, B, C)
test1 = arr.array('I', [1, 3, 5, 7, 9])
test2 = arr.array('I', [2, 4, 8, 10, 11, 12, 16])
merge2(test1,test2,C)