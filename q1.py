#Create two integer arrays A and B. The two arrays must contain at least 256 elements but
#must be of unequal size. Populate both arrays with randomly generated integers between
#0 and 1024. Sort array A using Shell Sort and array B using Quick Sort

#Python has arrays but they have to be imported

import array as arr #We import the array module and can designate it as arr as a shorthand
import random

#Initialisation of empty arrays
A = arr.array('I', [0]) * 256
B = arr.array('I', [0]) * 300

def pop_array(array):

    for x in range(len(array)):
        array[x] = random.randint(0, 1024)

    print("Array has now been randomly populated")

def quicksort(array, first_element, last_element):

    if first_element < last_element:
        pivot = partition(array, first_element, last_element)
        quicksort(array, first_element, pivot - 1)
        quicksort(array, pivot + 1, last_element)

    return array

def partition(array, first_element, last_element):

    pivot = array[last_element]
    i = first_element - 1
    for j in range(first_element, last_element):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[last_element] = array[last_element], array[i + 1]
    return i + 1

def shellsort(array):

    n = len(array)
    gap = len(array)//2

    while gap > 0: 
  
        for i in range(gap, n): 
            temp = array[i] 
  
            j = i 

            while  j >= gap and array[j-gap] >temp: 
                array[j] = array[j-gap] 
                j -= gap 

            array[j] = temp 
        gap //= 2

    return array

testl = arr.array('I', [0]) * 10
pop_array(testl)
print(testl)
shellsort(testl)
print(testl)

test2 = arr.array('I', [0]) * 20
pop_array(test2)
print(test2)
quicksort(test2, 0, len(test2) - 1)
print(test2)

pop_array(A)
pop_array(B)
shellsort(A)
quicksort(B, len(B) - 1)
print(A)
print(B)