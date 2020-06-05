#Write a program that, given a list of integers, finds all 2-pairs of integers that have the same product.
#A 2-pair is 2 distinct pairs of integers ((a,b),(c,d)) where a X b = c X d and a ≠ b ≠ c ≠ d.
#The range of integers in the list should be from 1 to 1024.

import random #used to populate array

def pop_array(array): #Same function in q1 and q2

    for i in range(len(array)):
        array[i] = random.randint(0, 1024)

def find_pairs(array, size):

    for a in range(size):
        for b in range(size):
            for c in range(size):
                for d in range(size):
                        if(array[a] == array[c] or array[b] == array[d] or array[a] == array[d] or array[b] == array[c]):
                            break
                        elif((array[a] * array[b]) == (array[c] * array[d])):
                            print(array[a], "x", array[b], "=", array[c], "x", array[d])

test_array = [0] * 30
pop_array(test_array)
print(test_array)
find_pairs(test_array, len(test_array))