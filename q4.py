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
    
    """while (i < len(arr)):
        for j in range(0, len(arr) - 1):
            combinations.append([arr[i], arr[j], (arr[i] * arr[j])])
        i += 1
    """
    while (i < len(arr)):
        temp_num = arr[i]
        for j in range(0, len(arr) - 1): #might have to remove the -1
            combinations.append([temp_num, arr[j], (temp_num * arr[j])])
        i += 1

    print("Combinations are", combinations)
    size = len(combinations)

    while(i < len(combinations)):
        temp_num = combinations[i] #loops one sublist at a time
        for j in range(0, len(combinations) - 1):
            temp_comb = combinations[j]
            if(temp_num[2] == temp_comb[2]) and (temp_num[0] != (temp_comb[0])) and (temp_num[0] != (temp_comb[1])):
                if(temp_num[1] != (temp_comb[0])) and (temp_num[1] != (temp_comb[1])):
                    if(temp_num[0] != temp_num[1] and temp_comb[0] != temp_comb[1]):
                        #Compares the element of the product
                        print(temp_num[0], "x", temp_num[1], "=", temp_comb[0], "x", temp_comb[1])
        i += 1

    print("Combination is of size", size)
#numlist = [3, 4, 6, 12, 1, 2, 5, 9, 10, 8, 14]
tupac = [2, 4, 32, 16, 1]
find_pairs(tupac)