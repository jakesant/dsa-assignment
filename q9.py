#Write a program that, given an array of integers, finds all integers in the array that are repeated more than once.
#Try to find the fastest and most memory-efficient way of doing this.

import time

numlist = [3, 3, 4, 9, 2, 13, 13, 5, 1, 2, 7, 2]

def hash_find_dups(array, size):
    starttime = time.time()
    hashtable = [0] * 100

    for i in range(0, size): 
        hashtable[array[i]] += 1

    for i in range(0, size): 
        if (hashtable[array[i]] > 1): 
            print(array[i], end = " ")
            hashtable[array[i]] = 0
    
    endtime = time.time()

    finaltime = endtime - starttime

    print("Time taken is %2.5f seconds" %(finaltime))

hash_find_dups(numlist, len(numlist))