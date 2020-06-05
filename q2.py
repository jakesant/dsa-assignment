#Take the two sorted arrays A and B from the question above and merge
#into a new array C. You must do this in linear time. Note that the size of C
#must be size of A plus size of B.

#Python has arrays but they have to be imported

import array as arr #We import the array module and can designate it as arr as a shorthand
import random

A = arr.array('I', [0]) * 256
B = arr.array('I', [0]) * 300
C = arr.array('I', [0])

def pop_array(array):

    for x in range(len(array)):
        array[x] = random.randint(0, 1024)

    print("Array has now been randomly populated")

def quicksort(array, first_index, last_index):

    if first_index < last_index:
        pivot = partition(array, first_index, last_index)
        quicksort(array, first_index, pivot - 1)
        quicksort(array, pivot + 1, last_index)

    return array

def partition(array, first_index, last_index):
    pivot = array[last_index]
    i = first_index - 1
    for j in range(first_index, last_index):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[last_index] = array[last_index], array[i + 1]
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

def merge_arrays(array1, array2, result):
    while len(array1) and len(array2):
        if array1[0] < array2[0]:
            result.append(array1.pop(0))
        else:
            result.append(array2.pop(0))

    result.extend(array1)
    result.extend(array2)


pop_array(A)
pop_array(B)
shellshort(A)
quicksort(B,0,len(B)-1)
merge_arrays(A, B, C)

test1 = arr.array('I', [1, 3, 5, 7, 9])
test2 = arr.array('I', [2, 4, 8, 10, 11, 12, 16])
test_result = arr.array('I', [0])
merge_arrays(test1,test2,test_result)
print(test_result)
print(len(test_result))