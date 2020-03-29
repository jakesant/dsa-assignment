#Write a program that, given an array of integers, finds all integers in the array that are repeated more than once.
#Try to find the fastest and most memory-efficient way of doing this.

import time

numlist = [3, 3, 4, 9, 2, 13, 13, 5, 1, 2, 7, 2]

#First try with sorting
def findDups():
    print("Hey")

#Now try with hashing
def hash_findDups(array, n):
    starttime = time.time()

    mp = [0] * 100

    for i in range(0, n): 
        mp[array[i]] += 1


    for i in range(0, n): 
        if (mp[array[i]] > 1): 
            print(array[i], end = " ") 
                
            # This is tricky, this  
            # is done to make sure  
            # that the current element  
            # is not printed again 
            mp[array[i]] = 0
    
    endtime = time.time()

    finaltime = endtime - starttime

    print("Time taken is %2.5f seconds" %(finaltime))

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

hash_findDups(numlist, len(numlist))