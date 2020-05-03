#Attempting question 1 of the DSA assignment

#Create two integer arrays A and B. The two arrays must contain at least 256 elements but
#must be of unequal size. Populate both arrays with randomly generated integers between
#0 and 1024. Sort array A using Shell Sort and array B using Quick Sort

#Python has arrays but they have to be imported

import array as arr #We import the array module and can designate it as arr as a shorthand
import random

#Empty Arrays
A = arr.array('I', [0]) * 256
B = arr.array('I', [0]) * 300

x = 0
#Implement random seed


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
            i += 1 #Error out of index occurs here
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

pop_arrays()
print(A)
shellshort(A)
print(A)
print(B)
quicksort(B,0,len(B)-1)
print(B)