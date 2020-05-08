#Write a program that, given a list of integers, finds all 2-pairs of integers that have the same product.
#A 2-pair is 2 distinct pairs of integers ((a,b),(c,d)) where a X b = c X d and a ≠ b ≠ c ≠ d.
#The range of integers in the list should be from 1 to 1024.

def pairs(arr):

    for i in range(len(arr)):
        print("Niggatest")
"""list = [integers]

pairs(list):

for i in range(len(list)):
    a = i, b = i+1, c = i+2, d = i+3
    if(a * b) == (c * d)
"""

def find_pairs(arr):
    """ take array [a,b,c,d] - unqiue integers
    compare integer a with a (itself), b and c
    then compare integer b with a, b(itself), c, d
    """

    pair_list = []
    combinations = []

    i = 0
    j = 0
    """for i in range(0, len(arr)):
        #Compare each integer to eachother
        for j in range(0, len(arr)):
            pair_list.append((arr[i], arr[j]))
            product = arr[i] * arr[j]
            combinations.append(product)
        """
    while (i < len(arr)):
        for j in range(0, len(arr) - 1):
            combinations.append([arr[i], arr[j], (arr[i] * arr[j])])
        i += 1
    
    print("Combinations are", combinations)
numlist = [3, 4, 6, 12, 1, 2, 5, 9, 10, 8, 14]
find_pairs(numlist)