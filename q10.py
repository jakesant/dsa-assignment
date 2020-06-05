#Write a recursive function that finds the largest number in a given list of integers.

numlist = [3,4,15,13,7,6,38,21]

def large(arr, size):
    if(size == 1):
        return arr[0] #Base case
    else:
        prev_num = large(arr, size-1)
        current_num = arr[size-1]
        if(prev_num > current_num):
            return prev_num
        else:
            return current_num

print("The largest number in the list is", large(numlist, len(numlist)))